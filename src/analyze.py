#!/usr/bin/env python3
"""
Scoring system and Pareto analysis for Artificial Analysis LLM Leaderboard.

**Version 9**: Per-request cost computed from the user-supplied formula:

    cost = (CacheHitRate * CacheHitPrice * InputTokens)
         + ((1 - CacheHitRate) * CacheWritePrice * InputTokens)
         + (SpeedMedian * RealTime * OutputPrice)

Where:
  - CacheHitRate    = global average scraped from
                      https://artificialanalysis.ai/agents/coding-agents
                      (mean of cacheHitRate across all model-agent combos;
                      see src/cache_hit_rate.py)
  - CacheHitPrice   = AA's `cacheHitPrice` (USD per 1M tokens)
  - CacheWritePrice = AA's `cacheWritePrice`. If missing, falls back to
                      `price1mInputTokens` (the regular input price).
  - InputTokens     = 10,000 (the AA default 10k input-token workload;
                      see https://artificialanalysis.ai/methodology/performance-benchmarking)
  - SpeedMedian     = AA's `medianOutputTokensPerSecond` (tokens/sec,
                      measured at the 10k input-token workload)
  - OutputPrice     = AA's `price1mOutputTokens` (USD per 1M tokens)
  - RealTime        = If ReasoningTime exists (non-null, non-'--'):
                        EndToEndResponseTimeTotal - LatencyFirstChunk
                          = medianEndToEndResponseTimeSeconds
                            - medianTimeToFirstTokenSeconds
                      If ReasoningTime is '--' (null):
                        EndToEndResponseTimeTotal
                          = medianEndToEndResponseTimeSeconds

The formula is applied as-is, with no unit conversion. Because AA prices are
in USD per 1M tokens while token counts are raw integers, the resulting cost
is a relative score (~$1k–$100k scale) used only for Pareto comparison and
linear normalization. This is intentional per the user's spec.

Data source: AA's Next.js RSC payload (~500 models × 93 fields)
"""

import json
import os
import sys
from collections import Counter
from fractions import Fraction

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# ══════════════════════════════════════════════════════════════════════
# Font setup
# ══════════════════════════════════════════════════════════════════════
_HEITI_FONTS = [
    # Noto Sans CJK SC 路径
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/truetype/noto/NotoSansSC-Regular.ttf",
    "/usr/share/fonts/truetype/noto/NotoSansSC-Bold.ttf",
    "/usr/share/fonts/truetype/chinese/SarasaMonoSC-Bold.ttf",
    "/usr/share/fonts/truetype/chinese/SarasaMonoSC-SemiBold.ttf",
    "/usr/share/fonts/truetype/chinese/SarasaMonoSC-Regular.ttf",
    # CI runner: Noto Serif SC (installed by .github/workflows/update-leaderboard.yml)
    "/usr/share/fonts/truetype/noto-serif-sc/NotoSerifSC-Regular.otf",
    "/usr/share/fonts/truetype/noto-serif-sc/NotoSerifSC-Regular.ttf",
]
_LATIN = ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]
for fp in _HEITI_FONTS:
    if os.path.exists(fp):
        try:
            fm.fontManager.addfont(fp)
        except Exception:
            pass
for fp in _LATIN:
    if os.path.exists(fp):
        try:
            fm.fontManager.addfont(fp)
        except Exception:
            pass
# 将 Noto Sans CJK SC 置于首选
plt.rcParams["font.sans-serif"] = ["Noto Sans CJK SC", "Sarasa Mono SC", "Noto Serif SC", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

# ── Paths ──
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
RAW_DATA_FILE = os.path.join(OUTPUT_DIR, "raw_data.json")
CACHE_HIT_RATE_FILE = os.path.join(OUTPUT_DIR, "cache_hit_rate.json")

# ── Cost-formula constants ──
# AA's default speed/latency workload is the 10k input-token prompt
# (see https://artificialanalysis.ai/methodology/performance-benchmarking).
# This is the InputTokens value used in the per-request cost formula.
INPUT_TOKENS_DEFAULT = 10_000

# ── Metrics (from AA's evaluation data) ──
# Maps our internal key → AA's field name in the RSC payload
METRIC_FIELDS = {
    "intelligenceIndex": "intelligenceIndex",
    "agenticIndex": "agenticIndex",
    "codingIndex": "codingIndex",
    "gpqa": "gpqa",
    "hle": "hle",
    "mmmuPro": "mmmuPro",
    "ifbench": "ifbench",
    "scicode": "scicode",
    "critpt": "critpt",
    "lcr": "lcr",
    "tau2": "tau2",
    "terminalbenchHard": "terminalbenchHard",
    "omniscience": "omniscience",
    "omniscienceAccuracy": "omniscienceAccuracy",
    "omniscienceNonHallucination": "omniscienceNonHallucination",
    "apexAgents": "apexAgents",
    "itbenchSre": "itbenchSre",
    "gdpvalNormalized": "gdpvalNormalized",
}

METRIC_LABELS = {
    "intelligenceIndex": "AA Intelligence Index",
    "agenticIndex": "AA Agentic Index",
    "codingIndex": "AA Coding Index",
    "gpqa": "GPQA Diamond",
    "hle": "Humanity's Last Exam",
    "mmmuPro": "MMMU Pro",
    "ifbench": "IFBench Instruction Following",
    "scicode": "SciCode Coding",
    "critpt": "CritPt Physics",
    "lcr": "AA-LCR Long Context",
    "tau2": "τ²-Bench Telecom",
    "terminalbenchHard": "Terminal-Bench Hard",
    "omniscience": "AA Omniscience Index",
    "omniscienceAccuracy": "AA-Omniscience Accuracy",
    "omniscienceNonHallucination": "AA-Omniscience Non-Hallucination",
    "apexAgents": "APEX-Agents-AA",
    "itbenchSre": "ITBench-SRE",
    "gdpvalNormalized": "GDPval-AA Normalized",
}

MIN_VALID_METRICS = 5


# ══════════════════════════════════════════════════════════════════════
# Data Loading & Computation
# ══════════════════════════════════════════════════════════════════════

def load_data():
    with open(RAW_DATA_FILE, encoding="utf-8") as f:
        return json.load(f)


def compute_scores(data):
    """Compute composite ability and extract AA's measured cost."""
    models = []
    for d in data:
        # Skip deprecated models
        if d.get("deprecated", False):
            continue

        m = {
            "model": d.get("name", "Unknown"),
            "slug": d.get("slug", ""),
            "is_reasoning": bool(d.get("reasoningModel", False)),
            "creator": d.get("modelCreatorName", ""),
            "context_window": d.get("contextWindowTokens"),
            "is_open_weights": d.get("isOpenWeights", False),
            # Pricing (direct from AA, USD per 1M tokens)
            "input_price": _to_frac(d.get("price1mInputTokens")),
            "output_price": _to_frac(d.get("price1mOutputTokens")),
            "cache_hit_price": _to_frac(d.get("cacheHitPrice")),
            "cache_write_price": _to_frac(d.get("cacheWritePrice")),
            "blended_price_721": _to_frac(d.get("price1mBlended7To2To1")),
            # AA's measured Intelligence Index cost (kept for reference / debugging)
            "intelligence_index_cost_total": _to_frac(d.get("intelligenceIndexCostTotal")),
            "intelligence_index_cost_input": _to_frac(d.get("intelligenceIndexCostInput")),
            "intelligence_index_cost_output": _to_frac(d.get("intelligenceIndexCostOutput")),
            "intelligence_index_cost_reasoning": _to_frac(d.get("intelligenceIndexCostReasoning")),
            "intelligence_index_cost_answer": _to_frac(d.get("intelligenceIndexCostAnswer")),
            # Speed / latency data (all measured at the 10k input-token workload)
            "speed": _to_frac(d.get("medianOutputTokensPerSecond")),
            "ttft": _to_frac(d.get("medianTimeToFirstTokenSeconds")),         # Latency First Chunk
            "total_response": _to_frac(d.get("medianEndToEndResponseTimeSeconds")),  # E2E Total
            "reasoning_time": _to_frac(d.get("medianReasoningTimeSeconds")),  # None for non-reasoning
            # Intelligence Index
            "intelligence_index": _to_frac(d.get("intelligenceIndex")),
            # Token counts
            "token_counts": d.get("intelligenceIndexTokenCounts"),
            "_parsed": {},
        }

        # Parse evaluation metrics
        for key, aa_field in METRIC_FIELDS.items():
            val = d.get(aa_field)
            m["_parsed"][key] = _to_frac(val)

        models.append(m)

    print(f"Models loaded (excluding deprecated): {len(models)}")
    print(f"  Reasoning models: {sum(1 for m in models if m['is_reasoning'])}")
    print(f"  Non-reasoning models: {sum(1 for m in models if not m['is_reasoning'])}")
    print(f"  With input_price:        {sum(1 for m in models if m['input_price'] is not None)}")
    print(f"  With output_price:       {sum(1 for m in models if m['output_price'] is not None)}")
    print(f"  With cache_hit_price:    {sum(1 for m in models if m['cache_hit_price'] is not None)}")
    print(f"  With cache_write_price:  {sum(1 for m in models if m['cache_write_price'] is not None)}")
    print(f"  With speed:              {sum(1 for m in models if m['speed'] is not None)}")
    print(f"  With ttft:               {sum(1 for m in models if m['ttft'] is not None)}")
    print(f"  With total_response:     {sum(1 for m in models if m['total_response'] is not None)}")
    print(f"  With reasoning_time:     {sum(1 for m in models if m['reasoning_time'] is not None)}")

    # ── Metric ranges (Fraction) ──
    metric_ranges = {}
    for key in METRIC_FIELDS:
        vals = [m["_parsed"][key] for m in models if m["_parsed"][key] is not None]
        if len(vals) >= 2:
            metric_ranges[key] = {"min": min(vals), "max": max(vals), "count": len(vals)}
        else:
            metric_ranges[key] = None

    # ── Normalize metrics ──
    for m in models:
        m["_norm"] = {}
        for key in METRIC_FIELDS:
            val = m["_parsed"][key]
            rng = metric_ranges.get(key)
            if val is None or rng is None:
                m["_norm"][key] = None
            elif rng["max"] == rng["min"]:
                m["_norm"][key] = Fraction(1, 2)
            else:
                m["_norm"][key] = (val - rng["min"]) / (rng["max"] - rng["min"])

    # ── Composite ability = exact Fraction mean ──
    for m in models:
        nv = [v for v in m["_norm"].values() if v is not None]
        m["composite_ability"] = sum(nv) / len(nv) if nv else None
        m["valid_metrics"] = len(nv)

    # Quality filter
    valid = [m for m in models
             if m["composite_ability"] is not None and m["valid_metrics"] >= MIN_VALID_METRICS]
    print(f"Models with ≥{MIN_VALID_METRICS} metrics: {len(valid)}")

    # ── Compute per-request cost via the user-supplied formula ──
    # cost = (CacheHitRate * CacheHitPrice * InputTokens)
    #      + ((1 - CacheHitRate) * CacheWritePrice * InputTokens)
    #      + (Speed * RealTime * OutputPrice)
    # where CacheWritePrice falls back to InputPrice when missing, and
    # RealTime = (E2E - TTFT) if ReasoningTime exists, else E2E.
    cache_hit_rate = _load_cache_hit_rate()
    print(f"\n  Global Cache Hit Rate (from coding-agents page): {cache_hit_rate:.6f}")
    print(f"  Input tokens (10k workload default): {INPUT_TOKENS_DEFAULT}")

    chr_frac = Fraction(cache_hit_rate).limit_denominator(10**12)
    input_tokens = Fraction(INPUT_TOKENS_DEFAULT)
    priced_count_breakdown = {"total": 0, "priced": 0, "missing_input_price": 0,
                               "missing_output_price": 0, "missing_speed": 0,
                               "missing_e2e": 0}
    for m in valid:
        priced_count_breakdown["total"] += 1
        cost, breakdown = _compute_formula_cost(m, chr_frac, input_tokens)
        m["per_request_cost"] = cost
        m["cost_breakdown"] = breakdown
        if cost is not None:
            priced_count_breakdown["priced"] += 1
        else:
            if m["input_price"] is None:
                priced_count_breakdown["missing_input_price"] += 1
            if m["output_price"] is None:
                priced_count_breakdown["missing_output_price"] += 1
            if m["speed"] is None:
                priced_count_breakdown["missing_speed"] += 1
            if m["total_response"] is None:
                priced_count_breakdown["missing_e2e"] += 1
    print(f"  Models with computable cost: {priced_count_breakdown['priced']}/{priced_count_breakdown['total']}")
    print(f"    Missing input_price:  {priced_count_breakdown['missing_input_price']}")
    print(f"    Missing output_price: {priced_count_breakdown['missing_output_price']}")
    print(f"    Missing speed:        {priced_count_breakdown['missing_speed']}")
    print(f"    Missing e2e total:    {priced_count_breakdown['missing_e2e']}")

    # ── Normalize cost (linear, Pareto max = 1) ──
    priced = [m for m in valid if m.get("per_request_cost") is not None and m["per_request_cost"] > 0]
    if priced:
        # Compute a preliminary Pareto to find the max cost on the frontier
        sorted_priced = sorted(priced, key=lambda m: (m["per_request_cost"], -m["composite_ability"]))
        prelim_frontier = []
        for m in sorted_priced:
            if any(_dominates(o, m) for o in prelim_frontier):
                continue
            prelim_frontier = [p for p in prelim_frontier if not _dominates(m, p)]
            prelim_frontier.append(m)

        # Max cost on the Pareto frontier is the normalization ceiling
        if prelim_frontier:
            max_pareto_cost = max(m["per_request_cost"] for m in prelim_frontier)
        else:
            max_pareto_cost = max(m["per_request_cost"] for m in priced)

        print(f"Formula cost range: {float(min(m['per_request_cost'] for m in priced)):.4f} – {float(max(m['per_request_cost'] for m in priced)):.4f}")
        print(f"Max Pareto frontier cost (normalization ceiling): {float(max_pareto_cost):.4f}")

        for m in priced:
            if max_pareto_cost > 0:
                m["normalized_cost"] = m["per_request_cost"] / max_pareto_cost
            else:
                m["normalized_cost"] = Fraction(1, 2)
    for m in valid:
        if "normalized_cost" not in m:
            m["normalized_cost"] = None

    return valid, metric_ranges


def _to_frac(val):
    """Convert a numeric value to Fraction, or None if null/invalid."""
    if val is None:
        return None
    try:
        return Fraction(val).limit_denominator(10**12)
    except (ValueError, TypeError, ZeroDivisionError):
        return None


# ══════════════════════════════════════════════════════════════════════
# Cost-formula helpers
# ══════════════════════════════════════════════════════════════════════

def _load_cache_hit_rate():
    """Load the global average Cache Hit Rate scraped from the AA coding-agents page.

    Falls back to a sensible default if the scrape output is missing, but emits
    a loud warning — the user should run `python src/cache_hit_rate.py` first.
    """
    if not os.path.exists(CACHE_HIT_RATE_FILE):
        print(f"\n  WARNING: {CACHE_HIT_RATE_FILE} not found.")
        print(f"           Run `python src/cache_hit_rate.py` to scrape the value from")
        print(f"           https://artificialanalysis.ai/agents/coding-agents first.")
        print(f"           Falling back to a placeholder value of 0.50 — results will be WRONG.")
        return 0.50
    with open(CACHE_HIT_RATE_FILE, encoding="utf-8") as f:
        data = json.load(f)
    chr_value = data.get("cache_hit_rate")
    if chr_value is None:
        print(f"\n  WARNING: cache_hit_rate.json has no `cache_hit_rate` field. Using 0.50.")
        return 0.50
    print(f"\n  Loaded cache_hit_rate.json: {chr_value:.6f} "
          f"(from {data.get('valid_count', '?')} valid combinations "
          f"out of {data.get('total_count', '?')} total)")
    return float(chr_value)


def _compute_formula_cost(m, cache_hit_rate, input_tokens):
    """Compute per-request cost using the user-supplied formula.

        cost = (CacheHitRate * CacheHitPrice * InputTokens)
             + ((1 - CacheHitRate) * CacheWritePrice * InputTokens)
             + (Speed * RealTime * OutputPrice)

    Returns (cost, breakdown_dict). cost is None if required fields are missing.
    All math is done with Fraction for exactness.

    Required fields:
      - input_price  (fallback for cache_write_price; also needed if cache_hit_price is None)
      - output_price
      - speed
      - total_response (E2E)
      - ttft (only when reasoning_time is not None)
    """
    # ── Resolve cache hit price ──
    # If cache_hit_price is missing, the cache-hit term cannot be computed.
    cache_hit_price = m.get("cache_hit_price")
    # ── Resolve cache write price (fallback to input price) ──
    cache_write_price = m.get("cache_write_price")
    cache_write_source = "cacheWritePrice"
    if cache_write_price is None:
        cache_write_price = m.get("input_price")
        cache_write_source = "inputPrice (fallback)"

    # ── Resolve output price ──
    output_price = m.get("output_price")

    # ── Resolve speed ──
    speed = m.get("speed")

    # ── Resolve E2E total ──
    e2e_total = m.get("total_response")

    # ── Resolve TTFT (Latency First Chunk) ──
    ttft = m.get("ttft")

    # ── Determine RealTime based on reasoning_time ──
    reasoning_time = m.get("reasoning_time")
    has_reasoning = reasoning_time is not None
    if has_reasoning:
        # RealTime = E2E Total - Latency First Chunk
        if e2e_total is None or ttft is None:
            real_time = None
            real_time_source = "E2E - TTFT (missing data)"
        else:
            real_time = e2e_total - ttft
            real_time_source = "E2E_total - TTFT (reasoning model)"
    else:
        # ReasoningTime is '--' (None) → RealTime = E2E Total
        real_time = e2e_total
        real_time_source = "E2E_total (non-reasoning)"

    # ── Check required fields for the formula ──
    # cache_hit_price can be None — we'll treat that term as 0 (no cache hit discount)
    # but we still need cache_write_price (or its input_price fallback), output_price,
    # speed, and real_time.
    missing = []
    if cache_write_price is None:
        missing.append("cache_write_price (and input_price fallback)")
    if output_price is None:
        missing.append("output_price")
    if speed is None:
        missing.append("speed")
    if real_time is None:
        missing.append("real_time")

    if missing:
        return None, {
            "computed": False,
            "reason": f"missing required fields: {', '.join(missing)}",
            "cache_hit_rate": float(cache_hit_rate),
            "input_tokens": int(input_tokens),
            "cache_hit_price": _frac_to_float(cache_hit_price),
            "cache_write_price": _frac_to_float(cache_write_price),
            "cache_write_source": cache_write_source,
            "output_price": _frac_to_float(output_price),
            "speed": _frac_to_float(speed),
            "e2e_total": _frac_to_float(e2e_total),
            "ttft": _frac_to_float(ttft),
            "reasoning_time": _frac_to_float(reasoning_time),
            "has_reasoning": has_reasoning,
            "real_time": _frac_to_float(real_time),
            "real_time_source": real_time_source,
        }

    # ── Compute the three terms ──
    # Term 1: cache-hit input cost (only if cache_hit_price is available)
    if cache_hit_price is not None:
        term1 = cache_hit_rate * cache_hit_price * input_tokens
    else:
        term1 = Fraction(0)
    # Term 2: cache-miss (or cache-write) input cost
    term2 = (Fraction(1) - cache_hit_rate) * cache_write_price * input_tokens
    # Term 3: output cost = speed * real_time * output_price
    term3 = speed * real_time * output_price

    cost = term1 + term2 + term3

    return cost, {
        "computed": True,
        "cache_hit_rate": float(cache_hit_rate),
        "input_tokens": int(input_tokens),
        "cache_hit_price": _frac_to_float(cache_hit_price),
        "cache_write_price": _frac_to_float(cache_write_price),
        "cache_write_source": cache_write_source,
        "output_price": _frac_to_float(output_price),
        "speed": _frac_to_float(speed),
        "e2e_total": _frac_to_float(e2e_total),
        "ttft": _frac_to_float(ttft),
        "reasoning_time": _frac_to_float(reasoning_time),
        "has_reasoning": has_reasoning,
        "real_time": _frac_to_float(real_time),
        "real_time_source": real_time_source,
        "term1_cache_hit_input": float(term1),
        "term2_cache_miss_input": float(term2),
        "term3_output": float(term3),
        "total_cost": float(cost),
    }


def _frac_to_float(v):
    """Fraction → float, or None."""
    if v is None:
        return None
    if isinstance(v, Fraction):
        return float(v)
    return v


# ══════════════════════════════════════════════════════════════════════
# Plot Models Filter
# ══════════════════════════════════════════════════════════════════════

def get_plot_models(models):
    """Filter models that have valid normalized_cost for plotting."""
    plot_models = [m for m in models if m.get("normalized_cost") is not None]
    print(f"\n  {len(plot_models)} models with valid cost data for plotting")
    return plot_models


# ══════════════════════════════════════════════════════════════════════
# Pareto frontier computation
# ══════════════════════════════════════════════════════════════════════

def compute_pareto(models):
    """Pareto frontier based on Intelligence Index cost vs composite ability."""
    priced = [m for m in models if m.get("per_request_cost") is not None and m["per_request_cost"] > 0]
    sorted_m = sorted(priced, key=lambda m: (m["per_request_cost"], -m["composite_ability"]))
    frontier = []
    for m in sorted_m:
        if any(_dominates(o, m) for o in frontier):
            continue
        frontier = [p for p in frontier if not _dominates(m, p)]
        frontier.append(m)
    frontier.sort(key=lambda m: m["composite_ability"], reverse=True)
    return frontier


def _dominates(a, b):
    return (a["composite_ability"] >= b["composite_ability"]
            and a["per_request_cost"] <= b["per_request_cost"]
            and (a["composite_ability"] > b["composite_ability"]
                 or a["per_request_cost"] < b["per_request_cost"]))


# ══════════════════════════════════════════════════════════════════════
# Visualization
# ══════════════════════════════════════════════════════════════════════

def plot_analysis(models, pareto):
    """Generate the Pareto scatter plot."""
    plot_models = [m for m in models if m.get("per_request_cost") is not None]
    pareto_names = {m["model"] for m in pareto}
    others = [m for m in plot_models if m["model"] not in pareto_names]

    # ── 固定画布：12x12 (1:1)，坐标轴(白框)位置每次完全一致 ─────────────
    fig = plt.figure(figsize=(12, 12), facecolor="#000000")
    ax = fig.add_axes([0.09, 0.13, 0.71, 0.71], facecolor="#000000")
    ax.set_aspect('equal', adjustable='box')

    # Boundary lines
    ax.plot([0, 1], [0, 0], color='#FFFFFF', linewidth=1.5, zorder=1)
    ax.plot([0, 0], [0, 1], color='#FFFFFF', linewidth=1.5, zorder=1)
    ax.plot([0, 1], [1, 1], color='#FFFFFF', linewidth=1.5, zorder=1)
    ax.plot([1, 1], [0, 1], color='#FFFFFF', linewidth=1.5, zorder=1)

    # Grid
    for v in [i / 10 for i in range(1, 10)]:
        ax.plot([0, 1], [v, v], color='#333333', alpha=0.5, linewidth=0.4, zorder=0)
        ax.plot([v, v], [0, 1], color='#333333', alpha=0.5, linewidth=0.4, zorder=0)

    # Scatter: other models (zorder=2, 可被帕累托点遮挡)
    ax.scatter(
        [float(m["normalized_cost"]) for m in others],
        [float(m["composite_ability"]) for m in others],
        c="#4A4A4A", s=20, alpha=0.45, zorder=2,
    )

    # Scatter: Pareto frontier (zorder=4, 点之间允许重叠)
    ax.scatter(
        [float(m["normalized_cost"]) for m in pareto],
        [float(m["composite_ability"]) for m in pareto],
        c="#00E5FF", s=100, alpha=0.95, zorder=4,
        edgecolors="#FFFFFF", linewidth=1.2,
    )

    # Pareto frontier line
    pf = sorted(pareto, key=lambda m: m["normalized_cost"])
    ax.plot(
        [float(m["normalized_cost"]) for m in pf],
        [float(m["composite_ability"]) for m in pf],
        c="#00E5FF", linewidth=2.0, alpha=0.35, zorder=3, linestyle="--",
    )

    ax.set_xlabel("归一化单请求成本 (0=免费, 1=最贵帕累托模型)",
                  fontsize=14, color="#FFFFFF", labelpad=12, fontweight="bold")
    ax.set_ylabel("综合能力 (0=最低, 1=最高)",
                  fontsize=14, color="#FFFFFF", labelpad=12, fontweight="bold")
    ax.set_title(
        "LLM 综合能力 vs 单请求成本 — Pareto前沿\n"
        "（成本 = 公式估算 | X轴线性归一化坐标）",
        fontsize=16, color="#FFFFFF", fontweight="bold", pad=18,
    )
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])
    ax.set_xticklabels(["0", "1"], color="#FFFFFF", fontsize=12, fontweight="bold")
    ax.set_yticklabels(["0", "1"], color="#FFFFFF", fontsize=12, fontweight="bold")
    margin = 0.05
    ax.set_xlim(-margin, 1 + margin)
    ax.set_ylim(-margin, 1 + margin)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.grid(False)
    ax.tick_params(axis='both', colors='#FFFFFF', length=5, width=1.2)

    # ── 图例：放在绘图区外的右侧留白，绝不遮挡白框/数据/标签 ─────────────
    from matplotlib.lines import Line2D
    handles = [
        Line2D([0], [0], marker='o', color='none', markerfacecolor='#4A4A4A',
               markersize=7, alpha=0.6),
        Line2D([0], [0], marker='o', color='none', markerfacecolor='#00E5FF',
               markeredgecolor='#FFFFFF', markersize=9),
    ]
    fig.legend(handles, [f"其他模型 ({len(others)})", f"Pareto前沿 ({len(pareto)})"],
               loc='center right', bbox_to_anchor=(0.995, 0.5),
               fontsize=11, framealpha=0.9, edgecolor="#FFFFFF",
               facecolor="#1A1A1A", labelcolor="#FFFFFF", borderpad=1)

    # 底部说明文字（移到画布底部留白，不占定义域）
    method = (
        f"X轴: 公式估算单请求成本(线性归一化) | Y轴: 综合能力(18指标均值) | "
        f"★ 成本 = CacheHit·CacheHitPrice + (1-CacheHit)·CacheWritePrice + Speed·RealTime·OutputPrice | 共{len(plot_models)}模型"
    )
    fig.text(0.445, 0.02, method, ha="center", va="bottom", fontsize=6.5,
             color="#AAAAAA", style="italic")

    # ── 标签确定性布局：只允许 正右/正左/正上/正下（水平或垂直偏移）─────────
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    dpi = fig.dpi
    ax_box = ax.get_window_extent(renderer)
    dots = [ax.transData.transform((float(m["normalized_cost"]),
                                    float(m["composite_ability"]))) for m in pf]
    R = 16.0      # 圆点半径(px)
    GAP = 10.0    # 标签与圆点间隙(px)
    M = 4.0       # 标签间安全边距(px)

    # 先测量每个标签文本框尺寸
    sizes = []
    tmps = []
    for i, m in enumerate(pf):
        t = ax.annotate(f"{i+1}. {m['model']}", xy=dots[i],
                        xytext=(0, 0), textcoords='offset points', fontsize=9,
                        bbox=dict(boxstyle="round,pad=0.15", facecolor="#1A1A1A"))
        tmps.append(t)
    fig.canvas.draw()
    for t in tmps:
        e = t.get_bbox_patch().get_window_extent(renderer)
        sizes.append((e.width, e.height))
    for t in tmps:
        t.remove()

    def box_at(i, dx, dy, ha, va):
        W, H = sizes[i]
        x, y = dots[i][0] + dx, dots[i][1] + dy
        x0 = x if ha == 'left' else (x - W if ha == 'right' else x - W / 2)
        y0 = (y - H / 2) if va == 'center' else (y if va == 'bottom' else y - H)
        return (x0, y0, x0 + W, y0 + H)

    def hits(a, b, m=M):
        return a[0] - m < b[2] and b[0] - m < a[2] and a[1] - m < b[3] and b[1] - m < a[3]

    placed, chosen = [], []
    for i in range(len(pf)):
        W, H = sizes[i]
        dx0, dy = dots[i][0], dots[i][1]
        cands = [(R + GAP, 0, 'left', 'center', False)]          # 正右
        xf = R + GAP                                              # 正右(更远,错开)
        for b in placed:
            if b[1] < dy + H / 2 and b[3] > dy - H / 2:
                xf = max(xf, b[2] + GAP - (dx0))
        cands.append((xf, 0, 'left', 'center', False))
        cands += [(-(R + GAP), 0, 'right', 'center', False),      # 正左
                  (0, R + GAP, 'center', 'bottom', False),        # 正上
                  (0, -(R + GAP), 'center', 'top', False)]        # 正下
        for k in range(1, 8):                                     # 正右+垂直错行(肘形连线)
            cands.append((R + GAP, -k * (H + GAP), 'left', 'center', True))
            cands.append((R + GAP, k * (H + GAP), 'left', 'center', True))

        sel = None
        for dx, dyo, ha, va, elbow in cands:
            b = box_at(i, dx, dyo, ha, va)
            if not (ax_box.x0 <= b[0] and b[2] <= ax_box.x1 and
                    ax_box.y0 <= b[1] and b[3] <= ax_box.y1):
                continue                                          # 出界
            if any(hits(b, p) for p in placed):
                continue                                          # 压到别的标签
            if any(hits(b, (d[0]-R, d[1]-R, d[0]+R, d[1]+R), 2)
                   for k, d in enumerate(dots) if k != i):
                continue                                          # 压到帕累托圆点
            if not elbow:                                         # 直连线不能穿过其它圆点
                seg_ok = True
                for k, d in enumerate(dots):
                    if k == i:
                        continue
                    if abs(d[1] - dy) < R + 2 and min(dx0, dx0 + dx) < d[0] < max(dx0, dx0 + dx):
                        seg_ok = False
# ── 标签布局：分界点前全水平、分界点后全垂直；高度排名=能力排名 ──────
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    ax_box = ax.get_window_extent(renderer)
    L, Rt, B, T = ax_box.x0, ax_box.x1, ax_box.y0, ax_box.y1
    pts = [(float(m["normalized_cost"]), float(m["composite_ability"])) for m in pf]
    dots = [ax.transData.transform(p) for p in pts]
    inv = ax.transData.inverted()
    R, GAP, M = 16.0, 16.0, 4.0

    # 测量标签框尺寸
    tmps = [ax.annotate(f"{i+1}. {m['model']}", xy=pts[i], xytext=(0, 0),
                        textcoords='offset points', fontsize=9,
                        bbox=dict(boxstyle="round,pad=0.15", facecolor="#1A1A1A"))
            for i, m in enumerate(pf)]
    fig.canvas.draw()
    sizes = []
    for t in tmps:
        e = t.get_bbox_patch().get_window_extent(renderer)
        sizes.append((e.width, e.height))
    for t in tmps:
        t.remove()

    # 分界点：第一个"与相邻前沿点连线最大斜率 ≤ 1"的模型；之前全水平、之后全垂直
    n = len(pf)
    split = n
    for i in range(n):
        sp = (pts[i][1]-pts[i-1][1]) / max(pts[i][0]-pts[i-1][0], 1e-9) if i > 0 else 1e9
        sn = (pts[i+1][1]-pts[i][1]) / max(pts[i+1][0]-pts[i][0], 1e-9) if i < n-1 else 1e9
        if max(sp, sn) <= 1.0:
            split = i
            break
    horiz = [i < split for i in range(n)]

    def _hit(a, b, m=M):
        return a[0]-m < b[2] and b[0]-m < a[2] and a[1]-m < b[3] and b[1]-m < a[3]

    def covers_dot(b, i):
        for k, d in enumerate(dots):
            if k != i and b[0]-2 < d[0] < b[2]+2 and b[1]-2 < d[1] < b[3]+2:
                return k
        return -1

    def fix_x(b, i, dx, placed_list):
        """水平平移：不压其他前沿点、不压已放标签、圆点保持在框正下/正上、不超定义域"""
        W = b[2]-b[0]
        cands = [b[0]]
        for k, d in enumerate(dots):
            if k != i and b[1]-2 < d[1] < b[3]+2:
                cands += [d[0]+R+GAP, d[0]-R-GAP-W]
        for x0 in cands:
            if x0 < L or x0+W > Rt or not (x0 <= dx <= x0+W):
                continue
            nb = (x0, b[1], x0+W, b[3])
            if covers_dot(nb, i) < 0 and not any(_hit(nb, p) for p in placed_list):
                return nb
        return None

    # 修复点：改为列表，避免遍历字典键导致的 TypeError
    placed_boxes = []
    result = {}

    # ── 垂直组：按能力 低→高 向上堆叠，全部置于圆点上方 → 高度排名=能力排名 ──
    vert_idx = sorted([i for i in range(n) if not horiz[i]], key=lambda i: pts[i][1])
    chain = None
    for i in vert_idx:
        W, H = sizes[i]
        dx, dy = dots[i]
        y0 = dy + R + GAP                      # 至少在自己圆点上方
        if chain is not None:
            y0 = max(y0, chain)                # 且必须高于所有更低能力者的标签
        if y0 + H > T:                         # 顶到定义域上限则下移(连线仍垂直)
            y0 = T - H
        x1 = min(dx + W/2, Rt)                 # 靠右出界时左移
        x0 = max(x1 - W, L)
        nb = fix_x((x0, y0, x0+W, y0+H), i, dx, placed_boxes)
        if nb is None:
            nb = (x0, y0, x0+W, y0+H)
        result[i] = ('v', nb)
        placed_boxes.append(nb)
        chain = nb[3] + M

    # ── 水平组：正右；冲突只向右错开，绝不向左出界 ──
    hor_idx = sorted([i for i in range(n) if horiz[i]], key=lambda i: -pts[i][1])
    for i in hor_idx:
        W, H = sizes[i]
        dx, dy = dots[i]
        x0 = dx + R + GAP
        for _ in range(25):
            b = (x0, dy-H/2, x0+W, dy+H/2)
            if b[2] > Rt:
                break
            push = None
            # 修复点：直接遍历列表中的元组
            for p in placed_boxes:
                if _hit(b, p):
                    push = max(push or 0, p[2]+GAP)
            k = covers_dot(b, i)
            if k >= 0:
                push = max(push or 0, dots[k][0]+R+GAP)
            if push is None:
                break
            x0 = push
        x0 = min(x0, Rt-W)
        b = (x0, dy-H/2, x0+W, dy+H/2)
        result[i] = ('h', b)
        placed_boxes.append(b)

    # ── 绘制：标签 zorder=5；连线 zorder=6(更高，可压别人标签、便于辨认归属) ──
    for i, m in enumerate(pf):
        kind, b = result[i]
        cx, cy = inv.transform(((b[0]+b[2])/2, (b[1]+b[3])/2))
        ax.text(cx, cy, f"{i+1}. {m['model']}", ha="center", va="center",
                fontsize=9, color="#FFFFFF", fontweight="bold", zorder=5,
                bbox=dict(boxstyle="round,pad=0.15", facecolor="#1A1A1A",
                          alpha=0.9, edgecolor="#00E5FF", linewidth=0.5))
    for i, m in enumerate(pf):
        kind, b = result[i]
        dx, dy = dots[i]
        if kind == 'h':
            p0 = inv.transform((dx+R, dy))
            p1 = inv.transform((b[0]-1, dy))
        else:
            p0 = inv.transform((dx, dy+R))
            p1 = inv.transform((dx, b[1]+1))
        ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color="#00E5FF",
                lw=0.7, alpha=0.7, zorder=6)

    out = os.path.join(OUTPUT_DIR, "pareto_analysis.png")
    plt.savefig(out, dpi=200, facecolor="#000000")
    plt.close()
    print(f"Plot saved to {out}")

# ══════════════════════════════════════════════════════════════════════
# Helper: Fraction → JSON
# ══════════════════════════════════════════════════════════════════════

def _frac_to_json(v):
    if v is None:
        return None
    if isinstance(v, Fraction):
        return float(v)
    return v


# ══════════════════════════════════════════════════════════════════════
# Output: JSON + README
# ══════════════════════════════════════════════════════════════════════

def save_results(models, pareto, metric_ranges):
    # Load cache hit rate metadata to embed in the output
    chr_meta = None
    if os.path.exists(CACHE_HIT_RATE_FILE):
        with open(CACHE_HIT_RATE_FILE, encoding="utf-8") as f:
            chr_data = json.load(f)
        chr_meta = {
            "value": chr_data.get("cache_hit_rate"),
            "valid_count": chr_data.get("valid_count"),
            "total_count": chr_data.get("total_count"),
            "source": chr_data.get("metadata", {}).get("source"),
        }

    output = {
        "metadata": {
            "source": "https://artificialanalysis.ai/leaderboards/models",
            "methodology": (
                "18 evaluation metrics normalized [0,1], averaged → composite ability; "
                "Pareto = non-dominated by per-request cost; "
                "X-axis: linear-normalized cost (cost/max(Pareto cost) → [0,1]); "
                "Y-axis: composite ability (linear, direct average); "
                "Cost = formula: (CacheHitRate·CacheHitPrice·InputTokens) + "
                "((1-CacheHitRate)·CacheWritePrice·InputTokens) + "
                "(Speed·RealTime·OutputPrice)"
            ),
            "cost_formula": {
                "expression": "(CacheHitRate * CacheHitPrice * InputTokens) + ((1 - CacheHitRate) * CacheWritePrice * InputTokens) + (Speed * RealTime * OutputPrice)",
                "input_tokens": INPUT_TOKENS_DEFAULT,
                "input_tokens_note": "AA default 10k input-token workload (https://artificialanalysis.ai/methodology/performance-benchmarking)",
                "cache_write_price_fallback": "If cacheWritePrice is missing, falls back to price1mInputTokens (regular input price)",
                "real_time_logic": {
                    "reasoning_model": "EndToEndResponseTimeTotal - LatencyFirstChunk (= medianEndToEndResponseTimeSeconds - medianTimeToFirstTokenSeconds)",
                    "non_reasoning_model": "EndToEndResponseTimeTotal (= medianEndToEndResponseTimeSeconds, when medianReasoningTimeSeconds is null/'--')",
                },
                "cache_hit_rate": chr_meta,
                "units_note": (
                    "AA prices are USD per 1M tokens, InputTokens is a raw count (10000), "
                    "Speed is tokens/sec, RealTime is seconds. The formula is applied as-is "
                    "with no unit conversion — the resulting cost is a relative score "
                    "used only for Pareto comparison and linear normalization."
                ),
            },
            "total_models": len(models),
            "pareto_count": len(pareto),
        },
        "metric_ranges": {
            METRIC_LABELS[k]: {
                "min": float(v["min"]),
                "max": float(v["max"]),
                "count": v["count"],
            } if isinstance(v, dict) else v
            for k, v in metric_ranges.items()
        },
        "pareto_frontier": [_export_model(m, i + 1) for i, m in enumerate(pareto)],
        "all_models": [
            {
                "model": m["model"],
                "creator": m["creator"],
                "composite_ability": float(m["composite_ability"]),
                "normalized_cost": _frac_to_json(m.get("normalized_cost")),
                "per_request_cost": _frac_to_json(m.get("per_request_cost")),
                "is_reasoning": m["is_reasoning"],
                "is_pareto": m["model"] in {p["model"] for p in pareto},
            }
            for m in sorted(models, key=lambda x: x["composite_ability"], reverse=True)
        ],
    }

    json_path = os.path.join(OUTPUT_DIR, "analysis_results.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"JSON saved to {json_path}")

    generate_readme(pareto, models)


def _export_model(m, rank):
    bd = m.get("cost_breakdown") or {}
    return {
        "rank": rank,
        "model": m["model"],
        "creator": m["creator"],
        "is_reasoning": m["is_reasoning"],
        "composite_ability": float(m["composite_ability"]),
        "per_request_cost": _frac_to_json(m.get("per_request_cost")),
        "normalized_cost": _frac_to_json(m.get("normalized_cost")),
        # Pricing (USD per 1M tokens)
        "input_price": _frac_to_json(m.get("input_price")),
        "output_price": _frac_to_json(m.get("output_price")),
        "cache_hit_price": _frac_to_json(m.get("cache_hit_price")),
        "cache_write_price": _frac_to_json(m.get("cache_write_price")),
        "blended_price_721": _frac_to_json(m.get("blended_price_721")),
        # Speed / latency (10k input-token workload)
        "speed": _frac_to_json(m["speed"]),
        "ttft": _frac_to_json(m["ttft"]),
        "total_response": _frac_to_json(m["total_response"]),
        "reasoning_time": _frac_to_json(m["reasoning_time"]),
        # Cost-formula breakdown
        "cost_breakdown": bd,
        # AA's measured Intelligence Index cost (kept for reference)
        "intelligence_index_cost_total": _frac_to_json(m.get("intelligence_index_cost_total")),
        "intelligence_index_cost_input": _frac_to_json(m.get("intelligence_index_cost_input")),
        "intelligence_index_cost_output": _frac_to_json(m.get("intelligence_index_cost_output")),
        "intelligence_index_cost_reasoning": _frac_to_json(m.get("intelligence_index_cost_reasoning")),
        "intelligence_index_cost_answer": _frac_to_json(m.get("intelligence_index_cost_answer")),
        "valid_metrics": m["valid_metrics"],
    }


def generate_readme(pareto, models):
    # Load cache hit rate for the README metadata
    chr_value = None
    chr_count = None
    if os.path.exists(CACHE_HIT_RATE_FILE):
        with open(CACHE_HIT_RATE_FILE, encoding="utf-8") as f:
            chr_data = json.load(f)
        chr_value = chr_data.get("cache_hit_rate")
        chr_count = chr_data.get("valid_count")

    lines = []
    lines.append("# LLM Leaderboard Pareto Analysis\n")
    lines.append("![Pareto Analysis](output/pareto_analysis.png)\n")
    lines.append("## Pareto 前沿模型（综合能力从高到低）\n")
    lines.append("| # | 模型 | 综合能力 | 单请求成本 | 归一化成本 | 推理 |")
    lines.append("|---|------|---------|-----------|-----------|------|")

    for i, m in enumerate(pareto):
        cost = m.get("per_request_cost")
        cost_str = f"{float(cost):.2f}" if cost is not None else "--"
        reas = "Y" if m["is_reasoning"] else "N"
        norm_c = f"{float(m['normalized_cost']):.4f}" if m.get("normalized_cost") is not None else "--"
        lines.append(
            f"| {i+1} | {m['model']} | {float(m['composite_ability']):.4f} "
            f"| {cost_str} | {norm_c} | {reas} |"
        )

    lines.append("")
    lines.append("### 评分方法")
    lines.append("")
    lines.append("1. **18项评估指标**各自线性归一化到 [0,1]")
    lines.append("2. **综合能力值** = 所有有效归一化分数的算术平均")
    lines.append("3. **Pareto前沿** = 不被任何其他模型支配的模型")
    lines.append("")
    lines.append("### 成本计算公式")
    lines.append("")
    lines.append("**X轴成本 = 单请求估算成本（公式）**")
    lines.append("")
    lines.append("```")
    lines.append("cost = (CacheHitRate × CacheHitPrice × InputTokens)")
    lines.append("     + ((1 − CacheHitRate) × CacheWritePrice × InputTokens)")
    lines.append("     + (SpeedMedian × RealTime × OutputPrice)")
    lines.append("```")
    lines.append("")
    lines.append("**参数来源与处理逻辑：**")
    lines.append("")
    lines.append("| 参数 | 来源 | 说明 |")
    lines.append("|------|------|------|")
    lines.append("| CacheHitRate | [AA Coding Agents](https://artificialanalysis.ai/agents/coding-agents) | 全部模型-Agent搭配的 `cacheHitRate` 求平均（" + (f"{chr_count} 个有效值" if chr_count else "?") + "，均值 = " + (f"{chr_value:.4f}" if chr_value is not None else "?") + "），对所有模型统一使用 |")
    lines.append("| CacheHitPrice | AA `cacheHitPrice` | 缓存命中的输入价格 (USD / 1M tokens) |")
    lines.append("| CacheWritePrice | AA `cacheWritePrice` | 若缺失，回退到 `price1mInputTokens` (普通输入价格) |")
    lines.append("| InputTokens | `10000` | AA 默认的 10k input-token 工作负载（[方法论](https://artificialanalysis.ai/methodology/performance-benchmarking)） |")
    lines.append("| SpeedMedian | AA `medianOutputTokensPerSecond` | 输出速度中位数 (tokens/sec)，10k input-token 工作负载下测量 |")
    lines.append("| OutputPrice | AA `price1mOutputTokens` | 输出价格 (USD / 1M tokens) |")
    lines.append("| RealTime | 见下 | 生成输出 token 的实际耗时（秒） |")
    lines.append("")
    lines.append("**RealTime 计算逻辑：**")
    lines.append("")
    lines.append("- 如果存在 Reasoning Time（推理模型）：")
    lines.append("  `RealTime = End-to-End Response Time Total − Latency First Chunk`")
    lines.append("  = `medianEndToEndResponseTimeSeconds − medianTimeToFirstTokenSeconds`")
    lines.append("- 如果 Reasoning Time 为 `--`（非推理模型）：")
    lines.append("  `RealTime = End-to-End Response Time Total`")
    lines.append("  = `medianEndToEndResponseTimeSeconds`")
    lines.append("")
    lines.append("**单位说明：** AA 价格以 USD / 1M tokens 为单位，InputTokens 为原始计数（10000），Speed 为 tokens/sec，RealTime 为秒。公式按原样计算，不做单位换算。最终成本是一个相对得分（用于 Pareto 比较和线性归一化），不是真实的美元金额。")
    lines.append("")
    lines.append("### 数据来源")
    lines.append("")
    lines.append(f"**主数据源**: [Artificial Analysis Leaderboard](https://artificialanalysis.ai/leaderboards/models)  ")
    lines.append(f"**Cache Hit Rate 数据源**: [AA Coding Agents](https://artificialanalysis.ai/agents/coding-agents)  ")
    lines.append(f"**性能方法论**: [AA Performance Benchmarking](https://artificialanalysis.ai/methodology/performance-benchmarking)  ")
    lines.append(f"**模型总数**: {len(models)}  ")

    readme_path = os.path.join(BASE_DIR, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"README saved to {readme_path}")


# ══════════════════════════════════════════════════════════════════════
# Main
# ══════════════════════════════════════════════════════════════════════

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    if not os.path.exists(RAW_DATA_FILE):
        print(f"ERROR: {RAW_DATA_FILE} not found. Run scrape.py first.")
        sys.exit(1)

    print("Loading data...")
    data = load_data()
    print(f"  {len(data)} models loaded")

    print("\nComputing scores & costs...")
    models, metric_ranges = compute_scores(data)

    with_cost = [m for m in models if m.get("per_request_cost") is not None and m["per_request_cost"] > 0]
    if with_cost:
        costs = [m["per_request_cost"] for m in with_cost]
        print(f"  Models with cost data: {len(with_cost)}/{len(models)}")
        print(f"  Cost range: {float(min(costs)):.4f} – {float(max(costs)):.4f}")

    print("\nComputing Pareto frontier...")
    pareto = compute_pareto(models)
    print(f"  Pareto frontier: {len(pareto)} models")

    print("\nGenerating visualization...")
    plot_models = get_plot_models(models)
    plot_analysis(plot_models, pareto)

    print("\nSaving results...")
    save_results(models, pareto, metric_ranges)

    # Print Pareto table
    print(f"\n{'='*120}")
    print(f"PARETO FRONTIER ({len(pareto)} models) — ranked by composite ability")
    print(f"{'='*120}")
    print(f"{'#':<3} {'Model':<36} {'Ability':>8} {'Cost':>14} {'NormCost':>9} {'Reas':>4}")
    print(f"{'-'*3} {'-'*36} {'-'*8} {'-'*14} {'-'*9} {'-'*4}")
    for i, m in enumerate(pareto):
        cost = f"{float(m['per_request_cost']):.2f}" if m.get("per_request_cost") else "--"
        nc = f"{float(m['normalized_cost']):.4f}" if m.get("normalized_cost") else "--"
        reas = "Y" if m["is_reasoning"] else "N"
        print(f"{i+1:<3} {m['model']:<36} {float(m['composite_ability']):>8.4f} "
              f"{cost:>14} {nc:>9} {reas:>4}")

    print("\nDone!")


if __name__ == "__main__":
    main()
