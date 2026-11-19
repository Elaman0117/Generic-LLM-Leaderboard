#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit, Invariance, and Regression Tests for MonotoneBenchmarkMapper (src/mapping.py)
===================================================================================

All tests run in pure Python without NumPy and never modify production output/.
"""

import json
import os
import sys
import tempfile
import unittest
from fractions import Fraction

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
RAW_DATA_PATH = os.path.join(OUTPUT_DIR, "raw_data.json")
MAPPING_MODEL_PATH = os.path.join(OUTPUT_DIR, "mapping_model.json")

sys.path.insert(0, os.path.join(BASE_DIR, "src"))

import hierarchy  # noqa: E402
from mapping import (  # noqa: E402
    DEFAULT_MODEL_PATH,
    FLAGSHIP_ORDERING_CHAINS,
    MonotoneBenchmarkMapper,
    aggregate_pseudo_huber_irls,
    build_adaptive_knots,
    eval_piecewise_linear,
    fit_monotone_spline_qp,
    load_mapping,
    project_bounded_simplex,
    save_mapping,
    spline_basis,
)


def _make_synthetic_dataset(n_models=60):
    """Build deterministic synthetic models across 3 vendors with 1 noisy metric."""
    metric_keys = ["m_good1", "m_good2", "m_good3", "m_noisy"]
    models = []
    constraints = []
    vendors = ["VendorA", "VendorB", "VendorC"]

    for v_idx, vendor in enumerate(vendors):
        prev_name = None
        for step in range(n_models // len(vendors)):
            ability = (step + 0.3 * v_idx) / (n_models // len(vendors))
            name = f"{vendor} Model v{step}"
            noisy_val = 1.0 - ability if step % 2 == 0 else 0.2 + 0.5 * ability
            parsed = {
                "m_good1": 10.0 + 80.0 * (ability ** 1.3),
                "m_good2": 20.0 + 70.0 * ability,
                "m_good3": 0.1 + 0.85 * math_tanh_like(ability),
                "m_noisy": noisy_val,
            }
            if step == 3:
                parsed["m_good3"] = None
            models.append({"name": name, "creator": vendor, "parsed": parsed})
            if prev_name is not None:
                constraints.append((name, prev_name, "Rule 2: version ordering"))
            prev_name = name

    metric_ranges = {}
    for k in metric_keys:
        vals = [m["parsed"][k] for m in models if m["parsed"][k] is not None]
        metric_ranges[k] = {"min": min(vals), "max": max(vals), "count": len(vals)}
    return models, metric_keys, metric_ranges, constraints


def math_tanh_like(x):
    return x / (0.4 + 0.6 * x) if x >= 0 else 0.0


class TestMonotonePrimitives(unittest.TestCase):
    """Verify low-level pure-Python spline, simplex, and IRLS building blocks."""

    def test_adaptive_knots_strictly_increasing(self):
        for xs in (
            [0.1, 0.5, 0.9],
            [0.0] * 45 + [1.0] * 10,
            [i / 150.0 for i in range(150)],
        ):
            knots = build_adaptive_knots(xs, dt_min=0.03)
            self.assertEqual(knots[0], 0.0)
            self.assertAlmostEqual(knots[-1], 1.0, places=9)
            for a, b in zip(knots, knots[1:]):
                self.assertGreater(b, a)

    def test_fit_monotone_spline_qp_enforces_positive_slope_under_anti_correlation(self):
        knots = [0.0, 0.25, 0.5, 0.75, 1.0]
        xs = [i / 40.0 for i in range(41)]
        phis = [spline_basis(x, knots) for x in xs]
        inverted_thetas = [1.0 - x for x in xs]
        c0, slopes, _ = fit_monotone_spline_qp(
            phis, inverted_thetas, num_segs=len(knots) - 1, eps_min=0.05, s_max=5.0
        )
        self.assertTrue(all(s >= 0.05 - 1e-12 for s in slopes))
        ys = [eval_piecewise_linear(x, knots, c0, slopes) for x in (-0.2, 0.0, 0.3, 0.7, 1.0, 1.3)]
        for y0, y1 in zip(ys, ys[1:]):
            self.assertGreater(y1, y0)

    def test_project_bounded_simplex(self):
        vals = [0.01, 5.0, 0.9, 1.2, 0.4]
        proj = project_bounded_simplex(vals, w_min=0.2, w_max=2.0, target_sum=5.0)
        self.assertAlmostEqual(sum(proj), 5.0, places=7)
        for w in proj:
            self.assertGreaterEqual(w, 0.2 - 1e-9)
            self.assertLessEqual(w, 2.0 + 1e-9)

    def test_pseudo_huber_irls_monotonicity_and_outlier_resistance(self):
        base = [0.60, 0.62, 0.61, 0.63, 0.02]
        ws = [1.0] * len(base)
        s_huber = aggregate_pseudo_huber_irls(base, ws, delta_huber=0.08, alpha_tail=0.05)
        s_mean = sum(base) / len(base)
        self.assertGreater(s_huber, s_mean + 0.08)

        bumped = list(base)
        bumped[4] = 0.05
        s_huber_bumped = aggregate_pseudo_huber_irls(bumped, ws, delta_huber=0.08, alpha_tail=0.05)
        self.assertGreater(s_huber_bumped, s_huber)


class TestMonotoneBenchmarkMapperBehavior(unittest.TestCase):
    """Verify monotonicity, zero label leakage, missingness, serialization, and pure-Python."""

    def setUp(self):
        self.models, self.metric_keys, self.metric_ranges, self.constraints = _make_synthetic_dataset()
        self.mapper = MonotoneBenchmarkMapper()
        self.mapper.fit(
            self.models,
            self.metric_keys,
            self.metric_ranges,
            constraints=self.constraints,
            verbose=False,
        )

    def test_strict_monotonicity_and_perturbation_monotonicity(self):
        mono = self.mapper.verify_monotonicity(num_grid=201)
        self.assertTrue(mono["all_strictly_monotone"])
        self.assertGreaterEqual(mono["min_slope_observed"], self.mapper.eps_min - 1e-12)
        self.assertEqual(mono["failing_benchmarks"], [])

        sample = self.models[10]["parsed"]
        base_score = self.mapper.score_model(sample)
        self.assertIsNotNone(base_score)

        for k in self.metric_keys:
            if sample.get(k) is None:
                continue
            span = self.metric_ranges[k]["max"] - self.metric_ranges[k]["min"]
            perturbed = dict(sample)
            perturbed[k] = sample[k] + 0.05 * span
            new_score = self.mapper.score_model(perturbed)
            self.assertGreater(
                new_score,
                base_score,
                f"Perturbing {k} upward must strictly increase score_model",
            )

    def test_zero_label_leakage_pure_function_invariance(self):
        """Renaming/shuffling model identity fields must never alter score_model."""
        for m in self.models[:15]:
            pure_metrics = dict(m["parsed"])
            expected = self.mapper.score_model(pure_metrics)

            for fake_name, fake_creator, fake_tier, fake_ver, fake_tag in [
                ("GPT-99 Ultra (max)", "OpenAI", "Tier 1", "v99", "max"),
                ("Tiny-0.1B (non-reasoning)", "Unknown", "Tier 4", "v0", "non-reasoning"),
                (m["name"], m["creator"], "Tier 2", "v1", "medium"),
            ]:
                injected = dict(pure_metrics)
                injected["name"] = fake_name
                injected["model"] = fake_name
                injected["full_name"] = fake_name
                injected["creator"] = fake_creator
                injected["tier"] = fake_tier
                injected["version"] = fake_ver
                injected["thinking_tag"] = fake_tag
                self.assertEqual(self.mapper.score_model(injected), expected)

        # Shuffling model order and renaming before score_model produces identical values
        for m in self.models[:5]:
            shuffled = {k: m["parsed"][k] for k in reversed(self.metric_keys)}
            self.assertEqual(self.mapper.score_model(shuffled), self.mapper.score_model(m["parsed"]))

    def test_missingness_and_none_fallbacks(self):
        unfitted = MonotoneBenchmarkMapper()
        self.assertIsNone(unfitted.score_model({"m_good1": 50.0}))

        self.assertIsNone(self.mapper.score_model({}))
        self.assertIsNone(self.mapper.score_model(None))  # type: ignore[arg-type]
        self.assertIsNone(self.mapper.score_model({k: None for k in self.metric_keys}))
        self.assertIsNone(self.mapper.score_model({"unknown_metric": 100.0}))

        partial = self.mapper.score_model({"m_good1": 50.0, "m_good2": None})
        self.assertIsNotNone(partial)

        # Fraction values (as produced in src/analyze.py) work seamlessly
        frac_score = self.mapper.score_model({"m_good1": Fraction(50, 1)})
        self.assertAlmostEqual(frac_score, partial, places=12)

    def test_serialization_round_trip(self):
        raw_dict = self.mapper.to_dict()
        restored = MonotoneBenchmarkMapper.from_dict(raw_dict)
        for m in self.models[:15]:
            self.assertEqual(
                restored.score_model(m["parsed"]),
                self.mapper.score_model(m["parsed"]),
            )
        self.assertEqual(restored.weights, self.mapper.weights)

        with tempfile.TemporaryDirectory() as tmp_dir:
            out_path = os.path.join(tmp_dir, "mapping_roundtrip.json")
            save_mapping(self.mapper, out_path)
            loaded = load_mapping(out_path)
            for m in self.models[:15]:
                self.assertEqual(
                    loaded.score_model(m["parsed"]),
                    self.mapper.score_model(m["parsed"]),
                )
            self.assertEqual(loaded.diagnostics.get("rounds"), self.mapper.diagnostics.get("rounds"))

    def test_stage1_unsupervised_fit_without_constraints(self):
        m_unsup = MonotoneBenchmarkMapper()
        m_unsup.fit(self.models, self.metric_keys, self.metric_ranges, constraints=None)
        self.assertTrue(m_unsup.is_fitted)
        self.assertTrue(m_unsup.verify_monotonicity()["all_strictly_monotone"])
        self.assertEqual(m_unsup.diagnostics.get("final_round"), "round_1")
        self.assertEqual(m_unsup.diagnostics.get("used_supervised_constraints"), 0)

    def test_pure_python_execution_without_numpy(self):
        old_np = sys.modules.get("numpy", "__MISSING__")
        sys.modules["numpy"] = None  # type: ignore[assignment]
        try:
            m_py = MonotoneBenchmarkMapper()
            m_py.fit(
                self.models,
                self.metric_keys,
                self.metric_ranges,
                constraints=self.constraints,
                verbose=False,
            )
            lovo = m_py.cross_validate_lovo(
                self.models,
                self.metric_keys,
                self.metric_ranges,
                self.constraints,
                vendors=["VendorA", "VendorB"],
                verbose=False,
            )
            self.assertGreater(lovo["summary"]["total_held_out_constraints"], 0)
            self.assertTrue(m_py.verify_monotonicity()["all_strictly_monotone"])
        finally:
            if old_np == "__MISSING__":
                sys.modules.pop("numpy", None)
            else:
                sys.modules["numpy"] = old_np


class TestFittedProductionMappingRegression(unittest.TestCase):
    """Read-only regression assertions against fitted output/mapping_model.json."""

    @classmethod
    def setUpClass(cls):
        if not os.path.exists(MAPPING_MODEL_PATH):
            raise unittest.SkipTest(f"Missing fitted mapping model: {MAPPING_MODEL_PATH}")
        cls.mapper = load_mapping(MAPPING_MODEL_PATH)
        with open(RAW_DATA_PATH, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
        cls.models, _ = hierarchy.extract_benchmarks(raw_data, min_valid=3)
        cls.models_by_name = {m["name"]: m for m in cls.models}
        cls.scores = cls.mapper.score_all(cls.models)

    def test_default_model_path_constant(self):
        self.assertEqual(
            os.path.abspath(DEFAULT_MODEL_PATH),
            os.path.abspath(MAPPING_MODEL_PATH),
        )

    def test_fitted_curves_monotonicity_and_perturbation(self):
        self.assertTrue(self.mapper.is_fitted)
        self.assertEqual(len(self.mapper.metric_keys), 38)
        mono = self.mapper.verify_monotonicity(num_grid=201)
        self.assertTrue(mono["all_strictly_monotone"])
        self.assertGreaterEqual(mono["min_slope_observed"], self.mapper.eps_min - 1e-12)

        # Spot-check upward perturbation monotonicity on real models
        for m in self.models[:15]:
            base_s = self.mapper.score_model(m["parsed"])
            self.assertIsNotNone(base_s)
            for k, val in m["parsed"].items():
                if val is None:
                    continue
                rng = self.mapper.metric_ranges.get(k)
                if not rng or rng["max"] <= rng["min"]:
                    continue
                bumped = dict(m["parsed"])
                bumped[k] = val + 0.05 * (rng["max"] - rng["min"])
                self.assertGreater(
                    self.mapper.score_model(bumped),
                    base_s,
                    f"Perturbing {k} on {m['name']} failed strict monotonicity",
                )

    def test_fitted_zero_leakage_invariance(self):
        for m in self.models[:10]:
            pure = {k: m["parsed"][k] for k in self.mapper.metric_keys}
            s_pure = self.mapper.score_model(pure)
            polluted = dict(pure)
            polluted.update({
                "name": "Fake-Model-0B (non-reasoning)",
                "creator": "FakeVendor",
                "tier": "Tier 4",
                "version": "0.1",
                "thinking_tag": "non-reasoning",
            })
            self.assertEqual(self.mapper.score_model(polluted), s_pure)

    def test_noisy_benchmarks_downweighted(self):
        w = self.mapper.weights
        self.assertTrue(all(self.mapper.w_min - 1e-9 <= v <= self.mapper.w_max + 1e-9 for v in w.values()))
        self.assertLess(w["omniscienceNonHallucination"], w["intelligenceIndex"])
        self.assertLess(w["healthbench"], w["intelligenceIndex"])
        self.assertLess(w["healthbench"], w["hle"])

    def test_rounds_progression_and_lovo_generalization(self):
        rounds = {r["round"]: r for r in self.mapper.diagnostics.get("rounds", [])}
        self.assertIn("round_0a", rounds)
        self.assertIn("round_0b", rounds)
        self.assertIn("round_1", rounds)
        self.assertIn("round_4b", rounds)

        self.assertGreater(rounds["round_0b"]["concordance_pct"], rounds["round_0a"]["concordance_pct"])
        self.assertGreater(rounds["round_1"]["concordance_pct"], rounds["round_0b"]["concordance_pct"])
        self.assertGreater(rounds["round_4b"]["concordance_pct"], rounds["round_1"]["concordance_pct"])
        self.assertGreater(rounds["round_4b"]["concordance_pct"], 97.5)

        lovo = self.mapper.diagnostics.get("lovo_cv", {})
        summary = lovo.get("summary", {})
        self.assertGreater(summary.get("total_held_out_constraints", 0), 2000)
        self.assertGreater(summary["r4_heldout_pct"], summary["r0_raw_pct"])
        self.assertGreater(summary["r4_heldout_pct"], summary["r0_loo_pct"])
        self.assertGreaterEqual(summary["r4_heldout_pct"], summary["r1_unsup_pct"])

    def test_all_flagship_chains_pass(self):
        self.assertEqual(len(FLAGSHIP_ORDERING_CHAINS), 10)
        for chain in FLAGSHIP_ORDERING_CHAINS:
            for a, b in zip(chain, chain[1:]):
                self.assertIn(a, self.scores, f"Missing flagship model {a}")
                self.assertIn(b, self.scores, f"Missing flagship model {b}")
                self.assertGreater(
                    self.scores[a],
                    self.scores[b],
                    f"Flagship inversion: {a} ({self.scores[a]:.4f}) <= {b} ({self.scores[b]:.4f})",
                )


if __name__ == "__main__":
    unittest.main()
