#!/usr/bin/env python3
"""
Scraper for Artificial Analysis Coding Agents page.

Extracts the Cache Hit Rate for ALL model-agent combinations from:
  https://artificialanalysis.ai/agents/coding-agents

The page's __next_f RSC payload contains the full dataset for all 23
model-agent combinations (even though the default UI only displays 16).
We parse the payload, locate every `cacheHitRate` field inside the
`mean` object of each combination, and average all valid values.

The resulting single global average is used by analyze.py as the
Cache Hit Rate in the per-request cost formula:

    cost = (CacheHitRate * CacheHitPrice * InputTokens)
         + ((1 - CacheHitRate) * CacheWritePrice * InputTokens)
         + (Speed * RealTime * OutputPrice)

Output: output/cache_hit_rate.json
  {
    "cache_hit_rate": 0.898608,
    "valid_count": 23,
    "total_count": 23,
    "combinations": [ {agent, model, cacheHitRate, ...}, ... ]
  }
"""

import json
import os
import sys

from playwright.sync_api import sync_playwright

URL = "https://artificialanalysis.ai/agents/coding-agents"
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "cache_hit_rate.json")

# JavaScript: parse every __next_f push() call with eval(), concatenate the
# unescaped fragments, then regex-extract every cacheHitRate value along
# with the surrounding agentName / displayLabel / id context.
EXTRACT_JS = r"""
(() => {
  const scripts = document.querySelectorAll('script');
  const fragments = [];
  for (let i = 0; i < scripts.length; i++) {
    const text = scripts[i].textContent || '';
    if (!text.includes('__next_f')) continue;
    const pushPattern = /self\.__next_f\.push\(\s*(\[.*?\])\s*\)\s*;?/gs;
    let m;
    while ((m = pushPattern.exec(text)) !== null) {
      try {
        const arr = eval(m[1]);
        if (arr && arr.length >= 2 && typeof arr[1] === 'string') {
          fragments.push(arr[1]);
        }
      } catch(e) { /* skip */ }
    }
  }
  const fullText = fragments.join('');

  // Each model-agent combination has a "mean" object with cacheHitRate.
  // We locate every cacheHitRate and walk backwards to find the enclosing
  // combination's id / agentName / displayLabel / hostModelSlug fields.
  const results = [];
  const pattern = /"cacheHitRate"\s*:\s*([0-9.eE+-]+)/g;
  let m;
  while ((m = pattern.exec(fullText)) !== null) {
    const value = parseFloat(m[1]);
    const idx = m.index;
    const before = fullText.substring(Math.max(0, idx - 3000), idx);
    const after = fullText.substring(idx, idx + 800);

    function findLast(pat, text) {
      const matches = [...text.matchAll(new RegExp(pat, 'g'))];
      return matches.length > 0 ? matches[matches.length - 1][1] : null;
    }
    function findFirst(pat, text) {
      const mm = new RegExp(pat).exec(text);
      return mm ? mm[1] : null;
    }

    const id           = findLast('"id"\\s*:\\s*"([^"]+)"', before);
    const agentName    = findLast('"agentName"\\s*:\\s*"([^"]+)"', before);
    const hostModelSlug= findLast('"hostModelSlug"\\s*:\\s*"([^"]+)"', before);
    const displayLabel = findLast('"displayLabel"\\s*:\\s*"([^"]+)"', before);
    // Also pull the sibling token-count fields that sit right next to cacheHitRate
    const inputTokens    = findFirst('"inputTokens"\\s*:\\s*([0-9.eE+-]+)', after);
    const cacheTokens    = findFirst('"cacheTokens"\\s*:\\s*([0-9.eE+-]+)', after);
    const cacheWriteTokens = findFirst('"cacheWriteTokens"\\s*:\\s*([0-9.eE+-]+)', after);
    const outputTokens   = findFirst('"outputTokens"\\s*:\\s*([0-9.eE+-]+)', after);
    const totalTokens    = findFirst('"totalTokens"\\s*:\\s*([0-9.eE+-]+)', after);

    results.push({
      id: id,
      agentName: agentName,
      hostModelSlug: hostModelSlug,
      displayLabel: displayLabel,
      cacheHitRate: value,
      inputTokens: inputTokens !== null ? parseFloat(inputTokens) : null,
      cacheTokens: cacheTokens !== null ? parseFloat(cacheTokens) : null,
      cacheWriteTokens: cacheWriteTokens !== null ? parseFloat(cacheWriteTokens) : null,
      outputTokens: outputTokens !== null ? parseFloat(outputTokens) : null,
      totalTokens: totalTokens !== null ? parseFloat(totalTokens) : null,
    });
  }
  return JSON.stringify({totalFragments: fragments.length, totalLength: fullText.length, results: results});
})()
"""


def scrape_cache_hit_rate():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        print(f"[1/3] Navigating to {URL} ...")
        page.goto(URL, wait_until="networkidle", timeout=90000)
        page.wait_for_timeout(5000)  # Wait for RSC stream to complete

        print("[2/3] Extracting cacheHitRate values from RSC payload ...")
        raw_json = page.evaluate(EXTRACT_JS)
        data = json.loads(raw_json)

        results = data["results"]
        print(f"  Parsed {data['totalFragments']} RSC fragments ({data['totalLength']} chars)")
        print(f"  Found {len(results)} cacheHitRate entries")

        # Filter to valid numeric values (positive, finite, not NaN)
        valid = [r for r in results
                 if r["cacheHitRate"] is not None
                 and isinstance(r["cacheHitRate"], float)
                 and r["cacheHitRate"] == r["cacheHitRate"]  # NaN check
                 and r["cacheHitRate"] > 0]
        invalid = [r for r in results if r not in valid]

        print(f"  Valid entries: {len(valid)} / {len(results)}")
        if invalid:
            print(f"  Skipped {len(invalid)} invalid entries:")
            for r in invalid:
                print(f"    {r.get('displayLabel') or r.get('agentName')}: cacheHitRate={r['cacheHitRate']}")

        if not valid:
            print("ERROR: No valid cacheHitRate values found.")
            browser.close()
            return None

        avg = sum(r["cacheHitRate"] for r in valid) / len(valid)
        print(f"  Average cacheHitRate: {avg:.6f}")
        print(f"  Range: {min(r['cacheHitRate'] for r in valid):.6f} - {max(r['cacheHitRate'] for r in valid):.6f}")

        print(f"[3/3] Saving to {OUTPUT_FILE} ...")
        output = {
            "metadata": {
                "source": URL,
                "description": (
                    "Average Cache Hit Rate across all model-agent combinations on the "
                    "Artificial Analysis Coding Agents benchmark. Used by analyze.py as "
                    "the global Cache Hit Rate in the per-request cost formula."
                ),
                "methodology": (
                    "All model-agent combinations' `mean.cacheHitRate` values are "
                    "extracted from the page's __next_f RSC payload. Valid (positive, "
                    "finite) values are averaged into a single global Cache Hit Rate "
                    "that is applied uniformly to every model in the leaderboard."
                ),
                "total_combinations": len(results),
                "valid_count": len(valid),
            },
            "cache_hit_rate": avg,
            "valid_count": len(valid),
            "total_count": len(results),
            "combinations": [
                {
                    "agent": r.get("agentName"),
                    "model_slug": r.get("hostModelSlug"),
                    "display_label": r.get("displayLabel"),
                    "cache_hit_rate": r["cacheHitRate"],
                    "input_tokens": r.get("inputTokens"),
                    "cache_tokens": r.get("cacheTokens"),
                    "cache_write_tokens": r.get("cacheWriteTokens"),
                    "output_tokens": r.get("outputTokens"),
                    "total_tokens": r.get("totalTokens"),
                }
                for r in sorted(valid, key=lambda x: x["cacheHitRate"])
            ],
        }
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(output, f, ensure_ascii=False, indent=2)

        browser.close()

    print(f"Done! cache_hit_rate = {avg:.6f} (from {len(valid)} combinations)")
    return avg


if __name__ == "__main__":
    try:
        avg = scrape_cache_hit_rate()
        if avg is None:
            sys.exit(1)
    except Exception as e:
        print(f"Scraping failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
