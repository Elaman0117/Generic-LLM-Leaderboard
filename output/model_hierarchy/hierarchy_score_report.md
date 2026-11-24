# Model Hierarchy & Monotonic Scoring Diagnostic Report

- **Total Evaluated Models**: 725 (Catalog Total: 766)
- **Series Hierarchy Grids**: 99
- **Benchmarks Mapped**: 38
- **Primary Scoring Method**: Zero-Leakage Monotone Benchmark Mapping (`src/mapping.py`, ZERO Dykstra label-clamping)
- **Strict Curve Monotonicity**: `True` (min slope `0.0500` >= `0.05`)
- **Total Constraints Evaluated**: 3139
- **Pure-Mapping Concordance**: 3087 / 3139 (98.34%)
- **Residual Genuine Inversions**: 52
- **LOVO Held-Out Generalization**: 98.55% across 2687 held-out pairs (R0_raw=86.68%, R0_LOO=93.19%, R1=98.36%)
- **Optional Post-Projection Reference (Dykstra, NOT used in primary scores)**: 3139 / 3139 (100.00%, 0 violations, converged in 11 epochs)

## Constraint Distribution & Pure-Mapping Concordance by Rule
1. **Rule 1 (Tier Ordering within same series & version)**: 586/607 (96.54%)
2. **Rule 2 (Version Ordering within same series & tier)**: 2049/2075 (98.75%)
3. **Rule 3 (Thinking Level Ordering within same model)**: 407/408 (99.75%)
4. **Rule 4 (Date Snapshot Ordering within same model stem)**: 45/49 (91.84%)

## Multi-Round Mapping Progression (Pure Benchmark Scores)

| Round | Method | Satisfied / Total | Concordance | Inversions | Rule 1 | Rule 2 | Rule 3 | Rule 4 |
|---|---|---|---|---|---|---|---|---|
| `round_0a` | Raw Min-Max Mean | 2685/3139 | **85.54%** | 454 | 90.0% | 84.5% | 86.8% | 63.3% |
| `round_0b` | LOO Linear Calibration | 2898/3139 | **92.32%** | 241 | 93.4% | 92.7% | 92.6% | 61.2% |
| `round_1` | Stage-1 Unsupervised Monotone Calibration | 3074/3139 | **97.93%** | 65 | 95.1% | 98.8% | 98.8% | 89.8% |
| `round_2` | Regularized Benchmark Weight Optimization | 3081/3139 | **98.15%** | 58 | 95.4% | 98.9% | 99.0% | 91.8% |
| `round_3` | Joint Monotone Curve + Weight Optimization | 3085/3139 | **98.28%** | 54 | 96.0% | 98.8% | 99.5% | 93.9% |
| `round_4a` | Pseudo-Huber IRLS Robust Aggregation | 3077/3139 | **98.02%** | 62 | 95.1% | 98.7% | 99.8% | 91.8% |
| `round_4b` | Huber/IRLS + Margin-Annealed Refinement | 3087/3139 | **98.34%** | 52 | 96.5% | 98.7% | 99.8% | 91.8% |

## Leave-One-Vendor-Out (LOVO) Cross-Validation

| Held-Out Vendor | Models | Held-Out Constraints | R0 Raw | R0 LOO | R1 Unsup | R4 Held-Out | vs R0 LOO |
|---|---|---|---|---|---|---|---|
| OpenAI | 113 | 948 | 89.03% | 95.04% | 99.05% | **99.26%** | +4.22% |
| Google | 74 | 482 | 86.72% | 92.95% | 98.76% | **98.76%** | +5.81% |
| Anthropic | 65 | 410 | 90.73% | 96.59% | 99.27% | **99.02%** | +2.44% |
| Alibaba | 87 | 449 | 88.86% | 92.87% | 96.88% | **97.77%** | +4.90% |
| DeepSeek | 36 | 143 | 72.03% | 79.72% | 97.20% | **97.20%** | +17.48% |
| Meta | 27 | 46 | 84.78% | 91.30% | 95.65% | **95.65%** | +4.35% |
| SpaceXAI | 27 | 146 | 72.60% | 87.67% | 96.58% | **96.58%** | +8.90% |
| Z AI | 23 | 63 | 76.19% | 92.06% | 98.41% | **98.41%** | +6.35% |
| **TOTAL LOVO** | — | **2687** | **86.68%** | **93.19%** | **98.36%** | **98.55%** | **+5.36%** |

## Flagship Ordering Chains

- **[PASS]** GPT-6.2 Astra (max) (0.9831) > GPT-6 Astra (max) (0.8761) > GPT-6 Astra (xhigh) (0.8472) > GPT-6 Astra (high) (0.8328) > GPT-6 Astra (medium) (0.8163)
- **[PASS]** GPT-6.2 Sol (max) (0.9472) > GPT-6.1 Sol (max) (0.8927) > GPT-6 Sol (max) (0.8103) > GPT-5.6 Sol (max) (0.7526)
- **[PASS]** GPT-6.2 Astra (max) (0.9831) > GPT-6.2 Sol (max) (0.9472)
- **[PASS]** Gemini 4 Neon (xhigh) (0.9642) > Gemini 4 Neon (high) (0.9552) > Gemini 4 Neon (medium) (0.9246)
- **[PASS]** Gemini 4 Carbon (high) (0.9346) > Gemini 4 Carbon (medium) (0.9254) > Gemini 4 Carbon (low) (0.8904)
- **[PASS]** Gemini 4 Carbon (high) (0.9346) > Gemini 4 Argon (high) (0.8464)
- **[PASS]** Claude Fable 5.2 (max) (1.0000) > Claude Fable 5.1 (max) (0.8522) > Claude Fable 5 (0.7370)
- **[PASS]** Claude Opus 5.5 (max) (0.9206) > Claude Opus 5.5 (xhigh) (0.8999) > Claude Opus 5.5 (high) (0.8643) > Claude Opus 5.5 (medium) (0.8353)
- **[PASS]** Grok 4.3 (high) (0.4914) > Grok 4.3 (medium) (0.4864)
- **[PASS]** MiniMax-M2.7 (0.4712) > MiniMax-M2.5 (0.4331)

## Top 30 Models by Pure Benchmark-Mapped Score

| Rank | Model | Creator | Thinking | Final Score (100) | Raw Avg | Mode |
|---|---|---|---|---|---|---|
| 1 | `Claude Fable 5.2 (max)` | Anthropic | max | **100.00** | 0.9324 | PURE-MAP |
| 2 | `GPT-6.2 Astra (max)` | OpenAI | max | **98.31** | 0.8886 | PURE-MAP |
| 3 | `Claude Fable 5.2 (xhigh)` | Anthropic | xhigh | **96.61** | 0.8956 | PURE-MAP |
| 4 | `Gemini 4 Neon (xhigh)` | Google | xhigh | **96.42** | 0.8775 | PURE-MAP |
| 5 | `GPT-6.2 Astra (xhigh)` | OpenAI | xhigh | **96.13** | 0.8568 | PURE-MAP |
| 6 | `Gemini 4 Neon (high)` | Google | high | **95.52** | 0.8776 | PURE-MAP |
| 7 | `GPT-6.2 Astra (high)` | OpenAI | high | **95.13** | 0.8445 | PURE-MAP |
| 8 | `Claude Fable 5.2 (high)` | Anthropic | high | **94.95** | 0.8845 | PURE-MAP |
| 9 | `GPT-6.2 Sol (max)` | OpenAI | max | **94.72** | 0.8306 | PURE-MAP |
| 10 | `Gemini 4 Carbon (high)` | Google | high | **93.46** | 0.8609 | PURE-MAP |
| 11 | `Gemini 4 Carbon (medium)` | Google | medium | **92.54** | 0.8504 | PURE-MAP |
| 12 | `Gemini 4 Neon (medium)` | Google | medium | **92.46** | 0.8351 | PURE-MAP |
| 13 | `Claude Opus 5.5 (max)` | Anthropic | max | **92.06** | 0.8540 | PURE-MAP |
| 14 | `GPT-6.2 Astra (medium)` | OpenAI | medium | **91.62** | 0.8004 | PURE-MAP |
| 15 | `GPT-6.2 Sol (xhigh)` | OpenAI | xhigh | **91.57** | 0.7838 | PURE-MAP |
| 16 | `Gemini 4 Hydrogen (xhigh)` | Google | xhigh | **91.46** | 0.8106 | PURE-MAP |
| 17 | `Claude Fable 5.2 (medium)` | Anthropic | medium | **91.32** | 0.8528 | PURE-MAP |
| 18 | `GPT-6.2 Sol (high)` | OpenAI | high | **90.84** | 0.7705 | PURE-MAP |
| 19 | `Claude Opus 5.5 (xhigh)` | Anthropic | xhigh | **89.99** | 0.8417 | PURE-MAP |
| 20 | `GPT-6.2 Sol (medium)` | OpenAI | medium | **89.32** | 0.7463 | PURE-MAP |
| 21 | `Claude Sonnet 5.5 (max)` | Anthropic | max | **89.30** | 0.8364 | PURE-MAP |
| 22 | `Claude Fable 5.2 (low)` | Anthropic | low | **89.28** | 0.8313 | PURE-MAP |
| 23 | `GPT-6.1 Sol (max)` | OpenAI | max | **89.27** | 0.8338 | PURE-MAP |
| 24 | `Gemini 4 Carbon (low)` | Google | low | **89.04** | 0.7868 | PURE-MAP |
| 25 | `Gemini 4 Hydrogen (high)` | Google | high | **88.99** | 0.7881 | PURE-MAP |
| 26 | `GPT-6 Astra (max)` | OpenAI | max | **87.61** | 0.8529 | PURE-MAP |
| 27 | `Claude Opus 5.5 (high)` | Anthropic | high | **86.43** | 0.7911 | PURE-MAP |
| 28 | `GPT-6.1 Sol (xhigh)` | OpenAI | xhigh | **86.38** | 0.8123 | PURE-MAP |
| 29 | `Muse Wonder Full (max)` | Meta | max | **85.94** | 0.8038 | PURE-MAP |
| 30 | `Gemini 4 Neon (low)` | Google | low | **85.74** | 0.7304 | PURE-MAP |

## Top Genuine Residual Data Inversions

| Higher Model | Lower Model | Score Higher | Score Lower | Diff | Reason |
|---|---|---|---|---|---|
| `Mistral Small 4 (non-reasoning)` | `Mistral Small 3.1` | 0.1579 | 0.2220 | -0.0641 | Rule 2: Series [Mistral - Mistral] tier [Tier 3 (Small / 7B)] Mistral v4 > Mistral v3.1 [matching thinking non-reasoning] |
| `GLM-5.2 (non-reasoning)` | `GLM-5.1 (non-reasoning)` | 0.3602 | 0.4182 | -0.0581 | Rule 2: Series [Z_AI - GLM] tier [Tier 1 (Flagship / Pro)] GLM-5.2 > GLM-5.1 [matching thinking non-reasoning] |
| `Mistral Small 3.2` | `Mistral Small 3.1` | 0.1676 | 0.2220 | -0.0544 | Rule 2: Series [Mistral - Mistral] tier [Tier 3 (Small / 7B)] Mistral v3.2 > Mistral v3.1 [matching thinking standard] |
| `Muse Spark 1.1 (xhigh)` | `Muse Spark Open (xhigh)` | 0.5943 | 0.6455 | -0.0512 | Rule 2: Series [Meta - Muse] tier [Tier 2 (Spark)] Muse 1.1 > Muse 1.0 [matching thinking xhigh] |
| `DeepSeek V4 Pro (max)` | `DeepSeek V4 Flash 0731 (max)` | 0.5702 | 0.6158 | -0.0456 | Rule 1: Series [DeepSeek - DeepSeek-V] version [DeepSeek V4] Tier 1 (Pro / Full) > Tier 2 (Flash) [matching thinking max] |
| `Ling-3.2-air` | `Ling 3.1 Flash 1019` | 0.6543 | 0.6958 | -0.0415 | Rule 2: Series [InclusionAI - Ling] tier [Tier 3 (Flash)] 2025-01 > Ling 3.1 [matching thinking reasoning] |
| `Mixtral 8x7B` | `Mistral Small (Sep)` | 0.0380 | 0.0776 | -0.0397 | Rule 1: Series [Mistral - Mistral] version [Mistral v1] Tier 2 (Medium) > Tier 3 (Small / 7B) [matching thinking standard] |
| `Gemini 2.5 Flash (Apr) (non-reasoning)` | `Gemini 2.5 Flash-Lite (Sep) (non-reasoning)` | 0.1944 | 0.2304 | -0.0360 | Rule 1: Series [Google - Gemini] version [Gemini 2.5] Tier 3 (Flash) > Tier 4 (Flash-Lite / Nano) [matching thinking non-reasoning] |
| `Claude 4 Opus (non-reasoning)` | `Claude 4 Sonnet (non-reasoning)` | 0.2275 | 0.2591 | -0.0316 | Rule 1: Series [Anthropic - Claude] version [Claude 4] Tier 2 (Opus) > Tier 3 (Sonnet) [matching thinking non-reasoning] |
| `DeepSeek V3.2 Exp` | `DeepSeek V3.1 Terminus` | 0.3486 | 0.3799 | -0.0313 | Rule 2: Series [DeepSeek - DeepSeek-V] tier [Tier 1 (Pro / Full)] DeepSeek V3.2 > DeepSeek V3.1 Terminus [matching thinking reasoning] |
| `Nemotron 3 Nano (non-reasoning)` | `NVIDIA Nemotron Nano 9B V2 (non-reasoning)` | 0.1395 | 0.1673 | -0.0278 | Rule 2: Series [NVIDIA - Nemotron] tier [Tier 3 (Nano 9B / 3 Nano / Lightning)] Nemotron 3 > Nemotron 2 [matching thinking non-reasoning] |
| `DeepSeek V4 Pro (max)` | `DeepSeek V4 Flash Vision (max)` | 0.5702 | 0.5977 | -0.0275 | Rule 1: Series [DeepSeek - DeepSeek-V] version [DeepSeek V4] Tier 1 (Pro / Full) > Tier 2 (Flash) [matching thinking max] |
| `Mistral Medium` | `Mistral Small (Sep)` | 0.0575 | 0.0776 | -0.0201 | Rule 1: Series [Mistral - Mistral] version [Mistral v1] Tier 2 (Medium) > Tier 3 (Small / 7B) [matching thinking standard] |
| `Qwen3 30B` | `Qwen3 14B` | 0.1864 | 0.2050 | -0.0186 | Rule 1: Series [Alibaba - Qwen] version [Qwen 3] Tier 5 (MoE Mid: 35B-30B A3B) > Tier 6 (Small: 14B-4B) [matching thinking reasoning] |
| `DeepSeek R1 Distill Llama 70B` | `DeepSeek R1 Distill Qwen 14B` | 0.1096 | 0.1280 | -0.0183 | Rule 1: Series [DeepSeek - DeepSeek-R] version [DeepSeek R1] Tier 2 (Distill 70B / 32B) > Tier 3 (Distill 14B / 8B / 1.5B) [matching thinking reasoning] |
| `Nova 2.0 Omni (medium)` | `Nova 2.0 Lite (medium)` | 0.2837 | 0.3009 | -0.0172 | Rule 1: Series [Amazon - Nova] version [Nova 2.0] Tier 1 (Omni / Pro / Premier) > Tier 2 (Lite) [matching thinking medium] |
| `Ling-3.2-air` | `Ling 3.1 Flash` | 0.6543 | 0.6698 | -0.0155 | Rule 2: Series [InclusionAI - Ling] tier [Tier 3 (Flash)] 2025-01 > Ling 3.1 [matching thinking reasoning] |
| `Grok 4.3 (high)` | `Grok 4.20 0309 v2` | 0.4914 | 0.5068 | -0.0154 | Rule 2: Series [SpaceXAI - Grok] tier [Tier 1 (Full / Flagship)] Grok 4.3 > Grok 4.20 [matching thinking high] |
| `GPT-5.1 Codex (high)` | `GPT-5 Codex (high)` | 0.4354 | 0.4505 | -0.0151 | Rule 2: Series [OpenAI - GPT-Codex] tier [Tier 1 (Codex)] GPT-5.1 > GPT-5 [matching thinking high] |
| `Gemini 1.5 Pro (May)` | `Gemini 1.5 Flash (Sep)` | 0.0947 | 0.1079 | -0.0132 | Rule 1: Series [Google - Gemini] version [Gemini 1.5] Tier 2 (Pro) > Tier 3 (Flash) [matching thinking standard] |
| `Mixtral 8x7B` | `Mistral Small (Feb)` | 0.0380 | 0.0505 | -0.0126 | Rule 1: Series [Mistral - Mistral] version [Mistral v1] Tier 2 (Medium) > Tier 3 (Small / 7B) [matching thinking standard] |
| `Motif 3` | `Motif 3 (Beta)` | 0.5325 | 0.5429 | -0.0104 | Rule 2: Series [Motif Technologies - Motif] tier [Tier 2 (Medium / MoE)] 2026-08 > 2026-07 [matching thinking reasoning] |
| `Qwen3 32B (non-reasoning)` | `Qwen2.5 72B` | 0.1278 | 0.1379 | -0.0102 | Rule 2: Series [Alibaba - Qwen] tier [Tier 3 (Dense Large: 110B-27B)] Qwen 3 > Qwen 2.5 [matching thinking non-reasoning] |
| `Qwen3.5 0.8B` | `Qwen3.5 0.8B (non-reasoning)` | 0.0585 | 0.0683 | -0.0098 | Rule 3: Same model [Qwen3.5 0.8B] higher thinking (reasoning > non-reasoning) |
| `Mistral Small 4 (non-reasoning)` | `Mistral Small 3.2` | 0.1579 | 0.1676 | -0.0097 | Rule 2: Series [Mistral - Mistral] tier [Tier 3 (Small / 7B)] Mistral v4 > Mistral v3.2 [matching thinking non-reasoning] |
