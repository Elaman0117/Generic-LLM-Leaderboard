#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Monotone Benchmark Calibration & Multi-Round Mapping Engine
===========================================================

Learns strictly monotonic per-benchmark calibration curves ``g_b: [0, 1] -> R``,
regularized benchmark weights ``w_b in [w_min, w_max]``, and Pseudo-Huber IRLS
robust aggregation to estimate composite model ability purely from a model's
38 raw benchmark scores.

Design Principles (ZERO LABEL LEAKAGE):
1. ``score_model(parsed_metrics)`` depends ONLY on the model's benchmark values
   and stored calibration parameters (``metric_ranges``, ``curves``, ``weights``,
   ``aggregation``, ``score_offset``, ``score_scale``). It never accesses model
   name, vendor, tier, version, release date, thinking tag, or hierarchy labels.
2. Every benchmark curve ``g_b`` is piecewise linear on adaptive quantile knots
   with every segment slope constrained to ``s_{b,r} >= eps_min > 0``, guaranteeing
   strict monotonicity (``x1 > x2 => g_b(x1) > g_b(x2)``).
3. Pseudo-Huber IRLS aggregation with a positive quadratic tail ``alpha_tail > 0``
   solves a strictly convex M-estimation objective whose unique minimizer is
   strictly increasing in every observed benchmark score while downweighting
   isolated noisy/anomalous benchmark evaluations on a model.
4. Multi-round optimization progression (Rounds 0 -> 1 -> 2 -> 3 -> 4+) and
   Leave-One-Vendor-Out (LOVO) cross-validation are logged transparently.
5. Pure Python standard library only (no NumPy/Matplotlib/SciPy required).
"""

import argparse
import json
import math
import os
import sys
import time
from typing import Dict, List, Optional, Sequence, Tuple

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
RAW_DATA_FILE = os.path.join(OUTPUT_DIR, "raw_data.json")
DEFAULT_MODEL_PATH = os.path.join(OUTPUT_DIR, "mapping_model.json")

DEFAULT_LOVO_VENDORS = [
    "OpenAI",
    "Google",
    "Anthropic",
    "Alibaba",
    "DeepSeek",
    "Meta",
    "SpaceXAI",
    "Z AI",
]

FLAGSHIP_ORDERING_CHAINS = [
    ["GPT-6.2 Astra (max)", "GPT-6 Astra (max)", "GPT-6 Astra (xhigh)", "GPT-6 Astra (high)", "GPT-6 Astra (medium)"],
    ["GPT-6.2 Sol (max)", "GPT-6.1 Sol (max)", "GPT-6 Sol (max)", "GPT-5.6 Sol (max)"],
    ["GPT-6.2 Astra (max)", "GPT-6.2 Sol (max)"],
    ["Gemini 4 Neon (xhigh)", "Gemini 4 Neon (high)", "Gemini 4 Neon (medium)"],
    ["Gemini 4 Carbon (high)", "Gemini 4 Carbon (medium)", "Gemini 4 Carbon (low)"],
    ["Gemini 4 Carbon (high)", "Gemini 4 Argon (high)"],
    ["Claude Fable 5.2 (max)", "Claude Fable 5.1 (max)", "Claude Fable 5"],
    ["Claude Opus 5.5 (max)", "Claude Opus 5.5 (xhigh)", "Claude Opus 5.5 (high)", "Claude Opus 5.5 (medium)"],
    ["Grok 4.3 (high)", "Grok 4.3 (medium)"],
    ["MiniMax-M2.7", "MiniMax-M2.5"],
]


# ══════════════════════════════════════════════════════════════════════
# Pure-Math Helpers (Zero Model Identity / Zero External Dependencies)
# ══════════════════════════════════════════════════════════════════════

def _to_float(val) -> Optional[float]:
    """Convert numeric/Fraction value to finite float, or None."""
    if val is None or isinstance(val, bool):
        return None
    try:
        f = float(val)
    except (TypeError, ValueError):
        return None
    if math.isnan(f) or math.isinf(f):
        return None
    return f


def _get_model_name(m: dict) -> str:
    """Extract display/key name across hierarchy.py and analyze.py schemas."""
    return str(m.get("name") or m.get("model") or m.get("full_name") or "")


def _get_parsed_metrics(m: dict) -> dict:
    """Extract raw parsed benchmark mapping across hierarchy.py and analyze.py schemas."""
    if "parsed" in m and isinstance(m["parsed"], dict):
        return m["parsed"]
    if "_parsed" in m and isinstance(m["_parsed"], dict):
        return m["_parsed"]
    return {}


def _normalize_vendor(name: str) -> str:
    """Normalize vendor string for LOVO grouping (e.g. 'Z AI' == 'Z_AI')."""
    return str(name or "").strip().lower().replace("_", " ")


def _canonical_rule_key(reason: str) -> str:
    """Map constraint reason string to canonical Rule 1/2/3/4 bucket key."""
    r = (reason or "").strip()
    low = r.lower()
    if low.startswith("rule 1") or "rule1" in low:
        return "rule1_tier"
    if low.startswith("rule 2") or "rule2" in low:
        return "rule2_version"
    if low.startswith("rule 3") or "rule3" in low:
        return "rule3_thinking"
    if low.startswith("rule 4") or "rule4" in low:
        return "rule4_date"
    return r.split(":")[0].strip() if ":" in r else (r or "other")


def _sanitize_metric_ranges(
    models: List[dict],
    metric_keys: Sequence[str],
    metric_ranges: Optional[Dict[str, Optional[dict]]],
) -> Dict[str, Optional[dict]]:
    """Convert metric_ranges to pure finite-float dicts, inferring missing ones if needed."""
    clean: Dict[str, Optional[dict]] = {}
    mr = metric_ranges or {}
    for k in metric_keys:
        rng = mr.get(k)
        if isinstance(rng, dict) and rng.get("count", 0) > 0:
            lo = _to_float(rng.get("min"))
            hi = _to_float(rng.get("max"))
            cnt = int(rng.get("count", 0))
            if lo is not None and hi is not None:
                clean[k] = {"min": lo, "max": hi, "count": cnt}
                continue
        vals = []
        for m in models:
            v = _to_float(_get_parsed_metrics(m).get(k))
            if v is not None:
                vals.append(v)
        if vals:
            clean[k] = {"min": min(vals), "max": max(vals), "count": len(vals)}
        else:
            clean[k] = None
    return clean


def _normalize_raw_value(val: Optional[float], rng: Optional[dict]) -> Optional[float]:
    """Map a single raw benchmark score to normalized [0, 1] scale using stored range."""
    v = _to_float(val)
    if v is None or rng is None or rng.get("count", 0) <= 0:
        return None
    lo = rng["min"]
    hi = rng["max"]
    if hi <= lo:
        return 0.5
    return (v - lo) / (hi - lo)


def build_adaptive_knots(xs: Sequence[float], dt_min: float = 0.03) -> List[float]:
    """Build strictly increasing adaptive quantile knots on [0, 1].

    K_b = 1 if N_b < 40, K_b = 3 if 40 <= N_b < 120, K_b = 6 if N_b >= 120.
    Guarantees every sub-interval width t_{r} - t_{r-1} >= dt_min.
    """
    n = len(xs)
    if n < 40:
        return [0.0, 1.0]
    k_segs = 3 if n < 120 else 6
    s = sorted(xs)
    knots = [0.0]
    for r in range(1, k_segs):
        pos = r * (n - 1) / k_segs
        lo = int(math.floor(pos))
        hi = min(n - 1, lo + 1)
        frac = pos - lo
        knots.append(s[lo] * (1.0 - frac) + s[hi] * frac)
    knots.append(1.0)

    dts = [max(0.0, knots[r] - knots[r - 1]) for r in range(1, k_segs + 1)]
    min_gap = min(dt_min, 0.5 / k_segs)
    for _ in range(25):
        fixed = [r for r in range(k_segs) if dts[r] < min_gap]
        if not fixed:
            break
        rem = 1.0 - len(fixed) * min_gap
        free_sum = sum(dts[r] for r in range(k_segs) if r not in fixed)
        for r in range(k_segs):
            if r in fixed:
                dts[r] = min_gap
            elif free_sum > 0.0:
                dts[r] = dts[r] * (rem / free_sum)
            else:
                dts[r] = rem / max(1, k_segs - len(fixed))

    out = [0.0]
    for dt in dts[:-1]:
        out.append(out[-1] + dt)
    out.append(1.0)
    return out


def spline_basis(x: float, knots: Sequence[float]) -> Tuple[float, ...]:
    """Evaluate piecewise-linear slope basis phi(x) so g(x) = c0 + sum_r phi_r(x) * s_r.

    Supports linear extrapolation outside [0, 1] using boundary slopes s_1 and s_K,
    preserving strict monotonicity everywhere on R.
    """
    k_segs = len(knots) - 1
    phi = [0.0] * k_segs
    for r in range(k_segs):
        t0 = knots[r]
        t1 = knots[r + 1]
        if r == 0 and x < t0:
            phi[r] = x - t0
        elif r == k_segs - 1 and x > t1:
            phi[r] = x - t0
        elif x <= t0:
            phi[r] = 0.0
        elif x >= t1:
            phi[r] = t1 - t0
        else:
            phi[r] = x - t0
    return tuple(phi)


def eval_piecewise_linear(x: float, knots: Sequence[float], c0: float, slopes: Sequence[float]) -> float:
    """Evaluate strictly monotone piecewise-linear curve g_b(x) directly."""
    k_segs = len(slopes)
    if k_segs == 0:
        return c0
    if x <= knots[0]:
        return c0 + slopes[0] * (x - knots[0])
    y = c0
    for r in range(k_segs):
        t0 = knots[r]
        t1 = knots[r + 1]
        if x <= t1 or r == k_segs - 1:
            return y + slopes[r] * (x - t0)
        y += slopes[r] * (t1 - t0)
    return y


def compute_knot_values(knots: Sequence[float], c0: float, slopes: Sequence[float]) -> Tuple[List[float], List[float]]:
    """Compute knot y-values and positive knot increments Delta_{b,r} = s_{b,r} * dt_r."""
    vals = [float(c0)]
    deltas = []
    for r, slope in enumerate(slopes):
        delta = float(slope) * (float(knots[r + 1]) - float(knots[r]))
        deltas.append(delta)
        vals.append(vals[-1] + delta)
    return vals, deltas


def fit_monotone_spline_qp(
    phis: Sequence[Tuple[float, ...]],
    thetas: Sequence[float],
    num_segs: int,
    lam_smooth: float = 0.05,
    eps_min: float = 0.05,
    s_max: float = 5.0,
    lam_prior: float = 1e-3,
) -> Tuple[float, List[float], float]:
    """Solve convex box-constrained spline QP for one benchmark via coordinate descent.

    Minimizes:
      sum_i (c0 + phi_i . s - theta_i)^2
      + lam_smooth * N_eff * sum_{r=1}^{K-1} (s_{r+1} - s_r)^2
      + lam_prior  * N_eff * sum_{r=1}^K (s_r - 1)^2
    subject to eps_min <= s_r <= s_max for all r.
    """
    n = len(phis)
    if n == 0:
        return 0.0, [1.0] * num_segs, 0.0

    n_eff = float(max(n, 20))
    ls = lam_smooth * n_eff
    lp = lam_prior * n_eff
    dim = num_segs + 1
    hess = [[0.0] * dim for _ in range(dim)]
    rhs = [0.0] * dim

    for i in range(n):
        row = [1.0] + list(phis[i])
        th = thetas[i]
        for a in range(dim):
            rhs[a] += row[a] * th
            ra = row[a]
            ha = hess[a]
            for c in range(dim):
                ha[c] += ra * row[c]

    for r in range(1, num_segs):
        hess[r][r] += ls
        hess[r + 1][r + 1] += ls
        hess[r][r + 1] -= ls
        hess[r + 1][r] -= ls

    for r in range(1, dim):
        hess[r][r] += lp
        rhs[r] += lp * 1.0

    params = [0.0] + [1.0] * num_segs
    params[0] = (sum(thetas) / n) - (sum(sum(p) for p in phis) / n)

    for _ in range(80):
        max_chg = 0.0
        for j in range(dim):
            hj = hess[j]
            off = sum(hj[c] * params[c] for c in range(dim) if c != j)
            new_val = (rhs[j] - off) / hj[j] if hj[j] > 0.0 else params[j]
            if j >= 1:
                if new_val < eps_min:
                    new_val = eps_min
                elif new_val > s_max:
                    new_val = s_max
            chg = abs(new_val - params[j])
            if chg > max_chg:
                max_chg = chg
            params[j] = new_val
        if max_chg < 1e-10:
            break

    c0 = params[0]
    slopes = params[1:]
    sq_err = 0.0
    for i in range(n):
        phi = phis[i]
        pred = c0 + sum(phi[r] * slopes[r] for r in range(num_segs))
        err = pred - thetas[i]
        sq_err += err * err
    return c0, slopes, sq_err / n


def project_bounded_simplex(
    values: Sequence[float],
    w_min: float,
    w_max: float,
    target_sum: Optional[float] = None,
) -> List[float]:
    """Exact Euclidean projection onto {w_min <= w_b <= w_max, sum_b w_b = target_sum}."""
    n = len(values)
    if n == 0:
        return []
    target = float(n) if target_sum is None else float(target_sum)
    target = max(n * w_min, min(n * w_max, target))
    lo = min(x - w_max for x in values) - 1.0
    hi = max(x - w_min for x in values) + 1.0
    for _ in range(50):
        mid = 0.5 * (lo + hi)
        s = sum(max(w_min, min(w_max, x - mid)) for x in values)
        if s > target:
            lo = mid
        else:
            hi = mid
    mid = 0.5 * (lo + hi)
    return [max(w_min, min(w_max, x - mid)) for x in values]


def aggregate_pseudo_huber_irls(
    zs: Sequence[float],
    ws: Sequence[float],
    delta_huber: float = 0.08,
    alpha_tail: float = 0.05,
    max_iters: int = 20,
    tol: float = 1e-10,
    init_s: Optional[float] = None,
) -> float:
    """Compute unique strictly-monotone Pseudo-Huber IRLS M-estimate of model ability."""
    n = len(zs)
    if n == 0:
        raise ValueError("Cannot aggregate empty score list")
    if n == 1:
        return float(zs[0])

    if init_s is None:
        num = 0.0
        den = 0.0
        for j in range(n):
            num += ws[j] * zs[j]
            den += ws[j]
        s = num / den if den > 0.0 else (sum(zs) / n)
    else:
        s = init_s

    inv_d2 = 1.0 / (delta_huber * delta_huber)
    for _ in range(max_iters):
        num_h = 0.0
        den_h = 0.0
        for j in range(n):
            r = s - zs[j]
            u = 1.0 / math.sqrt(1.0 + r * r * inv_d2) + alpha_tail
            wu = ws[j] * u
            num_h += wu * zs[j]
            den_h += wu
        if den_h <= 0.0:
            break
        s_new = num_h / den_h
        if abs(s_new - s) <= tol:
            return s_new
        s = s_new
    return s


def compute_loo_linear_scores(
    x_mat: List[List[Optional[float]]],
    max_rounds: int = 30,
    tol: float = 1e-4,
) -> Tuple[List[float], List[float], List[Tuple[float, float]]]:
    """Compute Round 0a raw min-max mean and Round 0b LOO linear calibrated scores."""
    n_models = len(x_mat)
    n_bench = len(x_mat[0]) if n_models else 0

    raw_means = []
    for m_idx in range(n_models):
        vals = [x for x in x_mat[m_idx] if x is not None]
        raw_means.append(sum(vals) / len(vals) if vals else 0.5)

    bounds = [(0.0, 1.0) for _ in range(n_bench)]
    for _ in range(max_rounds):
        norm_scores = [[None] * n_bench for _ in range(n_models)]
        for m_idx in range(n_models):
            row = x_mat[m_idx]
            out_row = norm_scores[m_idx]
            for b_idx in range(n_bench):
                x = row[b_idx]
                if x is not None:
                    lo, hi = bounds[b_idx]
                    out_row[b_idx] = lo + x * (hi - lo)

        new_bounds = []
        max_delta = 0.0
        for excl in range(n_bench):
            loo_avgs = {}
            for m_idx in range(n_models):
                row = norm_scores[m_idx]
                s_vals = [row[b] for b in range(n_bench) if b != excl and row[b] is not None]
                if s_vals:
                    loo_avgs[m_idx] = sum(s_vals) / len(s_vals)
            if not loo_avgs:
                new_bounds.append(bounds[excl])
                continue
            mn_a = min(loo_avgs.values())
            mx_a = max(loo_avgs.values())
            if mx_a > mn_a:
                inv_span = 1.0 / (mx_a - mn_a)
                norm_loo = {m_idx: (avg - mn_a) * inv_span for m_idx, avg in loo_avgs.items()}
            else:
                norm_loo = {m_idx: 0.5 for m_idx in loo_avgs}
            tested = [norm_loo[m_idx] for m_idx in norm_loo if x_mat[m_idx][excl] is not None]
            if tested:
                n_lo, n_hi = min(tested), max(tested)
            else:
                n_lo, n_hi = bounds[excl]
            max_delta = max(max_delta, abs(n_lo - bounds[excl][0]), abs(n_hi - bounds[excl][1]))
            new_bounds.append((n_lo, n_hi))
        bounds = new_bounds
        if max_delta < tol:
            break

    loo_means = []
    for m_idx in range(n_models):
        vals = []
        row = x_mat[m_idx]
        for b_idx in range(n_bench):
            x = row[b_idx]
            if x is not None:
                lo, hi = bounds[b_idx]
                vals.append(lo + x * (hi - lo))
        loo_means.append(sum(vals) / len(vals) if vals else 0.5)

    return raw_means, loo_means, bounds


def evaluate_constraints(
    score_map: Dict[str, float],
    constraints: Sequence[Tuple],
    top_k: int = 30,
) -> dict:
    """Evaluate overall and per-Rule 1/2/3/4 concordance plus top worst violations."""
    rule_buckets = {
        "rule1_tier": [0, 0],
        "rule2_version": [0, 0],
        "rule3_thinking": [0, 0],
        "rule4_date": [0, 0],
    }
    total_eval = 0
    satisfied = 0
    violations = []

    for c in constraints or ():
        if len(c) < 2:
            continue
        u_name = c[0]
        v_name = c[1]
        reason = c[2] if len(c) >= 3 else "constraint"
        if u_name == v_name:
            continue
        su = score_map.get(u_name)
        sv = score_map.get(v_name)
        if su is None or sv is None:
            continue

        total_eval += 1
        r_key = _canonical_rule_key(reason)
        if r_key not in rule_buckets:
            rule_buckets[r_key] = [0, 0]
        rule_buckets[r_key][1] += 1

        if su >= sv:
            satisfied += 1
            rule_buckets[r_key][0] += 1
        else:
            violations.append({
                "higher_model": u_name,
                "lower_model": v_name,
                "score_higher": float(su),
                "score_lower": float(sv),
                "diff": float(su - sv),
                "rule": r_key,
                "reason": str(reason),
            })

    violations.sort(key=lambda item: item["diff"])
    concordance = (satisfied / total_eval) if total_eval > 0 else 1.0
    by_rule = {}
    for rk, (ok_cnt, tot_cnt) in rule_buckets.items():
        if tot_cnt > 0 or rk in ("rule1_tier", "rule2_version", "rule3_thinking", "rule4_date"):
            by_rule[rk] = {
                "total": tot_cnt,
                "satisfied": ok_cnt,
                "violations": tot_cnt - ok_cnt,
                "concordance": (ok_cnt / tot_cnt) if tot_cnt > 0 else 1.0,
                "concordance_pct": (100.0 * ok_cnt / tot_cnt) if tot_cnt > 0 else 100.0,
            }

    return {
        "total_input_constraints": len(constraints) if constraints else 0,
        "total_constraints": total_eval,
        "satisfied": satisfied,
        "violations_count": total_eval - satisfied,
        "concordance": concordance,
        "concordance_pct": 100.0 * concordance,
        "by_rule": by_rule,
        "top_violations": violations[:top_k],
    }


def _evaluate_flagship_chains(score_map: Dict[str, float]) -> List[dict]:
    """Diagnostic check of key flagship ordering chains (metadata only)."""
    results = []
    for chain in FLAGSHIP_ORDERING_CHAINS:
        present = [(nm, score_map[nm]) for nm in chain if nm in score_map]
        ok = True
        inversions = []
        for i in range(len(present) - 1):
            u_nm, u_sc = present[i]
            v_nm, v_sc = present[i + 1]
            if u_sc < v_sc:
                ok = False
                inversions.append(f"{u_nm} ({u_sc:.4f}) < {v_nm} ({v_sc:.4f})")
        results.append({
            "chain": chain,
            "present_count": len(present),
            "scores": [{"model": nm, "score": float(sc)} for nm, sc in present],
            "passed": ok and len(present) == len(chain),
            "inversions": inversions,
        })
    return results


# ══════════════════════════════════════════════════════════════════════
# Main MonotoneBenchmarkMapper Class
# ══════════════════════════════════════════════════════════════════════

class MonotoneBenchmarkMapper:
    """Strictly monotone, zero-leakage multi-round benchmark calibration & mapping model."""

    def __init__(
        self,
        eps_min: float = 0.05,
        s_max: float = 5.0,
        w_min: float = 0.10,
        w_max: float = 3.2,
        lam_smooth_stage1: float = 0.05,
        lam_w: float = 1e-4,
        lam_align: float = 0.15,
        lam_smooth: float = 3e-4,
        lam_curve_prior: float = 0.0,
        align_mix: float = 0.0,
        delta_huber: float = 0.08,
        alpha_tail: float = 0.05,
        rule_balance_power: float = 0.5,
        irls_iters: int = 20,
        irls_tol: float = 1e-10,
    ):
        self.eps_min = float(eps_min)
        self.s_max = float(s_max)
        self.w_min = float(w_min)
        self.w_max = float(w_max)
        self.lam_smooth_stage1 = float(lam_smooth_stage1)
        self.lam_w = float(lam_w)
        self.lam_align = float(lam_align)
        self.lam_smooth = float(lam_smooth)
        self.lam_curve_prior = float(lam_curve_prior)
        self.align_mix = float(align_mix)
        self.delta_huber = float(delta_huber)
        self.alpha_tail = float(alpha_tail)
        self.rule_balance_power = float(rule_balance_power)
        self.irls_iters = int(irls_iters)
        self.irls_tol = float(irls_tol)

        # Learned inference parameters (purely per-benchmark math, zero model identity)
        self.metric_keys: List[str] = []
        self.metric_ranges: Dict[str, Optional[dict]] = {}
        self.curves: Dict[str, dict] = {}
        self.weights: Dict[str, float] = {}
        self.aggregation: dict = {
            "mode": "pseudo_huber_irls",
            "delta_huber": self.delta_huber,
            "alpha_tail": self.alpha_tail,
            "irls_iters": self.irls_iters,
            "irls_tol": self.irls_tol,
        }
        self.score_offset: float = 0.0
        self.score_scale: float = 1.0
        self.is_fitted: bool = False

        # Training diagnostics (stored for reporting/serialization only; never read in score_model)
        self.diagnostics: dict = {}

    def _clone_hparams(self) -> "MonotoneBenchmarkMapper":
        return MonotoneBenchmarkMapper(
            eps_min=self.eps_min,
            s_max=self.s_max,
            w_min=self.w_min,
            w_max=self.w_max,
            lam_smooth_stage1=self.lam_smooth_stage1,
            lam_w=self.lam_w,
            lam_align=self.lam_align,
            lam_smooth=self.lam_smooth,
            lam_curve_prior=self.lam_curve_prior,
            align_mix=self.align_mix,
            delta_huber=self.delta_huber,
            alpha_tail=self.alpha_tail,
            rule_balance_power=self.rule_balance_power,
            irls_iters=self.irls_iters,
            irls_tol=self.irls_tol,
        )

    def _prepare_training_tensors(
        self,
        models: List[dict],
        metric_keys: Sequence[str],
        metric_ranges: Optional[Dict[str, Optional[dict]]],
    ):
        keys = list(metric_keys)
        clean_ranges = _sanitize_metric_ranges(models, keys, metric_ranges)
        n_models = len(models)
        n_bench = len(keys)

        x_mat: List[List[Optional[float]]] = [[None] * n_bench for _ in range(n_models)]
        for m_idx, m in enumerate(models):
            parsed = _get_parsed_metrics(m)
            row = x_mat[m_idx]
            for b_idx, k in enumerate(keys):
                row[b_idx] = _normalize_raw_value(parsed.get(k), clean_ranges.get(k))

        knots_list: List[List[float]] = []
        obs_by_bench: List[List[Tuple[int, Tuple[float, ...]]]] = [[] for _ in range(n_bench)]
        m_b: List[List[int]] = [[] for _ in range(n_models)]
        m_phi: List[List[Tuple[float, ...]]] = [[] for _ in range(n_models)]

        for b_idx in range(n_bench):
            xs = [x_mat[m_idx][b_idx] for m_idx in range(n_models) if x_mat[m_idx][b_idx] is not None]
            kn = build_adaptive_knots(xs)
            knots_list.append(kn)
            for m_idx in range(n_models):
                x = x_mat[m_idx][b_idx]
                if x is not None:
                    phi = spline_basis(x, kn)
                    obs_by_bench[b_idx].append((m_idx, phi))
                    m_b[m_idx].append(b_idx)
                    m_phi[m_idx].append(phi)

        return keys, clean_ranges, x_mat, knots_list, obs_by_bench, m_b, m_phi

    def _run_stage1_unsupervised(
        self,
        x_mat: List[List[Optional[float]]],
        knots_list: List[List[float]],
        obs_by_bench: List[List[Tuple[int, Tuple[float, ...]]]],
        m_b: List[List[int]],
        m_phi: List[List[Tuple[float, ...]]],
        max_rounds: int = 40,
        tol: float = 1e-5,
    ):
        n_models = len(x_mat)
        n_bench = len(knots_list)
        raw_means, loo_means, _ = compute_loo_linear_scores(x_mat)

        mn_0 = min(loo_means) if loo_means else 0.0
        mx_0 = max(loo_means) if loo_means else 1.0
        span_0 = (mx_0 - mn_0) if mx_0 > mn_0 else 1.0
        theta = [(t - mn_0) / span_0 for t in loo_means]

        c0_list = [0.0] * n_bench
        slopes_list = [[1.0] * (len(knots_list[b]) - 1) for b in range(n_bench)]
        w_list = [1.0] * n_bench
        converged_round = max_rounds
        final_delta = 0.0
        history = []

        for rnd in range(1, max_rounds + 1):
            raw_w = []
            for b_idx in range(n_bench):
                obs = obs_by_bench[b_idx]
                if not obs:
                    raw_w.append(1.0)
                    continue
                phis = [p for _, p in obs]
                ths = [theta[m_idx] for m_idx, _ in obs]
                num_segs = len(knots_list[b_idx]) - 1
                c0, sl, mse = fit_monotone_spline_qp(
                    phis,
                    ths,
                    num_segs=num_segs,
                    lam_smooth=self.lam_smooth_stage1,
                    eps_min=self.eps_min,
                    s_max=self.s_max,
                )
                c0_list[b_idx] = c0
                slopes_list[b_idx] = sl
                mean_th = sum(ths) / len(ths)
                var_th = sum((t - mean_th) ** 2 for t in ths) / len(ths)
                nmse = mse / max(var_th, 0.005)
                nmse_shrunk = (len(obs) * nmse + 20.0 * 0.35) / (len(obs) + 20.0)
                raw_w.append(1.0 / (nmse_shrunk + 0.05))

            mean_rw = sum(raw_w) / max(1, n_bench)
            w_list = project_bounded_simplex(
                [rw / mean_rw for rw in raw_w],
                w_min=max(self.w_min, 0.15),
                w_max=min(self.w_max, 3.0),
            )

            th_new = []
            for m_idx in range(n_models):
                bs = m_b[m_idx]
                phis = m_phi[m_idx]
                if not bs:
                    th_new.append(0.5)
                    continue
                num = 0.0
                den = 0.0
                for j, b_idx in enumerate(bs):
                    phi = phis[j]
                    sl = slopes_list[b_idx]
                    z = c0_list[b_idx] + sum(phi[r] * sl[r] for r in range(len(sl)))
                    wb = w_list[b_idx]
                    num += wb * z
                    den += wb
                th_new.append(num / den if den > 0.0 else 0.5)

            mn_n = min(th_new) if th_new else 0.0
            mx_n = max(th_new) if th_new else 1.0
            if mx_n > mn_n:
                inv_s = 1.0 / (mx_n - mn_n)
                th_new = [(t - mn_n) * inv_s for t in th_new]
            else:
                th_new = [0.5] * n_models

            delta = max((abs(th_new[i] - theta[i]) for i in range(n_models)), default=0.0)
            theta = th_new
            final_delta = delta
            history.append({"round": rnd, "max_delta_theta": float(delta)})
            if delta < tol:
                converged_round = rnd
                break

        return raw_means, loo_means, theta, c0_list, slopes_list, w_list, {
            "converged_round": converged_round,
            "converged": final_delta < tol,
            "final_max_delta": float(final_delta),
            "history": history,
        }

    def _build_balanced_edges(
        self,
        models: List[dict],
        constraints: Sequence[Tuple],
    ) -> List[Tuple[int, int, str, float]]:
        name_to_idx: Dict[str, int] = {}
        for idx, m in enumerate(models):
            nm = _get_model_name(m)
            if nm and nm not in name_to_idx:
                name_to_idx[nm] = idx

        raw_pairs = []
        rule_counts: Dict[str, int] = {}
        for c in constraints or ():
            if len(c) < 2:
                continue
            ui = name_to_idx.get(c[0])
            vi = name_to_idx.get(c[1])
            if ui is not None and vi is not None and ui != vi:
                reason = c[2] if len(c) >= 3 else "constraint"
                rk = _canonical_rule_key(reason)
                raw_pairs.append((ui, vi, rk))
                rule_counts[rk] = rule_counts.get(rk, 0) + 1

        if not raw_pairs:
            return []

        rw = {r: 1.0 / (cnt ** self.rule_balance_power) for r, cnt in rule_counts.items()}
        tot_w = sum(rw[r] * cnt for r, cnt in rule_counts.items())
        return [(ui, vi, rk, rw[rk] / tot_w) for ui, vi, rk in raw_pairs]

    def _forward_models(
        self,
        m_b: List[List[int]],
        m_phi: List[List[Tuple[float, ...]]],
        c0s: List[float],
        sls: List[List[float]],
        ws: List[float],
        robust: bool = False,
        init_s: Optional[List[float]] = None,
    ):
        n_models = len(m_b)
        scores = [0.0] * n_models
        zs_all: List[List[float]] = [None] * n_models  # type: ignore
        aux: List[Tuple] = [None] * n_models  # type: ignore
        inv_d2 = 1.0 / (self.delta_huber * self.delta_huber)
        at = self.alpha_tail

        for m_idx in range(n_models):
            bs = m_b[m_idx]
            phis = m_phi[m_idx]
            n_o = len(bs)
            if n_o == 0:
                scores[m_idx] = 0.5
                zs_all[m_idx] = []
                aux[m_idx] = (1.0, None, None)
                continue

            zs = [0.0] * n_o
            num = 0.0
            den = 0.0
            for j in range(n_o):
                b_idx = bs[j]
                sl = sls[b_idx]
                phi = phis[j]
                z = c0s[b_idx]
                for r in range(len(sl)):
                    z += phi[r] * sl[r]
                zs[j] = z
                wv = ws[b_idx]
                num += wv * z
                den += wv

            zs_all[m_idx] = zs
            s_val = num / den if den > 0.0 else 0.5
            if not robust:
                scores[m_idx] = s_val
                aux[m_idx] = (den, None, None)
            else:
                if init_s is not None:
                    s_val = init_s[m_idx]
                for _ in range(8):
                    nh = 0.0
                    dh = 0.0
                    for j in range(n_o):
                        r = s_val - zs[j]
                        u = 1.0 / math.sqrt(1.0 + r * r * inv_d2) + at
                        wu = ws[bs[j]] * u
                        nh += wu * zs[j]
                        dh += wu
                    if dh <= 0.0:
                        break
                    sn = nh / dh
                    if abs(sn - s_val) < 1e-8:
                        s_val = sn
                        break
                    s_val = sn

                scores[m_idx] = s_val
                pv = [0.0] * n_o
                pp = [0.0] * n_o
                denom_d = 0.0
                for j in range(n_o):
                    r = s_val - zs[j]
                    t = 1.0 + r * r * inv_d2
                    sq = math.sqrt(t)
                    pv[j] = r / sq + at * r
                    p = 1.0 / (t * sq) + at
                    pp[j] = p
                    denom_d += ws[bs[j]] * p
                aux[m_idx] = (denom_d, pv, pp)

        return scores, zs_all, aux

    def _optimize_stage2_pass(
        self,
        m_b: List[List[int]],
        m_phi: List[List[Tuple[float, ...]]],
        theta_anchor: List[float],
        c0_init: List[float],
        sl_init: List[List[float]],
        w_init: List[float],
        w_prior: List[float],
        train_edges: List[Tuple[int, int, str, float]],
        opt_curves: bool,
        opt_weights: bool,
        robust: bool,
        steps: int,
        lr_w: float,
        lr_c: float,
        beta: float,
        tau: float,
        anneal_beta_to: Optional[float] = None,
        anneal_tau_to: Optional[float] = None,
        c0_prior: Optional[List[float]] = None,
        sl_prior: Optional[List[List[float]]] = None,
    ) -> Tuple[List[float], List[List[float]], List[float], List[float]]:
        n_models = len(m_b)
        n_bench = len(c0_init)
        c0s = list(c0_init)
        sls = [list(s) for s in sl_init]
        ws = list(w_init)
        c0_ref = c0_prior if c0_prior is not None else c0_init
        sl_ref = sl_prior if sl_prior is not None else sl_init

        mw = [0.0] * n_bench
        vw = [0.0] * n_bench
        mc0 = [0.0] * n_bench
        vc0 = [0.0] * n_bench
        msl = [[0.0] * len(s) for s in sls]
        vsl = [[0.0] * len(s) for s in sls]

        n_obs_total = max(1, sum(len(x) for x in m_b))
        align_coef = 2.0 * self.lam_align / n_obs_total
        amix = self.align_mix
        prev_s = None

        b1, b2, eps_a = 0.9, 0.999, 1e-8
        for step in range(1, steps + 1):
            prog = (step - 1) / max(1, steps - 1)
            cur_beta = beta if anneal_beta_to is None else (beta + prog * (anneal_beta_to - beta))
            cur_tau = tau if anneal_tau_to is None else (tau + prog * (anneal_tau_to - tau))

            scores, zs_all, aux = self._forward_models(
                m_b, m_phi, c0s, sls, ws, robust=robust, init_s=prev_s
            )
            prev_s = scores

            dL_dS = [0.0] * n_models
            for ui, vi, _, ew in train_edges:
                arg = cur_beta * (cur_tau - (scores[ui] - scores[vi]))
                if arg > 35.0:
                    sig = 1.0
                elif arg < -35.0:
                    sig = 0.0
                else:
                    sig = 1.0 / (1.0 + math.exp(-arg))
                g = -ew * sig
                dL_dS[ui] += g
                dL_dS[vi] -= g

            gw = [0.0] * n_bench
            gc0 = [0.0] * n_bench
            gsl = [[0.0] * len(s) for s in sls]

            for m_idx in range(n_models):
                bs = m_b[m_idx]
                if not bs:
                    continue
                ds = dL_dS[m_idx]
                phis = m_phi[m_idx]
                zs = zs_all[m_idx]
                sv = scores[m_idx]
                th_a = amix * sv + (1.0 - amix) * theta_anchor[m_idx]

                if not robust:
                    den = aux[m_idx][0]
                    if den <= 0.0:
                        continue
                    dd = ds / den
                    for j in range(len(bs)):
                        b = bs[j]
                        z = zs[j]
                        if opt_weights and ds != 0.0:
                            gw[b] += dd * (z - sv)
                        if opt_curves:
                            dz = dd * ws[b] + align_coef * (z - th_a)
                            gc0[b] += dz
                            phi = phis[j]
                            gb = gsl[b]
                            for r in range(len(phi)):
                                gb[r] += dz * phi[r]
                else:
                    denom_d, pv, pp = aux[m_idx]
                    if denom_d <= 0.0:
                        continue
                    dd = ds / denom_d
                    for j in range(len(bs)):
                        b = bs[j]
                        z = zs[j]
                        if opt_weights and ds != 0.0:
                            gw[b] += dd * (-pv[j])
                        if opt_curves:
                            dz = dd * ws[b] * pp[j] + align_coef * (z - th_a)
                            gc0[b] += dz
                            phi = phis[j]
                            gb = gsl[b]
                            for r in range(len(phi)):
                                gb[r] += dz * phi[r]

            if opt_weights:
                for b in range(n_bench):
                    gw[b] += 2.0 * self.lam_w * (ws[b] - w_prior[b])
            if opt_curves:
                lcp = 2.0 * self.lam_curve_prior
                for b in range(n_bench):
                    sb = sls[b]
                    gb = gsl[b]
                    sref = sl_ref[b]
                    gc0[b] += lcp * (c0s[b] - c0_ref[b])
                    for r in range(len(sb)):
                        gb[r] += lcp * (sb[r] - sref[r])
                    for r in range(len(sb) - 1):
                        df = sb[r + 1] - sb[r]
                        gb[r + 1] += 2.0 * self.lam_smooth * df
                        gb[r] -= 2.0 * self.lam_smooth * df

            bc1 = 1.0 - b1 ** step
            bc2 = 1.0 - b2 ** step

            if opt_weights:
                w_cand = []
                for b in range(n_bench):
                    g = gw[b]
                    mw[b] = b1 * mw[b] + (1.0 - b1) * g
                    vw[b] = b2 * vw[b] + (1.0 - b2) * g * g
                    w_cand.append(ws[b] - lr_w * (mw[b] / bc1) / (math.sqrt(vw[b] / bc2) + eps_a))
                ws = project_bounded_simplex(w_cand, w_min=self.w_min, w_max=self.w_max)

            if opt_curves:
                for b in range(n_bench):
                    g0 = gc0[b]
                    mc0[b] = b1 * mc0[b] + (1.0 - b1) * g0
                    vc0[b] = b2 * vc0[b] + (1.0 - b2) * g0 * g0
                    c0_new = c0s[b] - lr_c * (mc0[b] / bc1) / (math.sqrt(vc0[b] / bc2) + eps_a)
                    c0s[b] = max(-1.0, min(1.5, c0_new))
                    sb = sls[b]
                    gb = gsl[b]
                    mb = msl[b]
                    vb = vsl[b]
                    for r in range(len(sb)):
                        gr = gb[r]
                        mb[r] = b1 * mb[r] + (1.0 - b1) * gr
                        vb[r] = b2 * vb[r] + (1.0 - b2) * gr * gr
                        s_new = sb[r] - lr_c * (mb[r] / bc1) / (math.sqrt(vb[r] / bc2) + eps_a)
                        sb[r] = max(self.eps_min, min(self.s_max, s_new))

        scores, _, _ = self._forward_models(
            m_b, m_phi, c0s, sls, ws, robust=robust, init_s=prev_s
        )
        return c0s, sls, ws, scores

    def _store_learned_params(
        self,
        keys: List[str],
        clean_ranges: Dict[str, Optional[dict]],
        knots_list: List[List[float]],
        c0s: List[float],
        sls: List[List[float]],
        ws: List[float],
        aggregation_mode: str,
        models: List[dict],
    ) -> None:
        self.metric_keys = list(keys)
        self.metric_ranges = clean_ranges
        self.curves = {}
        self.weights = {}
        for b_idx, k in enumerate(keys):
            kn = [float(x) for x in knots_list[b_idx]]
            c0 = float(c0s[b_idx])
            slopes = [float(s) for s in sls[b_idx]]
            knot_vals, deltas = compute_knot_values(kn, c0, slopes)
            self.curves[k] = {
                "knots": kn,
                "c0": c0,
                "slopes": slopes,
                "knot_values": knot_vals,
                "deltas": deltas,
                "eps_min": self.eps_min,
                "s_max": self.s_max,
            }
            self.weights[k] = float(ws[b_idx])

        self.aggregation = {
            "mode": aggregation_mode,
            "delta_huber": self.delta_huber,
            "alpha_tail": self.alpha_tail,
            "irls_iters": self.irls_iters,
            "irls_tol": self.irls_tol,
        }
        self.score_offset = 0.0
        self.score_scale = 1.0
        self.is_fitted = True

        # Calibrate affine [0, 1] scale constants from training population
        raw_scores = [self.score_model(_get_parsed_metrics(m)) for m in models]
        valid_scores = [s for s in raw_scores if s is not None]
        if valid_scores:
            mn = min(valid_scores)
            mx = max(valid_scores)
            self.score_offset = float(mn)
            self.score_scale = float(mx - mn) if mx > mn else 1.0

    def _fit_with_precomputed(
        self,
        models: List[dict],
        keys: List[str],
        clean_ranges: Dict[str, Optional[dict]],
        x_mat: List[List[Optional[float]]],
        knots_list: List[List[float]],
        m_b: List[List[int]],
        m_phi: List[List[Tuple[float, ...]]],
        stage1_out: tuple,
        constraints: Optional[Sequence[Tuple]] = None,
        eval_constraints_list: Optional[Sequence[Tuple]] = None,
        verbose: bool = False,
    ) -> "MonotoneBenchmarkMapper":
        raw_means, loo_means, theta1, c0_1, sl_1, w_1, s1_meta = stage1_out
        rounds_log = []

        def _make_map(arr: Sequence[float]) -> Dict[str, float]:
            return {
                _get_model_name(models[i]): float(arr[i])
                for i in range(len(models))
                if _get_model_name(models[i])
            }

        eval_c = eval_constraints_list if eval_constraints_list is not None else constraints

        def _log_round(round_id: str, label: str, arr: Sequence[float]):
            if eval_c:
                ev = evaluate_constraints(_make_map(arr), eval_c, top_k=10)
                entry = {
                    "round": round_id,
                    "label": label,
                    "concordance": ev["concordance"],
                    "concordance_pct": ev["concordance_pct"],
                    "satisfied": ev["satisfied"],
                    "total_constraints": ev["total_constraints"],
                    "violations_count": ev["violations_count"],
                    "by_rule": ev["by_rule"],
                }
            else:
                entry = {"round": round_id, "label": label}
            rounds_log.append(entry)
            if verbose and eval_c:
                print(
                    f"  [{round_id}: {label}] {entry['satisfied']}/{entry['total_constraints']} "
                    f"= {entry['concordance_pct']:.2f}% ({entry['violations_count']} inv)"
                )

        _log_round("round_0a", "Raw Min-Max Mean", raw_means)
        _log_round("round_0b", "LOO Linear Calibration", loo_means)
        _log_round("round_1", "Stage-1 Unsupervised Monotone Calibration", theta1)

        if not constraints:
            self._store_learned_params(
                keys, clean_ranges, knots_list, c0_1, sl_1, w_1, "weighted_mean", models
            )
            self.diagnostics = {
                "stage1": s1_meta,
                "rounds": rounds_log,
                "final_round": "round_1",
                "used_supervised_constraints": 0,
            }
            return self

        train_edges = self._build_balanced_edges(models, constraints)
        if not train_edges:
            self._store_learned_params(
                keys, clean_ranges, knots_list, c0_1, sl_1, w_1, "weighted_mean", models
            )
            self.diagnostics = {
                "stage1": s1_meta,
                "rounds": rounds_log,
                "final_round": "round_1",
                "used_supervised_constraints": 0,
            }
            return self

        # Round 2: Regularized benchmark weight optimization
        c0_2, sl_2, w_2, s_2 = self._optimize_stage2_pass(
            m_b, m_phi, theta1, c0_1, sl_1, w_1, w_1, train_edges,
            opt_curves=False, opt_weights=True, robust=False,
            steps=140, lr_w=0.04, lr_c=0.0, beta=60.0, tau=0.015,
        )
        _log_round("round_2", "Regularized Benchmark Weight Optimization", s_2)

        # Round 3: Joint optimization of monotone spline curves g_b + weights w_b
        c0_3, sl_3, w_3, s_3 = self._optimize_stage2_pass(
            m_b, m_phi, theta1, c0_2, sl_2, w_2, w_1, train_edges,
            opt_curves=True, opt_weights=True, robust=False,
            steps=160, lr_w=0.025, lr_c=0.007, beta=70.0, tau=0.015,
            c0_prior=c0_1, sl_prior=sl_1,
        )
        _log_round("round_3", "Joint Monotone Curve + Weight Optimization", s_3)

        # Round 4a: Huber / IRLS Robust Aggregation on Round 3 parameters
        s_4a, _, _ = self._forward_models(m_b, m_phi, c0_3, sl_3, w_3, robust=True)
        _log_round("round_4a", "Pseudo-Huber IRLS Robust Aggregation", s_4a)

        # Round 4b: Margin-Annealed Second-Pass Refinement under Huber / IRLS scoring
        c0_4, sl_4, w_4, s_4b = self._optimize_stage2_pass(
            m_b, m_phi, theta1, c0_3, sl_3, w_3, w_1, train_edges,
            opt_curves=True, opt_weights=True, robust=True,
            steps=140, lr_w=0.02, lr_c=0.0045, beta=75.0, tau=0.014,
            anneal_beta_to=115.0, anneal_tau_to=0.008,
            c0_prior=c0_1, sl_prior=sl_1,
        )
        _log_round("round_4b", "Huber/IRLS + Margin-Annealed Refinement", s_4b)

        self._store_learned_params(
            keys, clean_ranges, knots_list, c0_4, sl_4, w_4, "pseudo_huber_irls", models
        )

        final_scores = self.score_all(models)
        final_eval = evaluate_constraints(final_scores, eval_c, top_k=40) if eval_c else None
        flagship_eval = _evaluate_flagship_chains(final_scores)
        mono_check = self.verify_monotonicity()

        self.diagnostics = {
            "stage1": s1_meta,
            "used_supervised_constraints": len(train_edges),
            "rounds": rounds_log,
            "final_round": "round_4b",
            "final_evaluation": final_eval,
            "flagship_chains": flagship_eval,
            "monotonicity_verified": mono_check,
            "learned_weights_sorted": sorted(
                [{"metric": k, "weight": w} for k, w in self.weights.items()],
                key=lambda d: -d["weight"],
            ),
        }
        return self

    def fit(
        self,
        models: List[dict],
        metric_keys: Sequence[str],
        metric_ranges: Optional[Dict[str, Optional[dict]]],
        constraints: Optional[Sequence[Tuple]] = None,
        max_stage1_rounds: int = 40,
        stage1_tol: float = 1e-5,
        verbose: bool = False,
    ) -> "MonotoneBenchmarkMapper":
        """Fit Stage 1 (unsupervised) and optional Stage 2 (multi-round + Huber IRLS)."""
        keys, clean_ranges, x_mat, knots_list, obs_by_bench, m_b, m_phi = self._prepare_training_tensors(
            models, metric_keys, metric_ranges
        )
        stage1_out = self._run_stage1_unsupervised(
            x_mat, knots_list, obs_by_bench, m_b, m_phi,
            max_rounds=max_stage1_rounds, tol=stage1_tol,
        )
        return self._fit_with_precomputed(
            models, keys, clean_ranges, x_mat, knots_list, m_b, m_phi,
            stage1_out, constraints=constraints, verbose=verbose,
        )

    def score_model(self, parsed_metrics: Dict[str, Optional[float]]) -> Optional[float]:
        """Score a single model purely from its benchmark scores (ZERO label leakage)."""
        if not self.is_fitted or not isinstance(parsed_metrics, dict):
            return None

        zs: List[float] = []
        ws: List[float] = []
        for k in self.metric_keys:
            rng = self.metric_ranges.get(k)
            if rng is None or rng.get("count", 0) <= 0:
                continue
            x = _normalize_raw_value(parsed_metrics.get(k), rng)
            if x is None:
                continue
            curve = self.curves.get(k)
            w = self.weights.get(k, 1.0)
            if curve is None or w <= 0.0:
                continue
            z = eval_piecewise_linear(x, curve["knots"], curve["c0"], curve["slopes"])
            zs.append(z)
            ws.append(w)

        if not zs:
            return None

        agg_mode = self.aggregation.get("mode", "pseudo_huber_irls")
        if agg_mode == "pseudo_huber_irls":
            raw_s = aggregate_pseudo_huber_irls(
                zs,
                ws,
                delta_huber=float(self.aggregation.get("delta_huber", self.delta_huber)),
                alpha_tail=float(self.aggregation.get("alpha_tail", self.alpha_tail)),
                max_iters=int(self.aggregation.get("irls_iters", self.irls_iters)),
                tol=float(self.aggregation.get("irls_tol", self.irls_tol)),
            )
        else:
            num = sum(ws[i] * zs[i] for i in range(len(zs)))
            den = sum(ws)
            raw_s = num / den if den > 0.0 else (sum(zs) / len(zs))

        scale = self.score_scale if self.score_scale > 0.0 else 1.0
        return float((raw_s - self.score_offset) / scale)

    def score_all(self, models: List[dict]) -> Dict[str, float]:
        """Independently score every model via score_model(parsed_metrics)."""
        out: Dict[str, float] = {}
        for m in models:
            nm = _get_model_name(m)
            sc = self.score_model(_get_parsed_metrics(m))
            if nm and sc is not None:
                out[nm] = sc
        return out

    @staticmethod
    def evaluate_constraints(
        score_map: Dict[str, float],
        constraints: Sequence[Tuple],
        top_k: int = 30,
    ) -> dict:
        """Evaluate overall and per-rule constraint concordance & worst violations."""
        return evaluate_constraints(score_map, constraints, top_k=top_k)

    def verify_monotonicity(self, num_grid: int = 101) -> dict:
        """Verify strictly positive slopes (>= eps_min) and strict monotonicity on [0, 1]."""
        all_ok = True
        min_slope = float("inf")
        failing = []
        xs = [i / max(1, num_grid - 1) for i in range(num_grid)]

        for k in self.metric_keys:
            curve = self.curves.get(k)
            if not curve:
                continue
            slopes = curve["slopes"]
            if not slopes or min(slopes) < self.eps_min - 1e-12:
                all_ok = False
                failing.append((k, "slope_below_eps_min"))
            min_slope = min(min_slope, min(slopes))
            prev_y = eval_piecewise_linear(xs[0], curve["knots"], curve["c0"], slopes)
            for x in xs[1:]:
                y = eval_piecewise_linear(x, curve["knots"], curve["c0"], slopes)
                if y <= prev_y:
                    all_ok = False
                    failing.append((k, "non_increasing_grid"))
                    break
                prev_y = y

        return {
            "all_strictly_monotone": all_ok,
            "min_slope_observed": float(min_slope) if min_slope < float("inf") else 0.0,
            "eps_min_required": float(self.eps_min),
            "failing_benchmarks": failing,
        }

    def cross_validate_lovo(
        self,
        models: List[dict],
        metric_keys: Sequence[str],
        metric_ranges: Optional[Dict[str, Optional[dict]]],
        constraints: Sequence[Tuple],
        vendors: Optional[Sequence[str]] = None,
        verbose: bool = False,
    ) -> dict:
        """Leave-One-Vendor-Out (LOVO) cross-validation.

        Stage 1 runs unsupervised (using 0 constraint labels). For each vendor v,
        Stage 2 is trained strictly WITHOUT any constraints involving vendor v's
        models, then evaluated on vendor v's held-out constraints.
        """
        target_vendors = list(vendors) if vendors is not None else list(DEFAULT_LOVO_VENDORS)
        keys, clean_ranges, x_mat, knots_list, obs_by_bench, m_b, m_phi = self._prepare_training_tensors(
            models, metric_keys, metric_ranges
        )
        stage1_out = self._run_stage1_unsupervised(x_mat, knots_list, obs_by_bench, m_b, m_phi)
        raw_means, loo_means, theta1, _, _, _, _ = stage1_out

        raw_map = {_get_model_name(models[i]): raw_means[i] for i in range(len(models))}
        loo_map = {_get_model_name(models[i]): loo_means[i] for i in range(len(models))}
        r1_map = {_get_model_name(models[i]): theta1[i] for i in range(len(models))}

        vendor_table = []
        agg_counts = {
            "total": 0,
            "r0_raw_ok": 0,
            "r0_loo_ok": 0,
            "r1_unsup_ok": 0,
            "r2_ok": 0,
            "r3_ok": 0,
            "r4_ok": 0,
        }

        for vendor in target_vendors:
            v_norm = _normalize_vendor(vendor)
            v_names = {
                _get_model_name(m)
                for m in models
                if _normalize_vendor(m.get("creator", "")) == v_norm
            }
            train_c = [c for c in constraints if c[0] not in v_names and c[1] not in v_names]
            held_c = [c for c in constraints if c[0] in v_names and c[1] in v_names]
            if not held_c:
                continue

            fold_mapper = self._clone_hparams()
            fold_mapper._fit_with_precomputed(
                models, keys, clean_ranges, x_mat, knots_list, m_b, m_phi,
                stage1_out, constraints=train_c, eval_constraints_list=held_c, verbose=False,
            )

            ev_raw = evaluate_constraints(raw_map, held_c, top_k=0)
            ev_loo = evaluate_constraints(loo_map, held_c, top_k=0)
            ev_r1 = evaluate_constraints(r1_map, held_c, top_k=0)
            fold_scores = fold_mapper.score_all(models)
            ev_r4 = evaluate_constraints(fold_scores, held_c, top_k=5)

            rounds_by_id = {r["round"]: r for r in fold_mapper.diagnostics.get("rounds", [])}
            ev_r2 = rounds_by_id.get("round_2", ev_r1)
            ev_r3 = rounds_by_id.get("round_3", ev_r2)

            n_pairs = ev_r4["total_constraints"]
            agg_counts["total"] += n_pairs
            agg_counts["r0_raw_ok"] += ev_raw["satisfied"]
            agg_counts["r0_loo_ok"] += ev_loo["satisfied"]
            agg_counts["r1_unsup_ok"] += ev_r1["satisfied"]
            agg_counts["r2_ok"] += ev_r2["satisfied"]
            agg_counts["r3_ok"] += ev_r3["satisfied"]
            agg_counts["r4_ok"] += ev_r4["satisfied"]

            row = {
                "vendor": vendor,
                "held_out_models": len(v_names),
                "held_out_constraints": n_pairs,
                "train_constraints": len(train_c),
                "r0_raw_pct": ev_raw["concordance_pct"],
                "r0_loo_pct": ev_loo["concordance_pct"],
                "r1_unsup_pct": ev_r1["concordance_pct"],
                "r2_heldout_pct": ev_r2["concordance_pct"],
                "r3_heldout_pct": ev_r3["concordance_pct"],
                "r4_heldout_pct": ev_r4["concordance_pct"],
                "delta_vs_r0_loo_pct": ev_r4["concordance_pct"] - ev_loo["concordance_pct"],
                "delta_vs_r1_pct": ev_r4["concordance_pct"] - ev_r1["concordance_pct"],
                "r4_by_rule": ev_r4["by_rule"],
            }
            vendor_table.append(row)
            if verbose:
                print(
                    f"  LOVO {vendor:10s} (N={n_pairs:4d}): "
                    f"R0_raw={row['r0_raw_pct']:5.2f}% | R0_LOO={row['r0_loo_pct']:5.2f}% | "
                    f"R1={row['r1_unsup_pct']:5.2f}% | R4_heldout={row['r4_heldout_pct']:5.2f}% "
                    f"(vs R1: {row['delta_vs_r1_pct']:+.2f}%)"
                )

        tot = max(1, agg_counts["total"])
        summary = {
            "total_held_out_constraints": agg_counts["total"],
            "r0_raw_pct": 100.0 * agg_counts["r0_raw_ok"] / tot,
            "r0_loo_pct": 100.0 * agg_counts["r0_loo_ok"] / tot,
            "r1_unsup_pct": 100.0 * agg_counts["r1_unsup_ok"] / tot,
            "r2_heldout_pct": 100.0 * agg_counts["r2_ok"] / tot,
            "r3_heldout_pct": 100.0 * agg_counts["r3_ok"] / tot,
            "r4_heldout_pct": 100.0 * agg_counts["r4_ok"] / tot,
            "delta_vs_r0_loo_pct": 100.0 * (agg_counts["r4_ok"] - agg_counts["r0_loo_ok"]) / tot,
            "delta_vs_r1_pct": 100.0 * (agg_counts["r4_ok"] - agg_counts["r1_unsup_ok"]) / tot,
        }
        return {"summary": summary, "vendors": vendor_table}

    def to_dict(self) -> dict:
        """Serialize mapper parameters and optimization diagnostics to JSON-safe dict."""
        return {
            "version": 1,
            "hyperparameters": {
                "eps_min": self.eps_min,
                "s_max": self.s_max,
                "w_min": self.w_min,
                "w_max": self.w_max,
                "lam_smooth_stage1": self.lam_smooth_stage1,
                "lam_w": self.lam_w,
                "lam_align": self.lam_align,
                "lam_smooth": self.lam_smooth,
                "lam_curve_prior": self.lam_curve_prior,
                "align_mix": self.align_mix,
                "delta_huber": self.delta_huber,
                "alpha_tail": self.alpha_tail,
                "rule_balance_power": self.rule_balance_power,
                "irls_iters": self.irls_iters,
                "irls_tol": self.irls_tol,
            },
            "is_fitted": self.is_fitted,
            "metric_keys": list(self.metric_keys),
            "metric_ranges": {
                k: (dict(v) if isinstance(v, dict) else None)
                for k, v in self.metric_ranges.items()
            },
            "curves": {
                k: {
                    "knots": list(v["knots"]),
                    "c0": float(v["c0"]),
                    "slopes": list(v["slopes"]),
                    "knot_values": list(v["knot_values"]),
                    "deltas": list(v["deltas"]),
                    "eps_min": float(v["eps_min"]),
                    "s_max": float(v["s_max"]),
                }
                for k, v in self.curves.items()
            },
            "weights": {k: float(w) for k, w in self.weights.items()},
            "aggregation": dict(self.aggregation),
            "score_offset": float(self.score_offset),
            "score_scale": float(self.score_scale),
            "diagnostics": self.diagnostics,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "MonotoneBenchmarkMapper":
        """Reconstruct a fitted MonotoneBenchmarkMapper from a serialized dict."""
        hp = d.get("hyperparameters", {})
        mapper = cls(
            eps_min=hp.get("eps_min", 0.05),
            s_max=hp.get("s_max", 5.0),
            w_min=hp.get("w_min", 0.10),
            w_max=hp.get("w_max", 3.2),
            lam_smooth_stage1=hp.get("lam_smooth_stage1", 0.05),
            lam_w=hp.get("lam_w", 1e-4),
            lam_align=hp.get("lam_align", 0.15),
            lam_smooth=hp.get("lam_smooth", 3e-4),
            lam_curve_prior=hp.get("lam_curve_prior", 0.0),
            align_mix=hp.get("align_mix", 0.0),
            delta_huber=hp.get("delta_huber", 0.08),
            alpha_tail=hp.get("alpha_tail", 0.05),
            rule_balance_power=hp.get("rule_balance_power", 0.5),
            irls_iters=hp.get("irls_iters", 20),
            irls_tol=hp.get("irls_tol", 1e-10),
        )
        mapper.is_fitted = bool(d.get("is_fitted", False))
        mapper.metric_keys = list(d.get("metric_keys", []))
        mapper.metric_ranges = dict(d.get("metric_ranges", {}))
        mapper.curves = dict(d.get("curves", {}))
        mapper.weights = {k: float(v) for k, v in d.get("weights", {}).items()}
        mapper.aggregation = dict(d.get("aggregation", mapper.aggregation))
        mapper.score_offset = float(d.get("score_offset", 0.0))
        mapper.score_scale = float(d.get("score_scale", 1.0))
        mapper.diagnostics = dict(d.get("diagnostics", {}))
        return mapper

    def save_mapping(self, path: str) -> None:
        """Persist serialized mapper & diagnostics to JSON file."""
        os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            json.dump(self.to_dict(), f, indent=2, ensure_ascii=False)

    @classmethod
    def load_mapping(cls, path: str) -> "MonotoneBenchmarkMapper":
        """Load MonotoneBenchmarkMapper from JSON file."""
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return cls.from_dict(data)


def save_mapping(mapper: MonotoneBenchmarkMapper, path: str) -> None:
    """Module-level convenience wrapper for MonotoneBenchmarkMapper.save_mapping."""
    mapper.save_mapping(path)


def load_mapping(path: str) -> MonotoneBenchmarkMapper:
    """Module-level convenience wrapper for MonotoneBenchmarkMapper.load_mapping."""
    return MonotoneBenchmarkMapper.load_mapping(path)


# ══════════════════════════════════════════════════════════════════════
# End-to-End Fitting + LOVO Validation Runner
# ══════════════════════════════════════════════════════════════════════

def train_and_evaluate(
    raw_data_path: str = RAW_DATA_FILE,
    model_out_path: Optional[str] = DEFAULT_MODEL_PATH,
    min_valid: int = 3,
    run_lovo: bool = True,
    verbose: bool = True,
) -> MonotoneBenchmarkMapper:
    """Load data + hierarchy constraints, fit mapper, run LOVO CV, and save JSON."""
    try:
        from src import hierarchy
    except ImportError:
        import hierarchy

    t0 = time.time()
    if hasattr(hierarchy, "load_hierarchy_dataset"):
        ds = hierarchy.load_hierarchy_dataset(
            raw_data_file=raw_data_path, min_valid=min_valid, load_from_disk=True
        )
        models = ds["models"]
        metric_ranges = ds["metric_ranges"]
        constraints = ds["constraints"]
        stats = ds["stats"]
    else:
        with open(raw_data_path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
        models_all, _ = hierarchy.extract_benchmarks(raw_data, min_valid=0)
        models, metric_ranges = hierarchy.extract_benchmarks(raw_data, min_valid=min_valid)
        mgr = hierarchy.VendorHierarchyManager(all_models=models_all, load_from_disk=True)
        constraints, stats = hierarchy.generate_hierarchy_constraints(models, mgr)
    metric_keys = list(hierarchy.BENCHMARK_DEFS.keys())

    if verbose:
        print("=" * 72)
        print("Monotone Benchmark Mapping & Multi-Round Calibration")
        print("=" * 72)
        print(f"Models: {len(models)} (min_valid={min_valid}), Benchmarks: {len(metric_keys)}")
        print(f"Constraints: {len(constraints)} {stats}")
        print("\n--- Multi-Round Fitting Progression ---")

    mapper = MonotoneBenchmarkMapper()
    mapper.fit(models, metric_keys, metric_ranges, constraints=constraints, verbose=verbose)

    if run_lovo:
        if verbose:
            print("\n--- Leave-One-Vendor-Out (LOVO) Cross-Validation ---")
        lovo_res = mapper.cross_validate_lovo(
            models, metric_keys, metric_ranges, constraints, verbose=verbose
        )
        mapper.diagnostics["lovo_cv"] = lovo_res
        if verbose:
            sm = lovo_res["summary"]
            print(
                f"  TOTAL LOVO ({sm['total_held_out_constraints']} pairs): "
                f"R0_raw={sm['r0_raw_pct']:.2f}% | R0_LOO={sm['r0_loo_pct']:.2f}% | "
                f"R1={sm['r1_unsup_pct']:.2f}% | R4_heldout={sm['r4_heldout_pct']:.2f}% "
                f"(vs R0_LOO: {sm['delta_vs_r0_loo_pct']:+.2f}%, vs R1: {sm['delta_vs_r1_pct']:+.2f}%)"
            )

    if verbose:
        mono = mapper.diagnostics.get("monotonicity_verified", {})
        print(
            f"\nMonotonicity check: passed={mono.get('all_strictly_monotone')}, "
            f"min_slope={mono.get('min_slope_observed', 0.0):.4f}"
        )
        print("\n--- Key Flagship Chains ---")
        for fc in mapper.diagnostics.get("flagship_chains", []):
            status = "PASS" if fc["passed"] else "FAIL"
            vals = " > ".join(f"{x['model']} ({x['score']:.4f})" for x in fc["scores"])
            print(f"  [{status}] {vals}")

    mapper.diagnostics["elapsed_seconds"] = round(time.time() - t0, 2)
    if model_out_path:
        mapper.save_mapping(model_out_path)
        if verbose:
            print(f"\nSaved mapping model & diagnostics to {model_out_path}")

    return mapper


def main():
    parser = argparse.ArgumentParser(description="Monotone Benchmark Calibration & Mapping Engine")
    parser.add_argument("--raw-data", default=RAW_DATA_FILE, help="Path to raw_data.json")
    parser.add_argument("--out", default=DEFAULT_MODEL_PATH, help="Output mapping_model.json path")
    parser.add_argument("--min-valid", type=int, default=3, help="Minimum valid benchmarks per model")
    parser.add_argument("--skip-lovo", action="store_true", help="Skip LOVO cross-validation")
    args = parser.parse_args()

    train_and_evaluate(
        raw_data_path=args.raw_data,
        model_out_path=args.out,
        min_valid=args.min_valid,
        run_lovo=not args.skip_lovo,
        verbose=True,
    )


if __name__ == "__main__":
    main()
