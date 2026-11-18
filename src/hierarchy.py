#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Model Hierarchy Management & Monotonic Benchmark Scoring Engine
==============================================================
Implements:
1. Extraction & dynamic leave-one-out calibration across all 38 benchmarks.
2. Grouping models by vendor, tier (vertical rows), version (horizontal columns),
   and reasoning/thinking levels.
3. 2D CSV grid export & import for vendor model hierarchies (enabling easy human review & editing).
4. Strictly compliant constraint generation for:
   - Rule 1: Same version, higher tier >= lower tier.
   - Rule 2: Same tier, newer version >= older version.
   - Rule 3: Same base model, higher thinking level >= lower thinking level.
5. Latent ability debiasing & Dykstra isotonic projection on the constraint DAG
   to ensure maximal satisfaction of monotonic hierarchy conditions.
6. Interactive diff and validation utilities for reviewing user edits.
"""

import argparse
import csv
import json
import math
import os
import re
import sys
from collections import defaultdict
from typing import Dict, List, Optional, Set, Tuple

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
HIERARCHY_DIR = os.path.join(OUTPUT_DIR, "model_hierarchy")
RAW_DATA_FILE = os.path.join(OUTPUT_DIR, "raw_data.json")

# ══════════════════════════════════════════════════════════════════════
# 1. 38 Candidate Benchmark Metrics Catalog
# ══════════════════════════════════════════════════════════════════════

BENCHMARK_DEFS = {
    "intelligenceIndex": {
        "name": "AA Intelligence Index",
        "aliases": ["intelligenceIndex", "artificial-analysis-intelligence-index"],
        "domain": "core_reasoning",
    },
    "hle": {
        "name": "Humanity's Last Exam",
        "aliases": ["hle", "humanitys-last-exam"],
        "domain": "core_reasoning",
    },
    "hleDiamond": {
        "name": "HLE Diamond",
        "aliases": ["hleDiamond", "hle-diamond"],
        "domain": "core_reasoning",
    },
    "gpqa": {
        "name": "GPQA Diamond",
        "aliases": ["gpqa", "gpqa-diamond"],
        "domain": "core_reasoning",
    },
    "critpt": {
        "name": "CritPt Physics",
        "aliases": ["critpt"],
        "domain": "math_stem",
    },
    "critptV2Hard": {
        "name": "CritPt v2 Hard",
        "aliases": ["critptV2Hard", "critpt-v2-hard", "critpt-v2"],
        "domain": "math_stem",
    },
    "aime2025": {
        "name": "AIME 2025",
        "aliases": ["aime2025", "aime-2025"],
        "domain": "math_stem",
    },
    "scicode": {
        "name": "SciCode Coding",
        "aliases": ["scicode"],
        "domain": "coding",
    },
    "livecodebench": {
        "name": "LiveCodeBench",
        "aliases": ["livecodebench"],
        "domain": "coding",
    },
    "frontiercode": {
        "name": "FrontierCode 1.1",
        "aliases": ["frontiercode"],
        "domain": "coding",
    },
    "frontiercode20": {
        "name": "FrontierCode 2.0",
        "aliases": ["frontiercode20", "frontiercode-2-0"],
        "domain": "coding",
    },
    "terminalbenchHard": {
        "name": "Terminal-Bench Hard",
        "aliases": ["terminalbenchHard", "terminalbench-hard"],
        "domain": "agentic",
    },
    "terminalbenchV21": {
        "name": "Terminal-Bench 2.1",
        "aliases": ["terminalBench21", "terminalbenchV21", "terminalbench-2-1"],
        "domain": "agentic",
    },
    "terminalbenchV40": {
        "name": "Terminal-Bench 4.0",
        "aliases": ["terminalBench40", "terminalbenchV40", "terminalbench-4-0"],
        "domain": "agentic",
    },
    "terminalbenchScience": {
        "name": "Terminal-Bench Science",
        "aliases": ["terminalbenchScience", "terminal-bench-science"],
        "domain": "agentic",
    },
    "tau2": {
        "name": "τ²-Bench Telecom",
        "aliases": ["tau2", "tau2-bench"],
        "domain": "agentic",
    },
    "tauBanking": {
        "name": "τ³-Bench Banking",
        "aliases": ["tauBanking", "tau3-banking"],
        "domain": "agentic",
    },
    "automationbench": {
        "name": "AutomationBench-AA",
        "aliases": ["automationbench", "automationbench-aa"],
        "domain": "agentic",
    },
    "briefcase": {
        "name": "AA-Briefcase v1.1",
        "aliases": ["briefcase", "aa-briefcase"],
        "domain": "agentic",
    },
    "gdpvalNormalized": {
        "name": "GDPval-AA Normalized",
        "aliases": ["gdpvalNormalized", "gdpval-aa-normalized", "gdpval-aa"],
        "domain": "agentic",
    },
    "gdpPdf": {
        "name": "GDP.pdf",
        "aliases": ["gdpPdf", "gdp-pdf"],
        "domain": "long_context",
    },
    "lcr": {
        "name": "AA-LCR Long Context",
        "aliases": ["lcr", "artificial-analysis-long-context-reasoning"],
        "domain": "long_context",
    },
    "mlcr": {
        "name": "MLCR Medical Long Context",
        "aliases": ["mlcr", "mlcr-aa"],
        "domain": "long_context",
    },
    "mmmuPro": {
        "name": "MMMU-Pro",
        "aliases": ["mmmuPro", "mmmu-pro"],
        "domain": "multimodal",
    },
    "code2video": {
        "name": "Code2Video-AA",
        "aliases": ["code2video", "code2video-aa"],
        "domain": "multimodal",
    },
    "aa3d": {
        "name": "AA-3D",
        "aliases": ["aa3d", "aa-3d"],
        "domain": "multimodal",
    },
    "omniscience": {
        "name": "AA Omniscience Index",
        "aliases": ["omniscience", "aa-omniscience"],
        "domain": "factuality",
    },
    "omniscienceAccuracy": {
        "name": "AA-Omniscience Accuracy",
        "aliases": ["omniscienceAccuracy", "omniscience-accuracy"],
        "domain": "factuality",
    },
    "omniscienceNonHallucination": {
        "name": "AA-Omniscience Non-Hallucination",
        "aliases": ["omniscienceNonHallucination", "omniscience-non-hallucination"],
        "domain": "factuality",
    },
    "ifbench": {
        "name": "IFBench",
        "aliases": ["ifbench"],
        "domain": "factuality",
    },
    "analystAgent": {
        "name": "AA Analyst Agent",
        "aliases": ["analystAgent", "aa-analyst-agent"],
        "domain": "agentic",
    },
    "apexAgents": {
        "name": "APEX-Agents-AA",
        "aliases": ["apexAgents", "apex-agents-aa"],
        "domain": "agentic",
    },
    "enterpriseOps": {
        "name": "EnterpriseOps-Gym-AA",
        "aliases": ["enterpriseOps", "enterprise-ops-gym-aa"],
        "domain": "agentic",
    },
    "itbenchSre": {
        "name": "ITBench-SRE",
        "aliases": ["itbenchSre", "itbench-aa", "itbench-sre"],
        "domain": "agentic",
    },
    "harveyLab": {
        "name": "Harvey LAB-AA",
        "aliases": ["harveyLab", "harvey-lab-aa"],
        "domain": "agentic",
    },
    "healthbench": {
        "name": "HealthBench",
        "aliases": ["healthbench"],
        "domain": "agentic",
    },
    "healthbenchProfessional": {
        "name": "HealthBench Professional",
        "aliases": ["healthbenchProfessional", "healthbench-professional"],
        "domain": "agentic",
    },
    "vials": {
        "name": "VIALS-AA / MKA",
        "aliases": ["vials", "vials-aa", "mka"],
        "domain": "multimodal",
    },
}

THINKING_LEVELS = {
    "max": 6,
    "xhigh": 5,
    "high": 4,
    "reasoning": 4,
    "medium": 3,
    "low": 2,
    "minimal": 1,
    "non-reasoning": 0,
    "standard": 0,
}


# ══════════════════════════════════════════════════════════════════════
# 2. Model Name & Thinking Level Parser
# ══════════════════════════════════════════════════════════════════════

def parse_model_name(full_name: str) -> Tuple[str, str, int]:
    """Parse a full model name into (base_name, thinking_tag, thinking_level).

    Thinking level order:
      max (6) > xhigh (5) > high/reasoning (4) > medium (3) > low (2) > minimal (1) > non-reasoning/standard (0)
    """
    clean_name = full_name.strip()
    m = re.search(r'\(([^)]+)\)$', clean_name)
    th_tag = "standard"
    th_lvl = 0
    base_name = clean_name

    if m:
        content = m.group(1).lower()
        if "non-reasoning" in content:
            th_tag, th_lvl = "non-reasoning", 0
        elif "max" in content:
            th_tag, th_lvl = "max", 6
        elif "xhigh" in content:
            th_tag, th_lvl = "xhigh", 5
        elif "high" in content:
            th_tag, th_lvl = "high", 4
        elif "medium" in content:
            th_tag, th_lvl = "medium", 3
        elif "low" in content:
            th_tag, th_lvl = "low", 2
        elif "minimal" in content:
            th_tag, th_lvl = "minimal", 1
        elif "fallback" in content or content == "reasoning":
            th_tag, th_lvl = "reasoning", 4

        # Strip parenthetical suffix if it represents thinking info or fallback
        if th_lvl > 0 or th_tag == "non-reasoning" or "fallback" in content or content == "reasoning":
            base_name = clean_name[:m.start()].strip()
            if "daybreak blue" in content:
                base_name += " (Daybreak Blue)"

    return base_name, th_tag, th_lvl


MONTH_MAP = {
    "jan": 1, "january": 1,
    "feb": 2, "february": 2,
    "mar": 3, "march": 3,
    "apr": 4, "april": 4,
    "may": 5,
    "jun": 6, "june": 6,
    "jul": 7, "july": 7,
    "aug": 8, "august": 8,
    "sep": 9, "sept": 9, "september": 9,
    "oct": 10, "october": 10,
    "nov": 11, "november": 11,
    "dec": 12, "december": 12
}


def parse_date_snapshot(base_name: str, release_date: Optional[str] = None) -> Tuple[str, Optional[Tuple[int, int, int, int]], Optional[str]]:
    """Parse date snapshot metadata from a model base name and/or release date.

    Returns:
      (stem, date_tuple, display_str)
      date_tuple is (year, month, day, sub_version) for chronological sorting.
    """
    stem = base_name.strip()

    # 1. Parenthesized month and optional year, e.g. (May), (June 2026), (Feb 2026), (Dec)
    m = re.search(r'\((jan|feb|mar|apr|may|june?|july?|aug|sep|sept|september|oct|nov|dec)(?:\s+(\d{4}))?\)$', stem, re.I)
    if m:
        month = MONTH_MAP[m.group(1).lower()]
        year = int(m.group(2)) if m.group(2) else (int(release_date[:4]) if release_date and len(release_date) >= 4 else 2024)
        clean_stem = stem[:m.start()].strip()
        disp = m.group(1).capitalize() + (f" {year}" if m.group(2) else "")
        return clean_stem, (year, month, 15, 0), disp

    # 2. 4-digit code e.g. 0813, 0731, 0905, 0324, 0613, 0309, 1017, optionally with v2
    m = re.search(r'(?:[\s\-_]|\()(\d{4})(?:[\s\-_]+v?(\d+))?\)?$', stem)
    if m:
        code = m.group(1)
        v_sub = int(m.group(2)) if m.group(2) else 0
        mm, dd = int(code[:2]), int(code[2:])
        if 1 <= mm <= 12 and 1 <= dd <= 31:
            year = int(release_date[:4]) if release_date and len(release_date) >= 4 else 2025
            clean_stem = stem[:m.start()].strip()
            disp = f"{code}" + (f" v{v_sub}" if v_sub > 0 else "")
            return clean_stem, (year, mm, dd, v_sub), disp
        # Check if YYMM, e.g. 2507 -> 2025-07, 2603 -> 2026-03
        yy = int(code[:2])
        if 23 <= yy <= 27 and 1 <= int(code[2:]) <= 12:
            year = 2000 + yy
            month = int(code[2:])
            clean_stem = stem[:m.start()].strip()
            disp = f"{year}-{month:02d}"
            return clean_stem, (year, month, 15, v_sub), disp

    # 3. Fallback to release_date if provided
    if release_date and len(release_date) >= 10:
        try:
            parts = [int(p) for p in release_date[:10].split("-")]
            return stem, (parts[0], parts[1], parts[2], 0), release_date[:10]
        except Exception:
            pass

    return stem, None, None


# ══════════════════════════════════════════════════════════════════════
# 3. Dynamic Leave-One-Out Calibration (38 Benchmarks)
# ══════════════════════════════════════════════════════════════════════

def extract_benchmarks(raw_data: List[dict], min_valid: int = 3) -> Tuple[List[dict], Dict[str, dict]]:
    """Extract and parse all 38 benchmark metrics from raw data items."""
    models = []
    metric_keys = list(BENCHMARK_DEFS.keys())

    for d in raw_data:
        full_name = d.get("shortName") or d.get("name") or "Unknown"
        creator = d.get("modelCreatorName") or "Unknown"
        date = d.get("releaseDate")
        slug = d.get("slug") or ""
        scores = d.get("scores") or {}

        parsed_metrics = {}
        valid_count = 0
        for k, info in BENCHMARK_DEFS.items():
            val = None
            for alias in info["aliases"]:
                if d.get(alias) is not None:
                    val = d.get(alias)
                    break
                if scores.get(alias) is not None:
                    val = scores.get(alias)
                    break
            if val is not None and isinstance(val, (int, float)):
                parsed_metrics[k] = float(val)
                valid_count += 1
            else:
                parsed_metrics[k] = None

        if valid_count >= min_valid:
            base_name, th_tag, th_lvl = parse_model_name(full_name)
            models.append({
                "name": full_name,
                "base_name": base_name,
                "creator": creator,
                "slug": slug,
                "date": date,
                "thinking_tag": th_tag,
                "thinking_level": th_lvl,
                "parsed": parsed_metrics,
                "valid_count": valid_count,
                "raw_item": d,
            })

    # Compute raw min / max ranges per benchmark
    metric_ranges = {}
    for k in metric_keys:
        vals = [m["parsed"][k] for m in models if m["parsed"][k] is not None]
        if vals:
            metric_ranges[k] = {"min": min(vals), "max": max(vals), "count": len(vals)}
        else:
            metric_ranges[k] = {"min": 0.0, "max": 1.0, "count": 0}

    return models, metric_ranges


def calibrate_benchmark_bounds(
    models: List[dict],
    metric_ranges: Dict[str, dict],
    tolerance: float = 1e-4,
    max_rounds: int = 30
) -> Tuple[Dict[str, dict], int]:
    """Execute dynamic leave-one-out scaling calibration across all benchmarks."""
    metric_keys = list(BENCHMARK_DEFS.keys())
    bounds = {k: {"lower": 0.0, "upper": 1.0} for k in metric_keys}
    converged_round = max_rounds

    for round_idx in range(1, max_rounds + 1):
        # 1. Map scores under current bounds
        norm_scores = {}
        for i, m in enumerate(models):
            norm_scores[i] = {}
            for k in metric_keys:
                val = m["parsed"][k]
                rng = metric_ranges[k]
                if val is None or rng["count"] == 0:
                    norm_scores[i][k] = None
                elif rng["max"] == rng["min"]:
                    norm_scores[i][k] = 0.5
                else:
                    raw_norm = (val - rng["min"]) / (rng["max"] - rng["min"])
                    low, high = bounds[k]["lower"], bounds[k]["upper"]
                    norm_scores[i][k] = low + raw_norm * (high - low)

        # 2. Parallel leave-one-out calculation
        new_bounds = {}
        round_max_delta = 0.0

        for excluded_k in metric_keys:
            leave_out_avgs = {}
            for i in range(len(models)):
                scores = [norm_scores[i][k] for k in metric_keys
                          if k != excluded_k and norm_scores[i][k] is not None]
                if scores:
                    leave_out_avgs[i] = sum(scores) / len(scores)

            if not leave_out_avgs:
                new_bounds[excluded_k] = dict(bounds[excluded_k])
                continue

            min_avg = min(leave_out_avgs.values())
            max_avg = max(leave_out_avgs.values())

            if max_avg > min_avg:
                norm_leave_out = {i: (avg - min_avg) / (max_avg - min_avg)
                                  for i, avg in leave_out_avgs.items()}
            else:
                norm_leave_out = {i: 0.5 for i in leave_out_avgs}

            tested = [norm_leave_out[i] for i, m in enumerate(models)
                      if m["parsed"][excluded_k] is not None and i in norm_leave_out]
            if tested:
                new_low = min(tested)
                new_high = max(tested)
            else:
                new_low = bounds[excluded_k]["lower"]
                new_high = bounds[excluded_k]["upper"]

            delta = max(abs(new_low - bounds[excluded_k]["lower"]),
                        abs(new_high - bounds[excluded_k]["upper"]))
            round_max_delta = max(round_max_delta, delta)
            new_bounds[excluded_k] = {"lower": new_low, "upper": new_high}

        bounds = new_bounds
        if round_max_delta < tolerance:
            converged_round = round_idx
            break

    # Apply calibrated bounds to all models
    for m in models:
        m["calibrated_scores"] = {}
        for k in metric_keys:
            val = m["parsed"][k]
            rng = metric_ranges[k]
            if val is None or rng["count"] == 0:
                m["calibrated_scores"][k] = None
            elif rng["max"] == rng["min"]:
                m["calibrated_scores"][k] = 0.5
            else:
                raw_norm = (val - rng["min"]) / (rng["max"] - rng["min"])
                low, high = bounds[k]["lower"], bounds[k]["upper"]
                m["calibrated_scores"][k] = low + raw_norm * (high - low)

    return bounds, converged_round


# ══════════════════════════════════════════════════════════════════════
# 4. Vendor & Series Hierarchy Definitions & CSV Grid Manager
# ══════════════════════════════════════════════════════════════════════

DEFAULT_SERIES_GRIDS = {
    "OpenAI - GPT": {
        "vendor": "OpenAI",
        "series": "GPT",
        "versions": [
            "GPT-3.5", "GPT-4", "GPT-4.1", "GPT-4.5", "GPT-5", "GPT-5.1",
            "GPT-5.2", "GPT-5.3", "GPT-5.4", "GPT-5.5", "GPT-5.6", "GPT-6", "GPT-6.1", "GPT-6.2"
        ],
        "tiers": [
            "Tier 1 (Astra / Pro)",
            "Tier 2 (Sol / Standard)",
            "Tier 3 (Terra / Mini)",
            "Tier 4 (Luna / Nano)",
        ],
        "mapping": {
            "Tier 1 (Astra / Pro)": {
                "GPT-5.4": ["GPT-5.4 Pro"],
                "GPT-5.5": ["GPT-5.5 Pro"],
                "GPT-6": ["GPT-6 Astra"],
                "GPT-6.2": ["GPT-6.2 Astra", "Astra for Law 6.2"],
            },
            "Tier 2 (Sol / Standard)": {
                "GPT-3.5": ["GPT-3.5 Turbo", "GPT-3.5 Turbo (0613)"],
                "GPT-4": ["GPT-4", "GPT-4 Turbo", "GPT-4o (Aug)", "GPT-4o (ChatGPT)", "GPT-4o (Mar)", "GPT-4o (May)", "GPT-4o (Nov)", "GPT-4o Realtime (Dec)"],
                "GPT-4.1": ["GPT-4.1"],
                "GPT-4.5": ["GPT-4.5 (Preview)"],
                "GPT-5": ["GPT-5", "GPT-5 (ChatGPT)", "GPT-5 Codex"],
                "GPT-5.1": ["GPT-5.1", "GPT-5.1 Codex"],
                "GPT-5.2": ["GPT-5.2", "GPT-5.2 Codex"],
                "GPT-5.3": ["GPT-5.3 Codex"],
                "GPT-5.4": ["GPT-5.4"],
                "GPT-5.5": ["GPT-5.5", "GPT-5.5 Instant (May 2026)", "GPT-5.5 Instant (June 2026)"],
                "GPT-5.6": ["GPT-5.6 Sol"],
                "GPT-6": ["GPT-6 Sol", "GPT-6 Sol (Daybreak Blue)"],
                "GPT-6.1": ["GPT-6.1 Sol"],
                "GPT-6.2": ["GPT-6.2 Sol"],
            },
            "Tier 3 (Terra / Mini)": {
                "GPT-4": ["GPT-4o mini", "GPT-4o mini Realtime (Dec)"],
                "GPT-4.1": ["GPT-4.1 mini"],
                "GPT-5": ["GPT-5 mini"],
                "GPT-5.1": ["GPT-5.1 Codex mini"],
                "GPT-5.4": ["GPT-5.4 mini"],
                "GPT-5.6": ["GPT-5.6 Terra"],
                "GPT-6.1": ["GPT-6.1 Terra"],
            },
            "Tier 4 (Luna / Nano)": {
                "GPT-4.1": ["GPT-4.1 nano"],
                "GPT-5": ["GPT-5 nano"],
                "GPT-5.4": ["GPT-5.4 nano"],
                "GPT-5.6": ["GPT-5.6 Luna"],
                "GPT-6": ["GPT-6 Luna"],
            }
        }
    },
    "OpenAI - o": {
        "vendor": "OpenAI",
        "series": "o",
        "versions": ["o1", "o3", "o4"],
        "tiers": [
            "Tier 1 (Pro)",
            "Tier 2 (Standard)",
            "Tier 3 (Mini)",
        ],
        "mapping": {
            "Tier 1 (Pro)": {
                "o1": ["o1-pro"],
                "o3": ["o3-pro"],
            },
            "Tier 2 (Standard)": {
                "o1": ["o1", "o1-preview"],
                "o3": ["o3"],
            },
            "Tier 3 (Mini)": {
                "o1": ["o1-mini"],
                "o3": ["o3-mini"],
                "o4": ["o4-mini"],
            }
        }
    },
    "OpenAI - GPT-OSS": {
        "vendor": "OpenAI",
        "series": "GPT-OSS",
        "versions": ["GPT-OSS"],
        "tiers": [
            "Tier 1 (120B)",
            "Tier 2 (20B)",
        ],
        "mapping": {
            "Tier 1 (120B)": {
                "GPT-OSS": ["gpt-oss-120b"],
            },
            "Tier 2 (20B)": {
                "GPT-OSS": ["gpt-oss-20b"],
            }
        }
    },
    "Google - Gemini": {
        # User instruction preserved: "Gemini 4有两个模型，是同等级但是是不同版本"
        "vendor": "Google",
        "series": "Gemini",
        "versions": [
            "Gemini 1.0", "Gemini 1.5", "Gemini 2.0", "Gemini 2.5",
            "Gemini 3.0", "Gemini 3.1", "Gemini 3.5", "Gemini 3.6",
            "Gemini 3.7", "Gemini 3.8", "Gemini 4 Argon", "Gemini 4 Carbon",
            "Gemini 4 Hydrogen", "Gemini 4 Neon"
        ],
        "tiers": [
            "Tier 1 (Ultra / Deep Think)",
            "Tier 2 (Pro)",
            "Tier 3 (Flash)",
            "Tier 4 (Flash-Lite / Nano)",
        ],
        "mapping": {
            "Tier 1 (Ultra / Deep Think)": {
                "Gemini 1.0": ["Gemini 1.0 Ultra"],
                "Gemini 3.0": ["Gemini 3 Deep Think"],
                "Gemini 4 Neon": ["Gemini 4 Neon"],
            },
            "Tier 2 (Pro)": {
                "Gemini 1.0": ["Gemini 1.0 Pro"],
                "Gemini 1.5": ["Gemini 1.5 Pro (May)", "Gemini 1.5 Pro (Sep)"],
                "Gemini 2.0": ["Gemini 2.0 Pro Experimental"],
                "Gemini 2.5": ["Gemini 2.5 Pro", "Gemini 2.5 Pro (Mar)", "Gemini 2.5 Pro (May)"],
                "Gemini 3.0": ["Gemini 3 Pro Preview"],
                "Gemini 3.1": ["Gemini 3.1 Pro Preview"],
                "Gemini 4 Argon": ["Gemini 4 Argon"],
                "Gemini 4 Carbon": ["Gemini 4 Carbon"],
            },
            "Tier 3 (Flash)": {
                "Gemini 1.5": ["Gemini 1.5 Flash (May)", "Gemini 1.5 Flash (Sep)"],
                "Gemini 2.0": ["Gemini 2.0 Flash", "Gemini 2.0 Flash (exp)", "Gemini 2.0 Flash Thinking exp. (Dec)", "Gemini 2.0 Flash Thinking exp. (Jan)"],
                "Gemini 2.5": ["Gemini 2.5 Flash", "Gemini 2.5 Flash (Apr)", "Gemini 2.5 Flash (Sep)"],
                "Gemini 3.0": ["Gemini 3 Flash"],
                "Gemini 3.5": ["Gemini 3.5 Flash"],
                "Gemini 3.6": ["Gemini 3.6 Flash"],
                "Gemini 3.7": ["Gemini 3.7 Flash"],
                "Gemini 3.8": ["Gemini 3.8 Flash"],
                "Gemini 4 Hydrogen": ["Gemini 4 Hydrogen"],
            },
            "Tier 4 (Flash-Lite / Nano)": {
                "Gemini 1.5": ["Gemini 1.5 Flash-8B"],
                "Gemini 2.0": ["Gemini 2.0 Flash-Lite (Feb)", "Gemini 2.0 Flash-Lite (Preview)"],
                "Gemini 2.5": ["Gemini 2.5 Flash-Lite", "Gemini 2.5 Flash-Lite (Sep)"],
                "Gemini 3.1": ["Gemini 3.1 Flash-Lite"],
                "Gemini 3.5": ["Gemini 3.5 Flash-Lite"],
            }
        }
    },
    "Google - Gemma": {
        "vendor": "Google",
        "series": "Gemma",
        "versions": ["Gemma 3", "Gemma 4"],
        "tiers": [
            "Tier 1 (Large: 31B-26B)",
            "Tier 2 (Mid: 12B)",
            "Tier 3 (Small: 4B-E4B)",
            "Tier 4 (Nano: 2B-270M)",
        ],
        "mapping": {
            "Tier 1 (Large: 31B-26B)": {
                "Gemma 3": ["Gemma 3 27B"],
                "Gemma 4": ["Gemma 4 31B", "Gemma 4 26B A4B", "DiffusionGemma 26B A4B"],
            },
            "Tier 2 (Mid: 12B)": {
                "Gemma 3": ["Gemma 3 12B"],
                "Gemma 4": ["Gemma 4 12B"],
            },
            "Tier 3 (Small: 4B-E4B)": {
                "Gemma 3": ["Gemma 3 4B", "Gemma 3n E4B", "Gemma 3n E4B (May)"],
                "Gemma 4": ["Gemma 4 E4B"],
            },
            "Tier 4 (Nano: 2B-270M)": {
                "Gemma 3": ["Gemma 3 1B", "Gemma 3 270M", "Gemma 3n E2B"],
                "Gemma 4": ["Gemma 4 E2B"],
            }
        }
    },
    "Anthropic - Claude": {
        "vendor": "Anthropic",
        "series": "Claude",
        "versions": [
            "Claude 2", "Claude 3", "Claude 3.5", "Claude 3.7", "Claude 4",
            "Claude 4.1", "Claude 4.5", "Claude 4.6", "Claude 4.7",
            "Claude 4.8", "Claude 5", "Claude 5.1", "Claude 5.2", "Claude 5.5"
        ],
        "tiers": [
            "Tier 1 (Opus)",
            "Tier 2 (Fable)",
            "Tier 3 (Sonnet)",
            "Tier 4 (Haiku)",
        ],
        "mapping": {
            "Tier 1 (Opus)": {
                "Claude 3": ["Claude 3 Opus"],
                "Claude 4": ["Claude 4 Opus"],
                "Claude 4.1": ["Claude 4.1 Opus"],
                "Claude 4.5": ["Claude Opus 4.5"],
                "Claude 4.6": ["Claude Opus 4.6"],
                "Claude 4.7": ["Claude Opus 4.7"],
                "Claude 4.8": ["Claude Opus 4.8"],
                "Claude 5": ["Claude Opus 5"],
                "Claude 5.5": ["Claude Opus 5.5"],
            },
            "Tier 2 (Fable)": {
                "Claude 5": ["Claude Fable 5"],
                "Claude 5.1": ["Claude Fable 5.1"],
                "Claude 5.2": ["Claude Fable 5.2"],
            },
            "Tier 3 (Sonnet)": {
                "Claude 3": ["Claude 3 Sonnet"],
                "Claude 3.5": ["Claude 3.5 Sonnet (June)", "Claude 3.5 Sonnet (Oct)"],
                "Claude 3.7": ["Claude 3.7 Sonnet"],
                "Claude 4": ["Claude 4 Sonnet"],
                "Claude 4.5": ["Claude 4.5 Sonnet"],
                "Claude 4.6": ["Claude Sonnet 4.6"],
                "Claude 5": ["Claude Sonnet 5"],
                "Claude 5.5": ["Claude Sonnet 5.5"],
            },
            "Tier 4 (Haiku)": {
                "Claude 2": ["Claude Instant", "Claude 2.0", "Claude 2.1"],
                "Claude 3": ["Claude 3 Haiku"],
                "Claude 3.5": ["Claude 3.5 Haiku"],
                "Claude 4.5": ["Claude 4.5 Haiku"],
                "Claude 5.5": ["Claude Haiku 5.5"],
            }
        }
    },
    "DeepSeek - DeepSeek-V": {
        "vendor": "DeepSeek",
        "series": "DeepSeek-V",
        "versions": [
            "DeepSeek V1", "DeepSeek V2", "DeepSeek V2.5", "DeepSeek V3",
            "DeepSeek V3.1", "DeepSeek V3.2", "DeepSeek V4", "DeepSeek V4.1"
        ],
        "tiers": [
            "Tier 1 (Pro / Full)",
            "Tier 2 (Flash / Terminus)",
            "Tier 3 (Lite)",
        ],
        "mapping": {
            "Tier 1 (Pro / Full)": {
                "DeepSeek V1": ["DeepSeek LLM 67B (V1)"],
                "DeepSeek V2": ["DeepSeek-V2", "DeepSeek-Coder-V2"],
                "DeepSeek V2.5": ["DeepSeek-V2.5", "DeepSeek-V2.5 (Dec)"],
                "DeepSeek V3": ["DeepSeek V3 (Dec)", "DeepSeek V3 0324"],
                "DeepSeek V3.1": ["DeepSeek V3.1"],
                "DeepSeek V3.2": ["DeepSeek V3.2", "DeepSeek V3.2 Exp", "DeepSeek V3.2 Speciale"],
                "DeepSeek V4": ["DeepSeek V4 Pro", "DeepSeek V4 Pro 0813"],
            },
            "Tier 2 (Flash / Terminus)": {
                "DeepSeek V3.1": ["DeepSeek V3.1 Terminus"],
                "DeepSeek V4": ["DeepSeek V4 Flash", "DeepSeek V4 Flash 0731", "DeepSeek V4 Flash Vision"],
                "DeepSeek V4.1": ["DeepSeek V4.1 Flash", "DeepSeek V4.1 Flash 1017"],
            },
            "Tier 3 (Lite)": {
                "DeepSeek V2": ["DeepSeek Coder V2 Lite"],
            }
        }
    },
    "DeepSeek - DeepSeek-R": {
        "vendor": "DeepSeek",
        "series": "DeepSeek-R",
        "versions": ["DeepSeek R1", "DeepSeek R1 0528"],
        "tiers": [
            "Tier 1 (Full / R1)",
            "Tier 2 (Distill 70B / 32B)",
            "Tier 3 (Distill 14B / 8B / 1.5B)",
        ],
        "mapping": {
            "Tier 1 (Full / R1)": {
                "DeepSeek R1": ["DeepSeek R1 (Jan)"],
                "DeepSeek R1 0528": ["DeepSeek R1 0528", "DeepSeek R1 0528 Qwen3 8B"],
            },
            "Tier 2 (Distill 70B / 32B)": {
                "DeepSeek R1": ["DeepSeek R1 Distill Llama 70B", "DeepSeek R1 Distill Qwen 32B"],
            },
            "Tier 3 (Distill 14B / 8B / 1.5B)": {
                "DeepSeek R1": ["DeepSeek R1 Distill Qwen 14B", "DeepSeek R1 Distill Llama 8B", "DeepSeek R1 Distill Qwen 1.5B"],
            }
        }
    },
    "Mistral - Mistral": {
        "vendor": "Mistral",
        "series": "Mistral",
        "versions": [
            "Mistral v1", "Mistral v2", "Mistral v3",
            "Mistral v3.1", "Mistral v3.2", "Mistral v3.5", "Mistral v4"
        ],
        "tiers": [
            "Tier 1 (Large / High-MoE)",
            "Tier 2 (Medium)",
            "Tier 3 (Small / Ministral / 7B)",
        ],
        "mapping": {
            "Tier 1 (Large / High-MoE)": {
                "Mistral v1": ["Mistral Large (Feb)"],
                "Mistral v2": ["Mistral Large 2 (Jul)", "Mistral Large 2 (Nov)", "Pixtral Large", "Mixtral 8x22B"],
                "Mistral v3": ["Mistral Large 3"],
                "Mistral v4": ["Mistral Large 4 Preview", "Mistral Large 4"],
            },
            "Tier 2 (Medium)": {
                "Mistral v1": ["Mistral Medium", "Mixtral 8x7B"],
                "Mistral v3": ["Mistral Medium 3"],
                "Mistral v3.1": ["Mistral Medium 3.1"],
                "Mistral v3.5": ["Mistral Medium 3.5"],
            },
            "Tier 3 (Small / Ministral / 7B)": {
                "Mistral v1": ["Mistral 7B", "Mistral Small (Feb)", "Mistral Small (Sep)"],
                "Mistral v3": ["Mistral Small 3", "Ministral 3 8B", "Ministral 3 14B", "Ministral 3 3B"],
                "Mistral v3.1": ["Mistral Small 3.1"],
                "Mistral v3.2": ["Mistral Small 3.2"],
                "Mistral v4": ["Mistral Small 4"],
            }
        }
    },
    "Mistral - Devstral": {
        "vendor": "Mistral",
        "series": "Devstral",
        "versions": ["Devstral 1", "Devstral 2"],
        "tiers": [
            "Tier 1 (Medium / Full)",
            "Tier 2 (Small)",
        ],
        "mapping": {
            "Tier 1 (Medium / Full)": {
                "Devstral 1": ["Devstral Medium"],
                "Devstral 2": ["Devstral 2"],
            },
            "Tier 2 (Small)": {
                "Devstral 1": ["Devstral Small", "Devstral Small (May)"],
                "Devstral 2": ["Devstral Small 2"],
            }
        }
    },
    "Mistral - Magistral": {
        "vendor": "Mistral",
        "series": "Magistral",
        "versions": ["Magistral 1.0", "Magistral 1.2"],
        "tiers": [
            "Tier 1 (Medium)",
            "Tier 2 (Small)",
        ],
        "mapping": {
            "Tier 1 (Medium)": {
                "Magistral 1.0": ["Magistral Medium 1"],
                "Magistral 1.2": ["Magistral Medium 1.2"],
            },
            "Tier 2 (Small)": {
                "Magistral 1.0": ["Magistral Small 1"],
                "Magistral 1.2": ["Magistral Small 1.2"],
            }
        }
    },
    "Alibaba - Qwen": {
        "vendor": "Alibaba",
        "series": "Qwen",
        "versions": [
            "Qwen 2", "Qwen 2.5", "Qwen 3", "Qwen 3.5",
            "Qwen 3.6", "Qwen 3.7", "Qwen 3.8", "Qwen 4"
        ],
        "tiers": [
            "Tier 1 (Max / Reasoning)",
            "Tier 2 (Plus / Ultra MoE)",
            "Tier 3 (Large: 122B-27B)",
            "Tier 4 (Small: 14B-4B)",
            "Tier 5 (Nano: 2B-0.6B)",
        ],
        "mapping": {
            "Tier 1 (Max / Reasoning)": {
                "Qwen 2.5": ["Qwen2.5 Max"],
                "Qwen 3": ["Qwen3 Max", "Qwen3 Max Thinking", "Qwen3 Max (Preview)", "Qwen3 Max Thinking (Preview)"],
                "Qwen 3.6": ["Qwen3.6 Max Preview"],
                "Qwen 3.7": ["Qwen3.7 Max"],
                "Qwen 3.8": ["Qwen3.8 Max", "Qwen3.8 Max (0902)"],
                "Qwen 4": ["Qwen4 Max"],
            },
            "Tier 2 (Plus / Ultra MoE)": {
                "Qwen 3": ["Qwen3 235B 2507", "Qwen3 235B A22B 2507", "Qwen3 VL 235B A22B"],
                "Qwen 3.5": ["Qwen3.5 Omni Plus", "Qwen3.5 397B A17B"],
                "Qwen 3.6": ["Qwen3.6 Plus"],
                "Qwen 3.7": ["Qwen3.7 Plus"],
                "Qwen 3.8": ["Qwen3.8 2.4T A95B"],
            },
            "Tier 3 (Large: 122B-27B)": {
                "Qwen 2": ["Qwen2 72B"],
                "Qwen 2.5": ["Qwen2.5 72B", "Qwen2.5 Coder 32B", "Qwen2.5 Instruct 32B", "Qwen2.5 Turbo"],
                "Qwen 3": ["Qwen3 30B", "Qwen3 32B", "Qwen3 235B", "Qwen3 Coder 480B", "Qwen3 Next 80B A3B", "Qwen3 Coder Next", "Qwen3 Omni 30B A3B", "Qwen3 VL 30B A3B", "Qwen3 30B A3B 2507", "Qwen3 VL 32B", "Qwen3 Coder 30B A3B"],
                "Qwen 3.5": ["Qwen3.5 122B A10B", "Qwen3.5 35B A3B", "Qwen3.5 27B", "Qwen3.5 Omni Flash"],
                "Qwen 3.6": ["Qwen3.6 35B A3B", "Qwen3.6 27B"],
                "Qwen 3.8": ["Qwen3.8 27B", "Qwen3.8-Flash-Next"],
            },
            "Tier 4 (Small: 14B-4B)": {
                "Qwen 2.5": ["Qwen2.5 Coder 7B"],
                "Qwen 3": ["Qwen3 14B", "Qwen3 8B", "Qwen3 4B", "Qwen3 VL 8B", "Qwen3 4B 2507", "Qwen3 VL 4B"],
                "Qwen 3.5": ["Qwen3.5 9B", "Qwen3.5 4B"],
            },
            "Tier 5 (Nano: 2B-0.6B)": {
                "Qwen 3": ["Qwen3 1.7B", "Qwen3 0.6B"],
                "Qwen 3.5": ["Qwen3.5 2B", "Qwen3.5 0.8B"],
            }
        }
    },
    "Alibaba - QwQ": {
        "vendor": "Alibaba",
        "series": "QwQ",
        "versions": ["QwQ Preview", "QwQ Release"],
        "tiers": ["Tier 1 (32B)"],
        "mapping": {
            "Tier 1 (32B)": {
                "QwQ Preview": ["QwQ 32B-Preview"],
                "QwQ Release": ["QwQ-32B"],
            }
        }
    },
    "SpaceXAI - Grok": {
        "vendor": "SpaceXAI",
        "series": "Grok",
        "versions": [
            "Grok-1", "Grok 2", "Grok 3", "Grok 4", "Grok 4.1", "Grok 4.20",
            "Grok 4.3", "Grok 4.5", "Grok 4.6", "Grok 4.7"
        ],
        "tiers": [
            "Tier 1 (Full / Flagship)",
            "Tier 2 (Fast / Mini)",
        ],
        "mapping": {
            "Tier 1 (Full / Flagship)": {
                "Grok-1": ["Grok-1"],
                "Grok 2": ["Grok 2", "Grok Beta"],
                "Grok 3": ["Grok 3", "Grok 3 Reasoning Beta"],
                "Grok 4": ["Grok 4", "Grok Build 0.1 0616"],
                "Grok 4.20": ["Grok 4.20 0309", "Grok 4.20 0309 v2"],
                "Grok 4.3": ["Grok 4.3"],
                "Grok 4.5": ["Grok 4.5"],
                "Grok 4.6": ["Grok 4.6"],
                "Grok 4.7": ["Grok 4.7"],
            },
            "Tier 2 (Fast / Mini)": {
                "Grok 3": ["Grok 3 mini Reasoning"],
                "Grok 4": ["Grok 4 Fast", "Grok Code Fast 1"],
                "Grok 4.1": ["Grok 4.1 Fast"],
            }
        }
    },
    "Meta - Llama": {
        "vendor": "Meta",
        "series": "Llama",
        "versions": [
            "Llama 1", "Llama 2", "Llama 3", "Llama 3.1", "Llama 3.2",
            "Llama 3.3", "Llama 4"
        ],
        "tiers": [
            "Tier 1 (Wonder / 405B / 65B)",
            "Tier 2 (Spark / 70B / 90B)",
            "Tier 3 (Glimmer / Scout / 13B / 11B)",
            "Tier 4 (Compact / Small: 8B / 7B / 3B / 1B)",
        ],
        "mapping": {
            "Tier 1 (Wonder / 405B / 65B)": {
                "Llama 1": ["Llama 65B"],
                "Llama 3.1": ["Llama 3.1 405B"],
            },
            "Tier 2 (Spark / 70B / 90B)": {
                "Llama 2": ["Llama 2 Chat 70B"],
                "Llama 3": ["Llama 3 70B"],
                "Llama 3.1": ["Llama 3.1 70B"],
                "Llama 3.2": ["Llama 3.2 90B (Vision)"],
                "Llama 3.3": ["Llama 3.3 70B"],
            },
            "Tier 3 (Glimmer / Scout / 13B / 11B)": {
                "Llama 2": ["Llama 2 Chat 13B"],
                "Llama 3.2": ["Llama 3.2 11B (Vision)"],
                "Llama 4": ["Llama 4 Maverick", "Llama 4 Scout"],
            },
            "Tier 4 (Compact / Small: 8B / 7B / 3B / 1B)": {
                "Llama 2": ["Llama 2 Chat 7B"],
                "Llama 3": ["Llama 3 8B"],
                "Llama 3.1": ["Llama 3.1 8B"],
                "Llama 3.2": ["Llama 3.2 3B", "Llama 3.2 1B"],
            }
        }
    },
    "Meta - Muse": {
        "vendor": "Meta",
        "series": "Muse",
        "versions": ["Muse 1.0", "Muse 1.1", "Muse 1.2", "Muse 1.3", "Muse 1.4"],
        "tiers": [
            "Tier 1 (Wonder)",
            "Tier 2 (Spark)",
            "Tier 3 (Ember)",
            "Tier 4 (Glimmer)",
        ],
        "mapping": {
            "Tier 1 (Wonder)": {
                "Muse 1.0": ["Muse Wonder", "Muse Wonder Full"],
            },
            "Tier 2 (Spark)": {
                "Muse 1.0": ["Muse Spark", "Muse Spark Open"],
                "Muse 1.1": ["Muse Spark 1.1"],
                "Muse 1.2": ["Muse Spark 1.2"],
                "Muse 1.3": ["Muse Spark 1.3"],
            },
            "Tier 3 (Ember)": {
                "Muse 1.4": ["Muse Ember"],
            },
            "Tier 4 (Glimmer)": {
                "Muse 1.0": ["Muse Glimmer"],
            }
        }
    },
    "Z_AI - GLM": {
        "vendor": "Z_AI",
        "series": "GLM",
        "versions": [
            "GLM-4.5", "GLM-4.6", "GLM-4.7", "GLM-5",
            "GLM-5.1", "GLM-5.2", "GLM-5.3"
        ],
        "tiers": [
            "Tier 1 (Flagship / Pro)",
            "Tier 2 (Turbo / Air)",
            "Tier 3 (Flash)",
        ],
        "mapping": {
            "Tier 1 (Flagship / Pro)": {
                "GLM-4.5": ["GLM-4.5", "GLM-4.5V"],
                "GLM-4.6": ["GLM-4.6", "GLM-4.6V"],
                "GLM-4.7": ["GLM-4.7"],
                "GLM-5": ["GLM-5"],
                "GLM-5.1": ["GLM-5.1"],
                "GLM-5.2": ["GLM-5.2"],
                "GLM-5.3": ["GLM-5.3"],
            },
            "Tier 2 (Turbo / Air)": {
                "GLM-4.5": ["GLM-4.5-Air"],
                "GLM-5": ["GLM-5-Turbo", "GLM 5V Turbo"],
            },
            "Tier 3 (Flash)": {
                "GLM-4.7": ["GLM-4.7-Flash"],
                "GLM-5.3": ["GLM-5.3-Flash"],
            }
        }
    },
    "Amazon - Nova": {
        "vendor": "Amazon",
        "series": "Nova",
        "versions": ["Nova 1.0", "Nova 2.0"],
        "tiers": [
            "Tier 1 (Omni / Pro / Premier)",
            "Tier 2 (Lite)",
            "Tier 3 (Micro)",
        ],
        "mapping": {
            "Tier 1 (Omni / Pro / Premier)": {
                "Nova 1.0": ["Nova Pro", "Nova Premier"],
                "Nova 2.0": ["Nova 2.0 Pro Preview", "Nova 2.0 Omni"],
            },
            "Tier 2 (Lite)": {
                "Nova 1.0": ["Nova Lite"],
                "Nova 2.0": ["Nova 2.0 Lite"],
            },
            "Tier 3 (Micro)": {
                "Nova 1.0": ["Nova Micro"],
            }
        }
    },
    "Kimi - Kimi": {
        "vendor": "Kimi",
        "series": "Kimi",
        "versions": ["Kimi K2", "Kimi K2.5", "Kimi K2.6", "Kimi K2.7", "Kimi K3", "Kimi K3.1"],
        "tiers": [
            "Tier 1 (Pro / Code / Thinking)",
            "Tier 2 (Standard)",
            "Tier 3 (Linear / Efficient)",
        ],
        "mapping": {
            "Tier 1 (Pro / Code / Thinking)": {
                "Kimi K2": ["Kimi K2 Thinking"],
                "Kimi K2.7": ["Kimi K2.7 Code"],
                "Kimi K3.1": ["Kimi K3.1 Pro"],
            },
            "Tier 2 (Standard)": {
                "Kimi K2": ["Kimi K2", "Kimi K2 0905"],
                "Kimi K2.5": ["Kimi K2.5"],
                "Kimi K2.6": ["Kimi K2.6"],
                "Kimi K3": ["Kimi K3"],
            },
            "Tier 3 (Linear / Efficient)": {
                "Kimi K2": ["Kimi Linear 48B A3B Instruct"],
            }
        }
    },
    "Xiaomi - MiMo": {
        "vendor": "Xiaomi",
        "series": "MiMo",
        "versions": ["MiMo V2", "MiMo V2.5", "MiMo V2.6"],
        "tiers": [
            "Tier 1 (Pro / Omni)",
            "Tier 2 (Flash / Base)",
        ],
        "mapping": {
            "Tier 1 (Pro / Omni)": {
                "MiMo V2": ["MiMo-V2-Pro", "MiMo-V2-Omni", "MiMo-V2-Omni-0327"],
                "MiMo V2.5": ["MiMo-V2.5-Pro"],
                "MiMo V2.6": ["MiMo-V2.6-Pro"],
            },
            "Tier 2 (Flash / Base)": {
                "MiMo V2": ["MiMo-V2-Flash", "MiMo-V2-Flash (Feb 2026)"],
                "MiMo V2.5": ["MiMo-V2.5"],
                "MiMo V2.6": ["MiMo-V2.6-Flash"],
            }
        }
    }
}

# Alias for backward compatibility
DEFAULT_VENDOR_GRIDS = DEFAULT_SERIES_GRIDS


def clean_series_name(token: str) -> str:
    """Clean a token to form a series name."""
    token = token.strip()
    m = re.match(r'([A-Za-z]+)', token)
    if m:
        val = m.group(1)
        if len(val) >= 2:
            return val
    return token or "Default"


def detect_creator_series(creator: str, models: List[dict]) -> Dict[str, List[dict]]:
    """Group an unlisted creator's models into distinct series."""
    series_groups = defaultdict(list)
    for m in models:
        base_name = m["base_name"]
        words = re.split(r'[\s\-_]+', base_name.strip())
        first = words[0] if words else creator
        if first.lower() in ('openchat', 'deep', 'meta', 'llama', 'tencent'):
            if len(words) > 1:
                first = words[1]
        series_name = clean_series_name(first)
        series_groups[series_name].append(m)
    return dict(series_groups)


def auto_generate_series_grid(vendor: str, series: str, series_models: List[dict]) -> dict:
    """Automatically build a (Tiers x Versions) 2D grid for an unlisted series."""
    base_info = {}
    for m in series_models:
        bn = m["base_name"]
        if bn not in base_info:
            base_info[bn] = {"date": m.get("date") or "2025-01-01", "name": bn}
        else:
            if m.get("date") and m["date"] < base_info[bn]["date"]:
                base_info[bn]["date"] = m["date"]

    sorted_bases = sorted(base_info.values(), key=lambda x: x["date"])

    def get_tier(name):
        n = name.lower()
        if any(w in n for w in ["ultra", "max", "pro", "large", "405b", "397b", "235b", "120b", "70b", "67b", "65b"]):
            return "Tier 1 (Flagship / Large)"
        elif any(w in n for w in ["medium", "plus", "mid", "32b", "30b", "27b", "24b", "20b", "14b"]):
            return "Tier 2 (Medium / MoE)"
        elif any(w in n for w in ["small", "flash", "mini", "8b", "7b", "4b"]):
            return "Tier 3 (Small / Fast)"
        else:
            return "Tier 4 (Compact / Nano)"

    ver_clusters = defaultdict(list)
    for b in sorted_bases:
        d = b["date"][:7] if b["date"] else "2025-01"
        ver_clusters[d].append(b["name"])

    versions = sorted(ver_clusters.keys())
    tiers = [
        "Tier 1 (Flagship / Large)",
        "Tier 2 (Medium / MoE)",
        "Tier 3 (Small / Fast)",
        "Tier 4 (Compact / Nano)",
    ]
    mapping = {t: {v: [] for v in versions} for t in tiers}
    for b in sorted_bases:
        t = get_tier(b["name"])
        d = b["date"][:7] if b["date"] else "2025-01"
        mapping[t][d].append(b["name"])

    return {
        "vendor": vendor,
        "series": series,
        "versions": versions,
        "tiers": tiers,
        "mapping": mapping
    }


class VendorHierarchyManager:
    """Manages 2D series hierarchy grids (Tiers x Versions) and imports/exports CSV files."""

    def __init__(self, hierarchy_dir: str = HIERARCHY_DIR, all_models: Optional[List[dict]] = None, load_from_disk: bool = True):
        self.hierarchy_dir = hierarchy_dir
        os.makedirs(self.hierarchy_dir, exist_ok=True)
        self.grids = {}
        self._initialize_grids(all_models or [], load_from_disk=load_from_disk)

    def _initialize_grids(self, all_models: List[dict], load_from_disk: bool = True):
        """Initialize series grids from disk if CSVs exist, else load default or auto-generate and export."""
        curated_vendors = set()
        for series_key, default_data in DEFAULT_SERIES_GRIDS.items():
            vendor_name = default_data.get("vendor", series_key.split(" - ")[0])
            curated_vendors.add(vendor_name)
            curated_vendors.add(vendor_name.replace("_", " "))
            curated_vendors.add(vendor_name.replace(" ", "_"))

            csv_path = os.path.join(self.hierarchy_dir, f"{series_key}.csv")
            if load_from_disk and os.path.exists(csv_path):
                grid = self._load_csv_grid(csv_path)
                grid["vendor"] = default_data.get("vendor", series_key.split(" - ")[0])
                grid["series"] = default_data.get("series", series_key.split(" - ")[-1])
                self.grids[series_key] = grid
            else:
                self.grids[series_key] = default_data
                self._save_csv_grid(csv_path, default_data)

        # 2. Auto-generate for remaining creators with models
        if all_models:
            creator_models = defaultdict(list)
            for m in all_models:
                creator_models[m["creator"]].append(m)

            for creator, mlist in creator_models.items():
                c_clean = creator.replace("_", " ")
                if creator in curated_vendors or c_clean in curated_vendors or creator.replace(" ", "_") in curated_vendors:
                    continue

                series_map = detect_creator_series(creator, mlist)
                for series_name, s_models in series_map.items():
                    series_key = f"{creator} - {series_name}"
                    csv_path = os.path.join(self.hierarchy_dir, f"{series_key}.csv")
                    if load_from_disk and os.path.exists(csv_path):
                        grid = self._load_csv_grid(csv_path)
                        grid["vendor"] = creator
                        grid["series"] = series_name
                        self.grids[series_key] = grid
                    else:
                        auto_grid = auto_generate_series_grid(creator, series_name, s_models)
                        self.grids[series_key] = auto_grid
                        self._save_csv_grid(csv_path, auto_grid)

        # 3. Load any extra custom series CSVs on disk
        if load_from_disk and os.path.exists(self.hierarchy_dir):
            for fname in os.listdir(self.hierarchy_dir):
                if fname.endswith(".csv") and fname != "all_vendors_hierarchy.csv" and " - " in fname:
                    s_key = fname[:-4]
                    if s_key not in self.grids:
                        self.grids[s_key] = self._load_csv_grid(os.path.join(self.hierarchy_dir, fname))

    def _save_csv_grid(self, filepath: str, grid_data: dict):
        """Export a 2D hierarchy grid to CSV."""
        versions = grid_data["versions"]
        tiers = grid_data["tiers"]
        mapping = grid_data.get("mapping", {})

        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Tier \\ Version"] + versions)
            for t in tiers:
                row = [t]
                t_map = mapping.get(t, {})
                for v in versions:
                    models = t_map.get(v, [])
                    row.append(" / ".join(models) if models else "")
                writer.writerow(row)

    def _load_csv_grid(self, filepath: str) -> dict:
        """Load a 2D hierarchy grid from CSV (supporting user modifications)."""
        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            rows = [r for r in reader if r]

        if not rows:
            return {"versions": [], "tiers": [], "mapping": {}}

        header = rows[0]
        versions = [col.strip() for col in header[1:] if col.strip()]
        tiers = []
        mapping = defaultdict(lambda: defaultdict(list))

        for row in rows[1:]:
            tier_name = row[0].strip()
            if not tier_name:
                continue
            tiers.append(tier_name)
            for col_idx, cell in enumerate(row[1:]):
                if col_idx < len(versions):
                    v_name = versions[col_idx]
                    cell_content = cell.strip()
                    if cell_content:
                        models = [m.strip() for m in re.split(r'[/;,]', cell_content) if m.strip()]
                        mapping[tier_name][v_name].extend(models)

        base_filename = os.path.splitext(os.path.basename(filepath))[0]
        if " - " in base_filename:
            vendor, series = base_filename.split(" - ", 1)
        else:
            vendor, series = base_filename, base_filename

        return {
            "vendor": vendor,
            "series": series,
            "versions": versions,
            "tiers": tiers,
            "mapping": dict(mapping)
        }

    def export_all_csvs(self, overwrite_existing: bool = True):
        """Export individual series CSVs and a combined master CSV."""
        for series_key, data in self.grids.items():
            path = os.path.join(self.hierarchy_dir, f"{series_key}.csv")
            if overwrite_existing or not os.path.exists(path):
                self._save_csv_grid(path, data)

        master_path = os.path.join(self.hierarchy_dir, "all_vendors_hierarchy.csv")
        with open(master_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Vendor", "Series", "Tier", "Version", "Base Models"])
            for series_key, data in self.grids.items():
                vendor = data.get("vendor", series_key.split(" - ")[0])
                series = data.get("series", series_key.split(" - ")[-1])
                tiers = data["tiers"]
                mapping = data.get("mapping", {})
                for t in tiers:
                    for v in data["versions"]:
                        models = mapping.get(t, {}).get(v, [])
                        if models:
                            writer.writerow([vendor, series, t, v, " / ".join(models)])

    def diff_with_default(self, target: str) -> List[str]:
        """Compare the current loaded grid against the default curated grid for a series or vendor."""
        matching_keys = []
        if target == "all":
            matching_keys = list(DEFAULT_SERIES_GRIDS.keys())
        elif target in DEFAULT_SERIES_GRIDS:
            matching_keys = [target]
        else:
            t_low = target.lower().strip()
            for k, grid in DEFAULT_SERIES_GRIDS.items():
                vendor = grid.get("vendor", "").lower()
                series = grid.get("series", "").lower()
                if (vendor == t_low or
                    vendor.replace(" ", "_") == t_low or
                    vendor.replace("_", " ") == t_low or
                    series == t_low or
                    k.lower() == t_low or
                    k.lower().startswith(t_low + " - ")):
                    matching_keys.append(k)

        if not matching_keys:
            return [f"No default curated grid defined matching '{target}'."]

        diffs = []
        for s_key in matching_keys:
            default_grid = DEFAULT_SERIES_GRIDS[s_key]
            cur_grid = self.grids.get(s_key)
            if not cur_grid:
                diffs.append(f"Series '{s_key}' not loaded in current hierarchy.")
                continue

            if default_grid.get("versions") != cur_grid.get("versions"):
                diffs.append(f"[{s_key}] Versions modified:\n  Default: {default_grid.get('versions')}\n  Current: {cur_grid.get('versions')}")
            if default_grid.get("tiers") != cur_grid.get("tiers"):
                diffs.append(f"[{s_key}] Tiers modified:\n  Default: {default_grid.get('tiers')}\n  Current: {cur_grid.get('tiers')}")

            def _get_placements(grid):
                places = {}
                for t in grid.get("tiers", []):
                    for v in grid.get("versions", []):
                        for m in grid.get("mapping", {}).get(t, {}).get(v, []):
                            places[m.lower().strip()] = (t, v, m.strip())
                return places

            def_places = _get_placements(default_grid)
            cur_places = _get_placements(cur_grid)

            for m_key, (dt, dv, orig_name) in def_places.items():
                if m_key not in cur_places:
                    diffs.append(f"[{s_key}] Model removed from grid: '{orig_name}' (was in [{dt}, {dv}])")
                elif (dt, dv) != (cur_places[m_key][0], cur_places[m_key][1]):
                    ct, cv, _ = cur_places[m_key]
                    diffs.append(f"[{s_key}] Model moved: '{orig_name}' moved from [{dt}, {dv}] -> [{ct}, {cv}]")

            for m_key, (ct, cv, orig_name) in cur_places.items():
                if m_key not in def_places:
                    diffs.append(f"[{s_key}] New model added to grid: '{orig_name}' in [{ct}, {cv}]")

        return diffs

    def get_model_position(self, vendor_or_series: str, base_name: str) -> Optional[Tuple[int, int]]:
        """Return (tier_rank, version_rank) for a base model within a series or vendor."""
        candidate_grids = []
        if vendor_or_series in self.grids:
            candidate_grids.append(self.grids[vendor_or_series])
        else:
            v_low = vendor_or_series.lower().strip()
            for k, grid in self.grids.items():
                vendor = grid.get("vendor", "").lower()
                series = grid.get("series", "").lower()
                if (vendor == v_low or
                    vendor.replace(" ", "_") == v_low or
                    vendor.replace("_", " ") == v_low or
                    series == v_low or
                    k.lower() == v_low or
                    k.lower().startswith(v_low + " - ")):
                    candidate_grids.append(grid)

        if not candidate_grids:
            candidate_grids = list(self.grids.values())

        for grid in candidate_grids:
            tiers = grid.get("tiers", [])
            versions = grid.get("versions", [])
            mapping = grid.get("mapping", {})
            for t_idx, t in enumerate(tiers):
                t_map = mapping.get(t, {})
                for v_idx, v in enumerate(versions):
                    cell_models = t_map.get(v, [])
                    for cm in cell_models:
                        if cm.lower() == base_name.lower():
                            return (t_idx, v_idx)
        return None

    def get_model_series(self, base_name: str) -> Optional[str]:
        """Return the series key for a base model."""
        for s_key, grid in self.grids.items():
            mapping = grid.get("mapping", {})
            for t in grid.get("tiers", []):
                for v in grid.get("versions", []):
                    cell_models = mapping.get(t, {}).get(v, [])
                    for cm in cell_models:
                        if cm.lower() == base_name.lower():
                            return s_key
        return None


# ══════════════════════════════════════════════════════════════════════
# 5. Strict Constraint Generation Engine
# ══════════════════════════════════════════════════════════════════════

def generate_hierarchy_constraints(
    models: List[dict],
    manager: VendorHierarchyManager
) -> Tuple[List[Tuple[str, str, str]], Dict[str, int]]:
    """Generate all directed ordering constraints S(u) >= S(v) adhering strictly to:

    Rule 1 (Same series, same version, higher tier >= lower tier):
      - Within the same series and same version column, higher tier row >= lower tier row.
      - Enforces higher-tier model >= ALL date snapshots of the lower tier in this version column.
      - If matching thinking level exists between base variants: compare ONLY matching thinking level.
      - If no matching thinking level exists in lower model: higher thinking of higher tier >=
        lower thinking of lower tier (Th_u > Th_v => S_u >= S_v).
      - Lower thinking of higher tier is NOT forced to beat higher thinking of lower tier.

    Rule 2 (Same series, same tier, newer version >= older version):
      - Within the same series and same tier row, newer version column >= older version column.
      - If matching thinking level exists: compare ONLY matching thinking level.
      - If no matching thinking level in older model: higher thinking of newer version >=
        lower thinking of older version (Th_u > Th_v => S_u >= S_v).
      - Lower thinking of newer version is NOT forced to beat higher thinking of older version.

    Rule 3 (Same base model, higher thinking >= lower thinking):
      - Within the same base model: higher thinking level >= lower thinking level.

    Rule 4 (Same model stem, newer date snapshot >= older date snapshot):
      - Within the same model stem (e.g. Claude 3.5 Sonnet Oct >= June; Gemini 1.5 Pro Sep >= May;
        Gemini 1.5 Flash Sep >= May; GPT-4o Nov >= Aug >= May; DeepSeek V4 Pro 0813 >= 0424).
      - Applies matching/unmatched thinking rules consistent with Rule 1/2.
    """
    constraints = []

    # Group models by base_name
    models_by_base = defaultdict(list)
    for m in models:
        models_by_base[m["base_name"]].append(m)

    # ── Rule 3: Within same base model, higher thinking >= lower thinking ──
    for base_name, variants in models_by_base.items():
        if len(variants) > 1:
            for i in range(len(variants)):
                for j in range(len(variants)):
                    if variants[i]["thinking_level"] > variants[j]["thinking_level"]:
                        u_name = variants[i]["name"]
                        v_name = variants[j]["name"]
                        r = (f"Rule 3: Same model [{base_name}] higher thinking "
                             f"({variants[i]['thinking_tag']} > {variants[j]['thinking_tag']})")
                        constraints.append((u_name, v_name, r, "rule3_thinking"))

    # Helper to generate cross-model variants constraints
    def _add_pair_constraints(h_models, l_models, reason, stat_key):
        h_lvls = {m["thinking_level"] for m in h_models}
        l_lvls = {m["thinking_level"] for m in l_models}
        common_lvls = h_lvls & l_lvls

        for hm in h_models:
            h_lvl = hm["thinking_level"]
            if h_lvl in common_lvls:
                for lm in l_models:
                    if lm["thinking_level"] == h_lvl:
                        constraints.append((
                            hm["name"], lm["name"],
                            f"{reason} [matching thinking {hm['thinking_tag']}]",
                            stat_key
                        ))
            else:
                for lm in l_models:
                    if h_lvl > lm["thinking_level"]:
                        constraints.append((
                            hm["name"], lm["name"],
                            f"{reason} [unmatched H:{hm['thinking_tag']} > L:{lm['thinking_tag']}]",
                            stat_key
                        ))

        for lm in l_models:
            l_lvl = lm["thinking_level"]
            if l_lvl not in common_lvls:
                eligible_h = [hm for hm in h_models if hm["thinking_level"] > l_lvl]
                if eligible_h:
                    lowest_h = min(eligible_h, key=lambda x: x["thinking_level"])
                    constraints.append((
                        lowest_h["name"], lm["name"],
                        f"{reason} [unmatched L:{lm['thinking_tag']} < H:{lowest_h['thinking_tag']}]",
                        stat_key
                    ))

    # ── Rule 4: Within same model stem, newer date snapshot >= older date snapshot ──
    stems = defaultdict(dict)
    for m in models:
        bn = m["base_name"]
        rd = m.get("date")
        stem, dt_tuple, disp = parse_date_snapshot(bn, rd)
        if dt_tuple:
            stems[stem][bn] = (dt_tuple, disp)

    for stem, b_dict in stems.items():
        if len(b_dict) > 1:
            sorted_bases = sorted(b_dict.items(), key=lambda x: x[1][0])
            for i in range(len(sorted_bases)):
                for j in range(i + 1, len(sorted_bases)):
                    o_bn, (o_dt, o_disp) = sorted_bases[i]
                    n_bn, (n_dt, n_disp) = sorted_bases[j]
                    if o_dt < n_dt:
                        o_mods = models_by_base.get(o_bn, [])
                        n_mods = models_by_base.get(n_bn, [])
                        if n_mods and o_mods:
                            reason = f"Rule 4: Same model [{stem}] newer date ({n_disp} > {o_disp})"
                            _add_pair_constraints(n_mods, o_mods, reason, "rule4_date")

    # ── Rule 1 & Rule 2 strictly within each series grid ──
    for series_key, grid in manager.grids.items():
        tiers = grid.get("tiers", [])
        versions = grid.get("versions", [])
        mapping = grid.get("mapping", {})

        # Rule 1: Within same version column, higher tier row (lower tier index) > lower tier row
        for v in versions:
            tier_cells_in_v = []
            for t_idx, t in enumerate(tiers):
                base_names = mapping.get(t, {}).get(v, [])
                if any(bn in models_by_base for bn in base_names):
                    tier_cells_in_v.append((t_idx, t, base_names))

            for i in range(len(tier_cells_in_v)):
                for j in range(i + 1, len(tier_cells_in_v)):
                    h_idx, h_tier, h_base_names = tier_cells_in_v[i]
                    l_idx, l_tier, l_base_names = tier_cells_in_v[j]
                    reason = f"Rule 1: Series [{series_key}] version [{v}] {h_tier} > {l_tier}"
                    for h_base in h_base_names:
                        h_mods = models_by_base.get(h_base, [])
                        for l_base in l_base_names:
                            l_mods = models_by_base.get(l_base, [])
                            if h_mods and l_mods:
                                _add_pair_constraints(h_mods, l_mods, reason, "rule1_tier")

        # Rule 2: Within same tier row, newer version (higher version index) > older version
        for t in tiers:
            ver_cells_in_t = []
            for v_idx, v in enumerate(versions):
                base_names = mapping.get(t, {}).get(v, [])
                if any(bn in models_by_base for bn in base_names):
                    ver_cells_in_t.append((v_idx, v, base_names))

            for i in range(len(ver_cells_in_t)):
                for j in range(i + 1, len(ver_cells_in_t)):
                    o_idx, o_ver, o_base_names = ver_cells_in_t[i]
                    n_idx, n_ver, n_base_names = ver_cells_in_t[j]
                    reason = f"Rule 2: Series [{series_key}] tier [{t}] {n_ver} > {o_ver}"
                    for n_base in n_base_names:
                        n_mods = models_by_base.get(n_base, [])
                        for o_base in o_base_names:
                            o_mods = models_by_base.get(o_base, [])
                            if n_mods and o_mods:
                                _add_pair_constraints(n_mods, o_mods, reason, "rule2_version")

    # Deduplicate constraints while tracking exact rule breakdown
    seen = set()
    unique_constraints = []
    stats = {"rule1_tier": 0, "rule2_version": 0, "rule3_thinking": 0, "rule4_date": 0}
    for u, v, r, s_key in constraints:
        if (u, v) not in seen and u != v:
            seen.add((u, v))
            unique_constraints.append((u, v, r))
            stats[s_key] += 1

    return unique_constraints, stats


# ══════════════════════════════════════════════════════════════════════
# 6. Scoring Engine: Debiased Aggregation & Dykstra Isotonic Projection
# ══════════════════════════════════════════════════════════════════════

class HierarchyScoreEngine:
    """Computes final composite ability from calibrated benchmark scores while

    strictly respecting hierarchy DAG constraints via Dykstra's algorithm.
    """

    def __init__(self, models: List[dict], constraints: List[Tuple[str, str, str]]):
        self.models = models
        self.constraints = constraints
        self.name_to_idx = {m["name"]: i for i, m in enumerate(models)}
        self.idx_to_name = {i: m["name"] for i, m in enumerate(models)}

    def compute_debiased_initial_ability(self) -> List[float]:
        """Estimate initial latent ability using 2-way benchmark offset debiasing.

        y_{m, b} ~ theta_m + delta_b
        Adjusts for differences in benchmark hardness so models taking harsh
        niche evaluations are not penalized.
        """
        metric_keys = list(BENCHMARK_DEFS.keys())
        raw_means = []
        for m in self.models:
            valid_vals = [v for v in m["calibrated_scores"].values() if v is not None]
            raw_means.append(sum(valid_vals) / len(valid_vals) if valid_vals else 0.5)

        metric_offsets = {}
        for k in metric_keys:
            diffs = []
            for i, m in enumerate(self.models):
                score = m["calibrated_scores"].get(k)
                if score is not None:
                    diffs.append(score - raw_means[i])
            metric_offsets[k] = sum(diffs) / len(diffs) if diffs else 0.0

        debiased_theta = []
        for i, m in enumerate(self.models):
            adj_scores = []
            for k in metric_keys:
                score = m["calibrated_scores"].get(k)
                if score is not None:
                    adj_scores.append(score - metric_offsets[k])
            if adj_scores:
                debiased_theta.append(sum(adj_scores) / len(adj_scores))
            else:
                debiased_theta.append(raw_means[i])

        return debiased_theta

    def project_isotonic(
        self,
        theta: List[float],
        eps_margin: float = 0.0005,
        max_epochs: int = 150,
        tol: float = 1e-6
    ) -> List[float]:
        """Solve min sum_i (S_i - theta_i)^2 s.t.

        S_u >= S_v + eps_margin for all (u, v) in constraints
        using Dykstra's cyclic projection algorithm.
        """
        edges = []
        for u_name, v_name, _ in self.constraints:
            u_idx = self.name_to_idx.get(u_name)
            v_idx = self.name_to_idx.get(v_name)
            if u_idx is not None and v_idx is not None:
                edges.append((u_idx, v_idx))

        if not edges:
            return list(theta)

        s = list(theta)
        increments = [[0.0, 0.0] for _ in edges]
        self.converged_epochs = max_epochs

        for epoch in range(1, max_epochs + 1):
            s_old = list(s)
            for k, (u, v) in enumerate(edges):
                s[u] -= increments[k][0]
                s[v] -= increments[k][1]

                if s[u] - s[v] < eps_margin:
                    avg = 0.5 * (s[u] + s[v])
                    new_u = avg + 0.5 * eps_margin
                    new_v = avg - 0.5 * eps_margin
                else:
                    new_u = s[u]
                    new_v = s[v]

                inc_u = new_u - s[u]
                inc_v = new_v - s[v]
                increments[k][0] = inc_u
                increments[k][1] = inc_v

                s[u] = new_u
                s[v] = new_v

            max_s_change = max(abs(s[i] - s_old[i]) for i in range(len(s)))
            is_feasible = all(s[u] >= s[v] - 1e-6 for u, v in edges)
            if is_feasible and (max_s_change < tol or epoch >= 50):
                self.converged_epochs = epoch
                break

        return s

    def run_pipeline(self) -> dict:
        """Run the complete scoring pipeline and return detailed diagnostics."""
        initial_theta = self.compute_debiased_initial_ability()
        final_scores_raw = self.project_isotonic(initial_theta)

        min_s = min(final_scores_raw)
        max_s = max(final_scores_raw)
        scale = max_s - min_s if max_s > min_s else 1.0

        for i, m in enumerate(self.models):
            m["raw_composite_avg"] = sum(
                v for v in m["calibrated_scores"].values() if v is not None
            ) / m["valid_count"]
            m["debiased_ability"] = initial_theta[i]
            m["final_ability_raw"] = final_scores_raw[i]
            m["composite_ability"] = (final_scores_raw[i] - min_s) / scale
            m["composite_score_100"] = m["composite_ability"] * 100.0

        satisfied = 0
        violations = []
        for u_name, v_name, reason in self.constraints:
            u_idx = self.name_to_idx.get(u_name)
            v_idx = self.name_to_idx.get(v_name)
            if u_idx is not None and v_idx is not None:
                score_u = self.models[u_idx]["composite_ability"]
                score_v = self.models[v_idx]["composite_ability"]
                if score_u >= score_v - 1e-6:
                    satisfied += 1
                else:
                    violations.append({
                        "higher_model": u_name,
                        "lower_model": v_name,
                        "score_higher": score_u,
                        "score_lower": score_v,
                        "diff": score_u - score_v,
                        "reason": reason
                    })

        total_c = len(self.constraints)
        sat_rate = (satisfied / total_c * 100.0) if total_c > 0 else 100.0

        return {
            "total_models": len(self.models),
            "total_constraints": total_c,
            "satisfied_constraints": satisfied,
            "satisfaction_rate": sat_rate,
            "violations_count": len(violations),
            "violations": violations,
            "converged_epochs": self.converged_epochs,
        }


# ══════════════════════════════════════════════════════════════════════
# 7. Main Execution & CLI
# ══════════════════════════════════════════════════════════════════════

def run_hierarchy_analysis(tolerance: float = 1e-4) -> dict:
    """Execute complete end-to-end hierarchy analysis, calibration, and scoring."""
    print("=" * 70)
    print("1. Loading raw model data...")
    with open(RAW_DATA_FILE, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    print("2. Extracting 38 benchmark metrics across models...")
    models, metric_ranges = extract_benchmarks(raw_data, min_valid=3)
    print(f"   Evaluated {len(models)} models across {len(BENCHMARK_DEFS)} benchmarks.")

    print("3. Running leave-one-out dynamic calibration...")
    bounds, converged_round = calibrate_benchmark_bounds(models, metric_ranges, tolerance=tolerance)
    print(f"   Dynamic calibration converged at round {converged_round}!")

    print("4. Initializing Series Hierarchy Grids (Tiers x Versions)...")
    hierarchy_mgr = VendorHierarchyManager(all_models=models)
    hierarchy_mgr.export_all_csvs(overwrite_existing=False)
    print(f"   Exported / Loaded {len(hierarchy_mgr.grids)} series CSV grids to {hierarchy_mgr.hierarchy_dir}")

    print("5. Generating ordering constraints (Rules 1, 2, 3, 4)...")
    constraints, stats = generate_hierarchy_constraints(models, hierarchy_mgr)
    print(f"   Total unique constraints: {len(constraints)}")
    print(f"     - Rule 1 (Tier ordering):       {stats['rule1_tier']}")
    print(f"     - Rule 2 (Version ordering):    {stats['rule2_version']}")
    print(f"     - Rule 3 (Thinking ordering):   {stats['rule3_thinking']}")
    print(f"     - Rule 4 (Date ordering):       {stats['rule4_date']}")

    print("6. Computing debiased latent ability & running Dykstra Isotonic Projection...")
    engine = HierarchyScoreEngine(models, constraints)
    diag = engine.run_pipeline()

    print("\n" + "=" * 70)
    print("FINAL SCORECARD:")
    print(f"  Total Constraints:       {diag['total_constraints']}")
    print(f"  Satisfied Constraints:   {diag['satisfied_constraints']}")
    print(f"  Satisfaction Rate:       {diag['satisfaction_rate']:.2f}%")
    print(f"  Inversions / Violations: {diag['violations_count']}")
    print("=" * 70 + "\n")

    report_file = os.path.join(hierarchy_mgr.hierarchy_dir, "hierarchy_score_report.md")
    with open(report_file, "w", encoding="utf-8") as f:
        f.write("# Model Hierarchy & Monotonic Scoring Diagnostic Report\n\n")
        f.write(f"- **Total Evaluated Models**: {diag['total_models']}\n")
        f.write(f"- **Benchmarks Calibrated**: {len(BENCHMARK_DEFS)}\n")
        f.write(f"- **Calibration Rounds**: {converged_round}\n")
        f.write(f"- **Total Constraints Evaluated**: {diag['total_constraints']}\n")
        f.write(f"- **Satisfied Constraints**: {diag['satisfied_constraints']} ({diag['satisfaction_rate']:.2f}%)\n")
        f.write(f"- **Inversions / Violations**: {diag['violations_count']}\n\n")

        f.write("## Constraint Distribution by Rule\n")
        f.write(f"1. **Rule 1 (Tier Ordering within same series & version)**: {stats['rule1_tier']} constraints\n")
        f.write(f"2. **Rule 2 (Version Ordering within same series & tier)**: {stats['rule2_version']} constraints\n")
        f.write(f"3. **Rule 3 (Thinking Level Ordering within same model)**: {stats['rule3_thinking']} constraints\n")
        f.write(f"4. **Rule 4 (Date Snapshot Ordering within same model stem)**: {stats['rule4_date']} constraints\n\n")

        f.write("## Top 30 Models by Final Composite Score\n\n")
        f.write("| Rank | Model | Creator | Thinking | Final Score (100) | Raw Avg | Status |\n")
        f.write("|---|---|---|---|---|---|---|\n")
        sorted_models = sorted(models, key=lambda x: -x["composite_ability"])
        for rk, m in enumerate(sorted_models[:30], 1):
            f.write(f"| {rk} | `{m['name']}` | {m['creator']} | {m['thinking_tag']} | "
                    f"**{m['composite_score_100']:.2f}** | {m['raw_composite_avg']:.4f} | PASS |\n")

    json_results_file = os.path.join(OUTPUT_DIR, "hierarchy_analysis_results.json")
    with open(json_results_file, "w", encoding="utf-8") as f:
        json.dump({
            "diagnostics": diag,
            "benchmark_bounds": bounds,
            "models": [{
                "name": m["name"],
                "creator": m["creator"],
                "base_name": m["base_name"],
                "thinking_tag": m["thinking_tag"],
                "thinking_level": m["thinking_level"],
                "composite_ability": m["composite_ability"],
                "composite_score_100": m["composite_score_100"],
                "raw_composite_avg": m["raw_composite_avg"],
                "valid_count": m["valid_count"],
            } for m in sorted_models]
        }, f, indent=2, ensure_ascii=False)

    print(f"Results written to:\n  - {report_file}\n  - {json_results_file}")
    return diag


def main():
    parser = argparse.ArgumentParser(description="Model Hierarchy Scoring & CSV Diagnostic Engine")
    parser.add_argument("--tolerance", type=float, default=1e-4, help="Calibration convergence tolerance")
    parser.add_argument("--export-csv", action="store_true", help="Force re-export all CSV hierarchy templates from defaults")
    parser.add_argument("--diff", type=str, nargs="?", const="all", help="Show differences between active CSV grids and default templates (pass vendor or series name, or omit for all)")
    args = parser.parse_args()

    if args.diff:
        mgr = VendorHierarchyManager()
        targets = [args.diff] if args.diff != "all" else list(DEFAULT_SERIES_GRIDS.keys())
        has_diff = False
        for t in targets:
            diffs = mgr.diff_with_default(t)
            if diffs:
                print(f"\n=== Hierarchy Diffs for {t} ===")
                for d in diffs:
                    print(f"  * {d}")
                has_diff = True
        if not has_diff:
            print("All inspected vendor / series CSV grids match default curated templates.")
        return

    if args.export_csv:
        with open(RAW_DATA_FILE, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
        models, _ = extract_benchmarks(raw_data)
        mgr = VendorHierarchyManager(all_models=models, load_from_disk=False)
        mgr.export_all_csvs(overwrite_existing=True)
        print(f"Exported {len(mgr.grids)} series hierarchy CSVs to {mgr.hierarchy_dir}")
        return

    run_hierarchy_analysis(tolerance=args.tolerance)


if __name__ == "__main__":
    main()
