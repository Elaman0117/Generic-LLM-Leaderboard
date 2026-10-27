# Standardized Benchmark Screening & Diagnostic Report

## 1. Candidate Benchmarks Scorecard (32 Candidates)

| # | Metric Key | Domain | Models | Coverage | Frontier Cov | Bounds [Low, High] | Span | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | `intelligenceIndex` | core_reasoning | 617 | 99.7% | 32/32 | [0.000, 1.000] | 1.000 | **PASS** |
| 2 | `hle` | core_reasoning | 616 | 99.5% | 32/32 | [0.000, 1.000] | 1.000 | **PASS** |
| 3 | `critpt` | math_stem | 588 | 95.0% | 32/32 | [0.024, 1.000] | 0.976 | **PASS** |
| 4 | `omniscience` | factuality | 588 | 95.0% | 32/32 | [0.020, 1.000] | 0.980 | **PASS** |
| 5 | `omniscienceAccuracy` | factuality | 588 | 95.0% | 32/32 | [0.014, 1.000] | 0.986 | **PASS** |
| 6 | `omniscienceNonHallucination` | factuality | 588 | 95.0% | 32/32 | [0.016, 1.000] | 0.984 | **PASS** |
| 7 | `lcr` | long_context | 586 | 94.7% | 32/32 | [0.000, 1.000] | 1.000 | **PASS** |
| 8 | `gpqa` | core_reasoning | 551 | 89.0% | 10/32 | [0.000, 0.995] | 0.995 | **PASS** |
| 9 | `ifbench` | factuality | 450 | 72.7% | 0/32 | [0.000, 0.909] | 0.909 | FAIL |
| 10 | `tau2` | agentic | 439 | 70.9% | 0/32 | [0.014, 0.896] | 0.882 | FAIL |
| 11 | `terminalbenchHard` | agentic | 432 | 69.8% | 0/32 | [0.018, 0.898] | 0.881 | FAIL |
| 12 | `gdpvalNormalized` | agentic | 307 | 49.6% | 32/32 | [0.035, 1.000] | 0.965 | **PASS** |
| 13 | `mmmuPro` | multimodal | 297 | 48.0% | 26/32 | [0.002, 1.000] | 0.998 | **PASS** |
| 14 | `livecodebench` | coding | 285 | 46.0% | 0/32 | [0.000, 0.718] | 0.718 | FAIL |
| 15 | `aime2025` | math_stem | 269 | 43.5% | 0/32 | [0.000, 0.726] | 0.726 | FAIL |
| 16 | `scicode` | coding | 243 | 39.3% | 32/32 | [0.035, 1.000] | 0.965 | **PASS** |
| 17 | `briefcase` | agentic | 243 | 39.3% | 32/32 | [0.035, 1.000] | 0.965 | **PASS** |
| 18 | `terminalbenchV21` | agentic | 242 | 39.1% | 10/32 | [0.034, 0.996] | 0.962 | **PASS** |
| 19 | `automationbench` | agentic | 235 | 38.0% | 32/32 | [0.035, 1.000] | 0.965 | **PASS** |
| 20 | `gdpPdf` | long_context | 234 | 37.8% | 32/32 | [0.033, 1.000] | 0.967 | **PASS** |
| 21 | `terminalbenchV40` | agentic | 232 | 37.5% | 32/32 | [0.035, 1.000] | 0.965 | **PASS** |
| 22 | `tauBanking` | agentic | 209 | 33.8% | 10/32 | [0.029, 1.000] | 0.971 | **PASS** |
| 23 | `mlcr` | long_context | 174 | 28.1% | 25/32 | [0.102, 1.000] | 0.898 | **PASS** |
| 24 | `terminalbenchScience` | agentic | 97 | 15.7% | 29/32 | [0.126, 1.000] | 0.874 | FAIL |
| 25 | `frontiercode` | coding | 77 | 12.4% | 29/32 | [0.127, 1.000] | 0.873 | FAIL |
| 26 | `analystAgent` | agentic | 51 | 8.2% | 10/32 | [0.288, 1.000] | 0.712 | FAIL |
| 27 | `enterpriseOps` | agentic | 50 | 8.1% | 6/32 | [0.306, 0.896] | 0.590 | FAIL |
| 28 | `itbenchSre` | agentic | 45 | 7.3% | 6/32 | [0.155, 1.000] | 0.845 | FAIL |
| 29 | `apexAgents` | agentic | 33 | 5.3% | 2/32 | [0.272, 0.829] | 0.557 | FAIL |
| 30 | `harveyLab` | agentic | 28 | 4.5% | 6/32 | [0.502, 1.000] | 0.498 | FAIL |
| 31 | `code2video` | multimodal | 27 | 4.4% | 11/32 | [0.482, 1.000] | 0.518 | FAIL |
| 32 | `aa3d` | multimodal | 23 | 3.7% | 9/32 | [0.483, 1.000] | 0.517 | FAIL |

## 2. Strategy Comparative Sanity Matrix

| Strategy | Metrics | Calibration Rounds | Inversion Anomaly | Top Model | Status |
|---|---|---|---|---|---|
| `stable_20` | 20 | 14 | Clean (0) | Claude Opus 5.5 (max with fallback) | **STABLE (VALID)** |
| `curated_balanced` | 20 | 15 | Clean (0) | Claude Opus 5.5 (max with fallback) | **STABLE (VALID)** |
| `curated_conservative` | 12 | 9 | Clean (0) | Claude Opus 5.5 (max with fallback) | **STABLE (VALID)** |
| `all_32` | 32 | 17 | YES (1 inversions) | GPT-6 Astra (xhigh) | **CHAOTIC (REJECTED)** |