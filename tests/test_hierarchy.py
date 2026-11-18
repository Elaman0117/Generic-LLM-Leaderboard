#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit and Regression Tests for Model Hierarchy Scoring Engine
===========================================================
"""

import json
import os
import shutil
import sys
import tempfile
import unittest

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
sys.path.insert(0, os.path.join(BASE_DIR, "src"))

from hierarchy import (
    BENCHMARK_DEFS,
    DEFAULT_SERIES_GRIDS,
    HierarchyScoreEngine,
    VendorHierarchyManager,
    extract_benchmarks,
    generate_hierarchy_constraints,
    parse_date_snapshot,
    parse_model_name,
    run_hierarchy_analysis,
)


class TestHierarchyModelParsing(unittest.TestCase):
    """Test model name parsing, thinking level categorization, and date snapshot extraction."""

    def test_thinking_level_extraction(self):
        cases = [
            ("GPT-6 Sol (max)", "GPT-6 Sol", "max", 6),
            ("GPT-6 Astra (xhigh)", "GPT-6 Astra", "xhigh", 5),
            ("GPT-6.1 Sol (high)", "GPT-6.1 Sol", "high", 4),
            ("Gemini 4 Carbon (medium)", "Gemini 4 Carbon", "medium", 3),
            ("GPT-6 Sol (low)", "GPT-6 Sol", "low", 2),
            ("GPT-5 nano (minimal)", "GPT-5 nano", "minimal", 1),
            ("GPT-6 Sol (non-reasoning)", "GPT-6 Sol", "non-reasoning", 0),
            ("Claude Opus 5.5 (max with fallback)", "Claude Opus 5.5", "max", 6),
            ("Claude Sonnet 4.6 (non-reasoning, high)", "Claude Sonnet 4.6", "non-reasoning", 0),
            ("Claude Sonnet 4.6 (non-reasoning, low)", "Claude Sonnet 4.6", "non-reasoning", 0),
            ("Claude Fable 5 (with fallback)", "Claude Fable 5", "reasoning", 4),
            ("GPT-6 Sol (Daybreak Blue, max)", "GPT-6 Sol (Daybreak Blue)", "max", 6),
            ("GPT-4o (May)", "GPT-4o (May)", "standard", 0),
            ("Gemini 1.5 Pro (Sep)", "Gemini 1.5 Pro (Sep)", "standard", 0),
        ]
        for full, exp_base, exp_tag, exp_lvl in cases:
            base, tag, lvl = parse_model_name(full)
            self.assertEqual(base, exp_base, f"Base name mismatch for {full}")
            self.assertEqual(tag, exp_tag, f"Thinking tag mismatch for {full}")
            self.assertEqual(lvl, exp_lvl, f"Thinking level mismatch for {full}")

    def test_date_snapshot_parsing(self):
        """Test parsing of date snapshot stamps across various model formats."""
        # Month in parentheses
        s1, dt1, d1 = parse_date_snapshot("Claude 3.5 Sonnet (June)", "2024-06-21")
        s2, dt2, d2 = parse_date_snapshot("Claude 3.5 Sonnet (Oct)", "2024-10-22")
        self.assertEqual(s1, s2, "Stems must match")
        self.assertEqual(s1, "Claude 3.5 Sonnet")
        self.assertLess(dt1, dt2, "June snapshot must be chronologically earlier than Oct snapshot")

        # Gemini Pro snapshots
        sp_may, dt_p_may, _ = parse_date_snapshot("Gemini 1.5 Pro (May)", "2024-05-15")
        sp_sep, dt_p_sep, _ = parse_date_snapshot("Gemini 1.5 Pro (Sep)", "2024-09-24")
        self.assertEqual(sp_may, sp_sep)
        self.assertLess(dt_p_may, dt_p_sep)

        # Gemini Flash snapshots
        sf_may, dt_f_may, _ = parse_date_snapshot("Gemini 1.5 Flash (May)", "2024-05-14")
        sf_sep, dt_f_sep, _ = parse_date_snapshot("Gemini 1.5 Flash (Sep)", "2024-09-24")
        self.assertEqual(sf_may, sf_sep)
        self.assertLess(dt_f_may, dt_f_sep)

        # 4-digit code snapshots
        s_ds_base, dt_ds_base, _ = parse_date_snapshot("DeepSeek V4 Pro", "2026-04-24")
        s_ds_0813, dt_ds_0813, _ = parse_date_snapshot("DeepSeek V4 Pro 0813", "2026-08-13")
        self.assertEqual(s_ds_base, s_ds_0813)
        self.assertLess(dt_ds_base, dt_ds_0813)

        # Sub-version snapshots
        s_grok1, dt_grok1, _ = parse_date_snapshot("Grok 4.20 0309", "2026-03-09")
        s_grok2, dt_grok2, _ = parse_date_snapshot("Grok 4.20 0309 v2", "2026-03-09")
        self.assertEqual(s_grok1, s_grok2)
        self.assertLess(dt_grok1, dt_grok2)


class TestHierarchyConstraintsRules(unittest.TestCase):
    """Test the core ordering rules (Series, Tiers, Versions, Thinking, Dates)."""

    def setUp(self):
        self.mgr = VendorHierarchyManager()

    def test_rule1_same_version_tier_ordering(self):
        """Rule 1: Same version, higher tier >= lower tier within same series."""
        pos_astra = self.mgr.get_model_position("OpenAI - GPT", "GPT-6 Astra")
        pos_sol = self.mgr.get_model_position("OpenAI - GPT", "GPT-6 Sol")

        self.assertIsNotNone(pos_astra)
        self.assertIsNotNone(pos_sol)
        # Astra tier rank (0) < Sol tier rank (1) means Astra is higher tier
        self.assertLess(pos_astra[0], pos_sol[0])
        # Same version index
        self.assertEqual(pos_astra[1], pos_sol[1])

    def test_rule2_same_tier_version_ordering(self):
        """Rule 2: Same tier, newer version >= older version within same series."""
        pos_sol_6 = self.mgr.get_model_position("OpenAI - GPT", "GPT-6 Sol")
        pos_sol_61 = self.mgr.get_model_position("OpenAI - GPT", "GPT-6.1 Sol")

        self.assertIsNotNone(pos_sol_6)
        self.assertIsNotNone(pos_sol_61)
        # Same tier
        self.assertEqual(pos_sol_6[0], pos_sol_61[0])
        # Newer version index (6.1 > 6)
        self.assertGreater(pos_sol_61[1], pos_sol_6[1])

    def test_gemini4_argon_carbon_same_tier_different_versions(self):
        """User special requirement:
        'Gemini 4有两个模型，是同等级但是是不同版本'
        """
        pos_argon = self.mgr.get_model_position("Google - Gemini", "Gemini 4 Argon")
        pos_carbon = self.mgr.get_model_position("Google - Gemini", "Gemini 4 Carbon")

        self.assertIsNotNone(pos_argon)
        self.assertIsNotNone(pos_carbon)
        # Same tier index
        self.assertEqual(pos_argon[0], pos_carbon[0], "Argon and Carbon must be same tier")
        # Different versions (Argon released before Carbon)
        self.assertNotEqual(pos_argon[1], pos_carbon[1], "Argon and Carbon must be different versions")
        self.assertLess(pos_argon[1], pos_carbon[1], "Argon is earlier version, Carbon is newer version")

    def test_new_models_hierarchy_integration(self):
        """Verify new frontier models are properly placed in their series hierarchy grids."""
        # GPT-6.2 Astra (Tier 1) vs GPT-6.2 Sol (Tier 2)
        pos_astra_62 = self.mgr.get_model_position("OpenAI - GPT", "GPT-6.2 Astra")
        pos_sol_62 = self.mgr.get_model_position("OpenAI - GPT", "GPT-6.2 Sol")
        pos_sol_61 = self.mgr.get_model_position("OpenAI - GPT", "GPT-6.1 Sol")
        self.assertIsNotNone(pos_astra_62)
        self.assertIsNotNone(pos_sol_62)
        self.assertLess(pos_astra_62[0], pos_sol_62[0], "GPT-6.2 Astra must be higher tier than GPT-6.2 Sol")
        self.assertEqual(pos_astra_62[1], pos_sol_62[1], "GPT-6.2 Astra and Sol must share version GPT-6.2")
        self.assertGreater(pos_sol_62[1], pos_sol_61[1], "GPT-6.2 Sol version must be newer than GPT-6.1 Sol")

        # Claude Fable 5.2 (Tier 2, Fable)
        pos_fable_52 = self.mgr.get_model_position("Anthropic - Claude", "Claude Fable 5.2")
        pos_fable_51 = self.mgr.get_model_position("Anthropic - Claude", "Claude Fable 5.1")
        self.assertIsNotNone(pos_fable_52)
        self.assertIsNotNone(pos_fable_51)
        self.assertEqual(pos_fable_52[0], pos_fable_51[0], "Fable 5.2 and 5.1 must share Fable tier")
        self.assertGreater(pos_fable_52[1], pos_fable_51[1], "Claude Fable 5.2 version must be newer than 5.1")

        # Qwen 4 Max (Tier 1, Max)
        pos_qwen4 = self.mgr.get_model_position("Alibaba - Qwen", "Qwen4 Max")
        pos_qwen38 = self.mgr.get_model_position("Alibaba - Qwen", "Qwen3.8 Max")
        self.assertIsNotNone(pos_qwen4)
        self.assertIsNotNone(pos_qwen38)
        self.assertEqual(pos_qwen4[0], pos_qwen38[0], "Qwen4 Max and Qwen3.8 Max must share Max tier")
        self.assertGreater(pos_qwen4[1], pos_qwen38[1], "Qwen4 Max version must be newer than Qwen3.8 Max")

        # Gemini 4 Neon (Tier 1) & Hydrogen (Tier 3)
        pos_neon = self.mgr.get_model_position("Google - Gemini", "Gemini 4 Neon")
        pos_hydrogen = self.mgr.get_model_position("Google - Gemini", "Gemini 4 Hydrogen")
        self.assertIsNotNone(pos_neon)
        self.assertIsNotNone(pos_hydrogen)
        self.assertEqual(pos_neon[0], 0, "Gemini 4 Neon must be Tier 1 (Ultra / Deep Think)")
        self.assertEqual(pos_hydrogen[0], 2, "Gemini 4 Hydrogen must be Tier 3 (Flash)")

        # Tencent Hy4
        pos_hy4 = self.mgr.get_model_position("Tencent - Hy", "Tencent Hy4")
        pos_hy3 = self.mgr.get_model_position("Tencent - Hy", "Hy3")
        self.assertIsNotNone(pos_hy4)
        self.assertIsNotNone(pos_hy3)
        self.assertEqual(pos_hy4[0], pos_hy3[0])
        self.assertGreater(pos_hy4[1], pos_hy3[1])

    def test_no_missing_evaluated_models_in_grids(self):
        """Assert that 100% of models evaluated by benchmark scoring are mapped to hierarchy grids."""
        with open(os.path.join(OUTPUT_DIR, "raw_data.json"), "r", encoding="utf-8") as f:
            raw_data = json.load(f)
        models, _ = extract_benchmarks(raw_data, min_valid=3)
        for m in models:
            bn = m["base_name"]
            series = self.mgr.get_model_series(bn)
            self.assertIsNotNone(series, f"Evaluated model '{m['name']}' (base: '{bn}') has no series grid mapping!")

    def test_series_isolation(self):
        """Verify strict series isolation: Rule 1 & Rule 2 NEVER cross between distinct series."""
        with open(os.path.join(OUTPUT_DIR, "raw_data.json"), "r", encoding="utf-8") as f:
            raw_data = json.load(f)
        models, _ = extract_benchmarks(raw_data)
        constraints, _ = generate_hierarchy_constraints(models, self.mgr)

        pairs = {(u, v) for u, v, _ in constraints}

        for u, v, reason in constraints:
            if "Rule 1" in reason or "Rule 2" in reason:
                u_base, _, _ = parse_model_name(u)
                v_base, _, _ = parse_model_name(v)
                u_series = self.mgr.get_model_series(u_base)
                v_series = self.mgr.get_model_series(v_base)
                if u_series and v_series:
                    self.assertEqual(
                        u_series, v_series,
                        f"Cross-series violation found under {reason}: {u} ({u_series}) vs {v} ({v_series})"
                    )

        # Explicitly check Google: Gemini vs Gemma must NEVER constrain each other
        gemini_names = {m["name"] for m in models if "Gemini" in m["base_name"]}
        gemma_names = {m["name"] for m in models if "Gemma" in m["base_name"]}
        for g_name in gemini_names:
            for gm_name in gemma_names:
                self.assertNotIn((g_name, gm_name), pairs, f"Gemini must not constrain Gemma: {g_name} >= {gm_name}")
                self.assertNotIn((gm_name, g_name), pairs, f"Gemma must not constrain Gemini: {gm_name} >= {g_name}")

        # Explicitly check OpenAI: GPT vs o vs GPT-OSS must NEVER constrain each other
        o_names = {m["name"] for m in models if m["base_name"].startswith(("o1", "o3", "o4"))}
        gpt_names = {m["name"] for m in models if m["base_name"].startswith(("GPT-4", "GPT-5", "GPT-6"))}
        oss_names = {m["name"] for m in models if "gpt-oss" in m["base_name"]}
        for o_n in o_names:
            for gpt_n in gpt_names:
                self.assertNotIn((o_n, gpt_n), pairs, f"'o' must not constrain GPT: {o_n} >= {gpt_n}")
                self.assertNotIn((gpt_n, o_n), pairs, f"GPT must not constrain 'o': {gpt_n} >= {o_n}")
            for oss_n in oss_names:
                self.assertNotIn((o_n, oss_n), pairs, f"'o' must not constrain GPT-OSS: {o_n} >= {oss_n}")
                self.assertNotIn((oss_n, o_n), pairs, f"GPT-OSS must not constrain 'o': {oss_n} >= {o_n}")

        # Explicitly check Meta: Llama vs Muse
        llama_names = {m["name"] for m in models if "Llama" in m["base_name"]}
        muse_names = {m["name"] for m in models if "Muse" in m["base_name"]}
        for l_n in llama_names:
            for m_n in muse_names:
                self.assertNotIn((l_n, m_n), pairs, f"Llama must not constrain Muse: {l_n} >= {m_n}")
                self.assertNotIn((m_n, l_n), pairs, f"Muse must not constrain Llama: {m_n} >= {l_n}")

    def test_date_checkpoint_ordering(self):
        """Rule 4: Newer date snapshot >= older date snapshot for the same model base stem."""
        with open(os.path.join(OUTPUT_DIR, "raw_data.json"), "r", encoding="utf-8") as f:
            raw_data = json.load(f)
        models, _ = extract_benchmarks(raw_data)
        constraints, stats = generate_hierarchy_constraints(models, self.mgr)
        pairs = {(u, v) for u, v, _ in constraints}

        self.assertGreater(stats["rule4_date"], 0, "Rule 4 constraints must be generated")

        # Gemini 1.5 Pro Sep >= May
        self.assertIn(("Gemini 1.5 Pro (Sep)", "Gemini 1.5 Pro (May)"), pairs)

        # Gemini 1.5 Flash Sep >= May
        self.assertIn(("Gemini 1.5 Flash (Sep)", "Gemini 1.5 Flash (May)"), pairs)

        # DeepSeek V4 Pro 0813 (max) >= DeepSeek V4 Pro (max)
        self.assertIn(("DeepSeek V4 Pro 0813 (max)", "DeepSeek V4 Pro (max)"), pairs)
        self.assertIn(("DeepSeek V4 Pro 0813 (non-reasoning)", "DeepSeek V4 Pro (non-reasoning)"), pairs)

        # DeepSeek V4 Flash 0731 (max) >= DeepSeek V4 Flash (max)
        self.assertIn(("DeepSeek V4 Flash 0731 (max)", "DeepSeek V4 Flash (max)"), pairs)

        # DeepSeek V3 0324 >= DeepSeek V3 (Dec)
        self.assertIn(("DeepSeek V3 0324", "DeepSeek V3 (Dec)"), pairs)

        # GPT-4o chronological
        self.assertIn(("GPT-4o (Nov)", "GPT-4o (Aug)"), pairs)
        self.assertIn(("GPT-4o (Aug)", "GPT-4o (May)"), pairs)

    def test_higher_tier_dominance_over_all_dated_checkpoints(self):
        """Task requirement:
        '有些时候不同日期的版本的同一个模型就是更高等级的比两个都强，然后新版比旧的强。'
        Within the same generation/version column, the higher-tier model is >= ALL date snapshots of lower-tier model.
        """
        with open(os.path.join(OUTPUT_DIR, "raw_data.json"), "r", encoding="utf-8") as f:
            raw_data = json.load(f)
        models, _ = extract_benchmarks(raw_data)
        constraints, _ = generate_hierarchy_constraints(models, self.mgr)
        pairs = {(u, v) for u, v, _ in constraints}

        # In Gemini 1.5: Pro (Tier 2) dominates ALL date snapshots of Flash (Tier 3)
        # 1. Higher tier beats newer date snapshot of lower tier:
        self.assertIn(("Gemini 1.5 Pro (May)", "Gemini 1.5 Flash (Sep)"), pairs,
                      "Gemini 1.5 Pro (May) must be >= Gemini 1.5 Flash (Sep)")
        # 2. Higher tier beats older date snapshot of lower tier:
        self.assertIn(("Gemini 1.5 Pro (May)", "Gemini 1.5 Flash (May)"), pairs)
        self.assertIn(("Gemini 1.5 Pro (Sep)", "Gemini 1.5 Flash (Sep)"), pairs)
        self.assertIn(("Gemini 1.5 Pro (Sep)", "Gemini 1.5 Flash (May)"), pairs)

        # In DeepSeek V4: Pro (Tier 1) dominates ALL date snapshots of Flash (Tier 2)
        # DeepSeek V4 Pro (max) >= DeepSeek V4 Flash 0731 (max)
        self.assertIn(("DeepSeek V4 Pro (max)", "DeepSeek V4 Flash 0731 (max)"), pairs)
        self.assertIn(("DeepSeek V4 Pro 0813 (max)", "DeepSeek V4 Flash 0731 (max)"), pairs)
        self.assertIn(("DeepSeek V4 Pro (max)", "DeepSeek V4 Flash (max)"), pairs)

    def test_rule1_unmatched_thinking_behavior(self):
        """Verify:
        Higher thinking of higher tier >= lower thinking of lower tier.
        Lower thinking of higher tier is NOT forced to beat higher thinking of lower tier.
        """
        mock_models = [
            {"name": "Top (high)", "base_name": "Top", "thinking_level": 4, "thinking_tag": "high", "creator": "TestVendor"},
            {"name": "Top (low)", "base_name": "Top", "thinking_level": 2, "thinking_tag": "low", "creator": "TestVendor"},
            {"name": "Bottom (medium)", "base_name": "Bottom", "thinking_level": 3, "thinking_tag": "medium", "creator": "TestVendor"},
            {"name": "Bottom (non-reasoning)", "base_name": "Bottom", "thinking_level": 0, "thinking_tag": "non-reasoning", "creator": "TestVendor"},
        ]

        test_mgr = VendorHierarchyManager()
        test_mgr.grids["TestVendor - SeriesA"] = {
            "vendor": "TestVendor",
            "series": "SeriesA",
            "versions": ["v1"],
            "tiers": ["Tier 1", "Tier 2"],
            "mapping": {
                "Tier 1": {"v1": ["Top"]},
                "Tier 2": {"v1": ["Bottom"]},
            }
        }

        constraints, _ = generate_hierarchy_constraints(mock_models, test_mgr)
        pairs = {(u, v) for u, v, _ in constraints}

        self.assertIn(("Top (high)", "Bottom (medium)"), pairs)
        self.assertIn(("Top (high)", "Bottom (non-reasoning)"), pairs)
        self.assertIn(("Top (low)", "Bottom (non-reasoning)"), pairs)
        self.assertNotIn(("Top (low)", "Bottom (medium)"), pairs)


class TestDykstraIsotonicEngine(unittest.TestCase):
    """Test the Dykstra projection engine on synthetic inversions."""

    def test_inversion_resolution(self):
        """If raw score of lower-tier model was higher than higher-tier model,
        Dykstra projection must resolve it so S(higher) >= S(lower).
        """
        models = [
            {
                "name": "Model_High",
                "base_name": "Model_High",
                "thinking_level": 6,
                "valid_count": 5,
                "calibrated_scores": {"m1": 0.40, "m2": 0.42},
            },
            {
                "name": "Model_Low",
                "base_name": "Model_Low",
                "thinking_level": 6,
                "valid_count": 5,
                "calibrated_scores": {"m1": 0.80, "m2": 0.85},
            }
        ]
        constraints = [("Model_High", "Model_Low", "Tier constraint")]
        engine = HierarchyScoreEngine(models, constraints)
        diag = engine.run_pipeline()

        self.assertEqual(diag["violations_count"], 0)
        self.assertEqual(diag["satisfaction_rate"], 100.0)
        score_high = models[0]["composite_ability"]
        score_low = models[1]["composite_ability"]
        self.assertGreaterEqual(score_high, score_low)


class TestEndToEndHierarchyAnalysis(unittest.TestCase):
    """End-to-end integration test running on full AA dataset."""

    def test_full_dataset_execution(self):
        diag = run_hierarchy_analysis(tolerance=1e-3)
        self.assertGreaterEqual(diag["total_models"], 600)
        self.assertGreaterEqual(diag["total_constraints"], 3000)
        self.assertEqual(diag["violations_count"], 0, "All constraints must be 100% satisfied")
        self.assertEqual(diag["satisfaction_rate"], 100.0)


class TestUserCSVEditingAndDiff(unittest.TestCase):
    """Test user modification of series CSV hierarchy files and diff reporting."""

    def test_custom_csv_override_and_diff(self):
        temp_dir = tempfile.mkdtemp()
        try:
            mgr_orig = VendorHierarchyManager(hierarchy_dir=temp_dir, load_from_disk=False)
            mgr_orig.export_all_csvs()

            openai_gpt_csv = os.path.join(temp_dir, "OpenAI - GPT.csv")
            self.assertTrue(os.path.exists(openai_gpt_csv), f"Expected {openai_gpt_csv} to exist")

            with open(openai_gpt_csv, "r", encoding="utf-8") as f:
                content = f.read()

            # Swap GPT-6 Sol into Tier 1
            modified_content = content.replace(
                "Tier 1 (Astra / Pro),,,,,,,,,GPT-5.4 Pro,GPT-5.5 Pro,,GPT-6 Astra,",
                "Tier 1 (Astra / Pro),,,,,,,,,GPT-5.4 Pro,GPT-5.5 Pro,,GPT-6 Astra / GPT-6 Sol,"
            ).replace(
                "GPT-6 Sol / GPT-6 Sol (Daybreak Blue)",
                "GPT-6 Sol (Daybreak Blue)"
            )
            with open(openai_gpt_csv, "w", encoding="utf-8") as f:
                f.write(modified_content)

            mgr_edited = VendorHierarchyManager(hierarchy_dir=temp_dir, load_from_disk=True)

            pos_sol = mgr_edited.get_model_position("OpenAI - GPT", "GPT-6 Sol")
            self.assertIsNotNone(pos_sol)
            self.assertEqual(pos_sol[0], 0, "GPT-6 Sol should now be in Tier 1 (rank 0)")

            diffs = mgr_edited.diff_with_default("OpenAI - GPT")
            self.assertTrue(any("GPT-6 Sol" in d and "moved" in d for d in diffs),
                            f"Diffs did not report GPT-6 Sol move: {diffs}")

            # Also verify vendor-level target diff
            diffs_vendor = mgr_edited.diff_with_default("OpenAI")
            self.assertTrue(any("GPT-6 Sol" in d and "moved" in d for d in diffs_vendor),
                            f"Vendor diff did not report GPT-6 Sol move: {diffs_vendor}")

        finally:
            shutil.rmtree(temp_dir)

    def test_openai_series_isolation_and_no_inversion(self):
        """Verify o1/o3/o4 are in their own isolated series ('OpenAI - o') and have no cross-constraints with GPT."""
        with open(os.path.join(OUTPUT_DIR, "raw_data.json"), "r", encoding="utf-8") as f:
            raw_data = json.load(f)
        models, _ = extract_benchmarks(raw_data)
        mgr = VendorHierarchyManager(all_models=models, load_from_disk=False)

        # Check separate series existence
        self.assertIn("OpenAI - o", mgr.grids)
        self.assertIn("OpenAI - GPT", mgr.grids)
        self.assertIn("OpenAI - GPT-OSS", mgr.grids)

        self.assertEqual(mgr.grids["OpenAI - o"]["versions"], ["o1", "o3", "o4"])
        self.assertIn("GPT-5", mgr.grids["OpenAI - GPT"]["versions"])
        self.assertIn("GPT-6", mgr.grids["OpenAI - GPT"]["versions"])

        constraints, stats = generate_hierarchy_constraints(models, mgr)

        # Ensure no cross-series constraints between o-series and GPT-series
        for u, v, _ in constraints:
            self.assertFalse(("o1" in u or "o3" in u or "o4" in u) and "GPT-6" in v,
                             f"Invalid cross-series constraint found: {u} >= {v}")
            self.assertFalse("GPT-6" in u and ("o1" in v or "o3" in v or "o4" in v),
                             f"Invalid cross-series constraint found: {u} >= {v}")

        # Check stats exact sum
        self.assertEqual(
            stats["rule1_tier"] + stats["rule2_version"] + stats["rule3_thinking"] + stats["rule4_date"],
            len(constraints),
            "Constraint stats sum must exactly match total unique constraints"
        )

        # Check total series grids count >= 50
        self.assertGreaterEqual(len(mgr.grids), 50, "All creators/series should have a grid")


if __name__ == "__main__":
    unittest.main()
