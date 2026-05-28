#!/usr/bin/env python3
"""
Scraper for Artificial Analysis LLM Leaderboard.
Expands Intelligence + Price + Speed + Latency + End-to-End Response Time
to capture all timing columns including Reasoning Time.

Column layout (after expanding ALL groups) — updated 2026-05-28:
  0:  Model (with lightbulb SVG for reasoning models)
  1:  Context Window
  2:  Creator
  3:  License (Features — new column)
  4-18: 15 Intelligence sub-metrics (original)
  19:  ITBench-AA (new 16th Intelligence metric)
  20: Blended USD/1M Tokens
  21: Input Price USD/1M Tokens
  22: Output Price USD/1M Tokens
  23: Median Tokens/s
  24-27: P5/P25/P75/P95 Tokens/s (Speed detail, ignored)
  28: Latency First Chunk (s) (TTFT)
  29: First Answer (s)
  30-33: P5/P25/P75/P95 First Chunk (s) (ignored)
  34: Total Response (s)
  35: Reasoning Time (s)
  36: Further Analysis (ignored)
"""

import json
import os
import sys

from playwright.sync_api import sync_playwright

URL = "https://artificialanalysis.ai/leaderboards/models"
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "raw_data.json")
MIN_MODELS_EXPECTED = 10

# 16 Intelligence sub-metrics (columns 4..19)
# ITBench-AA added 2026-05-28 between APEX-Agents-AA and MMMU_Pro
INTEL_METRICS = [
    "AA_Intelligence_Index",
    "AA_Omniscience_Index",
    "GDPval_AA",
    "Terminal_Bench_Hard",
    "Tau2_Bench",
    "AA_LCR",
    "AA_Omniscience_Accuracy",
    "AA_Omniscience_Non_Hallucination",
    "HLE",
    "GPQA_Diamond",
    "SciCode",
    "IFBench",
    "CritPt",
    "APEX_Agents_AA",
    "ITBench_AA",
    "MMMU_Pro",
]

# Key price + timing columns
# After full expansion, column indices are (updated 2026-05-28):
PRICE_SPEED_LATENCY = {
    "Blended_Price": 20,
    "Input_Price": 21,
    "Output_Price": 22,
    "Speed_TokensPerSec": 23,
    "Latency_First_Chunk_s": 28,
    "First_Answer_s": 29,
    "Total_Response_s": 34,
    "Reasoning_Time_s": 35,
}


def scrape_leaderboard():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        print(f"[1/6] Navigating to {URL} ...")
        page.goto(URL, wait_until="networkidle", timeout=60000)
        page.wait_for_timeout(5000)

        # Expand ALL column groups
        print("[2/6] Expanding all column groups ...")
        groups = ["Features", "Intelligence", "Price", "Speed", "Latency", "End-to-End Response Time"]
        for group in groups:
            btn = page.locator("th").filter(has=page.get_by_role("button", name=group)).locator("button").first
            btn.click()
            page.wait_for_timeout(1000)

        # Verify expansions
        print("[3/6] Verifying expansions ...")
        expected = {
            "Features": "3", "Intelligence": "16", "Price": "3",
            "Speed": "5", "Latency": "6", "End-to-End Response Time": "2",
        }
        for name, exp in expected.items():
            th = page.locator('th[colspan]', has_text=name).first
            cs = th.get_attribute("colspan")
            print(f"  {name} colspan = {cs} (expected {exp})")

        # Extract data via JS (including lightbulb detection for reasoning models)
        print("[4/6] Extracting table data ...")
        js_code = """
        (args) => {
            const intel = args.intelMetrics;
            const psl = args.priceSpeedLatency;
            const rows = document.querySelectorAll('tbody tr');
            const result = [];
            for (const row of rows) {
                const c = row.querySelectorAll('td');
                if (c.length < 36) continue;
                const d = {
                    Model: c[0].textContent.trim(),
                    Is_Reasoning: c[0].querySelector('svg.lucide-lightbulb') !== null,
                };
                // Intelligence metrics (columns 4..19)
                for (let i = 0; i < intel.length; i++)
                    d[intel[i]] = c[4 + i].textContent.trim();
                // Price/Speed/Latency columns (specific indices)
                for (const [key, idx] of Object.entries(psl))
                    d[key] = c[idx].textContent.trim();
                result.push(d);
            }
            return result;
        }
        """
        data = page.evaluate(js_code, {
            "intelMetrics": INTEL_METRICS,
            "priceSpeedLatency": PRICE_SPEED_LATENCY,
        })

        print(f"[5/6] Scraped {len(data)} models")
        reasoning_count = sum(1 for d in data if d.get("Is_Reasoning"))
        if data:
            s = data[0]
            print(f"  Sample: {s['Model']}, Reasoning={s['Is_Reasoning']}, "
                  f"Intel={s['AA_Intelligence_Index']}, "
                  f"Blended={s['Blended_Price']}, Speed={s['Speed_TokensPerSec']}, "
                  f"TTFT={s['Latency_First_Chunk_s']}, Total={s['Total_Response_s']}, "
                  f"ReasonT={s['Reasoning_Time_s']}")
        print(f"  Reasoning models: {reasoning_count}/{len(data)}")

        print(f"[6/6] Saving to {OUTPUT_FILE} ...")
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        browser.close()

    print(f"Done! {len(data)} models saved.")
    return data


if __name__ == "__main__":
    try:
        data = scrape_leaderboard()
        if len(data) < MIN_MODELS_EXPECTED:
            print(f"ERROR: Only {len(data)} models scraped.")
            sys.exit(1)
    except Exception as e:
        print(f"Scraping failed: {e}")
        sys.exit(1)
