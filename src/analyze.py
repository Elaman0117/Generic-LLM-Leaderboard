#!/usr/bin/env python3
"""
Scoring system and Pareto analysis for Artificial Analysis LLM Leaderboard.

**Version 8**: Uses AA's own measured cost data directly.

Key change from v7: Instead of estimating per-request cost from timing/speed data
and blended prices, we now use AA's `intelligenceIndexCostTotal` — the actual
measured cost to run the complete AA Intelligence Index benchmark suite.

This eliminates all the problems with:
  - Estimating output tokens from timing data
  - Not knowing reasoning token counts for models without Reasoning_Time
  - Assuming a fixed 7:2:1 cache:input:output ratio
  - Missing cache hit pricing data

The X-axis now represents the real cost to run a standardized benchmark suite,
which is a much more meaningful and accurate cost metric.

Data source: AA's Next.js RSC payload (500 models × 88 fields)
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
            # Pricing (direct from AA)
            "input_price": _to_frac(d.get("price1mInputTokens")),
            "output_price": _to_frac(d.get("price1mOutputTokens")),
            "cache_hit_price": _to_frac(d.get("cacheHitPrice")),
            "blended_price_721": _to_frac(d.get("price1mBlended7To2To1")),
            # AA's measured Intelligence Index cost (THE KEY METRIC)
            "intelligence_index_cost_total": _to_frac(d.get("intelligenceIndexCostTotal")),
            "intelligence_index_cost_input": _to_frac(d.get("intelligenceIndexCostInput")),
            "intelligence_index_cost_output": _to_frac(d.get("intelligenceIndexCostOutput")),
            "intelligence_index_cost_reasoning": _to_frac(d.get("intelligenceIndexCostReasoning")),
            "intelligence_index_cost_answer": _to_frac(d.get("intelligenceIndexCostAnswer")),
            # Speed data
            "speed": _to_frac(d.get("medianOutputTokensPerSecond")),
            "ttft": _to_frac(d.get("medianTimeToFirstTokenSeconds")),
            "total_response": _to_frac(d.get("medianEndToEndResponseTimeSeconds")),
            "reasoning_time": _to_frac(d.get("medianReasoningTimeSeconds")),
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
    print(f"  With intelligence_index_cost_total: {sum(1 for m in models if m['intelligence_index_cost_total'] is not None)}")

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

    # ── Use AA's measured cost directly ──
    # The cost is the actual cost in USD to run the AA Intelligence Index
    for m in valid:
        m["per_request_cost"] = m["intelligence_index_cost_total"]

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

        print(f"Intelligence Index cost range: ${float(min(m['per_request_cost'] for m in priced)):.2f} – ${float(max(m['per_request_cost'] for m in priced)):.2f}")
        print(f"Max Pareto frontier cost (normalization ceiling): ${float(max_pareto_cost):.2f}")

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
    try:
        from adjustText import adjust_text
        has_adj = True
    except ImportError:
        has_adj = False

    plot_models = [m for m in models if m.get("per_request_cost") is not None]
    pareto_names = {m["model"] for m in pareto}
    others = [m for m in plot_models if m["model"] not in pareto_names]

    fig, ax = plt.subplots(figsize=(14, 14))
    fig.patch.set_facecolor("#000000")
    ax.set_facecolor("#000000")
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

    # Scatter: other models
    ax.scatter(
        [float(m["normalized_cost"]) for m in others],
        [float(m["composite_ability"]) for m in others],
        c="#4A4A4A", s=20, alpha=0.45, zorder=2,
        label=f"其他模型 ({len(others)})",
    )

    # Scatter: Pareto frontier
    ax.scatter(
        [float(m["normalized_cost"]) for m in pareto],
        [float(m["composite_ability"]) for m in pareto],
        c="#00E5FF", s=100, alpha=0.95, zorder=4,
        edgecolors="#FFFFFF", linewidth=1.2,
        label=f"Pareto前沿 ({len(pareto)})",
    )

    # Pareto frontier line
    pf = sorted(pareto, key=lambda m: m["normalized_cost"])
    ax.plot(
        [float(m["normalized_cost"]) for m in pf],
        [float(m["composite_ability"]) for m in pf],
        c="#00E5FF", linewidth=2.0, alpha=0.35, zorder=3, linestyle="--",
    )

    # Pareto model labels
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

    ax.set_xlabel("归一化 Intelligence Index 运行成本 (0=免费, 1=最贵帕累托模型)",
                  fontsize=13, color="#FFFFFF", labelpad=10, fontweight="bold")
    ax.set_ylabel("综合能力 (0=最低, 1=最高)",
                  fontsize=13, color="#FFFFFF", labelpad=10, fontweight="bold")
    ax.set_title(
        f"LLM 综合能力 vs Intelligence Index 运行成本 — Pareto前沿\n"
        f"（成本数据来自AA实测 | X轴线性归一化坐标）",
        fontsize=15, color="#FFFFFF", fontweight="bold", pad=16,
    )

    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])
    ax.set_xticklabels(["0", "1"], color="#FFFFFF", fontsize=12, fontweight="bold")
    ax.set_yticklabels(["0", "1"], color="#FFFFFF", fontsize=12, fontweight="bold")

    margin = 0.07
    ax.set_xlim(-margin, 1 + margin)
    ax.set_ylim(-margin, 1 + margin)

    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.grid(False)
    ax.tick_params(axis='both', colors='#FFFFFF', length=5, width=1.2)

    legend = ax.legend(loc="upper left", fontsize=10.5,
                       framealpha=0.85, edgecolor="#FFFFFF",
                       facecolor="#1A1A1A", labelcolor="#FFFFFF")

    method = (
        f"X轴: AA实测Intelligence Index运行成本(线性归一化) | Y轴: 综合能力(18指标均值)\n"
        f"★ 成本为AA实测数据，非估算 | 共{len(plot_models)}模型"
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
                "18 evaluation metrics normalized [0,1], averaged → composite ability; "
                "Pareto = non-dominated by Intelligence Index cost; "
                "X-axis: linear-normalized cost (cost/max(Pareto cost) → [0,1]); "
                "Y-axis: composite ability (linear, direct average); "
                "Cost = AA's measured Intelligence Index total cost (not estimated)"
            ),
            "cost_source": "intelligenceIndexCostTotal from AA RSC payload — actual measured cost to run the complete AA Intelligence Index benchmark suite",
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
                "intelligence_index_cost_total": _frac_to_json(m.get("intelligence_index_cost_total")),
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
        "creator": m["creator"],
        "is_reasoning": m["is_reasoning"],
        "composite_ability": float(m["composite_ability"]),
        "intelligence_index_cost_usd": _frac_to_json(m.get("intelligence_index_cost_total")),
        "intelligence_index_cost_input": _frac_to_json(m.get("intelligence_index_cost_input")),
        "intelligence_index_cost_output": _frac_to_json(m.get("intelligence_index_cost_output")),
        "intelligence_index_cost_reasoning": _frac_to_json(m.get("intelligence_index_cost_reasoning")),
        "intelligence_index_cost_answer": _frac_to_json(m.get("intelligence_index_cost_answer")),
        "normalized_cost": _frac_to_json(m.get("normalized_cost")),
        "input_price": _frac_to_json(m.get("input_price")),
        "output_price": _frac_to_json(m.get("output_price")),
        "cache_hit_price": _frac_to_json(m.get("cache_hit_price")),
        "blended_price_721": _frac_to_json(m.get("blended_price_721")),
        "speed": _frac_to_json(m["speed"]),
        "ttft": _frac_to_json(m["ttft"]),
        "total_response": _frac_to_json(m["total_response"]),
        "reasoning_time": _frac_to_json(m["reasoning_time"]),
        "valid_metrics": m["valid_metrics"],
    }


def generate_readme(pareto, models):
    lines = []
    lines.append("# LLM Leaderboard Pareto Analysis\n")
    lines.append("![Pareto Analysis](output/pareto_analysis.png)\n")
    lines.append("## Pareto 前沿模型（综合能力从高到低）\n")
    lines.append("| # | 模型 | 综合能力 | Intelligence Index成本 (USD) | 归一化成本 | 推理 |")
    lines.append("|---|------|---------|---------------------------|-----------|------|")

    for i, m in enumerate(pareto):
        cost = m.get("intelligence_index_cost_total")
        cost_str = f"${float(cost):.2f}" if cost is not None else "--"
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
    lines.append("### 成本说明")
    lines.append("")
    lines.append("**X轴成本 = AA 实测 Intelligence Index 运行成本**")
    lines.append("")
    lines.append("成本数据来自 Artificial Analysis 的实测数据 (`intelligenceIndexCostTotal`)，")
    lines.append("即运行完整的 AA Intelligence Index 基准测试套件的实际费用。")
    lines.append("这比自行估算更准确，因为：")
    lines.append("- 包含了 reasoning tokens 的实际收费")
    lines.append("- 包含了 cache hit/input/output 的实际 token 分配")
    lines.append("- 基于标准化的 benchmark 套件，可公平比较")
    lines.append("")
    lines.append("### 数据来源")
    lines.append("")
    lines.append(f"**数据来源**: [Artificial Analysis](https://artificialanalysis.ai/leaderboards/models)  ")
    lines.append(f"**方法论**: [AA Methodology](https://artificialanalysis.ai/methodology)  ")
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
        print(f"  Cost range: ${float(min(costs)):.2f} – ${float(max(costs)):.2f}")

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
    print(f"{'#':<3} {'Model':<36} {'Ability':>8} {'Cost$':>12} {'NormCost':>9} {'Reas':>4}")
    print(f"{'-'*3} {'-'*36} {'-'*8} {'-'*12} {'-'*9} {'-'*4}")
    for i, m in enumerate(pareto):
        cost = f"${float(m['per_request_cost']):.2f}" if m.get("per_request_cost") else "--"
        nc = f"{float(m['normalized_cost']):.4f}" if m.get("normalized_cost") else "--"
        reas = "Y" if m["is_reasoning"] else "N"
        print(f"{i+1:<3} {m['model']:<36} {float(m['composite_ability']):>8.4f} "
              f"{cost:>12} {nc:>9} {reas:>4}")

    print("\nDone!")


if __name__ == "__main__":
    main()
