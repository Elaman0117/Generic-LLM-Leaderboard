# Model Hierarchy & Monotonic Scoring Diagnostic Report

- **Total Evaluated Models**: 723 (Catalog Total: 763)
- **Series Hierarchy Grids**: 99
- **Benchmarks Mapped**: 38
- **Primary Scoring Method**: Zero-Leakage Monotone Benchmark Mapping (`src/mapping.py`, ZERO Dykstra label-clamping)
- **Strict Curve Monotonicity**: `True` (min slope `0.0500` >= `0.05`)
- **Total Constraints Evaluated**: 3133
- **Pure-Mapping Concordance**: 3083 / 3133 (98.40%)
- **Residual Genuine Inversions**: 50
- **LOVO Held-Out Generalization**: 98.55% across 2687 held-out pairs (R0_raw=86.79%, R0_LOO=93.26%, R1=98.36%)
- **Optional Post-Projection Reference (Dykstra, NOT used in primary scores)**: 3133 / 3133 (100.00%, 0 violations, converged in 11 epochs)

## Constraint Distribution & Pure-Mapping Concordance by Rule
1. **Rule 1 (Tier Ordering within same series & version)**: 586/607 (96.54%)
2. **Rule 2 (Version Ordering within same series & tier)**: 2045/2069 (98.84%)
3. **Rule 3 (Thinking Level Ordering within same model)**: 407/408 (99.75%)
4. **Rule 4 (Date Snapshot Ordering within same model stem)**: 45/49 (91.84%)

## Multi-Round Mapping Progression (Pure Benchmark Scores)

| Round | Method | Satisfied / Total | Concordance | Inversions | Rule 1 | Rule 2 | Rule 3 | Rule 4 |
|---|---|---|---|---|---|---|---|---|
| `round_0a` | Raw Min-Max Mean | 2685/3133 | **85.70%** | 448 | 90.0% | 84.6% | 87.5% | 63.3% |
| `round_0b` | LOO Linear Calibration | 2896/3133 | **92.44%** | 237 | 93.4% | 92.8% | 93.1% | 61.2% |
| `round_1` | Stage-1 Unsupervised Monotone Calibration | 3070/3133 | **97.99%** | 63 | 95.1% | 98.9% | 98.8% | 89.8% |
| `round_2` | Regularized Benchmark Weight Optimization | 3078/3133 | **98.24%** | 55 | 95.4% | 99.0% | 99.3% | 91.8% |
| `round_3` | Joint Monotone Curve + Weight Optimization | 3081/3133 | **98.34%** | 52 | 96.0% | 98.9% | 99.5% | 93.9% |
| `round_4a` | Pseudo-Huber IRLS Robust Aggregation | 3075/3133 | **98.15%** | 58 | 95.4% | 98.8% | 99.8% | 91.8% |
| `round_4b` | Huber/IRLS + Margin-Annealed Refinement | 3083/3133 | **98.40%** | 50 | 96.5% | 98.8% | 99.8% | 91.8% |

## Leave-One-Vendor-Out (LOVO) Cross-Validation

| Held-Out Vendor | Models | Held-Out Constraints | R0 Raw | R0 LOO | R1 Unsup | R4 Held-Out | vs R0 LOO |
|---|---|---|---|---|---|---|---|
| OpenAI | 113 | 948 | 89.03% | 95.04% | 99.05% | **99.26%** | +4.22% |
| Google | 74 | 482 | 87.34% | 93.36% | 98.76% | **98.76%** | +5.39% |
| Anthropic | 65 | 410 | 90.73% | 96.59% | 99.27% | **99.02%** | +2.44% |
| Alibaba | 87 | 449 | 88.86% | 92.87% | 96.88% | **97.77%** | +4.90% |
| DeepSeek | 36 | 143 | 72.03% | 79.72% | 97.20% | **97.20%** | +17.48% |
| Meta | 27 | 46 | 84.78% | 91.30% | 95.65% | **95.65%** | +4.35% |
| SpaceXAI | 27 | 146 | 72.60% | 87.67% | 96.58% | **96.58%** | +8.90% |
| Z AI | 23 | 63 | 76.19% | 92.06% | 98.41% | **98.41%** | +6.35% |
| **TOTAL LOVO** | — | **2687** | **86.79%** | **93.26%** | **98.36%** | **98.55%** | **+5.28%** |

## Flagship Ordering Chains

- **[PASS]** GPT-6.2 Astra (max) (0.9826) > GPT-6 Astra (max) (0.8750) > GPT-6 Astra (xhigh) (0.8483) > GPT-6 Astra (high) (0.8339) > GPT-6 Astra (medium) (0.8173)
- **[PASS]** GPT-6.2 Sol (max) (0.9454) > GPT-6.1 Sol (max) (0.8910) > GPT-6 Sol (max) (0.8086) > GPT-5.6 Sol (max) (0.7536)
- **[PASS]** GPT-6.2 Astra (max) (0.9826) > GPT-6.2 Sol (max) (0.9454)
- **[PASS]** Gemini 4 Neon (xhigh) (0.9609) > Gemini 4 Neon (high) (0.9557) > Gemini 4 Neon (medium) (0.9251)
- **[PASS]** Gemini 4 Carbon (high) (0.9325) > Gemini 4 Carbon (medium) (0.9261) > Gemini 4 Carbon (low) (0.8903)
- **[PASS]** Gemini 4 Carbon (high) (0.9325) > Gemini 4 Argon (high) (0.8464)
- **[PASS]** Claude Fable 5.2 (max) (1.0000) > Claude Fable 5.1 (max) (0.8522) > Claude Fable 5 (0.7383)
- **[PASS]** Claude Opus 5.5 (max) (0.9213) > Claude Opus 5.5 (xhigh) (0.9021) > Claude Opus 5.5 (high) (0.8654) > Claude Opus 5.5 (medium) (0.8362)
- **[PASS]** Grok 4.3 (high) (0.4907) > Grok 4.3 (medium) (0.4860)
- **[PASS]** MiniMax-M2.7 (0.4705) > MiniMax-M2.5 (0.4325)

## Top 30 Models by Pure Benchmark-Mapped Score

| Rank | Model | Creator | Thinking | Final Score (100) | Raw Avg | Mode |
|---|---|---|---|---|---|---|
| 1 | `Claude Fable 5.2 (max)` | Anthropic | max | **100.00** | 0.9324 | PURE-MAP |
| 2 | `GPT-6.2 Astra (max)` | OpenAI | max | **98.26** | 0.8886 | PURE-MAP |
| 3 | `Claude Fable 5.2 (xhigh)` | Anthropic | xhigh | **96.83** | 0.8955 | PURE-MAP |
| 4 | `GPT-6.2 Astra (xhigh)` | OpenAI | xhigh | **96.20** | 0.8568 | PURE-MAP |
| 5 | `Gemini 4 Neon (xhigh)` | Google | xhigh | **96.09** | 0.8870 | PURE-MAP |
| 6 | `Gemini 4 Neon (high)` | Google | high | **95.57** | 0.8768 | PURE-MAP |
| 7 | `GPT-6.2 Astra (high)` | OpenAI | high | **95.19** | 0.8444 | PURE-MAP |
| 8 | `Claude Fable 5.2 (high)` | Anthropic | high | **95.14** | 0.8845 | PURE-MAP |
| 9 | `GPT-6.2 Sol (max)` | OpenAI | max | **94.54** | 0.8305 | PURE-MAP |
| 10 | `Gemini 4 Carbon (high)` | Google | high | **93.25** | 0.8753 | PURE-MAP |
| 11 | `Gemini 4 Carbon (medium)` | Google | medium | **92.61** | 0.8503 | PURE-MAP |
| 12 | `Gemini 4 Neon (medium)` | Google | medium | **92.51** | 0.8350 | PURE-MAP |
| 13 | `Claude Opus 5.5 (max)` | Anthropic | max | **92.13** | 0.8540 | PURE-MAP |
| 14 | `GPT-6.2 Astra (medium)` | OpenAI | medium | **91.55** | 0.8003 | PURE-MAP |
| 15 | `GPT-6.2 Sol (xhigh)` | OpenAI | xhigh | **91.47** | 0.7838 | PURE-MAP |
| 16 | `Claude Fable 5.2 (medium)` | Anthropic | medium | **91.42** | 0.8527 | PURE-MAP |
| 17 | `GPT-6.2 Sol (high)` | OpenAI | high | **90.75** | 0.7704 | PURE-MAP |
| 18 | `Gemini 4 Hydrogen (xhigh)` | Google | xhigh | **90.68** | 0.8033 | PURE-MAP |
| 19 | `Claude Opus 5.5 (xhigh)` | Anthropic | xhigh | **90.21** | 0.8417 | PURE-MAP |
| 20 | `Claude Fable 5.2 (low)` | Anthropic | low | **89.34** | 0.8312 | PURE-MAP |
| 21 | `Claude Sonnet 5.5 (max)` | Anthropic | max | **89.27** | 0.8364 | PURE-MAP |
| 22 | `GPT-6.2 Sol (medium)` | OpenAI | medium | **89.19** | 0.7462 | PURE-MAP |
| 23 | `GPT-6.1 Sol (max)` | OpenAI | max | **89.10** | 0.8337 | PURE-MAP |
| 24 | `Gemini 4 Carbon (low)` | Google | low | **89.03** | 0.7867 | PURE-MAP |
| 25 | `Gemini 4 Hydrogen (high)` | Google | high | **88.96** | 0.7881 | PURE-MAP |
| 26 | `GPT-6 Astra (max)` | OpenAI | max | **87.50** | 0.8528 | PURE-MAP |
| 27 | `Claude Opus 5.5 (high)` | Anthropic | high | **86.54** | 0.7911 | PURE-MAP |
| 28 | `GPT-6.1 Sol (xhigh)` | OpenAI | xhigh | **86.44** | 0.8122 | PURE-MAP |
| 29 | `Muse Wonder Full (max)` | Meta | max | **86.09** | 0.8037 | PURE-MAP |
| 30 | `Gemini 4 Neon (low)` | Google | low | **85.73** | 0.7304 | PURE-MAP |

## Top Genuine Residual Data Inversions

| Higher Model | Lower Model | Score Higher | Score Lower | Diff | Reason |
|---|---|---|---|---|---|
| `Mistral Small 4 (non-reasoning)` | `Mistral Small 3.1` | 0.1576 | 0.2214 | -0.0637 | Rule 2: Series [Mistral - Mistral] tier [Tier 3 (Small / 7B)] Mistral v4 > Mistral v3.1 [matching thinking non-reasoning] |
| `GLM-5.2 (non-reasoning)` | `GLM-5.1 (non-reasoning)` | 0.3601 | 0.4180 | -0.0578 | Rule 2: Series [Z_AI - GLM] tier [Tier 1 (Flagship / Pro)] GLM-5.2 > GLM-5.1 [matching thinking non-reasoning] |
| `Mistral Small 3.2` | `Mistral Small 3.1` | 0.1671 | 0.2214 | -0.0543 | Rule 2: Series [Mistral - Mistral] tier [Tier 3 (Small / 7B)] Mistral v3.2 > Mistral v3.1 [matching thinking standard] |
| `Muse Spark 1.1 (xhigh)` | `Muse Spark Open (xhigh)` | 0.5940 | 0.6448 | -0.0508 | Rule 2: Series [Meta - Muse] tier [Tier 2 (Spark)] Muse 1.1 > Muse 1.0 [matching thinking xhigh] |
| `DeepSeek V4 Pro (max)` | `DeepSeek V4 Flash 0731 (max)` | 0.5699 | 0.6169 | -0.0470 | Rule 1: Series [DeepSeek - DeepSeek-V] version [DeepSeek V4] Tier 1 (Pro / Full) > Tier 2 (Flash) [matching thinking max] |
| `Mixtral 8x7B` | `Mistral Small (Sep)` | 0.0379 | 0.0775 | -0.0396 | Rule 1: Series [Mistral - Mistral] version [Mistral v1] Tier 2 (Medium) > Tier 3 (Small / 7B) [matching thinking standard] |
| `Gemini 2.5 Flash (Apr) (non-reasoning)` | `Gemini 2.5 Flash-Lite (Sep) (non-reasoning)` | 0.1940 | 0.2299 | -0.0359 | Rule 1: Series [Google - Gemini] version [Gemini 2.5] Tier 3 (Flash) > Tier 4 (Flash-Lite / Nano) [matching thinking non-reasoning] |
| `Claude 4 Opus (non-reasoning)` | `Claude 4 Sonnet (non-reasoning)` | 0.2270 | 0.2588 | -0.0317 | Rule 1: Series [Anthropic - Claude] version [Claude 4] Tier 2 (Opus) > Tier 3 (Sonnet) [matching thinking non-reasoning] |
| `DeepSeek V3.2 Exp` | `DeepSeek V3.1 Terminus` | 0.3480 | 0.3790 | -0.0311 | Rule 2: Series [DeepSeek - DeepSeek-V] tier [Tier 1 (Pro / Full)] DeepSeek V3.2 > DeepSeek V3.1 Terminus [matching thinking reasoning] |
| `DeepSeek V4 Pro (max)` | `DeepSeek V4 Flash Vision (max)` | 0.5699 | 0.5978 | -0.0279 | Rule 1: Series [DeepSeek - DeepSeek-V] version [DeepSeek V4] Tier 1 (Pro / Full) > Tier 2 (Flash) [matching thinking max] |
| `Nemotron 3 Nano (non-reasoning)` | `NVIDIA Nemotron Nano 9B V2 (non-reasoning)` | 0.1391 | 0.1669 | -0.0279 | Rule 2: Series [NVIDIA - Nemotron] tier [Tier 3 (Nano 9B / 3 Nano / Lightning)] Nemotron 3 > Nemotron 2 [matching thinking non-reasoning] |
| `Mistral Medium` | `Mistral Small (Sep)` | 0.0575 | 0.0775 | -0.0201 | Rule 1: Series [Mistral - Mistral] version [Mistral v1] Tier 2 (Medium) > Tier 3 (Small / 7B) [matching thinking standard] |
| `Qwen3 30B` | `Qwen3 14B` | 0.1861 | 0.2045 | -0.0184 | Rule 1: Series [Alibaba - Qwen] version [Qwen 3] Tier 5 (MoE Mid: 35B-30B A3B) > Tier 6 (Small: 14B-4B) [matching thinking reasoning] |
| `DeepSeek R1 Distill Llama 70B` | `DeepSeek R1 Distill Qwen 14B` | 0.1095 | 0.1278 | -0.0183 | Rule 1: Series [DeepSeek - DeepSeek-R] version [DeepSeek R1] Tier 2 (Distill 70B / 32B) > Tier 3 (Distill 14B / 8B / 1.5B) [matching thinking reasoning] |
| `Nova 2.0 Omni (medium)` | `Nova 2.0 Lite (medium)` | 0.2830 | 0.3002 | -0.0173 | Rule 1: Series [Amazon - Nova] version [Nova 2.0] Tier 1 (Omni / Pro / Premier) > Tier 2 (Lite) [matching thinking medium] |
| `Grok 4.3 (high)` | `Grok 4.20 0309 v2` | 0.4907 | 0.5064 | -0.0157 | Rule 2: Series [SpaceXAI - Grok] tier [Tier 1 (Full / Flagship)] Grok 4.3 > Grok 4.20 [matching thinking high] |
| `GPT-5.1 Codex (high)` | `GPT-5 Codex (high)` | 0.4350 | 0.4501 | -0.0151 | Rule 2: Series [OpenAI - GPT-Codex] tier [Tier 1 (Codex)] GPT-5.1 > GPT-5 [matching thinking high] |
| `Gemini 1.5 Pro (May)` | `Gemini 1.5 Flash (Sep)` | 0.0945 | 0.1078 | -0.0133 | Rule 1: Series [Google - Gemini] version [Gemini 1.5] Tier 2 (Pro) > Tier 3 (Flash) [matching thinking standard] |
| `Mixtral 8x7B` | `Mistral Small (Feb)` | 0.0379 | 0.0505 | -0.0125 | Rule 1: Series [Mistral - Mistral] version [Mistral v1] Tier 2 (Medium) > Tier 3 (Small / 7B) [matching thinking standard] |
| `Motif 3` | `Motif 3 (Beta)` | 0.5329 | 0.5436 | -0.0107 | Rule 2: Series [Motif Technologies - Motif] tier [Tier 2 (Medium / MoE)] 2026-08 > 2026-07 [matching thinking reasoning] |
| `Qwen3 32B (non-reasoning)` | `Qwen2.5 72B` | 0.1276 | 0.1377 | -0.0101 | Rule 2: Series [Alibaba - Qwen] tier [Tier 3 (Dense Large: 110B-27B)] Qwen 3 > Qwen 2.5 [matching thinking non-reasoning] |
| `Qwen3.5 0.8B` | `Qwen3.5 0.8B (non-reasoning)` | 0.0580 | 0.0678 | -0.0098 | Rule 3: Same model [Qwen3.5 0.8B] higher thinking (reasoning > non-reasoning) |
| `Mistral Small 4 (non-reasoning)` | `Mistral Small 3.2` | 0.1576 | 0.1671 | -0.0095 | Rule 2: Series [Mistral - Mistral] tier [Tier 3 (Small / 7B)] Mistral v4 > Mistral v3.2 [matching thinking non-reasoning] |
| `LFM2.5-8B-A1B` | `LFM2.5-2.6B` | 0.1559 | 0.1652 | -0.0093 | Rule 1: Series [Liquid AI - LFM] version [LFM 2.5] Tier 3 (Small: 8B) > Tier 4 (Compact: 2.6B-1.7B) [matching thinking reasoning] |
| `Gemini 2.5 Flash (Apr)` | `Gemini 2.5 Flash-Lite (Sep)` | 0.2623 | 0.2714 | -0.0091 | Rule 1: Series [Google - Gemini] version [Gemini 2.5] Tier 3 (Flash) > Tier 4 (Flash-Lite / Nano) [matching thinking reasoning] |
