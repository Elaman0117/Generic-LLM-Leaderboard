# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

## 全部模型（综合能力从高到低，最优 = 1，最差 = 0）

共收录 **Status: All**（含已弃用）的全部模型；按重新归一化后的综合能力排序。「帕累托」列：✅ = 总体帕累托前沿模型，❌ = 被支配，— = 无成本数据无法判定。图表纵轴以总体帕累托前沿第一级（y0 = 0.5887，即前沿左端点 Ling-3.0-flash-VL）为 0：综合能力 ≥ 该级且有成本数据的 104 个模型入图，416 个能力低于第一级、23 个缺少成本数据的模型不出现在图中（本表不受影响，仍完整列出全部模型）。

| # | 品牌 | 模型 | 综合能力 | 单请求成本 | 横轴位置 | 帕累托 |
|---|------|------|---------|-----------|-----------|------|
| 1 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (max with fallback) | 1.0000 | 998,846.30 | 1.0000 | ✅ |
| 2 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (xhigh with fallback) | 0.9933 | 279,615.07 | 0.9608 | ✅ |
| 3 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (xhigh) | 0.9868 | 407,667.23 | 0.9804 | ❌ |
| 4 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (max) | 0.9825 | 951,792.64 | 0.9902 | ❌ |
| 5 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (high) | 0.9636 | 124,973.96 | 0.8922 | ✅ |
| 6 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (high with fallback) | 0.9600 | 64,477.50 | 0.8333 | ✅ |
| 7 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (max) | 0.9562 | 94,101.34 | 0.8529 | ❌ |
| 8 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (xhigh) | 0.9430 | 49,040.29 | 0.7941 | ✅ |
| 9 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (medium) | 0.9386 | 52,055.03 | 0.8137 | ❌ |
| 10 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5 (with fallback) | 0.9376 | 312,918.92 | 0.9706 | ❌ |
| 11 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (high) | 0.9298 | 38,051.26 | 0.6765 | ✅ |
| 12 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (max) | 0.9215 | 144,866.09 | 0.9118 | ❌ |
| 13 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (medium with fallback) | 0.9202 | 49,648.37 | 0.8039 | ❌ |
| 14 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.3 (max) | 0.9101 | 12,704.93 | 0.3333 | ✅ |
| 15 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (low) | 0.8952 | 46,525.27 | 0.7647 | ❌ |
| 16 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.3 (xhigh) | 0.8846 | 12,704.93 | 0.3333 | ❌ |
| 17 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (low with fallback) | 0.8827 | 46,263.65 | 0.7451 | ❌ |
| 18 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (medium) | 0.8765 | 25,155.84 | 0.5882 | ❌ |
| 19 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3 (max) | 0.8675 | 14,201.02 | 0.3873 | ❌ |
| 20 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (xhigh) | 0.8665 | 66,666.71 | 0.8431 | ❌ |
| 21 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (max) | 0.8533 | 198,445.55 | 0.9510 | ❌ |
| 22 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3 (max) | 0.8520 | 41,923.47 | 0.7108 | ❌ |
| 23 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (high) | 0.8514 | 17,922.96 | 0.4510 | ❌ |
| 24 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (high) | 0.8481 | 15,797.19 | 0.4118 | ❌ |
| 25 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (xhigh) | 0.8461 | 21,035.19 | 0.5098 | ❌ |
| 26 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (xhigh) | 0.8456 | 150,296.49 | 0.9216 | ❌ |
| 27 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (high) | 0.8433 | 32,270.68 | 0.6373 | ❌ |
| 28 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.8 (max) | 0.8367 | 46,322.09 | 0.7549 | ❌ |
| 29 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (medium) | 0.8297 | 16,978.44 | 0.4412 | ❌ |
| 30 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.7 (max) | 0.8214 | 43,449.97 | 0.7353 | ❌ |
| 31 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (medium) | 0.8181 | — | — | — |
| 32 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (high) | 0.8164 | 14,249.46 | 0.4020 | ❌ |
| 33 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (xhigh) | 0.8157 | 188,722.20 | 0.9412 | ❌ |
| 34 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (medium) | 0.8148 | 21,848.09 | 0.5392 | ❌ |
| 35 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (high) | 0.8135 | 47,405.41 | 0.7843 | ❌ |
| 36 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 Max | 0.8121 | 18,422.62 | 0.4657 | ❌ |
| 37 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (medium) | 0.8083 | 7,622.11 | 0.1863 | ✅ |
| 38 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3-Flash | 0.8076 | 1,575.37 | 0.0196 | ✅ |
| 39 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (low) | 0.7932 | 23,930.18 | 0.5784 | ❌ |
| 40 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (medium) | 0.7916 | 31,134.56 | 0.6176 | ❌ |
| 41 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.3 Codex (xhigh) | 0.7912 | 96,814.60 | 0.8627 | ❌ |
| 42 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 2.4T A95B | 0.7869 | 18,422.62 | 0.4657 | ❌ |
| 43 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.2 (xhigh) | 0.7859 | 12,704.93 | 0.3333 | ❌ |
| 44 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (max) | 0.7830 | 150,529.79 | 0.9314 | ❌ |
| 45 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.5 (high) | 0.7777 | 9,921.85 | 0.2647 | ❌ |
| 46 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash | 0.7770 | 32,907.41 | 0.6569 | ❌ |
| 47 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (xhigh) | 0.7683 | 32,430.78 | 0.6471 | ❌ |
| 48 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (medium) | 0.7677 | 31,455.80 | 0.6275 | ❌ |
| 49 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8-Flash-Next | 0.7617 | 1,405.65 | 0.0098 | ✅ |
| 50 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.2 (max) | 0.7603 | 14,201.02 | 0.3873 | ❌ |
| 51 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (low) | 0.7594 | 3,756.68 | 0.0882 | ❌ |
| 52 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.1 Pro Preview | 0.7580 | 42,051.16 | 0.7255 | ❌ |
| 53 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.6 (max) | 0.7486 | 46,922.00 | 0.7745 | ❌ |
| 54 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 v2 | 0.7443 | 7,820.87 | 0.1961 | ❌ |
| 55 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.1 (xhigh) | 0.7413 | — | — | — |
| 56 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (low) | 0.7375 | 19,996.41 | 0.5000 | ❌ |
| 57 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark | 0.7356 | — | — | — |
| 58 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3 Pro Preview (high) | 0.7333 | — | — | — |
| 59 | <img src="https://artificialanalysis.ai/img/logos/sapiens.svg" width="18" alt="Sapiens AI" /> Sapiens AI | Agnes 2.5 Pro Beta | 0.7329 | — | — | — |
| 60 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (medium) | 0.7302 | 7,363.85 | 0.1667 | ❌ |
| 61 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.6 Flash | 0.7295 | 16,678.95 | 0.4216 | ❌ |
| 62 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (max) | 0.7270 | 19,910.57 | 0.4902 | ❌ |
| 63 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.6 | 0.7234 | 21,820.50 | 0.5294 | ❌ |
| 64 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (high) | 0.7225 | 12,214.63 | 0.3137 | ❌ |
| 65 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (low) | 0.7219 | — | — | — |
| 66 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (xhigh) | 0.7203 | 132,881.82 | 0.9020 | ❌ |
| 67 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 Codex (xhigh) | 0.7196 | — | — | — |
| 68 | <img src="https://artificialanalysis.ai/img/logos/sapiens.svg" width="18" alt="Sapiens AI" /> Sapiens AI | Agnes 3.0 Flash | 0.7186 | 448.72 | 0.0000 | ✅ |
| 69 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 Max Preview | 0.7180 | 21,588.18 | 0.5196 | ❌ |
| 70 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro 0813 (max) | 0.7148 | 11,012.72 | 0.2941 | ❌ |
| 71 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (low) | 0.7075 | 26,575.76 | 0.5980 | ❌ |
| 72 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.5 | 0.7048 | 39,388.69 | 0.6863 | ❌ |
| 73 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 | 0.7045 | — | — | — |
| 74 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.7 (Non-reasoning, high) | 0.7003 | 21,896.11 | 0.5490 | ❌ |
| 75 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (low) | 0.6950 | 10,299.02 | 0.2745 | ❌ |
| 76 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash (max) | 0.6941 | 3,215.00 | 0.0588 | ❌ |
| 77 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.7 Max | 0.6893 | 27,871.92 | 0.6078 | ❌ |
| 78 | <img src="https://artificialanalysis.ai/img/logos/motif_small.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif 3 | 0.6887 | — | — | — |
| 79 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3 Flash | 0.6882 | 5,794.75 | 0.1373 | ❌ |
| 80 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (xhigh) | 0.6849 | 8,237.24 | 0.2059 | ❌ |
| 81 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (low) | 0.6820 | 13,487.58 | 0.3627 | ❌ |
| 82 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 Plus | 0.6795 | 18,953.15 | 0.4804 | ❌ |
| 83 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (xhigh) | 0.6792 | 6,465.25 | 0.1569 | ❌ |
| 84 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash Vision (max) | 0.6771 | 3,664.59 | 0.0735 | ❌ |
| 85 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash 0731 (max) | 0.6766 | 3,664.59 | 0.0735 | ❌ |
| 86 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (low) | 0.6725 | 5,124.98 | 0.1275 | ❌ |
| 87 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Pro | 0.6708 | — | — | — |
| 88 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (high) | 0.6655 | 2,431.48 | 0.0392 | ❌ |
| 89 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (medium) | 0.6652 | — | — | — |
| 90 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (max) | 0.6648 | 99,427.47 | 0.8725 | ❌ |
| 91 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3 (low) | 0.6558 | 41,923.47 | 0.7108 | ❌ |
| 92 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (medium) | 0.6542 | 11,130.43 | 0.3039 | ❌ |
| 93 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 Codex (high) | 0.6518 | — | — | — |
| 94 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (max) | 0.6513 | 4,504.69 | 0.1078 | ❌ |
| 95 | <img src="https://artificialanalysis.ai/img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M3 | 0.6480 | 3,766.07 | 0.0980 | ❌ |
| 96 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5 | 0.6467 | 13,957.77 | 0.3725 | ❌ |
| 97 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 (high) | 0.6465 | 37,183.44 | 0.6667 | ❌ |
| 98 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.7 Plus | 0.6415 | 4,642.52 | 0.1176 | ❌ |
| 99 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (high) | 0.6413 | 1,816.73 | 0.0294 | ❌ |
| 100 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (xhigh) | 0.6389 | 16,941.79 | 0.4314 | ❌ |
| 101 | <img src="https://artificialanalysis.ai/img/logos/apodex.svg" width="18" alt="Apodex" /> Apodex | Apodex 1.1 | 0.6336 | — | — | — |
| 102 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 Codex (high) | 0.6335 | — | — | — |
| 103 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.1 | 0.6277 | 21,975.98 | 0.5588 | ❌ |
| 104 | <img src="https://artificialanalysis.ai/img/logos/motif_small.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif 3 (Beta) | 0.6269 | — | — | — |
| 105 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Omni-0327 | 0.6237 | — | — | — |
| 106 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (medium) | 0.6214 | 41,119.86 | 0.6961 | ❌ |
| 107 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok Build 0.1 0616 | 0.6159 | 7,421.77 | 0.1765 | ❌ |
| 108 | <img src="https://artificialanalysis.ai/img/logos/mbzuai_small.svg" width="18" alt="MBZUAI Institute of Foundation Models" /> MBZUAI Institute of Foundation Models | K2 Horizon 375B A23B | 0.6152 | — | — | — |
| 109 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.6 (Non-reasoning, high) | 0.6146 | 22,751.23 | 0.5686 | ❌ |
| 110 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5-Turbo | 0.6141 | — | — | — |
| 111 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.7 Code | 0.6123 | 13,216.68 | 0.3529 | ❌ |
| 112 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 | 0.6121 | — | — | — |
| 113 | <img src="https://artificialanalysis.ai/img/logos/nex_small.svg" width="18" alt="Nex AGI" /> Nex AGI | Nex-N2-Pro | 0.6106 | 8,881.80 | 0.2451 | ❌ |
| 114 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (high) | 0.6098 | 8,413.17 | 0.2255 | ❌ |
| 115 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (xhigh) | 0.6062 | 109,833.22 | 0.8824 | ❌ |
| 116 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 Instant (May 2026) | 0.6029 | — | — | — |
| 117 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (high) | 0.6012 | 58,246.95 | 0.8235 | ❌ |
| 118 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Opus | 0.6002 | — | — | — |
| 119 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (high) | 0.5978 | 9,148.26 | 0.2549 | ❌ |
| 120 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (low) | 0.5938 | 10,705.21 | 0.2843 | ❌ |
| 121 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5-Pro | 0.5935 | 2,438.44 | 0.0490 | ❌ |
| 122 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (minimal) | 0.5927 | 8,252.94 | 0.2157 | ❌ |
| 123 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (Non-reasoning) | 0.5925 | 8,870.88 | 0.2353 | ❌ |
| 124 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 27B | 0.5912 | 6,158.16 | 0.1471 | ❌ |
| 125 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash (Feb 2026) | 0.5909 | — | — | — |
| 126 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Omni | 0.5893 | — | — | — |
| 127 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-3.0-flash-VL | 0.5887 | 0.00 | 0.0000 | ✅ |
| 128 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (max) | 0.5882 | — | — | — |
| 129 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o3 | 0.5881 | 15,235.14 | 0.4083 | ❌ |
| 130 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.5 | 0.5868 | — | — | — |
| 131 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM 5V Turbo | 0.5847 | — | — | — |
| 132 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5 | 0.5822 | 800.33 | 0.0050 | ❌ |
| 133 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (Non-reasoning) | 0.5801 | 17,750.68 | 0.4492 | ❌ |
| 134 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (medium) | 0.5787 | 4,056.33 | 0.1021 | ❌ |
| 135 | <img src="https://artificialanalysis.ai/img/logos/thinking_machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling | 0.5781 | 12,262.58 | 0.3157 | ❌ |
| 136 | <img src="https://artificialanalysis.ai/img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Open2 250B | 0.5775 | — | — | — |
| 137 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.1 Opus | 0.5765 | — | — | — |
| 138 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (Non-reasoning, high) | 0.5752 | 13,513.19 | 0.3633 | ❌ |
| 139 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 Thinking | 0.5743 | 6,566.33 | 0.1580 | ❌ |
| 140 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.5 (Non-reasoning) | 0.5726 | 22,027.56 | 0.5595 | ❌ |
| 141 | <img src="https://artificialanalysis.ai/img/logos/thinking_machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling Small | 0.5720 | 3,726.53 | 0.0835 | ❌ |
| 142 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (xhigh) | 0.5712 | 13,305.64 | 0.3562 | ❌ |
| 143 | <img src="https://artificialanalysis.ai/img/logos/multiversecomputing_small.svg" width="18" alt="Multiverse Computing" /> Multiverse Computing | Quasar 438B (max) | 0.5711 | 4,816.33 | 0.1213 | ❌ |
| 144 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (Non-reasoning, low) | 0.5695 | 13,673.55 | 0.3667 | ❌ |
| 145 | <img src="https://artificialanalysis.ai/img/logos/china_mobile_small.png" width="18" alt="China Mobile" /> China Mobile | JT-4.1 Flash 236B A21B | 0.5681 | — | — | — |
| 146 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.6 (Non-reasoning) | 0.5674 | 4,471.41 | 0.1074 | ❌ |
| 147 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3 Pro Preview (low) | 0.5669 | — | — | — |
| 148 | <img src="https://artificialanalysis.ai/img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 4 | 0.5640 | 3,726.53 | 0.0835 | ❌ |
| 149 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (high) | 0.5634 | — | — | — |
| 150 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 27B | 0.5620 | 22,549.93 | 0.5661 | ❌ |
| 151 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 Codex mini (high) | 0.5576 | — | — | — |
| 152 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Sonnet | 0.5553 | 20,411.05 | 0.5040 | ❌ |
| 153 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (low) | 0.5545 | 12,302.63 | 0.3173 | ❌ |
| 154 | <img src="https://artificialanalysis.ai/img/logos/tencent_small.svg" width="18" alt="Tencent" /> Tencent | Hy3-preview | 0.5541 | — | — | — |
| 155 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (medium) | 0.5536 | 8,237.24 | 0.2059 | ❌ |
| 156 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Ultra | 0.5516 | 9,425.88 | 0.2585 | ❌ |
| 157 | <img src="https://artificialanalysis.ai/img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.5 | 0.5482 | 3,481.89 | 0.0678 | ❌ |
| 158 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.1 (Non-reasoning) | 0.5481 | 5,794.23 | 0.1372 | ❌ |
| 159 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 Omni Plus | 0.5469 | 3,513.99 | 0.0688 | ❌ |
| 160 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 397B A17B | 0.5451 | 13,585.93 | 0.3648 | ❌ |
| 161 | <img src="https://artificialanalysis.ai/img/logos/kwaikat_small.svg" width="18" alt="KwaiKAT" /> KwaiKAT | KAT-Coder-Pro V2 | 0.5424 | — | — | — |
| 162 | <img src="https://artificialanalysis.ai/img/logos/sktelecom_small.svg" width="18" alt="SK Telecom" /> SK Telecom | A.X-K2 | 0.5411 | — | — | — |
| 163 | <img src="https://artificialanalysis.ai/img/logos/tencent_small.svg" width="18" alt="Tencent" /> Tencent | Hy3 | 0.5407 | 1,778.78 | 0.0280 | ❌ |
| 164 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.1 Fast | 0.5400 | — | — | — |
| 165 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (low) | 0.5393 | 8,237.24 | 0.2059 | ❌ |
| 166 | <img src="https://artificialanalysis.ai/img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.7 | 0.5387 | 4,320.47 | 0.1056 | ❌ |
| 167 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.0 Flash | 0.5386 | 731.63 | 0.0042 | ❌ |
| 168 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash-Lite | 0.5363 | 7,666.43 | 0.1885 | ❌ |
| 169 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano | 0.5340 | 1,997.00 | 0.0326 | ❌ |
| 170 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max Thinking | 0.5334 | — | — | — |
| 171 | <img src="https://artificialanalysis.ai/img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.1 | 0.5331 | 3,158.16 | 0.0582 | ❌ |
| 172 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (medium) | 0.5322 | 1,263.31 | 0.0089 | ❌ |
| 173 | <img src="https://artificialanalysis.ai/img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step 3.7 Flash | 0.5281 | 3,359.35 | 0.0638 | ❌ |
| 174 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 35B A3B | 0.5274 | 5,131.80 | 0.1276 | ❌ |
| 175 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (medium) | 0.5250 | 8,930.48 | 0.2469 | ❌ |
| 176 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B | 0.5243 | 2,758.91 | 0.0534 | ❌ |
| 177 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7 | 0.5239 | 11,500.00 | 0.3074 | ❌ |
| 178 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 | 0.5238 | — | — | — |
| 179 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.5 (Non-reasoning) | 0.5224 | — | — | — |
| 180 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash | 0.5211 | — | — | — |
| 181 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (medium) | 0.5204 | 6,363.78 | 0.1537 | ❌ |
| 182 | <img src="https://artificialanalysis.ai/img/logos/sapiens.svg" width="18" alt="Sapiens AI" /> Sapiens AI | Agnes 2.5 Pro Alpha | 0.5156 | 2,581.97 | 0.0510 | ❌ |
| 183 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3 Flash (Non-reasoning) | 0.5156 | 2,721.72 | 0.0529 | ❌ |
| 184 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (Non-reasoning) | 0.5147 | 24,690.81 | 0.5846 | ❌ |
| 185 | <img src="https://artificialanalysis.ai/img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | G9v3-39A5B | 0.5143 | — | — | — |
| 186 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 35B A3B | 0.5132 | 13,461.45 | 0.3618 | ❌ |
| 187 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5 (Non-reasoning) | 0.5110 | 4,304.72 | 0.1054 | ❌ |
| 188 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Sonnet | 0.5055 | — | — | — |
| 189 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 122B A10B | 0.5054 | 8,210.88 | 0.2053 | ❌ |
| 190 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 397B A17B (Non-reasoning) | 0.5048 | 2,706.75 | 0.0527 | ❌ |
| 191 | <img src="https://artificialanalysis.ai/img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step 3.5 Flash 2603 | 0.5038 | 992.18 | 0.0068 | ❌ |
| 192 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 Fast | 0.4980 | — | — | — |
| 193 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 3 mini Reasoning (high) | 0.4899 | 2,118.62 | 0.0346 | ❌ |
| 194 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 27B (Non-reasoning) | 0.4895 | 2,444.46 | 0.0491 | ❌ |
| 195 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Sonnet (Non-reasoning) | 0.4892 | 13,066.44 | 0.3473 | ❌ |
| 196 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Speciale | 0.4882 | — | — | — |
| 197 | <img src="https://artificialanalysis.ai/img/logos/china_mobile_small.png" width="18" alt="China Mobile" /> China Mobile | JT-35B-Flash | 0.4866 | — | — | — |
| 198 | <img src="https://artificialanalysis.ai/img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step 3.5 Flash | 0.4860 | 802.72 | 0.0050 | ❌ |
| 199 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 31B | 0.4838 | 0.00 | 0.0000 | ❌ |
| 200 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Glimmer (high) | 0.4783 | 4,313.44 | 0.1055 | ❌ |
| 201 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (low) | 0.4769 | 1,105.93 | 0.0077 | ❌ |
| 202 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (high) | 0.4763 | 17,668.55 | 0.4484 | ❌ |
| 203 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (Non-reasoning) | 0.4744 | 12,518.68 | 0.3260 | ❌ |
| 204 | <img src="https://artificialanalysis.ai/img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2 | 0.4733 | 3,158.16 | 0.0582 | ❌ |
| 205 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.2 (Non-reasoning) | 0.4719 | 6,414.23 | 0.1553 | ❌ |
| 206 | <img src="https://artificialanalysis.ai/img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE 2.0 | 0.4708 | — | — | — |
| 207 | <img src="https://artificialanalysis.ai/img/logos/bytedance_small.svg" width="18" alt="ByteDance Seed" /> ByteDance Seed | Doubao Seed Code | 0.4705 | — | — | — |
| 208 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 Instant (June 2026) | 0.4705 | 82,372.44 | 0.8492 | ❌ |
| 209 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o4-mini (high) | 0.4703 | 17,946.55 | 0.4517 | ❌ |
| 210 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o1 | 0.4693 | — | — | — |
| 211 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (low) | 0.4662 | 8,918.54 | 0.2465 | ❌ |
| 212 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (Non-reasoning) | 0.4657 | 10,166.26 | 0.2711 | ❌ |
| 213 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 27B (Non-reasoning) | 0.4629 | 2,841.13 | 0.0544 | ❌ |
| 214 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (Non-reasoning) | 0.4590 | 791.24 | 0.0049 | ❌ |
| 215 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-2.6-1T | 0.4553 | 6,408.16 | 0.1551 | ❌ |
| 216 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.7 Sonnet | 0.4551 | — | — | — |
| 217 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3.5 | 0.4541 | 20,961.73 | 0.5091 | ❌ |
| 218 | <img src="https://artificialanalysis.ai/img/logos/kwaikat_small.svg" width="18" alt="KwaiKAT" /> KwaiKAT | KAT-Coder-Pro V1 | 0.4524 | — | — | — |
| 219 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Sonnet (Non-reasoning) | 0.4518 | — | — | — |
| 220 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (medium) | 0.4484 | 28,614.52 | 0.6102 | ❌ |
| 221 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Sep) | 0.4464 | — | — | — |
| 222 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 122B A10B (Non-reasoning) | 0.4444 | 2,835.87 | 0.0544 | ❌ |
| 223 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Haiku | 0.4437 | 11,713.07 | 0.3093 | ❌ |
| 224 | <img src="https://artificialanalysis.ai/img/logos/cohere_small.svg" width="18" alt="Cohere" /> Cohere | Command A+ | 0.4433 | 0.00 | 0.0000 | ❌ |
| 225 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Exp | 0.4418 | — | — | — |
| 226 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Pro | 0.4415 | 37,185.22 | 0.6667 | ❌ |
| 227 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (Non-reasoning) | 0.4397 | 10,436.50 | 0.2779 | ❌ |
| 228 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (low) | 0.4329 | 25,659.01 | 0.5918 | ❌ |
| 229 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.7 Sonnet (Non-reasoning) | 0.4313 | — | — | — |
| 230 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max Thinking (Preview) | 0.4303 | 15,632.65 | 0.4108 | ❌ |
| 231 | <img src="https://artificialanalysis.ai/img/logos/longcat_small.svg" width="18" alt="LongCat" /> LongCat | LongCat 2.0 | 0.4286 | — | — | — |
| 232 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash | 0.4253 | 10,250.93 | 0.2733 | ❌ |
| 233 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (medium) | 0.4243 | 6,408.16 | 0.1551 | ❌ |
| 234 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 9B | 0.4226 | 571.17 | 0.0021 | ❌ |
| 235 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5-Pro (Non-reasoning) | 0.4207 | 918.55 | 0.0062 | ❌ |
| 236 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Haiku (Non-reasoning) | 0.4201 | 4,384.05 | 0.1064 | ❌ |
| 237 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 Terminus | 0.4197 | — | — | — |
| 238 | <img src="https://artificialanalysis.ai/img/logos/baidu_small.svg" width="18" alt="Baidu" /> Baidu | ERNIE 5.0 Thinking Preview | 0.4170 | — | — | — |
| 239 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 0905 | 0.4169 | 1,685.86 | 0.0243 | ❌ |
| 240 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.1 Flash-Lite | 0.4165 | 3,800.18 | 0.0985 | ❌ |
| 241 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (Non-reasoning) | 0.4161 | — | — | — |
| 242 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 235B A22B (Reasoning) | 0.4159 | 10,210.88 | 0.2723 | ❌ |
| 243 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 26B A4B | 0.4151 | — | — | — |
| 244 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 (Non-reasoning) | 0.4144 | — | — | — |
| 245 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-2.6-1T | 0.4128 | — | — | — |
| 246 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 35B A3B (Non-reasoning) | 0.4088 | 1,963.09 | 0.0320 | ❌ |
| 247 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (low) | 0.4085 | — | — | — |
| 248 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 (Non-reasoning) | 0.4072 | — | — | — |
| 249 | <img src="https://artificialanalysis.ai/img/logos/tencent_small.svg" width="18" alt="Tencent" /> Tencent | Hy3-preview (Non-reasoning) | 0.4055 | — | — | — |
| 250 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (high) | 0.4055 | 5,423.19 | 0.1320 | ❌ |
| 251 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6 | 0.4049 | 11,000.00 | 0.2937 | ❌ |
| 252 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (medium) | 0.4033 | 2,087.04 | 0.0341 | ❌ |
| 253 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7 (Non-reasoning) | 0.4024 | 6,660.54 | 0.1591 | ❌ |
| 254 | <img src="https://artificialanalysis.ai/img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.5 33B | 0.4020 | — | — | — |
| 255 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (medium) | 0.4009 | — | — | — |
| 256 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 v2 (Non-reasoning) | 0.3986 | 3,944.58 | 0.1006 | ❌ |
| 257 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 4B | 0.3970 | 390.82 | 0.0000 | ❌ |
| 258 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 12B | 0.3947 | 802.72 | 0.0050 | ❌ |
| 259 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 | 0.3939 | — | — | — |
| 260 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5 | 0.3931 | — | — | — |
| 261 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (high) | 0.3899 | 6,408.16 | 0.1551 | ❌ |
| 262 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max | 0.3876 | 4,339.93 | 0.1058 | ❌ |
| 263 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 31B (Non-reasoning) | 0.3845 | 1,635.37 | 0.0222 | ❌ |
| 264 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok Code Fast 1 | 0.3844 | — | — | — |
| 265 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 | 0.3832 | 1,608.54 | 0.0210 | ❌ |
| 266 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 0528 | 0.3825 | — | — | — |
| 267 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash (Non-reasoning) | 0.3818 | — | — | — |
| 268 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 35B A3B (Non-reasoning) | 0.3816 | 1,831.49 | 0.0297 | ❌ |
| 269 | <img src="https://artificialanalysis.ai/img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE | 0.3812 | — | — | — |
| 270 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Sep) (Non-reasoning) | 0.3768 | — | — | — |
| 271 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.2 30B | 0.3743 | 2,088.27 | 0.0341 | ❌ |
| 272 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (Non-reasoning) | 0.3743 | 1,033.30 | 0.0072 | ❌ |
| 273 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (minimal) | 0.3739 | 7,827.61 | 0.1962 | ❌ |
| 274 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 32B (Reasoning) | 0.3729 | 1,684.35 | 0.0242 | ❌ |
| 275 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 | 0.3717 | 10,957.43 | 0.2924 | ❌ |
| 276 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 (Non-reasoning) | 0.3704 | 8,080.77 | 0.2023 | ❌ |
| 277 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (low) | 0.3694 | 6,408.16 | 0.1551 | ❌ |
| 278 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7-Flash | 0.3685 | 1,700.00 | 0.0248 | ❌ |
| 279 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (Non-reasoning) | 0.3664 | 4,017.55 | 0.1016 | ❌ |
| 280 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6 (Non-reasoning) | 0.3653 | 1,716.21 | 0.0255 | ❌ |
| 281 | <img src="https://artificialanalysis.ai/img/logos/servicenow_small.svg" width="18" alt="ServiceNow" /> ServiceNow | Apriel-v1.5-15B-Thinker | 0.3619 | — | — | — |
| 282 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Super | 0.3598 | 1,726.49 | 0.0259 | ❌ |
| 283 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 9B (Non-reasoning) | 0.3587 | 234.76 | 0.0000 | ❌ |
| 284 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 Omni Flash | 0.3574 | 768.15 | 0.0046 | ❌ |
| 285 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder 480B | 0.3562 | 5,694.40 | 0.1359 | ❌ |
| 286 | <img src="https://artificialanalysis.ai/img/logos/deepcogito_small.png" width="18" alt="Deep Cogito" /> Deep Cogito | Cogito v2.1 | 0.3555 | — | — | — |
| 287 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Sep) | 0.3552 | — | — | — |
| 288 | <img src="https://artificialanalysis.ai/img/logos/inceptionlabs_small.svg" width="18" alt="Inception" /> Inception | Mercury 2 | 0.3530 | 2,701.65 | 0.0527 | ❌ |
| 289 | <img src="https://artificialanalysis.ai/img/logos/servicenow_small.svg" width="18" alt="ServiceNow" /> ServiceNow | Apriel-v1.6-15B-Thinker | 0.3512 | — | — | — |
| 290 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 26B A4B (Non-reasoning) | 0.3505 | 1,492.61 | 0.0150 | ❌ |
| 291 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 3 | 0.3492 | — | — | — |
| 292 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6V | 0.3490 | 2,408.16 | 0.0389 | ❌ |
| 293 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 Terminus (Non-reasoning) | 0.3482 | — | — | — |
| 294 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron Cascade 2 30B A3B | 0.3451 | — | — | — |
| 295 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (ChatGPT) | 0.3428 | — | — | — |
| 296 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Magistral Medium 1.2 | 0.3374 | — | — | — |
| 297 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max (Preview) | 0.3369 | 5,034.84 | 0.1257 | ❌ |
| 298 | <img src="https://artificialanalysis.ai/img/logos/arcee_small.svg" width="18" alt="Arcee AI" /> Arcee AI | Trinity Large Thinking | 0.3367 | 2,381.80 | 0.0385 | ❌ |
| 299 | <img src="https://artificialanalysis.ai/img/logos/openbmb_small.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-2B | 0.3359 | — | — | — |
| 300 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3.5 Lightning | 0.3349 | 1,005.27 | 0.0069 | ❌ |
| 301 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.0 Tiny | 0.3319 | 0.00 | 0.0000 | ❌ |
| 302 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Exp (Non-reasoning) | 0.3307 | — | — | — |
| 303 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-120b (high) | 0.3291 | 2,750.68 | 0.0533 | ❌ |
| 304 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Sep) (Non-reasoning) | 0.3280 | — | — | — |
| 305 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 (Non-reasoning) | 0.3275 | — | — | — |
| 306 | <img src="https://artificialanalysis.ai/img/logos/multiversecomputing_small.svg" width="18" alt="Multiverse Computing" /> Multiverse Computing | HyperNova 60B 2605 (high) | 0.3261 | 371.09 | 0.0000 | ❌ |
| 307 | <img src="https://artificialanalysis.ai/img/logos/bytedance_small.svg" width="18" alt="ByteDance Seed" /> ByteDance Seed | Seed-OSS-36B-Instruct | 0.3234 | 1,535.71 | 0.0174 | ❌ |
| 308 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o (Nov) | 0.3195 | 21,849.98 | 0.5396 | ❌ |
| 309 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B A22B 2507 | 0.3193 | 5,871.26 | 0.1394 | ❌ |
| 310 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Non-reasoning) | 0.3180 | 1,916.64 | 0.0312 | ❌ |
| 311 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B 2507 (Non-reasoning) | 0.3163 | 708.48 | 0.0039 | ❌ |
| 312 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o (Aug) | 0.3163 | 19,328.18 | 0.4843 | ❌ |
| 313 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite | 0.3134 | 2,463.60 | 0.0494 | ❌ |
| 314 | <img src="https://artificialanalysis.ai/img/logos/cohere_small.svg" width="18" alt="Cohere" /> Cohere | North Mini Code | 0.3103 | 0.00 | 0.0000 | ❌ |
| 315 | <img src="https://artificialanalysis.ai/img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | G9v3-3B | 0.3100 | — | — | — |
| 316 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.1 Fast (Non-reasoning) | 0.3098 | — | — | — |
| 317 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (minimal) | 0.3089 | 1,531.55 | 0.0172 | ❌ |
| 318 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 4 | 0.3086 | 1,579.08 | 0.0198 | ❌ |
| 319 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 12B (Non-reasoning) | 0.3077 | 275.79 | 0.0000 | ❌ |
| 320 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 235B A22B | 0.3073 | 1,227.20 | 0.0086 | ❌ |
| 321 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | QwQ-32B | 0.3044 | — | — | — |
| 322 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-1T | 0.3042 | — | — | — |
| 323 | <img src="https://artificialanalysis.ai/img/logos/openbmb_small.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-1B | 0.3040 | — | — | — |
| 324 | <img src="https://artificialanalysis.ai/img/logos/openbmb_small.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-1B (Non-reasoning) | 0.3040 | — | — | — |
| 325 | <img src="https://artificialanalysis.ai/img/logos/mbzuai_small.svg" width="18" alt="MBZUAI Institute of Foundation Models" /> MBZUAI Institute of Foundation Models | K2 Think V2 | 0.3033 | — | — | — |
| 326 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Pixtral Large | 0.3016 | — | — | — |
| 327 | <img src="https://artificialanalysis.ai/img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Open 100B | 0.2993 | — | — | — |
| 328 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o3-mini | 0.2971 | 13,262.54 | 0.3546 | ❌ |
| 329 | <img src="https://artificialanalysis.ai/img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax M1 80k | 0.2960 | — | — | — |
| 330 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5-Air | 0.2957 | 2,539.63 | 0.0505 | ❌ |
| 331 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (Non-reasoning) | 0.2954 | 3,915.68 | 0.1002 | ❌ |
| 332 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 4B (Non-reasoning) | 0.2930 | 92.86 | 0.0000 | ❌ |
| 333 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder Next | 0.2927 | 4,301.61 | 0.1053 | ❌ |
| 334 | <img src="https://artificialanalysis.ai/img/logos/china_mobile_small.png" width="18" alt="China Mobile" /> China Mobile | JT-MINI | 0.2911 | — | — | — |
| 335 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Next 80B A3B (Reasoning) | 0.2910 | 3,079.08 | 0.0573 | ❌ |
| 336 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3 | 0.2895 | 1,873.14 | 0.0304 | ❌ |
| 337 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.2 8B | 0.2888 | 798.72 | 0.0050 | ❌ |
| 338 | <img src="https://artificialanalysis.ai/img/logos/naver_small.webp" width="18" alt="Naver" /> Naver | HyperCLOVA X SEED Think (32B) | 0.2887 | — | — | — |
| 339 | <img src="https://artificialanalysis.ai/img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax M1 40k | 0.2884 | — | — | — |
| 340 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 Fast (Non-reasoning) | 0.2873 | — | — | — |
| 341 | <img src="https://artificialanalysis.ai/img/logos/mbzuai_small.svg" width="18" alt="MBZUAI Institute of Foundation Models" /> MBZUAI Institute of Foundation Models | K2-V2 (high) | 0.2865 | — | — | — |
| 342 | <img src="https://artificialanalysis.ai/img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE (Non-reasoning) | 0.2860 | — | — | — |
| 343 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (Non-reasoning) | 0.2854 | 6,732.72 | 0.1599 | ❌ |
| 344 | <img src="https://artificialanalysis.ai/img/logos/korea-telecom_small.png" width="18" alt="Korea Telecom" /> Korea Telecom | Mi:dm K 2.5 Pro | 0.2836 | — | — | — |
| 345 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (Non-reasoning) | 0.2822 | 1,091.59 | 0.0076 | ❌ |
| 346 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o3-mini (high) | 0.2802 | 25,223.73 | 0.5887 | ❌ |
| 347 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | DiffusionGemma 26B A4B | 0.2774 | — | — | — |
| 348 | <img src="https://artificialanalysis.ai/img/logos/prime-intellect_small.svg" width="18" alt="Prime Intellect" /> Prime Intellect | INTELLECT-3 | 0.2772 | — | — | — |
| 349 | <img src="https://artificialanalysis.ai/img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 3 | 0.2770 | 1,721.17 | 0.0257 | ❌ |
| 350 | <img src="https://artificialanalysis.ai/img/logos/trillionlabs_small.svg" width="18" alt="Trillion Labs" /> Trillion Labs | Tri-21B-think Preview | 0.2755 | — | — | — |
| 351 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 30B A3B (Reasoning) | 0.2746 | 6,105.44 | 0.1457 | ❌ |
| 352 | <img src="https://artificialanalysis.ai/img/logos/longcat_small.svg" width="18" alt="LongCat" /> LongCat | LongCat Flash Lite | 0.2742 | — | — | — |
| 353 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 E4B | 0.2740 | 260.54 | 0.0000 | ❌ |
| 354 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-20b (low) | 0.2733 | 536.90 | 0.0015 | ❌ |
| 355 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.1 405B | 0.2722 | — | — | — |
| 356 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova Premier | 0.2715 | 14,702.06 | 0.4049 | ❌ |
| 357 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 2.6 Flash | 0.2707 | — | — | — |
| 358 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 E4B (Non-reasoning) | 0.2705 | 64.17 | 0.0000 | ❌ |
| 359 | <img src="https://artificialanalysis.ai/img/logos/trillionlabs_small.svg" width="18" alt="Trillion Labs" /> Trillion Labs | Tri-21B-Think | 0.2698 | — | — | — |
| 360 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano | 0.2661 | 526.36 | 0.0014 | ❌ |
| 361 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (Non-reasoning) | 0.2630 | 1,794.52 | 0.0286 | ❌ |
| 362 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 32B | 0.2624 | 515.97 | 0.0012 | ❌ |
| 363 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Next 80B A3B | 0.2623 | 1,131.38 | 0.0079 | ❌ |
| 364 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano Omni 30B A3B | 0.2609 | — | — | — |
| 365 | <img src="https://artificialanalysis.ai/img/logos/nousresearch_small.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 405B | 0.2605 | 8,027.21 | 0.2010 | ❌ |
| 366 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 mini | 0.2597 | 2,103.87 | 0.0343 | ❌ |
| 367 | <img src="https://artificialanalysis.ai/img/logos/mbzuai_small.svg" width="18" alt="MBZUAI Institute of Foundation Models" /> MBZUAI Institute of Foundation Models | K2-V2 (medium) | 0.2577 | — | — | — |
| 368 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Large 3 | 0.2573 | 1,130.82 | 0.0079 | ❌ |
| 369 | <img src="https://artificialanalysis.ai/img/logos/korea-telecom_small.png" width="18" alt="Korea Telecom" /> Korea Telecom | Mi:dm K 2.5 Pro Preview | 0.2570 | — | — | — |
| 370 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-1T | 0.2570 | — | — | — |
| 371 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 (Jan) | 0.2569 | — | — | — |
| 372 | <img src="https://artificialanalysis.ai/img/logos/motif_small.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif-2-12.7B | 0.2565 | — | — | — |
| 373 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3 0324 | 0.2548 | — | — | — |
| 374 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 8B (Reasoning) | 0.2536 | 5,344.90 | 0.1308 | ❌ |
| 375 | <img src="https://artificialanalysis.ai/img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step3 VL 10B | 0.2522 | — | — | — |
| 376 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-20b (high) | 0.2506 | 506.63 | 0.0010 | ❌ |
| 377 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Super 49B v1.5 | 0.2497 | 1,210.88 | 0.0085 | ❌ |
| 378 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.0 Flash | 0.2492 | — | — | — |
| 379 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7-Flash (Non-reasoning) | 0.2490 | 300.01 | 0.0000 | ❌ |
| 380 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-120b (low) | 0.2483 | 2,862.50 | 0.0547 | ❌ |
| 381 | <img src="https://artificialanalysis.ai/img/logos/baidu_small.svg" width="18" alt="Baidu" /> Baidu | ERNIE 4.5 300B A47B | 0.2462 | — | — | — |
| 382 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 4 Maverick | 0.2460 | 2,986.43 | 0.0562 | ❌ |
| 383 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Magistral Medium 1 | 0.2460 | — | — | — |
| 384 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral Medium | 0.2440 | — | — | — |
| 385 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.5 Haiku | 0.2433 | — | — | — |
| 386 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B 2507 | 0.2432 | — | — | — |
| 387 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (Non-reasoning) | 0.2428 | — | — | — |
| 388 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral 2 | 0.2426 | 0.00 | 0.0000 | ❌ |
| 389 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 4 (Non-reasoning) | 0.2426 | 443.68 | 0.0000 | ❌ |
| 390 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4 | 0.2423 | — | — | — |
| 391 | <img src="https://artificialanalysis.ai/img/logos/nousresearch_small.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 405B (Non-reasoning) | 0.2410 | 2,333.98 | 0.0378 | ❌ |
| 392 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder 30B A3B | 0.2398 | 1,913.30 | 0.0312 | ❌ |
| 393 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3.1 | 0.2379 | 1,769.50 | 0.0276 | ❌ |
| 394 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-8B-A1B | 0.2376 | — | — | — |
| 395 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 30B A3B | 0.2372 | 699.02 | 0.0038 | ❌ |
| 396 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6V (Non-reasoning) | 0.2365 | 779.50 | 0.0047 | ❌ |
| 397 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Omni 30B A3B (Reasoning) | 0.2347 | 2,556.80 | 0.0507 | ❌ |
| 398 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B A3B 2507 | 0.2342 | 6,105.44 | 0.1457 | ❌ |
| 399 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B | 0.2308 | 21,369.05 | 0.5158 | ❌ |
| 400 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5V | 0.2299 | 4,816.33 | 0.1213 | ❌ |
| 401 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 12B v2 VL | 0.2289 | 1,605.44 | 0.0209 | ❌ |
| 402 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Large 2 (Nov) | 0.2278 | — | — | — |
| 403 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.2 3B | 0.2273 | 386.86 | 0.0000 | ❌ |
| 404 | <img src="https://artificialanalysis.ai/img/logos/tii_small.svg" width="18" alt="TII UAE" /> TII UAE | Falcon-H1R-7B | 0.2264 | — | — | — |
| 405 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Ultra | 0.2255 | — | — | — |
| 406 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral Small 2 | 0.2223 | 0.00 | 0.0000 | ❌ |
| 407 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 E2B | 0.2171 | — | — | — |
| 408 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova Pro | 0.2165 | — | — | — |
| 409 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3.1 32B Think | 0.2156 | — | — | — |
| 410 | <img src="https://artificialanalysis.ai/img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam 105B (high) | 0.2151 | — | — | — |
| 411 | <img src="https://artificialanalysis.ai/img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.0 32B | 0.2141 | — | — | — |
| 412 | <img src="https://artificialanalysis.ai/img/logos/mbzuai_small.svg" width="18" alt="MBZUAI Institute of Foundation Models" /> MBZUAI Institute of Foundation Models | K2-V2 (low) | 0.2121 | — | — | — |
| 413 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 9B V2 | 0.2118 | 421.09 | 0.0000 | ❌ |
| 414 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Non-reasoning) | 0.2093 | 381.98 | 0.0000 | ❌ |
| 415 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-flash-2.0 | 0.2093 | — | — | — |
| 416 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Super 49B v1.5 (Non-reasoning) | 0.2075 | 519.78 | 0.0013 | ❌ |
| 417 | <img src="https://artificialanalysis.ai/img/logos/nousresearch_small.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 70B | 0.2059 | — | — | — |
| 418 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-2.6B | 0.2049 | 0.00 | 0.0000 | ❌ |
| 419 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral Small (May) | 0.2046 | — | — | — |
| 420 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova Lite | 0.2041 | 331.87 | 0.0000 | ❌ |
| 421 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Magistral Small 1.2 | 0.2015 | — | — | — |
| 422 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.3 Nemotron Super 49B | 0.2011 | — | — | — |
| 423 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 32B | 0.1998 | — | — | — |
| 424 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen2.5 72B | 0.1998 | — | — | — |
| 425 | <img src="https://artificialanalysis.ai/img/logos/nanbeige_small.png" width="18" alt="Nanbeige" /> Nanbeige | Nanbeige4.1-3B | 0.1993 | — | — | — |
| 426 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-flash-2.0 | 0.1990 | 367.86 | 0.0000 | ❌ |
| 427 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 8B | 0.1987 | 631.99 | 0.0029 | ❌ |
| 428 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 2B | 0.1975 | — | — | — |
| 429 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3 (Dec) | 0.1975 | — | — | — |
| 430 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B | 0.1971 | 6,105.44 | 0.1457 | ❌ |
| 431 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Magistral Small 1 | 0.1970 | — | — | — |
| 432 | <img src="https://artificialanalysis.ai/img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 2 | 0.1920 | — | — | — |
| 433 | <img src="https://artificialanalysis.ai/img/logos/cohere_small.svg" width="18" alt="Cohere" /> Cohere | Command A | 0.1917 | 7,334.67 | 0.1664 | ❌ |
| 434 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Large 2 (Jul) | 0.1913 | — | — | — |
| 435 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral Small | 0.1911 | — | — | — |
| 436 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B (Non-reasoning) | 0.1910 | 2,228.83 | 0.0363 | ❌ |
| 437 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.1 Nemotron 70B | 0.1896 | 1,808.82 | 0.0291 | ❌ |
| 438 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 4B (Reasoning) | 0.1873 | — | — | — |
| 439 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3 Haiku | 0.1859 | — | — | — |
| 440 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3.2 | 0.1853 | 234.74 | 0.0000 | ❌ |
| 441 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.3 Nemotron Super 49B (Non-reasoning) | 0.1844 | — | — | — |
| 442 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B A3B 2507 (Non-reasoning) | 0.1826 | 709.36 | 0.0039 | ❌ |
| 443 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.1 70B | 0.1808 | 632.02 | 0.0029 | ❌ |
| 444 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 9B V2 (Non-reasoning) | 0.1804 | 177.51 | 0.0000 | ❌ |
| 445 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B | 0.1803 | — | — | — |
| 446 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5V (Non-reasoning) | 0.1788 | 1,394.68 | 0.0097 | ❌ |
| 447 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 E2B (Non-reasoning) | 0.1787 | — | — | — |
| 448 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 32B (Non-reasoning) | 0.1779 | 571.85 | 0.0021 | ❌ |
| 449 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3.1 | 0.1770 | 232.76 | 0.0000 | ❌ |
| 450 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano 4B | 0.1752 | — | — | — |
| 451 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 32B | 0.1752 | 1,684.35 | 0.0242 | ❌ |
| 452 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 4 Scout | 0.1742 | 499.63 | 0.0009 | ❌ |
| 453 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3.1 32B Instruct | 0.1731 | — | — | — |
| 454 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Omni 30B A3B | 0.1716 | 792.54 | 0.0049 | ❌ |
| 455 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (minimal) | 0.1709 | 337.02 | 0.0000 | ❌ |
| 456 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B 2507 (Non-reasoning) | 0.1695 | — | — | — |
| 457 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 14B | 0.1684 | 10,684.52 | 0.2838 | ❌ |
| 458 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Ministral 3 14B | 0.1680 | 221.86 | 0.0000 | ❌ |
| 459 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 32B Think | 0.1655 | — | — | — |
| 460 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Llama 70B | 0.1650 | 3,119.05 | 0.0577 | ❌ |
| 461 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 14B | 0.1635 | — | — | — |
| 462 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.1 30B | 0.1632 | — | — | — |
| 463 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi Linear 48B A3B Instruct | 0.1631 | — | — | — |
| 464 | <img src="https://artificialanalysis.ai/img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 2 (Non-reasoning) | 0.1624 | — | — | — |
| 465 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 2B (Non-reasoning) | 0.1623 | — | — | — |
| 466 | <img src="https://artificialanalysis.ai/img/logos/nousresearch_small.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 70B (Non-reasoning) | 0.1594 | — | — | — |
| 467 | <img src="https://artificialanalysis.ai/img/logos/ai21_small.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba Reasoning 3B | 0.1589 | — | — | — |
| 468 | <img src="https://artificialanalysis.ai/img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.0 32B (Non-reasoning) | 0.1568 | — | — | — |
| 469 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 nano | 0.1554 | 525.68 | 0.0014 | ❌ |
| 470 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.3 70B | 0.1553 | 7,012.62 | 0.1630 | ❌ |
| 471 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.1 8B | 0.1549 | 41.64 | 0.0000 | ❌ |
| 472 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova Micro | 0.1540 | 201.83 | 0.0000 | ❌ |
| 473 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 24B A2B | 0.1535 | — | — | — |
| 474 | <img src="https://artificialanalysis.ai/img/logos/ai21_small.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba 1.7 Large | 0.1524 | — | — | — |
| 475 | <img src="https://artificialanalysis.ai/img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam 30B (high) | 0.1506 | — | — | — |
| 476 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o mini | 0.1499 | 1,180.36 | 0.0083 | ❌ |
| 477 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 12B v2 VL (Non-reasoning) | 0.1490 | 498.75 | 0.0009 | ❌ |
| 478 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3 | 0.1483 | 236.91 | 0.0000 | ❌ |
| 479 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.1 8B | 0.1452 | 86.08 | 0.0000 | ❌ |
| 480 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B (Non-reasoning) | 0.1444 | 700.54 | 0.0038 | ❌ |
| 481 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano (Non-reasoning) | 0.1418 | 155.93 | 0.0000 | ❌ |
| 482 | <img src="https://artificialanalysis.ai/img/logos/celeris.svg" width="18" alt="Celeris" /> Celeris | Celeris-1 | 0.1387 | 1,051.58 | 0.0073 | ❌ |
| 483 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H Small | 0.1386 | 284.13 | 0.0000 | ❌ |
| 484 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 4B | 0.1383 | — | — | — |
| 485 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Ministral 3 8B | 0.1372 | 163.68 | 0.0000 | ❌ |
| 486 | <img src="https://artificialanalysis.ai/img/logos/openbmb_small.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM-V 4.6 1.3B | 0.1364 | — | — | — |
| 487 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 0528 Qwen3 8B | 0.1347 | — | — | — |
| 488 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 14B (Non-reasoning) | 0.1325 | 1,122.65 | 0.0079 | ❌ |
| 489 | <img src="https://artificialanalysis.ai/img/logos/microsoft_small.svg" width="18" alt="Microsoft" /> Microsoft | Phi-4 | 0.1279 | 365.77 | 0.0000 | ❌ |
| 490 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.1 Nemotron Nano 4B v1.1 | 0.1266 | — | — | — |
| 491 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 270M | 0.1252 | — | — | — |
| 492 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 8B | 0.1237 | 5,344.90 | 0.1308 | ❌ |
| 493 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3 70B | 0.1199 | — | — | — |
| 494 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.2 11B (Vision) | 0.1196 | 364.78 | 0.0000 | ❌ |
| 495 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.2 3B | 0.1165 | — | — | — |
| 496 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 7B Think | 0.1159 | — | — | — |
| 497 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 27B | 0.1150 | — | — | — |
| 498 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-1.2B-Instruct | 0.1094 | — | — | — |
| 499 | <img src="https://artificialanalysis.ai/img/logos/reka_small.svg" width="18" alt="Reka AI" /> Reka AI | Reka Flash 3 | 0.1089 | — | — | — |
| 500 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 2.6B | 0.1086 | — | — | — |
| 501 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-mini-2.0 | 0.1082 | — | — | — |
| 502 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 8B (Non-reasoning) | 0.1072 | 545.35 | 0.0017 | ❌ |
| 503 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Ministral 3 3B | 0.1067 | 114.49 | 0.0000 | ❌ |
| 504 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 0.8B | 0.1067 | — | — | — |
| 505 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Molmo2-8B | 0.1044 | — | — | — |
| 506 | <img src="https://artificialanalysis.ai/img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam M | 0.1039 | — | — | — |
| 507 | <img src="https://artificialanalysis.ai/img/logos/ai21_small.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba 1.7 Mini | 0.1026 | — | — | — |
| 508 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-1.2B-Thinking | 0.1012 | — | — | — |
| 509 | <img src="https://artificialanalysis.ai/img/logos/swiss-ai-initiative_small.png" width="18" alt="Swiss AI Initiative" /> Swiss AI Initiative | Apertus 70B Instruct | 0.0946 | — | — | — |
| 510 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 7B | 0.0930 | — | — | — |
| 511 | <img src="https://artificialanalysis.ai/img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | Exaone 4.0 1.2B | 0.0920 | — | — | — |
| 512 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H 1B | 0.0914 | — | — | — |
| 513 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | OLMo 2 32B | 0.0913 | — | — | — |
| 514 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.2 1B | 0.0906 | — | — | — |
| 515 | <img src="https://artificialanalysis.ai/img/logos/microsoft_small.svg" width="18" alt="Microsoft" /> Microsoft | Phi-4 Mini | 0.0901 | 0.00 | 0.0000 | ❌ |
| 516 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 1.7B | 0.0891 | — | — | — |
| 517 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 0.8B (Non-reasoning) | 0.0861 | — | — | — |
| 518 | <img src="https://artificialanalysis.ai/img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | Exaone 4.0 1.2B (Non-reasoning) | 0.0850 | — | — | — |
| 519 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 8B A1B | 0.0832 | — | — | — |
| 520 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 Micro | 0.0806 | — | — | — |
| 521 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.1 3B | 0.0801 | — | — | — |
| 522 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 12B | 0.0769 | — | — | — |
| 523 | <img src="https://artificialanalysis.ai/img/logos/microsoft_small.svg" width="18" alt="Microsoft" /> Microsoft | Phi-3 Mini | 0.0751 | — | — | — |
| 524 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 3.3 8B | 0.0722 | 245.32 | 0.0000 | ❌ |
| 525 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-VL-1.6B | 0.0699 | — | — | — |
| 526 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 1B | 0.0690 | — | — | — |
| 527 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 350M | 0.0682 | — | — | — |
| 528 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 1.2B | 0.0663 | — | — | — |
| 529 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 0.6B | 0.0656 | — | — | — |
| 530 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3 8B | 0.0654 | — | — | — |
| 531 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral 7B | 0.0631 | 272.96 | 0.0000 | ❌ |
| 532 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 4B | 0.0613 | — | — | — |
| 533 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 1.7B (Non-reasoning) | 0.0574 | — | — | — |
| 534 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 1B | 0.0570 | — | — | — |
| 535 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | OLMo 2 7B | 0.0569 | — | — | — |
| 536 | <img src="https://artificialanalysis.ai/img/logos/swiss-ai-initiative_small.png" width="18" alt="Swiss AI Initiative" /> Swiss AI Initiative | Apertus 8B Instruct | 0.0560 | — | — | — |
| 537 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3n E4B | 0.0542 | — | — | — |
| 538 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H 350M | 0.0518 | — | — | — |
| 539 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Molmo 7B-D | 0.0486 | — | — | — |
| 540 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 0.6B (Non-reasoning) | 0.0445 | — | — | — |
| 541 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3n E2B | 0.0369 | — | — | — |
| 542 | <img src="https://artificialanalysis.ai/img/logos/cohere_small.svg" width="18" alt="Cohere" /> Cohere | Tiny Aya Global | 0.0365 | — | — | — |
| 543 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 1.5B | 0.0000 | — | — | — |

## 品牌帕累托前沿连线（仅体现在图中）

以下十一个品牌在图中拥有单独的帕累托连线（较窄宽度，品牌主题色，图层高于总体灰色连线）。表中数量为**入图顶点数**——品牌前沿上低于总体前沿第一级的顶点同样不入图（本表与图例一致）：

| 品牌 | 主题色 | 品牌前沿模型数（入图） |
|------|--------|--------------|
| <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | `#cc785c` | 11 |
| <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | `#1f1f1f` | 11 |
| <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | `#0089f4` | 1 |
| <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | `#1c7ff8` | 2 |
| <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | `#34A853` | 4 |
| <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | `#736cd3` | 6 |
| <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | `#047AFE` | 3 |
| <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | `#ff7018` | 3 |
| <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | `#2243e6` | 3 |
| <img src="https://artificialanalysis.ai/img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | `#EB3568` | 1 |
| <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | `#ff6900` | 1 |

## 评分方法

1. **20项评估指标**各自线性归一化到 [0,1]
   （AA Intelligence Index、GPQA Diamond、Humanity's Last Exam、MMMU Pro、IFBench Instruction Following、SciCode Coding、CritPt Physics、AA-LCR Long Context、AA Omniscience Index、AA-Omniscience Accuracy、AA-Omniscience Non-Hallucination、GDPval-AA Normalized、AA Analyst Agent、APEX-Agents-AA、ITBench-SRE、τ²-Bench Telecom、τ³-Bench Banking、Terminal-Bench Hard、Terminal-Bench 2.1、Terminal-Bench 4.0）
   > V18（2026-09-12）：AA 更新了基准列——新增 AA Analyst Agent、τ³-Bench Banking、Terminal-Bench 2.1 / 4.0 四项；AA Agentic Index 与 AA Coding Index 已从 AA 的数据源中移除，相应剔除。指标数由 18 → 20。
2. **综合能力值** = 所有有效归一化分数的算术平均
3. **综合能力再归一化**：线性映射到 [0,1]，性能最好的模型 = 1，最差的模型 = 0
4. **Pareto前沿** = 不被任何其他模型支配的模型（综合能力 ≥ 且成本 ≤，且至少一项严格更优；成本为 0 的免费模型同样参与——横轴左端恒为 0，免费模型是合法前沿候选）
5. **模型范围** = Status: All（含已弃用模型；缺少足够评估数据者不参与排名）
6. **图表纵轴基线（V17）**：图表的 y = 0 取总体帕累托前沿的第一级（最低能力；本例 y0 = 0.5887，即前沿左端点 Ling-3.0-flash-VL）；综合能力低于该级的模型不出现在图表中（表格不受影响）。图中纵坐标 chart_y = (能力 - y0)/(1 - y0)，因此前沿左端点恰好落在 (0, 0)、最优模型恰好为 y = 1。该过滤在横轴映射构建之前完成


## 横轴映射（分位数等密度映射，V17）与分布分析

横轴（单请求成本）按**经验分位数（rank）映射**——以 103 个入图正成本模型（综合能力 ≥ 前沿第一级）的成本分布为基准：

```
x = 0                            当 c ≤ 0（免费模型，钉在最左缘）
x = interp(log10(c); knots)      当 c > 0
```

其中 knots = (log10(c_i), 名次_i/(n-1)) 为入图正成本模型按成本排序后的 97 个锚点（相同 log10(c) 的并列组取平均名次，保证 x 是 z = log10(c) 的单值函数；n-1 归一化使最大成本恰为 x = 1）。该映射在 **y 基线过滤之后**构建（V17：先以帕累托前沿第一级为 y = 0、剔除低性能模型，再对入图模型建映射）。（V18 修正：并列判定改用相同的 log10(c)，消除浮点上相差 ~1e-12 的成本经 log10 后折合到同一 z 造成的同 z 双锚点、个别模型 x 偏离名次的问题；修正后 x 对每个入图模型严格线性于名次。）

**该映射保证：**

- **函数端点严格钉死**：c = 0 → x = 0；最大成本 → x = 1——函数经过 (0,0) 与 (1,1)；
- **严格均匀密度**：x 是模型名次的线性函数（相同 log10(c) 并列组取平均名次），因此**任意等宽区段的模型数恒定**（每 0.1 宽度约 10 个模型）——无论截取哪一段，模型数 ÷ 宽度都等于全图的模型总数 ÷ 总宽度。V12 的单一 logistic 函数在过滤后的分布上做不到（十分位在 8~24 间摆动），故替换为精确分位数映射；
- 各数量级区间的入图模型数：1–10: 0，10–100: 0，100–1k: 1，1k–10k: 27，10k–100k: 62
- **同一倍率区间的宽度 ∝ 该区间模型数**——均匀密度的必然结果：1k→10k 与 100k→1M 同为 10 倍率，但前者 27 个模型、后者 13 个，前者宽度约为后者的 2.1 倍。若改用「等倍率等距」（纯对数轴），两段的模型密度将相差 2.1 倍，与均匀密度目标冲突——两者数学上不可兼得，本图以均匀密度（最高优先级）为准；
- **左端恒为 0**（c = 0；1 个免费模型位于最左缘）
- 最低正成本 448.72 → x = 0.0000；最高成本 998,846 → x = 1.0000（严格 = 1）
- 中位数位置 0.500（≈ 0.5 居中）；左右两半模型数：左 52 / 右 52
- 横轴十分位模型数：12，10，10，10，10，11，10，10，10，11（x 为名次的线性函数；n/10 非整数时各十分位在 ±1 内取整，相同 log10(c) 并列组共享同一 x、落在边界的哪一侧可再移动 ±1）
- **10^x 数量级指示**（位置 = x(10^x)）：10^0 → 0.000，10^1 → 0.000，10^2 → 0.000，10^3 → 0.007，10^4 → 0.267，10^5 → 0.873

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
**模型总数（Status: All）**: 543 个参与排名（另有模型因评估数据不足未列入；总体帕累托前沿 12 个；图表入图 104 个——综合能力 ≥ 前沿第一级）  

## 图表说明（黑底）

（V17 起本说明置于文末，图表之后直接跟随模型表格。）

图表说明：**灰色实线** = 总体帕累托前沿；**彩色细线** = 十一个品牌的单独帕累托前沿（品牌主题色，图层高于总体连线；暗色品牌元素带窄白边；顶点按（横轴位置、能力升序）连接，等成本点自下而上）；品牌前沿模型圆点同样使用品牌颜色。模型名称/思考程度标注优先骑在连线之上（点的左/右两侧皆可，同一条线段可容纳两个标签——各贴各的点；文字与连线平行、中轴线重合，连线仅在文字两侧绘制）；骑线位被其他标签占据时自动「让位」——占用者挪到自己的另一个骑线位，双方都保持骑线；实在骑不上线时按四级优先依次退让（V16）：离点最近位置的上方/下方平行偏移 → 点的两条连线延长线上就近 → 两连线夹角扇区内就近。标签规则（V13/V15）：品牌前沿模型共享的前导块按「最长有效切点」剔除 —— 切点止于分界符，或止于字母且其后紧跟数字（如 Claude Opus 5 → Opus 5、GPT-5.6 Sol → 5.6 Sol、Kimi K2.6 → 2.6、Qwen3.8 Max → 3.8 Max、MiMo-V2.5 → 2.5、MiniMax-M2.1 → 2.1）；(non-reasoning) 简写为 (non)；同一模型在品牌连线上相邻出现 2 次以上时仅性能最低者保留全名、相邻较高者只标思考程度，不相邻的重复出现保留全名（每次重新计算）；标签位置与序列同向（V15）——品牌前沿上越靠右上的模型，其标签重心必须同时更靠右且更靠上（两分量都 >= 0，至少是 (0,0)，仅其一非负不算合格；初始放置违反时自动就近重摆，单标签无解（被前后邻居夹死）时按窗口级联重排整体挪动，均不产生新的重叠）。纵轴 y = 0 = 总体帕累托前沿第一级（y0 = 0.5887，前沿左端点 Ling-3.0-flash-VL 恰为 (0,0)），能力低于该级的 416 个模型与缺少成本数据的 23 个模型不出现在图中；横轴为分位数等密度映射（见上文「横轴映射」节），10^x 数量级指示位于 x(10^x)，同一倍率区间的宽度与该区间内模型数成正比。
