#!/usr/bin/env python3
"""
Scoring system, per-request cost calculation, and Pareto analysis
for Artificial Analysis LLM Leaderboard.

Per-request cost logic:
  Case A: Non-reasoning model
    - TTFT is genuine processing latency, no tokens generated during it
    - Output tokens = (Total_Response - TTFT) × Speed
    - Cost = (In_tokens × In_Price + Out_tokens × Out_Price) / 1M

  Case B: Reasoning model WITH Reasoning_Time data
    - TTFT is time to first CoT token (thinking already started)
    - (Total - TTFT) already includes all reasoning + visible output tokens
    - Reasoning_Time is a subset of (Total - TTFT), NOT additive
    - Output tokens = (Total_Response - TTFT) × Speed
    - Cost = (In_tokens × In_Price + Out_tokens × Out_Price) / 1M

  Case C: Reasoning model WITHOUT Reasoning_Time data
    - Model's CoT is not output/visible, so First Chunk is meaningless
    - The model is generating tokens (hidden reasoning) the entire time
    - Assume ALL time is spent generating tokens
    - Output tokens = Total_Response × Speed
    - Cost = (In_tokens × In_Price + Out_tokens × Out_Price) / 1M

  Input/Output ratio:
    r = (Blended - Output_Price) / (Input_Price - Output_Price)
    Input_tokens = Output_tokens × r / (1-r)

Pareto frontier:
  X-axis = per-request cost (normalized), Y-axis = composite ability
  A model dominates another if it is cheaper AND more capable.
"""

import json
import os
import sys
from collections import Counter

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# ── Font setup ──
_CJK = [
    "/usr/share/fonts/truetype/chinese/SarasaMonoSC-Regular.ttf",
    "/usr/share/fonts/truetype/noto-serif-sc/NotoSerifSC-Regular.ttf",
    "/usr/share/fonts/truetype/lxgw-wenkai/LXGWWenKai-Regular.ttf",
]
_LATIN = ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]
for fp in _CJK:
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
MIN_INPUT_OUTPUT_RATIO = 0.01
MAX_INPUT_OUTPUT_RATIO = 0.99


# ── Parsing ──
def parse_val(s):
    if s in ("--", ""):
        return None
    s = s.replace("%", "").replace("$", "").replace(",", "").strip()
    try:
        return float(s)
    except ValueError:
        return None


def parse_price(s):
    if s in ("--", ""):
        return None
    s = s.replace("$", "").replace(",", "").strip()
    try:
        return float(s)
    except ValueError:
        return None


# ── Core ──
def load_data():
    with open(RAW_DATA_FILE, encoding="utf-8") as f:
        return json.load(f)


def compute_scores(data):
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

    # Metric ranges
    metric_ranges = {}
    for metric in METRICS:
        vals = [m["_parsed"][metric] for m in models if m["_parsed"][metric] is not None]
        if len(vals) >= 2:
            metric_ranges[metric] = {"min": min(vals), "max": max(vals), "count": len(vals)}
        else:
            metric_ranges[metric] = None

    # Normalize metrics
    for m in models:
        m["_norm"] = {}
        for metric in METRICS:
            val = m["_parsed"][metric]
            rng = metric_ranges.get(metric)
            if val is None or rng is None:
                m["_norm"][metric] = None
            elif rng["max"] == rng["min"]:
                m["_norm"][metric] = 0.5
            else:
                m["_norm"][metric] = (val - rng["min"]) / (rng["max"] - rng["min"])

    # Composite ability
    for m in models:
        nv = [v for v in m["_norm"].values() if v is not None]
        m["composite_ability"] = sum(nv) / len(nv) if nv else None
        m["valid_metrics"] = len(nv)

    # Quality filter: need ≥5 valid metrics
    valid = [m for m in models
             if m["composite_ability"] is not None and m["valid_metrics"] >= MIN_VALID_METRICS]
    print(f"Models with ≥{MIN_VALID_METRICS} metrics: {len(valid)}")

    # ── Per-request cost ──
    for m in valid:
        m["input_output_ratio"] = None
        m["total_output_tokens"] = None
        m["input_tokens"] = None
        m["per_request_cost"] = None
        m["cost_method"] = None

        # Step 1: Input/output ratio from prices
        if (m["input_price"] is not None and m["output_price"] is not None
                and m["input_price"] != m["output_price"] and m["input_price"] > 0 and m["output_price"] > 0):
            r = (m["blended_price"] - m["output_price"]) / (m["input_price"] - m["output_price"])
            r = max(MIN_INPUT_OUTPUT_RATIO, min(MAX_INPUT_OUTPUT_RATIO, r))
            m["input_output_ratio"] = round(r, 4)

        # Step 2: Calculate output tokens based on model type
        has_speed = m["speed"] is not None and m["speed"] > 0
        has_total = m["total_response"] is not None and m["total_response"] > 0
        has_ttft = m["ttft"] is not None and m["ttft"] > 0
        has_rtime = m["reasoning_time"] is not None and m["reasoning_time"] > 0

        if not (has_speed and has_total):
            continue  # Can't compute without speed and total time

        if not m["is_reasoning"]:
            # ── Case A: Non-reasoning model ──
            if has_ttft:
                output_time = m["total_response"] - m["ttft"]
                if output_time <= 0:
                    output_time = m["total_response"]
                m["total_output_tokens"] = round(output_time * m["speed"], 1)
                m["cost_method"] = "non-reasoning"
            else:
                m["total_output_tokens"] = round(m["total_response"] * m["speed"], 1)
                m["cost_method"] = "non-reasoning-no-ttft"

        elif has_rtime:
            # ── Case B: Reasoning model WITH Reasoning_Time ──
            # (Total - TTFT) already includes reasoning + visible output, NOT additive
            if has_ttft:
                output_time = m["total_response"] - m["ttft"]
                if output_time <= 0:
                    output_time = m["total_response"]
                m["total_output_tokens"] = round(output_time * m["speed"], 1)
            else:
                m["total_output_tokens"] = round(m["total_response"] * m["speed"], 1)
            m["cost_method"] = "reasoning-with-time"

        else:
            # ── Case C: Reasoning model WITHOUT Reasoning_Time ──
            # CoT not visible → first chunk meaningless → all time generates tokens
            m["total_output_tokens"] = round(m["total_response"] * m["speed"], 1)
            m["cost_method"] = "reasoning-no-time"

        # Step 3: Input tokens from ratio
        if m["input_output_ratio"] is not None and m["input_output_ratio"] < 1:
            if m["total_output_tokens"] is not None and m["total_output_tokens"] > 0:
                m["input_tokens"] = round(
                    m["total_output_tokens"] * m["input_output_ratio"] / (1 - m["input_output_ratio"]), 1
                )

        # Step 4: Per-request cost
        if (m["input_tokens"] is not None and m["total_output_tokens"] is not None
                and m["input_price"] is not None and m["output_price"] is not None):
            cost = (m["input_tokens"] * m["input_price"]
                    + m["total_output_tokens"] * m["output_price"]) / 1_000_000
            m["per_request_cost"] = round(cost, 6)

    # ── Normalize per-request cost ──
    priced = [m for m in valid if m.get("per_request_cost") is not None]
    if priced:
        costs = [m["per_request_cost"] for m in priced]
        min_c, max_c = min(costs), max(costs)
        print(f"Per-request cost range: ${min_c:.4f} – ${max_c:.4f}")
        for m in priced:
            m["normalized_cost"] = 0.5 if max_c == min_c else (m["per_request_cost"] - min_c) / (max_c - min_c)
    # Models without per_request_cost get no normalized_cost
    for m in valid:
        if "normalized_cost" not in m:
            m["normalized_cost"] = None

    return valid, metric_ranges


def compute_pareto(models):
    """Pareto frontier based on per-request cost (X) vs composite ability (Y).
    Only models with a valid per_request_cost are considered."""
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
    """a dominates b if a is cheaper AND at least as capable, or more capable AND at most as expensive."""
    return (a["composite_ability"] >= b["composite_ability"]
            and a["per_request_cost"] <= b["per_request_cost"]
            and (a["composite_ability"] > b["composite_ability"] or a["per_request_cost"] < b["per_request_cost"]))


# ── Visualization ──
def plot_analysis(models, pareto):
    try:
        from adjustText import adjust_text
        has_adj = True
    except ImportError:
        has_adj = False

    # Only plot models with per_request_cost
    plot_models = [m for m in models if m.get("per_request_cost") is not None]
    pareto_names = {m["model"] for m in pareto}
    others = [m for m in plot_models if m["model"] not in pareto_names]

    fig, ax = plt.subplots(figsize=(18, 13))
    fig.patch.set_facecolor("#FAFBFC")
    ax.set_facecolor("#FAFBFC")

    ax.scatter(
        [m["normalized_cost"] for m in others],
        [m["composite_ability"] for m in others],
        c="#CBD5E1", s=28, alpha=0.5, zorder=2,
        label=f"其他模型 ({len(others)})",
    )

    ax.scatter(
        [m["normalized_cost"] for m in pareto],
        [m["composite_ability"] for m in pareto],
        c="#4C6EF5", s=90, alpha=0.9, zorder=4,
        edgecolors="#364FC7", linewidth=1.5,
        label=f"Pareto前沿 ({len(pareto)})",
    )

    pf = sorted(pareto, key=lambda m: m["normalized_cost"])
    ax.plot(
        [m["normalized_cost"] for m in pf],
        [m["composite_ability"] for m in pf],
        c="#4C6EF5", linewidth=1.8, alpha=0.35, zorder=3, linestyle="--",
    )

    texts = []
    for i, m in enumerate(pf):
        label = f"{i+1}. {m['model']}"
        t = ax.text(
            m["normalized_cost"], m["composite_ability"], label,
            fontsize=8.5, ha="left", va="bottom", color="#1E3A5F",
            fontweight="bold", zorder=5,
            bbox=dict(boxstyle="round,pad=0.12", facecolor="white", alpha=0.7,
                      edgecolor="#90CAF9", linewidth=0.5),
        )
        texts.append(t)

    if has_adj:
        adjust_text(texts, arrowprops=dict(arrowstyle="->", color="#90A4AE", lw=0.6),
                    expand_points=(1.8, 1.8), force_text=(0.3, 0.5),
                    force_points=(0.1, 0.1), lim=200)

    ax.set_xlabel("归一化单次价格 (0=最便宜, 1=最贵)", fontsize=14, color="#37474F", labelpad=12)
    ax.set_ylabel("综合能力值 (0=最低, 1=最高)", fontsize=14, color="#37474F", labelpad=12)
    ax.set_title(
        "LLM 综合能力 vs 单次请求价格 — Pareto前沿\n"
        "基于 Artificial Analysis Intelligence 15项子指标线性归一化",
        fontsize=15, color="#263238", fontweight="bold", pad=18,
    )
    ax.set_xlim(-0.03, 1.05)
    ax.set_ylim(-0.03, 1.05)
    ax.grid(True, alpha=0.12, color="#90A4AE")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#B0BEC5")
    ax.spines["bottom"].set_color("#B0BEC5")
    ax.legend(loc="upper left", fontsize=10.5, framealpha=0.9, edgecolor="#CFD8DC")

    method = (f"15项Intelligence指标线性归一化→均值=综合能力 | Pareto前沿{len(pareto)} | 共{len(plot_models)}模型\n"
              f"单次价格: 非推理/推理有ReasonT=(Total-TTFT)×Speed; "
              f"推理无ReasonT=Total×Speed (CoT不可见,first chunk无意义)")
    ax.text(0.98, 0.02, method, transform=ax.transAxes, fontsize=6.5,
            va="bottom", ha="right", color="#546E7A", style="italic",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#ECEFF1", alpha=0.8,
                      edgecolor="#B0BEC5", linewidth=0.5))

    plt.tight_layout()
    out = os.path.join(OUTPUT_DIR, "pareto_analysis.png")
    plt.savefig(out, dpi=200, bbox_inches="tight", facecolor="#FAFBFC")
    plt.close()
    print(f"Plot saved to {out}")


# ── Output ──
def save_results(models, pareto, metric_ranges):
    # JSON
    output = {
        "metadata": {
            "source": "https://artificialanalysis.ai/leaderboards/models",
            "methodology": "15 Intelligence metrics normalized [0,1], averaged; Pareto = non-dominated by per-request cost",
            "per_request_cost": {
                "non_reasoning": "Output_tokens = (Total - TTFT) × Speed; Cost = (In × InPrice + Out × OutPrice) / 1M",
                "reasoning_with_time": "Output_tokens = (Total - TTFT) × Speed (reasoning already included, NOT additive); Cost = (In × InPrice + Out × OutPrice) / 1M",
                "reasoning_no_time": "Output_tokens = Total × Speed (CoT not visible, first chunk meaningless); Cost = (In × InPrice + Out × OutPrice) / 1M",
            },
            "total_models": len(models),
            "pareto_count": len(pareto),
        },
        "metric_ranges": {METRIC_LABELS[k]: v for k, v in metric_ranges.items() if v is not None},
        "pareto_frontier": [_export_model(m, i + 1) for i, m in enumerate(pareto)],
        "all_models": [
            {
                "model": m["model"],
                "composite_ability": round(m["composite_ability"], 4),
                "per_request_cost": m.get("per_request_cost"),
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
        "composite_ability": round(m["composite_ability"], 4),
        "per_request_cost_usd": m.get("per_request_cost"),
        "input_output_ratio": m.get("input_output_ratio"),
        "speed": m["speed"],
        "ttft": m["ttft"],
        "total_response": m["total_response"],
        "reasoning_time": m["reasoning_time"],
        "total_output_tokens": m.get("total_output_tokens"),
        "input_tokens": m.get("input_tokens"),
        "cost_method": m.get("cost_method"),
        "valid_metrics": m["valid_metrics"],
    }


def generate_readme(pareto, models):
    lines = []
    lines.append("# LLM Leaderboard Pareto Analysis\n")
    lines.append("![Pareto Analysis](output/pareto_analysis.png)\n")
    lines.append("## Pareto 前沿模型（综合能力从高到低）\n")
    lines.append("| # | 模型 | 综合能力 | 单次价格 (USD) | 推理 |")
    lines.append("|---|------|---------|---------------|------|")

    for i, m in enumerate(pareto):
        prc = m.get("per_request_cost")
        prc_str = f"${prc:.4f}" if prc is not None else "--"
        reas = "🧠" if m["is_reasoning"] else "—"
        lines.append(
            f"| {i+1} | {m['model']} | {m['composite_ability']:.4f} "
            f"| {prc_str} | {reas} |"
        )

    lines.append("")
    lines.append("### 评分方法")
    lines.append("")
    lines.append("1. **15项Intelligence子指标**各自线性归一化到 [0,1]（最低→0，最高→1，\"--\"忽略）")
    lines.append("2. **综合能力值** = 所有有效归一化分数的算术平均")
    lines.append("3. **Pareto前沿** = 不被任何其他模型支配的模型（不存在单次更便宜且更强的选择）")
    lines.append("")
    lines.append("### 单次请求价格计算")
    lines.append("")
    lines.append("```")
    lines.append("输入输出比 r = (Blended - Output_Price) / (Input_Price - Output_Price)")
    lines.append("")
    lines.append("# 非推理模型 & 推理模型（有 Reasoning Time）：")
    lines.append("输出tokens = (Total_Response - TTFT) × Speed")
    lines.append("# 对推理模型：TTFT=首CoT token时间，(Total-TTFT)已含reasoning+可见输出，不加倍")
    lines.append("")
    lines.append("# 推理模型（无 Reasoning Time）：")
    lines.append("输出tokens = Total_Response × Speed")
    lines.append("# CoT不可见→first chunk无意义，假设全程都在生成token")
    lines.append("")
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


# ── Main ──
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    if not os.path.exists(RAW_DATA_FILE):
        print(f"ERROR: {RAW_DATA_FILE} not found. Run scrape.py first.")
        sys.exit(1)

    print("Loading data...")
    data = load_data()
    print(f"  {len(data)} models loaded")

    print("\nComputing scores & per-request costs...")
    models, metric_ranges = compute_scores(data)

    # Stats
    with_prc = [m for m in models if m.get("per_request_cost") is not None]
    if with_prc:
        costs = [m["per_request_cost"] for m in with_prc]
        print(f"  Per-request cost: {len(with_prc)}/{len(models)} models computable")
        print(f"  Range: ${min(costs):.4f} – ${max(costs):.4f}")

    # Cost method breakdown
    methods = Counter(m.get("cost_method") for m in models if m.get("cost_method"))
    print(f"  Cost methods: {dict(methods)}")

    print("\nComputing Pareto frontier (based on per-request cost)...")
    pareto = compute_pareto(models)
    print(f"  Pareto frontier: {len(pareto)} models")

    print("\nGenerating visualization...")
    plot_analysis(models, pareto)

    print("\nSaving results...")
    save_results(models, pareto, metric_ranges)

    # Print Pareto table
    print(f"\n{'='*100}")
    print(f"PARETO FRONTIER ({len(pareto)} models) — ranked by composite ability")
    print(f"{'='*100}")
    print(f"{'#':<3} {'Model':<38} {'Ability':>8} {'PerReq$':>10} {'Reas?':>6} {'Method':<22}")
    print(f"{'-'*3} {'-'*38} {'-'*8} {'-'*10} {'-'*6} {'-'*22}")
    for i, m in enumerate(pareto):
        prc = f"${m['per_request_cost']:.4f}" if m.get("per_request_cost") else "--"
        reas = "Y" if m["is_reasoning"] else "N"
        method = (m.get("cost_method") or "—")[:22]
        print(f"{i+1:<3} {m['model']:<38} {m['composite_ability']:>8.4f} {prc:>10} {reas:>6} {method:<22}")

    print("\n✅ Analysis complete!")


if __name__ == "__main__":
    main()
