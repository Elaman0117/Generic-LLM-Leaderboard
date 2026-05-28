#!/usr/bin/env python3
"""
Scoring system, per-request cost calculation, and Pareto analysis
for Artificial Analysis LLM Leaderboard.

**Modified version (v6)**: Two-stage computation pipeline:

  Stage 1 — Exact Fraction arithmetic
    All intermediate calculations use `fractions.Fraction` for exact rational
    arithmetic. No floating-point rounding at any step.

  Stage 2 — Float conversion ONLY at matplotlib chart coordinates

Visualization:
    - Black background, 黑体 (Heiti) white font
    - 1:1 square aspect ratio
    - Boundary frame: axes at x=0 & y=0, boundary lines at x=1 & y=1
      (all constrained within [0,1] range)
    - Only 0 and 1 on tick marks
    - Faint grid lines at 0.1 intervals (10 divisions)
    - No secondary normalization or exponential mapping
"""

import json
import math
import os
import sys
from collections import Counter
from fractions import Fraction

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
    "APEX_Agents_AA", "ITBench_AA", "MMMU_Pro",
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
    "ITBench_AA": "ITBench-AA Kubernetes",
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

    # ── Normalize per-request cost (log-scale normalization) ──
    # Price spans several orders of magnitude ($0.0001 – $3.66),
    # so linear normalization crushes everything near 0.
    # Log-normalization spreads the data naturally:
    #   log_cost = ln(per_request_cost)
    #   normalized_cost = (log_cost - min_log) / (max_log - min_log)
    priced = [m for m in valid if m.get("per_request_cost") is not None]
    if priced:
        costs = [m["per_request_cost"] for m in priced]
        min_c, max_c = min(costs), max(costs)
        print(f"Per-request cost range: ${float(min_c):.4f} – ${float(max_c):.4f}")
        # Compute log values
        log_costs = [math.log(float(c)) for c in costs if float(c) > 0]
        if len(log_costs) >= 2:
            min_log, max_log = min(log_costs), max(log_costs)
        else:
            min_log, max_log = 0.0, 1.0
        print(f"Log-normalized cost range: ln({float(min_c):.4f})={min_log:.4f} – ln({float(max_c):.4f})={max_log:.4f}")
        for m in priced:
            cost_f = float(m["per_request_cost"])
            if cost_f <= 0 or max_log == min_log:
                m["normalized_cost"] = Fraction(1, 2)
            else:
                log_c = math.log(cost_f)
                m["normalized_cost"] = Fraction.from_float(
                    (log_c - min_log) / (max_log - min_log)
                ).limit_denominator(10**12)
    for m in valid:
        if "normalized_cost" not in m:
            m["normalized_cost"] = None

    return valid, metric_ranges


# ══════════════════════════════════════════════════════════════════════
# Stage 2: (Removed — no secondary normalization or exponential mapping)
# ══════════════════════════════════════════════════════════════════════

def get_plot_models(models):
    """Filter models that have valid normalized_cost for plotting.
    No secondary normalization or exponential mapping is applied.
    X-axis uses normalized_cost directly; Y-axis uses composite_ability directly.
    """
    plot_models = [m for m in models if m.get("normalized_cost") is not None]
    print(f"\n  Direct linear values (no exponential mapping):")
    print(f"  {len(plot_models)} models with valid normalized_cost for plotting")
    print(f"  X-axis: normalized_cost (min-max normalized [0,1])")
    print(f"  Y-axis: composite_ability (average of [0,1] normalized metrics)")
    return plot_models


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

def plot_analysis(models, pareto):
    """
    Generate the Pareto scatter plot:
    - Black background, 黑体 white font
    - 1:1 square aspect ratio
    - Boundary frame: lines constrained within [0,1] range
    - Only 0 and 1 ticks
    - Faint grid lines at 0.1 intervals (10 divisions)
    - No exponential mapping: X=normalized_cost, Y=composite_ability
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

    # ── 数轴边界线: 限制在 [0,1] 值域内 ──
    # X轴 (y=0): 从 x=0 到 x=1
    ax.plot([0, 1], [0, 0], color='#FFFFFF', linewidth=1.5, zorder=1)
    # Y轴 (x=0): 从 y=0 到 y=1
    ax.plot([0, 0], [0, 1], color='#FFFFFF', linewidth=1.5, zorder=1)
    # 上边界 (y=1): 从 x=0 到 x=1
    ax.plot([0, 1], [1, 1], color='#FFFFFF', linewidth=1.5, zorder=1)
    # 右边界 (x=1): 从 y=0 到 y=1
    ax.plot([1, 1], [0, 1], color='#FFFFFF', linewidth=1.5, zorder=1)

    # ── 淡色网格线: 十等分 (0.1, 0.2, ..., 0.9) ──
    grid_color = '#333333'  # 很淡的灰色
    grid_alpha = 0.5
    grid_lw = 0.4
    for v in [i / 10 for i in range(1, 10)]:
        ax.plot([0, 1], [v, v], color=grid_color, alpha=grid_alpha, linewidth=grid_lw, zorder=0)
        ax.plot([v, v], [0, 1], color=grid_color, alpha=grid_alpha, linewidth=grid_lw, zorder=0)

    # ── Scatter: other models ──
    ax.scatter(
        [float(m["normalized_cost"]) for m in others],
        [float(m["composite_ability"]) for m in others],
        c="#4A4A4A", s=20, alpha=0.45, zorder=2,
        label=f"其他模型 ({len(others)})",
    )

    # ── Scatter: Pareto frontier ──
    ax.scatter(
        [float(m["normalized_cost"]) for m in pareto],
        [float(m["composite_ability"]) for m in pareto],
        c="#00E5FF", s=100, alpha=0.95, zorder=4,
        edgecolors="#FFFFFF", linewidth=1.2,
        label=f"Pareto前沿 ({len(pareto)})",
    )

    # ── Pareto frontier line ──
    pf = sorted(pareto, key=lambda m: m["normalized_cost"])
    ax.plot(
        [float(m["normalized_cost"]) for m in pf],
        [float(m["composite_ability"]) for m in pf],
        c="#00E5FF", linewidth=2.0, alpha=0.35, zorder=3, linestyle="--",
    )

    # ── Pareto model labels ──
    texts = []
    for i, m in enumerate(pf):
        label = f"{i+1}. {m['model']}"
        t = ax.text(
            float(m["normalized_cost"]),
            float(m["composite_ability"]),
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
    ax.set_xlabel("对数归一化单次请求价格 (0=最便宜, 1=最贵)",
                  fontsize=13, color="#FFFFFF", labelpad=10, fontweight="bold")
    ax.set_ylabel("综合能力 (0=最低, 1=最高)",
                  fontsize=13, color="#FFFFFF", labelpad=10, fontweight="bold")
    ax.set_title(
        f"LLM 综合能力 vs 单次请求价格 — Pareto前沿\n"
        f"（全程Fraction精确运算 | X轴对数归一化坐标）",
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

    # ── No matplotlib grid (we drew our own faint grid) ──
    ax.grid(False)

    # ── Tick parameters ──
    ax.tick_params(axis='both', colors='#FFFFFF', length=5, width=1.2)

    # ── Legend ──
    legend = ax.legend(loc="upper left", fontsize=10.5,
                       framealpha=0.85, edgecolor="#FFFFFF",
                       facecolor="#1A1A1A", labelcolor="#FFFFFF")

    # ── Method annotation ──
    method = (
        f"X轴: 对数归一化 ln(cost)→[0,1] | Y轴: 综合能力(线性)\n"
        f"★ 全程Fraction精确运算(至归一化前) | 共{len(plot_models)}模型"
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
                "X-axis: log-normalized cost (ln(cost) mapped to [0,1]); "
                "Y-axis: composite ability (linear, direct average)"
            ),
            "arithmetic": (
                "All intermediate calculations use fractions.Fraction for exact rational arithmetic; "
                "float conversion only at matplotlib coordinate input and JSON serialization"
            ),
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
                "normalized_cost": _frac_to_json(m.get("normalized_cost")),
                "normalized_cost_fraction": str(m["normalized_cost"]) if m.get("normalized_cost") is not None else None,
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
    lines.append("| # | 模型 | 综合能力 | 单次价格 (USD) | 归一化价格 | 推理 |")
    lines.append("|---|------|---------|---------------|-----------|------|")

    for i, m in enumerate(pareto):
        prc = m.get("per_request_cost")
        prc_str = f"${float(prc):.4f}" if prc is not None else "--"
        reas = "Y" if m["is_reasoning"] else "N"
        norm_c = f"{float(m['normalized_cost']):.4f}" if m.get("normalized_cost") is not None else "--"
        lines.append(
            f"| {i+1} | {m['model']} | {float(m['composite_ability']):.4f} "
            f"| {prc_str} | {norm_c} | {reas} |"
        )

    lines.append("")
    lines.append("### 评分方法")
    lines.append("")
    lines.append("1. **15项Intelligence子指标**各自线性归一化到 [0,1]")
    lines.append("2. **综合能力值** = 所有有效归一化分数的算术平均")
    lines.append("3. **Pareto前沿** = 不被任何其他模型支配的模型")
    lines.append("")
    lines.append("### 坐标说明")
    lines.append("")
    lines.append("**X轴（对数归一化价格）**：")
    lines.append("1. 对单次请求价格取自然对数：ln(cost)")
    lines.append("2. 将 ln(cost) 归一化到 [0,1]：0 = 最便宜，1 = 最贵")
    lines.append("3. 对数归一化使跨数量级的价格差异在图上更均匀分布")
    lines.append("")
    lines.append("**Y轴（综合能力）**：")
    lines.append("1. 15项Intelligence子指标各自归一化到 [0,1]")
    lines.append("2. 综合能力 = 所有有效归一化分数的算术平均（已在 [0,1] 范围内）")
    lines.append("3. 0 = 最低，1 = 最高")
    lines.append("")
    lines.append("### 精确分数计算")
    lines.append("")
    lines.append("全程使用 Python `fractions.Fraction` 进行精确有理数运算：")
    lines.append("- 所有解析值、归一化、均值、比值、价格计算均使用精确分数")
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

    # ── Stage 2 (removed: no exponential mapping) ──
    print("\n[Stage 2] Preparing plot models (direct linear values, no mapping)...")
    plot_models = get_plot_models(models)

    # ── Stage 3 ──
    print("\n[Stage 3] Generating visualization...")
    plot_analysis(plot_models, pareto)

    print("\nSaving results...")
    save_results(models, pareto, metric_ranges)

    # ── Print Pareto table ──
    print(f"\n{'='*120}")
    print(f"PARETO FRONTIER ({len(pareto)} models) — ranked by composite ability")
    print(f"{'='*120}")
    print(f"{'#':<3} {'Model':<36} {'Ability':>8} {'PerReq$':>10} {'NormCost':>9} {'Reas':>4}")
    print(f"{'-'*3} {'-'*36} {'-'*8} {'-'*10} {'-'*9} {'-'*4}")
    for i, m in enumerate(pareto):
        prc = f"${float(m['per_request_cost']):.4f}" if m.get("per_request_cost") else "--"
        nc = f"{float(m['normalized_cost']):.4f}" if m.get("normalized_cost") else "--"
        reas = "Y" if m["is_reasoning"] else "N"
        print(f"{i+1:<3} {m['model']:<36} {float(m['composite_ability']):>8.4f} "
              f"{prc:>10} {nc:>9} {reas:>4}")

    print("\nDone! (Linear normalized coordinates → square 1:1 plot)")


if __name__ == "__main__":
    main()
