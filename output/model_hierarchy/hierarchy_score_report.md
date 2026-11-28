# Model Hierarchy & Monotonic Scoring Diagnostic Report

- **Total Evaluated Models**: 727 (Catalog Total: 768)
- **Series Hierarchy Grids**: 99
- **Benchmarks Mapped**: 38
- **Primary Scoring Method**: Zero-Leakage Monotone Benchmark Mapping (`src/mapping.py`, ZERO Dykstra label-clamping)
- **Strict Curve Monotonicity**: `True` (min slope `0.0500` >= `0.05`)
- **Total Constraints Evaluated**: 3140
- **Pure-Mapping Concordance**: 3089 / 3140 (98.38%)
- **Residual Genuine Inversions**: 51
- **LOVO Held-Out Generalization**: 98.55% across 2687 held-out pairs (R0_raw=86.71%, R0_LOO=93.15%, R1=98.40%)
- **Optional Post-Projection Reference (Dykstra, NOT used in primary scores)**: 3140 / 3140 (100.00%, 0 violations, converged in 11 epochs)

## Constraint Distribution & Pure-Mapping Concordance by Rule
1. **Rule 1 (Tier Ordering within same series & version)**: 586/607 (96.54%)
2. **Rule 2 (Version Ordering within same series & tier)**: 2050/2076 (98.75%)
3. **Rule 3 (Thinking Level Ordering within same model)**: 407/408 (99.75%)
4. **Rule 4 (Date Snapshot Ordering within same model stem)**: 46/49 (93.88%)

## Multi-Round Mapping Progression (Pure Benchmark Scores)

| Round | Method | Satisfied / Total | Concordance | Inversions | Rule 1 | Rule 2 | Rule 3 | Rule 4 |
|---|---|---|---|---|---|---|---|---|
| `round_0a` | Raw Min-Max Mean | 2687/3140 | **85.57%** | 453 | 90.1% | 84.5% | 86.8% | 63.3% |
| `round_0b` | LOO Linear Calibration | 2897/3140 | **92.26%** | 243 | 93.4% | 92.6% | 92.4% | 61.2% |
| `round_1` | Stage-1 Unsupervised Monotone Calibration | 3076/3140 | **97.96%** | 64 | 95.1% | 98.8% | 99.0% | 89.8% |
| `round_2` | Regularized Benchmark Weight Optimization | 3082/3140 | **98.15%** | 58 | 95.4% | 98.9% | 99.3% | 91.8% |
| `round_3` | Joint Monotone Curve + Weight Optimization | 3086/3140 | **98.28%** | 54 | 96.0% | 98.8% | 99.5% | 93.9% |
| `round_4a` | Pseudo-Huber IRLS Robust Aggregation | 3078/3140 | **98.03%** | 62 | 95.1% | 98.7% | 99.8% | 91.8% |
| `round_4b` | Huber/IRLS + Margin-Annealed Refinement | 3089/3140 | **98.38%** | 51 | 96.5% | 98.7% | 99.8% | 93.9% |

## Leave-One-Vendor-Out (LOVO) Cross-Validation

| Held-Out Vendor | Models | Held-Out Constraints | R0 Raw | R0 LOO | R1 Unsup | R4 Held-Out | vs R0 LOO |
|---|---|---|---|---|---|---|---|
| OpenAI | 113 | 948 | 89.03% | 95.04% | 99.05% | **99.26%** | +4.22% |
| Google | 74 | 482 | 86.93% | 92.74% | 98.96% | **98.76%** | +6.02% |
| Anthropic | 65 | 410 | 90.73% | 96.59% | 99.27% | **99.02%** | +2.44% |
| Alibaba | 87 | 449 | 88.86% | 92.87% | 96.88% | **97.77%** | +4.90% |
| DeepSeek | 36 | 143 | 72.03% | 79.72% | 97.20% | **97.20%** | +17.48% |
| Meta | 27 | 46 | 84.78% | 91.30% | 95.65% | **95.65%** | +4.35% |
| SpaceXAI | 27 | 146 | 72.60% | 87.67% | 96.58% | **96.58%** | +8.90% |
| Z AI | 23 | 63 | 76.19% | 92.06% | 98.41% | **98.41%** | +6.35% |
| **TOTAL LOVO** | — | **2687** | **86.71%** | **93.15%** | **98.40%** | **98.55%** | **+5.40%** |

## Flagship Ordering Chains

- **[PASS]** GPT-6.2 Astra (max) (0.9829) > GPT-6 Astra (max) (0.8757) > GPT-6 Astra (xhigh) (0.8467) > GPT-6 Astra (high) (0.8323) > GPT-6 Astra (medium) (0.8159)
- **[PASS]** GPT-6.2 Sol (max) (0.9472) > GPT-6.1 Sol (max) (0.8927) > GPT-6 Sol (max) (0.8105) > GPT-5.6 Sol (max) (0.7532)
- **[PASS]** GPT-6.2 Astra (max) (0.9829) > GPT-6.2 Sol (max) (0.9472)
- **[PASS]** Gemini 4 Neon (xhigh) (0.9640) > Gemini 4 Neon (high) (0.9553) > Gemini 4 Neon (medium) (0.9248)
- **[PASS]** Gemini 4 Carbon (high) (0.9440) > Gemini 4 Carbon (medium) (0.9258) > Gemini 4 Carbon (low) (0.8915)
- **[PASS]** Gemini 4 Carbon (high) (0.9440) > Gemini 4 Argon (high) (0.8471)
- **[PASS]** Claude Fable 5.2 (max) (1.0000) > Claude Fable 5.1 (max) (0.8527) > Claude Fable 5 (0.7376)
- **[PASS]** Claude Opus 5.5 (max) (0.9211) > Claude Opus 5.5 (xhigh) (0.9007) > Claude Opus 5.5 (high) (0.8647) > Claude Opus 5.5 (medium) (0.8359)
- **[PASS]** Grok 4.3 (high) (0.4925) > Grok 4.3 (medium) (0.4874)
- **[PASS]** MiniMax-M2.7 (0.4723) > MiniMax-M2.5 (0.4340)

## Top 30 Models by Pure Benchmark-Mapped Score

| Rank | Model | Creator | Thinking | Final Score (100) | Raw Avg | Mode |
|---|---|---|---|---|---|---|
| 1 | `Claude Fable 5.2 (max)` | Anthropic | max | **100.00** | 0.9324 | PURE-MAP |
| 2 | `GPT-6.2 Astra (max)` | OpenAI | max | **98.29** | 0.8885 | PURE-MAP |
| 3 | `Claude Fable 5.2 (xhigh)` | Anthropic | xhigh | **96.64** | 0.8955 | PURE-MAP |
| 4 | `Gemini 4 Neon (xhigh)` | Google | xhigh | **96.40** | 0.8775 | PURE-MAP |
| 5 | `GPT-6.2 Astra (xhigh)` | OpenAI | xhigh | **96.16** | 0.8568 | PURE-MAP |
| 6 | `Gemini 4 Neon (high)` | Google | high | **95.53** | 0.8776 | PURE-MAP |
| 7 | `GPT-6.2 Astra (high)` | OpenAI | high | **95.16** | 0.8445 | PURE-MAP |
| 8 | `Claude Fable 5.2 (high)` | Anthropic | high | **94.98** | 0.8844 | PURE-MAP |
| 9 | `GPT-6.2 Sol (max)` | OpenAI | max | **94.72** | 0.8304 | PURE-MAP |
| 10 | `Gemini 4 Carbon (high)` | Google | high | **94.40** | 0.8589 | PURE-MAP |
| 11 | `Gemini 4 Carbon (medium)` | Google | medium | **92.58** | 0.8503 | PURE-MAP |
| 12 | `Gemini 4 Neon (medium)` | Google | medium | **92.48** | 0.8350 | PURE-MAP |
| 13 | `Claude Opus 5.5 (max)` | Anthropic | max | **92.11** | 0.8542 | PURE-MAP |
| 14 | `GPT-6.2 Astra (medium)` | OpenAI | medium | **91.64** | 0.8002 | PURE-MAP |
| 15 | `GPT-6.2 Sol (xhigh)` | OpenAI | xhigh | **91.58** | 0.7836 | PURE-MAP |
| 16 | `Gemini 4 Hydrogen (xhigh)` | Google | xhigh | **91.50** | 0.8106 | PURE-MAP |
| 17 | `Claude Fable 5.2 (medium)` | Anthropic | medium | **91.32** | 0.8526 | PURE-MAP |
| 18 | `GPT-6.2 Sol (high)` | OpenAI | high | **90.87** | 0.7703 | PURE-MAP |
| 19 | `Claude Opus 5.5 (xhigh)` | Anthropic | xhigh | **90.07** | 0.8421 | PURE-MAP |
| 20 | `Claude Sonnet 5.5 (max)` | Anthropic | max | **89.37** | 0.8366 | PURE-MAP |
| 21 | `GPT-6.2 Sol (medium)` | OpenAI | medium | **89.32** | 0.7459 | PURE-MAP |
| 22 | `Claude Fable 5.2 (low)` | Anthropic | low | **89.29** | 0.8312 | PURE-MAP |
| 23 | `GPT-6.1 Sol (max)` | OpenAI | max | **89.27** | 0.8337 | PURE-MAP |
| 24 | `Gemini 4 Carbon (low)` | Google | low | **89.15** | 0.7865 | PURE-MAP |
| 25 | `Gemini 4 Hydrogen (high)` | Google | high | **89.05** | 0.7882 | PURE-MAP |
| 26 | `GPT-6 Astra (max)` | OpenAI | max | **87.57** | 0.8528 | PURE-MAP |
| 27 | `Claude Opus 5.5 (high)` | Anthropic | high | **86.47** | 0.7910 | PURE-MAP |
| 28 | `GPT-6.1 Sol (xhigh)` | OpenAI | xhigh | **86.36** | 0.8121 | PURE-MAP |
| 29 | `Muse Wonder Full (max)` | Meta | max | **85.97** | 0.8036 | PURE-MAP |
| 30 | `Gemini 4 Neon (low)` | Google | low | **85.74** | 0.7303 | PURE-MAP |

## Top Genuine Residual Data Inversions

| Higher Model | Lower Model | Score Higher | Score Lower | Diff | Reason |
|---|---|---|---|---|---|
| `Mistral Small 4 (non-reasoning)` | `Mistral Small 3.1` | 0.1581 | 0.2220 | -0.0639 | Rule 2: Series [Mistral - Mistral] tier [Tier 3 (Small / 7B)] Mistral v4 > Mistral v3.1 [matching thinking non-reasoning] |
| `GLM-5.2 (non-reasoning)` | `GLM-5.1 (non-reasoning)` | 0.3605 | 0.4187 | -0.0582 | Rule 2: Series [Z_AI - GLM] tier [Tier 1 (Flagship / Pro)] GLM-5.2 > GLM-5.1 [matching thinking non-reasoning] |
| `Mistral Small 3.2` | `Mistral Small 3.1` | 0.1676 | 0.2220 | -0.0544 | Rule 2: Series [Mistral - Mistral] tier [Tier 3 (Small / 7B)] Mistral v3.2 > Mistral v3.1 [matching thinking standard] |
| `Muse Spark 1.1 (xhigh)` | `Muse Spark Open (xhigh)` | 0.5952 | 0.6466 | -0.0514 | Rule 2: Series [Meta - Muse] tier [Tier 2 (Spark)] Muse 1.1 > Muse 1.0 [matching thinking xhigh] |
| `DeepSeek V4 Pro (max)` | `DeepSeek V4 Flash 0731 (max)` | 0.5711 | 0.6169 | -0.0458 | Rule 1: Series [DeepSeek - DeepSeek-V] version [DeepSeek V4] Tier 1 (Pro / Full) > Tier 2 (Flash) [matching thinking max] |
| `Ling-3.2-air` | `Ling 3.1 Flash 1019` | 0.6563 | 0.6982 | -0.0418 | Rule 2: Series [InclusionAI - Ling] tier [Tier 3 (Flash)] 2025-01 > Ling 3.1 [matching thinking reasoning] |
| `Mixtral 8x7B` | `Mistral Small (Sep)` | 0.0378 | 0.0776 | -0.0398 | Rule 1: Series [Mistral - Mistral] version [Mistral v1] Tier 2 (Medium) > Tier 3 (Small / 7B) [matching thinking standard] |
| `Gemini 2.5 Flash (Apr) (non-reasoning)` | `Gemini 2.5 Flash-Lite (Sep) (non-reasoning)` | 0.1946 | 0.2308 | -0.0362 | Rule 1: Series [Google - Gemini] version [Gemini 2.5] Tier 3 (Flash) > Tier 4 (Flash-Lite / Nano) [matching thinking non-reasoning] |
| `Claude 4 Opus (non-reasoning)` | `Claude 4 Sonnet (non-reasoning)` | 0.2278 | 0.2594 | -0.0317 | Rule 1: Series [Anthropic - Claude] version [Claude 4] Tier 2 (Opus) > Tier 3 (Sonnet) [matching thinking non-reasoning] |
| `DeepSeek V3.2 Exp` | `DeepSeek V3.1 Terminus` | 0.3492 | 0.3808 | -0.0315 | Rule 2: Series [DeepSeek - DeepSeek-V] tier [Tier 1 (Pro / Full)] DeepSeek V3.2 > DeepSeek V3.1 Terminus [matching thinking reasoning] |
| `Nemotron 3 Nano (non-reasoning)` | `NVIDIA Nemotron Nano 9B V2 (non-reasoning)` | 0.1395 | 0.1674 | -0.0279 | Rule 2: Series [NVIDIA - Nemotron] tier [Tier 3 (Nano 9B / 3 Nano / Lightning)] Nemotron 3 > Nemotron 2 [matching thinking non-reasoning] |
| `DeepSeek V4 Pro (max)` | `DeepSeek V4 Flash Vision (max)` | 0.5711 | 0.5988 | -0.0277 | Rule 1: Series [DeepSeek - DeepSeek-V] version [DeepSeek V4] Tier 1 (Pro / Full) > Tier 2 (Flash) [matching thinking max] |
| `Mistral Medium` | `Mistral Small (Sep)` | 0.0575 | 0.0776 | -0.0201 | Rule 1: Series [Mistral - Mistral] version [Mistral v1] Tier 2 (Medium) > Tier 3 (Small / 7B) [matching thinking standard] |
| `Qwen3 30B` | `Qwen3 14B` | 0.1864 | 0.2049 | -0.0185 | Rule 1: Series [Alibaba - Qwen] version [Qwen 3] Tier 5 (MoE Mid: 35B-30B A3B) > Tier 6 (Small: 14B-4B) [matching thinking reasoning] |
| `DeepSeek R1 Distill Llama 70B` | `DeepSeek R1 Distill Qwen 14B` | 0.1096 | 0.1279 | -0.0183 | Rule 1: Series [DeepSeek - DeepSeek-R] version [DeepSeek R1] Tier 2 (Distill 70B / 32B) > Tier 3 (Distill 14B / 8B / 1.5B) [matching thinking reasoning] |
| `Nova 2.0 Omni (medium)` | `Nova 2.0 Lite (medium)` | 0.2844 | 0.3016 | -0.0171 | Rule 1: Series [Amazon - Nova] version [Nova 2.0] Tier 1 (Omni / Pro / Premier) > Tier 2 (Lite) [matching thinking medium] |
| `GPT-5.1 Codex (high)` | `GPT-5 Codex (high)` | 0.4362 | 0.4513 | -0.0151 | Rule 2: Series [OpenAI - GPT-Codex] tier [Tier 1 (Codex)] GPT-5.1 > GPT-5 [matching thinking high] |
| `Grok 4.3 (high)` | `Grok 4.20 0309 v2` | 0.4925 | 0.5076 | -0.0151 | Rule 2: Series [SpaceXAI - Grok] tier [Tier 1 (Full / Flagship)] Grok 4.3 > Grok 4.20 [matching thinking high] |
| `Ling-3.2-air` | `Ling 3.1 Flash` | 0.6563 | 0.6711 | -0.0147 | Rule 2: Series [InclusionAI - Ling] tier [Tier 3 (Flash)] 2025-01 > Ling 3.1 [matching thinking reasoning] |
| `Gemini 1.5 Pro (May)` | `Gemini 1.5 Flash (Sep)` | 0.0947 | 0.1080 | -0.0132 | Rule 1: Series [Google - Gemini] version [Gemini 1.5] Tier 2 (Pro) > Tier 3 (Flash) [matching thinking standard] |
| `Mixtral 8x7B` | `Mistral Small (Feb)` | 0.0378 | 0.0504 | -0.0126 | Rule 1: Series [Mistral - Mistral] version [Mistral v1] Tier 2 (Medium) > Tier 3 (Small / 7B) [matching thinking standard] |
| `Qwen3 32B (non-reasoning)` | `Qwen2.5 72B` | 0.1277 | 0.1381 | -0.0104 | Rule 2: Series [Alibaba - Qwen] tier [Tier 3 (Dense Large: 110B-27B)] Qwen 3 > Qwen 2.5 [matching thinking non-reasoning] |
| `Motif 3` | `Motif 3 (Beta)` | 0.5339 | 0.5438 | -0.0099 | Rule 2: Series [Motif Technologies - Motif] tier [Tier 2 (Medium / MoE)] 2026-08 > 2026-07 [matching thinking reasoning] |
| `Qwen3.5 0.8B` | `Qwen3.5 0.8B (non-reasoning)` | 0.0586 | 0.0684 | -0.0098 | Rule 3: Same model [Qwen3.5 0.8B] higher thinking (reasoning > non-reasoning) |
| `LFM2.5-8B-A1B` | `LFM2.5-2.6B` | 0.1559 | 0.1656 | -0.0097 | Rule 1: Series [Liquid AI - LFM] version [LFM 2.5] Tier 3 (Small: 8B) > Tier 4 (Compact: 2.6B-1.7B) [matching thinking reasoning] |
