# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

## 全部模型（综合能力从高到低，最优 = 1，最差 = 0）

共收录 **Status: All**（含已弃用）的全部模型；按重新归一化后的综合能力排序。「帕累托」列：✅ = 总体帕累托前沿模型，❌ = 被支配，— = 无成本数据无法判定。图表纵轴以总体帕累托前沿第一级（y0 = 0.6320，即前沿左端点 Ling-3.0-flash-VL）为 0：综合能力 ≥ 该级且有成本数据的 95 个模型入图，439 个能力低于第一级、14 个缺少成本数据的模型不出现在图中（本表不受影响，仍完整列出全部模型）。

| # | 品牌 | 模型 | 综合能力 | 单请求成本 | 横轴位置 | 帕累托 |
|---|------|------|---------|-----------|-----------|------|
| 1 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (max with fallback) | 1.0000 | 720,368.00 | 0.9892 | ✅ |
| 2 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (xhigh with fallback) | 0.9876 | 300,585.19 | 0.9570 | ✅ |
| 3 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (xhigh) | 0.9768 | 357,789.54 | 0.9785 | ❌ |
| 4 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (max) | 0.9740 | 925,405.83 | 1.0000 | ❌ |
| 5 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (high) | 0.9577 | 135,969.29 | 0.8817 | ✅ |
| 6 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (max) | 0.9575 | 74,257.91 | 0.8387 | ✅ |
| 7 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (high with fallback) | 0.9550 | 65,473.67 | 0.8280 | ✅ |
| 8 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5 (with fallback) | 0.9475 | 355,073.73 | 0.9677 | ❌ |
| 9 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (xhigh) | 0.9471 | 46,656.39 | 0.7312 | ✅ |
| 10 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (medium) | 0.9362 | 52,203.83 | 0.7957 | ❌ |
| 11 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.3 (max) | 0.9340 | 12,705.20 | 0.2903 | ✅ |
| 12 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (high) | 0.9330 | 32,070.28 | 0.6344 | ❌ |
| 13 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (max) | 0.9297 | 139,262.92 | 0.9032 | ❌ |
| 14 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.3 (xhigh) | 0.9271 | 12,705.20 | 0.2903 | ✅ |
| 15 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (medium with fallback) | 0.9226 | 50,457.55 | 0.7849 | ❌ |
| 16 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (low) | 0.8987 | 48,345.51 | 0.7742 | ❌ |
| 17 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (medium) | 0.8912 | 26,789.15 | 0.5806 | ❌ |
| 18 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (low with fallback) | 0.8891 | 47,155.93 | 0.7527 | ❌ |
| 19 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3 (max) | 0.8862 | 41,924.14 | 0.7043 | ❌ |
| 20 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (xhigh) | 0.8855 | 62,894.25 | 0.8172 | ❌ |
| 21 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (xhigh) | 0.8831 | 17,651.73 | 0.3871 | ❌ |
| 22 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (high) | 0.8787 | 22,158.61 | 0.5376 | ❌ |
| 23 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (high) | 0.8781 | 21,229.78 | 0.4839 | ❌ |
| 24 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (medium) | 0.8738 | 19,450.09 | 0.4516 | ❌ |
| 25 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (xhigh) | 0.8738 | 136,595.39 | 0.8925 | ❌ |
| 26 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3 (max) | 0.8686 | 14,201.30 | 0.3602 | ❌ |
| 27 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (high) | 0.8658 | 27,526.00 | 0.6022 | ❌ |
| 28 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 Max (0902) | 0.8648 | 18,423.05 | 0.4086 | ❌ |
| 29 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.8 (max) | 0.8599 | 46,801.13 | 0.7419 | ❌ |
| 30 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (max) | 0.8585 | 174,832.92 | 0.9355 | ❌ |
| 31 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (high) | 0.8533 | 56,780.68 | 0.8065 | ❌ |
| 32 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (high) | 0.8495 | 14,018.66 | 0.3441 | ❌ |
| 33 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (medium) | 0.8472 | — | — | — |
| 34 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 Max | 0.8448 | 18,423.05 | 0.4086 | ❌ |
| 35 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (medium) | 0.8420 | 20,473.83 | 0.4731 | ❌ |
| 36 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.2 (xhigh) | 0.8363 | 12,705.20 | 0.2903 | ❌ |
| 37 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 2.4T A95B | 0.8295 | 18,423.05 | 0.4086 | ❌ |
| 38 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (low) | 0.8168 | 23,098.58 | 0.5591 | ❌ |
| 39 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (max) | 0.8157 | 139,729.66 | 0.9140 | ❌ |
| 40 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3-Flash | 0.8140 | 1,575.40 | 0.0215 | ✅ |
| 41 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.5 (high) | 0.8135 | 9,303.95 | 0.2151 | ❌ |
| 42 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.7 (max) | 0.8132 | 47,652.95 | 0.7634 | ❌ |
| 43 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (xhigh) | 0.8104 | 234,521.45 | 0.9462 | ❌ |
| 44 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash | 0.8098 | 40,002.41 | 0.6882 | ❌ |
| 45 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (medium) | 0.8056 | 31,314.87 | 0.6237 | ❌ |
| 46 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.2 (max) | 0.8024 | 14,201.30 | 0.3602 | ❌ |
| 47 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (medium) | 0.8013 | 7,884.05 | 0.1720 | ❌ |
| 48 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (xhigh) | 0.8006 | 25,117.63 | 0.5699 | ❌ |
| 49 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (medium) | 0.7940 | 32,952.51 | 0.6452 | ❌ |
| 50 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.1 Pro Preview | 0.7938 | 43,377.42 | 0.7204 | ❌ |
| 51 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.3 Codex (xhigh) | 0.7936 | 108,031.53 | 0.8710 | ❌ |
| 52 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.1 (xhigh) | 0.7873 | — | — | — |
| 53 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (low) | 0.7789 | 20,146.67 | 0.4624 | ❌ |
| 54 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8-Flash-Next | 0.7711 | 1,405.68 | 0.0108 | ✅ |
| 55 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.6 Flash | 0.7700 | 15,655.97 | 0.3763 | ❌ |
| 56 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (high) | 0.7628 | 12,266.01 | 0.2688 | ❌ |
| 57 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sapiens.svg" width="18" alt="Sapiens AI" /> Sapiens AI | Agnes 3.0 Flash | 0.7559 | 448.74 | 0.0000 | ✅ |
| 58 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.6 (max) | 0.7508 | 35,758.80 | 0.6559 | ❌ |
| 59 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (max) | 0.7507 | 18,621.26 | 0.4301 | ❌ |
| 60 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (low) | 0.7501 | — | — | — |
| 61 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (low) | 0.7476 | 3,850.76 | 0.0968 | ❌ |
| 62 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 v2 | 0.7467 | 8,886.04 | 0.1935 | ❌ |
| 63 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro 0813 (max) | 0.7433 | 11,013.04 | 0.2473 | ❌ |
| 64 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (low) | 0.7429 | 10,635.54 | 0.2366 | ❌ |
| 65 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark | 0.7378 | — | — | — |
| 66 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3 Pro Preview (high) | 0.7355 | — | — | — |
| 67 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (medium) | 0.7325 | 7,188.65 | 0.1613 | ❌ |
| 68 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sapiens.svg" width="18" alt="Sapiens AI" /> Sapiens AI | Agnes 2.5 Pro Beta | 0.7308 | — | — | — |
| 69 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.7 Max | 0.7244 | 27,872.42 | 0.6129 | ❌ |
| 70 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (xhigh) | 0.7224 | 94,388.94 | 0.8495 | ❌ |
| 71 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 Codex (xhigh) | 0.7217 | — | — | — |
| 72 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash (max) | 0.7211 | 3,215.07 | 0.0538 | ❌ |
| 73 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 Max Preview | 0.7202 | 21,588.55 | 0.5054 | ❌ |
| 74 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (xhigh) | 0.7194 | 8,237.36 | 0.1828 | ❌ |
| 75 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.6 | 0.7180 | 21,820.69 | 0.5161 | ❌ |
| 76 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (xhigh) | 0.7169 | 7,120.68 | 0.1505 | ❌ |
| 77 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.5 | 0.7068 | 37,172.26 | 0.6667 | ❌ |
| 78 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 | 0.7066 | — | — | — |
| 79 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash Vision (max) | 0.7049 | 3,664.70 | 0.0699 | ❌ |
| 80 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (low) | 0.7046 | 26,974.18 | 0.5914 | ❌ |
| 81 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (xhigh) | 0.7029 | 22,469.37 | 0.5484 | ❌ |
| 82 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.7 (Non-reasoning, high) | 0.7022 | 21,529.13 | 0.4946 | ❌ |
| 83 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash 0731 (max) | 0.7004 | 3,664.70 | 0.0699 | ❌ |
| 84 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (max) | 0.6938 | 100,860.88 | 0.8602 | ❌ |
| 85 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (medium) | 0.6912 | 11,051.32 | 0.2581 | ❌ |
| 86 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3 Flash | 0.6901 | 5,979.47 | 0.1398 | ❌ |
| 87 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M3 | 0.6846 | 3,766.15 | 0.0860 | ❌ |
| 88 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (low) | 0.6839 | 13,666.48 | 0.3226 | ❌ |
| 89 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (high) | 0.6821 | 2,086.09 | 0.0323 | ❌ |
| 90 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.7 Plus | 0.6819 | 4,642.63 | 0.1183 | ❌ |
| 91 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 Plus | 0.6781 | 18,953.29 | 0.4409 | ❌ |
| 92 | <img src="https://artificialanalysis.ai/img/logos//img/logos/motif_small.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif 3 | 0.6779 | — | — | — |
| 93 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (low) | 0.6745 | 4,966.62 | 0.1290 | ❌ |
| 94 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Pro | 0.6727 | — | — | — |
| 95 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (max) | 0.6725 | 4,504.80 | 0.1075 | ❌ |
| 96 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3 (low) | 0.6700 | 41,924.14 | 0.7043 | ❌ |
| 97 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.1 | 0.6672 | 21,976.21 | 0.5269 | ❌ |
| 98 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (medium) | 0.6671 | — | — | — |
| 99 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (high) | 0.6611 | 10,594.71 | 0.2258 | ❌ |
| 100 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (high) | 0.6594 | 2,431.59 | 0.0430 | ❌ |
| 101 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (high) | 0.6574 | 9,008.46 | 0.2043 | ❌ |
| 102 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mbzuai_small.svg" width="18" alt="MBZUAI Institute of Foundation Models" /> MBZUAI Institute of Foundation Models | K2 Horizon 375B A23B | 0.6563 | — | — | — |
| 103 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 Codex (high) | 0.6536 | — | — | — |
| 104 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 (high) | 0.6505 | 37,810.22 | 0.6774 | ❌ |
| 105 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5 | 0.6484 | 13,957.97 | 0.3333 | ❌ |
| 106 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.7 Code | 0.6480 | 13,216.87 | 0.3118 | ❌ |
| 107 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (xhigh) | 0.6373 | 147,034.23 | 0.9247 | ❌ |
| 108 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 Codex (high) | 0.6352 | — | — | — |
| 109 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-3.0-flash-VL | 0.6320 | 0.00 | 0.0000 | ✅ |
| 110 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (low) | 0.6275 | 10,914.11 | 0.2445 | ❌ |
| 111 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Omni-0327 | 0.6253 | — | — | — |
| 112 | <img src="https://artificialanalysis.ai/img/logos//img/logos/apodex.svg" width="18" alt="Apodex" /> Apodex | Apodex 1.1 | 0.6243 | — | — | — |
| 113 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (medium) | 0.6231 | 33,500.85 | 0.6473 | ❌ |
| 114 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5-Pro | 0.6229 | 2,438.55 | 0.0431 | ❌ |
| 115 | <img src="https://artificialanalysis.ai/img/logos//img/logos/thinking_machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling | 0.6228 | 12,262.79 | 0.2688 | ❌ |
| 116 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (max) | 0.6194 | — | — | — |
| 117 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok Build 0.1 0616 | 0.6179 | 7,421.97 | 0.1650 | ❌ |
| 118 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (high) | 0.6167 | 69,143.75 | 0.8326 | ❌ |
| 119 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5 | 0.6166 | 800.37 | 0.0054 | ❌ |
| 120 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.6 (Non-reasoning, high) | 0.6161 | 22,628.35 | 0.5511 | ❌ |
| 121 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5-Turbo | 0.6157 | — | — | — |
| 122 | <img src="https://artificialanalysis.ai/img/logos//img/logos/thinking_machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling Small | 0.6151 | 3,726.59 | 0.0798 | ❌ |
| 123 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 | 0.6138 | — | — | — |
| 124 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 4 | 0.6113 | 3,726.59 | 0.0798 | ❌ |
| 125 | <img src="https://artificialanalysis.ai/img/logos//img/logos/multiversecomputing_small.svg" width="18" alt="Multiverse Computing" /> Multiverse Computing | Quasar 438B (max) | 0.6064 | 4,816.47 | 0.1241 | ❌ |
| 126 | <img src="https://artificialanalysis.ai/img/logos//img/logos/motif_small.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif 3 (Beta) | 0.6048 | — | — | — |
| 127 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 Instant (May 2026) | 0.6045 | — | — | — |
| 128 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Opus | 0.6025 | — | — | — |
| 129 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nex_small.svg" width="18" alt="Nex AGI" /> Nex AGI | Nex-N2-Pro | 0.6018 | — | — | — |
| 130 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (xhigh) | 0.6012 | 13,284.98 | 0.3135 | ❌ |
| 131 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (high) | 0.5999 | — | — | — |
| 132 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 27B | 0.5961 | 22,550.07 | 0.5498 | ❌ |
| 133 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (minimal) | 0.5941 | 8,293.23 | 0.1838 | ❌ |
| 134 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 27B | 0.5926 | 6,158.24 | 0.1416 | ❌ |
| 135 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash (Feb 2026) | 0.5925 | — | — | — |
| 136 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Sonnet | 0.5920 | 17,187.56 | 0.3847 | ❌ |
| 137 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.5 | 0.5917 | — | — | — |
| 138 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Omni | 0.5908 | — | — | — |
| 139 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Ultra | 0.5897 | 8,870.98 | 0.1933 | ❌ |
| 140 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o3 | 0.5896 | 17,118.36 | 0.3843 | ❌ |
| 141 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Open2 250B | 0.5888 | — | — | — |
| 142 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (medium) | 0.5871 | 9,256.53 | 0.2134 | ❌ |
| 143 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM 5V Turbo | 0.5862 | — | — | — |
| 144 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (medium) | 0.5831 | 8,237.36 | 0.1828 | ❌ |
| 145 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash-Lite | 0.5805 | 9,438.74 | 0.2162 | ❌ |
| 146 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (medium) | 0.5802 | 3,939.75 | 0.0983 | ❌ |
| 147 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 397B A17B | 0.5796 | 13,586.07 | 0.3207 | ❌ |
| 148 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.1 Opus | 0.5782 | — | — | — |
| 149 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (Non-reasoning, high) | 0.5766 | 13,121.83 | 0.3079 | ❌ |
| 150 | <img src="https://artificialanalysis.ai/img/logos//img/logos/tencent_small.svg" width="18" alt="Tencent" /> Tencent | Hy3 | 0.5764 | 1,855.38 | 0.0278 | ❌ |
| 151 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 Thinking | 0.5758 | 6,566.47 | 0.1455 | ❌ |
| 152 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (medium) | 0.5740 | 1,219.96 | 0.0094 | ❌ |
| 153 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.5 (Non-reasoning) | 0.5739 | 21,903.53 | 0.5219 | ❌ |
| 154 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (Non-reasoning) | 0.5715 | 17,975.77 | 0.3962 | ❌ |
| 155 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (Non-reasoning, low) | 0.5708 | 13,159.16 | 0.3094 | ❌ |
| 156 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mbzuai_small.svg" width="18" alt="MBZUAI Institute of Foundation Models" /> MBZUAI Institute of Foundation Models | K2 Horizon MoVA 36B A4B | 0.5700 | — | — | — |
| 157 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.6 (Non-reasoning) | 0.5688 | 4,529.29 | 0.1095 | ❌ |
| 158 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.7 | 0.5685 | 4,320.55 | 0.1047 | ❌ |
| 159 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3 Pro Preview (low) | 0.5683 | — | — | — |
| 160 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (low) | 0.5677 | 8,237.36 | 0.1828 | ❌ |
| 161 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (Non-reasoning) | 0.5663 | 8,799.07 | 0.1922 | ❌ |
| 162 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 Codex mini (high) | 0.5590 | — | — | — |
| 163 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sktelecom_small.svg" width="18" alt="SK Telecom" /> SK Telecom | A.X-K2 | 0.5566 | — | — | — |
| 164 | <img src="https://artificialanalysis.ai/img/logos//img/logos/china_mobile_small.png" width="18" alt="China Mobile" /> China Mobile | JT-4.1 Flash 236B A21B | 0.5560 | — | — | — |
| 165 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (low) | 0.5559 | 11,771.73 | 0.2646 | ❌ |
| 166 | <img src="https://artificialanalysis.ai/img/logos//img/logos/tencent_small.svg" width="18" alt="Tencent" /> Tencent | Hy3-preview | 0.5554 | — | — | — |
| 167 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 35B A3B | 0.5548 | 13,461.55 | 0.3177 | ❌ |
| 168 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.5 | 0.5495 | 3,481.97 | 0.0636 | ❌ |
| 169 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.1 (Non-reasoning) | 0.5494 | 5,672.44 | 0.1367 | ❌ |
| 170 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 Omni Plus | 0.5481 | 3,634.11 | 0.0689 | ❌ |
| 171 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (high) | 0.5458 | 15,300.83 | 0.3725 | ❌ |
| 172 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 122B A10B | 0.5431 | 8,210.98 | 0.1820 | ❌ |
| 173 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.1 Fast | 0.5413 | — | — | — |
| 174 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sapiens.svg" width="18" alt="Sapiens AI" /> Sapiens AI | Agnes 2.5 Pro Alpha | 0.5408 | 2,582.08 | 0.0453 | ❌ |
| 175 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step 3.7 Flash | 0.5367 | 3,359.39 | 0.0592 | ❌ |
| 176 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | G9v3-39A5B | 0.5355 | — | — | — |
| 177 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano | 0.5352 | 1,885.02 | 0.0284 | ❌ |
| 178 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max Thinking | 0.5346 | — | — | — |
| 179 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.1 | 0.5344 | 3,158.24 | 0.0531 | ❌ |
| 180 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 35B A3B | 0.5285 | 5,131.86 | 0.1309 | ❌ |
| 181 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B | 0.5280 | 2,831.32 | 0.0489 | ❌ |
| 182 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.0 Flash | 0.5250 | 731.65 | 0.0046 | ❌ |
| 183 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7 | 0.5245 | 11,500.00 | 0.2622 | ❌ |
| 184 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.5 (Non-reasoning) | 0.5236 | — | — | — |
| 185 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 | 0.5231 | — | — | — |
| 186 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash | 0.5222 | — | — | — |
| 187 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (medium) | 0.5215 | 6,959.66 | 0.1491 | ❌ |
| 188 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (low) | 0.5215 | 1,184.45 | 0.0091 | ❌ |
| 189 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kwaikat_small.svg" width="18" alt="KwaiKAT" /> KwaiKAT | KAT-Coder-Pro V2 | 0.5212 | — | — | — |
| 190 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (low) | 0.5209 | 8,939.53 | 0.1983 | ❌ |
| 191 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 31B | 0.5184 | 0.00 | 0.0000 | ❌ |
| 192 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3 Flash (Non-reasoning) | 0.5167 | 2,785.27 | 0.0482 | ❌ |
| 193 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Glimmer (high) | 0.5143 | 4,313.51 | 0.1046 | ❌ |
| 194 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Sonnet | 0.5127 | — | — | — |
| 195 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5 (Non-reasoning) | 0.5120 | 4,342.51 | 0.1050 | ❌ |
| 196 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 397B A17B (Non-reasoning) | 0.5058 | 2,743.22 | 0.0477 | ❌ |
| 197 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step 3.5 Flash 2603 | 0.5050 | 992.20 | 0.0075 | ❌ |
| 198 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 Instant (June 2026) | 0.5040 | 82,373.56 | 0.8434 | ❌ |
| 199 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (Non-reasoning) | 0.5017 | 24,643.36 | 0.5674 | ❌ |
| 200 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 Fast | 0.4990 | — | — | — |
| 201 | <img src="https://artificialanalysis.ai/img/logos//img/logos/cohere_small.svg" width="18" alt="Cohere" /> Cohere | Command A+ | 0.4922 | 0.00 | 0.0000 | ❌ |
| 202 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 3 mini Reasoning (high) | 0.4911 | 2,118.68 | 0.0333 | ❌ |
| 203 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 27B (Non-reasoning) | 0.4905 | 2,506.39 | 0.0442 | ❌ |
| 204 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-2.6-1T | 0.4903 | 6,408.24 | 0.1440 | ❌ |
| 205 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Sonnet (Non-reasoning) | 0.4902 | 13,056.42 | 0.3052 | ❌ |
| 206 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Speciale | 0.4894 | — | — | — |
| 207 | <img src="https://artificialanalysis.ai/img/logos//img/logos/china_mobile_small.png" width="18" alt="China Mobile" /> China Mobile | JT-35B-Flash | 0.4876 | — | — | — |
| 208 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step 3.5 Flash | 0.4871 | 802.75 | 0.0055 | ❌ |
| 209 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Pro | 0.4845 | 33,021.96 | 0.6454 | ❌ |
| 210 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3.5 | 0.4803 | 20,962.07 | 0.4801 | ❌ |
| 211 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mbzuai_small.svg" width="18" alt="MBZUAI Institute of Foundation Models" /> MBZUAI Institute of Foundation Models | K2 Horizon 7B | 0.4801 | — | — | — |
| 212 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE 2.0 | 0.4777 | — | — | — |
| 213 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (Non-reasoning) | 0.4753 | 12,462.95 | 0.2786 | ❌ |
| 214 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2 | 0.4743 | 3,158.24 | 0.0531 | ❌ |
| 215 | <img src="https://artificialanalysis.ai/img/logos//img/logos/bytedance_small.svg" width="18" alt="ByteDance Seed" /> ByteDance Seed | Doubao Seed Code | 0.4714 | — | — | — |
| 216 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Haiku | 0.4713 | 13,826.08 | 0.3285 | ❌ |
| 217 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o4-mini (high) | 0.4712 | 22,854.50 | 0.5550 | ❌ |
| 218 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o1 | 0.4703 | — | — | — |
| 219 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (Non-reasoning) | 0.4688 | 10,193.12 | 0.2226 | ❌ |
| 220 | <img src="https://artificialanalysis.ai/img/logos//img/logos/longcat_small.svg" width="18" alt="LongCat" /> LongCat | LongCat 2.0 | 0.4633 | — | — | — |
| 221 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (Non-reasoning) | 0.4598 | 822.48 | 0.0057 | ❌ |
| 222 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.2 (Non-reasoning) | 0.4593 | 6,547.80 | 0.1454 | ❌ |
| 223 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (medium) | 0.4578 | 28,614.76 | 0.6153 | ❌ |
| 224 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.7 Sonnet | 0.4561 | — | — | — |
| 225 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 27B (Non-reasoning) | 0.4536 | 2,891.00 | 0.0497 | ❌ |
| 226 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kwaikat_small.svg" width="18" alt="KwaiKAT" /> KwaiKAT | KAT-Coder-Pro V1 | 0.4531 | — | — | — |
| 227 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Sonnet (Non-reasoning) | 0.4525 | — | — | — |
| 228 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (low) | 0.4505 | 25,659.32 | 0.5735 | ❌ |
| 229 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 Terminus | 0.4500 | — | — | — |
| 230 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.1 Flash-Lite | 0.4494 | 3,485.84 | 0.0637 | ❌ |
| 231 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Sep) | 0.4472 | — | — | — |
| 232 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Exp | 0.4426 | — | — | — |
| 233 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (Non-reasoning) | 0.4403 | 10,780.89 | 0.2407 | ❌ |
| 234 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 122B A10B (Non-reasoning) | 0.4373 | 2,874.61 | 0.0495 | ❌ |
| 235 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.7 Sonnet (Non-reasoning) | 0.4320 | — | — | — |
| 236 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max Thinking (Preview) | 0.4310 | 15,632.95 | 0.3761 | ❌ |
| 237 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 9B | 0.4296 | 571.21 | 0.0023 | ❌ |
| 238 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash | 0.4260 | 15,248.57 | 0.3720 | ❌ |
| 239 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 26B A4B | 0.4257 | — | — | — |
| 240 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (medium) | 0.4251 | 6,408.24 | 0.1440 | ❌ |
| 241 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5-Pro (Non-reasoning) | 0.4213 | 825.80 | 0.0057 | ❌ |
| 242 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Haiku (Non-reasoning) | 0.4207 | 4,379.06 | 0.1056 | ❌ |
| 243 | <img src="https://artificialanalysis.ai/img/logos//img/logos/baidu_small.svg" width="18" alt="Baidu" /> Baidu | ERNIE 5.0 Thinking Preview | 0.4178 | — | — | — |
| 244 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 0905 | 0.4176 | 1,681.64 | 0.0240 | ❌ |
| 245 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (Non-reasoning) | 0.4167 | — | — | — |
| 246 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 235B A22B (Reasoning) | 0.4165 | 10,210.98 | 0.2228 | ❌ |
| 247 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.5 33B | 0.4153 | — | — | — |
| 248 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 (Non-reasoning) | 0.4150 | — | — | — |
| 249 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-2.6-1T | 0.4135 | — | — | — |
| 250 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (low) | 0.4093 | — | — | — |
| 251 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 (Non-reasoning) | 0.4078 | — | — | — |
| 252 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (high) | 0.4070 | 6,408.24 | 0.1440 | ❌ |
| 253 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (high) | 0.4061 | 6,908.50 | 0.1487 | ❌ |
| 254 | <img src="https://artificialanalysis.ai/img/logos//img/logos/tencent_small.svg" width="18" alt="Tencent" /> Tencent | Hy3-preview (Non-reasoning) | 0.4061 | — | — | — |
| 255 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 4B | 0.4056 | 390.82 | 0.0000 | ❌ |
| 256 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 35B A3B (Non-reasoning) | 0.4039 | 1,929.42 | 0.0293 | ❌ |
| 257 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (medium) | 0.4039 | 2,695.11 | 0.0470 | ❌ |
| 258 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7 (Non-reasoning) | 0.4029 | 6,685.13 | 0.1467 | ❌ |
| 259 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openbmb_small.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-2B | 0.4024 | — | — | — |
| 260 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 12B | 0.4017 | 802.75 | 0.0055 | ❌ |
| 261 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (medium) | 0.4015 | — | — | — |
| 262 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 v2 (Non-reasoning) | 0.3991 | 3,952.36 | 0.0986 | ❌ |
| 263 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (Non-reasoning) | 0.3957 | 3,992.57 | 0.0993 | ❌ |
| 264 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 | 0.3945 | — | — | — |
| 265 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5 | 0.3937 | — | — | — |
| 266 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6 | 0.3918 | 11,000.00 | 0.2469 | ❌ |
| 267 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inceptionlabs_small.svg" width="18" alt="Inception" /> Inception | Mercury 2 | 0.3887 | 2,947.23 | 0.0504 | ❌ |
| 268 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 31B (Non-reasoning) | 0.3885 | 1,634.78 | 0.0229 | ❌ |
| 269 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.2 30B | 0.3884 | 2,088.29 | 0.0323 | ❌ |
| 270 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max | 0.3881 | 4,371.69 | 0.1055 | ❌ |
| 271 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (Non-reasoning) | 0.3876 | 1,029.99 | 0.0078 | ❌ |
| 272 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mbzuai_small.svg" width="18" alt="MBZUAI Institute of Foundation Models" /> MBZUAI Institute of Foundation Models | K2 Horizon 3.7B | 0.3864 | — | — | — |
| 273 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok Code Fast 1 | 0.3849 | — | — | — |
| 274 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE | 0.3845 | — | — | — |
| 275 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 | 0.3838 | 1,597.28 | 0.0220 | ❌ |
| 276 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Super | 0.3836 | 1,726.54 | 0.0250 | ❌ |
| 277 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 0528 | 0.3830 | — | — | — |
| 278 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3.5 Lightning | 0.3812 | 1,005.27 | 0.0076 | ❌ |
| 279 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Sep) (Non-reasoning) | 0.3772 | — | — | — |
| 280 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.0 Tiny | 0.3770 | 0.00 | 0.0000 | ❌ |
| 281 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 35B A3B (Non-reasoning) | 0.3751 | 1,805.50 | 0.0267 | ❌ |
| 282 | <img src="https://artificialanalysis.ai/img/logos//img/logos/arcee_small.svg" width="18" alt="Arcee AI" /> Arcee AI | Trinity Large Thinking | 0.3747 | 2,381.86 | 0.0416 | ❌ |
| 283 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (minimal) | 0.3744 | 7,979.17 | 0.1750 | ❌ |
| 284 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 32B (Reasoning) | 0.3733 | 1,684.39 | 0.0241 | ❌ |
| 285 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 | 0.3721 | 11,041.81 | 0.2554 | ❌ |
| 286 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 (Non-reasoning) | 0.3708 | 7,962.05 | 0.1745 | ❌ |
| 287 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (low) | 0.3698 | 6,408.24 | 0.1440 | ❌ |
| 288 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 9B (Non-reasoning) | 0.3692 | 232.34 | 0.0000 | ❌ |
| 289 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7-Flash | 0.3689 | 1,700.00 | 0.0244 | ❌ |
| 290 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6 (Non-reasoning) | 0.3657 | 1,727.26 | 0.0250 | ❌ |
| 291 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B A22B 2507 | 0.3626 | 5,871.32 | 0.1387 | ❌ |
| 292 | <img src="https://artificialanalysis.ai/img/logos//img/logos/servicenow_small.svg" width="18" alt="ServiceNow" /> ServiceNow | Apriel-v1.5-15B-Thinker | 0.3622 | — | — | — |
| 293 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-120b (high) | 0.3586 | 2,750.69 | 0.0478 | ❌ |
| 294 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 Omni Flash | 0.3577 | 804.74 | 0.0055 | ❌ |
| 295 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder 480B | 0.3566 | 5,735.42 | 0.1374 | ❌ |
| 296 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Sep) | 0.3555 | — | — | — |
| 297 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron Cascade 2 30B A3B | 0.3552 | — | — | — |
| 298 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepcogito_small.png" width="18" alt="Deep Cogito" /> Deep Cogito | Cogito v2.1 | 0.3547 | — | — | — |
| 299 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash (Non-reasoning) | 0.3530 | — | — | — |
| 300 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Magistral Medium 1.2 | 0.3525 | — | — | — |
| 301 | <img src="https://artificialanalysis.ai/img/logos//img/logos/servicenow_small.svg" width="18" alt="ServiceNow" /> ServiceNow | Apriel-v1.6-15B-Thinker | 0.3516 | — | — | — |
| 302 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 26B A4B (Non-reasoning) | 0.3507 | 1,490.21 | 0.0163 | ❌ |
| 303 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 3 | 0.3495 | — | — | — |
| 304 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6V | 0.3493 | 2,408.24 | 0.0423 | ❌ |
| 305 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 Terminus (Non-reasoning) | 0.3485 | — | — | — |
| 306 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (ChatGPT) | 0.3439 | — | — | — |
| 307 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | G9v3-3B | 0.3395 | — | — | — |
| 308 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 4 | 0.3386 | 1,579.12 | 0.0216 | ❌ |
| 309 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max (Preview) | 0.3372 | 5,074.27 | 0.1303 | ❌ |
| 310 | <img src="https://artificialanalysis.ai/img/logos//img/logos/multiversecomputing_small.svg" width="18" alt="Multiverse Computing" /> Multiverse Computing | HyperNova 60B 2605 (high) | 0.3359 | 371.10 | 0.0000 | ❌ |
| 311 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.2 8B | 0.3341 | 798.74 | 0.0054 | ❌ |
| 312 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Exp (Non-reasoning) | 0.3309 | — | — | — |
| 313 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Sep) (Non-reasoning) | 0.3282 | — | — | — |
| 314 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 (Non-reasoning) | 0.3276 | — | — | — |
| 315 | <img src="https://artificialanalysis.ai/img/logos//img/logos/cohere_small.svg" width="18" alt="Cohere" /> Cohere | North Mini Code | 0.3269 | 0.00 | 0.0000 | ❌ |
| 316 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o3-mini (high) | 0.3240 | 27,162.02 | 0.5951 | ❌ |
| 317 | <img src="https://artificialanalysis.ai/img/logos//img/logos/bytedance_small.svg" width="18" alt="ByteDance Seed" /> ByteDance Seed | Seed-OSS-36B-Instruct | 0.3236 | 1,535.77 | 0.0191 | ❌ |
| 318 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o (Nov) | 0.3198 | 21,981.58 | 0.5272 | ❌ |
| 319 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Non-reasoning) | 0.3181 | 1,899.82 | 0.0287 | ❌ |
| 320 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 3 | 0.3175 | 1,721.21 | 0.0249 | ❌ |
| 321 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B 2507 (Non-reasoning) | 0.3165 | 707.73 | 0.0043 | ❌ |
| 322 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o (Aug) | 0.3164 | 19,326.98 | 0.4490 | ❌ |
| 323 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mbzuai_small.svg" width="18" alt="MBZUAI Institute of Foundation Models" /> MBZUAI Institute of Foundation Models | K2 Think V2 | 0.3154 | — | — | — |
| 324 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite | 0.3135 | 4,795.33 | 0.1234 | ❌ |
| 325 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder Next | 0.3103 | 4,240.05 | 0.1034 | ❌ |
| 326 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.1 Fast (Non-reasoning) | 0.3097 | — | — | — |
| 327 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (minimal) | 0.3090 | 1,517.00 | 0.0179 | ❌ |
| 328 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Next 80B A3B (Reasoning) | 0.3088 | 3,079.12 | 0.0521 | ❌ |
| 329 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano | 0.3085 | 526.37 | 0.0015 | ❌ |
| 330 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 12B (Non-reasoning) | 0.3078 | 278.29 | 0.0000 | ❌ |
| 331 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 235B A22B | 0.3073 | 1,232.26 | 0.0095 | ❌ |
| 332 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | QwQ-32B | 0.3060 | — | — | — |
| 333 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-1T | 0.3043 | — | — | — |
| 334 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openbmb_small.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-1B | 0.3042 | — | — | — |
| 335 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openbmb_small.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-1B (Non-reasoning) | 0.3041 | — | — | — |
| 336 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Pixtral Large | 0.3029 | — | — | — |
| 337 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Open 100B | 0.2994 | — | — | — |
| 338 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o3-mini | 0.2985 | 12,568.79 | 0.2837 | ❌ |
| 339 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 4B (Non-reasoning) | 0.2972 | 92.68 | 0.0000 | ❌ |
| 340 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax M1 80k | 0.2960 | — | — | — |
| 341 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5-Air | 0.2958 | 2,539.67 | 0.0447 | ❌ |
| 342 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (Non-reasoning) | 0.2951 | 3,996.09 | 0.0993 | ❌ |
| 343 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 E4B | 0.2950 | 260.55 | 0.0000 | ❌ |
| 344 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (Non-reasoning) | 0.2935 | 6,720.21 | 0.1470 | ❌ |
| 345 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | DiffusionGemma 26B A4B | 0.2911 | — | — | — |
| 346 | <img src="https://artificialanalysis.ai/img/logos//img/logos/china_mobile_small.png" width="18" alt="China Mobile" /> China Mobile | JT-MINI | 0.2911 | — | — | — |
| 347 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Large 3 | 0.2900 | 1,131.06 | 0.0087 | ❌ |
| 348 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3 | 0.2895 | 1,842.51 | 0.0275 | ❌ |
| 349 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax M1 40k | 0.2895 | — | — | — |
| 350 | <img src="https://artificialanalysis.ai/img/logos//img/logos/naver_small.webp" width="18" alt="Naver" /> Naver | HyperCLOVA X SEED Think (32B) | 0.2887 | — | — | — |
| 351 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3 0324 | 0.2874 | — | — | — |
| 352 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 Fast (Non-reasoning) | 0.2872 | — | — | — |
| 353 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mbzuai_small.svg" width="18" alt="MBZUAI Institute of Foundation Models" /> MBZUAI Institute of Foundation Models | K2-V2 (high) | 0.2865 | — | — | — |
| 354 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE (Non-reasoning) | 0.2860 | — | — | — |
| 355 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 (Jan) | 0.2853 | — | — | — |
| 356 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3.1 | 0.2840 | 1,767.97 | 0.0259 | ❌ |
| 357 | <img src="https://artificialanalysis.ai/img/logos//img/logos/korea-telecom_small.png" width="18" alt="Korea Telecom" /> Korea Telecom | Mi:dm K 2.5 Pro | 0.2835 | — | — | — |
| 358 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (Non-reasoning) | 0.2819 | 1,085.86 | 0.0083 | ❌ |
| 359 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 4 Maverick | 0.2815 | 2,995.58 | 0.0510 | ❌ |
| 360 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-20b (high) | 0.2804 | 506.65 | 0.0011 | ❌ |
| 361 | <img src="https://artificialanalysis.ai/img/logos//img/logos/prime-intellect_small.svg" width="18" alt="Prime Intellect" /> Prime Intellect | INTELLECT-3 | 0.2772 | — | — | — |
| 362 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano Omni 30B A3B | 0.2762 | — | — | — |
| 363 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B A3B 2507 | 0.2759 | 6,105.49 | 0.1411 | ❌ |
| 364 | <img src="https://artificialanalysis.ai/img/logos//img/logos/trillionlabs_small.svg" width="18" alt="Trillion Labs" /> Trillion Labs | Tri-21B-think Preview | 0.2755 | — | — | — |
| 365 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 30B A3B (Reasoning) | 0.2746 | 6,105.49 | 0.1411 | ❌ |
| 366 | <img src="https://artificialanalysis.ai/img/logos//img/logos/longcat_small.svg" width="18" alt="LongCat" /> LongCat | LongCat Flash Lite | 0.2741 | — | — | — |
| 367 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-20b (low) | 0.2732 | 536.92 | 0.0017 | ❌ |
| 368 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.1 405B | 0.2722 | — | — | — |
| 369 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova Premier | 0.2714 | 14,648.62 | 0.3653 | ❌ |
| 370 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 mini | 0.2708 | 2,126.10 | 0.0336 | ❌ |
| 371 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 E4B (Non-reasoning) | 0.2703 | 63.97 | 0.0000 | ❌ |
| 372 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 2.6 Flash | 0.2703 | — | — | — |
| 373 | <img src="https://artificialanalysis.ai/img/logos//img/logos/trillionlabs_small.svg" width="18" alt="Trillion Labs" /> Trillion Labs | Tri-21B-Think | 0.2697 | — | — | — |
| 374 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.2 3B | 0.2678 | 386.87 | 0.0000 | ❌ |
| 375 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (Non-reasoning) | 0.2628 | 1,798.64 | 0.0266 | ❌ |
| 376 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 32B | 0.2624 | 509.22 | 0.0012 | ❌ |
| 377 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Next 80B A3B | 0.2622 | 1,152.79 | 0.0089 | ❌ |
| 378 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nousresearch_small.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 405B | 0.2605 | 8,027.46 | 0.1765 | ❌ |
| 379 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral 2 | 0.2603 | 0.00 | 0.0000 | ❌ |
| 380 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mbzuai_small.svg" width="18" alt="MBZUAI Institute of Foundation Models" /> MBZUAI Institute of Foundation Models | K2-V2 (medium) | 0.2576 | — | — | — |
| 381 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-1T | 0.2569 | — | — | — |
| 382 | <img src="https://artificialanalysis.ai/img/logos//img/logos/motif_small.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif-2-12.7B | 0.2563 | — | — | — |
| 383 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-120b (low) | 0.2558 | 2,862.50 | 0.0493 | ❌ |
| 384 | <img src="https://artificialanalysis.ai/img/logos//img/logos/korea-telecom_small.png" width="18" alt="Korea Telecom" /> Korea Telecom | Mi:dm K 2.5 Pro Preview | 0.2556 | — | — | — |
| 385 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.5 Haiku | 0.2540 | — | — | — |
| 386 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 8B (Reasoning) | 0.2534 | 5,344.94 | 0.1333 | ❌ |
| 387 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step3 VL 10B | 0.2520 | — | — | — |
| 388 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Super 49B v1.5 | 0.2496 | 1,210.98 | 0.0093 | ❌ |
| 389 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.0 Flash | 0.2491 | — | — | — |
| 390 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7-Flash (Non-reasoning) | 0.2488 | 314.89 | 0.0000 | ❌ |
| 391 | <img src="https://artificialanalysis.ai/img/logos//img/logos/baidu_small.svg" width="18" alt="Baidu" /> Baidu | ERNIE 4.5 300B A47B | 0.2462 | — | — | — |
| 392 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Magistral Medium 1 | 0.2458 | — | — | — |
| 393 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral Medium | 0.2438 | — | — | — |
| 394 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B 2507 | 0.2430 | — | — | — |
| 395 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4 | 0.2429 | — | — | — |
| 396 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (Non-reasoning) | 0.2425 | — | — | — |
| 397 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 4 (Non-reasoning) | 0.2422 | 446.75 | 0.0000 | ❌ |
| 398 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nousresearch_small.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 405B (Non-reasoning) | 0.2408 | 2,337.53 | 0.0402 | ❌ |
| 399 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder 30B A3B | 0.2396 | 1,923.18 | 0.0291 | ❌ |
| 400 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-8B-A1B | 0.2374 | — | — | — |
| 401 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 30B A3B | 0.2369 | 702.77 | 0.0042 | ❌ |
| 402 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral Small 2 | 0.2366 | 0.00 | 0.0000 | ❌ |
| 403 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6V (Non-reasoning) | 0.2361 | 782.65 | 0.0052 | ❌ |
| 404 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 E2B | 0.2348 | — | — | — |
| 405 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Omni 30B A3B (Reasoning) | 0.2344 | 2,556.86 | 0.0449 | ❌ |
| 406 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-2.6B | 0.2338 | — | — | — |
| 407 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B | 0.2305 | 21,369.22 | 0.4889 | ❌ |
| 408 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5V | 0.2295 | 4,816.47 | 0.1241 | ❌ |
| 409 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 12B v2 VL | 0.2286 | 1,605.49 | 0.0222 | ❌ |
| 410 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Large 2 (Nov) | 0.2276 | — | — | — |
| 411 | <img src="https://artificialanalysis.ai/img/logos//img/logos/tii_small.svg" width="18" alt="TII UAE" /> TII UAE | Falcon-H1R-7B | 0.2261 | — | — | — |
| 412 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Ultra | 0.2253 | — | — | — |
| 413 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3 (Dec) | 0.2196 | — | — | — |
| 414 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nanbeige_small.png" width="18" alt="Nanbeige" /> Nanbeige | Nanbeige4.1-3B | 0.2162 | — | — | — |
| 415 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova Pro | 0.2161 | — | — | — |
| 416 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3.1 32B Think | 0.2152 | — | — | — |
| 417 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3.2 | 0.2148 | 237.50 | 0.0000 | ❌ |
| 418 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam 105B (high) | 0.2147 | — | — | — |
| 419 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.0 32B | 0.2138 | — | — | — |
| 420 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Magistral Small 1.2 | 0.2130 | — | — | — |
| 421 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mbzuai_small.svg" width="18" alt="MBZUAI Institute of Foundation Models" /> MBZUAI Institute of Foundation Models | K2-V2 (low) | 0.2118 | — | — | — |
| 422 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 9B V2 | 0.2114 | 421.10 | 0.0000 | ❌ |
| 423 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 2B | 0.2111 | — | — | — |
| 424 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-flash-2.0 | 0.2089 | — | — | — |
| 425 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Non-reasoning) | 0.2088 | 384.49 | 0.0000 | ❌ |
| 426 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Super 49B v1.5 (Non-reasoning) | 0.2071 | 638.17 | 0.0033 | ❌ |
| 427 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nousresearch_small.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 70B | 0.2054 | — | — | — |
| 428 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 4 Scout | 0.2051 | 502.51 | 0.0011 | ❌ |
| 429 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral Small (May) | 0.2041 | — | — | — |
| 430 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 32B | 0.2041 | 1,684.39 | 0.0241 | ❌ |
| 431 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova Lite | 0.2036 | 332.63 | 0.0000 | ❌ |
| 432 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 32B | 0.2009 | — | — | — |
| 433 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.3 Nemotron Super 49B | 0.2006 | — | — | — |
| 434 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen2.5 72B | 0.1995 | — | — | — |
| 435 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-flash-2.0 | 0.1985 | 370.67 | 0.0000 | ❌ |
| 436 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 8B | 0.1981 | 625.45 | 0.0031 | ❌ |
| 437 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 14B | 0.1978 | 10,684.61 | 0.2380 | ❌ |
| 438 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B | 0.1966 | 6,105.49 | 0.1411 | ❌ |
| 439 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Magistral Small 1 | 0.1965 | — | — | — |
| 440 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Ministral 3 14B | 0.1927 | 221.25 | 0.0000 | ❌ |
| 441 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Large 2 (Jul) | 0.1919 | — | — | — |
| 442 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 2 | 0.1915 | — | — | — |
| 443 | <img src="https://artificialanalysis.ai/img/logos//img/logos/cohere_small.svg" width="18" alt="Cohere" /> Cohere | Command A | 0.1913 | 7,220.51 | 0.1618 | ❌ |
| 444 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral Small | 0.1906 | — | — | — |
| 445 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B (Non-reasoning) | 0.1905 | 2,213.12 | 0.0364 | ❌ |
| 446 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3.1 | 0.1896 | 237.65 | 0.0000 | ❌ |
| 447 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.1 Nemotron 70B | 0.1891 | 1,710.80 | 0.0247 | ❌ |
| 448 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano 4B | 0.1873 | — | — | — |
| 449 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 4B (Reasoning) | 0.1866 | — | — | — |
| 450 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3 Haiku | 0.1853 | — | — | — |
| 451 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.3 Nemotron Super 49B (Non-reasoning) | 0.1840 | — | — | — |
| 452 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B A3B 2507 (Non-reasoning) | 0.1821 | 706.83 | 0.0043 | ❌ |
| 453 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B | 0.1808 | — | — | — |
| 454 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.1 70B | 0.1803 | 637.51 | 0.0033 | ❌ |
| 455 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 9B V2 (Non-reasoning) | 0.1798 | 171.78 | 0.0000 | ❌ |
| 456 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 32B (Non-reasoning) | 0.1789 | 571.67 | 0.0023 | ❌ |
| 457 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5V (Non-reasoning) | 0.1781 | 1,449.90 | 0.0137 | ❌ |
| 458 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 E2B (Non-reasoning) | 0.1780 | — | — | — |
| 459 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 2B (Non-reasoning) | 0.1758 | — | — | — |
| 460 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.1 30B | 0.1754 | — | — | — |
| 461 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3.1 32B Instruct | 0.1725 | — | — | — |
| 462 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Omni 30B A3B | 0.1709 | 793.32 | 0.0054 | ❌ |
| 463 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (minimal) | 0.1701 | 325.75 | 0.0000 | ❌ |
| 464 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B 2507 (Non-reasoning) | 0.1689 | — | — | — |
| 465 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.1 8B | 0.1674 | 41.52 | 0.0000 | ❌ |
| 466 | <img src="https://artificialanalysis.ai/img/logos//img/logos/celeris.svg" width="18" alt="Celeris" /> Celeris | Celeris-1 | 0.1665 | 1,033.16 | 0.0079 | ❌ |
| 467 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o mini | 0.1650 | 1,170.60 | 0.0090 | ❌ |
| 468 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 32B Think | 0.1648 | — | — | — |
| 469 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 14B | 0.1644 | — | — | — |
| 470 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Llama 70B | 0.1644 | 3,119.22 | 0.0526 | ❌ |
| 471 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 nano | 0.1640 | 536.64 | 0.0017 | ❌ |
| 472 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.3 70B | 0.1636 | 7,012.48 | 0.1496 | ❌ |
| 473 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi Linear 48B A3B Instruct | 0.1632 | — | — | — |
| 474 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Ministral 3 8B | 0.1628 | 164.28 | 0.0000 | ❌ |
| 475 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 2 (Non-reasoning) | 0.1618 | — | — | — |
| 476 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nousresearch_small.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 70B (Non-reasoning) | 0.1588 | — | — | — |
| 477 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai21_small.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba Reasoning 3B | 0.1582 | — | — | — |
| 478 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.0 32B (Non-reasoning) | 0.1562 | — | — | — |
| 479 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.1 8B | 0.1560 | 85.90 | 0.0000 | ❌ |
| 480 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova Micro | 0.1534 | 204.77 | 0.0000 | ❌ |
| 481 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 24B A2B | 0.1528 | — | — | — |
| 482 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai21_small.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba 1.7 Large | 0.1517 | — | — | — |
| 483 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam 30B (high) | 0.1499 | — | — | — |
| 484 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 8B | 0.1494 | 5,344.94 | 0.1333 | ❌ |
| 485 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3 | 0.1486 | 237.95 | 0.0000 | ❌ |
| 486 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 12B v2 VL (Non-reasoning) | 0.1482 | 586.52 | 0.0025 | ❌ |
| 487 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openbmb_small.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM-V 4.6 1.3B | 0.1477 | — | — | — |
| 488 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B (Non-reasoning) | 0.1436 | 697.08 | 0.0041 | ❌ |
| 489 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano (Non-reasoning) | 0.1409 | 158.44 | 0.0000 | ❌ |
| 490 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H Small | 0.1378 | 279.72 | 0.0000 | ❌ |
| 491 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 4B | 0.1374 | — | — | — |
| 492 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 27B | 0.1367 | — | — | — |
| 493 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 0528 Qwen3 8B | 0.1338 | — | — | — |
| 494 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Ministral 3 3B | 0.1325 | 117.70 | 0.0000 | ❌ |
| 495 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 14B (Non-reasoning) | 0.1317 | 1,122.40 | 0.0086 | ❌ |
| 496 | <img src="https://artificialanalysis.ai/img/logos//img/logos/microsoft_small.svg" width="18" alt="Microsoft" /> Microsoft | Phi-4 | 0.1271 | 367.62 | 0.0000 | ❌ |
| 497 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.1 Nemotron Nano 4B v1.1 | 0.1268 | — | — | — |
| 498 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 270M | 0.1244 | — | — | — |
| 499 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3 70B | 0.1190 | — | — | — |
| 500 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.2 11B (Vision) | 0.1186 | 362.80 | 0.0000 | ❌ |
| 501 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.2 3B | 0.1168 | — | — | — |
| 502 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 0.8B | 0.1155 | — | — | — |
| 503 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 7B Think | 0.1150 | — | — | — |
| 504 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-1.2B-Instruct | 0.1084 | — | — | — |
| 505 | <img src="https://artificialanalysis.ai/img/logos//img/logos/reka_small.svg" width="18" alt="Reka AI" /> Reka AI | Reka Flash 3 | 0.1079 | — | — | — |
| 506 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 2.6B | 0.1076 | — | — | — |
| 507 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-mini-2.0 | 0.1074 | — | — | — |
| 508 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 8B (Non-reasoning) | 0.1063 | 538.75 | 0.0017 | ❌ |
| 509 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Molmo2-8B | 0.1033 | — | — | — |
| 510 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam M | 0.1029 | — | — | — |
| 511 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai21_small.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba 1.7 Mini | 0.1016 | — | — | — |
| 512 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-1.2B-Thinking | 0.1002 | — | — | — |
| 513 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 12B | 0.0982 | — | — | — |
| 514 | <img src="https://artificialanalysis.ai/img/logos//img/logos/microsoft_small.svg" width="18" alt="Microsoft" /> Microsoft | Phi-4 Mini | 0.0980 | 0.00 | 0.0000 | ❌ |
| 515 | <img src="https://artificialanalysis.ai/img/logos//img/logos/swiss-ai-initiative_small.png" width="18" alt="Swiss AI Initiative" /> Swiss AI Initiative | Apertus 70B Instruct | 0.0935 | — | — | — |
| 516 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 0.8B (Non-reasoning) | 0.0929 | — | — | — |
| 517 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 7B | 0.0919 | — | — | — |
| 518 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | OLMo 2 32B | 0.0910 | — | — | — |
| 519 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | Exaone 4.0 1.2B | 0.0909 | — | — | — |
| 520 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H 1B | 0.0904 | — | — | — |
| 521 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.2 1B | 0.0895 | — | — | — |
| 522 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 1.7B | 0.0880 | — | — | — |
| 523 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.1 3B | 0.0864 | — | — | — |
| 524 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | Exaone 4.0 1.2B (Non-reasoning) | 0.0839 | — | — | — |
| 525 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 8B A1B | 0.0822 | — | — | — |
| 526 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 Micro | 0.0795 | — | — | — |
| 527 | <img src="https://artificialanalysis.ai/img/logos//img/logos/microsoft_small.svg" width="18" alt="Microsoft" /> Microsoft | Phi-3 Mini | 0.0751 | — | — | — |
| 528 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 3.3 8B | 0.0712 | 246.62 | 0.0000 | ❌ |
| 529 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-VL-1.6B | 0.0685 | — | — | — |
| 530 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 1B | 0.0678 | — | — | — |
| 531 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 350M | 0.0670 | — | — | — |
| 532 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 4B | 0.0660 | — | — | — |
| 533 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 1.2B | 0.0651 | — | — | — |
| 534 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 0.6B | 0.0644 | — | — | — |
| 535 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3 8B | 0.0642 | — | — | — |
| 536 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral 7B | 0.0620 | 274.03 | 0.0000 | ❌ |
| 537 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3n E4B | 0.0580 | — | — | — |
| 538 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mbzuai_small.svg" width="18" alt="MBZUAI Institute of Foundation Models" /> MBZUAI Institute of Foundation Models | K2 Horizon 0.9B | 0.0567 | — | — | — |
| 539 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | OLMo 2 7B | 0.0564 | — | — | — |
| 540 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 1.7B (Non-reasoning) | 0.0561 | — | — | — |
| 541 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 1B | 0.0557 | — | — | — |
| 542 | <img src="https://artificialanalysis.ai/img/logos//img/logos/swiss-ai-initiative_small.png" width="18" alt="Swiss AI Initiative" /> Swiss AI Initiative | Apertus 8B Instruct | 0.0547 | — | — | — |
| 543 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H 350M | 0.0505 | — | — | — |
| 544 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Molmo 7B-D | 0.0477 | — | — | — |
| 545 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 0.6B (Non-reasoning) | 0.0432 | — | — | — |
| 546 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3n E2B | 0.0355 | — | — | — |
| 547 | <img src="https://artificialanalysis.ai/img/logos//img/logos/cohere_small.svg" width="18" alt="Cohere" /> Cohere | Tiny Aya Global | 0.0351 | — | — | — |
| 548 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 1.5B | 0.0000 | — | — | — |

## 品牌帕累托前沿连线（仅体现在图中）

以下十一个品牌在图中拥有单独的帕累托连线（较窄宽度，品牌主题色，图层高于总体灰色连线）。表中数量为**入图顶点数**——品牌前沿上低于总体前沿第一级的顶点同样不入图（本表与图例一致）：

| 品牌 | 主题色 | 品牌前沿模型数（入图） |
|------|--------|--------------|
| <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | `#cc785c` | 11 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | `#1f1f1f` | 10 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | `#0089f4` | 2 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | `#1c7ff8` | 2 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | `#34A853` | 4 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | `#736cd3` | 5 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | `#047AFE` | 3 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | `#ff7018` | 4 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | `#2243e6` | 3 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | `#EB3568` | 1 |

## 评分方法

1. **20项评估指标**各自线性归一化到 [0,1]
   （AA Intelligence Index、GPQA Diamond、Humanity's Last Exam、MMMU Pro、IFBench Instruction Following、SciCode Coding、CritPt Physics、AA-LCR Long Context、AA Omniscience Index、AA-Omniscience Accuracy、AA-Omniscience Non-Hallucination、GDPval-AA Normalized、AA Analyst Agent、APEX-Agents-AA、ITBench-SRE、τ²-Bench Telecom、τ³-Bench Banking、Terminal-Bench Hard、Terminal-Bench 2.1、Terminal-Bench 4.0）
   > V18（2026-09-12）：AA 更新了基准列——新增 AA Analyst Agent、τ³-Bench Banking、Terminal-Bench 2.1 / 4.0 四项；AA Agentic Index 与 AA Coding Index 已从 AA 的数据源中移除，相应剔除。指标数由 18 → 20。
2. **综合能力值** = 所有有效归一化分数的算术平均
3. **综合能力再归一化**：线性映射到 [0,1]，性能最好的模型 = 1，最差的模型 = 0
4. **Pareto前沿** = 不被任何其他模型支配的模型（综合能力 ≥ 且成本 ≤，且至少一项严格更优；成本为 0 的免费模型同样参与——横轴左端恒为 0，免费模型是合法前沿候选）
5. **模型范围** = Status: All（含已弃用模型；缺少足够评估数据者不参与排名）
6. **图表纵轴基线（V17）**：图表的 y = 0 取总体帕累托前沿的第一级（最低能力；本例 y0 = 0.6320，即前沿左端点 Ling-3.0-flash-VL）；综合能力低于该级的模型不出现在图表中（表格不受影响）。图中纵坐标 chart_y = (能力 - y0)/(1 - y0)，因此前沿左端点恰好落在 (0, 0)、最优模型恰好为 y = 1。该过滤在横轴映射构建之前完成


## 横轴映射（分位数等密度映射，V17）与分布分析

横轴（单请求成本）按**经验分位数（rank）映射**——以 94 个入图正成本模型（综合能力 ≥ 前沿第一级）的成本分布为基准：

```
x = 0                            当 c ≤ 0（免费模型，钉在最左缘）
x = interp(log10(c); knots)      当 c > 0
```

其中 knots = (log10(c_i), 名次_i/(n-1)) 为入图正成本模型按成本排序后的 87 个锚点（相同 log10(c) 的并列组取平均名次，保证 x 是 z = log10(c) 的单值函数；n-1 归一化使最大成本恰为 x = 1）。该映射在 **y 基线过滤之后**构建（V17：先以帕累托前沿第一级为 y = 0、剔除低性能模型，再对入图模型建映射）。（V18 修正：并列判定改用相同的 log10(c)，消除浮点上相差 ~1e-12 的成本经 log10 后折合到同一 z 造成的同 z 双锚点、个别模型 x 偏离名次的问题；修正后 x 对每个入图模型严格线性于名次。）

**该映射保证：**

- **函数端点严格钉死**：c = 0 → x = 0；最大成本 → x = 1——函数经过 (0,0) 与 (1,1)；
- **严格均匀密度**：x 是模型名次的线性函数（相同 log10(c) 并列组取平均名次），因此**任意等宽区段的模型数恒定**（每 0.1 宽度约 9 个模型）——无论截取哪一段，模型数 ÷ 宽度都等于全图的模型总数 ÷ 总宽度。V12 的单一 logistic 函数在过滤后的分布上做不到（十分位在 8~24 间摆动），故替换为精确分位数映射；
- 各数量级区间的入图模型数：1–10: 0，10–100: 0，100–1k: 1，1k–10k: 20，10k–100k: 59
- **同一倍率区间的宽度 ∝ 该区间模型数**——均匀密度的必然结果：1k→10k 与 100k→1M 同为 10 倍率，但前者 20 个模型、后者 14 个，前者宽度约为后者的 1.4 倍。若改用「等倍率等距」（纯对数轴），两段的模型密度将相差 1.4 倍，与均匀密度目标冲突——两者数学上不可兼得，本图以均匀密度（最高优先级）为准；
- **左端恒为 0**（c = 0；1 个免费模型位于最左缘）
- 最低正成本 448.74 → x = 0.0000；最高成本 925,406 → x = 1.0000（严格 = 1）
- 中位数位置 0.495（≈ 0.5 居中）；左右两半模型数：左 48 / 右 47
- 横轴十分位模型数：11，9，10，8，10，9，9，10，9，10（x 为名次的线性函数；n/10 非整数时各十分位在 ±1 内取整，相同 log10(c) 并列组共享同一 x、落在边界的哪一侧可再移动 ±1）
- **10^x 数量级指示**（位置 = x(10^x)）：10^0 → 0.000，10^1 → 0.000，10^2 → 0.000，10^3 → 0.008，10^4 → 0.221，10^5 → 0.859

## 图中标注规则

品牌帕累托前沿模型全部标注。V13/V15/V16 规则：

1. **品牌公共前缀剔除（最长有效切点）**：品牌全部前沿模型共享的前导块被剔除 —— 切点须止于分界符（空格/连字符/下划线，如 'Claude '、'GPT-'、'GLM-'、'Grok '、'DeepSeek V4 '），或止于字母且每个名称在切点后紧跟数字（品牌/系列字母 + 版本号，如 'Kimi K|2.6'、'Qwen|3.8'、'MiMo-V|2.5'、'MiniMax-M|2.1'）—— 实例：Claude Opus 5 (high) → Opus 5 (high)、GPT-5.6 Sol → 5.6 Sol、Kimi K2.6 → 2.6、Qwen3.8 Max → 3.8 Max、MiMo-V2.5-Pro → 2.5-Pro；剔除后任一名称为空或产生重复标签则该切点作废，顺次尝试更短切点；
2. **(non-reasoning) → (non)**：思考程度中的 Non-reasoning 简写为 non（含组合式：Non-reasoning, high → non, high）；
3. **相邻同名 run 短标签（每次重新计算）**：品牌连线上连续 2 个以上顶点属于同一模型时，仅性能最低者（run 首位）保留全名，其后相邻的较高者只标思考程度（如 Opus 5 的 (low) (medium) (high) (xhigh) 序列仅首项带族名）；同名模型不相邻的重复出现不合并、保留全名 —— A-B(high)-B(xhigh)-C-B(max) 标注为 A-B(high)-(xhigh)-C-B(max)，因此交错家族（Gemini 3.7 / 3.8 Flash、Claude Fable 5.1 / Opus 5）始终可分辨。

4. **标签位置与序列同向（V15）**：品牌前沿上越靠右上的模型，其标签重心必须同时更靠右且更靠上 —— 对前沿相邻对 A→B（B 更靠右上），标签位移的两个分量须同时 >= 0（至少是 (0,0)），既不得更左、也不得更低（只要有一个分量非负不算合格；V14 的投影规则会放过「更右但更低」，V15 起视为违反；等成本堆叠即：上方模型的标签既在上方、也不更左）；初始放置违反时就近重摆（不产生新的重叠、不破坏与前后邻居的同向关系，最多 6 轮；单标签重摆无解——标签被前后邻居夹死、局部约束盒为空——时，自动升级为以违规对为中心逐级扩大的窗口级联重排，整段相邻标签作为一个阶梯整体重排，修不好的配对在日志中报告）。

5. **标签摆放四级优先（V16）**：① 尽量多的标签骑在连线段上——点的右侧（去路段）或左侧（来路段）皆可，同一条线段允许容纳两个标签（各贴各的点）；目标骑线位仅被其他标签占据时触发「让位」——占用者挪到自己的另一个骑线位，双方都保持骑线。② 骑不上线的标签在「假设线能放下该标签」的离点最近位置的上方或下方、与线平行摆放（右/左侧 × 上/下方四组合；互相掣肘的标签自然错开成对角组合）。③ 仍放不下时放在点的两条连线延长线上的最近点。④ 最后在两条连线夹角形成的扇区（连线前上方空白区）内就近放置，文字保持与邻近连线平行。

标注文字与连线平行且中轴线重合；文字下方不绘制连线，仅在文字两侧绘制（若两侧仍有区域）；文字使用品牌颜色，无边框、无背景。

## 成本计算公式

**X轴成本 = 单请求估算成本（公式）**

```
cost = (CacheHitRate × CacheHitPrice × InputTokens)
     + ((1 − CacheHitRate) × CacheWritePrice × InputTokens)
     + (SpeedMedian × RealTime × OutputPrice)
```

**参数来源与处理逻辑：**

| 参数 | 来源 | 说明 |
|------|------|------|
| CacheHitRate | [AA Coding Agents](https://artificialanalysis.ai/agents/coding-agents) | 全部模型-Agent搭配的 `cacheHitRate` 求平均（15 个有效值，均值 = 0.9473），对所有模型统一使用 |
| CacheHitPrice | AA `cacheHitPrice` | 缓存命中的输入价格 (USD / 1M tokens) |
| CacheWritePrice | AA `cacheWritePrice` | 若缺失，回退到 `price1mInputTokens` (普通输入价格) |
| InputTokens | `10000` | AA 默认的 10k input-token 工作负载（[方法论](https://artificialanalysis.ai/methodology/performance-benchmarking)） |
| SpeedMedian | AA `medianOutputTokensPerSecond` | 输出速度中位数 (tokens/sec)，10k input-token 工作负载下测量 |
| OutputPrice | AA `price1mOutputTokens` | 输出价格 (USD / 1M tokens) |
| RealTime | 见下 | 生成输出 token 的实际耗时（秒） |

**RealTime 计算逻辑：**

- 如果存在 Reasoning Time（推理模型）：
  `RealTime = End-to-End Response Time Total − Latency First Chunk`
  = `medianEndToEndResponseTimeSeconds − medianTimeToFirstTokenSeconds`
- 如果 Reasoning Time 为 `--`（非推理模型）：
  `RealTime = End-to-End Response Time Total`
  = `medianEndToEndResponseTimeSeconds`

**单位说明：** AA 价格以 USD / 1M tokens 为单位，InputTokens 为原始计数（10000），Speed 为 tokens/sec，RealTime 为秒。公式按原样计算，不做单位换算。最终成本是一个相对得分（用于 Pareto 比较和对数映射），不是真实的美元金额。

### 数据来源

**主数据源**: [Artificial Analysis Leaderboard](https://artificialanalysis.ai/leaderboards/models)（Status: All）  
**Cache Hit Rate 数据源**: [AA Coding Agents](https://artificialanalysis.ai/agents/coding-agents)  
**性能方法论**: [AA Performance Benchmarking](https://artificialanalysis.ai/methodology/performance-benchmarking)  
**模型总数（Status: All）**: 548 个参与排名（另有模型因评估数据不足未列入；总体帕累托前沿 12 个；图表入图 95 个——综合能力 ≥ 前沿第一级）  

## 图表说明（黑底）

（V17 起本说明置于文末，图表之后直接跟随模型表格。）

图表说明：**灰色实线** = 总体帕累托前沿；**彩色细线** = 十一个品牌的单独帕累托前沿（品牌主题色，图层高于总体连线；暗色品牌元素带窄白边；顶点按（横轴位置、能力升序）连接，等成本点自下而上）；品牌前沿模型圆点同样使用品牌颜色。模型名称/思考程度标注优先骑在连线之上（点的左/右两侧皆可，同一条线段可容纳两个标签——各贴各的点；文字与连线平行、中轴线重合，连线仅在文字两侧绘制）；骑线位被其他标签占据时自动「让位」——占用者挪到自己的另一个骑线位，双方都保持骑线；实在骑不上线时按四级优先依次退让（V16）：离点最近位置的上方/下方平行偏移 → 点的两条连线延长线上就近 → 两连线夹角扇区内就近。标签规则（V13/V15）：品牌前沿模型共享的前导块按「最长有效切点」剔除 —— 切点止于分界符，或止于字母且其后紧跟数字（如 Claude Opus 5 → Opus 5、GPT-5.6 Sol → 5.6 Sol、Kimi K2.6 → 2.6、Qwen3.8 Max → 3.8 Max、MiMo-V2.5 → 2.5、MiniMax-M2.1 → 2.1）；(non-reasoning) 简写为 (non)；同一模型在品牌连线上相邻出现 2 次以上时仅性能最低者保留全名、相邻较高者只标思考程度，不相邻的重复出现保留全名（每次重新计算）；标签位置与序列同向（V15）——品牌前沿上越靠右上的模型，其标签重心必须同时更靠右且更靠上（两分量都 >= 0，至少是 (0,0)，仅其一非负不算合格；初始放置违反时自动就近重摆，单标签无解（被前后邻居夹死）时按窗口级联重排整体挪动，均不产生新的重叠）。纵轴 y = 0 = 总体帕累托前沿第一级（y0 = 0.6320，前沿左端点 Ling-3.0-flash-VL 恰为 (0,0)），能力低于该级的 439 个模型与缺少成本数据的 14 个模型不出现在图中；横轴为分位数等密度映射（见上文「横轴映射」节），10^x 数量级指示位于 x(10^x)，同一倍率区间的宽度与该区间内模型数成正比。
