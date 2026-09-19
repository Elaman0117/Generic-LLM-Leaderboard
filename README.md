# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

## 全部模型（综合能力从高到低，最优 = 1，最差 = 0）

共收录 **Status: All**（含已弃用）的全部模型；按重新归一化后的综合能力排序。「帕累托」列：✅ = 总体帕累托前沿模型，❌ = 被支配，— = 无成本数据无法判定。图表纵轴以总体帕累托前沿第一级（y0 = 0.6339，即前沿左端点 Ling-3.0-flash-VL）为 0：综合能力 ≥ 该级且有成本数据的 95 个模型入图，440 个能力低于第一级、15 个缺少成本数据的模型不出现在图中（本表不受影响，仍完整列出全部模型）。

| # | 品牌 | 模型 | 综合能力 | 单请求成本 | 横轴位置 | 帕累托 |
|---|------|------|---------|-----------|-----------|------|
| 1 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (max with fallback) | 1.0000 | 901,601.53 | 1.0000 | ✅ |
| 2 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (xhigh with fallback) | 0.9907 | 328,481.14 | 0.9570 | ✅ |
| 3 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (xhigh) | 0.9795 | 445,817.06 | 0.9785 | ❌ |
| 4 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (max) | 0.9767 | 857,676.44 | 0.9892 | ❌ |
| 5 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (high) | 0.9604 | 169,007.50 | 0.9140 | ✅ |
| 6 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (max) | 0.9603 | 104,868.11 | 0.8602 | ✅ |
| 7 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (high with fallback) | 0.9580 | 73,798.66 | 0.8387 | ✅ |
| 8 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5 (with fallback) | 0.9500 | 352,300.10 | 0.9677 | ❌ |
| 9 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (xhigh) | 0.9500 | 70,101.22 | 0.8280 | ✅ |
| 10 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (medium) | 0.9388 | 54,032.21 | 0.7634 | ✅ |
| 11 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.3 (max) | 0.9369 | 12,705.20 | 0.2903 | ✅ |
| 12 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (high) | 0.9358 | 47,164.56 | 0.7097 | ❌ |
| 13 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (max) | 0.9301 | 173,682.41 | 0.9247 | ❌ |
| 14 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.3 (xhigh) | 0.9299 | 12,705.20 | 0.2903 | ✅ |
| 15 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (medium with fallback) | 0.9254 | 48,784.92 | 0.7312 | ❌ |
| 16 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (low) | 0.9012 | 48,002.17 | 0.7204 | ❌ |
| 17 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (medium) | 0.8938 | 25,906.87 | 0.5591 | ❌ |
| 18 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (low with fallback) | 0.8918 | 46,899.97 | 0.6989 | ❌ |
| 19 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3 (max) | 0.8884 | 41,924.14 | 0.6828 | ❌ |
| 20 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (xhigh) | 0.8879 | 66,729.79 | 0.8172 | ❌ |
| 21 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (xhigh) | 0.8859 | 21,006.30 | 0.4624 | ❌ |
| 22 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (high) | 0.8814 | 24,630.50 | 0.5484 | ❌ |
| 23 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (high) | 0.8806 | 20,372.24 | 0.4516 | ❌ |
| 24 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (medium) | 0.8766 | 21,308.68 | 0.4731 | ❌ |
| 25 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (xhigh) | 0.8759 | 146,588.79 | 0.9032 | ❌ |
| 26 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3 (max) | 0.8697 | 14,201.30 | 0.3495 | ❌ |
| 27 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (high) | 0.8682 | 33,978.97 | 0.6237 | ❌ |
| 28 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 Max (0902) | 0.8656 | 18,423.05 | 0.4086 | ❌ |
| 29 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.8 (max) | 0.8621 | 62,828.98 | 0.7957 | ❌ |
| 30 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (max) | 0.8606 | 232,681.08 | 0.9355 | ❌ |
| 31 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (high) | 0.8555 | 62,219.92 | 0.7849 | ❌ |
| 32 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step 5 Preview | 0.8545 | 7,751.08 | 0.1613 | ✅ |
| 33 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (high) | 0.8519 | 15,818.45 | 0.3763 | ❌ |
| 34 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (medium) | 0.8496 | — | — | — |
| 35 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 Max | 0.8474 | 18,423.05 | 0.3925 | ❌ |
| 36 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (medium) | 0.8424 | 22,443.79 | 0.5269 | ❌ |
| 37 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.2 (xhigh) | 0.8389 | 12,705.20 | 0.2903 | ❌ |
| 38 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 2.4T A95B | 0.8322 | 18,423.05 | 0.3925 | ❌ |
| 39 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (low) | 0.8190 | 24,342.54 | 0.5376 | ❌ |
| 40 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (max) | 0.8180 | 108,679.07 | 0.8817 | ❌ |
| 41 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3-Flash | 0.8167 | 1,575.40 | 0.0108 | ✅ |
| 42 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.5 (high) | 0.8158 | 9,630.29 | 0.2043 | ❌ |
| 43 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.7 (max) | 0.8153 | 50,838.98 | 0.7527 | ❌ |
| 44 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (xhigh) | 0.8125 | 275,581.41 | 0.9462 | ❌ |
| 45 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash | 0.8117 | 34,764.66 | 0.6344 | ❌ |
| 46 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (medium) | 0.8076 | 35,805.79 | 0.6452 | ❌ |
| 47 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.2 (max) | 0.8045 | 14,201.30 | 0.3495 | ❌ |
| 48 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (medium) | 0.8036 | 8,257.68 | 0.1828 | ❌ |
| 49 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (xhigh) | 0.8028 | 31,160.74 | 0.6022 | ❌ |
| 50 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.1 Pro Preview | 0.7954 | 58,543.31 | 0.7742 | ❌ |
| 51 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (medium) | 0.7953 | 31,334.31 | 0.6129 | ❌ |
| 52 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.3 Codex (xhigh) | 0.7949 | 105,905.73 | 0.8710 | ❌ |
| 53 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.1 (xhigh) | 0.7896 | — | — | — |
| 54 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (low) | 0.7809 | 19,839.73 | 0.4409 | ❌ |
| 55 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8-Flash-Next | 0.7736 | 1,405.68 | 0.0000 | ✅ |
| 56 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.6 Flash | 0.7722 | 15,199.66 | 0.3656 | ❌ |
| 57 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (high) | 0.7649 | 11,738.59 | 0.2688 | ❌ |
| 58 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sapiens.svg" width="18" alt="Sapiens AI" /> Sapiens AI | Agnes 3.0 Flash | 0.7584 | — | — | — |
| 59 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (low) | 0.7523 | — | — | — |
| 60 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (max) | 0.7523 | 18,569.80 | 0.4194 | ❌ |
| 61 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.6 (max) | 0.7520 | 39,142.97 | 0.6667 | ❌ |
| 62 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (low) | 0.7498 | 3,879.25 | 0.0860 | ❌ |
| 63 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 v2 | 0.7479 | 9,082.41 | 0.1935 | ❌ |
| 64 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro 0813 (max) | 0.7457 | 11,013.04 | 0.2366 | ❌ |
| 65 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (low) | 0.7453 | 11,252.95 | 0.2581 | ❌ |
| 66 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark | 0.7396 | — | — | — |
| 67 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3 Pro Preview (high) | 0.7367 | — | — | — |
| 68 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (medium) | 0.7337 | 7,517.11 | 0.1505 | ❌ |
| 69 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sapiens.svg" width="18" alt="Sapiens AI" /> Sapiens AI | Agnes 2.5 Pro Beta | 0.7329 | — | — | — |
| 70 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.7 Max | 0.7261 | 27,872.42 | 0.5806 | ❌ |
| 71 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash (max) | 0.7237 | 3,215.07 | 0.0430 | ❌ |
| 72 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (xhigh) | 0.7236 | 97,708.37 | 0.8495 | ❌ |
| 73 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 Codex (xhigh) | 0.7229 | — | — | — |
| 74 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (xhigh) | 0.7216 | 8,237.36 | 0.1720 | ❌ |
| 75 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 Max Preview | 0.7214 | 21,588.55 | 0.4839 | ❌ |
| 76 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.6 | 0.7197 | 21,820.69 | 0.5054 | ❌ |
| 77 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (xhigh) | 0.7190 | 6,399.84 | 0.1398 | ❌ |
| 78 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.5 | 0.7080 | 38,931.06 | 0.6559 | ❌ |
| 79 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 | 0.7078 | — | — | — |
| 80 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash Vision (max) | 0.7072 | 3,664.70 | 0.0591 | ❌ |
| 81 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (low) | 0.7063 | 26,625.85 | 0.5699 | ❌ |
| 82 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (xhigh) | 0.7053 | 28,232.03 | 0.5914 | ❌ |
| 83 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.7 (Non-reasoning, high) | 0.7034 | 21,783.99 | 0.4946 | ❌ |
| 84 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash 0731 (max) | 0.7026 | 3,664.70 | 0.0591 | ❌ |
| 85 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (max) | 0.6955 | 66,240.57 | 0.8065 | ❌ |
| 86 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (medium) | 0.6931 | 11,007.90 | 0.2258 | ❌ |
| 87 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3 Flash | 0.6912 | 5,834.97 | 0.1290 | ❌ |
| 88 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M3 | 0.6864 | 3,766.15 | 0.0753 | ❌ |
| 89 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (low) | 0.6850 | 13,463.97 | 0.3226 | ❌ |
| 90 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (high) | 0.6841 | 2,295.98 | 0.0215 | ❌ |
| 91 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.7 Plus | 0.6833 | 4,642.63 | 0.1075 | ❌ |
| 92 | <img src="https://artificialanalysis.ai/img/logos//img/logos/motif_small.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif 3 | 0.6799 | — | — | — |
| 93 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 Plus | 0.6797 | 18,953.29 | 0.4301 | ❌ |
| 94 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (low) | 0.6756 | 5,334.68 | 0.1183 | ❌ |
| 95 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (max) | 0.6741 | 4,504.80 | 0.0968 | ❌ |
| 96 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Pro | 0.6738 | — | — | — |
| 97 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3 (low) | 0.6719 | 41,924.14 | 0.6828 | ❌ |
| 98 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.1 | 0.6688 | 21,976.21 | 0.5161 | ❌ |
| 99 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (medium) | 0.6682 | — | — | — |
| 100 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (high) | 0.6634 | 11,223.97 | 0.2473 | ❌ |
| 101 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (high) | 0.6612 | 2,431.59 | 0.0323 | ❌ |
| 102 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (high) | 0.6588 | 10,048.39 | 0.2151 | ❌ |
| 103 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm_small.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 375B A23B | 0.6585 | — | — | — |
| 104 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 Codex (high) | 0.6546 | — | — | — |
| 105 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 (high) | 0.6519 | 49,211.54 | 0.7419 | ❌ |
| 106 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.7 Code | 0.6496 | 13,216.87 | 0.3118 | ❌ |
| 107 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5 | 0.6494 | 13,957.97 | 0.3333 | ❌ |
| 108 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (xhigh) | 0.6388 | 111,550.24 | 0.8925 | ❌ |
| 109 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 Codex (high) | 0.6362 | — | — | — |
| 110 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-3.0-flash-VL | 0.6339 | 0.00 | 0.0000 | ✅ |
| 111 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (low) | 0.6291 | 10,885.65 | 0.2245 | ❌ |
| 112 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Omni-0327 | 0.6263 | — | — | — |
| 113 | <img src="https://artificialanalysis.ai/img/logos//img/logos/apodex.svg" width="18" alt="Apodex" /> Apodex | Apodex 1.1 | 0.6261 | — | — | — |
| 114 | <img src="https://artificialanalysis.ai/img/logos//img/logos/thinking_machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling | 0.6245 | 12,262.79 | 0.2807 | ❌ |
| 115 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5-Pro | 0.6244 | 2,438.55 | 0.0324 | ❌ |
| 116 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (medium) | 0.6241 | 28,073.20 | 0.5867 | ❌ |
| 117 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (max) | 0.6209 | — | — | — |
| 118 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok Build 0.1 0616 | 0.6197 | 7,421.97 | 0.1497 | ❌ |
| 119 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (high) | 0.6182 | 67,411.04 | 0.8194 | ❌ |
| 120 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5 | 0.6181 | 800.37 | 0.0000 | ❌ |
| 121 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.6 (Non-reasoning, high) | 0.6171 | 22,366.38 | 0.5251 | ❌ |
| 122 | <img src="https://artificialanalysis.ai/img/logos//img/logos/thinking_machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling Small | 0.6168 | 3,726.59 | 0.0690 | ❌ |
| 123 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5-Turbo | 0.6167 | — | — | — |
| 124 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 | 0.6148 | — | — | — |
| 125 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 4 | 0.6131 | 3,726.59 | 0.0690 | ❌ |
| 126 | <img src="https://artificialanalysis.ai/img/logos//img/logos/multiversecomputing_small.svg" width="18" alt="Multiverse Computing" /> Multiverse Computing | Quasar 438B (max) | 0.6082 | 4,816.47 | 0.1104 | ❌ |
| 127 | <img src="https://artificialanalysis.ai/img/logos//img/logos/motif_small.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif 3 (Beta) | 0.6068 | — | — | — |
| 128 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 Instant (May 2026) | 0.6055 | — | — | — |
| 129 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Opus | 0.6034 | — | — | — |
| 130 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nex_small.svg" width="18" alt="Nex AGI" /> Nex AGI | Nex-N2-Pro | 0.6034 | — | — | — |
| 131 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (xhigh) | 0.6026 | 17,412.66 | 0.3865 | ❌ |
| 132 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (high) | 0.6015 | — | — | — |
| 133 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 27B | 0.5976 | 22,550.07 | 0.5275 | ❌ |
| 134 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (minimal) | 0.5951 | 8,303.81 | 0.1834 | ❌ |
| 135 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 27B | 0.5936 | 6,158.24 | 0.1353 | ❌ |
| 136 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash (Feb 2026) | 0.5934 | — | — | — |
| 137 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Sonnet | 0.5934 | 19,158.69 | 0.4326 | ❌ |
| 138 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.5 | 0.5930 | — | — | — |
| 139 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Omni | 0.5918 | — | — | — |
| 140 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Ultra | 0.5912 | 8,870.98 | 0.1909 | ❌ |
| 141 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o3 | 0.5906 | 15,927.97 | 0.3771 | ❌ |
| 142 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Open2 250B | 0.5904 | — | — | — |
| 143 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (medium) | 0.5891 | 9,474.85 | 0.2013 | ❌ |
| 144 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM 5V Turbo | 0.5871 | — | — | — |
| 145 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (medium) | 0.5850 | 8,237.36 | 0.1720 | ❌ |
| 146 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash-Lite | 0.5821 | 10,458.75 | 0.2198 | ❌ |
| 147 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (medium) | 0.5811 | 3,845.17 | 0.0828 | ❌ |
| 148 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 397B A17B | 0.5809 | 13,586.07 | 0.3253 | ❌ |
| 149 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.1 Opus | 0.5791 | — | — | — |
| 150 | <img src="https://artificialanalysis.ai/img/logos//img/logos/tencent_small.svg" width="18" alt="Tencent" /> Tencent | Hy3 | 0.5781 | 1,855.38 | 0.0154 | ❌ |
| 151 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (Non-reasoning, high) | 0.5775 | 13,187.42 | 0.3106 | ❌ |
| 152 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 Thinking | 0.5767 | 6,566.47 | 0.1415 | ❌ |
| 153 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (medium) | 0.5751 | 1,301.57 | 0.0000 | ❌ |
| 154 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.5 (Non-reasoning) | 0.5749 | 21,934.70 | 0.5133 | ❌ |
| 155 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (Non-reasoning) | 0.5733 | 17,826.19 | 0.3890 | ❌ |
| 156 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm_small.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon MoVA 36B A4B | 0.5718 | — | — | — |
| 157 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (Non-reasoning, low) | 0.5718 | 13,227.03 | 0.3123 | ❌ |
| 158 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.7 | 0.5699 | 4,320.55 | 0.0938 | ❌ |
| 159 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.6 (Non-reasoning) | 0.5697 | 4,502.70 | 0.0967 | ❌ |
| 160 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (low) | 0.5696 | 8,237.36 | 0.1720 | ❌ |
| 161 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3 Pro Preview (low) | 0.5693 | — | — | — |
| 162 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (Non-reasoning) | 0.5681 | 9,005.97 | 0.1926 | ❌ |
| 163 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 Codex mini (high) | 0.5599 | — | — | — |
| 164 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sktelecom_small.svg" width="18" alt="SK Telecom" /> SK Telecom | A.X-K2 | 0.5582 | — | — | — |
| 165 | <img src="https://artificialanalysis.ai/img/logos//img/logos/china_mobile_small.png" width="18" alt="China Mobile" /> China Mobile | JT-4.1 Flash 236B A21B | 0.5578 | — | — | — |
| 166 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (low) | 0.5568 | 12,569.41 | 0.2874 | ❌ |
| 167 | <img src="https://artificialanalysis.ai/img/logos//img/logos/tencent_small.svg" width="18" alt="Tencent" /> Tencent | Hy3-preview | 0.5563 | — | — | — |
| 168 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 35B A3B | 0.5561 | 13,461.55 | 0.3225 | ❌ |
| 169 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.5 | 0.5504 | 3,481.97 | 0.0528 | ❌ |
| 170 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.1 (Non-reasoning) | 0.5503 | 5,684.08 | 0.1259 | ❌ |
| 171 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 Omni Plus | 0.5490 | 3,513.45 | 0.0539 | ❌ |
| 172 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (high) | 0.5470 | 14,097.67 | 0.3426 | ❌ |
| 173 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 122B A10B | 0.5444 | 8,210.98 | 0.1715 | ❌ |
| 174 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sapiens.svg" width="18" alt="Sapiens AI" /> Sapiens AI | Agnes 2.5 Pro Alpha | 0.5424 | 2,582.08 | 0.0346 | ❌ |
| 175 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.1 Fast | 0.5421 | — | — | — |
| 176 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step 3.7 Flash | 0.5379 | 3,359.39 | 0.0484 | ❌ |
| 177 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | G9v3-39A5B | 0.5372 | — | — | — |
| 178 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano | 0.5361 | 1,767.40 | 0.0140 | ❌ |
| 179 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max Thinking | 0.5355 | — | — | — |
| 180 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.1 | 0.5353 | 3,158.24 | 0.0423 | ❌ |
| 181 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 35B A3B | 0.5294 | 5,131.86 | 0.1153 | ❌ |
| 182 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B | 0.5278 | 2,762.06 | 0.0372 | ❌ |
| 183 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.0 Flash | 0.5265 | 731.65 | 0.0000 | ❌ |
| 184 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7 | 0.5260 | 11,500.00 | 0.2636 | ❌ |
| 185 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.5 (Non-reasoning) | 0.5244 | — | — | — |
| 186 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 | 0.5242 | — | — | — |
| 187 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash | 0.5231 | — | — | — |
| 188 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (low) | 0.5230 | 1,182.40 | 0.0000 | ❌ |
| 189 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (low) | 0.5227 | 9,118.04 | 0.1943 | ❌ |
| 190 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kwaikat_small.svg" width="18" alt="KwaiKAT" /> KwaiKAT | KAT-Coder-Pro V2 | 0.5224 | — | — | — |
| 191 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (medium) | 0.5223 | 6,926.78 | 0.1451 | ❌ |
| 192 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-3.0-flash-Fin | 0.5214 | 0.00 | 0.0000 | ❌ |
| 193 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 31B | 0.5195 | 0.00 | 0.0000 | ❌ |
| 194 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3 Flash (Non-reasoning) | 0.5175 | 2,781.88 | 0.0374 | ❌ |
| 195 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Glimmer (high) | 0.5156 | 4,313.51 | 0.0937 | ❌ |
| 196 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Sonnet | 0.5138 | — | — | — |
| 197 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5 (Non-reasoning) | 0.5129 | 4,289.37 | 0.0932 | ❌ |
| 198 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 397B A17B (Non-reasoning) | 0.5066 | 2,744.59 | 0.0369 | ❌ |
| 199 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step 3.5 Flash 2603 | 0.5058 | 992.20 | 0.0000 | ❌ |
| 200 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 Instant (June 2026) | 0.5050 | 82,373.56 | 0.8429 | ❌ |
| 201 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (Non-reasoning) | 0.5030 | 24,765.12 | 0.5495 | ❌ |
| 202 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 Fast | 0.4998 | — | — | — |
| 203 | <img src="https://artificialanalysis.ai/img/logos//img/logos/cohere_small.svg" width="18" alt="Cohere" /> Cohere | Command A+ | 0.4931 | 0.00 | 0.0000 | ❌ |
| 204 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 3 mini Reasoning (high) | 0.4919 | 2,118.68 | 0.0192 | ❌ |
| 205 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-2.6-1T | 0.4914 | 6,408.24 | 0.1399 | ❌ |
| 206 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 27B (Non-reasoning) | 0.4913 | 2,488.49 | 0.0331 | ❌ |
| 207 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Sonnet (Non-reasoning) | 0.4910 | 13,035.34 | 0.3043 | ❌ |
| 208 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Speciale | 0.4902 | — | — | — |
| 209 | <img src="https://artificialanalysis.ai/img/logos//img/logos/china_mobile_small.png" width="18" alt="China Mobile" /> China Mobile | JT-35B-Flash | 0.4884 | — | — | — |
| 210 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step 3.5 Flash | 0.4879 | 802.75 | 0.0000 | ❌ |
| 211 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Pro | 0.4854 | 35,547.86 | 0.6425 | ❌ |
| 212 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm_small.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 7B | 0.4816 | — | — | — |
| 213 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3.5 | 0.4814 | 20,962.07 | 0.4616 | ❌ |
| 214 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE 2.0 | 0.4789 | — | — | — |
| 215 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (Non-reasoning) | 0.4761 | 12,302.32 | 0.2816 | ❌ |
| 216 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2 | 0.4751 | 3,158.24 | 0.0423 | ❌ |
| 217 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Haiku | 0.4723 | 11,472.51 | 0.2630 | ❌ |
| 218 | <img src="https://artificialanalysis.ai/img/logos//img/logos/bytedance_small.svg" width="18" alt="ByteDance Seed" /> ByteDance Seed | Doubao Seed Code | 0.4721 | — | — | — |
| 219 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o4-mini (high) | 0.4720 | 20,269.06 | 0.4496 | ❌ |
| 220 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o1 | 0.4710 | — | — | — |
| 221 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (Non-reasoning) | 0.4703 | 10,072.05 | 0.2153 | ❌ |
| 222 | <img src="https://artificialanalysis.ai/img/logos//img/logos/longcat_small.svg" width="18" alt="LongCat" /> LongCat | LongCat 2.0 | 0.4646 | — | — | — |
| 223 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.2 (Non-reasoning) | 0.4611 | 6,372.68 | 0.1393 | ❌ |
| 224 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (Non-reasoning) | 0.4605 | 832.53 | 0.0000 | ❌ |
| 225 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (medium) | 0.4586 | 28,614.76 | 0.5929 | ❌ |
| 226 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.7 Sonnet | 0.4568 | — | — | — |
| 227 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 27B (Non-reasoning) | 0.4548 | 2,849.23 | 0.0384 | ❌ |
| 228 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kwaikat_small.svg" width="18" alt="KwaiKAT" /> KwaiKAT | KAT-Coder-Pro V1 | 0.4542 | — | — | — |
| 229 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Sonnet (Non-reasoning) | 0.4533 | — | — | — |
| 230 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (low) | 0.4513 | 25,659.32 | 0.5571 | ❌ |
| 231 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 Terminus | 0.4510 | — | — | — |
| 232 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.1 Flash-Lite | 0.4502 | 3,270.97 | 0.0451 | ❌ |
| 233 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Sep) | 0.4479 | — | — | — |
| 234 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Exp | 0.4433 | — | — | — |
| 235 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (Non-reasoning) | 0.4410 | 10,507.94 | 0.2203 | ❌ |
| 236 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 122B A10B (Non-reasoning) | 0.4383 | 2,851.29 | 0.0384 | ❌ |
| 237 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.7 Sonnet (Non-reasoning) | 0.4327 | — | — | — |
| 238 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max Thinking (Preview) | 0.4317 | 15,632.95 | 0.3732 | ❌ |
| 239 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 9B | 0.4304 | 571.21 | 0.0000 | ❌ |
| 240 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash | 0.4267 | 13,012.32 | 0.3033 | ❌ |
| 241 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 26B A4B | 0.4266 | — | — | — |
| 242 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (medium) | 0.4258 | 6,408.24 | 0.1399 | ❌ |
| 243 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5-Pro (Non-reasoning) | 0.4220 | 926.46 | 0.0000 | ❌ |
| 244 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Haiku (Non-reasoning) | 0.4214 | 4,397.60 | 0.0950 | ❌ |
| 245 | <img src="https://artificialanalysis.ai/img/logos//img/logos/baidu_small.svg" width="18" alt="Baidu" /> Baidu | ERNIE 5.0 Thinking Preview | 0.4184 | — | — | — |
| 246 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 0905 | 0.4182 | 1,705.96 | 0.0130 | ❌ |
| 247 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (Non-reasoning) | 0.4174 | — | — | — |
| 248 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 235B A22B (Reasoning) | 0.4172 | 10,210.98 | 0.2169 | ❌ |
| 249 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.5 33B | 0.4161 | — | — | — |
| 250 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 (Non-reasoning) | 0.4156 | — | — | — |
| 251 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-2.6-1T | 0.4141 | — | — | — |
| 252 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (low) | 0.4099 | — | — | — |
| 253 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 (Non-reasoning) | 0.4085 | — | — | — |
| 254 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (high) | 0.4077 | 6,408.24 | 0.1399 | ❌ |
| 255 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (high) | 0.4067 | 4,798.04 | 0.1101 | ❌ |
| 256 | <img src="https://artificialanalysis.ai/img/logos//img/logos/tencent_small.svg" width="18" alt="Tencent" /> Tencent | Hy3-preview (Non-reasoning) | 0.4067 | — | — | — |
| 257 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 4B | 0.4062 | 390.82 | 0.0000 | ❌ |
| 258 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 35B A3B (Non-reasoning) | 0.4050 | 1,857.72 | 0.0155 | ❌ |
| 259 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (medium) | 0.4045 | 2,398.84 | 0.0297 | ❌ |
| 260 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7 (Non-reasoning) | 0.4036 | 6,686.33 | 0.1427 | ❌ |
| 261 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openbmb_small.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-2B | 0.4034 | — | — | — |
| 262 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 12B | 0.4024 | 802.75 | 0.0000 | ❌ |
| 263 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (medium) | 0.4021 | — | — | — |
| 264 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 v2 (Non-reasoning) | 0.3998 | 3,932.05 | 0.0870 | ❌ |
| 265 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (Non-reasoning) | 0.3968 | 3,998.61 | 0.0882 | ❌ |
| 266 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 | 0.3952 | — | — | — |
| 267 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5 | 0.3944 | — | — | — |
| 268 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6 | 0.3928 | 11,000.00 | 0.2257 | ❌ |
| 269 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inceptionlabs_small.svg" width="18" alt="Inception" /> Inception | Mercury 2 | 0.3895 | 3,193.37 | 0.0427 | ❌ |
| 270 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.2 30B | 0.3893 | 2,088.29 | 0.0188 | ❌ |
| 271 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 31B (Non-reasoning) | 0.3893 | 1,634.82 | 0.0118 | ❌ |
| 272 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (Non-reasoning) | 0.3888 | 1,028.57 | 0.0000 | ❌ |
| 273 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max | 0.3888 | 4,313.37 | 0.0937 | ❌ |
| 274 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm_small.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 3.7B | 0.3876 | — | — | — |
| 275 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok Code Fast 1 | 0.3856 | — | — | — |
| 276 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE | 0.3852 | — | — | — |
| 277 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 | 0.3844 | 1,592.78 | 0.0111 | ❌ |
| 278 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Super | 0.3843 | 1,726.54 | 0.0134 | ❌ |
| 279 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 0528 | 0.3836 | — | — | — |
| 280 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3.5 Lightning | 0.3822 | 1,005.27 | 0.0000 | ❌ |
| 281 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.0 Tiny | 0.3779 | 0.00 | 0.0000 | ❌ |
| 282 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Sep) (Non-reasoning) | 0.3778 | — | — | — |
| 283 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 35B A3B (Non-reasoning) | 0.3760 | 1,738.61 | 0.0136 | ❌ |
| 284 | <img src="https://artificialanalysis.ai/img/logos//img/logos/arcee_small.svg" width="18" alt="Arcee AI" /> Arcee AI | Trinity Large Thinking | 0.3753 | 2,381.86 | 0.0284 | ❌ |
| 285 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (minimal) | 0.3750 | 7,781.92 | 0.1620 | ❌ |
| 286 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 32B (Reasoning) | 0.3739 | 1,684.39 | 0.0127 | ❌ |
| 287 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 | 0.3727 | 10,897.39 | 0.2246 | ❌ |
| 288 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 (Non-reasoning) | 0.3714 | 7,929.95 | 0.1653 | ❌ |
| 289 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (low) | 0.3704 | 6,408.24 | 0.1399 | ❌ |
| 290 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 9B (Non-reasoning) | 0.3698 | 230.71 | 0.0000 | ❌ |
| 291 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7-Flash | 0.3695 | 1,700.00 | 0.0129 | ❌ |
| 292 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6 (Non-reasoning) | 0.3663 | 1,693.48 | 0.0128 | ❌ |
| 293 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B A22B 2507 | 0.3632 | 5,871.32 | 0.1298 | ❌ |
| 294 | <img src="https://artificialanalysis.ai/img/logos//img/logos/servicenow_small.svg" width="18" alt="ServiceNow" /> ServiceNow | Apriel-v1.5-15B-Thinker | 0.3628 | — | — | — |
| 295 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-120b (high) | 0.3594 | 2,750.69 | 0.0370 | ❌ |
| 296 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 Omni Flash | 0.3583 | 774.45 | 0.0000 | ❌ |
| 297 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder 480B | 0.3572 | 5,671.45 | 0.1256 | ❌ |
| 298 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Sep) | 0.3561 | — | — | — |
| 299 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron Cascade 2 30B A3B | 0.3558 | — | — | — |
| 300 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepcogito_small.png" width="18" alt="Deep Cogito" /> Deep Cogito | Cogito v2.1 | 0.3553 | — | — | — |
| 301 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash (Non-reasoning) | 0.3539 | — | — | — |
| 302 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Magistral Medium 1.2 | 0.3531 | — | — | — |
| 303 | <img src="https://artificialanalysis.ai/img/logos//img/logos/servicenow_small.svg" width="18" alt="ServiceNow" /> ServiceNow | Apriel-v1.6-15B-Thinker | 0.3522 | — | — | — |
| 304 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 26B A4B (Non-reasoning) | 0.3513 | 1,492.07 | 0.0056 | ❌ |
| 305 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 3 | 0.3501 | — | — | — |
| 306 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6V | 0.3499 | 2,408.24 | 0.0305 | ❌ |
| 307 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 Terminus (Non-reasoning) | 0.3491 | — | — | — |
| 308 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (ChatGPT) | 0.3444 | — | — | — |
| 309 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | G9v3-3B | 0.3405 | — | — | — |
| 310 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 4 | 0.3392 | 1,579.12 | 0.0108 | ❌ |
| 311 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max (Preview) | 0.3377 | 5,029.34 | 0.1137 | ❌ |
| 312 | <img src="https://artificialanalysis.ai/img/logos//img/logos/multiversecomputing_small.svg" width="18" alt="Multiverse Computing" /> Multiverse Computing | HyperNova 60B 2605 (high) | 0.3365 | — | — | — |
| 313 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.2 8B | 0.3349 | 798.74 | 0.0000 | ❌ |
| 314 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Exp (Non-reasoning) | 0.3314 | — | — | — |
| 315 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Sep) (Non-reasoning) | 0.3287 | — | — | — |
| 316 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 (Non-reasoning) | 0.3282 | — | — | — |
| 317 | <img src="https://artificialanalysis.ai/img/logos//img/logos/cohere_small.svg" width="18" alt="Cohere" /> Cohere | North Mini Code | 0.3274 | 0.00 | 0.0000 | ❌ |
| 318 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o3-mini (high) | 0.3245 | 24,959.17 | 0.5512 | ❌ |
| 319 | <img src="https://artificialanalysis.ai/img/logos//img/logos/bytedance_small.svg" width="18" alt="ByteDance Seed" /> ByteDance Seed | Seed-OSS-36B-Instruct | 0.3242 | 1,535.77 | 0.0083 | ❌ |
| 320 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o (Nov) | 0.3203 | 21,755.70 | 0.4931 | ❌ |
| 321 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Non-reasoning) | 0.3186 | 1,925.96 | 0.0165 | ❌ |
| 322 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 3 | 0.3181 | 1,721.21 | 0.0133 | ❌ |
| 323 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B 2507 | 0.3170 | 713.14 | 0.0000 | ❌ |
| 324 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o (Aug) | 0.3170 | 19,243.78 | 0.4337 | ❌ |
| 325 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm_small.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Think V2 | 0.3159 | — | — | — |
| 326 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite | 0.3140 | 3,235.92 | 0.0438 | ❌ |
| 327 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder Next | 0.3109 | 4,295.29 | 0.0933 | ❌ |
| 328 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.1 Fast (Non-reasoning) | 0.3102 | — | — | — |
| 329 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (minimal) | 0.3095 | 1,553.48 | 0.0094 | ❌ |
| 330 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Next 80B A3B (Reasoning) | 0.3093 | 3,079.12 | 0.0413 | ❌ |
| 331 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano | 0.3090 | 526.37 | 0.0000 | ❌ |
| 332 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 12B (Non-reasoning) | 0.3083 | 281.16 | 0.0000 | ❌ |
| 333 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 235B A22B | 0.3078 | 1,215.20 | 0.0000 | ❌ |
| 334 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | QwQ-32B | 0.3065 | — | — | — |
| 335 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-1T | 0.3048 | — | — | — |
| 336 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openbmb_small.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-1B | 0.3047 | — | — | — |
| 337 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openbmb_small.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-1B (Non-reasoning) | 0.3046 | — | — | — |
| 338 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Pixtral Large | 0.3034 | — | — | — |
| 339 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Open 100B | 0.2999 | — | — | — |
| 340 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o3-mini | 0.2990 | 13,368.50 | 0.3184 | ❌ |
| 341 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 4B (Non-reasoning) | 0.2976 | 92.93 | 0.0000 | ❌ |
| 342 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax M1 80k | 0.2965 | — | — | — |
| 343 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5-Air | 0.2962 | 2,539.67 | 0.0339 | ❌ |
| 344 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (Non-reasoning) | 0.2958 | 4,085.17 | 0.0897 | ❌ |
| 345 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 E4B | 0.2955 | 260.55 | 0.0000 | ❌ |
| 346 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (Non-reasoning) | 0.2940 | 6,771.49 | 0.1436 | ❌ |
| 347 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | DiffusionGemma 26B A4B | 0.2916 | — | — | — |
| 348 | <img src="https://artificialanalysis.ai/img/logos//img/logos/china_mobile_small.png" width="18" alt="China Mobile" /> China Mobile | JT-MINI | 0.2916 | — | — | — |
| 349 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Large 3 | 0.2906 | 1,138.69 | 0.0000 | ❌ |
| 350 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3 | 0.2899 | 1,828.22 | 0.0150 | ❌ |
| 351 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax M1 40k | 0.2899 | — | — | — |
| 352 | <img src="https://artificialanalysis.ai/img/logos//img/logos/naver_small.webp" width="18" alt="Naver" /> Naver | HyperCLOVA X SEED Think (32B) | 0.2891 | — | — | — |
| 353 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3 0324 | 0.2879 | — | — | — |
| 354 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 Fast (Non-reasoning) | 0.2877 | — | — | — |
| 355 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm_small.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (high) | 0.2870 | — | — | — |
| 356 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE (Non-reasoning) | 0.2865 | — | — | — |
| 357 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 (Jan) | 0.2858 | — | — | — |
| 358 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3.1 | 0.2845 | 1,856.39 | 0.0154 | ❌ |
| 359 | <img src="https://artificialanalysis.ai/img/logos//img/logos/korea-telecom_small.png" width="18" alt="Korea Telecom" /> Korea Telecom | Mi:dm K 2.5 Pro | 0.2840 | — | — | — |
| 360 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (Non-reasoning) | 0.2825 | 1,081.79 | 0.0000 | ❌ |
| 361 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 4 Maverick | 0.2820 | 2,998.90 | 0.0403 | ❌ |
| 362 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-20b (high) | 0.2809 | 506.65 | 0.0000 | ❌ |
| 363 | <img src="https://artificialanalysis.ai/img/logos//img/logos/prime-intellect_small.svg" width="18" alt="Prime Intellect" /> Prime Intellect | INTELLECT-3 | 0.2776 | — | — | — |
| 364 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano Omni 30B A3B | 0.2766 | — | — | — |
| 365 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B A3B 2507 | 0.2763 | 6,105.49 | 0.1343 | ❌ |
| 366 | <img src="https://artificialanalysis.ai/img/logos//img/logos/trillionlabs_small.svg" width="18" alt="Trillion Labs" /> Trillion Labs | Tri-21B-think Preview | 0.2760 | — | — | — |
| 367 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 30B A3B (Reasoning) | 0.2750 | 6,105.49 | 0.1343 | ❌ |
| 368 | <img src="https://artificialanalysis.ai/img/logos//img/logos/longcat_small.svg" width="18" alt="LongCat" /> LongCat | LongCat Flash Lite | 0.2745 | — | — | — |
| 369 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-20b (low) | 0.2737 | 536.92 | 0.0000 | ❌ |
| 370 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.1 405B | 0.2727 | — | — | — |
| 371 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova Premier | 0.2719 | 14,620.06 | 0.3564 | ❌ |
| 372 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 mini | 0.2712 | 2,153.00 | 0.0197 | ❌ |
| 373 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 E4B (Non-reasoning) | 0.2708 | 63.61 | 0.0000 | ❌ |
| 374 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 2.6 Flash | 0.2707 | — | — | — |
| 375 | <img src="https://artificialanalysis.ai/img/logos//img/logos/trillionlabs_small.svg" width="18" alt="Trillion Labs" /> Trillion Labs | Tri-21B-Think | 0.2702 | — | — | — |
| 376 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.2 3B | 0.2682 | 386.87 | 0.0000 | ❌ |
| 377 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (Non-reasoning) | 0.2632 | 1,818.10 | 0.0148 | ❌ |
| 378 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 32B | 0.2628 | 514.90 | 0.0000 | ❌ |
| 379 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Next 80B A3B | 0.2626 | 1,148.94 | 0.0000 | ❌ |
| 380 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nousresearch_small.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 405B | 0.2609 | 8,027.46 | 0.1675 | ❌ |
| 381 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral 2 | 0.2609 | 0.00 | 0.0000 | ❌ |
| 382 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm_small.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (medium) | 0.2580 | — | — | — |
| 383 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-1T | 0.2573 | — | — | — |
| 384 | <img src="https://artificialanalysis.ai/img/logos//img/logos/motif_small.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif-2-12.7B | 0.2567 | — | — | — |
| 385 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-120b (low) | 0.2562 | 2,862.50 | 0.0385 | ❌ |
| 386 | <img src="https://artificialanalysis.ai/img/logos//img/logos/korea-telecom_small.png" width="18" alt="Korea Telecom" /> Korea Telecom | Mi:dm K 2.5 Pro Preview | 0.2560 | — | — | — |
| 387 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.5 Haiku | 0.2544 | — | — | — |
| 388 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 8B (Reasoning) | 0.2538 | 5,344.94 | 0.1185 | ❌ |
| 389 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step3 VL 10B | 0.2524 | — | — | — |
| 390 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Super 49B v1.5 | 0.2500 | 1,210.98 | 0.0000 | ❌ |
| 391 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.0 Flash | 0.2495 | — | — | — |
| 392 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7-Flash (Non-reasoning) | 0.2492 | 305.74 | 0.0000 | ❌ |
| 393 | <img src="https://artificialanalysis.ai/img/logos//img/logos/baidu_small.svg" width="18" alt="Baidu" /> Baidu | ERNIE 4.5 300B A47B | 0.2466 | — | — | — |
| 394 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Magistral Medium 1 | 0.2462 | — | — | — |
| 395 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral Medium | 0.2442 | — | — | — |
| 396 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B 2507 | 0.2434 | — | — | — |
| 397 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4 | 0.2433 | — | — | — |
| 398 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (Non-reasoning) | 0.2429 | — | — | — |
| 399 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 4 (Non-reasoning) | 0.2426 | 467.39 | 0.0000 | ❌ |
| 400 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nousresearch_small.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 405B (Non-reasoning) | 0.2412 | 2,343.22 | 0.0253 | ❌ |
| 401 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder 30B A3B | 0.2400 | 1,874.36 | 0.0157 | ❌ |
| 402 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-8B-A1B | 0.2378 | — | — | — |
| 403 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 30B A3B | 0.2373 | 696.64 | 0.0000 | ❌ |
| 404 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral Small 2 | 0.2371 | 0.00 | 0.0000 | ❌ |
| 405 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6V (Non-reasoning) | 0.2365 | 778.08 | 0.0000 | ❌ |
| 406 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 E2B | 0.2352 | — | — | — |
| 407 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Omni 30B A3B (Reasoning) | 0.2348 | 2,556.86 | 0.0342 | ❌ |
| 408 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-2.6B | 0.2342 | — | — | — |
| 409 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B | 0.2309 | 21,369.22 | 0.4755 | ❌ |
| 410 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5V | 0.2299 | 4,816.47 | 0.1104 | ❌ |
| 411 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 12B v2 VL | 0.2289 | 1,605.49 | 0.0113 | ❌ |
| 412 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Large 2 (Nov) | 0.2280 | — | — | — |
| 413 | <img src="https://artificialanalysis.ai/img/logos//img/logos/tii_small.svg" width="18" alt="TII UAE" /> TII UAE | Falcon-H1R-7B | 0.2265 | — | — | — |
| 414 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Ultra | 0.2257 | — | — | — |
| 415 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3 (Dec) | 0.2199 | — | — | — |
| 416 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nanbeige_small.png" width="18" alt="Nanbeige" /> Nanbeige | Nanbeige4.1-3B | 0.2165 | — | — | — |
| 417 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova Pro | 0.2164 | — | — | — |
| 418 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3.1 32B Think | 0.2156 | — | — | — |
| 419 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3.2 | 0.2151 | 235.64 | 0.0000 | ❌ |
| 420 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam 105B (high) | 0.2150 | — | — | — |
| 421 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.0 32B | 0.2142 | — | — | — |
| 422 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Magistral Small 1.2 | 0.2133 | — | — | — |
| 423 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm_small.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (low) | 0.2121 | — | — | — |
| 424 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 9B V2 | 0.2118 | 421.10 | 0.0000 | ❌ |
| 425 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 2B | 0.2114 | — | — | — |
| 426 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-flash-2.0 | 0.2092 | — | — | — |
| 427 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Non-reasoning) | 0.2092 | 381.31 | 0.0000 | ❌ |
| 428 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Super 49B v1.5 (Non-reasoning) | 0.2075 | 551.02 | 0.0000 | ❌ |
| 429 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nousresearch_small.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 70B | 0.2058 | — | — | — |
| 430 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 4 Scout | 0.2055 | 496.66 | 0.0000 | ❌ |
| 431 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral Small (May) | 0.2044 | — | — | — |
| 432 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 32B | 0.2044 | 1,684.39 | 0.0127 | ❌ |
| 433 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova Lite | 0.2039 | 335.11 | 0.0000 | ❌ |
| 434 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 32B | 0.2012 | — | — | — |
| 435 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.3 Nemotron Super 49B | 0.2009 | — | — | — |
| 436 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen2.5 72B | 0.1998 | — | — | — |
| 437 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-flash-2.0 | 0.1988 | 373.36 | 0.0000 | ❌ |
| 438 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 8B | 0.1985 | 625.55 | 0.0000 | ❌ |
| 439 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 14B | 0.1981 | 10,684.61 | 0.2223 | ❌ |
| 440 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B | 0.1969 | 6,105.49 | 0.1343 | ❌ |
| 441 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Magistral Small 1 | 0.1968 | — | — | — |
| 442 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Ministral 3 14B | 0.1930 | 221.65 | 0.0000 | ❌ |
| 443 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Large 2 (Jul) | 0.1923 | — | — | — |
| 444 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 2 | 0.1918 | — | — | — |
| 445 | <img src="https://artificialanalysis.ai/img/logos//img/logos/cohere_small.svg" width="18" alt="Cohere" /> Cohere | Command A | 0.1916 | 7,365.61 | 0.1492 | ❌ |
| 446 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral Small | 0.1909 | — | — | — |
| 447 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B (Non-reasoning) | 0.1908 | 2,207.19 | 0.0204 | ❌ |
| 448 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3.1 | 0.1900 | 234.95 | 0.0000 | ❌ |
| 449 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.1 Nemotron 70B | 0.1894 | 1,662.22 | 0.0123 | ❌ |
| 450 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano 4B | 0.1876 | — | — | — |
| 451 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 4B (Reasoning) | 0.1869 | — | — | — |
| 452 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3 Haiku | 0.1856 | — | — | — |
| 453 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.3 Nemotron Super 49B (Non-reasoning) | 0.1843 | — | — | — |
| 454 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B A3B 2507 (Non-reasoning) | 0.1824 | 708.19 | 0.0000 | ❌ |
| 455 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B | 0.1811 | — | — | — |
| 456 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.1 70B | 0.1806 | 634.93 | 0.0000 | ❌ |
| 457 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 9B V2 (Non-reasoning) | 0.1801 | 188.77 | 0.0000 | ❌ |
| 458 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 32B (Non-reasoning) | 0.1792 | 570.98 | 0.0000 | ❌ |
| 459 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5V (Non-reasoning) | 0.1784 | 1,399.64 | 0.0000 | ❌ |
| 460 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 E2B (Non-reasoning) | 0.1783 | — | — | — |
| 461 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 2B (Non-reasoning) | 0.1761 | — | — | — |
| 462 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.1 30B | 0.1756 | — | — | — |
| 463 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3.1 32B Instruct | 0.1728 | — | — | — |
| 464 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Omni 30B A3B | 0.1712 | 796.65 | 0.0000 | ❌ |
| 465 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (minimal) | 0.1704 | 325.29 | 0.0000 | ❌ |
| 466 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B 2507 (Non-reasoning) | 0.1692 | — | — | — |
| 467 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.1 8B | 0.1677 | 41.39 | 0.0000 | ❌ |
| 468 | <img src="https://artificialanalysis.ai/img/logos//img/logos/celeris.svg" width="18" alt="Celeris" /> Celeris | Celeris-1 | 0.1668 | 1,128.49 | 0.0000 | ❌ |
| 469 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o mini | 0.1652 | 1,163.52 | 0.0000 | ❌ |
| 470 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 32B Think | 0.1651 | — | — | — |
| 471 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 14B | 0.1646 | — | — | — |
| 472 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Llama 70B | 0.1646 | — | — | — |
| 473 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 nano | 0.1642 | 536.04 | 0.0000 | ❌ |
| 474 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.3 70B | 0.1639 | 7,559.29 | 0.1525 | ❌ |
| 475 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi Linear 48B A3B Instruct | 0.1635 | — | — | — |
| 476 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Ministral 3 8B | 0.1631 | 164.95 | 0.0000 | ❌ |
| 477 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 2 (Non-reasoning) | 0.1620 | — | — | — |
| 478 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nousresearch_small.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 70B (Non-reasoning) | 0.1590 | — | — | — |
| 479 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai21_small.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba Reasoning 3B | 0.1585 | — | — | — |
| 480 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.0 32B (Non-reasoning) | 0.1565 | — | — | — |
| 481 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.1 8B | 0.1563 | 82.81 | 0.0000 | ❌ |
| 482 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova Micro | 0.1536 | 205.32 | 0.0000 | ❌ |
| 483 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 24B A2B | 0.1531 | — | — | — |
| 484 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai21_small.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba 1.7 Large | 0.1520 | — | — | — |
| 485 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam 30B (high) | 0.1501 | — | — | — |
| 486 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 8B | 0.1496 | 5,344.94 | 0.1185 | ❌ |
| 487 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3 | 0.1489 | 241.11 | 0.0000 | ❌ |
| 488 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 12B v2 VL (Non-reasoning) | 0.1484 | 603.28 | 0.0000 | ❌ |
| 489 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openbmb_small.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM-V 4.6 1.3B | 0.1480 | — | — | — |
| 490 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B (Non-reasoning) | 0.1439 | 690.45 | 0.0000 | ❌ |
| 491 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano (Non-reasoning) | 0.1411 | 156.64 | 0.0000 | ❌ |
| 492 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H Small | 0.1380 | 283.58 | 0.0000 | ❌ |
| 493 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 4B | 0.1376 | — | — | — |
| 494 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 27B | 0.1369 | — | — | — |
| 495 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 0528 Qwen3 8B | 0.1340 | — | — | — |
| 496 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Ministral 3 3B | 0.1327 | 116.37 | 0.0000 | ❌ |
| 497 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 14B (Non-reasoning) | 0.1319 | 1,125.08 | 0.0000 | ❌ |
| 498 | <img src="https://artificialanalysis.ai/img/logos//img/logos/microsoft_small.svg" width="18" alt="Microsoft" /> Microsoft | Phi-4 | 0.1273 | 359.80 | 0.0000 | ❌ |
| 499 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.1 Nemotron Nano 4B v1.1 | 0.1270 | — | — | — |
| 500 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 270M | 0.1246 | — | — | — |
| 501 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3 70B | 0.1192 | — | — | — |
| 502 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.2 11B (Vision) | 0.1188 | 363.04 | 0.0000 | ❌ |
| 503 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.2 3B | 0.1169 | — | — | — |
| 504 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 0.8B | 0.1157 | — | — | — |
| 505 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 7B Think | 0.1152 | — | — | — |
| 506 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-1.2B-Instruct | 0.1086 | — | — | — |
| 507 | <img src="https://artificialanalysis.ai/img/logos//img/logos/reka_small.svg" width="18" alt="Reka AI" /> Reka AI | Reka Flash 3 | 0.1081 | — | — | — |
| 508 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 2.6B | 0.1078 | — | — | — |
| 509 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-mini-2.0 | 0.1076 | — | — | — |
| 510 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 8B (Non-reasoning) | 0.1064 | 551.02 | 0.0000 | ❌ |
| 511 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Molmo2-8B | 0.1034 | — | — | — |
| 512 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam M | 0.1031 | — | — | — |
| 513 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai21_small.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba 1.7 Mini | 0.1017 | — | — | — |
| 514 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-1.2B-Thinking | 0.1003 | — | — | — |
| 515 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 12B | 0.0984 | — | — | — |
| 516 | <img src="https://artificialanalysis.ai/img/logos//img/logos/microsoft_small.svg" width="18" alt="Microsoft" /> Microsoft | Phi-4 Mini | 0.0982 | 0.00 | 0.0000 | ❌ |
| 517 | <img src="https://artificialanalysis.ai/img/logos//img/logos/swiss-ai-initiative_small.png" width="18" alt="Swiss AI Initiative" /> Swiss AI Initiative | Apertus 70B Instruct | 0.0937 | — | — | — |
| 518 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 0.8B (Non-reasoning) | 0.0930 | — | — | — |
| 519 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 7B | 0.0921 | — | — | — |
| 520 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | OLMo 2 32B | 0.0911 | — | — | — |
| 521 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | Exaone 4.0 1.2B | 0.0911 | — | — | — |
| 522 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H 1B | 0.0905 | — | — | — |
| 523 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.2 1B | 0.0897 | — | — | — |
| 524 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 1.7B | 0.0882 | — | — | — |
| 525 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.1 3B | 0.0865 | — | — | — |
| 526 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | Exaone 4.0 1.2B (Non-reasoning) | 0.0841 | — | — | — |
| 527 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 8B A1B | 0.0823 | — | — | — |
| 528 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 Micro | 0.0796 | — | — | — |
| 529 | <img src="https://artificialanalysis.ai/img/logos//img/logos/microsoft_small.svg" width="18" alt="Microsoft" /> Microsoft | Phi-3 Mini | 0.0752 | — | — | — |
| 530 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 3.3 8B | 0.0713 | 244.62 | 0.0000 | ❌ |
| 531 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-VL-1.6B | 0.0687 | — | — | — |
| 532 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 1B | 0.0679 | — | — | — |
| 533 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 350M | 0.0671 | — | — | — |
| 534 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 4B | 0.0661 | — | — | — |
| 535 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 1.2B | 0.0652 | — | — | — |
| 536 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 0.6B | 0.0645 | — | — | — |
| 537 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3 8B | 0.0643 | — | — | — |
| 538 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral 7B | 0.0621 | 276.50 | 0.0000 | ❌ |
| 539 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3n E4B | 0.0580 | — | — | — |
| 540 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm_small.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 0.9B | 0.0568 | — | — | — |
| 541 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | OLMo 2 7B | 0.0565 | — | — | — |
| 542 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 1.7B (Non-reasoning) | 0.0562 | — | — | — |
| 543 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 1B | 0.0558 | — | — | — |
| 544 | <img src="https://artificialanalysis.ai/img/logos//img/logos/swiss-ai-initiative_small.png" width="18" alt="Swiss AI Initiative" /> Swiss AI Initiative | Apertus 8B Instruct | 0.0548 | — | — | — |
| 545 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H 350M | 0.0506 | — | — | — |
| 546 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Molmo 7B-D | 0.0478 | — | — | — |
| 547 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 0.6B (Non-reasoning) | 0.0433 | — | — | — |
| 548 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3n E2B | 0.0356 | — | — | — |
| 549 | <img src="https://artificialanalysis.ai/img/logos//img/logos/cohere_small.svg" width="18" alt="Cohere" /> Cohere | Tiny Aya Global | 0.0352 | — | — | — |
| 550 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 1.5B | 0.0000 | — | — | — |

## 品牌帕累托前沿连线（仅体现在图中）

以下十一个品牌在图中拥有单独的帕累托连线（较窄宽度，品牌主题色，图层高于总体灰色连线）。表中数量为**入图顶点数**——品牌前沿上低于总体前沿第一级的顶点同样不入图（本表与图例一致）：

| 品牌 | 主题色 | 品牌前沿模型数（入图） |
|------|--------|--------------|
| <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | `#cc785c` | 10 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | `#1f1f1f` | 10 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | `#0089f4` | 3 |
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
6. **图表纵轴基线（V17）**：图表的 y = 0 取总体帕累托前沿的第一级（最低能力；本例 y0 = 0.6339，即前沿左端点 Ling-3.0-flash-VL）；综合能力低于该级的模型不出现在图表中（表格不受影响）。图中纵坐标 chart_y = (能力 - y0)/(1 - y0)，因此前沿左端点恰好落在 (0, 0)、最优模型恰好为 y = 1。该过滤在横轴映射构建之前完成


## 横轴映射（分位数等密度映射，V17）与分布分析

横轴（单请求成本）按**经验分位数（rank）映射**——以 94 个入图正成本模型（综合能力 ≥ 前沿第一级）的成本分布为基准：

```
x = 0                            当 c ≤ 0（免费模型，钉在最左缘）
x = interp(log10(c); knots)      当 c > 0
```

其中 knots = (log10(c_i), 名次_i/(n-1)) 为入图正成本模型按成本排序后的 88 个锚点（相同 log10(c) 的并列组取平均名次，保证 x 是 z = log10(c) 的单值函数；n-1 归一化使最大成本恰为 x = 1）。该映射在 **y 基线过滤之后**构建（V17：先以帕累托前沿第一级为 y = 0、剔除低性能模型，再对入图模型建映射）。（V18 修正：并列判定改用相同的 log10(c)，消除浮点上相差 ~1e-12 的成本经 log10 后折合到同一 z 造成的同 z 双锚点、个别模型 x 偏离名次的问题；修正后 x 对每个入图模型严格线性于名次。）

**该映射保证：**

- **函数端点严格钉死**：c = 0 → x = 0；最大成本 → x = 1——函数经过 (0,0) 与 (1,1)；
- **严格均匀密度**：x 是模型名次的线性函数（相同 log10(c) 并列组取平均名次），因此**任意等宽区段的模型数恒定**（每 0.1 宽度约 9 个模型）——无论截取哪一段，模型数 ÷ 宽度都等于全图的模型总数 ÷ 总宽度。V12 的单一 logistic 函数在过滤后的分布上做不到（十分位在 8~24 间摆动），故替换为精确分位数映射；
- 各数量级区间的入图模型数：1–10: 0，10–100: 0，100–1k: 0，1k–10k: 20，10k–100k: 60
- **同一倍率区间的宽度 ∝ 该区间模型数**——均匀密度的必然结果：1k→10k 与 100k→1M 同为 10 倍率，但前者 20 个模型、后者 14 个，前者宽度约为后者的 1.4 倍。若改用「等倍率等距」（纯对数轴），两段的模型密度将相差 1.4 倍，与均匀密度目标冲突——两者数学上不可兼得，本图以均匀密度（最高优先级）为准；
- **左端恒为 0**（c = 0；1 个免费模型位于最左缘）
- 最低正成本 1,405.68 → x = 0.0000；最高成本 901,602 → x = 1.0000（严格 = 1）
- 中位数位置 0.495（≈ 0.5 居中）；左右两半模型数：左 48 / 右 47
- 横轴十分位模型数：11，9，10，9，9，9，10，9，9，10（x 为名次的线性函数；n/10 非整数时各十分位在 ±1 内取整，相同 log10(c) 并列组共享同一 x、落在边界的哪一侧可再移动 ±1）
- **10^x 数量级指示**（位置 = x(10^x)）：10^0 → 0.000，10^1 → 0.000，10^2 → 0.000，10^3 → 0.000，10^4 → 0.214，10^5 → 0.853

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
**模型总数（Status: All）**: 550 个参与排名（另有模型因评估数据不足未列入；总体帕累托前沿 13 个；图表入图 95 个——综合能力 ≥ 前沿第一级）  

## 图表说明（黑底）

（V17 起本说明置于文末，图表之后直接跟随模型表格。）

图表说明：**灰色实线** = 总体帕累托前沿；**彩色细线** = 十一个品牌的单独帕累托前沿（品牌主题色，图层高于总体连线；暗色品牌元素带窄白边；顶点按（横轴位置、能力升序）连接，等成本点自下而上）；品牌前沿模型圆点同样使用品牌颜色。模型名称/思考程度标注优先骑在连线之上（点的左/右两侧皆可，同一条线段可容纳两个标签——各贴各的点；文字与连线平行、中轴线重合，连线仅在文字两侧绘制）；骑线位被其他标签占据时自动「让位」——占用者挪到自己的另一个骑线位，双方都保持骑线；实在骑不上线时按四级优先依次退让（V16）：离点最近位置的上方/下方平行偏移 → 点的两条连线延长线上就近 → 两连线夹角扇区内就近。标签规则（V13/V15）：品牌前沿模型共享的前导块按「最长有效切点」剔除 —— 切点止于分界符，或止于字母且其后紧跟数字（如 Claude Opus 5 → Opus 5、GPT-5.6 Sol → 5.6 Sol、Kimi K2.6 → 2.6、Qwen3.8 Max → 3.8 Max、MiMo-V2.5 → 2.5、MiniMax-M2.1 → 2.1）；(non-reasoning) 简写为 (non)；同一模型在品牌连线上相邻出现 2 次以上时仅性能最低者保留全名、相邻较高者只标思考程度，不相邻的重复出现保留全名（每次重新计算）；标签位置与序列同向（V15）——品牌前沿上越靠右上的模型，其标签重心必须同时更靠右且更靠上（两分量都 >= 0，至少是 (0,0)，仅其一非负不算合格；初始放置违反时自动就近重摆，单标签无解（被前后邻居夹死）时按窗口级联重排整体挪动，均不产生新的重叠）。纵轴 y = 0 = 总体帕累托前沿第一级（y0 = 0.6339，前沿左端点 Ling-3.0-flash-VL 恰为 (0,0)），能力低于该级的 440 个模型与缺少成本数据的 15 个模型不出现在图中；横轴为分位数等密度映射（见上文「横轴映射」节），10^x 数量级指示位于 x(10^x)，同一倍率区间的宽度与该区间内模型数成正比。
