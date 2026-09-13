#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scoring system and Pareto analysis for Artificial Analysis LLM Leaderboard.

**Version 18** — benchmark columns updated to AA's new payload (20 metrics)

AA redesigned the models-leaderboard RSC payload: the old 96-field array
is gone (its `agenticIndex` / `codingIndex` — the AA Agentic and Coding
Indexes — no longer ship at all), and four newer benchmark columns are
now carried.  METRIC_FIELDS therefore moves 18 → 20:

  removed:  agenticIndex (AA Agentic Index),
            codingIndex  (AA Coding Index)
  added:    analystAgent    — AA Analyst Agent
            tauBanking      — τ³-Bench Banking ("Intelligence Index v4.3 …
                              𝜏³-Banking is removed …" per AA's own note;
                              historical scores remain in the payload)
            terminalbenchV21 — Terminal-Bench 2.1
            terminalbenchV40 — Terminal-Bench 4.0 ("Terminal-Bench moves
                              to v4.0")

The cost pipeline is untouched — it computes from prices/speed/latency,
not from the (now missing) intelligenceIndexCostTotal.  scrape.py (V18)
merges the page's display-metadata `models` array into the main one by
slug, restoring `name` / `releaseDate`; creator slugs are derived from
the creator name where AA no longer provides them.

**Version 17** — chart scope, axis mapping and font determinism
(user feedback, four items):

A.  **README order.**  The long chart-explanation paragraph now lives at
    the END of the file; the chart is followed directly by the model
    table.

B.  **Deterministic fonts.**  Subsets of "Sarasa Mono SC" (Regular +
    Bold) ship in repo/fonts/ and are registered FIRST, so every machine
    — including the GitHub Actions runner — renders the identical sans
    typeface.  (The runner previously had none of the families listed
    before Sarasa and fell back to "Noto Serif SC", a SERIF font that
    the old workflow explicitly installed: that is why the GitHub chart
    text turned serif.)  The workflow font-install step is gone, and a
    runtime coverage check warns if any drawn character is missing from
    the bundled subsets.

C.  **Chart Y baseline.**  y = 0 sits at the FIRST (lowest) level of
    the overall Pareto frontier; models with lower composite ability do
    not appear in the chart at all (they stay in the README table).
    chart_y = (ability - y0) / (1 - y0), so the frontier's first point
    lands exactly on (0, 0) and the best model on y = 1.  The filter is
    applied BEFORE the X mapping is built.

D.  **X mapping = exact empirical-quantile (rank) mapping** over the
    chart-visible models: piecewise-linear in log10(c) (same-z tie
    groups averaged — V18: ties detected on equal log10(c), which also
    absorbs float costs differing by ~1e-12 that log10 collapses to the
    same z), pinned to pass (0,0) and (1,1) exactly, and — being
    linear in model rank — uniform in density: ANY equal-width segment
    holds the same number of models (the user's top priority).  The V12
    logistic could not do this on the filtered distribution (its decile
    counts swung 8-24).  Consequence, by design: same-multiplier decade
    widths are proportional to the model count inside that decade —
    uniform density and log-equidistance are mathematically
    incompatible, and density wins.

E.  **Right frame edge.**  The [0,1] frame's fourth segment was
    [[1,1],[0,0]] — y runs from 0 to 0, a degenerate single point — so
    the right edge was never drawn.  Now [[1,1],[1,0]]: all four edges
    are sealed.

**Version 16** — label placement rebuilt as the user's four-tier
priority flow.  (1) Every label that CAN ride a line does so, on
either side of its dot — a segment may carry two labels, one beside
each dot; a blocked on-line slot triggers a *yield*: the occupying
label is moved to another on-line slot of its own so BOTH stay on
the line.  (2) Labels that cannot ride sit parallel to the line,
directly above or below the nearest on-line position (left/right x
above/below combinations).  (3) Next, the nearest points on the
extension rays of the dot's two connecting segments.  (4) Finally,
the nearest position inside the sector between those two segments
(the wedge on the line's forward/upper side), still parallel to
the nearer segment.  Also fixes the V11-V15 "in"-segment direction
bug: backward candidates were generated PAST the dot (along the
incoming segment's forward extension), so no label ever sat on the
left-side segment between its dot and the previous vertex.

**Version 15** — monotonicity tightened from V14's projection rule to a
componentwise rule (user feedback: the label displacement must satisfy
BOTH x and y simultaneously — at least (0, 0); passing when just one
of them is >= 0 is not enough).  Within one brand's Pareto frontier a
model further to the upper-right must have its label centroid further
right AND further up — never trading one axis for the other.
The Version 13 label-text rules (user feedback: don't throw the baby
out with the bathwater — shorten labels where it is safe, keep them
distinguishable where it is not) still apply:

A.  **Prefix stripping extended.**  The strippable shared leading block
    is now the LONGEST valid cut inside the shared prefix.  A cut is
    valid when it ends at a word separator ("Claude ", "GPT-", "GLM-",
    "Grok ", "DeepSeek V4 ") OR ends with a letter whose following
    character is a digit in every name — a brand/series letter in front
    of a version number ("Kimi K|2.6", "Qwen|3.8 Max", "MiMo-V|2.5",
    "MiniMax-M|2.5").  This strips the prefixes V12 missed (Qwen,
    MiMo, Kimi's K) while names stay readable and distinguishable.

B.  **Adjacent same-family runs shortened — recomputed every time.**
    When 2+ CONSECUTIVE vertices of a brand polyline belong to the same
    model family, the lowest one (run head) keeps the full label and
    the higher adjacent members show only their thinking level
    ("(xhigh)").  Runs are maximal consecutive groups: a family that
    reappears after an interruption is NOT merged —
    A-B(high)-B(xhigh)-C-B(max) labels as A-B(high)-(xhigh)-C-B(max) —
    so interleaved families (Gemini 3.7/3.8 Flash, Fable 5.1 vs Opus 5
    at the top) always carry full labels and stay distinguishable.

C.  "(non-reasoning)" → "(non)" (unchanged); equal-cost vertex order
    (bottom-up) and the logistic single-function X mapping are
    unchanged from Version 12.

D.  **Monotone label placement per brand chain (V15).**  After the
    greedy pass, a repair pass walks each brand frontier in
    (axis_x, ability) order; for every adjacent pair A→B (B further
    upper-right) the label displacement (label_B − label_A) must be
    componentwise non-negative: dx >= 0 AND dy >= 0 — at least
    (0, 0), BOTH at once; either axis alone is not enough.  V14's
    projection rule let "further right but lower" pairs pass; V15
    treats them as violations, so equal-cost stacks order their labels
    bottom-up and left-to-right as well.  A violating label is
    re-seated at the nearest collision-free candidate inside the
    componentwise box imposed by its two neighbours, without breaking
    pairs that are still in order (up to 6 rounds).  Pairs whose local
    box is empty (the label is wedged between its neighbours) are
    then repaired by a whole-window cascade reflow that grows step
    by step around the stuck pair, re-seating the affected run as
    one staircase; pairs that cannot be fixed are reported).

Black canvas, riding labels, table, cost formula, data sources and
exact-Fraction arithmetic are unchanged from Version 11.
"""

import bisect
import json
import math
import os
import sys
from fractions import Fraction

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.patheffects as pe
from matplotlib.colors import to_rgb

# ══════════════════════════════════════════════════════════════════════
# Font setup (V17-B: deterministic, identical rendering everywhere)
# ══════════════════════════════════════════════════════════════════════
# ── Paths ──（先于字体注册：字体文件内嵌于仓库）
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
RAW_DATA_FILE = os.path.join(OUTPUT_DIR, "raw_data.json")
CACHE_HIT_RATE_FILE = os.path.join(OUTPUT_DIR, "cache_hit_rate.json")

# 内嵌字体（repo/fonts/，scripts/build_fonts.py 生成的 Sarasa Mono SC 子集）：
# 最先注册 → 任何机器（含 GitHub Actions runner）都用同一份字体文件，
# 渲染与本地完全一致。V17 之前 runner 上没有列表中排在 Noto Serif SC 之前
# 的任何族，于是回退到 workflow 专门安装的 Noto Serif SC（衬线）——
# 这正是 GitHub 图表文字变成衬线的原因。
_BUNDLED_FONTS = [
    os.path.join(BASE_DIR, "fonts", "SarasaMonoSC-Regular.ttf"),
    os.path.join(BASE_DIR, "fonts", "SarasaMonoSC-Bold.ttf"),
]
# 开发机回退：系统安装的同族字体（与内嵌子集同源，仅本地使用）
_HEITI_FONTS = [
    "/usr/share/fonts/truetype/chinese/SarasaMonoSC-Regular.ttf",
    "/usr/share/fonts/truetype/chinese/SarasaMonoSC-Bold.ttf",
]
for fp in _BUNDLED_FONTS + _HEITI_FONTS:
    if os.path.exists(fp):
        try:
            fm.fontManager.addfont(fp)
        except Exception:
            pass
plt.rcParams["font.sans-serif"] = ["Sarasa Mono SC", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False


# ── Cost-formula constants ──
INPUT_TOKENS_DEFAULT = 10_000

# ── Brand Pareto lines (chart only) ──
# Creators as named on the AA page; "Xiaomi" is the creator of the MiMo
# model family (the user refers to this brand as "Mimo").
BRAND_LINE_CREATORS = [
    "Anthropic", "OpenAI", "Meta", "Z AI", "Google", "SpaceXAI",
    "Kimi", "Alibaba", "DeepSeek", "MiniMax", "Xiaomi",
]
BRAND_DISPLAY_NAMES = {  # chart legend / README display names
    "Xiaomi": "Xiaomi · MiMo",
}
# Base URL of the creator logos as served by the AA page (src="/img/logos/...")
LOGO_BASE_URL = "https://artificialanalysis.ai/img/logos/"

# ── Chart style (V11: black background) ──
BG_COLOR = "#0A0A0D"            # 黑底
OVERALL_LINE_COLOR = "#A8A8B2"  # 总体帕累托连线：直线灰色（黑底上可读）
CLOUD_COLOR = "#5A5A66"          # 非前沿模型散点
FRAME_COLOR = "#3C3C46"
GRID_COLOR = "#15151B"           # 十分位淡网格
DECADE_GRID_COLOR = "#22222C"   # 10^x 数量级指示竖线
TEXT_COLOR = "#EAEAEF"
MUTED_TEXT_COLOR = "#9C9CA6"
DARK_LUM_THRESHOLD = 0.32        # 亮度低于此值的品牌色 → 窄白边包裹

# ── Label / marker sizes ──
FS_FULL = 7.0                    # 标签字号（短标签）
FS_LEVEL = 6.1                   # 标签字号（长标签，长度 ≥ LABEL_LONG_LEN）
LABEL_LONG_LEN = 22              # 超过此字符数的标签用小一号字体
MS_CLOUD = 8                     # 非前沿散点大小 (pt²)
MS_BRAND = 26                    # 品牌前沿 · 非总体前沿
MS_BRAND_GLOBAL = 44             # 品牌前沿 · 同时在总体前沿
MS_OTHER_GLOBAL = 38             # 其他品牌的总体前沿点
LW_OVERALL = 2.2                 # 总体帕累托线宽
LW_BRAND = 1.1                   # 品牌线宽（较窄，避免遮挡）

# ── Metrics (from AA's evaluation data) ──
# V18: agenticIndex / codingIndex (AA Agentic / Coding Index) were removed
# from AA's models payload; the four new benchmark columns are added —
# analystAgent, tauBanking (τ³-Bench Banking), terminalbenchV21 (2.1) and
# terminalbenchV40 (4.0).  20 metrics total.
METRIC_FIELDS = {
    "intelligenceIndex": "intelligenceIndex",
    "gpqa": "gpqa",
    "hle": "hle",
    "mmmuPro": "mmmuPro",
    "ifbench": "ifbench",
    "scicode": "scicode",
    "critpt": "critpt",
    "lcr": "lcr",
    "omniscience": "omniscience",
    "omniscienceAccuracy": "omniscienceAccuracy",
    "omniscienceNonHallucination": "omniscienceNonHallucination",
    "gdpvalNormalized": "gdpvalNormalized",
    "analystAgent": "analystAgent",
    "apexAgents": "apexAgents",
    "itbenchSre": "itbenchSre",
    "tau2": "tau2",
    "tauBanking": "tauBanking",
    "terminalbenchHard": "terminalbenchHard",
    "terminalbenchV21": "terminalbenchV21",
    "terminalbenchV40": "terminalbenchV40",
}

METRIC_LABELS = {
    "intelligenceIndex": "AA Intelligence Index",
    "gpqa": "GPQA Diamond",
    "hle": "Humanity's Last Exam",
    "mmmuPro": "MMMU Pro",
    "ifbench": "IFBench Instruction Following",
    "scicode": "SciCode Coding",
    "critpt": "CritPt Physics",
    "lcr": "AA-LCR Long Context",
    "omniscience": "AA Omniscience Index",
    "omniscienceAccuracy": "AA-Omniscience Accuracy",
    "omniscienceNonHallucination": "AA-Omniscience Non-Hallucination",
    "gdpvalNormalized": "GDPval-AA Normalized",
    "analystAgent": "AA Analyst Agent",
    "apexAgents": "APEX-Agents-AA",
    "itbenchSre": "ITBench-SRE",
    "tau2": "τ²-Bench Telecom",
    "tauBanking": "τ³-Bench Banking",
    "terminalbenchHard": "Terminal-Bench Hard",
    "terminalbenchV21": "Terminal-Bench 2.1",
    "terminalbenchV40": "Terminal-Bench 4.0",
}

MIN_VALID_METRICS = 5


# ══════════════════════════════════════════════════════════════════════
# Data Loading & Computation
# ══════════════════════════════════════════════════════════════════════

def load_data():
    with open(RAW_DATA_FILE, encoding="utf-8") as f:
        return json.load(f)


def compute_scores(data):
    """Compute composite ability and per-request cost for ALL models.

    Version 10: no `deprecated` filter — every model from the RSC payload
    (Status: All on the AA leaderboard) is analyzed.  Display name is
    AA's `shortName`; creator/color/logo fields are kept for the brand
    column and per-brand Pareto lines.
    """
    models = []
    n_deprecated = 0
    for d in data:
        if d.get("deprecated", False):
            n_deprecated += 1
        m = {
            # Requirement 8: short display name
            "model": d.get("shortName") or d.get("name", "Unknown"),
            "full_name": d.get("name", "Unknown"),
            "slug": d.get("slug", ""),
            # V18: payload uses `isReasoning` (old field name kept as fallback)
            "is_reasoning": bool(d.get("reasoningModel", d.get("isReasoning", False))),
            "is_deprecated": bool(d.get("deprecated", False)),
            # Requirement 6/7: brand column & brand theme colors
            "creator": d.get("modelCreatorName", ""),
            "creator_slug": (d.get("modelCreatorSlug")
                             or _derive_creator_slug(d.get("modelCreatorName"))),
            "creator_color": d.get("modelCreatorColor") or "#888888",
            "creator_logo": d.get("modelCreatorLogo") or "",
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
            # Speed / latency data (all measured at the 10k input-token workload)
            "speed": _to_frac(d.get("medianOutputTokensPerSecond")),
            "ttft": _to_frac(d.get("medianTimeToFirstTokenSeconds")),
            "total_response": _to_frac(d.get("medianEndToEndResponseTimeSeconds")),
            "reasoning_time": _to_frac(d.get("medianReasoningTimeSeconds")),
            "intelligence_index": _to_frac(d.get("intelligenceIndex")),
            "_parsed": {},
        }
        for key, aa_field in METRIC_FIELDS.items():
            m["_parsed"][key] = _to_frac(d.get(aa_field))
        models.append(m)

    print(f"Models loaded (Status: All, including {n_deprecated} deprecated): {len(models)}")

    # ── Metric ranges (Fraction) — over ALL models ──
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
        m["composite_ability_raw"] = sum(nv) / len(nv) if nv else None
        m["valid_metrics"] = len(nv)

    # Quality filter (models with too few evaluated metrics cannot be ranked)
    valid = [m for m in models
             if m["composite_ability_raw"] is not None and m["valid_metrics"] >= MIN_VALID_METRICS]
    print(f"Models with ≥{MIN_VALID_METRICS} metrics: {len(valid)} "
          f"({len(models) - len(valid)} lack evaluation data and are not ranked)")

    # ── Requirement 4: re-normalize composite ability to [0, 1] ──
    # best-performing model = 1, worst-performing model = 0
    abilities = [m["composite_ability_raw"] for m in valid]
    min_a, max_a = min(abilities), max(abilities)
    print(f"Composite ability (raw) range: {float(min_a):.4f} – {float(max_a):.4f}")
    for m in valid:
        if max_a > min_a:
            m["composite_ability"] = (m["composite_ability_raw"] - min_a) / (max_a - min_a)
        else:
            m["composite_ability"] = Fraction(1, 2)
    best = max(valid, key=lambda m: m["composite_ability"])
    worst = min(valid, key=lambda m: m["composite_ability"])
    print(f"  Re-normalized: best = {best['model']} → 1.0000, worst = {worst['model']} → 0.0000")

    # ── Per-request cost via the user-supplied formula (unchanged) ──
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

    # 横轴映射延迟到标签构建之后（见 build_axis_mapping()）。此处先初始化 axis_x。
    for m in valid:
        m["axis_x"] = None
    priced = [m for m in valid
              if m.get("per_request_cost") is not None and m["per_request_cost"] >= 0]
    if priced:
        cmin = float(min(m['per_request_cost'] for m in priced))
        cmax = float(max(m['per_request_cost'] for m in priced))
        n_free = sum(1 for m in priced if m['per_request_cost'] == 0)
        print(f"\n  Cost range: {cmin:.2f} – {cmax:.2f}  "
              f"({len(priced)} priced, {n_free} free/cost-0)")

    return valid, metric_ranges


def _to_frac(val):
    """Convert a numeric value to Fraction, or None if null/invalid."""
    if val is None:
        return None
    try:
        return Fraction(val).limit_denominator(10**12)
    except (ValueError, TypeError, ZeroDivisionError):
        return None


def _derive_creator_slug(name):
    """V18: AA's payload no longer carries modelCreatorSlug — derive a
    stable slug from the creator name (metadata only, JSON output field)."""
    if not name:
        return ""
    import re as _re
    slug = _re.sub(r"[^a-z0-9]+", "-", str(name).strip().lower()).strip("-")
    return slug


# ══════════════════════════════════════════════════════════════════════
# Cost-formula helpers (unchanged from Version 9)
# ══════════════════════════════════════════════════════════════════════

def _load_cache_hit_rate():
    """Load the global average Cache Hit Rate scraped from the AA coding-agents page."""
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
    """
    cache_hit_price = m.get("cache_hit_price")
    cache_write_price = m.get("cache_write_price")
    cache_write_source = "cacheWritePrice"
    if cache_write_price is None:
        cache_write_price = m.get("input_price")
        cache_write_source = "inputPrice (fallback)"
    output_price = m.get("output_price")
    speed = m.get("speed")
    e2e_total = m.get("total_response")
    ttft = m.get("ttft")
    reasoning_time = m.get("reasoning_time")
    has_reasoning = reasoning_time is not None
    if has_reasoning:
        if e2e_total is None or ttft is None:
            real_time = None
            real_time_source = "E2E - TTFT (missing data)"
        else:
            real_time = e2e_total - ttft
            real_time_source = "E2E_total - TTFT (reasoning model)"
    else:
        real_time = e2e_total
        real_time_source = "E2E_total (non-reasoning)"

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

    if cache_hit_price is not None:
        term1 = cache_hit_rate * cache_hit_price * input_tokens
    else:
        term1 = Fraction(0)
    term2 = (Fraction(1) - cache_hit_rate) * cache_write_price * input_tokens
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
# Pareto frontier computation
# ══════════════════════════════════════════════════════════════════════

def compute_pareto(models):
    """Pareto frontier (max ability, min cost) over the given model set.

    V11: cost 0 (free models) is a valid cost and participates — the
    left edge of the X axis is pinned to 0, so free models are genuine
    frontier candidates (a free model can only be dominated by another
    free model).
    """
    priced = [m for m in models if m.get("per_request_cost") is not None and m["per_request_cost"] >= 0]
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


def compute_brand_frontiers(models):
    """Requirement 7: per-brand Pareto frontiers for the eleven listed brands.

    A model on the global frontier is automatically on its brand's frontier
    (a subset cannot contain a dominator the full set does not).
    """
    frontiers = {}
    for brand in BRAND_LINE_CREATORS:
        bm = [m for m in models if m.get("creator") == brand]
        frontier = compute_pareto(bm)
        if frontier:
            frontiers[brand] = frontier
    for brand, fr in frontiers.items():
        print(f"  {brand}: {len([m for m in models if m.get('creator') == brand and m.get('per_request_cost') is not None])} priced / "
              f"{len(fr)} on brand frontier")
    return frontiers


def apply_chart_baseline(models, pareto):
    """V17-C: the chart's y = 0 sits at the FIRST (lowest) level of the
    overall Pareto frontier.

    Models with lower composite ability do not appear in the chart at
    all (they stay in the README table).  This filter runs BEFORE the
    X-axis mapping is built (build_axis_mapping fits the mapping to the
    chart-visible models only).  Visible models get

        chart_y = (composite_ability - y0) / (1 - y0)

    so the frontier's first point lands exactly on (0, 0) and the best
    model on y = 1.
    """
    y0 = min(float(m["composite_ability"]) for m in pareto)
    first = next(m for m in pareto if float(m["composite_ability"]) == y0)
    for m in models:
        a = m.get("composite_ability")
        m["chart_y"] = ((float(a) - y0) / (1.0 - y0)
                        if a is not None and float(a) >= y0 else None)
    n_vis = sum(1 for m in models if m.get("chart_y") is not None)
    n_plotted = sum(1 for m in models
                    if m.get("chart_y") is not None
                    and m.get("per_request_cost") is not None
                    and m["per_request_cost"] >= 0)
    print(f"  Baseline y0 = {y0:.4f} (first Pareto level: {first['model']})")
    print(f"  Chart scope: {n_plotted} plotted / {n_vis} at-or-above baseline / "
          f"{len(models)} total — {len(models) - n_vis} below baseline "
          f"(table-only) + {n_vis - n_plotted} above baseline without cost data")
    return {
        "baseline": y0,
        "baseline_model": first["model"],
        "visible_models": n_vis,
        "plotted_models": n_plotted,
        "no_cost_visible": n_vis - n_plotted,
        "below_baseline": len(models) - n_vis,
        "total_models": len(models),
        "note": ("chart y = (ability - baseline)/(1 - baseline); models below "
                 "the first overall-Pareto level are excluded from the chart "
                 "but kept in the README table"),
    }


# ══════════════════════════════════════════════════════════════════════
# Requirement 9 (V13 revision): label texts for brand-frontier models
# ══════════════════════════════════════════════════════════════════════

def split_name_level(short_name):
    """Split a display name into (base, level).

    'Claude Fable 5.1 (max with fallback)' → ('Claude Fable 5.1', 'max with fallback')
    'GLM-5.3-Flash'                        → ('GLM-5.3-Flash', None)
    """
    s = (short_name or "").strip()
    if s.endswith(")"):
        i = s.rfind("(")
        if i > 0:
            return s[:i].strip(), s[i + 1:-1].strip()
    return s, None


def _short_level(level):
    """V12: '(non-reasoning)' → '(non)'（含组合式 'Non-reasoning, high' → 'non, high'）。

    后续：档位里的 'with fallback' 后缀去掉，只留思考档位——
    'max with fallback' → 'max'；裸 '(with fallback)' 去掉后无档位，
    返回 None 即标签只显示 base 名。
    """
    if level is None:
        return None
    lv = level.strip()
    low = lv.lower()
    if low == "non-reasoning":
        return "non"
    if low.startswith("non-reasoning,"):
        return "non" + lv[len("non-reasoning"):]
    if low == "with fallback":
        return None
    if low.endswith(" with fallback"):
        short = lv[: -len(" with fallback")].strip()
        return short or None
    return lv


def _strippable_prefix(names, brand_name):
    """V13-A: brand-frontier shared leading block size in chars (0 = keep).

    Find the LONGEST valid cut inside the case-insensitive longest common
    prefix of the bases (name minus its bracketed thinking level), where
    1 <= cut < len(shortest base):

      1) separator cut — the char before the cut is a space / hyphen /
         underscore: "Claude |Sonnet 5", "GPT-|5.6", "GLM-|4.7",
         "Grok |4.6", "DeepSeek V4 |Pro" (a brand name + separator is
         naturally covered by this rule);
      2) version cut — the char before the cut is a letter AND the char
         at the cut is a digit in every base (a brand/series letter in
         front of a version number): "Kimi K|2.6", "Qwen|3.8 Max",
         "MiMo-V|2.5", "MiniMax-M|2.5".

    A cut that empties any name or produces duplicate labels is rejected
    and shorter cuts are tried in turn, so stripping only shortens the
    labels and never hurts distinguishability.
    """
    if len(names) < 2:
        # V17: a single vertex shares nothing — keep the full label
        # (e.g. Meta's one visible vertex "Muse Spark 1.3" must not
        # collapse to "1.3")
        return 0
    parts = [split_name_level(n) for n in names]
    low = [p[0].lower() for p in parts]
    levels = [_short_level(p[1]) for p in parts]

    p = low[0]
    for q in low[1:]:
        i = 0
        while i < len(p) and i < len(q) and p[i] == q[i]:
            i += 1
        p = p[:i]
        if not p:
            return 0

    shortest = min(len(b) for b in low)
    for cut in range(min(len(p), shortest - 1), 0, -1):
        c = p[cut - 1]
        if c not in " -_":
            # version cut: prefix ends with a letter and every base
            # continues with a digit right after the cut
            if not c.isalpha() or not all(b[cut].isdigit() for b in low):
                continue
        texts = []
        for (base, _), lv in zip(parts, levels):
            t = base[cut:].lstrip(" -_")
            if not t:
                texts = None
                break
            texts.append(f"{t} ({lv})" if lv else t)
        if texts is not None and len(set(texts)) == len(texts):
            return cut
    return 0


def _label_text(name, prefix_len):
    """V13: full label = base (shared prefix stripped) + ' (level)'; '(non-reasoning)' shortened to '(non)'."""
    base, level = split_name_level(name)
    if prefix_len:
        base = base[prefix_len:].lstrip(" -_")
    lv = _short_level(level)
    return f"{base} ({lv})" if lv else base


def build_label_specs(models, pareto, brand_frontiers):
    """Assign a chart label to every labeled model.

    Labeled models = all brand-frontier models of the eleven listed brands
    plus global-frontier models of every other brand.

    V13 rules:
      A. brand-shared leading block is stripped at the longest valid cut
         (separator cut or letter->digit version cut, _strippable_prefix);
      B. "(non-reasoning)" is shortened to "(non)";
      C. ADJACENT same-family runs are shortened: when 2+ CONSECUTIVE
         vertices of a brand polyline (ordered by (axis_x, ability), the
         drawing order) belong to the same model family, the run head
         (lowest performance) keeps the full label and the higher
         adjacent members show only their thinking level "(level)".
         Runs are maximal consecutive groups recomputed per brand — a
         family reappearing after an interruption (A-B-B-C-B) is NOT
         merged, so interleaved families (Gemini 3.7 vs 3.8 Flash,
         Claude Fable 5.1 vs Opus 5) always carry full labels and stay
         distinguishable.
    """
    labeled = {}
    n_level_only = 0

    for brand, fr in brand_frontiers.items():
        names = [m["model"] for m in fr]
        plen = _strippable_prefix(names, brand)
        if plen:
            print(f"    prefix stripped: {brand:<12} "
                  f"{split_name_level(names[0])[0][:plen]!r} "
                  f"({plen} chars, {len(fr)} models)")
        # vertex order = polyline drawing order: (axis_x, ability) asc
        order = sorted(fr, key=lambda m: (float(m["axis_x"]),
                                          float(m["composite_ability"])))
        # maximal consecutive same-family runs, recomputed per brand
        runs = []
        for m in order:
            base = split_name_level(m["model"])[0]
            if runs and runs[-1][0] == base:
                runs[-1][1].append(m)
            else:
                runs.append((base, [m]))
        for base, members in runs:
            if len(members) == 1:
                labeled[id(members[0])] = _label_text(members[0]["model"], plen)
                continue
            # run of 2+: the lowest one (run head) keeps the full label,
            # higher adjacent members show only their thinking level
            for i, m in enumerate(members):
                lv = _short_level(split_name_level(m["model"])[1])
                if i == 0 or lv is None:
                    labeled[id(m)] = _label_text(m["model"], plen)
                else:
                    labeled[id(m)] = f"({lv})"
                    n_level_only += 1
            print(f"    adjacent run:   {brand:<12} {base!r} x{len(members)} "
                  f"-> head keeps full label, {len(members) - 1} level-only")

    # Global-frontier models of brands without a dedicated brand line
    brand_models = {id(m) for fr in brand_frontiers.values() for m in fr}
    others = [m for m in pareto if id(m) not in brand_models]
    for m in others:
        labeled[id(m)] = _label_text(m["model"], 0)

    print(f"\n  Chart labels: {len(labeled)} total "
          f"({sum(1 for m in brand_frontiers.values() for _ in m)} brand-frontier + {len(others)} other global-frontier)")
    print(f"  Adjacent-run level-only labels: {n_level_only}")
    lens = [len(t) for t in labeled.values()]
    print(f"  Label length: mean={sum(lens)/len(lens):.1f} chars, max={max(lens)}, "
          f"long (>={LABEL_LONG_LEN} chars, small font): {sum(1 for L in lens if L >= LABEL_LONG_LEN)}")

    # attach labels & brand-line membership to the models
    for m in models:
        m["chart_label"] = labeled.get(id(m))
        m["brand_frontier_of"] = None
    for brand, fr in brand_frontiers.items():
        for m in fr:
            m["brand_frontier_of"] = brand
    return labeled


# ══════════════════════════════════════════════════════════════════════
# V17-D: exact empirical-quantile (rank) X mapping — uniform density,
# endpoint pins (0,0)/(1,1), built AFTER the V17-C baseline filter
# ══════════════════════════════════════════════════════════════════════


def _color_lum(color):
    """Relative luminance of any matplotlib-parsable color (0..1)."""
    try:
        r, g, b = to_rgb(color)
        return 0.299 * r + 0.587 * g + 0.114 * b
    except Exception:
        return 0.5


def _is_dark_color(color):
    """暗色元素 → 需要一层窄白边包裹（黑底上才可见）。"""
    return _color_lum(color) < DARK_LUM_THRESHOLD


def build_axis_mapping(models, brand_frontiers):
    """V17-D 精确分位数（rank）横轴映射 —— 等密度。

        x = 0                      当 c <= 0（免费模型钉在最左缘）
        x = interp(z; knots)       当 c > 0，其中 z = log10(c)

    knots = (z_i, 名次_i/(n-1))：**入图**（chart_y 非空，V17-C 过滤之后）
    正成本模型按 log10(c) 排序的 n 个锚点，相同 log10(c) 的并列组取平均名次（保证
    x 是 z 的单值函数）。端点严格钉死：c = 0 → x = 0；最大成本 → x = 1
    （若最贵成本并列导致 x_max < 1，则整体按比例归一，右端点仍严格为 1）。

    x 是名次的线性函数 ⇒ **任意等宽区段的模型数恒定**（用户最高优先级：
    无论截取哪一段，模型数/宽度 = 全图模型数/总宽度）。V12 的单一
    logistic 在过滤后的分布上做不到（十分位在 8~24 间摆动），故弃用。
    10^x 数量级指示位于 x(10^x)；同倍率区间的宽度 ∝ 该区间的模型数。

    同时把 m["axis_x"] 写入全部可计价模型（表格仍给每行横轴位置；
    低于入图最低成本者截断到 0）。
    """
    priced = [m for m in models
              if m.get("per_request_cost") is not None and m["per_request_cost"] >= 0]
    vis = [m for m in priced if m.get("chart_y") is not None]
    pos = sorted(float(m["per_request_cost"]) for m in vis
                 if float(m["per_request_cost"]) > 0)
    n = len(pos)

    # 锚点：相同 log10(c) 的并列组取平均名次
    # V18 修正：并列判定改用**相等的 z = log10(c)**——两个相差 ~1e-12 的不同
    # float 成本经 log10 会弽合到完全相同的 z（实测：12935.130860966676 与
    # …678），若按原始成本分组会产生两个同 z 不同 x 的锚点，既违反“x 是 z
    # 的单值函数”，又让 bisect_right 把所有同 z 成本都落到最后一个锚点上
    # （个别模型 x 偏离名次 1.5/102，十分位计数 9↔11 摆动）。改按 z 分组后
    # x 对每个入图模型严格等于（组内平均名次）/(n-1)，与文献描述一致。
    knots = []
    i = 0
    while i < n:
        z = math.log10(pos[i])
        j = i
        while j + 1 < n and math.log10(pos[j + 1]) == z:
            j += 1
        knots.append((z, (i + j) / 2.0 / max(n - 1, 1)))
        i = j + 1
    # 端点钉死 (1,1)：若最贵成本并列使 x_max < 1，按比例归一
    if knots and 0.0 < knots[-1][1] < 1.0:
        top = knots[-1][1]
        knots = [(z, x / top) for z, x in knots]
    zs = [k[0] for k in knots]

    def f(cost):
        c = float(cost)
        if c <= 0.0 or not knots:
            return 0.0
        z = math.log10(c)
        if z <= zs[0]:
            return knots[0][1]
        if z >= zs[-1]:
            return knots[-1][1]
        k = bisect.bisect_right(zs, z) - 1
        z0, x0 = knots[k]
        z1, x1 = knots[k + 1]
        return x0 + (x1 - x0) * (z - z0) / (z1 - z0)

    for m in priced:
        m["axis_x"] = f(m["per_request_cost"])

    # 均匀密度质量：x 线性于名次，十分位严格均匀（并列平均仅影响边界）
    xs = sorted(f(c) for c in pos)
    devs = [abs(x - (r + 0.5) / n) for r, x in enumerate(xs)] if xs else [0.0]
    max_dev = max(devs)
    mean_dev = sum(devs) / max(n, 1)

    # 10^x 数量级指示（位置 = x(10^x)）
    decades = []
    if pos:
        zmax = math.log10(pos[-1])
        for e10 in range(0, int(math.floor(zmax)) + 1):
            d = 10.0 ** e10
            if d <= pos[-1]:
                decades.append({"price": d, "x": f(d)})

    left = sum(1 for m in vis if float(m["axis_x"]) < 0.5)
    meta = {
        "mapping": ("exact empirical-quantile (rank) mapping over the "
                    "chart-visible models, piecewise-linear in log10(c)"),
        "function": ("x = 0 for c <= 0; x = interp(log10(c) over knots "
                     "(z_i, rank_i/(n-1))) for c > 0 — knots are the sorted "
                     "log-costs of the n chart-visible positive-cost models "
                     "(same-z tie groups averaged; V18: ties detected on equal "
                     "log10(c) — x is exactly linear in rank for every visible "
                     "model); endpoints pinned (0,0)/(1,1)"),
        "knots": len(knots),
        "fit": {
            "fitted_models": n,
            "method": "empirical quantile mapping (x linear in model rank)",
            "max_abs_ecdf_deviation": max_dev,
            "mean_abs_ecdf_deviation": mean_dev,
            "uniform_density": True,
            "note": ("x is linear in rank: any equal-width segment holds the "
                     "same number of models by construction"),
        },
        "left_edge_cost": 0.0,
        "free_models": sum(1 for m in vis if float(m["per_request_cost"]) == 0),
        "plotted_models": len(vis),
        "total_models": len(models),
        "min_positive_cost": pos[0] if pos else None,
        "x_at_min_positive_cost": knots[0][1] if knots else None,
        "max_cost": pos[-1] if pos else None,
        "x_at_max_cost": knots[-1][1] if knots else None,
        "decade_ticks": decades,
        "left_half_models": left,
        "right_half_models": len(vis) - left,
        "map_fn": f,
    }
    print(f"\n  X mapping (V17 quantile): {len(knots)} knots over {n} "
          f"chart-visible positive-cost models")
    if knots:
        print(f"  Endpoint pins: c=0 -> x=0; max c={pos[-1]:,.0f} -> "
              f"x={knots[-1][1]:.6f} (must be exactly 1)")
    print(f"  Uniform density: x linear in rank — each 0.1-wide decile "
          f"holds ~{n / 10:.1f} models; |x-ECDF| max={max_dev:.4f}")
    print(f"  Free models pinned at x=0: {meta['free_models']}; "
          f"left/right half = {left}/{len(vis) - left}")
    if decades:
        pos_s = ", ".join(f"10^{int(round(math.log10(d['price'])))}->{d['x']:.4f}"
                          for d in decades)
        print(f"  Decade indicators: {pos_s}")
    return meta


# ══════════════════════════════════════════════════════════════════════
# Requirement 5b: X-axis distribution analysis
# ══════════════════════════════════════════════════════════════════════

def analyze_x_distribution(models, mapping_meta):
    """Verify the adaptive mapping spreads models across the whole X axis.

    V17: the mapping is the exact empirical-quantile (rank) mapping over
    the CHART-VISIBLE models, so the decile occupancy is uniform by
    construction (x is linear in rank); only equal-cost tie averaging at
    decile boundaries can shift a model by one bin.
    """
    xs = [float(m["axis_x"]) for m in models
          if m.get("axis_x") is not None and m.get("chart_y") is not None]
    if not xs:
        return {"plotted_models": 0}
    xs.sort()
    n = len(xs)
    deciles = [0] * 10
    for x in xs:
        b = min(int(x * 10), 9)
        deciles[b] += 1
    left = sum(1 for x in xs if x < 0.5)
    result = {
        "plotted_models": n,
        "x_min": xs[0],
        "x_max": xs[-1],
        "median": xs[n // 2],
        "left_half_models": left,
        "right_half_models": n - left,
        "decile_counts": deciles,
        "note": (
            "quantile mapping (V17): x = interp(log10(c) over the rank knots of "
            "the chart-visible models); uniform density by construction; "
            "endpoints pinned (0,0)/(1,1); left edge c = 0; 10^x indicators "
            "sit at x(10^x)"
        ),
    }
    print(f"\n  X distribution: n={n}, median={result['median']:.3f}, "
          f"left/right = {left}/{n - left}")
    print(f"  Decile counts: {deciles}")
    empty = [i for i, c in enumerate(deciles) if c == 0]
    if empty:
        print(f"  WARNING: empty deciles {empty} — models do not use the full axis width")
    else:
        print(f"  OK: every decile of the X axis contains models — full-width coverage")
    return result


# ══════════════════════════════════════════════════════════════════════
# Visualization
# ══════════════════════════════════════════════════════════════════════

def _fmt_cost_tick(v):
    """1000 → '1k', 1000000 → '1M' (for the decade gridline ticks)."""
    if v >= 1_000_000:
        s = v / 1_000_000
        return f"{s:g}M"
    if v >= 1_000:
        s = v / 1_000
        return f"{s:g}k"
    return f"{v:g}"


def check_font_coverage(strings):
    """V17-B：确认所有将绘制的字符都在内嵌字体里有字形。

    内嵌字体是 Sarasa Mono SC 的子集（scripts/build_fonts.py 生成）；若
    未来的模型名/文案包含子集外的字符，matplotlib 会逐字回退到
    DejaVu Sans（拉丁可读但字形不一致）或渲染成方块（CJK）——本检查
    让缺字在日志里显式报警，而不是悄悄变样。
    """
    try:
        from matplotlib import ft2font
        paths = [p for p in _BUNDLED_FONTS if os.path.exists(p)]
        if not paths:
            print("  (font check skipped: repo/fonts/ not found)")
            return
        cov = set()
        for p in paths:
            ff = ft2font.FT2Font(p)
            for cp in range(0x20, 0x10000):
                if ff.get_char_index(cp):
                    cov.add(chr(cp))
        chars = {ch for s in strings for ch in s if ord(ch) >= 0x20}
        missing = sorted(ch for ch in chars if ch not in cov)
        if missing:
            print(f"  WARNING: {len(missing)} chars missing from bundled font "
                  f"(fallback/tofu risk): {''.join(missing[:60])}")
        else:
            print(f"  Font coverage OK: {len(chars)} unique chars, 0 missing "
                  f"({len(cov)} glyphs available in bundled subsets)")
    except Exception as e:
        print(f"  (font coverage check skipped: {e})")


def plot_analysis(models, pareto, brand_frontiers, x_dist, mapping_meta):
    """Generate the Pareto scatter plot (V17 layout).

    - Black background; dark brand elements get a narrow white outline.
    - X axis: exact empirical-quantile (rank) mapping over the
      chart-visible models (V17-D) — piecewise-linear in log10(c),
      endpoints pinned at (0,0)/(1,1), uniform model density; 10^x
      magnitude indicators sit at x(10^x).
    - Y axis: 0 = first (lowest) level of the overall Pareto frontier
      (V17-C); models below that level are not drawn at all — the
      frontier's first point sits exactly on (0,0), the best model on
      y = 1.
    - Overall Pareto frontier: solid gray line.  Eleven brand frontiers:
      thin brand-colored lines drawn ABOVE it; vertices ordered by
      (axis_x, ability) so equal-cost points connect bottom-up.
    - Labels (family + thinking level, brand-shared prefix stripped;
      2+ consecutive same-family vertices shorten to level-only labels
      after the run head) ride ON the Pareto lines whenever the
      adjacent segment is long enough; otherwise they take the nearest
      collision-free spot.
    """
    plot_models = [m for m in models
                   if m.get("axis_x") is not None and m.get("chart_y") is not None]
    pareto_names = {id(m) for m in pareto}
    brand_line_models = {id(m) for fr in brand_frontiers.values() for m in fr}

    # ── 画布 14.5x14：绘图区更大（标签骑线后页边距需求减小，角部更宽松）──
    fig = plt.figure(figsize=(14.5, 14), facecolor=BG_COLOR)
    ax = fig.add_axes([0.055, 0.13, 0.71, 0.76], facecolor=BG_COLOR)
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(-0.03, 1.06)
    ax.set_ylim(-0.04, 1.055)

    # Boundary frame [0,1]²
    # V17-E: 第四段曾为 [[1,1],[0,0]]（y 从 0 到 0 的退化点），右边从未画出
    for seg in ([[0, 1], [0, 0]], [[0, 0], [0, 1]], [[0, 1], [1, 1]], [[1, 1], [1, 0]]):
        ax.plot(seg[0], seg[1], color=FRAME_COLOR, linewidth=1.2, zorder=1)

    # Grid: faint decile grid + 10^x magnitude lines (positions = x(10^x))
    for v in [i / 10 for i in range(1, 10)]:
        ax.plot([0, 1], [v, v], color=GRID_COLOR, linewidth=0.4, zorder=0)
        ax.plot([v, v], [0, 1], color=GRID_COLOR, linewidth=0.4, zorder=0)
    decade_lines = [d["x"] for d in mapping_meta.get("decade_ticks", [])
                    if 0.008 < d["x"] < 0.985]
    for xv in decade_lines:
        ax.plot([xv, xv], [0, 1], color=DECADE_GRID_COLOR, linewidth=0.8, zorder=0)

    # X ticks: 0 (left edge, c=0) + 10^x indicators at x(10^x)
    tick_pos, tick_lab = [0.0], ["0"]
    last = 0.0
    for d in mapping_meta.get("decade_ticks", []):
        xv = d["x"]
        if xv < 0.008 or xv > 1.0005 or xv - last < 0.009:
            continue
        tick_pos.append(xv)
        tick_lab.append(_fmt_cost_tick(d["price"]))
        last = xv
    ax.set_xticks(tick_pos)
    ax.set_xticklabels(tick_lab, color=TEXT_COLOR, fontsize=8)
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_yticklabels(["0", "0.25", "0.50", "0.75", "1"], color=TEXT_COLOR, fontsize=8)
    ax.tick_params(axis='both', colors=MUTED_TEXT_COLOR, length=4, width=0.8)

    # ── Axis labels / suptitle / footnote（先创建，供标签避让测量）────────
    y0 = mapping_meta.get("y_axis", {}).get("baseline", 0.0)
    n_vis = mapping_meta.get("plotted_models", 0)
    n_knots = mapping_meta.get("knots", 0)
    ax.set_xlabel(
        "单请求成本 c — 分位数映射（等密度：任意等宽区段模型数恒定，"
        f"每 0.1 宽约 {n_vis / 10:.0f} 个；函数端点 (0,0) 与 (1,1)；"
        f"{n_knots} 个入图正成本模型经验分布线性插值；左端 c = 0 免费模型）",
        fontsize=12, color=TEXT_COLOR, labelpad=8, fontweight="bold")
    ax.set_ylabel(f"综合能力（0 = 总体帕累托前沿第一级 y0={y0:.3f}，1 = 最优）",
                  fontsize=12, color=TEXT_COLOR, labelpad=10, fontweight="bold")
    st = fig.suptitle(
        "LLM 综合能力 vs 单请求成本 — Pareto 前沿\n"
        "灰线 = 总体前沿 | 彩色细线 = 11 品牌前沿 | 横轴 = 分位数映射（等密度，端点 (0,0)/(1,1)）",
        fontsize=14, color=TEXT_COLOR, fontweight="bold", x=0.36, y=0.988,
        ha="center", va="top",
    )
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.grid(False)

    # ── Legend: 右侧留白区（黑底样式）──────────────────────────────────
    from matplotlib.lines import Line2D
    n_others = sum(1 for m in plot_models
                   if id(m) not in pareto_names and id(m) not in brand_line_models)
    handles = [
        Line2D([0], [0], marker='o', color='none', markerfacecolor=CLOUD_COLOR,
               markersize=4.5, alpha=0.6, label=f"其他模型 ({n_others})"),
        Line2D([0], [0], color=OVERALL_LINE_COLOR, linewidth=LW_OVERALL,
               marker='o', markerfacecolor=OVERALL_LINE_COLOR, markersize=5.5,
               label=f"总体帕累托前沿 ({len(pareto)})"),
    ]
    for brand in BRAND_LINE_CREATORS:
        fr = brand_frontiers.get(brand)
        if not fr:
            continue
        color = fr[0].get("creator_color") or "#888888"
        disp = BRAND_DISPLAY_NAMES.get(brand, brand)
        h = Line2D([0], [0], color=color, linewidth=1.4,
                   marker='o', markerfacecolor=color, markersize=5,
                   markeredgecolor='white' if _is_dark_color(color) else 'none',
                   markeredgewidth=0.6, label=f"{disp} ({len(fr)})")
        if _is_dark_color(color):
            h.set_path_effects([pe.withStroke(linewidth=2.4, foreground="white")])
        handles.append(h)
    legend = fig.legend(handles=handles, loc='center right', bbox_to_anchor=(0.995, 0.5),
                        fontsize=9.5, framealpha=0.92, edgecolor=FRAME_COLOR,
                        facecolor="#111116", labelcolor=TEXT_COLOR, borderpad=0.9)

    # 底部说明文字
    n_free = mapping_meta.get("free_models", 0)
    n_total = mapping_meta.get("total_models", len(models))
    method = (
        f"X轴: 分位数映射 x = Q(log10 c) — {n_knots} 个入图正成本模型的经验分布线性插值; "
        f"等密度(每 0.1 宽 ≈ {n_vis / 10:.0f} 个模型), 端点钉死 (0,0)/(1,1); "
        f"10^x 指示位于 x(10^x); 同倍率区间宽度 ∝ 该区间模型数 | "
        f"Y轴: 综合能力({len(METRIC_FIELDS)}指标均值; 0 = 总体前沿第一级 y0={y0:.3f}, 1 = 最优; "
        f"低于第一级的模型不入图) | "
        f"成本 = CacheHit·CacheHitPrice + (1-CacheHit)·CacheWritePrice + Speed·RealTime·OutputPrice | "
        f"入图 {len(plot_models)}/{n_total} 模型(含{n_free}个免费)"
    )
    footnote = fig.text(0.36, 0.016, method, ha="center", va="bottom", fontsize=6.5,
                        color=MUTED_TEXT_COLOR, style="italic")

    # V17-B: 内嵌字体字符覆盖检查（缺字会回退/变方块，日志中显式警告）
    check_font_coverage(
        [st.get_text(), ax.xaxis.label.get_text(), ax.yaxis.label.get_text(),
         footnote.get_text()] + tick_lab
        + [h.get_label() for h in handles]
        + [m["chart_label"] for m in plot_models if m.get("chart_label")])

    # ── V12 标签流程：先放置（供连线断开计算），再画断线、圆点、文字 ────
    fig.canvas.draw()   # renderer ready, exclusions measurable
    exclusions = [legend, st, ax.xaxis.label, ax.yaxis.label, footnote]
    exclusions += list(ax.get_xticklabels()) + list(ax.get_yticklabels())
    placements = _place_labels(ax, fig, plot_models, pareto, brand_frontiers, exclusions)
    _draw_pareto_lines(ax, placements, pareto, brand_frontiers)
    _draw_markers(ax, plot_models, pareto, brand_frontiers)
    _draw_label_texts(ax, placements)

    out = os.path.join(OUTPUT_DIR, "pareto_analysis.png")
    plt.savefig(out, dpi=200, facecolor=BG_COLOR)
    plt.close()
    print(f"Plot saved to {out}")


# ══════════════════════════════════════════════════════════════════════
# V11 label layout: labels ride ON the Pareto lines (要求二)
# ══════════════════════════════════════════════════════════════════════

_PAD = 2.5       # 标签碰撞检测外扩 (px, 画布 dpi)
_EXCL_PAD = 4.0  # 禁区（图例/标题/轴标签/刻度/脚注）外扩 (px)


def _marker_size(m, pareto_ids, brand_line_ids):
    """Marker area (pt²) — V11 缩小版元素。"""
    if id(m) in brand_line_ids:
        return MS_BRAND_GLOBAL if id(m) in pareto_ids else MS_BRAND
    if id(m) in pareto_ids:
        return MS_OTHER_GLOBAL
    return MS_CLOUD


def _unit(x, y):
    L = math.hypot(x, y)
    return (x / L, y / L) if L > 1e-9 else (1.0, 0.0)


def _norm_angle(angle_deg):
    """把文字旋转角规范到 (-90, 90]，避免上下颠倒。"""
    while angle_deg > 90:
        angle_deg -= 180
    while angle_deg <= -90:
        angle_deg += 180
    return angle_deg


def _obb_specs(cx, cy, w, h, angle_deg):
    """旋转矩形 (OBB) 的快速碰撞规格。"""
    a = math.radians(angle_deg)
    ux, uy = math.cos(a), math.sin(a)
    nx, ny = -uy, ux
    hw, hh = w / 2.0, h / 2.0
    return {
        "cx": cx, "cy": cy, "ux": ux, "uy": uy, "nx": nx, "ny": ny,
        "hw": hw, "hh": hh, "r": math.hypot(hw, hh), "r2": hw * hw + hh * hh,
    }


def _obb_hits_obb(o1, o2):
    dxc, dyc = o2["cx"] - o1["cx"], o2["cy"] - o1["cy"]
    rr = o1["r"] + o2["r"]
    if dxc * dxc + dyc * dyc > rr * rr:
        return False
    for ax, ay in ((o1["ux"], o1["uy"]), (o1["nx"], o1["ny"]),
                   (o2["ux"], o2["uy"]), (o2["nx"], o2["ny"])):
        c1 = o1["cx"] * ax + o1["cy"] * ay
        c2 = o2["cx"] * ax + o2["cy"] * ay
        e1 = (o1["hw"] * abs(o1["ux"] * ax + o1["uy"] * ay)
              + o1["hh"] * abs(o1["nx"] * ax + o1["ny"] * ay))
        e2 = (o2["hw"] * abs(o2["ux"] * ax + o2["uy"] * ay)
              + o2["hh"] * abs(o2["nx"] * ax + o2["ny"] * ay))
        if abs(c2 - c1) > e1 + e2:
            return False
    return True


def _obb_hits_aabb(o, box):
    x0, y0, x1, y1 = box
    if (o["cx"] + o["r"] < x0 or o["cx"] - o["r"] > x1
            or o["cy"] + o["r"] < y0 or o["cy"] - o["r"] > y1):
        return False
    corners = ((x0, y0), (x1, y0), (x1, y1), (x0, y1))
    for ax, ay, half in ((o["ux"], o["uy"], o["hw"]), (o["nx"], o["ny"], o["hh"])):
        c = o["cx"] * ax + o["cy"] * ay
        ps = [px * ax + py * ay for px, py in corners]
        if min(ps) > c + half or max(ps) < c - half:
            return False
    for c, ext, b0, b1 in ((o["cx"], o["hw"] * abs(o["ux"]) + o["hh"] * abs(o["nx"]), x0, x1),
                           (o["cy"], o["hw"] * abs(o["uy"]) + o["hh"] * abs(o["ny"]), y0, y1)):
        if c + ext < b0 or c - ext > b1:
            return False
    return True


def _obb_hits_circle(o, cx, cy, r):
    dx, dy = cx - o["cx"], cy - o["cy"]
    rr = o["r"] + r
    if dx * dx + dy * dy > rr * rr:
        return False
    lx = dx * o["ux"] + dy * o["uy"]
    ly = dx * o["nx"] + dy * o["ny"]
    qx = max(-o["hw"], min(o["hw"], lx))
    qy = max(-o["hh"], min(o["hh"], ly))
    return (lx - qx) ** 2 + (ly - qy) ** 2 <= r * r


def _label_color(m):
    col = m.get("creator_color") or "#B0B0B8"
    try:
        to_rgb(col)
        return col
    except Exception:
        return "#B0B0B8"


def _gen_candidates(m, P, R, w, h, pi_j, polylines, rad):
    """V16 标签候选阶梯 —— 按用户指定的四级优先流程产出 (cx, cy, ang, kind)：

    1. online  骑在点旁的两条连线段上：右（去路 P→Q）与左（来路 A→P）
       两侧均可，沿线就近扫描；同一条线段允许容纳两个标签——各贴各的
       点，位置够就行；两侧都空时先右侧（尽量单独放）。
    2. offset  实在骑不上线：在「假设线能放下该标签」的离点最近位置的
       上方或下方、与线平行摆放（右/左侧 × 上/下方四组合，垂直间距就
       近优先；互相掣肘的标签自然错开成对角组合）。
    3. extend  仍放不下：点的两条连线延长线上的最近点（来路方向越过
       点继续前延 + 去路方向越过点向后延），沿线就近扫描。
    4. sector  仍放不下：两条连线夹角形成的扇区（去路射线逆时针扫到
       来路反向射线——即连线的前上方空白区）内按到点距离就近扫描，
       文字保持与更贴近的那条连线平行。

    注：V11–V15 的「后方线段」候选实际生成在 P 点前方（来路方向的延
    长线上），标签从未真正落在点左侧的 A–P 线段上；V16 修正该方向并
    按上述四级优先重排全部候选。
    """
    ONL_CAP = 80.0    # 骑线扫描离点距离上限（「在点的旁边」限制）
    EXT_CAP = 110.0   # 延长线扫描距离
    SEC_RMAX = 135.0  # 扇区扫描最大半径

    def _ang(read):
        return _norm_angle(math.degrees(math.atan2(read[1], read[0])))

    segs = []          # (side, read, L, Rfar)：side ∈ {"out","in"}
    if pi_j is not None:
        pi, j = pi_j
        pl = polylines[pi]
        pts, ids, n = pl["pts"], pl["ids"], len(pl["pts"])
        if j + 1 < n:  # 右侧：P → Q（文字沿 P→Q 阅读方向）
            q = pts[j + 1]
            segs.append(("out", _unit(q[0] - P[0], q[1] - P[1]),
                         math.hypot(q[0] - P[0], q[1] - P[1]),
                         rad[ids[j + 1]] + 2.0))
        if j >= 1:     # 左侧：A → P（文字沿 A→P 阅读方向）
            a = pts[j - 1]
            segs.append(("in", _unit(P[0] - a[0], P[1] - a[1]),
                         math.hypot(P[0] - a[0], P[1] - a[1]),
                         rad[ids[j - 1]] + 2.0))

    if not segs:
        # 无折线（罕见）：对角方向兜底（延伸 + 偏移 + 上半扇区）
        diag = _unit(1.0, 0.85)
        ang0 = _norm_angle(40.4)
        nrm = (-diag[1], diag[0])
        yield (P[0] + diag[0] * (R + 2.0 + w / 2),
               P[1] + diag[1] * (R + 2.0 + w / 2), ang0, "extend")
        for dperp in (h / 2 + R + 3.0, h / 2 + R + 9.0,
                      h / 2 + R + 16.0, h / 2 + R + 26.0):
            for perp in (1, -1):
                for t in (R + 1.0, R + 1.0 + w * 0.45):
                    yield (P[0] + diag[0] * (t + w / 2) + nrm[0] * perp * dperp,
                           P[1] + diag[1] * (t + w / 2) + nrm[1] * perp * dperp,
                           ang0, "offset")
        for r in (R + h / 2 + 6.0, 22.0, 36.0, 52.0, 72.0, 96.0, 126.0):
            for adeg in (90, 75, 105, 60, 120, 45, 135, 30, 150, 15, 165):
                th = math.radians(adeg)
                yield (P[0] + r * math.cos(th), P[1] + r * math.sin(th),
                       ang0, "sector")
        return

    # ── 1) 骑线：右/左两侧沿线就近扫描；两侧按【离点距离】归并
    #    （同距先右侧）—— 出侧近处被占时，入侧的近位优先于出侧的
    #    远位（V16-C：此前先扫完整条出侧才试入侧，标签被推得很远）。
    onl = []
    for s_rank, (side, read, L, Rfar) in enumerate(segs):
        sgn = 1.0 if side == "out" else -1.0
        ang = _ang(read)
        t_lo = R + 1.0
        # V16-B/C：圆点检查用 slim 盒（rad-2.0）—— 外端只需让文字盒
        # 错开远端圆点即可，可比 V11 的保守估计多用约 4px 线段长。
        t_hi = L - w - Rfar + 3.0
        if t_hi < t_lo:
            continue
        t_cap = min(t_hi, t_lo + ONL_CAP)
        ts = []
        t = t_lo
        while t < t_cap:
            ts.append(t)
            t += 5.0
        ts.append(t_cap)
        for t in ts:
            onl.append((t, s_rank,
                        P[0] + sgn * read[0] * (t + w / 2),
                        P[1] + sgn * read[1] * (t + w / 2), ang))
    for (_t, _sr, cx, cy, ang) in sorted(onl, key=lambda c: (c[0], c[1])):
        yield (cx, cy, ang, "online")

    # ── 2) 平行偏移：离点最近位置的上方/下方（四组合，间距就近）──
    for dperp in (h / 2 + R + 3.0, h / 2 + R + 9.0,
                  h / 2 + R + 16.0, h / 2 + R + 26.0):
        for (side, read, L, Rfar) in segs:
            sgn = 1.0 if side == "out" else -1.0
            ang = _ang(read)
            nrm = (-read[1], read[0])   # +1 = 阅读方向左侧（线的上方）
            for perp in (1, -1):
                for t in (R + 1.0, R + 1.0 + w * 0.45):
                    cx = P[0] + sgn * read[0] * (t + w / 2) + nrm[0] * perp * dperp
                    cy = P[1] + sgn * read[1] * (t + w / 2) + nrm[1] * perp * dperp
                    yield (cx, cy, ang, "offset")

    # ── 3) 延长线：来路越过点前延 + 去路越过点后延，就近扫描 ──────
    exts = []
    for (side, read, L, Rfar) in reversed(segs):
        if side == "in":
            exts.append((read[0], read[1], _ang(read)))       # A→P 继续向前
        else:
            exts.append((-read[0], -read[1], _ang(read)))     # P→Q 反向越过 P
    for (dx, dy, ang) in exts:
        t = R + 2.0
        while t <= EXT_CAP:
            yield (P[0] + dx * (t + w / 2), P[1] + dy * (t + w / 2),
                   ang, "extend")
            t += 6.0

    # ── 4) 扇区：两连线夹角的前上方空白区，就近极坐标扫描 ──────────
    out_seg = next((s for s in segs if s[0] == "out"), None)
    in_seg = next((s for s in segs if s[0] == "in"), None)
    if out_seg is not None and in_seg is not None:
        d_out, d_in = out_seg[1], in_seg[1]
        lo = math.atan2(d_out[1], d_out[0])
        hi = math.atan2(-d_in[1], -d_in[0])
        a1, a2 = _ang(d_out), _ang(d_in)
        r1, r2 = d_out, (-d_in[0], -d_in[1])
    elif out_seg is not None:
        d_out = out_seg[1]
        lo = math.atan2(d_out[1], d_out[0])
        hi = lo + math.pi
        a1 = a2 = _ang(d_out)
        r1 = r2 = d_out
    else:
        d_in = in_seg[1]
        lo = math.atan2(d_in[1], d_in[0])
        hi = lo + math.pi
        a1 = a2 = _ang(d_in)
        r1 = r2 = d_in
    sweep = (hi - lo) % (2.0 * math.pi)
    if sweep < 1e-6:
        sweep = 2.0 * math.pi
    n_step = max(7, min(31, int(math.degrees(sweep) / 8.0) + 1))
    pool = []
    r = R + h / 2 + 4.0
    while r <= SEC_RMAX:
        for k in range(n_step):
            th = lo + sweep * k / (n_step - 1.0)
            dx, dy = math.cos(th), math.sin(th)
            c1 = abs(math.atan2(dx * r1[1] - dy * r1[0],
                                dx * r1[0] + dy * r1[1]))
            c2 = abs(math.atan2(dx * r2[1] - dy * r2[0],
                                dx * r2[0] + dy * r2[1]))
            ang = a1 if c1 <= c2 else a2
            pool.append((r, k, P[0] + dx * r, P[1] + dy * r, ang))
        r += 8.0
    for (_r, _k, cx, cy, ang) in pool:
        yield (cx, cy, ang, "sector")


def _place_labels(ax, fig, plot_models, pareto, brand_frontiers, exclusions):
    """V16 标签放置：四级优先流程（骑线〔含让位〕→ 平行偏移 → 延长
    线 → 扇区），候选细节见 _gen_candidates，主流程见 V16 注释段。
    V15：放置后按品牌序列做位置单调性修复（越靠右上的模型，标签
    重心必须同时更靠右且更靠上——两分量都 >= 0），详见 V15-A 段。

    碰撞对象：画布边界、图例/标题/轴标签/刻度/脚注（禁区）、已放置
    标签、前沿圆点。连线不参与碰撞——文字下方的连线会断开，仅在
    文字两侧绘制。
    """
    items = [m for m in plot_models if m.get("chart_label")]
    if not items:
        return []
    renderer = fig.canvas.get_renderer()
    W, H = fig.bbox.width, fig.bbox.height
    tr = ax.transData.transform

    pareto_ids = {id(p) for p in pareto}
    brand_line_ids = {id(m) for fr in brand_frontiers.values() for m in fr}

    dot, rad = {}, {}
    for m in plot_models:
        dot[id(m)] = tr((float(m["axis_x"]), float(m["chart_y"])))
        rad[id(m)] = math.sqrt(_marker_size(m, pareto_ids, brand_line_ids)) / 72.0 * fig.dpi / 2.0
    avoid = [(dot[id(m)][0], dot[id(m)][1], rad[id(m)])
             for m in plot_models if id(m) in pareto_ids or id(m) in brand_line_ids]

    excl = []
    for obj in exclusions:
        try:
            e = obj.get_window_extent(renderer)
            excl.append((e.x0 - _EXCL_PAD, e.y0 - _EXCL_PAD,
                         e.x1 + _EXCL_PAD, e.y1 + _EXCL_PAD))
        except Exception:
            pass

    # 文字尺寸（与最终绘制一致的字号/字重；长标签用小一号字体）
    meas = {}
    for m in items:
        fs = FS_LEVEL if len(m["chart_label"]) >= LABEL_LONG_LEN else FS_FULL
        t = ax.text(0.5, 0.5, m["chart_label"], fontsize=fs, fontweight="bold")
        bb = t.get_window_extent(renderer)
        meas[id(m)] = (bb.width, bb.height, fs, False)
        t.remove()

    # 折线（像素）：总体 + 各品牌（≥2 点）；模型 → (折线, 序号)，品牌折线优先
    # V12-C：顶点按 (axis_x, 综合能力升序) 排序 —— 成本相同（浮点精度内）
    # 的点自下而上连接，消除 Qwen3.8 Max→2.4T A95B、MiniMax M2.1→M2 的
    # 向下折返段（V11 稳定排序保留了能力降序导致先升后降）
    _vkey = lambda m: (float(m["axis_x"]), float(m["composite_ability"]))
    polylines = []
    pf_sorted = sorted(pareto, key=_vkey)
    polylines.append({"brand": None,
                      "pts": [dot[id(m)] for m in pf_sorted],
                      "ids": [id(m) for m in pf_sorted]})
    for brand in BRAND_LINE_CREATORS:
        fr = brand_frontiers.get(brand)
        if fr and len(fr) >= 2:
            fbs = sorted(fr, key=_vkey)
            polylines.append({"brand": brand,
                              "pts": [dot[id(m)] for m in fbs],
                              "ids": [id(m) for m in fbs]})
    loc = {}
    for pi, pl in enumerate(polylines):
        for j, mid in enumerate(pl["ids"]):
            if pl["brand"] is None:
                loc.setdefault(mid, (pi, j))
            else:
                loc[mid] = (pi, j)

    placed_obb = []

    def collide(obb, slack=1.5, slim=None):
        """违规计分；0 = 无碰撞。出画布/压禁区为大数（硬拒绝）。
        V16-B：圆点碰撞按候选类别分档 —— online 用「文字真实盒」
        （slim，不含 _PAD）对 rad-2.0（文字可以贴着圆点边缘掠过），
        offset 用 slim 盒对 rad+0.5，extend/sector 用外扩盒对 rad+1.5
        （默认，与 V11–V15 一致）。标签-标签 / 禁区 / 画布始终用外
        扩盒 obb。"""
        if (obb["cx"] - obb["r"] < 8 or obb["cx"] + obb["r"] > W - 8
                or obb["cy"] - obb["r"] < 8 or obb["cy"] + obb["r"] > H - 8):
            return 10 ** 6
        for b in excl:
            if _obb_hits_aabb(obb, b):
                return 10 ** 6
        score = 0
        for o in placed_obb:
            if _obb_hits_obb(obb, o):
                score += 10
        box = slim if slim is not None else obb
        for (cx, cy, r) in avoid:
            if _obb_hits_circle(box, cx, cy, r + slack):
                score += 20
        return score

    def _soft_blockers(obb, slim, slack):
        """返回仅被【标签】挡住的占用者 OBB 列表（可让位）；若有任何
        硬碰撞（画布/禁区/圆点〔slim 盒 + rad+slack〕）返回 None。"""
        if (obb["cx"] - obb["r"] < 8 or obb["cx"] + obb["r"] > W - 8
                or obb["cy"] - obb["r"] < 8 or obb["cy"] + obb["r"] > H - 8):
            return None
        for b in excl:
            if _obb_hits_aabb(obb, b):
                return None
        for (cx, cy, r) in avoid:
            if _obb_hits_circle(slim, cx, cy, r + slack):
                return None
        return [o for o in placed_obb if _obb_hits_obb(obb, o)]

    def _cand_ok(cx, cy, bw, bh, ang, kind):
        """按候选类别做相应严格度的零碰撞检查；通过返回 (obb, slim)。"""
        obb = _obb_specs(cx, cy, bw + 2 * _PAD, bh + 2 * _PAD, ang)
        if kind == "online":
            slim = _obb_specs(cx, cy, bw, bh, ang)
            return (obb, slim) if collide(obb, -2.0, slim) == 0 else None
        if kind == "offset":
            slim = _obb_specs(cx, cy, bw, bh, ang)
            return (obb, slim) if collide(obb, 0.5, slim) == 0 else None
        return (obb, None) if collide(obb) == 0 else None

    placements = []
    # V16-B：能力升序（自下而上）。降序会造成「入侧级联」——链条顶端
    # 标签先抢占下方共享线段，逐级把更低标签挤出侧。升序让每个标签
    # 自然取得自己的出侧（右/上方向），每段线段容纳其【低端】模型的
    # 标签 —— 正是用户要求的图式。
    order = sorted(items, key=lambda m: float(m["composite_ability"]))
    n_fallback = 0
    n_yield = 0
    dists = []

    def _reseat_online(p, avoid_obb):
        """V16 骑线让位：把已放置标签 p 挪到它自己的另一个骑线位置。
        候选 = p 的全部 online 候选（离 p 当前位置就近优先），新位置须
        零碰撞且不压 avoid_obb（后来者的目标位）。成功返回 True。"""
        m = p["model"]
        P0 = dot[id(m)]
        R0 = rad[id(m)] + 1.0
        w0, h0, _fs0, _lv0 = meas[id(m)]
        own = p["obb"]
        for k in range(len(placed_obb) - 1, -1, -1):
            if placed_obb[k] is own:
                placed_obb.pop(k)
                break
        cands = []
        for (cx, cy, ang, kind) in _gen_candidates(m, P0, R0, w0, h0,
                                                   loc.get(id(m)), polylines, rad):
            if kind != "online":
                break          # online 候选最优先产出，遇到其它类别即止
            cands.append((math.hypot(cx - P0[0], cy - P0[1]),
                          math.hypot(cx - p["cx"], cy - p["cy"]),
                          cx, cy, ang, kind))
        cands.sort(key=lambda c: (c[0], c[1]))
        for (_d0, _d1, cx, cy, ang, kind) in cands:
            chk = _cand_ok(cx, cy, w0, h0, ang, kind)
            if chk is None:
                continue
            obb = chk[0]
            if _obb_hits_obb(obb, avoid_obb):
                continue
            p["cx"], p["cy"], p["angle"], p["kind"], p["obb"] = (
                cx, cy, ang, kind, obb)
            obb["owner"] = p
            placed_obb.append(obb)
            return True
        placed_obb.append(own)
        return False

    # ── V16 主放置流程（用户指定的四级优先 + 骑线让位）────────────
    # ① 能骑线的尽量骑线：点的右侧/左侧沿线就近扫描，同一条线段允许
    #    容纳两个标签（各贴各的点）；目标位仅被其他标签占据时先让位
    #    ——占用者挪到它自己的另一个骑线位，双方都保持骑线。
    # ② 实在骑不上线：在「假设线能放下该标签」的离点最近位置的上方
    #    或下方平行摆放（右/左侧 × 上/下方四组合）。
    # ③ 仍放不下：点的两条连线延长线上就近分布。
    # ④ 仍放不下：两条连线夹角扇区（前上方空白区）内就近。
    # 兜底：全候选最小碰撞者（与 V12 起一致，零碰撞不可得时才启用）。
    recs = {}
    for m in order:
        w, h, fs, _lvl = meas[id(m)]
        color = _label_color(m)
        rec = {"model": m, "text": m["chart_label"], "fs": fs,
               "brand": m.get("creator"), "full_name": m.get("full_name"),
               "color": color, "halo": _is_dark_color(color),
               "cx": 0.0, "cy": 0.0, "w": w, "h": h, "angle": 0.0,
               "obb": None, "kind": None}
        got = None
        gen = list(_gen_candidates(m, dot[id(m)], rad[id(m)] + 1.0, w, h,
                                   loc.get(id(m)), polylines, rad))
        failed_sets = set()
        for (cx, cy, ang, kind) in gen:
            if kind != "online":
                break
            obb = _obb_specs(cx, cy, w + 2 * _PAD, h + 2 * _PAD, ang)
            slim = _obb_specs(cx, cy, w, h, ang)
            bl = _soft_blockers(obb, slim, -2.0)
            if bl is None:
                continue        # 圆点/禁区/画布硬阻挡：让位解决不了
            if not bl:
                got = (cx, cy, ang, kind, obb)
                break
            key = frozenset(id(o) for o in bl)
            if key in failed_sets:
                continue        # 同一组占用者已试过让位且失败
            moved = []
            ok = True
            for ob in bl:
                q = ob.get("owner")
                if q is None:
                    ok = False
                    break
                orig = (q["cx"], q["cy"], q["angle"], q["kind"], q["obb"])
                if not _reseat_online(q, obb):
                    ok = False
                    break
                moved.append((q,) + orig)
            if ok and not _soft_blockers(obb, slim, -2.0):
                got = (cx, cy, ang, kind, obb)
                n_yield += len(moved)
                break
            failed_sets.add(key)
            for (q, cx0, cy0, ang0, kind0, obb0) in moved:
                for k in range(len(placed_obb) - 1, -1, -1):
                    if placed_obb[k] is q["obb"]:
                        placed_obb.pop(k)
                        break
                q["cx"], q["cy"], q["angle"], q["kind"], q["obb"] = (
                    cx0, cy0, ang0, kind0, obb0)
                placed_obb.append(obb0)
        if got is None:
            for (cx, cy, ang, kind) in gen:
                if kind == "online":
                    continue
                chk = _cand_ok(cx, cy, w, h, ang, kind)
                if chk is not None:
                    got = (cx, cy, ang, kind, chk[0])
                    break
        if got is None:
            best = None
            for (cx, cy, ang, kind) in gen:
                obb = _obb_specs(cx, cy, w + 2 * _PAD, h + 2 * _PAD, ang)
                if kind == "online":
                    slim = _obb_specs(cx, cy, w, h, ang)
                    s = collide(obb, -2.0, slim)
                elif kind == "offset":
                    slim = _obb_specs(cx, cy, w, h, ang)
                    s = collide(obb, 0.5, slim)
                else:
                    s = collide(obb)
                if best is None or s < best[0]:
                    best = (s, cx, cy, ang, kind, obb)
            if best is not None:
                got = best[1:]
                n_fallback += 1
        if got is not None:
            cx, cy, ang, kind, obb = got
            rec.update(cx=cx, cy=cy, angle=ang, kind=kind, obb=obb)
            obb["owner"] = rec
            placed_obb.append(obb)
            recs[id(m)] = rec
    placements = [recs[id(m)] for m in order if id(m) in recs]

    # V16 诊断：导出主放置流程刚结束（未做单调性修复）的初始布局
    try:
        with open(os.path.join(OUTPUT_DIR, "label_placements_initial.json"), "w", encoding="utf-8") as fh:
            json.dump([{k: p[k] for k in ("text", "fs", "brand", "full_name",
                            "cx", "cy", "w", "h", "angle", "kind")}
                       for p in placements], fh, ensure_ascii=False, indent=1)
    except Exception:
        pass

    # ── V15-A：品牌序列标签位置单调性（两分量同时非负）─────────────────
    # 用户规则（V15 加强）：同一品牌前沿中，越靠右上的模型，其标签重心
    # 必须同时更靠右且更靠上 —— 相邻对 A→B 的标签位移 (dx, dy) 须满足
    # dx >= -TOL_MONO 且 dy >= -TOL_MONO：两者同时满足、至少是 (0,0)，
    # 只要有一个分量非负不算合格（V14 的投影规则放过 "+71/-58 更右
    # 但更低" 这类情形，V15 起一律视为违反；等成本堆叠退化为「上方的
    # 模型标签既在上方、也不更左」）。违反时就近重摆：先试 B（新位置
    # 两分量同时 >= A 的标签，且不翻越当前仍同向的后继），失败再对称
    # 试 A（须 <= B 的标签、不翻越当前仍同向的前驱）；要求无碰撞、离
    # 自身圆点最近、优先骑线。最多迭代 6 轮；修不好的配对记入
    # mono_unresolved 报告。
    TOL_MONO = 1.0

    def _dots_equal(mA, mB):
        return (math.hypot(dot[id(mB)][0] - dot[id(mA)][0],
                           dot[id(mB)][1] - dot[id(mA)][1]) <= 1e-9)

    def _mono_bad(A, B):
        return (B["cx"] - A["cx"] < -TOL_MONO
                or B["cy"] - A["cy"] < -TOL_MONO)

    def _try_reseat(p, cons):
        """就地重摆标签 p。cons = [(rx, ry, sx, sy)]，sx/sy ∈ {+1,-1,0}：
        要求 (cx-rx)*sx >= -TOL_MONO 且 (cy-ry)*sy >= -TOL_MONO ——
        两分量同时满足的盒式约束（0 = 该轴不限）。成功返回 True。"""
        m = p["model"]
        P0 = dot[id(m)]
        R0 = rad[id(m)] + 1.0
        w0, h0, _fs0, _lv0 = meas[id(m)]
        own = p["obb"]
        for k in range(len(placed_obb) - 1, -1, -1):
            if placed_obb[k] is own:
                placed_obb.pop(k)
                break
        # V16：候选生成器已按「骑线 → 平行偏移 → 延长线 → 扇区」的
        # 优先级有序产出，直接按产出顺序尝试（不再按距离重排）。
        cands = [(0, math.hypot(cx - P0[0], cy - P0[1]), cx, cy, ang, kind)
                 for (cx, cy, ang, kind) in _gen_candidates(
                     m, P0, R0, w0, h0, loc.get(id(m)), polylines, rad)]
        got = None
        for _tier, _d, cx, cy, ang, kind in cands:
            ok = True
            for (rx, ry, sx, sy) in cons:
                if sx != 0 and (cx - rx) * sx < -TOL_MONO:
                    ok = False
                    break
                if sy != 0 and (cy - ry) * sy < -TOL_MONO:
                    ok = False
                    break
            if not ok:
                continue
            chk = _cand_ok(cx, cy, w0, h0, ang, kind)
            if chk is not None:
                got = (cx, cy, ang, kind, chk[0])
                break
        if got is None:
            placed_obb.append(own)
            return False
        p["cx"], p["cy"], p["angle"], p["kind"], p["obb"] = got
        placed_obb.append(got[4])
        return True

    pl_by_id = {id(p["model"]): p for p in placements}
    chains = []
    for brand in BRAND_LINE_CREATORS:
        fr = brand_frontiers.get(brand)
        if fr and len(fr) >= 2:
            ch = [pl_by_id[id(m)] for m in sorted(fr, key=_vkey)
                  if id(m) in pl_by_id]
            if len(ch) >= 2:
                chains.append((brand, ch))

    n_mono_moved = 0
    mono_unresolved = []
    for _rnd in range(6):
        viol = []
        for brand, ch in chains:
            for i in range(len(ch) - 1):
                if _dots_equal(ch[i]["model"], ch[i + 1]["model"]):
                    continue  # 圆点完全重合：无「更靠右上」次序可言
                if _mono_bad(ch[i], ch[i + 1]):
                    viol.append((brand, ch, i))
        mono_unresolved = []
        if not viol:
            break
        progressed = False
        for brand, ch, i in viol:
            A, B = ch[i], ch[i + 1]
            if not _mono_bad(A, B):
                continue  # 本轮早先的修复已顺带恢复该对
            # 先重摆 B：新位置两分量同时 >= A 的标签；对后继仅在当前
            # 仍同向的轴上设上限（不把 B 摆到后继之上/之右）
            consB = [(A["cx"], A["cy"], 1, 1)]
            if i + 2 < len(ch):
                nxt = ch[i + 2]
                sxN = -1 if nxt["cx"] >= B["cx"] - TOL_MONO else 0
                syN = -1 if nxt["cy"] >= B["cy"] - TOL_MONO else 0
                if sxN or syN:
                    consB.append((nxt["cx"], nxt["cy"], sxN, syN))
            if _try_reseat(B, consB):
                n_mono_moved += 1
                progressed = True
                continue
            # 失败再对称重摆 A：新位置两分量同时 <= B 的标签；对前驱仅
            # 在当前仍同向的轴上设下限
            consA = [(B["cx"], B["cy"], -1, -1)]
            if i >= 1:
                prv = ch[i - 1]
                sxP = 1 if prv["cx"] <= A["cx"] + TOL_MONO else 0
                syP = 1 if prv["cy"] <= A["cy"] + TOL_MONO else 0
                if sxP or syP:
                    consA.append((prv["cx"], prv["cy"], sxP, syP))
            if _try_reseat(A, consA):
                n_mono_moved += 1
                progressed = True
            else:
                mono_unresolved.append((brand, A["text"], B["text"],
                                        round(B["cx"] - A["cx"]),
                                        round(B["cy"] - A["cy"])))
        if not progressed:
            break

    # ── V15-B：窗口级联重排（单标签盒约束无解时）───────────────────
    # 修不动的配对往往是被前后邻居标签夹死（局部盒为空，如 Fable-high
    # 的标签夹在 (xhigh) 与 Opus (max) 之间且上下颠倒）—— 需要把相邻
    # 标签一起挪：以违规对为中心取链窗口并逐级扩大，窗口内标签全部
    # 摘下后按链序重摆，每个标签两分量同时 ≥ 窗口内前一个；首/尾标签
    # 不破坏与窗口外前驱/后继原已同向的轴。任一标签摆不下则整窗恢复
    # 原状、窗口再扩大一级重试（直至整链）。

    def _place_one(p, cons):
        """为已摘下的标签 p 就近找位（窗口重排用）。候选：原位（满足
        约束即不动）→ 骑线/延伸 → 就近扫描/偏移 → 原位按约束夹紧后
        ±96px 细网格平移（角取原角或 0°）。成功更新 p 并注册 obb。"""
        m = p["model"]
        P0 = dot[id(m)]
        R0 = rad[id(m)] + 1.0
        w0, h0, _fs0, _lv0 = meas[id(m)]

        def _okc(cx, cy):
            for (rx, ry, sx, sy) in cons:
                if sx != 0 and (cx - rx) * sx < -TOL_MONO:
                    return False
                if sy != 0 and (cy - ry) * sy < -TOL_MONO:
                    return False
            return True

        cands = [(0, -1.0, p["cx"], p["cy"], p["angle"], p["kind"])]
        pool = []
        # V16：生成器顺序 = 优先级顺序（骑线 → 偏移 → 延长线 → 扇区）
        for (cx, cy, ang, kind) in _gen_candidates(m, P0, R0, w0, h0,
                                                   loc.get(id(m)), polylines, rad):
            cands.append((1, math.hypot(cx - P0[0], cy - P0[1]),
                          cx, cy, ang, kind))
        # 约束导向平移：把原位夹进约束盒，±96px 细网格微调
        tx, ty = p["cx"], p["cy"]
        for (rx, ry, sx, sy) in cons:
            if sx == 1 and tx < rx:
                tx = rx
            elif sx == -1 and tx > rx:
                tx = rx
            if sy == 1 and ty < ry:
                ty = ry
            elif sy == -1 and ty > ry:
                ty = ry
        for angT in (p["angle"], 0.0):
            for ddx in range(-96, 97, 12):
                for ddy in range(-96, 97, 12):
                    pool.append((math.hypot(tx + ddx - P0[0],
                                            ty + ddy - P0[1]),
                                 tx + ddx, ty + ddy, angT, "scan"))
        pool.sort(key=lambda c: c[0])
        cands.extend((1,) + c for c in pool)
        for _tier, _d, cx, cy, ang, kind in cands:
            if not _okc(cx, cy):
                continue
            chk = _cand_ok(cx, cy, w0, h0, ang, kind)
            if chk is not None:
                obb = chk[0]
                p["cx"], p["cy"], p["angle"], p["kind"], p["obb"] = (
                    cx, cy, ang, kind, obb)
                obb["owner"] = p
                placed_obb.append(obb)
                return True
        return False

    def _reflow_window(ch, lo, hi):
        """重排 ch[lo..hi]（含端点）。成功返回 True；失败整窗恢复原状。"""
        win = ch[lo:hi + 1]
        orig = [(p, p["cx"], p["cy"], p["angle"], p["kind"], p["obb"])
                for p in win]
        ext_lo = ch[lo - 1] if lo > 0 else None
        ext_hi = ch[hi + 1] if hi + 1 < len(ch) else None
        for (_p, _x, _y, _a, _kd, ob) in orig:
            for q in range(len(placed_obb) - 1, -1, -1):
                if placed_obb[q] is ob:
                    placed_obb.pop(q)
                    break
        newly = []
        ok = True
        for k, p in enumerate(win):
            cons = []
            if k == 0 and ext_lo is not None:
                sx0 = 1 if ext_lo["cx"] <= orig[0][1] + TOL_MONO else 0
                sy0 = 1 if ext_lo["cy"] <= orig[0][2] + TOL_MONO else 0
                if sx0 or sy0:
                    cons.append((ext_lo["cx"], ext_lo["cy"], sx0, sy0))
            if k > 0:
                cons.append((win[k - 1]["cx"], win[k - 1]["cy"], 1, 1))
            if k == len(win) - 1 and ext_hi is not None:
                sxN = -1 if ext_hi["cx"] >= orig[-1][1] - TOL_MONO else 0
                syN = -1 if ext_hi["cy"] >= orig[-1][2] - TOL_MONO else 0
                if sxN or syN:
                    cons.append((ext_hi["cx"], ext_hi["cy"], sxN, syN))
            if _place_one(p, cons):
                newly.append(p["obb"])
            else:
                ok = False
                break
        if not ok:
            for ob in newly:
                for q in range(len(placed_obb) - 1, -1, -1):
                    if placed_obb[q] is ob:
                        placed_obb.pop(q)
                        break
            for (p, cx, cy, a, kd, ob) in orig:
                p["cx"], p["cy"], p["angle"], p["kind"], p["obb"] = (
                    cx, cy, a, kd, ob)
                placed_obb.append(ob)
            return False
        return True

    def _reflow_escalating(ch, i):
        lo, hi = i, i + 1
        while True:
            if _reflow_window(ch, lo, hi):
                return True
            if lo == 0 and hi >= len(ch) - 1:
                return False
            lo = max(0, lo - 1)
            hi = min(len(ch) - 1, hi + 1)

    n_reflow = 0
    for _brr in range(4):
        _bad = []
        for brand, ch in chains:
            for i in range(len(ch) - 1):
                if _dots_equal(ch[i]["model"], ch[i + 1]["model"]):
                    continue
                if _mono_bad(ch[i], ch[i + 1]):
                    _bad.append((brand, ch, i))
        if not _bad:
            break
        _prog = False
        for brand, ch, i in _bad:
            if not _mono_bad(ch[i], ch[i + 1]):
                continue
            if _reflow_escalating(ch, i):
                n_reflow += 1
                _prog = True
        if not _prog:
            break

    # 最终未解决清单（V15-A 单标签重摆 + V15-B 窗口重排后仍违反的配对）
    mono_unresolved = []
    for brand, ch in chains:
        for i in range(len(ch) - 1):
            if _dots_equal(ch[i]["model"], ch[i + 1]["model"]):
                continue
            if _mono_bad(ch[i], ch[i + 1]):
                mono_unresolved.append((brand, ch[i]["text"], ch[i + 1]["text"],
                                        round(ch[i + 1]["cx"] - ch[i]["cx"]),
                                        round(ch[i + 1]["cy"] - ch[i]["cy"])))

    # ── V16-D：就近收紧遍 ─────────────────────────────────────────
    # 单调性修复（单标签重摆 / 窗口重排）可能把标签挪得很远。对离点
    # 超过 60px 的标签，在保持与链前后邻居同向（单调性不被破坏）且
    # 零碰撞的前提下再就近重摆一次；仅当新位置显著更近（>5px）时接
    # 受。按离点距离降序、多轮迭代（先收紧远处标签可能为近处标签腾
    # 出空间）。
    nbr = {}
    for _br, ch in chains:
        for k, p in enumerate(ch):
            nbr[id(p["model"])] = (ch[k - 1] if k > 0 else None,
                                   ch[k + 1] if k + 1 < len(ch) else None)

    def _tighten(p):
        m = p["model"]
        P0 = dot[id(m)]
        d_old = math.hypot(p["cx"] - P0[0], p["cy"] - P0[1])
        prev, nxt = nbr.get(id(m), (None, None))
        cons = []
        if prev is not None:
            cons.append((prev["cx"], prev["cy"], 1, 1))
        if nxt is not None:
            cons.append((nxt["cx"], nxt["cy"], -1, -1))
        if not cons:
            cons.append((P0[0] - 1e9, P0[1] - 1e9, 0, 0))  # 无约束占位
        snap = (p["cx"], p["cy"], p["angle"], p["kind"], p["obb"])
        if _try_reseat(p, cons):
            d_new = math.hypot(p["cx"] - P0[0], p["cy"] - P0[1])
            if d_new < d_old - 5.0:
                return True
            # 新位置不够近：回滚
            for k in range(len(placed_obb) - 1, -1, -1):
                if placed_obb[k] is p["obb"]:
                    placed_obb.pop(k)
                    break
            p["cx"], p["cy"], p["angle"], p["kind"], p["obb"] = snap
            placed_obb.append(snap[4])
        return False

    n_tight = 0
    for _tr in range(3):
        far_p = [p for p in placements
                 if math.hypot(p["cx"] - dot[id(p["model"])][0],
                               p["cy"] - dot[id(p["model"])][1]) > 60.0]
        if not far_p:
            break
        far_p.sort(key=lambda p: -math.hypot(
            p["cx"] - dot[id(p["model"])][0],
            p["cy"] - dot[id(p["model"])][1]))
        _prog = False
        for p in far_p:
            if _tighten(p):
                n_tight += 1
                _prog = True
        if not _prog:
            break

    # 重摆可能改变 kind 分布与到点距离——重算统计
    n_online = sum(1 for p in placements if p["kind"] == "online")
    n_offset = sum(1 for p in placements if p["kind"] == "offset")
    n_extend = sum(1 for p in placements if p["kind"] == "extend")
    n_sector = sum(1 for p in placements if p["kind"] == "sector")
    for p in placements:
        P1 = dot[id(p["model"])]
        dists.append((math.hypot(p["cx"] - P1[0], p["cy"] - P1[1]),
                      p["kind"], p["text"]))

    print(f"  Labels: {len(placements)} placed — riding on lines: {n_online} "
          f"(yield moves: {n_yield}), parallel offset: {n_offset}, "
          f"extend: {n_extend}, sector: {n_sector}, "
          f"min-collision fallback: {n_fallback}")
    print(f"  Label order repair (V15 componentwise monotonicity, dx>=0 AND dy>=0): "
          f"{n_mono_moved} re-seated + {n_reflow} window reflows, "
          f"{len(mono_unresolved)} pairs unresolved; "
          f"proximity tightening (V16-D): {n_tight} labels pulled closer")
    for _ub, _ua, _u2, _dx, _dy in mono_unresolved[:10]:
        print(f"    unresolved [{_ub}] {_ua!r} -> {_u2!r} "
              f"d=({_dx:+d},{_dy:+d})")

    # 诊断导出：真实放置结果（供 scripts/diag_v12_overlap.py 离线核查）
    try:
        with open(os.path.join(OUTPUT_DIR, "label_placements.json"), "w", encoding="utf-8") as fh:
            json.dump([{**{k: p[k] for k in ("text", "fs", "brand", "full_name",
                            "cx", "cy", "w", "h", "angle", "kind")},
                        "dot": [round(dot[id(p["model"])][0], 1),
                                round(dot[id(p["model"])][1], 1)],
                        "loc": list(loc.get(id(p["model"]), ()))}
                       for p in placements], fh, ensure_ascii=False, indent=1)
    except Exception:
        pass

    if dists:
        ds = sorted(d[0] for d in dists)
        print(f"  Label distance to own dot (px, dpi-100): median={ds[len(ds)//2]:.0f}, "
              f"p90={ds[int(len(ds)*0.9)]:.0f}, max={ds[-1]:.0f}")
        far = [d for d in dists if d[0] > 70]
        if far:
            print(f"  WARNING: {len(far)} labels farther than 70px from their dot:")
            for d0, kind, txt in sorted(far, reverse=True)[:12]:
                print(f"    {d0:6.0f}px  [{kind:<7}] {txt}")
    return placements


def _bisect_edge(A, B, t_cov, t_free, covered):
    """在 t_cov(被覆盖) 与 t_free(自由) 之间二分求边界（返回自由侧 t）。"""
    for _ in range(7):
        tm = (t_cov + t_free) / 2.0
        x = A[0] + (B[0] - A[0]) * tm
        y = A[1] + (B[1] - A[1]) * tm
        if covered(x, y):
            t_cov = tm
        else:
            t_free = tm
    return t_free


def _draw_pareto_lines(ax, placements, pareto, brand_frontiers):
    """画帕累托连线：文字下方不画线，仅在文字两侧绘制（要求二）。"""
    tr = ax.transData.transform
    inv = ax.transData.inverted()
    obbs = [_obb_specs(p["cx"], p["cy"], p["w"] + 1.5, p["h"] + 1.5, p["angle"])
            for p in placements]

    def covered(x, y):
        for o in obbs:
            dx, dy = x - o["cx"], y - o["cy"]
            if dx * dx + dy * dy > o["r2"]:
                continue
            if (abs(dx * o["ux"] + dy * o["uy"]) <= o["hw"]
                    and abs(dx * o["nx"] + dy * o["ny"]) <= o["hh"]):
                return True
        return False

    # V12-C：顶点按 (axis_x, 综合能力升序) 排序，等成本点自下而上连接
    _vkey = lambda m: (float(m["axis_x"]), float(m["composite_ability"]))
    polylines = []
    pf = sorted(pareto, key=_vkey)
    if len(pf) >= 2:
        polylines.append({
            "pts": [tr((float(m["axis_x"]), float(m["chart_y"]))) for m in pf],
            "color": OVERALL_LINE_COLOR, "lw": LW_OVERALL, "z": 3, "halo": False,
        })
    for brand in BRAND_LINE_CREATORS:
        fr = brand_frontiers.get(brand)
        if fr and len(fr) >= 2:
            fbs = sorted(fr, key=_vkey)
            color = fbs[0].get("creator_color") or "#888888"
            polylines.append({
                "pts": [tr((float(m["axis_x"]), float(m["chart_y"]))) for m in fbs],
                "color": color, "lw": LW_BRAND, "z": 4,
                "halo": _is_dark_color(color),
            })

    for pl in polylines:
        pts = pl["pts"]
        for k in range(len(pts) - 1):
            A, B = pts[k], pts[k + 1]
            L = math.hypot(B[0] - A[0], B[1] - A[1])
            if L < 0.5:
                continue
            ns = max(2, int(L / 1.6))
            dt = 1.0 / ns
            runs = []
            t_start = None
            for i in range(ns + 1):
                t = i * dt
                x = A[0] + (B[0] - A[0]) * t
                y = A[1] + (B[1] - A[1]) * t
                if covered(x, y):
                    if t_start is not None:
                        runs.append((t_start, t))
                        t_start = None
                else:
                    if t_start is None:
                        t_start = t
            if t_start is not None:
                runs.append((t_start, 1.0))
            for (t0, t1) in runs:
                if t0 > 0:
                    t0 = _bisect_edge(A, B, t0 - dt, t0, covered)
                if t1 < 1.0:
                    t1 = _bisect_edge(A, B, t1, t1 - dt, covered)
                x0, y0 = A[0] + (B[0] - A[0]) * t0, A[1] + (B[1] - A[1]) * t0
                x1, y1 = A[0] + (B[0] - A[0]) * t1, A[1] + (B[1] - A[1]) * t1
                if math.hypot(x1 - x0, y1 - y0) < 1.0:
                    continue
                p0 = inv.transform((x0, y0))
                p1 = inv.transform((x1, y1))
                line, = ax.plot([p0[0], p1[0]], [p0[1], p1[1]],
                                color=pl["color"], lw=pl["lw"], alpha=0.95,
                                zorder=pl["z"], linestyle="-", clip_on=False)
                if pl["halo"]:
                    line.set_path_effects(
                        [pe.withStroke(linewidth=pl["lw"] + 1.2, foreground="white")])


def _draw_markers(ax, plot_models, pareto, brand_frontiers):
    """圆点：暗色品牌元素加窄白边，其余用背景色描边分离连线。"""
    pareto_ids = {id(p) for p in pareto}
    brand_line_ids = {id(m) for fr in brand_frontiers.values() for m in fr}

    def xs(ms):
        return [float(m["axis_x"]) for m in ms]

    def ys(ms):
        return [float(m["chart_y"]) for m in ms]

    others = [m for m in plot_models
              if id(m) not in pareto_ids and id(m) not in brand_line_ids]
    if others:
        ax.scatter(xs(others), ys(others), c=CLOUD_COLOR, s=MS_CLOUD,
                   alpha=0.5, zorder=2, edgecolors="none", linewidths=0)
    other_global = [m for m in plot_models
                    if id(m) in pareto_ids and id(m) not in brand_line_ids]
    if other_global:
        ax.scatter(xs(other_global), ys(other_global), c=OVERALL_LINE_COLOR,
                   s=MS_OTHER_GLOBAL, alpha=0.95, zorder=5,
                   edgecolors=BG_COLOR, linewidths=0.8)
    for brand in BRAND_LINE_CREATORS:
        fr = brand_frontiers.get(brand)
        if not fr:
            continue
        color = fr[0].get("creator_color") or "#888888"
        edge = "white" if _is_dark_color(color) else BG_COLOR
        on = [m for m in fr if id(m) in pareto_ids]
        off = [m for m in fr if id(m) not in pareto_ids]
        if off:
            ax.scatter(xs(off), ys(off), c=color, s=MS_BRAND, alpha=0.9,
                       zorder=5, edgecolors=edge, linewidths=0.6)
        if on:
            ax.scatter(xs(on), ys(on), c=color, s=MS_BRAND_GLOBAL, alpha=1.0,
                       zorder=6, edgecolors=edge, linewidths=0.7)


def _draw_label_texts(ax, placements):
    """裸品牌色文字（无框、无背景），与连线平行；暗色加窄白描边。"""
    inv = ax.transData.inverted()
    for p in placements:
        cx, cy = inv.transform((p["cx"], p["cy"]))
        t = ax.text(cx, cy, p["text"], fontsize=p["fs"], fontweight="bold",
                    color=p["color"], ha="center", va="center",
                    rotation=p["angle"], rotation_mode="anchor",
                    zorder=7, clip_on=False)
        if p["halo"]:
            t.set_path_effects([pe.withStroke(linewidth=1.6, foreground="white")])



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

def _brand_cell(creator, logo):
    """Requirement 6: brand column = the AA page's own logo + creator name."""
    if logo:
        url = f"{LOGO_BASE_URL}{logo}"
        return f'<img src="{url}" width="18" alt="{creator}" /> {creator}'
    return creator or "--"


def save_results(models, pareto, brand_frontiers, metric_ranges, x_dist, mapping_meta):
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

    axis_meta = {k: v for k, v in mapping_meta.items() if k != "map_fn"}
    output = {
        "metadata": {
            "source": "https://artificialanalysis.ai/leaderboards/models",
            "model_status": "All (including deprecated models)",
            "methodology": (
                f"{len(METRIC_FIELDS)} evaluation metrics normalized [0,1], averaged → composite ability, "
                "then re-normalized linearly so best model = 1 and worst = 0; "
                "Pareto = non-dominated by per-request cost (cost 0/free models "
                "participate); "
                "chart Y-axis (V17): y = 0 at the FIRST (lowest) level of the "
                "overall Pareto frontier — models below it are excluded from "
                "the chart but kept in the table; chart_y = (ability-y0)/(1-y0); "
                "X-axis (V17): exact empirical-quantile (rank) mapping over the "
                "chart-visible models — piecewise-linear in log10(c), equal-cost "
                "ties averaged, endpoints pinned at (0,0) and (1,1), uniform "
                "density (x linear in rank: any equal-width segment holds the "
                "same number of models); 10^x magnitude indicators sit at "
                "x(10^x), so same-multiplier decade widths are proportional to "
                "the model count inside that decade; "
                "11 brands get their own thin Pareto lines (brand theme colors, "
                "drawn above the solid gray overall Pareto line; vertices "
                "ordered by (axis_x, ability) so equal-cost points connect "
                "bottom-up); dark brand elements carry a narrow white outline "
                "on the black canvas; "
                "labels ride ON the Pareto lines when the adjacent segment allows "
                "(parallel to the line, mid-axis coincident, line gapped under the "
                "text, bare brand-colored text), else take the nearest free spot; "
                "every label = model family (brand-shared leading block "
                "stripped at the longest valid cut: ending at a separator, "
                "or at a letter followed by a digit in every name) plus "
                "thinking level, '(non-reasoning)' shortened to '(non)'; "
                "2+ consecutive same-family vertices shorten to "
                "level-only labels after the run head (runs recomputed "
                "per brand; non-adjacent occurrences keep full labels)"
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
                    "used only for Pareto comparison and axis mapping."
                ),
            },
            "total_models": len(models),
            "pareto_count": len(pareto),
            "x_axis_mapping": axis_meta,
            "y_axis": mapping_meta.get("y_axis", {}),
            "x_axis_distribution": x_dist,
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
        "brand_frontiers": {
            brand: [_export_model(m, i + 1) for i, m in enumerate(fr)]
            for brand, fr in brand_frontiers.items()
        },
        "all_models": [
            {
                "model": m["model"],
                "full_name": m["full_name"],
                "creator": m["creator"],
                "creator_slug": m["creator_slug"],
                "creator_color": m["creator_color"],
                "creator_logo_url": (LOGO_BASE_URL + m["creator_logo"]) if m["creator_logo"] else None,
                "is_deprecated": m["is_deprecated"],
                "composite_ability": float(m["composite_ability"]),
                "per_request_cost": _frac_to_json(m.get("per_request_cost")),
                "x_axis_position": _frac_to_json(m.get("axis_x")),
                "in_chart": m.get("chart_y") is not None and m.get("axis_x") is not None,
                "chart_y": (float(m["chart_y"]) if m.get("chart_y") is not None else None),
                "is_pareto": id(m) in {id(p) for p in pareto},
                "brand_frontier_of": m.get("brand_frontier_of"),
            }
            for m in sorted(models, key=lambda x: (x["composite_ability"], x["model"]), reverse=True)
        ],
    }

    json_path = os.path.join(OUTPUT_DIR, "analysis_results.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"JSON saved to {json_path}")

    generate_readme(models, pareto, brand_frontiers, x_dist, mapping_meta)


def _export_model(m, rank):
    return {
        "rank": rank,
        "model": m["model"],
        "full_name": m["full_name"],
        "creator": m["creator"],
        "creator_color": m["creator_color"],
        "creator_logo_url": (LOGO_BASE_URL + m["creator_logo"]) if m["creator_logo"] else None,
        "is_reasoning": m["is_reasoning"],
        "is_pareto": True,
        "chart_label": m.get("chart_label"),
        "composite_ability": float(m["composite_ability"]),
        "per_request_cost": _frac_to_json(m.get("per_request_cost")),
        "x_axis_position": _frac_to_json(m.get("axis_x")),
        "in_chart": m.get("chart_y") is not None and m.get("axis_x") is not None,
        "chart_y": (float(m["chart_y"]) if m.get("chart_y") is not None else None),
        "input_price": _frac_to_json(m.get("input_price")),
        "output_price": _frac_to_json(m.get("output_price")),
        "cache_hit_price": _frac_to_json(m.get("cache_hit_price")),
        "cache_write_price": _frac_to_json(m.get("cache_write_price")),
        "speed": _frac_to_json(m["speed"]),
        "ttft": _frac_to_json(m["ttft"]),
        "total_response": _frac_to_json(m["total_response"]),
        "reasoning_time": _frac_to_json(m["reasoning_time"]),
        "cost_breakdown": m.get("cost_breakdown"),
        "valid_metrics": m["valid_metrics"],
    }


def generate_readme(models, pareto, brand_frontiers, x_dist, mapping_meta):
    chr_value, chr_count = None, None
    if os.path.exists(CACHE_HIT_RATE_FILE):
        with open(CACHE_HIT_RATE_FILE, encoding="utf-8") as f:
            chr_data = json.load(f)
        chr_value = chr_data.get("cache_hit_rate")
        chr_count = chr_data.get("valid_count")

    ya = mapping_meta.get("y_axis", {})
    y0 = ya.get("baseline")
    y0s = f"{y0:.4f}" if y0 is not None else "?"
    y0m = ya.get("baseline_model", "?")
    n_vis = mapping_meta.get("plotted_models", 0)
    n_total = len(models)

    lines = []
    lines.append("# LLM Leaderboard Pareto Analysis\n")
    lines.append("![Pareto Analysis](output/pareto_analysis.png)\n")


    # ── 全部模型表格（要求一/三/六/八）──────────────────────────────────
    lines.append("## 全部模型（综合能力从高到低，最优 = 1，最差 = 0）\n")
    lines.append("共收录 **Status: All**（含已弃用）的全部模型；按重新归一化后的综合能力排序。"
                 "「帕累托」列：✅ = 总体帕累托前沿模型，❌ = 被支配，— = 无成本数据无法判定。"
                 f"图表纵轴以总体帕累托前沿第一级（y0 = {y0s}，即前沿左端点 {y0m}）为 0："
                 f"综合能力 ≥ 该级且有成本数据的 {n_vis} 个模型入图，{ya.get('below_baseline', 0)} 个"
                 f"能力低于第一级、{ya.get('no_cost_visible', 0)} 个缺少成本数据的模型不出现在图中"
                 "（本表不受影响，仍完整列出全部模型）。\n")
    lines.append("| # | 品牌 | 模型 | 综合能力 | 单请求成本 | 横轴位置 | 帕累托 |")
    lines.append("|---|------|------|---------|-----------|-----------|------|")

    pareto_ids = {id(p) for p in pareto}
    ranked = sorted(models, key=lambda x: (x["composite_ability"], x["model"]), reverse=True)
    for i, m in enumerate(ranked):
        ab = f"{float(m['composite_ability']):.4f}"
        cost = m.get("per_request_cost")
        cost_str = f"{float(cost):,.2f}" if cost is not None else "—"
        lx = m.get("axis_x")
        lx_str = f"{float(lx):.4f}" if lx is not None else "—"
        if m.get("brand_frontier_of"):
            mark = "✅" if id(m) in pareto_ids else "❌"
        elif cost is not None:
            mark = "✅" if id(m) in pareto_ids else "❌"
        else:
            mark = "—"
        lines.append(
            f"| {i+1} | {_brand_cell(m['creator'], m['creator_logo'])} | {m['model']} "
            f"| {ab} | {cost_str} | {lx_str} | {mark} |"
        )

    # ── 品牌前沿说明（图例表）────────────────────────────────────────────
    lines.append("\n## 品牌帕累托前沿连线（仅体现在图中）\n")
    lines.append("以下十一个品牌在图中拥有单独的帕累托连线（较窄宽度，品牌主题色，图层高于总体灰色连线）。"
                 "表中数量为**入图顶点数**——品牌前沿上低于总体前沿第一级的顶点同样不入图（本表与图例一致）：\n")
    lines.append("| 品牌 | 主题色 | 品牌前沿模型数（入图） |")
    lines.append("|------|--------|--------------|")
    for brand in BRAND_LINE_CREATORS:
        fr = brand_frontiers.get(brand)
        if not fr:
            continue
        logo = fr[0].get("creator_logo")
        lines.append(f"| {_brand_cell(brand, logo)} | `{fr[0].get('creator_color') or '#888888'}` | {len(fr)} |")

    # ── 评分方法 ─────────────────────────────────────────────────────────
    lines.append("\n## 评分方法\n")
    lines.append(f"1. **{len(METRIC_FIELDS)}项评估指标**各自线性归一化到 [0,1]")
    metric_list = "、".join(METRIC_LABELS[k] for k in METRIC_FIELDS)
    lines.append(f"   （{metric_list}）")
    lines.append("   > V18（2026-09-12）：AA 更新了基准列——新增 AA Analyst Agent、τ³-Bench Banking、"
                 "Terminal-Bench 2.1 / 4.0 四项；AA Agentic Index 与 AA Coding Index 已从 AA 的数据源中移除，"
                 "相应剔除。指标数由 18 → 20。")
    lines.append("2. **综合能力值** = 所有有效归一化分数的算术平均")
    lines.append("3. **综合能力再归一化**：线性映射到 [0,1]，性能最好的模型 = 1，最差的模型 = 0")
    lines.append("4. **Pareto前沿** = 不被任何其他模型支配的模型（综合能力 ≥ 且成本 ≤，且至少一项严格更优；"
                 "成本为 0 的免费模型同样参与——横轴左端恒为 0，免费模型是合法前沿候选）")
    lines.append("5. **模型范围** = Status: All（含已弃用模型；缺少足够评估数据者不参与排名）")
    lines.append(f"6. **图表纵轴基线（V17）**：图表的 y = 0 取总体帕累托前沿的第一级（最低能力；本例 "
                 f"y0 = {y0s}，即前沿左端点 {y0m}）；综合能力低于该级的模型不出现在图表中（表格不受影响）。"
                 "图中纵坐标 chart_y = (能力 - y0)/(1 - y0)，因此前沿左端点恰好落在 (0, 0)、"
                 "最优模型恰好为 y = 1。该过滤在横轴映射构建之前完成")
    lines.append("")

    # ── 横轴映射与分布分析 ────────────────────────────────────────────────
    lines.append("\n## 横轴映射（分位数等密度映射，V17）与分布分析\n")
    if x_dist.get("plotted_models"):
        n_knots = mapping_meta.get("knots", 0)
        fit = mapping_meta.get("fit", {})
        dec_ticks = mapping_meta.get("decade_ticks", [])
        lines.append(f"横轴（单请求成本）按**经验分位数（rank）映射**——以 {fit.get('fitted_models', 0)} 个"
                     "入图正成本模型（综合能力 ≥ 前沿第一级）的成本分布为基准：\n")
        lines.append("```")
        lines.append("x = 0                            当 c ≤ 0（免费模型，钉在最左缘）")
        lines.append("x = interp(log10(c); knots)      当 c > 0")
        lines.append("```\n")
        lines.append(f"其中 knots = (log10(c_i), 名次_i/(n-1)) 为入图正成本模型按成本排序后的 {n_knots} 个"
                     "锚点（相同 log10(c) 的并列组取平均名次，保证 x 是 z = log10(c) 的单值函数；"
                     "n-1 归一化使最大成本恰为 x = 1）。"
                     "该映射在 **y 基线过滤之后**构建（V17：先以帕累托前沿第一级为 y = 0、剔除低性能模型，"
                     "再对入图模型建映射）。（V18 修正：并列判定改用相同的 log10(c)，"
                     "消除浮点上相差 ~1e-12 的成本经 log10 后折合到同一 z 造成的同 z 双锚点、"
                     "个别模型 x 偏离名次的问题；修正后 x 对每个入图模型严格线性于名次。）\n")
        lines.append("**该映射保证：**\n")
        lines.append("- **函数端点严格钉死**：c = 0 → x = 0；最大成本 → x = 1——函数经过 (0,0) 与 (1,1)；")
        lines.append(f"- **严格均匀密度**：x 是模型名次的线性函数（相同 log10(c) 并列组取平均名次），"
                     f"因此**任意等宽区段的模型数恒定**（每 0.1 宽度约 {fit.get('fitted_models', 0) / 10:.0f} 个模型）"
                     "——无论截取哪一段，"
                     "模型数 ÷ 宽度都等于全图的模型总数 ÷ 总宽度。V12 的单一 logistic 函数在过滤后的分布上"
                     "做不到（十分位在 8~24 间摆动），故替换为精确分位数映射；")
        vis_costs = [float(m["per_request_cost"]) for m in models
                     if m.get("chart_y") is not None
                     and m.get("per_request_cost") is not None
                     and float(m["per_request_cost"]) > 0]
        pairs = [(a["price"], b["price"]) for a, b in zip(dec_ticks, dec_ticks[1:])]
        if pairs:
            seg = "，".join(f"{_fmt_cost_tick(lo)}–{_fmt_cost_tick(hi)}: "
                            f"{sum(1 for c in vis_costs if lo < c <= hi)}"
                            for lo, hi in pairs)
            lines.append(f"- 各数量级区间的入图模型数：{seg}")
        n_1 = sum(1 for c in vis_costs if 1e3 < c <= 1e4)
        n_2 = sum(1 for c in vis_costs if 1e5 < c <= 1e6)
        if n_1 and n_2:
            lines.append(f"- **同一倍率区间的宽度 ∝ 该区间模型数**——均匀密度的必然结果：1k→10k 与 "
                         f"100k→1M 同为 10 倍率，但前者 {n_1} 个模型、后者 {n_2} 个，前者宽度约为后者的 "
                         f"{n_1 / n_2:.1f} 倍。若改用「等倍率等距」（纯对数轴），两段的模型密度将相差 "
                         f"{n_1 / n_2:.1f} 倍，与均匀密度目标冲突——两者数学上不可兼得，本图以均匀密度"
                         "（最高优先级）为准；")
        lines.append(f"- **左端恒为 0**（c = 0；{mapping_meta.get('free_models', 0)} 个免费模型位于最左缘）")
        lines.append(f"- 最低正成本 {mapping_meta.get('min_positive_cost', 0):,.2f} → x = "
                     f"{mapping_meta.get('x_at_min_positive_cost', 0):.4f}；"
                     f"最高成本 {mapping_meta.get('max_cost', 0):,.0f} → x = "
                     f"{mapping_meta.get('x_at_max_cost', 0):.4f}（严格 = 1）")
        lines.append(f"- 中位数位置 {x_dist.get('median', 0):.3f}（≈ 0.5 居中）；左右两半模型数："
                     f"左 {x_dist.get('left_half_models', 0)} / 右 {x_dist.get('right_half_models', 0)}")
        dec = x_dist.get("decile_counts", [])
        if dec:
            lines.append("- 横轴十分位模型数：" + "，".join(str(c) for c in dec)
                         + "（x 为名次的线性函数；n/10 非整数时各十分位在 ±1 内取整，"
                         "相同 log10(c) 并列组共享同一 x、落在边界的哪一侧可再移动 ±1）")
        if dec_ticks:
            lines.append("- **10^x 数量级指示**（位置 = x(10^x)）："
                         + "，".join(f"10^{int(round(math.log10(d['price'])))} → {d['x']:.3f}"
                                     for d in dec_ticks))
        lines.append("")

    # ── 标注规则 ─────────────────────────────────────────────────────────
    lines.append("## 图中标注规则\n")
    lines.append("品牌帕累托前沿模型全部标注。V13/V15/V16 规则：\n")
    lines.append("1. **品牌公共前缀剔除（最长有效切点）**：品牌全部前沿模型共享的前导块被剔除 —— 切点须止于"
                 "分界符（空格/连字符/下划线，如 \'Claude \'、\'GPT-\'、\'GLM-\'、\'Grok \'、\'DeepSeek V4 \'），"
                 "或止于字母且每个名称在切点后紧跟数字（品牌/系列字母 + 版本号，如 \'Kimi K|2.6\'、\'Qwen|3.8\'、"
                 "\'MiMo-V|2.5\'、\'MiniMax-M|2.1\'）—— 实例：Claude Opus 5 (high) → Opus 5 (high)、"
                 "GPT-5.6 Sol → 5.6 Sol、Kimi K2.6 → 2.6、Qwen3.8 Max → 3.8 Max、MiMo-V2.5-Pro → 2.5-Pro；"
                 "剔除后任一名称为空或产生重复标签则该切点作废，顺次尝试更短切点；")
    lines.append("2. **(non-reasoning) → (non)**：思考程度中的 Non-reasoning 简写为 non"
                 "（含组合式：Non-reasoning, high → non, high）；")
    lines.append("3. **相邻同名 run 短标签（每次重新计算）**：品牌连线上连续 2 个以上顶点属于同一模型时，"
                 "仅性能最低者（run 首位）保留全名，其后相邻的较高者只标思考程度（如 Opus 5 的 "
                 "(low) (medium) (high) (xhigh) 序列仅首项带族名）；同名模型不相邻的重复出现不合并、"
                 "保留全名 —— A-B(high)-B(xhigh)-C-B(max) 标注为 A-B(high)-(xhigh)-C-B(max)，"
                 "因此交错家族（Gemini 3.7 / 3.8 Flash、Claude Fable 5.1 / Opus 5）始终可分辨。\n")
    lines.append("4. **标签位置与序列同向（V15）**：品牌前沿上越靠右上的模型，其标签重心必须同时更靠右且更靠上 —— "
                 "对前沿相邻对 A→B（B 更靠右上），标签位移的两个分量须同时 >= 0（至少是 (0,0)），"
                 "既不得更左、也不得更低（只要有一个分量非负不算合格；V14 的投影规则会放过「更右但更低」，V15 起视为违反；"
                 "等成本堆叠即：上方模型的标签既在上方、也不更左）；初始放置违反时就近重摆"
                 "（不产生新的重叠、不破坏与前后邻居的同向关系，最多 6 轮；单标签重摆无解——标签被前后邻居夹死、局部约束盒为空——时，自动升级为以违规对为中心逐级扩大的窗口级联重排，整段相邻标签作为一个阶梯整体重排，修不好的配对在日志中报告）。\n")
    lines.append("5. **标签摆放四级优先（V16）**：① 尽量多的标签骑在连线段上——点的右侧（去路段）"
                 "或左侧（来路段）皆可，同一条线段允许容纳两个标签（各贴各的点）；目标骑线位仅被其他"
                 "标签占据时触发「让位」——占用者挪到自己的另一个骑线位，双方都保持骑线。"
                 "② 骑不上线的标签在「假设线能放下该标签」的离点最近位置的上方或下方、与线平行摆放"
                 "（右/左侧 × 上/下方四组合；互相掣肘的标签自然错开成对角组合）。③ 仍放不下时放在点的"
                 "两条连线延长线上的最近点。④ 最后在两条连线夹角形成的扇区（连线前上方空白区）内就近"
                 "放置，文字保持与邻近连线平行。\n")
    lines.append("标注文字与连线平行且中轴线重合；文字下方不绘制连线，仅在文字两侧绘制（若两侧仍有"
                 "区域）；文字使用品牌颜色，无边框、无背景。\n")

    # ── 成本计算公式 ─────────────────────────────────────────────────────
    lines.append("## 成本计算公式\n")
    lines.append("**X轴成本 = 单请求估算成本（公式）**\n")
    lines.append("```")
    lines.append("cost = (CacheHitRate × CacheHitPrice × InputTokens)")
    lines.append("     + ((1 − CacheHitRate) × CacheWritePrice × InputTokens)")
    lines.append("     + (SpeedMedian × RealTime × OutputPrice)")
    lines.append("```\n")
    lines.append("**参数来源与处理逻辑：**\n")
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
    lines.append("**RealTime 计算逻辑：**\n")
    lines.append("- 如果存在 Reasoning Time（推理模型）：")
    lines.append("  `RealTime = End-to-End Response Time Total − Latency First Chunk`")
    lines.append("  = `medianEndToEndResponseTimeSeconds − medianTimeToFirstTokenSeconds`")
    lines.append("- 如果 Reasoning Time 为 `--`（非推理模型）：")
    lines.append("  `RealTime = End-to-End Response Time Total`")
    lines.append("  = `medianEndToEndResponseTimeSeconds`")
    lines.append("")
    lines.append("**单位说明：** AA 价格以 USD / 1M tokens 为单位，InputTokens 为原始计数（10000），Speed 为 tokens/sec，RealTime 为秒。公式按原样计算，不做单位换算。最终成本是一个相对得分（用于 Pareto 比较和对数映射），不是真实的美元金额。")
    lines.append("")

    # ── 数据来源 ─────────────────────────────────────────────────────────
    lines.append("### 数据来源\n")
    lines.append(f"**主数据源**: [Artificial Analysis Leaderboard](https://artificialanalysis.ai/leaderboards/models)（Status: All）  ")
    lines.append(f"**Cache Hit Rate 数据源**: [AA Coding Agents](https://artificialanalysis.ai/agents/coding-agents)  ")
    lines.append(f"**性能方法论**: [AA Performance Benchmarking](https://artificialanalysis.ai/methodology/performance-benchmarking)  ")
    lines.append(f"**模型总数（Status: All）**: {len(ranked)} 个参与排名（另有模型因评估数据不足未列入；"
                 f"总体帕累托前沿 {len(pareto)} 个；图表入图 {n_vis} 个——综合能力 ≥ 前沿第一级）  ")

    # ── 图表说明（V17-A：原先位于表格之前，现移至文末）──────────────────
    lines.append("\n## 图表说明（黑底）\n")
    lines.append("（V17 起本说明置于文末，图表之后直接跟随模型表格。）\n")
    lines.append("图表说明：**灰色实线** = 总体帕累托前沿；**彩色细线** = 十一个品牌的单独帕累托前沿"
                 "（品牌主题色，图层高于总体连线；暗色品牌元素带窄白边；顶点按（横轴位置、能力升序）"
                 "连接，等成本点自下而上）；品牌前沿模型圆点同样使用品牌颜色。"
                 "模型名称/思考程度标注优先骑在连线之上（点的左/右两侧皆可，同一条线段可容纳两个标签——各贴各的点；文字与连线平行、中轴线重合，连线仅在文字两侧绘制）；"
                 "骑线位被其他标签占据时自动「让位」——占用者挪到自己的另一个骑线位，双方都保持骑线；"
                 "实在骑不上线时按四级优先依次退让（V16）：离点最近位置的上方/下方平行偏移 → 点的两条连线延长线上就近 → 两连线夹角扇区内就近。"
                 "标签规则（V13/V15）：品牌前沿模型共享的前导块按「最长有效切点」剔除 —— "
                 "切点止于分界符，或止于字母且其后紧跟数字（如 Claude Opus 5 → Opus 5、GPT-5.6 Sol → 5.6 Sol、"
                 "Kimi K2.6 → 2.6、Qwen3.8 Max → 3.8 Max、MiMo-V2.5 → 2.5、MiniMax-M2.1 → 2.1）；"
                 "(non-reasoning) 简写为 (non)；同一模型在品牌连线上相邻出现 2 次以上时仅性能最低者保留全名、"
                 "相邻较高者只标思考程度，不相邻的重复出现保留全名（每次重新计算）；标签位置与序列同向（V15）——品牌前沿上越靠右上的模型，其标签重心必须同时更靠右且更靠上（两分量都 >= 0，至少是 (0,0)，仅其一非负不算合格；初始放置违反时自动就近重摆，单标签无解（被前后邻居夹死）时按窗口级联重排整体挪动，均不产生新的重叠）。"
                 f"纵轴 y = 0 = 总体帕累托前沿第一级（y0 = {y0s}，前沿左端点 {y0m} 恰为 (0,0)），"
                 f"能力低于该级的 {ya.get('below_baseline', 0)} 个模型与缺少成本数据的 "
                 f"{ya.get('no_cost_visible', 0)} 个模型不出现在图中；"
                 "横轴为分位数等密度映射（见上文「横轴映射」节），10^x 数量级指示位于 x(10^x)，"
                 "同一倍率区间的宽度与该区间内模型数成正比。\n")

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

    print("=" * 60)
    print("Generic LLM Leaderboard Pareto Analysis — Version 18")
    print(f"  {len(METRIC_FIELDS)} benchmark metrics "
          f"(V18: +analystAgent +tauBanking +terminalbenchV21/V40, "
          f"-agenticIndex -codingIndex)")
    print("=" * 60)

    print("Loading data...")
    data = load_data()
    print(f"  {len(data)} models loaded")

    print("\nComputing scores & costs (Status: All)...")
    models, metric_ranges = compute_scores(data)

    with_cost = [m for m in models if m.get("per_request_cost") is not None and m["per_request_cost"] >= 0]
    if with_cost:
        costs = [m["per_request_cost"] for m in with_cost]
        print(f"  Models with cost data: {len(with_cost)}/{len(models)}")
        print(f"  Cost range: {float(min(costs)):.4f} – {float(max(costs)):.4f}")

    print("\nComputing Pareto frontier (overall, incl. free models)...")
    pareto = compute_pareto(models)
    print(f"  Pareto frontier: {len(pareto)} models")

    print("\nComputing brand Pareto frontiers (11 brands)...")
    brand_frontiers = compute_brand_frontiers(models)

    print("\nApplying chart Y baseline (V17: y = 0 at the first overall-Pareto level)...")
    yb = apply_chart_baseline(models, pareto)
    # V17-C: models below the first Pareto level do not appear in the chart —
    # brand frontiers keep only their chart-visible vertices (table unaffected)
    brand_frontiers = {b: [m for m in fr if m.get("chart_y") is not None]
                       for b, fr in brand_frontiers.items()}
    brand_frontiers = {b: fr for b, fr in brand_frontiers.items() if fr}

    print("\nBuilding X-axis mapping (V17: quantile mapping fitted AFTER the filter)...")
    mapping_meta = build_axis_mapping(models, brand_frontiers)
    mapping_meta["y_axis"] = yb

    print("\nBuilding chart labels (V16: four-tier on-line-first placement"
          " with yield + V13/V15 text & monotonicity rules)...")
    build_label_specs(models, pareto, brand_frontiers)

    print("\nAnalyzing X-axis distribution...")
    x_dist = analyze_x_distribution(models, mapping_meta)

    print("\nGenerating visualization...")
    plot_analysis(models, pareto, brand_frontiers, x_dist, mapping_meta)

    print("\nSaving results...")
    save_results(models, pareto, brand_frontiers, metric_ranges, x_dist, mapping_meta)

    # Console summary of the overall frontier
    print(f"\n{'='*120}")
    print(f"PARETO FRONTIER ({len(pareto)} models) — ranked by composite ability")
    print(f"{'='*120}")
    print(f"{'#':<3} {'Model':<38} {'Ability':>8} {'Cost':>14} {'X':>6} {'Creator':<14}")
    print(f"{'-'*3} {'-'*38} {'-'*8} {'-'*14} {'-'*6} {'-'*14}")
    for i, m in enumerate(pareto):
        cost = f"{float(m['per_request_cost']):,.2f}" if m.get("per_request_cost") is not None else "--"
        lx = f"{float(m['axis_x']):.3f}" if m.get("axis_x") is not None else "--"
        print(f"{i+1:<3} {m['model']:<38} {float(m['composite_ability']):>8.4f} "
              f"{cost:>14} {lx:>6} {m.get('creator', ''):<14}")

    print("\nDone!")


if __name__ == "__main__":
    main()
