#!/usr/bin/env python3
"""
Scoring system, per-request cost calculation, and Pareto analysis
for Artificial Analysis LLM Leaderboard.

**Modified version (v5)**: Three-stage computation pipeline:

  Stage 1 — Exact Fraction arithmetic
    All intermediate calculations use `fractions.Fraction` for exact rational
    arithmetic. No floating-point rounding at any step.

  Stage 2 — Power-law exponential mapping (f(x) = x^p)
    A continuous mathematical function, NOT a rank reassignment.
    The power parameter p is determined ONLY from the Pareto frontier
    models' data distribution (specifically, their median value), so that
    after mapping, values are centered around 0.5.

    f(x) = x^p where p = log(0.5) / log(median_pareto)
    - f(0) = 0, f(1) = 1 (endpoints preserved)
    - f(median) = 0.5 (median maps to center)
    - The mapping is a smooth monotonic function from [0,1] to [0,1]
    - No forced uniform distribution, just a mathematical transformation

    X-axis: normalized_cost → x^p_x (p_x from Pareto cost median)
    Y-axis: ability_rescaled → y^p_y (p_y from Pareto ability median)

  Stage 3 — Float conversion ONLY at matplotlib chart coordinates

Visualization:
    - Black background, 黑体 (Heiti) white font
    - 1:1 square aspect ratio
    - Boundary frame: axes at x=0 & y=0, boundary lines at x=1 & y=1
    - Only 0 and 1 on tick marks
    - Dashed lines from each Pareto model to both axes with pre-mapping values
"""

import json
import math
import os
import sys
from collections import Counter
from fractions import Fraction

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# ══════════════════════════════════════════════════════════════════════
# Font setup — 黑体风格, 白色字体 on 黑色背景
# ══════════════════════════════════════════════════════════════════════
_HEITI_FONTS = [
    "/usr/share/fonts/truetype/chinese/SarasaMonoSC-Bold.ttf",
    "/usr/share/fonts/truetype/chinese/SarasaMonoSC-SemiBold.ttf",
    "/usr/share/fonts/truetype/chinese/SarasaMonoSC-Regular.ttf",
]
_LATIN = ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]
for fp in _HEITI_FONTS:
    if os.path.exists(fp):
        fm.fontManager.addfont(fp)
        break
for fp in _LATIN:
    if os.path.exists(fp):
        fm.fontManager.addfont(fp)
        break
plt.rcParams["font.sans-serif"] = ["Sarasa Mono SC", "Noto Serif SC", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

# ── Paths ──
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
RAW_DATA_FILE = os.path.join(OUTPUT_DIR, "raw_data.json")

# ── Metrics ──
METRICS = [
    "AA_Intelligence_Index", "AA_Omniscience_Index", "GDPval_AA",
    "Terminal_Bench_Hard", "Tau2_Bench", "AA_LCR",
    "AA_Omniscience_Accuracy", "AA_Omniscience_Non_Hallucination",
    "HLE", "GPQA_Diamond", "SciCode", "IFBench", "CritPt",
    "APEX_Agents_AA", "MMMU_Pro",
]
METRIC_LABELS = {
    "AA_Intelligence_Index": "AA Intelligence Index",
    "AA_Omniscience_Index": "AA Omniscience Index",
    "GDPval_AA": "GDPval-AA Agentic Work",
    "Terminal_Bench_Hard": "Terminal-Bench Hard",
    "Tau2_Bench": "τ²-Bench Telecom",
    "AA_LCR": "AA-LCR Long Context",
    "AA_Omniscience_Accuracy": "AA-Omniscience Accuracy",
    "AA_Omniscience_Non_Hallucination": "AA-Omniscience Non-Hallucination",
    "HLE": "Humanity's Last Exam",
    "GPQA_Diamond": "GPQA Diamond",
    "SciCode": "SciCode Coding",
    "IFBench": "IFBench Instruction Following",
    "CritPt": "CritPt Physics",
    "APEX_Agents_AA": "APEX-Agents-AA Office",
    "MMMU_Pro": "MMMU Pro Visual",
}
MIN_VALID_METRICS = 5
MIN_INPUT_OUTPUT_RATIO = Fraction(1, 100)      # 0.01
MAX_INPUT_OUTPUT_RATIO = Fraction(99, 100)     # 0.99


# ══════════════════════════════════════════════════════════════════════
# Stage 1: Parsing & Exact Fraction Computation
# ══════════════════════════════════════════════════════════════════════

def parse_val(s):
    if s in ("--", ""):
        return None
    s = s.replace("%", "").replace("$", "").replace(",", "").strip()
    try:
        return Fraction(s)
    except (ValueError, ZeroDivisionError):
        return None


def parse_price(s):
    if s in ("--", ""):
        return None
    s = s.replace("$", "").replace(",", "").strip()
    try:
        return Fraction(s)
    except (ValueError, ZeroDivisionError):
        return None


def load_data():
    with open(RAW_DATA_FILE, encoding="utf-8") as f:
        return json.load(f)


def compute_scores(data):
    """Stage 1: All computation in exact Fraction arithmetic."""
    models = []
    for d in data:
        blended = parse_price(d.get("Blended_Price", "--"))
        if blended is None or blended <= 0:
            continue

        m = {
            "model": d["Model"],
            "is_reasoning": bool(d.get("Is_Reasoning", False)),
            "blended_price": blended,
            "input_price": parse_price(d.get("Input_Price", "--")),
            "output_price": parse_price(d.get("Output_Price", "--")),
            "speed": parse_val(d.get("Speed_TokensPerSec", "--")),
            "ttft": parse_val(d.get("Latency_First_Chunk_s", "--")),
            "total_response": parse_val(d.get("Total_Response_s", "--")),
            "reasoning_time": parse_val(d.get("Reasoning_Time_s", "--")),
            "_parsed": {},
        }
        for metric in METRICS:
            m["_parsed"][metric] = parse_val(d.get(metric, "--"))
        models.append(m)

    print(f"Models with valid blended price: {len(models)}")
    print(f"  Reasoning models: {sum(1 for m in models if m['is_reasoning'])}")
    print(f"  Non-reasoning models: {sum(1 for m in models if not m['is_reasoning'])}")

    # ── Metric ranges (Fraction) ──
    metric_ranges = {}
    for metric in METRICS:
        vals = [m["_parsed"][metric] for m in models if m["_parsed"][metric] is not None]
        if len(vals) >= 2:
            metric_ranges[metric] = {"min": min(vals), "max": max(vals), "count": len(vals)}
        else:
            metric_ranges[metric] = None

    # ── Normalize metrics ──
    for m in models:
        m["_norm"] = {}
        for metric in METRICS:
            val = m["_parsed"][metric]
            rng = metric_ranges.get(metric)
            if val is None or rng is None:
                m["_norm"][metric] = None
            elif rng["max"] == rng["min"]:
                m["_norm"][metric] = Fraction(1, 2)
            else:
                m["_norm"][metric] = (val - rng["min"]) / (rng["max"] - rng["min"])

    # ── Composite ability = exact Fraction mean ──
    for m in models:
        nv = [v for v in m["_norm"].values() if v is not None]
        m["composite_ability"] = sum(nv) / len(nv) if nv else None
        m["valid_metrics"] = len(nv)

    # Quality filter
    valid = [m for m in models
             if m["composite_ability"] is not None and m["valid_metrics"] >= MIN_VALID_METRICS]
    print(f"Models with ≥{MIN_VALID_METRICS} metrics: {len(valid)}")

    # ── Per-request cost (exact Fraction) ──
    for m in valid:
        m["input_output_ratio"] = None
        m["total_output_tokens"] = None
        m["input_tokens"] = None
        m["per_request_cost"] = None
        m["cost_method"] = None

        if (m["input_price"] is not None and m["output_price"] is not None
                and m["input_price"] != m["output_price"]
                and m["input_price"] > 0 and m["output_price"] > 0):
            r = (m["blended_price"] - m["output_price"]) / (m["input_price"] - m["output_price"])
            r = max(MIN_INPUT_OUTPUT_RATIO, min(MAX_INPUT_OUTPUT_RATIO, r))
            m["input_output_ratio"] = r

        has_speed = m["speed"] is not None and m["speed"] > 0
        has_total = m["total_response"] is not None and m["total_response"] > 0
        has_ttft = m["ttft"] is not None and m["ttft"] > 0
        has_rtime = m["reasoning_time"] is not None and m["reasoning_time"] > 0

        if not (has_speed and has_total):
            continue

        if not m["is_reasoning"]:
            if has_ttft:
                output_time = m["total_response"] - m["ttft"]
                if output_time <= 0:
                    output_time = m["total_response"]
                m["total_output_tokens"] = output_time * m["speed"]
                m["cost_method"] = "non-reasoning"
            else:
                m["total_output_tokens"] = m["total_response"] * m["speed"]
                m["cost_method"] = "non-reasoning-no-ttft"
        elif has_rtime:
            if has_ttft:
                output_time = m["total_response"] - m["ttft"]
                if output_time <= 0:
                    output_time = m["total_response"]
                m["total_output_tokens"] = output_time * m["speed"]
            else:
                m["total_output_tokens"] = m["total_response"] * m["speed"]
            m["cost_method"] = "reasoning-with-time"
        else:
            m["total_output_tokens"] = m["total_response"] * m["speed"]
            m["cost_method"] = "reasoning-no-time"

        if m["input_output_ratio"] is not None and m["input_output_ratio"] < 1:
            if m["total_output_tokens"] is not None and m["total_output_tokens"] > 0:
                m["input_tokens"] = (
                    m["total_output_tokens"]
                    * m["input_output_ratio"]
                    / (1 - m["input_output_ratio"])
                )

        if (m["input_tokens"] is not None and m["total_output_tokens"] is not None
                and m["input_price"] is not None and m["output_price"] is not None):
            cost = (
                m["input_tokens"] * m["input_price"]
                + m["total_output_tokens"] * m["output_price"]
            ) / 1_000_000
            m["per_request_cost"] = cost

    # ── Normalize per-request cost (Fraction min-max) ──
    priced = [m for m in valid if m.get("per_request_cost") is not None]
    if priced:
        costs = [m["per_request_cost"] for m in priced]
        min_c, max_c = min(costs), max(costs)
        print(f"Per-request cost range: ${float(min_c):.4f} – ${float(max_c):.4f}")
        for m in priced:
            if max_c == min_c:
                m["normalized_cost"] = Fraction(1, 2)
            else:
                m["normalized_cost"] = (m["per_request_cost"] - min_c) / (max_c - min_c)
    for m in valid:
        if "normalized_cost" not in m:
            m["normalized_cost"] = None

    return valid, metric_ranges


# ══════════════════════════════════════════════════════════════════════
# Stage 2: Power-law Exponential Mapping (f(x) = x^p)
# ══════════════════════════════════════════════════════════════════════

def _compute_power_param(pareto_models, value_key):
    """Compute the power parameter p for the mapping f(x) = x^p,
    determined ONLY from the Pareto frontier models' data distribution.

    The parameter is chosen so that the median of the Pareto models'
    values maps to 0.5:
        median_pareto^p = 0.5
        p = log(0.5) / log(median_pareto)

    This ensures that after mapping, the Pareto models' values are
    centered around 0.5 — no forced uniform distribution, just a
    smooth mathematical function that re-centers the data.

    Returns p (float), or 1.0 if the median is degenerate.
    """
    vals = [m.get(value_key) for m in pareto_models if m.get(value_key) is not None]
    if len(vals) < 2:
        return 1.0  # identity mapping if insufficient data
    # Compute median using exact Fraction comparison
    sorted_vals = sorted(vals)
    n = len(sorted_vals)
    if n % 2 == 1:
        median_frac = sorted_vals[n // 2]
    else:
        median_frac = (sorted_vals[n // 2 - 1] + sorted_vals[n // 2]) / 2
    median_f = float(median_frac)
    # Edge cases
    if median_f <= 0.0 or median_f >= 1.0:
        return 1.0  # identity mapping
    # p = log(0.5) / log(median)
    p = math.log(0.5) / math.log(median_f)
    # Clamp to reasonable range to avoid extreme distortion
    p = max(0.05, min(20.0, p))
    return p


def apply_index_mapping(models, pareto):
    """Apply power-law exponential mapping to both axes.

    The mapping function f(x) = x^p is a smooth continuous function
    from [0,1] to [0,1] with f(0)=0, f(1)=1.
    The power parameter p is determined ONLY from the Pareto frontier
    models' median, so that f(median) = 0.5.

    This is NOT a rank reassignment — it is a mathematical function
    transformation that makes the distribution more centered.

    X-axis: normalized_cost → (normalized_cost)^p_x
    Y-axis: ability_rescaled → (ability_rescaled)^p_y
    """
    plot_models = [m for m in models if m.get("normalized_cost") is not None]

    # ── Y-axis Step 1: Re-normalize composite_ability → ability_rescaled ──
    abilities = [m["composite_ability"] for m in plot_models if m["composite_ability"] is not None]
    if abilities:
        min_a, max_a = min(abilities), max(abilities)
        for m in plot_models:
            if m["composite_ability"] is not None:
                if max_a == min_a:
                    m["ability_rescaled"] = Fraction(1, 2)
                else:
                    m["ability_rescaled"] = (
                        (m["composite_ability"] - min_a) / (max_a - min_a)
                    )
            else:
                m["ability_rescaled"] = None
    else:
        for m in plot_models:
            m["ability_rescaled"] = None

    # ── Determine power parameters from Pareto models ONLY ──
    pareto_priced = [m for m in pareto if m.get("normalized_cost") is not None]

    p_x = _compute_power_param(pareto_priced, "normalized_cost")
    p_y = _compute_power_param(pareto_priced, "ability_rescaled")

    # Compute Pareto medians for reporting
    pareto_costs = sorted([m["normalized_cost"] for m in pareto_priced])
    n_pc = len(pareto_costs)
    median_cost = float(pareto_costs[n_pc // 2]) if n_pc % 2 == 1 else float((pareto_costs[n_pc // 2 - 1] + pareto_costs[n_pc // 2]) / 2)

    pareto_abilities = sorted([m["ability_rescaled"] for m in pareto_priced if m.get("ability_rescaled") is not None])
    n_pa = len(pareto_abilities)
    median_ability = float(pareto_abilities[n_pa // 2]) if n_pa % 2 == 1 else float((pareto_abilities[n_pa // 2 - 1] + pareto_abilities[n_pa // 2]) / 2) if n_pa >= 2 else 0.5

    print(f"\n  Power-law exponential mapping (f(x) = x^p):")
    print(f"  Pareto models: {len(pareto_priced)}")
    print(f"  X-axis: median(normalized_cost) = {median_cost:.4f} → p_x = {p_x:.4f}")
    print(f"  Y-axis: median(ability_rescaled) = {median_ability:.4f} → p_y = {p_y:.4f}")
    print(f"  f(median) = median^p → {median_cost:.4f}^{p_x:.4f} = {median_cost**p_x:.4f} (X), "
          f"{median_ability:.4f}^{p_y:.4f} = {median_ability**p_y:.4f} (Y)")

    # ── Apply f(x) = x^p to ALL models ──
    for m in plot_models:
        # X-axis: exponential_cost = normalized_cost^p_x
        nc = float(m["normalized_cost"])
        m["exponential_cost"] = nc ** p_x

        # Y-axis: exponential_ability = ability_rescaled^p_y
        if m.get("ability_rescaled") is not None:
            ar = float(m["ability_rescaled"])
            m["exponential_ability"] = ar ** p_y
        else:
            m["exponential_ability"] = None

    print(f"  Mapped {len(plot_models)} total models through power-law function")

    # Store params for JSON output and visualization
    return plot_models, {"p_x": p_x, "p_y": p_y,
                         "median_cost": median_cost, "median_ability": median_ability}


# ══════════════════════════════════════════════════════════════════════
# Pareto frontier computation
# ══════════════════════════════════════════════════════════════════════

def compute_pareto(models):
    """Pareto frontier based on original per-request cost vs composite ability."""
    priced = [m for m in models if m.get("per_request_cost") is not None]
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
# Stage 3: Visualization
# ══════════════════════════════════════════════════════════════════════

def plot_analysis(models, pareto, mapping_params):
    """
    Generate the Pareto scatter plot:
    - Black background, 黑体 white font
    - 1:1 square aspect ratio
    - Axes at x=0 & y=0, boundary lines at x=1 & y=1
    - Only 0 and 1 ticks
    - Dashed lines from Pareto models to axes with pre-mapping values
    """
    try:
        from adjustText import adjust_text
        has_adj = True
    except ImportError:
        has_adj = False

    plot_models = [m for m in models if m.get("per_request_cost") is not None]
    pareto_names = {m["model"] for m in pareto}
    others = [m for m in plot_models if m["model"] not in pareto_names]

    # ── Figure: 黑色背景, 1:1 正方形 ──
    fig, ax = plt.subplots(figsize=(14, 14))
    fig.patch.set_facecolor("#000000")
    ax.set_facecolor("#000000")
    ax.set_aspect('equal', adjustable='box')

    # ── 数轴边界线: x=0, y=0 (数轴) + x=1, y=1 (图像边界) ──
    ax.axhline(y=0, color='#FFFFFF', linewidth=1.5, zorder=1)
    ax.axvline(x=0, color='#FFFFFF', linewidth=1.5, zorder=1)
    ax.axhline(y=1, color='#FFFFFF', linewidth=1.5, zorder=1)
    ax.axvline(x=1, color='#FFFFFF', linewidth=1.5, zorder=1)

    # ── Scatter: other models ──
    ax.scatter(
        [float(m["exponential_cost"]) for m in others],
        [float(m["exponential_ability"]) for m in others],
        c="#4A4A4A", s=20, alpha=0.45, zorder=2,
        label=f"其他模型 ({len(others)})",
    )

    # ── Scatter: Pareto frontier ──
    ax.scatter(
        [float(m["exponential_cost"]) for m in pareto],
        [float(m["exponential_ability"]) for m in pareto],
        c="#00E5FF", s=100, alpha=0.95, zorder=4,
        edgecolors="#FFFFFF", linewidth=1.2,
        label=f"Pareto前沿 ({len(pareto)})",
    )

    # ── Pareto frontier line ──
    pf = sorted(pareto, key=lambda m: m["exponential_cost"])
    ax.plot(
        [float(m["exponential_cost"]) for m in pf],
        [float(m["exponential_ability"]) for m in pf],
        c="#00E5FF", linewidth=2.0, alpha=0.35, zorder=3, linestyle="--",
    )

    # ── Dashed lines from each Pareto model to both axes ──
    for m in pf:
        x_idx = float(m["exponential_cost"])
        y_idx = float(m["exponential_ability"])
        x_pre = float(m["normalized_cost"])
        y_pre = float(m["ability_rescaled"])

        # 垂直虚线：从点向下连到X轴
        ax.plot([x_idx, x_idx], [0, y_idx],
                '--', color='#AAAAAA', alpha=0.40, linewidth=0.6, zorder=1)
        # 水平虚线：从点向左连到Y轴
        ax.plot([0, x_idx], [y_idx, y_idx],
                '--', color='#AAAAAA', alpha=0.40, linewidth=0.6, zorder=1)

        # X轴标注：指数化前的价格小数
        ax.text(x_idx, -0.035, f"{x_pre:.3f}",
                ha='center', va='top', fontsize=6,
                color='#CCCCCC', fontweight='bold', rotation=45)

        # Y轴标注：指数化前的综合性能小数
        ax.text(-0.03, y_idx, f"{y_pre:.3f}",
                ha='right', va='center', fontsize=6,
                color='#CCCCCC', fontweight='bold')

    # ── Pareto model labels ──
    texts = []
    for i, m in enumerate(pf):
        label = f"{i+1}. {m['model']}"
        t = ax.text(
            float(m["exponential_cost"]),
            float(m["exponential_ability"]),
            label,
            fontsize=8, ha="left", va="bottom",
            color="#FFFFFF", fontweight="bold", zorder=5,
            bbox=dict(boxstyle="round,pad=0.12",
                      facecolor="#1A1A1A", alpha=0.85,
                      edgecolor="#00E5FF", linewidth=0.5),
        )
        texts.append(t)

    if has_adj:
        adjust_text(texts,
                    arrowprops=dict(arrowstyle="->", color="#888888", lw=0.5),
                    expand_points=(1.8, 1.8),
                    force_text=(0.3, 0.5),
                    force_points=(0.1, 0.1),
                    lim=200)

    # ── Axis labels ──
    ax.set_xlabel("指数化单次价格 (0=最便宜, 1=最贵)",
                  fontsize=13, color="#FFFFFF", labelpad=10, fontweight="bold")
    ax.set_ylabel("指数化综合能力 (0=最低, 1=最高)",
                  fontsize=13, color="#FFFFFF", labelpad=10, fontweight="bold")
    p_x = mapping_params["p_x"]
    p_y = mapping_params["p_y"]
    ax.set_title(
        f"LLM 综合能力 vs 单次请求价格 — Pareto前沿\n"
        f"指数化映射 f(x) = x^p | X: p={p_x:.2f}, Y: p={p_y:.2f}\n"
        f"（映射参数仅由帕累托模型中位数决定 | 虚线标注=映射前小数）",
        fontsize=15, color="#FFFFFF", fontweight="bold", pad=16,
    )

    # ── Ticks: 只保留 0 和 1 ──
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])
    ax.set_xticklabels(["0", "1"], color="#FFFFFF", fontsize=12, fontweight="bold")
    ax.set_yticklabels(["0", "1"], color="#FFFFFF", fontsize=12, fontweight="bold")

    # ── Axis limits: 留小边距放标注 ──
    margin = 0.07
    ax.set_xlim(-margin, 1 + margin)
    ax.set_ylim(-margin, 1 + margin)

    # ── Spines: 隐藏（由边界线替代） ──
    for spine in ax.spines.values():
        spine.set_visible(False)

    # ── No grid ──
    ax.grid(False)

    # ── Tick parameters ──
    ax.tick_params(axis='both', colors='#FFFFFF', length=5, width=1.2)

    # ── Legend ──
    legend = ax.legend(loc="upper left", fontsize=10.5,
                       framealpha=0.85, edgecolor="#FFFFFF",
                       facecolor="#1A1A1A", labelcolor="#FFFFFF")

    # ── Method annotation ──
    p_x = mapping_params["p_x"]
    p_y = mapping_params["p_y"]
    med_c = mapping_params["median_cost"]
    med_a = mapping_params["median_ability"]
    method = (
        f"指数化映射 f(x) = x^p | 参数仅由帕累托前沿{len(pareto)}模型中位数决定\n"
        f"X: p_x = {p_x:.3f} (median = {med_c:.3f} → 0.5) | "
        f"Y: p_y = {p_y:.3f} (median = {med_a:.3f} → 0.5)\n"
        f"★ 全程Fraction精确运算(至映射前) | 虚线端标注=映射前归一化小数值 | 共{len(plot_models)}模型"
    )
    ax.text(0.98, 0.02, method, transform=ax.transAxes, fontsize=6,
            va="bottom", ha="right", color="#AAAAAA", style="italic",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#111111", alpha=0.85,
                      edgecolor="#444444", linewidth=0.5))

    plt.tight_layout()
    out = os.path.join(OUTPUT_DIR, "pareto_analysis.png")
    plt.savefig(out, dpi=200, bbox_inches="tight", facecolor="#000000")
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
    output = {
        "metadata": {
            "source": "https://artificialanalysis.ai/leaderboards/models",
            "methodology": (
                "15 Intelligence metrics normalized [0,1], averaged → composite ability; "
                "Pareto = non-dominated by per-request cost; "
                "Power-law exponential mapping f(x) = x^p where p = log(0.5)/log(median_pareto)"
            ),
            "arithmetic": (
                "All intermediate calculations use fractions.Fraction for exact rational arithmetic "
                "up to the point before the power-law mapping; the mapping f(x) = x^p with "
                "non-integer p inherently requires float, but the parameter p is determined "
                "by exact Fraction median of Pareto models"
            ),
            "index_mapping": {
                "type": "power-law: f(x) = x^p where p = log(0.5) / log(median_pareto)",
                "x_axis": f"p_x determined by median normalized_cost of Pareto models",
                "y_axis": f"p_y determined by median ability_rescaled of Pareto models",
                "note": "f(0)=0, f(1)=1 always; f(median)=0.5; smooth continuous monotonic function",
            },
            "per_request_cost": {
                "non_reasoning": "Output_tokens = (Total - TTFT) × Speed; Cost = (In × InPrice + Out × OutPrice) / 1M",
                "reasoning_with_time": "Output_tokens = (Total - TTFT) × Speed; Cost = (In × InPrice + Out × OutPrice) / 1M",
                "reasoning_no_time": "Output_tokens = Total × Speed; Cost = (In × InPrice + Out × OutPrice) / 1M",
            },
            "total_models": len(models),
            "pareto_count": len(pareto),
        },
        "metric_ranges": {
            METRIC_LABELS[k]: {
                "min": float(v["min"]),
                "max": float(v["max"]),
                "count": v["count"],
                "min_fraction": str(v["min"]),
                "max_fraction": str(v["max"]),
            } if isinstance(v, dict) else v
            for k, v in metric_ranges.items()
        },
        "pareto_frontier": [_export_model(m, i + 1) for i, m in enumerate(pareto)],
        "all_models": [
            {
                "model": m["model"],
                "composite_ability": float(m["composite_ability"]),
                "composite_ability_fraction": str(m["composite_ability"]),
                "ability_rescaled": _frac_to_json(m.get("ability_rescaled")),
                "ability_rescaled_fraction": str(m["ability_rescaled"]) if m.get("ability_rescaled") is not None else None,
                "exponential_cost": _frac_to_json(m.get("exponential_cost")),
                "exponential_ability": _frac_to_json(m.get("exponential_ability")),
                "per_request_cost": _frac_to_json(m.get("per_request_cost")),
                "per_request_cost_fraction": str(m["per_request_cost"]) if m.get("per_request_cost") is not None else None,
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
    return {
        "rank": rank,
        "model": m["model"],
        "is_reasoning": m["is_reasoning"],
        "composite_ability": float(m["composite_ability"]),
        "composite_ability_fraction": str(m["composite_ability"]),
        "ability_rescaled": _frac_to_json(m.get("ability_rescaled")),
        "ability_rescaled_fraction": str(m.get("ability_rescaled")) if m.get("ability_rescaled") is not None else None,
        "exponential_cost": _frac_to_json(m.get("exponential_cost")),
        "exponential_ability": _frac_to_json(m.get("exponential_ability")),
        "per_request_cost_usd": _frac_to_json(m.get("per_request_cost")),
        "per_request_cost_fraction": str(m["per_request_cost"]) if m.get("per_request_cost") is not None else None,
        "normalized_cost": _frac_to_json(m.get("normalized_cost")),
        "normalized_cost_fraction": str(m["normalized_cost"]) if m.get("normalized_cost") is not None else None,
        "input_output_ratio": _frac_to_json(m.get("input_output_ratio")),
        "input_output_ratio_fraction": str(m["input_output_ratio"]) if m.get("input_output_ratio") is not None else None,
        "speed": _frac_to_json(m["speed"]),
        "ttft": _frac_to_json(m["ttft"]),
        "total_response": _frac_to_json(m["total_response"]),
        "reasoning_time": _frac_to_json(m["reasoning_time"]),
        "total_output_tokens": _frac_to_json(m.get("total_output_tokens")),
        "total_output_tokens_fraction": str(m.get("total_output_tokens")) if m.get("total_output_tokens") is not None else None,
        "input_tokens": _frac_to_json(m.get("input_tokens")),
        "input_tokens_fraction": str(m.get("input_tokens")) if m.get("input_tokens") is not None else None,
        "cost_method": m.get("cost_method"),
        "valid_metrics": m["valid_metrics"],
    }


def generate_readme(pareto, models):
    lines = []
    lines.append("# LLM Leaderboard Pareto Analysis\n")
    lines.append("![Pareto Analysis](output/pareto_analysis.png)\n")
    lines.append("## Pareto 前沿模型（综合能力从高到低）\n")
    lines.append("| # | 模型 | 综合能力 | 再归一化 | 指数化能力 | 单次价格 (USD) | 归一化价格 | 指数化价格 | 推理 |")
    lines.append("|---|------|---------|---------|-----------|---------------|-----------|-----------|------|")

    for i, m in enumerate(pareto):
        prc = m.get("per_request_cost")
        prc_str = f"${float(prc):.4f}" if prc is not None else "--"
        reas = "Y" if m["is_reasoning"] else "N"
        ab_rescaled = f"{float(m['ability_rescaled']):.4f}" if m.get("ability_rescaled") is not None else "--"
        exp_ab = f"{float(m['exponential_ability']):.4f}" if m.get("exponential_ability") is not None else "--"
        norm_c = f"{float(m['normalized_cost']):.4f}" if m.get("normalized_cost") is not None else "--"
        exp_c = f"{float(m['exponential_cost']):.4f}" if m.get("exponential_cost") is not None else "--"
        lines.append(
            f"| {i+1} | {m['model']} | {float(m['composite_ability']):.4f} "
            f"| {ab_rescaled} | {exp_ab} | {prc_str} | {norm_c} | {exp_c} | {reas} |"
        )

    lines.append("")
    lines.append("### 评分方法")
    lines.append("")
    lines.append("1. **15项Intelligence子指标**各自线性归一化到 [0,1]")
    lines.append("2. **综合能力值** = 所有有效归一化分数的算术平均")
    lines.append("3. **Pareto前沿** = 不被任何其他模型支配的模型")
    lines.append("")
    lines.append("### 指数化映射方法")
    lines.append("")
    lines.append("**映射函数**：f(x) = x^p，其中 p = log(0.5) / log(median_pareto)")
    lines.append("")
    lines.append("**核心原则**：")
    lines.append("- 映射是连续数学函数，不是排名重分配")
    lines.append("- f(0) = 0, f(1) = 1（端点不变）")
    lines.append("- f(median) = 0.5（中位数映射到0.5，使分布以0.5为中心）")
    lines.append("- 参数 p 仅由帕累托前沿模型的数据分布决定")
    lines.append("")
    lines.append("**X轴（价格）**：")
    lines.append("1. 所有模型单次请求价格 min-max 归一化到 [0,1]")
    lines.append("2. 仅取帕累托前沿模型的归一化价格中位数，计算 p_x")
    lines.append("3. 对所有模型应用 exponential_cost = normalized_cost^p_x")
    lines.append("")
    lines.append("**Y轴（综合能力）**：")
    lines.append("1. 综合能力再归一化：最低=0，最高=1")
    lines.append("2. 仅取帕累托前沿模型的再归一化中位数，计算 p_y")
    lines.append("3. 对所有模型应用 exponential_ability = ability_rescaled^p_y")
    lines.append("")
    lines.append("### 精确分数计算")
    lines.append("")
    lines.append("全程使用 Python `fractions.Fraction` 进行精确有理数运算：")
    lines.append("- 所有解析值、归一化、均值、比值、价格计算均使用精确分数")
    lines.append("- 幂函数映射 f(x) = x^p 参数由 Fraction 中位数确定，映射本身因非整数指数需用 float")
    lines.append("- 仅在绘图坐标传入 matplotlib 及 JSON 序列化时转为浮点数")
    lines.append("")
    lines.append("### 单次请求价格计算")
    lines.append("")
    lines.append("```")
    lines.append("输入输出比 r = (Blended - Output_Price) / (Input_Price - Output_Price)")
    lines.append("非推理/推理有ReasonT: 输出tokens = (Total_Response - TTFT) × Speed")
    lines.append("推理无ReasonT: 输出tokens = Total_Response × Speed")
    lines.append("输入tokens = 输出tokens × r / (1-r)")
    lines.append("单次价格 = (输入tokens × Input_Price + 输出tokens × Output_Price) / 1,000,000")
    lines.append("```")
    lines.append("")
    lines.append(f"**数据来源**: [Artificial Analysis](https://artificialanalysis.ai/leaderboards/models)  ")
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

    # ── Stage 1 ──
    print("\n[Stage 1] Computing scores & per-request costs (exact Fraction arithmetic)...")
    models, metric_ranges = compute_scores(data)

    with_prc = [m for m in models if m.get("per_request_cost") is not None]
    if with_prc:
        costs = [m["per_request_cost"] for m in with_prc]
        print(f"  Per-request cost: {len(with_prc)}/{len(models)} models computable")
        print(f"  Range: ${float(min(costs)):.4f} – ${float(max(costs)):.4f}")

    methods = Counter(m.get("cost_method") for m in models if m.get("cost_method"))
    print(f"  Cost methods: {dict(methods)}")

    # ── Pareto frontier (computed BEFORE index mapping) ──
    print("\nComputing Pareto frontier (exact Fraction comparison on original values)...")
    pareto = compute_pareto(models)
    print(f"  Pareto frontier: {len(pareto)} models")

    # ── Stage 2 ──
    print("\n[Stage 2] Applying power-law exponential mapping (f(x) = x^p)...")
    plot_models, mapping_params = apply_index_mapping(models, pareto)

    # ── Stage 3 ──
    print("\n[Stage 3] Generating visualization...")
    plot_analysis(plot_models, pareto, mapping_params)

    print("\nSaving results...")
    save_results(models, pareto, metric_ranges)

    # ── Print Pareto table ──
    print(f"\n{'='*120}")
    print(f"PARETO FRONTIER ({len(pareto)} models) — ranked by composite ability")
    print(f"{'='*120}")
    print(f"{'#':<3} {'Model':<36} {'Ability':>8} {'Rescaled':>9} "
          f"{'Exp.Ab':>7} {'PerReq$':>10} {'NormCost':>9} {'Exp.Cost':>8} {'Reas':>4}")
    print(f"{'-'*3} {'-'*36} {'-'*8} {'-'*9} {'-'*7} {'-'*10} {'-'*9} {'-'*8} {'-'*4}")
    for i, m in enumerate(pareto):
        prc = f"${float(m['per_request_cost']):.4f}" if m.get("per_request_cost") else "--"
        ab_r = f"{float(m['ability_rescaled']):.4f}" if m.get("ability_rescaled") else "--"
        exp_ab = f"{float(m['exponential_ability']):.4f}" if m.get("exponential_ability") else "--"
        nc = f"{float(m['normalized_cost']):.4f}" if m.get("normalized_cost") else "--"
        exp_c = f"{float(m['exponential_cost']):.4f}" if m.get("exponential_cost") else "--"
        reas = "Y" if m["is_reasoning"] else "N"
        print(f"{i+1:<3} {m['model']:<36} {float(m['composite_ability']):>8.4f} "
              f"{ab_r:>9} {exp_ab:>7} {prc:>10} {nc:>9} {exp_c:>8} {reas:>4}")

    print("\nDone! (Power-law exponential mapping → square 1:1 plot)")


if __name__ == "__main__":
    main()
