# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

## 全部模型（综合能力从高到低，最优 = 1，最差 = 0）

共收录 **Status: All**（含已弃用）的全部模型；按重新归一化后的综合能力排序。「帕累托」列：✅ = 总体帕累托前沿模型，❌ = 被支配，— = 无成本数据无法判定。图表纵轴以总体帕累托前沿第一级（y0 = 0.5020，即前沿左端点 Gemma 4 31B）为 0：综合能力 ≥ 该级且有成本数据的 151 个模型入图，350 个能力低于第一级、41 个缺少成本数据的模型不出现在图中（本表不受影响，仍完整列出全部模型）。

| # | 品牌 | 模型 | 综合能力 | 单请求成本 | 横轴位置 | 帕累托 |
|---|------|------|---------|-----------|-----------|------|
| 1 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (max with fallback) | 1.0000 | 993,565.79 | 0.9933 | ✅ |
| 2 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (xhigh with fallback) | 0.9923 | 347,784.11 | 0.9799 | ✅ |
| 3 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (max) | 0.9762 | 1,050,667.16 | 1.0000 | ❌ |
| 4 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (xhigh) | 0.9699 | 462,548.07 | 0.9866 | ❌ |
| 5 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (max) | 0.9633 | 104,243.46 | 0.9060 | ✅ |
| 6 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (high with fallback) | 0.9592 | 102,197.80 | 0.8993 | ✅ |
| 7 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (high) | 0.9560 | 171,903.51 | 0.9463 | ❌ |
| 8 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5 (with fallback) | 0.9560 | 293,962.09 | 0.9732 | ❌ |
| 9 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (xhigh) | 0.9508 | 57,520.10 | 0.8456 | ✅ |
| 10 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (medium) | 0.9398 | 57,792.25 | 0.8523 | ❌ |
| 11 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (high) | 0.9309 | 42,914.42 | 0.8121 | ✅ |
| 12 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (max) | 0.9292 | 195,355.06 | 0.9530 | ❌ |
| 13 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.3 (max) | 0.9268 | 12,935.13 | 0.4530 | ✅ |
| 14 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (medium with fallback) | 0.9264 | 58,294.96 | 0.8591 | ❌ |
| 15 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.3 (xhigh) | 0.9210 | 12,935.13 | 0.4530 | ❌ |
| 16 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (low) | 0.9003 | 50,251.48 | 0.8322 | ❌ |
| 17 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3 (max) | 0.8977 | 42,488.50 | 0.8020 | ❌ |
| 18 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (low with fallback) | 0.8934 | 52,918.45 | 0.8389 | ❌ |
| 19 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (medium) | 0.8915 | 26,628.38 | 0.7114 | ❌ |
| 20 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (xhigh) | 0.8903 | 79,394.03 | 0.8792 | ❌ |
| 21 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (xhigh) | 0.8877 | 23,056.11 | 0.6711 | ❌ |
| 22 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (high) | 0.8850 | 21,882.69 | 0.6242 | ❌ |
| 23 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (medium) | 0.8740 | 19,910.34 | 0.5973 | ❌ |
| 24 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (high) | 0.8695 | 31,767.03 | 0.7315 | ❌ |
| 25 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.8 (max) | 0.8658 | 41,599.37 | 0.7852 | ❌ |
| 26 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3 (max) | 0.8648 | 14,439.59 | 0.5369 | ❌ |
| 27 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (high) | 0.8634 | 20,226.41 | 0.6040 | ❌ |
| 28 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (xhigh) | 0.8612 | 117,618.16 | 0.9329 | ❌ |
| 29 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (max) | 0.8551 | 203,257.74 | 0.9597 | ❌ |
| 30 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.2 (xhigh) | 0.8436 | 12,935.13 | 0.4530 | ❌ |
| 31 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (medium) | 0.8418 | 22,856.19 | 0.6577 | ❌ |
| 32 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (high) | 0.8416 | 59,199.42 | 0.8658 | ❌ |
| 33 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (Non-reasoning) | 0.8384 | — | — | — |
| 34 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (high) | 0.8321 | 14,442.48 | 0.5436 | ❌ |
| 35 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (medium) | 0.8303 | 10,783.37 | 0.3826 | ✅ |
| 36 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 Max | 0.8295 | 18,788.84 | 0.5738 | ❌ |
| 37 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.5 (high) | 0.8213 | 10,601.16 | 0.3758 | ✅ |
| 38 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 2.4T A95B | 0.8208 | 18,788.84 | 0.5738 | ❌ |
| 39 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (max) | 0.8172 | 154,388.97 | 0.9396 | ❌ |
| 40 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.7 (max) | 0.8171 | 37,922.72 | 0.7584 | ❌ |
| 41 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (low) | 0.8151 | 24,704.11 | 0.6913 | ❌ |
| 42 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3-Flash | 0.8116 | 1,601.32 | 0.0336 | ✅ |
| 43 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (xhigh) | 0.8091 | 33,991.43 | 0.7383 | ❌ |
| 44 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (xhigh) | 0.8089 | 208,465.01 | 0.9664 | ❌ |
| 45 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (medium) | 0.8088 | 8,951.41 | 0.3356 | ❌ |
| 46 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.2 (max) | 0.8052 | 14,439.59 | 0.5369 | ❌ |
| 47 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (medium) | 0.8006 | 35,841.41 | 0.7517 | ❌ |
| 48 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash | 0.7968 | 38,250.95 | 0.7651 | ❌ |
| 49 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (medium) | 0.7851 | 34,066.76 | 0.7450 | ❌ |
| 50 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.3 Codex (xhigh) | 0.7847 | 111,626.07 | 0.9262 | ❌ |
| 51 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.1 Pro Preview | 0.7795 | 46,124.54 | 0.8255 | ❌ |
| 52 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (low) | 0.7782 | 20,904.86 | 0.6174 | ❌ |
| 53 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.1 (xhigh) | 0.7779 | — | — | — |
| 54 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (high) | 0.7670 | 12,356.31 | 0.4228 | ❌ |
| 55 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.6 Flash | 0.7657 | 14,434.59 | 0.5235 | ❌ |
| 56 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (max) | 0.7652 | 20,872.97 | 0.6107 | ❌ |
| 57 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8-Flash-Next | 0.7651 | 1,433.69 | 0.0268 | ✅ |
| 58 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (low) | 0.7651 | 3,904.97 | 0.1678 | ❌ |
| 59 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.7 Max | 0.7620 | 28,290.47 | 0.7248 | ❌ |
| 60 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (low) | 0.7523 | 3,896.84 | 0.1611 | ❌ |
| 61 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro 0813 (max) | 0.7428 | 11,279.75 | 0.3893 | ❌ |
| 62 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.6 (max) | 0.7425 | 41,867.24 | 0.7919 | ❌ |
| 63 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (low) | 0.7417 | 11,463.79 | 0.4094 | ❌ |
| 64 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 v2 | 0.7383 | 8,779.41 | 0.3221 | ❌ |
| 65 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark | 0.7326 | — | — | — |
| 66 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (xhigh) | 0.7318 | 8,423.89 | 0.3087 | ❌ |
| 67 | <img src="https://artificialanalysis.ai/img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M3 | 0.7300 | 3,831.99 | 0.1544 | ❌ |
| 68 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3 Pro Preview (high) | 0.7273 | — | — | — |
| 69 | <img src="https://artificialanalysis.ai/img/logos/sapiens.svg" width="18" alt="Sapiens AI" /> Sapiens AI | Agnes 2.5 Pro Beta | 0.7257 | — | — | — |
| 70 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (medium) | 0.7242 | 6,863.36 | 0.2617 | ❌ |
| 71 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (xhigh) | 0.7239 | 25,795.62 | 0.7047 | ❌ |
| 72 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (low) | 0.7177 | 27,174.60 | 0.7181 | ❌ |
| 73 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.6 | 0.7154 | 21,985.82 | 0.6376 | ❌ |
| 74 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (xhigh) | 0.7144 | 106,181.25 | 0.9128 | ❌ |
| 75 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 Codex (xhigh) | 0.7137 | — | — | — |
| 76 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 Max Preview | 0.7122 | 21,901.04 | 0.6309 | ❌ |
| 77 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (xhigh) | 0.7108 | 8,331.42 | 0.2953 | ❌ |
| 78 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash Vision (max) | 0.7091 | 3,753.74 | 0.1208 | ❌ |
| 79 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (max) | 0.7061 | 97,133.31 | 0.8926 | ❌ |
| 80 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash 0731 (max) | 0.7053 | 3,753.74 | 0.1208 | ❌ |
| 81 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3 Flash | 0.7026 | 6,062.47 | 0.2349 | ❌ |
| 82 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (medium) | 0.6994 | 11,446.49 | 0.4027 | ❌ |
| 83 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.5 | 0.6990 | 41,077.77 | 0.7785 | ❌ |
| 84 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 | 0.6988 | — | — | — |
| 85 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (high) | 0.6959 | 2,308.44 | 0.0537 | ❌ |
| 86 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.7 (Non-reasoning, high) | 0.6946 | 23,003.99 | 0.6644 | ❌ |
| 87 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 Plus | 0.6917 | 19,073.48 | 0.5839 | ❌ |
| 88 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (max) | 0.6841 | 4,594.97 | 0.1879 | ❌ |
| 89 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (high) | 0.6806 | 14,219.32 | 0.5034 | ❌ |
| 90 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (low) | 0.6764 | 14,227.09 | 0.5101 | ❌ |
| 91 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (high) | 0.6755 | 10,256.97 | 0.3691 | ❌ |
| 92 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.7 Plus | 0.6749 | 4,738.78 | 0.2013 | ❌ |
| 93 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.1 | 0.6743 | 22,172.69 | 0.6443 | ❌ |
| 94 | <img src="https://artificialanalysis.ai/img/logos/motif_small.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif 3 | 0.6743 | — | — | — |
| 95 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (high) | 0.6703 | 2,521.76 | 0.0604 | ❌ |
| 96 | <img src="https://artificialanalysis.ai/img/logos/mbzuai_small.svg" width="18" alt="MBZUAI Institute of Foundation Models" /> MBZUAI Institute of Foundation Models | K2 Horizon 375B A23B | 0.6678 | — | — | — |
| 97 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 (high) | 0.6670 | 43,836.28 | 0.8188 | ❌ |
| 98 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (low) | 0.6670 | 5,469.67 | 0.2215 | ❌ |
| 99 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3 (low) | 0.6662 | 42,488.50 | 0.8020 | ❌ |
| 100 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Pro | 0.6654 | — | — | — |
| 101 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (medium) | 0.6598 | — | — | — |
| 102 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5-Pro | 0.6544 | 2,528.72 | 0.0671 | ❌ |
| 103 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok Build 0.1 0616 | 0.6487 | 7,589.19 | 0.2685 | ❌ |
| 104 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.7 Code | 0.6483 | 13,375.73 | 0.4631 | ❌ |
| 105 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (xhigh) | 0.6469 | 110,988.83 | 0.9195 | ❌ |
| 106 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 Codex (high) | 0.6465 | — | — | — |
| 107 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5 | 0.6414 | 14,125.19 | 0.4899 | ❌ |
| 108 | <img src="https://artificialanalysis.ai/img/logos/apodex.svg" width="18" alt="Apodex" /> Apodex | Apodex 1.1 | 0.6356 | — | — | — |
| 109 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (low) | 0.6347 | 11,349.48 | 0.3960 | ❌ |
| 110 | <img src="https://artificialanalysis.ai/img/logos/thinking_machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling Small | 0.6283 | 3,776.76 | 0.1342 | ❌ |
| 111 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 Codex (high) | 0.6283 | — | — | — |
| 112 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Ultra | 0.6245 | 9,509.59 | 0.3557 | ❌ |
| 113 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5 | 0.6241 | 829.05 | 0.0067 | ✅ |
| 114 | <img src="https://artificialanalysis.ai/img/logos/nex_small.svg" width="18" alt="Nex AGI" /> Nex AGI | Nex-N2-Pro | 0.6237 | 8,934.12 | 0.3289 | ❌ |
| 115 | <img src="https://artificialanalysis.ai/img/logos/thinking_machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling | 0.6217 | 12,436.28 | 0.4362 | ❌ |
| 116 | <img src="https://artificialanalysis.ai/img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 4 | 0.6211 | 3,776.76 | 0.1342 | ❌ |
| 117 | <img src="https://artificialanalysis.ai/img/logos/motif_small.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif 3 (Beta) | 0.6201 | — | — | — |
| 118 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Omni-0327 | 0.6186 | — | — | — |
| 119 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (medium) | 0.6164 | 38,591.90 | 0.7718 | ❌ |
| 120 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (max) | 0.6159 | — | — | — |
| 121 | <img src="https://artificialanalysis.ai/img/logos/multiversecomputing_small.svg" width="18" alt="Multiverse Computing" /> Multiverse Computing | Quasar 438B (max) | 0.6139 | 4,941.89 | 0.2081 | ❌ |
| 122 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (high) | 0.6130 | 75,127.73 | 0.8725 | ❌ |
| 123 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (Non-reasoning) | 0.6118 | 9,182.61 | 0.3423 | ❌ |
| 124 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.6 (Non-reasoning, high) | 0.6096 | 23,662.90 | 0.6846 | ❌ |
| 125 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5-Turbo | 0.6091 | — | — | — |
| 126 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.5 | 0.6076 | — | — | — |
| 127 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 | 0.6072 | — | — | — |
| 128 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 Instant (May 2026) | 0.5980 | — | — | — |
| 129 | <img src="https://artificialanalysis.ai/img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.7 | 0.5978 | 4,386.39 | 0.1745 | ❌ |
| 130 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 27B | 0.5948 | 22,675.49 | 0.6510 | ❌ |
| 131 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (high) | 0.5928 | — | — | — |
| 132 | <img src="https://artificialanalysis.ai/img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Open2 250B | 0.5917 | — | — | — |
| 133 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (minimal) | 0.5878 | 8,674.90 | 0.3154 | ❌ |
| 134 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 27B | 0.5864 | 6,220.94 | 0.2416 | ❌ |
| 135 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (xhigh) | 0.5862 | 15,154.52 | 0.5503 | ❌ |
| 136 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash (Feb 2026) | 0.5861 | — | — | — |
| 137 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (Non-reasoning) | 0.5859 | 18,787.75 | 0.5638 | ❌ |
| 138 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Omni | 0.5846 | — | — | — |
| 139 | <img src="https://artificialanalysis.ai/img/logos/tencent_small.svg" width="18" alt="Tencent" /> Tencent | Hy3 | 0.5834 | 1,800.12 | 0.0403 | ❌ |
| 140 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o3 | 0.5833 | 17,790.81 | 0.5570 | ❌ |
| 141 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (low) | 0.5822 | 8,331.42 | 0.2953 | ❌ |
| 142 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (medium) | 0.5818 | 1,256.22 | 0.0201 | ❌ |
| 143 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM 5V Turbo | 0.5800 | — | — | — |
| 144 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (medium) | 0.5770 | 9,607.86 | 0.3624 | ❌ |
| 145 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Sonnet | 0.5765 | 19,486.18 | 0.5906 | ❌ |
| 146 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (medium) | 0.5740 | 3,786.47 | 0.1409 | ❌ |
| 147 | <img src="https://artificialanalysis.ai/img/logos/sapiens.svg" width="18" alt="Sapiens AI" /> Sapiens AI | Agnes 2.5 Pro Alpha | 0.5734 | 2,674.05 | 0.0738 | ❌ |
| 148 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.1 Opus | 0.5718 | — | — | — |
| 149 | <img src="https://artificialanalysis.ai/img/logos/kwaikat_small.svg" width="18" alt="KwaiKAT" /> KwaiKAT | KAT-Coder-Pro V2 | 0.5707 | — | — | — |
| 150 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (Non-reasoning, high) | 0.5705 | 14,185.74 | 0.4966 | ❌ |
| 151 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 Thinking | 0.5696 | 6,691.89 | 0.2550 | ❌ |
| 152 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash-Lite | 0.5692 | 8,109.64 | 0.2752 | ❌ |
| 153 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 397B A17B | 0.5690 | 13,711.49 | 0.4765 | ❌ |
| 154 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.5 (Non-reasoning) | 0.5679 | 23,312.34 | 0.6779 | ❌ |
| 155 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (Non-reasoning, low) | 0.5649 | 14,284.99 | 0.5168 | ❌ |
| 156 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.6 (Non-reasoning) | 0.5628 | 4,717.74 | 0.1946 | ❌ |
| 157 | <img src="https://artificialanalysis.ai/img/logos/china_mobile_small.png" width="18" alt="China Mobile" /> China Mobile | JT-4.1 Flash 236B A21B | 0.5626 | — | — | — |
| 158 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3 Pro Preview (low) | 0.5623 | — | — | — |
| 159 | <img src="https://artificialanalysis.ai/img/logos/sktelecom_small.svg" width="18" alt="SK Telecom" /> SK Telecom | A.X-K2 | 0.5613 | — | — | — |
| 160 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (Non-reasoning) | 0.5577 | 25,660.02 | 0.6980 | ❌ |
| 161 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (medium) | 0.5547 | 8,331.42 | 0.2953 | ❌ |
| 162 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Opus | 0.5545 | — | — | — |
| 163 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 35B A3B | 0.5542 | 13,539.93 | 0.4698 | ❌ |
| 164 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 Codex mini (high) | 0.5531 | — | — | — |
| 165 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (low) | 0.5500 | 12,369.59 | 0.4295 | ❌ |
| 166 | <img src="https://artificialanalysis.ai/img/logos/tencent_small.svg" width="18" alt="Tencent" /> Tencent | Hy3-preview | 0.5496 | — | — | — |
| 167 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7 | 0.5465 | 11,500.00 | 0.4161 | ❌ |
| 168 | <img src="https://artificialanalysis.ai/img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step 3.7 Flash | 0.5445 | 3,392.84 | 0.1007 | ❌ |
| 169 | <img src="https://artificialanalysis.ai/img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.5 | 0.5438 | 3,554.09 | 0.1074 | ❌ |
| 170 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.1 (Non-reasoning) | 0.5436 | 6,038.22 | 0.2282 | ❌ |
| 171 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 Omni Plus | 0.5424 | 3,822.15 | 0.1477 | ❌ |
| 172 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.1 Fast | 0.5356 | — | — | — |
| 173 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B | 0.5306 | 2,963.59 | 0.0872 | ❌ |
| 174 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano | 0.5296 | 1,853.20 | 0.0470 | ❌ |
| 175 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max Thinking | 0.5290 | — | — | — |
| 176 | <img src="https://artificialanalysis.ai/img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.1 | 0.5288 | 3,220.94 | 0.0940 | ❌ |
| 177 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 122B A10B | 0.5278 | 8,294.59 | 0.2819 | ❌ |
| 178 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 35B A3B | 0.5231 | 5,184.12 | 0.2148 | ❌ |
| 179 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (low) | 0.5229 | 1,197.08 | 0.0134 | ❌ |
| 180 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 | 0.5219 | — | — | — |
| 181 | <img src="https://artificialanalysis.ai/img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | G9v3-39A5B | 0.5206 | — | — | — |
| 182 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.0 Flash | 0.5201 | 744.19 | 0.0000 | ✅ |
| 183 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Sonnet | 0.5184 | — | — | — |
| 184 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.5 (Non-reasoning) | 0.5182 | — | — | — |
| 185 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash | 0.5168 | — | — | — |
| 186 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (medium) | 0.5161 | 6,677.71 | 0.2483 | ❌ |
| 187 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3 Flash (Non-reasoning) | 0.5114 | 2,868.31 | 0.0805 | ❌ |
| 188 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (low) | 0.5111 | 9,499.18 | 0.3490 | ❌ |
| 189 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 Instant (June 2026) | 0.5069 | 83,314.17 | 0.8859 | ❌ |
| 190 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5 (Non-reasoning) | 0.5068 | 4,466.06 | 0.1812 | ❌ |
| 191 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (high) | 0.5036 | 13,795.79 | 0.4832 | ❌ |
| 192 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 31B | 0.5020 | 0.00 | 0.0000 | ✅ |
| 193 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 397B A17B (Non-reasoning) | 0.5007 | 2,906.04 | 0.0832 | ❌ |
| 194 | <img src="https://artificialanalysis.ai/img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step 3.5 Flash 2603 | 0.4997 | 1,008.92 | 0.0103 | ❌ |
| 195 | <img src="https://artificialanalysis.ai/img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE 2.0 | 0.4948 | — | — | — |
| 196 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 Fast | 0.4939 | — | — | — |
| 197 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Glimmer (high) | 0.4914 | 4,378.31 | 0.1744 | ❌ |
| 198 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3.5 | 0.4888 | 21,244.25 | 0.6198 | ❌ |
| 199 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 3 mini Reasoning (high) | 0.4859 | 2,165.71 | 0.0517 | ❌ |
| 200 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 27B (Non-reasoning) | 0.4855 | 2,572.00 | 0.0692 | ❌ |
| 201 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Sonnet (Non-reasoning) | 0.4853 | 13,834.26 | 0.4840 | ❌ |
| 202 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Speciale | 0.4843 | — | — | — |
| 203 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Haiku | 0.4828 | 14,431.10 | 0.5233 | ❌ |
| 204 | <img src="https://artificialanalysis.ai/img/logos/china_mobile_small.png" width="18" alt="China Mobile" /> China Mobile | JT-35B-Flash | 0.4826 | — | — | — |
| 205 | <img src="https://artificialanalysis.ai/img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step 3.5 Flash | 0.4821 | 823.65 | 0.0063 | ❌ |
| 206 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.2 (Non-reasoning) | 0.4821 | 6,646.35 | 0.2479 | ❌ |
| 207 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 27B (Non-reasoning) | 0.4804 | 2,973.90 | 0.0875 | ❌ |
| 208 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-2.6-1T | 0.4773 | 6,470.94 | 0.2453 | ❌ |
| 209 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (Non-reasoning) | 0.4759 | 10,586.91 | 0.3756 | ❌ |
| 210 | <img src="https://artificialanalysis.ai/img/logos/cohere_small.svg" width="18" alt="Cohere" /> Cohere | Command A+ | 0.4707 | 0.00 | 0.0000 | ❌ |
| 211 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (Non-reasoning) | 0.4706 | 12,823.06 | 0.4415 | ❌ |
| 212 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o1 | 0.4695 | — | — | — |
| 213 | <img src="https://artificialanalysis.ai/img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2 | 0.4695 | 3,220.94 | 0.0940 | ❌ |
| 214 | <img src="https://artificialanalysis.ai/img/logos/bytedance_small.svg" width="18" alt="ByteDance Seed" /> ByteDance Seed | Doubao Seed Code | 0.4666 | — | — | — |
| 215 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o4-mini (high) | 0.4665 | 23,593.53 | 0.6832 | ❌ |
| 216 | <img src="https://artificialanalysis.ai/img/logos/longcat_small.svg" width="18" alt="LongCat" /> LongCat | LongCat 2.0 | 0.4647 | 8,066.31 | 0.2746 | ❌ |
| 217 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Pro | 0.4646 | 36,261.21 | 0.7531 | ❌ |
| 218 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 122B A10B (Non-reasoning) | 0.4595 | 3,001.60 | 0.0883 | ❌ |
| 219 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (Non-reasoning) | 0.4553 | 896.26 | 0.0081 | ❌ |
| 220 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (Non-reasoning) | 0.4547 | 10,745.03 | 0.3811 | ❌ |
| 221 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.7 Sonnet | 0.4531 | — | — | — |
| 222 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.1 Flash-Lite | 0.4525 | 3,535.40 | 0.1066 | ❌ |
| 223 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (medium) | 0.4521 | 28,810.82 | 0.7259 | ❌ |
| 224 | <img src="https://artificialanalysis.ai/img/logos/kwaikat_small.svg" width="18" alt="KwaiKAT" /> KwaiKAT | KAT-Coder-Pro V1 | 0.4487 | — | — | — |
| 225 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Sonnet (Non-reasoning) | 0.4481 | — | — | — |
| 226 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Sep) | 0.4427 | — | — | — |
| 227 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 9B | 0.4427 | 599.43 | 0.0000 | ❌ |
| 228 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Exp | 0.4382 | — | — | — |
| 229 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (low) | 0.4376 | 25,920.60 | 0.7057 | ❌ |
| 230 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 Terminus | 0.4299 | — | — | — |
| 231 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 26B A4B | 0.4279 | — | — | — |
| 232 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.7 Sonnet (Non-reasoning) | 0.4278 | — | — | — |
| 233 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max Thinking (Preview) | 0.4268 | 15,883.78 | 0.5523 | ❌ |
| 234 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash | 0.4218 | 10,711.67 | 0.3799 | ❌ |
| 235 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (medium) | 0.4209 | 6,470.94 | 0.2453 | ❌ |
| 236 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 35B A3B (Non-reasoning) | 0.4195 | 2,018.40 | 0.0496 | ❌ |
| 237 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5-Pro (Non-reasoning) | 0.4172 | 911.26 | 0.0084 | ❌ |
| 238 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Haiku (Non-reasoning) | 0.4167 | 4,662.28 | 0.1916 | ❌ |
| 239 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 4B | 0.4144 | 397.09 | 0.0000 | ❌ |
| 240 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6 | 0.4140 | 11,000.00 | 0.3855 | ❌ |
| 241 | <img src="https://artificialanalysis.ai/img/logos/baidu_small.svg" width="18" alt="Baidu" /> Baidu | ERNIE 5.0 Thinking Preview | 0.4136 | — | — | — |
| 242 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 0905 | 0.4135 | 1,806.13 | 0.0410 | ❌ |
| 243 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (Non-reasoning) | 0.4127 | — | — | — |
| 244 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 235B A22B (Reasoning) | 0.4125 | 10,294.59 | 0.3699 | ❌ |
| 245 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 (Non-reasoning) | 0.4110 | — | — | — |
| 246 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-2.6-1T | 0.4095 | — | — | — |
| 247 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (low) | 0.4052 | — | — | — |
| 248 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 (Non-reasoning) | 0.4039 | — | — | — |
| 249 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 31B (Non-reasoning) | 0.4037 | 1,634.75 | 0.0347 | ❌ |
| 250 | <img src="https://artificialanalysis.ai/img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.5 33B | 0.4031 | — | — | — |
| 251 | <img src="https://artificialanalysis.ai/img/logos/tencent_small.svg" width="18" alt="Tencent" /> Tencent | Hy3-preview (Non-reasoning) | 0.4022 | — | — | — |
| 252 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (high) | 0.4022 | 5,685.53 | 0.2241 | ❌ |
| 253 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 35B A3B (Non-reasoning) | 0.4003 | 1,869.61 | 0.0472 | ❌ |
| 254 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (medium) | 0.4000 | 2,353.87 | 0.0552 | ❌ |
| 255 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (Non-reasoning) | 0.3997 | 4,272.26 | 0.1730 | ❌ |
| 256 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7 (Non-reasoning) | 0.3991 | 6,723.56 | 0.2563 | ❌ |
| 257 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 12B | 0.3978 | 823.65 | 0.0063 | ❌ |
| 258 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (medium) | 0.3977 | — | — | — |
| 259 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 v2 (Non-reasoning) | 0.3954 | 4,158.55 | 0.1714 | ❌ |
| 260 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (high) | 0.3951 | 6,470.94 | 0.2453 | ❌ |
| 261 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 | 0.3907 | — | — | — |
| 262 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5 | 0.3899 | — | — | — |
| 263 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.2 30B | 0.3868 | 2,113.38 | 0.0510 | ❌ |
| 264 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max | 0.3845 | 4,621.22 | 0.1894 | ❌ |
| 265 | <img src="https://artificialanalysis.ai/img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE | 0.3833 | — | — | — |
| 266 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (Non-reasoning) | 0.3831 | 1,074.24 | 0.0114 | ❌ |
| 267 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok Code Fast 1 | 0.3813 | — | — | — |
| 268 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 | 0.3801 | 1,702.35 | 0.0371 | ❌ |
| 269 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 0528 | 0.3794 | — | — | — |
| 270 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Sep) (Non-reasoning) | 0.3737 | — | — | — |
| 271 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Super | 0.3735 | 1,766.77 | 0.0392 | ❌ |
| 272 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash (Non-reasoning) | 0.3732 | — | — | — |
| 273 | <img src="https://artificialanalysis.ai/img/logos/inceptionlabs_small.svg" width="18" alt="Inception" /> Inception | Mercury 2 | 0.3726 | 2,845.70 | 0.0798 | ❌ |
| 274 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (minimal) | 0.3708 | 8,107.74 | 0.2751 | ❌ |
| 275 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 32B (Reasoning) | 0.3698 | 1,717.84 | 0.0376 | ❌ |
| 276 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 | 0.3687 | 11,267.78 | 0.3891 | ❌ |
| 277 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 (Non-reasoning) | 0.3674 | 8,310.31 | 0.2876 | ❌ |
| 278 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (low) | 0.3664 | 6,470.94 | 0.2453 | ❌ |
| 279 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7-Flash | 0.3655 | 1,700.00 | 0.0370 | ❌ |
| 280 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6 (Non-reasoning) | 0.3623 | 1,945.90 | 0.0485 | ❌ |
| 281 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Magistral Medium 1.2 | 0.3618 | — | — | — |
| 282 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3.5 Lightning | 0.3607 | 1,007.36 | 0.0103 | ❌ |
| 283 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 9B (Non-reasoning) | 0.3604 | 266.04 | 0.0000 | ❌ |
| 284 | <img src="https://artificialanalysis.ai/img/logos/servicenow_small.svg" width="18" alt="ServiceNow" /> ServiceNow | Apriel-v1.5-15B-Thinker | 0.3589 | — | — | — |
| 285 | <img src="https://artificialanalysis.ai/img/logos/arcee_small.svg" width="18" alt="Arcee AI" /> Arcee AI | Trinity Large Thinking | 0.3571 | 2,434.12 | 0.0577 | ❌ |
| 286 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 Omni Flash | 0.3545 | 822.69 | 0.0062 | ❌ |
| 287 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder 480B | 0.3533 | 6,185.21 | 0.2401 | ❌ |
| 288 | <img src="https://artificialanalysis.ai/img/logos/deepcogito_small.png" width="18" alt="Deep Cogito" /> Deep Cogito | Cogito v2.1 | 0.3526 | — | — | — |
| 289 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Sep) | 0.3523 | — | — | — |
| 290 | <img src="https://artificialanalysis.ai/img/logos/openbmb_small.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-2B | 0.3496 | — | — | — |
| 291 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron Cascade 2 30B A3B | 0.3496 | — | — | — |
| 292 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 4 | 0.3490 | 1,610.47 | 0.0339 | ❌ |
| 293 | <img src="https://artificialanalysis.ai/img/logos/servicenow_small.svg" width="18" alt="ServiceNow" /> ServiceNow | Apriel-v1.6-15B-Thinker | 0.3483 | — | — | — |
| 294 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 26B A4B (Non-reasoning) | 0.3476 | 1,494.38 | 0.0294 | ❌ |
| 295 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 3 | 0.3463 | — | — | — |
| 296 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6V | 0.3462 | 2,470.94 | 0.0589 | ❌ |
| 297 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 Terminus (Non-reasoning) | 0.3454 | — | — | — |
| 298 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-120b (high) | 0.3434 | 2,755.91 | 0.0767 | ❌ |
| 299 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B A22B 2507 | 0.3401 | 5,919.39 | 0.2268 | ❌ |
| 300 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (ChatGPT) | 0.3400 | — | — | — |
| 301 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.0 Tiny | 0.3345 | 0.00 | 0.0000 | ❌ |
| 302 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max (Preview) | 0.3342 | 5,355.79 | 0.2188 | ❌ |
| 303 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Exp (Non-reasoning) | 0.3280 | — | — | — |
| 304 | <img src="https://artificialanalysis.ai/img/logos/cohere_small.svg" width="18" alt="Cohere" /> Cohere | North Mini Code | 0.3257 | 0.00 | 0.0000 | ❌ |
| 305 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Sep) (Non-reasoning) | 0.3253 | — | — | — |
| 306 | <img src="https://artificialanalysis.ai/img/logos/multiversecomputing_small.svg" width="18" alt="Multiverse Computing" /> Multiverse Computing | HyperNova 60B 2605 (high) | 0.3252 | 379.46 | 0.0000 | ❌ |
| 307 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 (Non-reasoning) | 0.3248 | — | — | — |
| 308 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 1.5 Pro (Sep) | 0.3221 | — | — | — |
| 309 | <img src="https://artificialanalysis.ai/img/logos/bytedance_small.svg" width="18" alt="ByteDance Seed" /> ByteDance Seed | Seed-OSS-36B-Instruct | 0.3208 | 1,579.66 | 0.0327 | ❌ |
| 310 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o (Nov) | 0.3169 | 22,158.63 | 0.6438 | ❌ |
| 311 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Non-reasoning) | 0.3154 | 1,986.19 | 0.0491 | ❌ |
| 312 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Next 80B A3B (Reasoning) | 0.3146 | 3,110.47 | 0.0911 | ❌ |
| 313 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B 2507 (Non-reasoning) | 0.3137 | 758.10 | 0.0012 | ❌ |
| 314 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o (Aug) | 0.3137 | 19,522.34 | 0.5912 | ❌ |
| 315 | <img src="https://artificialanalysis.ai/img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | G9v3-3B | 0.3136 | — | — | — |
| 316 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.2 8B | 0.3125 | 808.14 | 0.0051 | ❌ |
| 317 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite | 0.3109 | 3,567.09 | 0.1078 | ❌ |
| 318 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder Next | 0.3101 | 4,267.63 | 0.1729 | ❌ |
| 319 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 4B (Non-reasoning) | 0.3092 | 99.54 | 0.0000 | ❌ |
| 320 | <img src="https://artificialanalysis.ai/img/logos/mbzuai_small.svg" width="18" alt="MBZUAI Institute of Foundation Models" /> MBZUAI Institute of Foundation Models | K2 Think V2 | 0.3088 | — | — | — |
| 321 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.1 Fast (Non-reasoning) | 0.3072 | — | — | — |
| 322 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (minimal) | 0.3064 | 1,606.70 | 0.0337 | ❌ |
| 323 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 12B (Non-reasoning) | 0.3052 | 299.75 | 0.0000 | ❌ |
| 324 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 235B A22B | 0.3048 | 1,312.52 | 0.0224 | ❌ |
| 325 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o3-mini (high) | 0.3028 | 26,407.19 | 0.7096 | ❌ |
| 326 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | QwQ-32B | 0.3019 | — | — | — |
| 327 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-1T | 0.3017 | — | — | — |
| 328 | <img src="https://artificialanalysis.ai/img/logos/openbmb_small.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-1B | 0.3016 | — | — | — |
| 329 | <img src="https://artificialanalysis.ai/img/logos/openbmb_small.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-1B (Non-reasoning) | 0.3015 | — | — | — |
| 330 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Pixtral Large | 0.2992 | — | — | — |
| 331 | <img src="https://artificialanalysis.ai/img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Open 100B | 0.2969 | — | — | — |
| 332 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o3-mini | 0.2947 | 12,738.63 | 0.4403 | ❌ |
| 333 | <img src="https://artificialanalysis.ai/img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax M1 80k | 0.2936 | — | — | — |
| 334 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5-Air | 0.2933 | 2,575.20 | 0.0693 | ❌ |
| 335 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (Non-reasoning) | 0.2930 | 4,060.57 | 0.1700 | ❌ |
| 336 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 2.6 Flash | 0.2902 | — | — | — |
| 337 | <img src="https://artificialanalysis.ai/img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 3 | 0.2890 | 1,749.43 | 0.0386 | ❌ |
| 338 | <img src="https://artificialanalysis.ai/img/logos/china_mobile_small.png" width="18" alt="China Mobile" /> China Mobile | JT-MINI | 0.2887 | — | — | — |
| 339 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (Non-reasoning) | 0.2887 | 7,065.10 | 0.2637 | ❌ |
| 340 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3 | 0.2872 | 1,927.18 | 0.0482 | ❌ |
| 341 | <img src="https://artificialanalysis.ai/img/logos/naver_small.webp" width="18" alt="Naver" /> Naver | HyperCLOVA X SEED Think (32B) | 0.2863 | — | — | — |
| 342 | <img src="https://artificialanalysis.ai/img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax M1 40k | 0.2860 | — | — | — |
| 343 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 Fast (Non-reasoning) | 0.2850 | — | — | — |
| 344 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | DiffusionGemma 26B A4B | 0.2849 | — | — | — |
| 345 | <img src="https://artificialanalysis.ai/img/logos/mbzuai_small.svg" width="18" alt="MBZUAI Institute of Foundation Models" /> MBZUAI Institute of Foundation Models | K2-V2 (high) | 0.2842 | — | — | — |
| 346 | <img src="https://artificialanalysis.ai/img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE (Non-reasoning) | 0.2837 | — | — | — |
| 347 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano | 0.2834 | 536.82 | 0.0000 | ❌ |
| 348 | <img src="https://artificialanalysis.ai/img/logos/korea-telecom_small.png" width="18" alt="Korea Telecom" /> Korea Telecom | Mi:dm K 2.5 Pro | 0.2812 | — | — | — |
| 349 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 mini | 0.2805 | 2,176.04 | 0.0519 | ❌ |
| 350 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (Non-reasoning) | 0.2799 | 1,123.15 | 0.0123 | ❌ |
| 351 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 E4B | 0.2792 | 264.73 | 0.0000 | ❌ |
| 352 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Large 3 | 0.2758 | 1,235.80 | 0.0179 | ❌ |
| 353 | <img src="https://artificialanalysis.ai/img/logos/prime-intellect_small.svg" width="18" alt="Prime Intellect" /> Prime Intellect | INTELLECT-3 | 0.2750 | — | — | — |
| 354 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3 0324 | 0.2733 | — | — | — |
| 355 | <img src="https://artificialanalysis.ai/img/logos/trillionlabs_small.svg" width="18" alt="Trillion Labs" /> Trillion Labs | Tri-21B-think Preview | 0.2733 | — | — | — |
| 356 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 (Jan) | 0.2724 | — | — | — |
| 357 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 30B A3B (Reasoning) | 0.2724 | 6,147.30 | 0.2385 | ❌ |
| 358 | <img src="https://artificialanalysis.ai/img/logos/longcat_small.svg" width="18" alt="LongCat" /> LongCat | LongCat Flash Lite | 0.2719 | — | — | — |
| 359 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-120b (low) | 0.2718 | 2,862.50 | 0.0803 | ❌ |
| 360 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-20b (low) | 0.2711 | 551.55 | 0.0000 | ❌ |
| 361 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.1 405B | 0.2700 | — | — | — |
| 362 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova Premier | 0.2693 | 15,047.21 | 0.5493 | ❌ |
| 363 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 E4B (Non-reasoning) | 0.2683 | 67.74 | 0.0000 | ❌ |
| 364 | <img src="https://artificialanalysis.ai/img/logos/trillionlabs_small.svg" width="18" alt="Trillion Labs" /> Trillion Labs | Tri-21B-Think | 0.2676 | — | — | — |
| 365 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano Omni 30B A3B | 0.2663 | — | — | — |
| 366 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-20b (high) | 0.2649 | 519.19 | 0.0000 | ❌ |
| 367 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 4 Maverick | 0.2644 | 2,992.71 | 0.0880 | ❌ |
| 368 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (Non-reasoning) | 0.2609 | 1,880.61 | 0.0474 | ❌ |
| 369 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 32B | 0.2603 | 551.87 | 0.0000 | ❌ |
| 370 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Next 80B A3B | 0.2602 | 1,161.85 | 0.0129 | ❌ |
| 371 | <img src="https://artificialanalysis.ai/img/logos/nousresearch_small.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 405B | 0.2584 | 8,236.48 | 0.2798 | ❌ |
| 372 | <img src="https://artificialanalysis.ai/img/logos/mbzuai_small.svg" width="18" alt="MBZUAI Institute of Foundation Models" /> MBZUAI Institute of Foundation Models | K2-V2 (medium) | 0.2556 | — | — | — |
| 373 | <img src="https://artificialanalysis.ai/img/logos/korea-telecom_small.png" width="18" alt="Korea Telecom" /> Korea Telecom | Mi:dm K 2.5 Pro Preview | 0.2549 | — | — | — |
| 374 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-1T | 0.2549 | — | — | — |
| 375 | <img src="https://artificialanalysis.ai/img/logos/motif_small.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif-2-12.7B | 0.2544 | — | — | — |
| 376 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral 2 | 0.2531 | 0.00 | 0.0000 | ❌ |
| 377 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3.1 | 0.2528 | 1,911.88 | 0.0479 | ❌ |
| 378 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B A3B 2507 | 0.2526 | 6,147.30 | 0.2385 | ❌ |
| 379 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 8B (Reasoning) | 0.2516 | 5,382.57 | 0.2195 | ❌ |
| 380 | <img src="https://artificialanalysis.ai/img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step3 VL 10B | 0.2502 | — | — | — |
| 381 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.5 Haiku | 0.2479 | — | — | — |
| 382 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Super 49B v1.5 | 0.2477 | 1,294.59 | 0.0217 | ❌ |
| 383 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.0 Flash | 0.2472 | — | — | — |
| 384 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7-Flash (Non-reasoning) | 0.2470 | 327.43 | 0.0000 | ❌ |
| 385 | <img src="https://artificialanalysis.ai/img/logos/baidu_small.svg" width="18" alt="Baidu" /> Baidu | ERNIE 4.5 300B A47B | 0.2442 | — | — | — |
| 386 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Magistral Medium 1 | 0.2440 | — | — | — |
| 387 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.2 3B | 0.2436 | 391.57 | 0.0000 | ❌ |
| 388 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral Medium | 0.2420 | — | — | — |
| 389 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B 2507 | 0.2413 | — | — | — |
| 390 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (Non-reasoning) | 0.2408 | — | — | — |
| 391 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 4 (Non-reasoning) | 0.2406 | 478.02 | 0.0000 | ❌ |
| 392 | <img src="https://artificialanalysis.ai/img/logos/nousresearch_small.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 405B (Non-reasoning) | 0.2390 | 2,533.81 | 0.0674 | ❌ |
| 393 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder 30B A3B | 0.2379 | 1,979.89 | 0.0490 | ❌ |
| 394 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-8B-A1B | 0.2357 | — | — | — |
| 395 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 30B A3B | 0.2352 | 736.89 | 0.0000 | ❌ |
| 396 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6V (Non-reasoning) | 0.2346 | 813.03 | 0.0055 | ❌ |
| 397 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Omni 30B A3B (Reasoning) | 0.2328 | 2,609.12 | 0.0709 | ❌ |
| 398 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4 | 0.2297 | — | — | — |
| 399 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral Small 2 | 0.2296 | 0.00 | 0.0000 | ❌ |
| 400 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B | 0.2290 | 21,515.54 | 0.6217 | ❌ |
| 401 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5V | 0.2280 | 4,941.89 | 0.2081 | ❌ |
| 402 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 12B v2 VL | 0.2271 | 1,647.30 | 0.0352 | ❌ |
| 403 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Large 2 (Nov) | 0.2259 | — | — | — |
| 404 | <img src="https://artificialanalysis.ai/img/logos/tii_small.svg" width="18" alt="TII UAE" /> TII UAE | Falcon-H1R-7B | 0.2246 | — | — | — |
| 405 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Ultra | 0.2236 | — | — | — |
| 406 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 E2B | 0.2220 | — | — | — |
| 407 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Magistral Small 1.2 | 0.2195 | — | — | — |
| 408 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova Pro | 0.2147 | — | — | — |
| 409 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-2.6B | 0.2147 | 0.00 | 0.0000 | ❌ |
| 410 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3.1 32B Think | 0.2138 | — | — | — |
| 411 | <img src="https://artificialanalysis.ai/img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam 105B (high) | 0.2133 | — | — | — |
| 412 | <img src="https://artificialanalysis.ai/img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.0 32B | 0.2124 | — | — | — |
| 413 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3 (Dec) | 0.2120 | — | — | — |
| 414 | <img src="https://artificialanalysis.ai/img/logos/mbzuai_small.svg" width="18" alt="MBZUAI Institute of Foundation Models" /> MBZUAI Institute of Foundation Models | K2-V2 (low) | 0.2104 | — | — | — |
| 415 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 9B V2 | 0.2101 | 429.46 | 0.0000 | ❌ |
| 416 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Non-reasoning) | 0.2076 | 401.93 | 0.0000 | ❌ |
| 417 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-flash-2.0 | 0.2076 | — | — | — |
| 418 | <img src="https://artificialanalysis.ai/img/logos/nanbeige_small.png" width="18" alt="Nanbeige" /> Nanbeige | Nanbeige4.1-3B | 0.2066 | — | — | — |
| 419 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Super 49B v1.5 (Non-reasoning) | 0.2058 | 658.30 | 0.0000 | ❌ |
| 420 | <img src="https://artificialanalysis.ai/img/logos/nousresearch_small.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 70B | 0.2042 | — | — | — |
| 421 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral Small (May) | 0.2029 | — | — | — |
| 422 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova Lite | 0.2025 | 341.11 | 0.0000 | ❌ |
| 423 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.3 Nemotron Super 49B | 0.1994 | — | — | — |
| 424 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 32B | 0.1982 | — | — | — |
| 425 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen2.5 72B | 0.1982 | — | — | — |
| 426 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-flash-2.0 | 0.1973 | 395.45 | 0.0000 | ❌ |
| 427 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 8B | 0.1971 | 681.05 | 0.0000 | ❌ |
| 428 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 2B | 0.1961 | — | — | — |
| 429 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3.2 | 0.1961 | 257.81 | 0.0000 | ❌ |
| 430 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B | 0.1955 | 6,147.30 | 0.2385 | ❌ |
| 431 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Magistral Small 1 | 0.1953 | — | — | — |
| 432 | <img src="https://artificialanalysis.ai/img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 2 | 0.1904 | — | — | — |
| 433 | <img src="https://artificialanalysis.ai/img/logos/cohere_small.svg" width="18" alt="Cohere" /> Cohere | Command A | 0.1902 | 7,860.75 | 0.2720 | ❌ |
| 434 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 32B | 0.1900 | 1,717.84 | 0.0376 | ❌ |
| 435 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Large 2 (Jul) | 0.1898 | — | — | — |
| 436 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral Small | 0.1896 | — | — | — |
| 437 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B (Non-reasoning) | 0.1894 | 2,375.13 | 0.0559 | ❌ |
| 438 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.1 Nemotron 70B | 0.1881 | 1,924.00 | 0.0481 | ❌ |
| 439 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 4B (Reasoning) | 0.1857 | — | — | — |
| 440 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 4 Scout | 0.1854 | 532.65 | 0.0000 | ❌ |
| 441 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3 Haiku | 0.1844 | — | — | — |
| 442 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3.1 | 0.1835 | 258.07 | 0.0000 | ❌ |
| 443 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.3 Nemotron Super 49B (Non-reasoning) | 0.1829 | — | — | — |
| 444 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 14B | 0.1815 | 10,757.77 | 0.3816 | ❌ |
| 445 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B A3B 2507 (Non-reasoning) | 0.1812 | 772.15 | 0.0023 | ❌ |
| 446 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.1 70B | 0.1793 | 749.08 | 0.0004 | ❌ |
| 447 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 9B V2 (Non-reasoning) | 0.1789 | 190.63 | 0.0000 | ❌ |
| 448 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B | 0.1788 | — | — | — |
| 449 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano 4B | 0.1786 | — | — | — |
| 450 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5V (Non-reasoning) | 0.1773 | 1,606.56 | 0.0337 | ❌ |
| 451 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o mini | 0.1772 | 1,178.60 | 0.0131 | ❌ |
| 452 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 E2B (Non-reasoning) | 0.1772 | — | — | — |
| 453 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 32B (Non-reasoning) | 0.1765 | 608.92 | 0.0000 | ❌ |
| 454 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Ministral 3 14B | 0.1758 | 263.18 | 0.0000 | ❌ |
| 455 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3.1 32B Instruct | 0.1717 | — | — | — |
| 456 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Omni 30B A3B | 0.1702 | 839.06 | 0.0069 | ❌ |
| 457 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.1 30B | 0.1702 | — | — | — |
| 458 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (minimal) | 0.1695 | 349.18 | 0.0000 | ❌ |
| 459 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 nano | 0.1693 | 548.00 | 0.0000 | ❌ |
| 460 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B 2507 (Non-reasoning) | 0.1681 | — | — | — |
| 461 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 32B Think | 0.1641 | — | — | — |
| 462 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Llama 70B | 0.1637 | 3,265.54 | 0.0957 | ❌ |
| 463 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 2B (Non-reasoning) | 0.1633 | — | — | — |
| 464 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 14B | 0.1622 | — | — | — |
| 465 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi Linear 48B A3B Instruct | 0.1618 | — | — | — |
| 466 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.3 70B | 0.1614 | 7,013.59 | 0.2632 | ❌ |
| 467 | <img src="https://artificialanalysis.ai/img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 2 (Non-reasoning) | 0.1611 | — | — | — |
| 468 | <img src="https://artificialanalysis.ai/img/logos/nousresearch_small.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 70B (Non-reasoning) | 0.1581 | — | — | — |
| 469 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.1 8B | 0.1578 | 45.74 | 0.0000 | ❌ |
| 470 | <img src="https://artificialanalysis.ai/img/logos/ai21_small.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba Reasoning 3B | 0.1576 | — | — | — |
| 471 | <img src="https://artificialanalysis.ai/img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.0 32B (Non-reasoning) | 0.1555 | — | — | — |
| 472 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova Micro | 0.1528 | 209.31 | 0.0000 | ❌ |
| 473 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 24B A2B | 0.1523 | — | — | — |
| 474 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.1 8B | 0.1513 | 91.97 | 0.0000 | ❌ |
| 475 | <img src="https://artificialanalysis.ai/img/logos/ai21_small.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba 1.7 Large | 0.1512 | — | — | — |
| 476 | <img src="https://artificialanalysis.ai/img/logos/celeris.svg" width="18" alt="Celeris" /> Celeris | Celeris-1 | 0.1501 | 1,008.85 | 0.0103 | ❌ |
| 477 | <img src="https://artificialanalysis.ai/img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam 30B (high) | 0.1494 | — | — | — |
| 478 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 12B v2 VL (Non-reasoning) | 0.1478 | 544.86 | 0.0000 | ❌ |
| 479 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3 | 0.1470 | 257.94 | 0.0000 | ❌ |
| 480 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Ministral 3 8B | 0.1470 | 195.77 | 0.0000 | ❌ |
| 481 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B (Non-reasoning) | 0.1432 | 734.36 | 0.0000 | ❌ |
| 482 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano (Non-reasoning) | 0.1406 | 182.39 | 0.0000 | ❌ |
| 483 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H Small | 0.1374 | 291.41 | 0.0000 | ❌ |
| 484 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 4B | 0.1372 | — | — | — |
| 485 | <img src="https://artificialanalysis.ai/img/logos/openbmb_small.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM-V 4.6 1.3B | 0.1359 | — | — | — |
| 486 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 0528 Qwen3 8B | 0.1336 | — | — | — |
| 487 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 8B | 0.1331 | 5,382.57 | 0.2195 | ❌ |
| 488 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 14B (Non-reasoning) | 0.1314 | 1,188.27 | 0.0133 | ❌ |
| 489 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 27B | 0.1269 | — | — | — |
| 490 | <img src="https://artificialanalysis.ai/img/logos/microsoft_small.svg" width="18" alt="Microsoft" /> Microsoft | Phi-4 | 0.1269 | 393.09 | 0.0000 | ❌ |
| 491 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.1 Nemotron Nano 4B v1.1 | 0.1256 | — | — | — |
| 492 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 270M | 0.1242 | — | — | — |
| 493 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3 70B | 0.1189 | — | — | — |
| 494 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.2 11B (Vision) | 0.1186 | 432.99 | 0.0000 | ❌ |
| 495 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.2 3B | 0.1156 | — | — | — |
| 496 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 7B Think | 0.1149 | — | — | — |
| 497 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Ministral 3 3B | 0.1126 | 135.50 | 0.0000 | ❌ |
| 498 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-1.2B-Instruct | 0.1085 | — | — | — |
| 499 | <img src="https://artificialanalysis.ai/img/logos/reka_small.svg" width="18" alt="Reka AI" /> Reka AI | Reka Flash 3 | 0.1080 | — | — | — |
| 500 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 2.6B | 0.1077 | — | — | — |
| 501 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-mini-2.0 | 0.1074 | — | — | — |
| 502 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 8B (Non-reasoning) | 0.1064 | 583.21 | 0.0000 | ❌ |
| 503 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 0.8B | 0.1058 | — | — | — |
| 504 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Molmo2-8B | 0.1035 | — | — | — |
| 505 | <img src="https://artificialanalysis.ai/img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam M | 0.1030 | — | — | — |
| 506 | <img src="https://artificialanalysis.ai/img/logos/ai21_small.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba 1.7 Mini | 0.1017 | — | — | — |
| 507 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-1.2B-Thinking | 0.1003 | — | — | — |
| 508 | <img src="https://artificialanalysis.ai/img/logos/swiss-ai-initiative_small.png" width="18" alt="Swiss AI Initiative" /> Swiss AI Initiative | Apertus 70B Instruct | 0.0938 | — | — | — |
| 509 | <img src="https://artificialanalysis.ai/img/logos/microsoft_small.svg" width="18" alt="Microsoft" /> Microsoft | Phi-4 Mini | 0.0931 | 0.00 | 0.0000 | ❌ |
| 510 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 7B | 0.0922 | — | — | — |
| 511 | <img src="https://artificialanalysis.ai/img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | Exaone 4.0 1.2B | 0.0913 | — | — | — |
| 512 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H 1B | 0.0907 | — | — | — |
| 513 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | OLMo 2 32B | 0.0905 | — | — | — |
| 514 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.2 1B | 0.0898 | — | — | — |
| 515 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 1.7B | 0.0884 | — | — | — |
| 516 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 12B | 0.0865 | — | — | — |
| 517 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 0.8B (Non-reasoning) | 0.0862 | — | — | — |
| 518 | <img src="https://artificialanalysis.ai/img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | Exaone 4.0 1.2B (Non-reasoning) | 0.0843 | — | — | — |
| 519 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.1 3B | 0.0833 | — | — | — |
| 520 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 8B A1B | 0.0825 | — | — | — |
| 521 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 Micro | 0.0800 | — | — | — |
| 522 | <img src="https://artificialanalysis.ai/img/logos/microsoft_small.svg" width="18" alt="Microsoft" /> Microsoft | Phi-3 Mini | 0.0745 | — | — | — |
| 523 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 3.3 8B | 0.0716 | 252.15 | 0.0000 | ❌ |
| 524 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 4B | 0.0694 | — | — | — |
| 525 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-VL-1.6B | 0.0693 | — | — | — |
| 526 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 1B | 0.0685 | — | — | — |
| 527 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 350M | 0.0676 | — | — | — |
| 528 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 1.2B | 0.0658 | — | — | — |
| 529 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 0.6B | 0.0651 | — | — | — |
| 530 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3 8B | 0.0649 | — | — | — |
| 531 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral 7B | 0.0626 | 324.54 | 0.0000 | ❌ |
| 532 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3n E4B | 0.0623 | — | — | — |
| 533 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 1.7B (Non-reasoning) | 0.0569 | — | — | — |
| 534 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 1B | 0.0565 | — | — | — |
| 535 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | OLMo 2 7B | 0.0564 | — | — | — |
| 536 | <img src="https://artificialanalysis.ai/img/logos/swiss-ai-initiative_small.png" width="18" alt="Swiss AI Initiative" /> Swiss AI Initiative | Apertus 8B Instruct | 0.0555 | — | — | — |
| 537 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H 350M | 0.0514 | — | — | — |
| 538 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Molmo 7B-D | 0.0482 | — | — | — |
| 539 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 0.6B (Non-reasoning) | 0.0442 | — | — | — |
| 540 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3n E2B | 0.0366 | — | — | — |
| 541 | <img src="https://artificialanalysis.ai/img/logos/cohere_small.svg" width="18" alt="Cohere" /> Cohere | Tiny Aya Global | 0.0362 | — | — | — |
| 542 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 1.5B | 0.0000 | — | — | — |

## 品牌帕累托前沿连线（仅体现在图中）

以下十一个品牌在图中拥有单独的帕累托连线（较窄宽度，品牌主题色，图层高于总体灰色连线）。表中数量为**入图顶点数**——品牌前沿上低于总体前沿第一级的顶点同样不入图（本表与图例一致）：

| 品牌 | 主题色 | 品牌前沿模型数（入图） |
|------|--------|--------------|
| <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | `#cc785c` | 11 |
| <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | `#1f1f1f` | 13 |
| <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | `#0089f4` | 1 |
| <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | `#1c7ff8` | 2 |
| <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | `#34A853` | 8 |
| <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | `#736cd3` | 7 |
| <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | `#047AFE` | 5 |
| <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | `#ff7018` | 3 |
| <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | `#2243e6` | 3 |
| <img src="https://artificialanalysis.ai/img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | `#EB3568` | 3 |
| <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | `#ff6900` | 2 |

## 评分方法

1. **18项评估指标**各自线性归一化到 [0,1]
2. **综合能力值** = 所有有效归一化分数的算术平均
3. **综合能力再归一化**：线性映射到 [0,1]，性能最好的模型 = 1，最差的模型 = 0
4. **Pareto前沿** = 不被任何其他模型支配的模型（综合能力 ≥ 且成本 ≤，且至少一项严格更优；成本为 0 的免费模型同样参与——横轴左端恒为 0，免费模型是合法前沿候选）
5. **模型范围** = Status: All（含已弃用模型；缺少足够评估数据者不参与排名）
6. **图表纵轴基线（V17）**：图表的 y = 0 取总体帕累托前沿的第一级（最低能力；本例 y0 = 0.5020，即前沿左端点 Gemma 4 31B）；综合能力低于该级的模型不出现在图表中（表格不受影响）。图中纵坐标 chart_y = (能力 - y0)/(1 - y0)，因此前沿左端点恰好落在 (0, 0)、最优模型恰好为 y = 1。该过滤在横轴映射构建之前完成


## 横轴映射（分位数等密度映射，V17）与分布分析

横轴（单请求成本）按**经验分位数（rank）映射**——以 150 个入图正成本模型（综合能力 ≥ 前沿第一级）的成本分布为基准：

```
x = 0                            当 c ≤ 0（免费模型，钉在最左缘）
x = interp(log10(c); knots)      当 c > 0
```

其中 knots = (log10(c_i), 名次_i/(n-1)) 为入图正成本模型按成本排序后的 145 个锚点（等成本并列取平均名次，保证 x 是成本的单值函数；n-1 归一化使最大成本恰为 x = 1）。该映射在 **y 基线过滤之后**构建（V17：先以帕累托前沿第一级为 y = 0、剔除低性能模型，再对入图模型建映射）。

**该映射保证：**

- **函数端点严格钉死**：c = 0 → x = 0；最大成本 → x = 1——函数经过 (0,0) 与 (1,1)；
- **严格均匀密度**：x 是模型名次的线性函数，因此**任意等宽区段的模型数恒定**（每 0.1 宽度恰为 15 个模型）——无论截取哪一段，模型数 ÷ 宽度都等于全图的模型总数 ÷ 总宽度。V12 的单一 logistic 函数在过滤后的分布上做不到（十分位在 8~24 间摆动），故替换为精确分位数映射；
- 各数量级区间的入图模型数：1–10: 0，10–100: 0，100–1k: 2，1k–10k: 53，10k–100k: 79，100k–1M: 15
- **同一倍率区间的宽度 ∝ 该区间模型数**——均匀密度的必然结果：1k→10k 与 100k→1M 同为 10 倍率，但前者 53 个模型、后者 15 个，前者宽度约为后者的 3.5 倍。若改用「等倍率等距」（纯对数轴），两段的模型密度将相差 3.5 倍，与均匀密度目标冲突——两者数学上不可兼得，本图以均匀密度（最高优先级）为准；
- **左端恒为 0**（c = 0；1 个免费模型位于最左缘）
- 最低正成本 744.19 → x = 0.0000；最高成本 1,050,667 → x = 1.0000（严格 = 1）
- 中位数位置 0.497（≈ 0.5 居中）；左右两半模型数：左 76 / 右 75
- 横轴十分位模型数：16，15，16，14，15，15，15，14，16，15（严格均匀：x 为名次的线性函数，仅等成本并列的边界归属可致 ±1）
- **10^x 数量级指示**（位置 = x(10^x)）：10^0 → 0.000，10^1 → 0.000，10^2 → 0.000，10^3 → 0.010，10^4 → 0.367，10^5 → 0.896，10^6 → 0.994

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
| CacheHitRate | [AA Coding Agents](https://artificialanalysis.ai/agents/coding-agents) | 全部模型-Agent搭配的 `cacheHitRate` 求平均（68 个有效值，均值 = 0.9264），对所有模型统一使用 |
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
**模型总数（Status: All）**: 542 个参与排名（另有模型因评估数据不足未列入；总体帕累托前沿 14 个；图表入图 151 个——综合能力 ≥ 前沿第一级）  

## 图表说明（黑底）

（V17 起本说明置于文末，图表之后直接跟随模型表格。）

图表说明：**灰色实线** = 总体帕累托前沿；**彩色细线** = 十一个品牌的单独帕累托前沿（品牌主题色，图层高于总体连线；暗色品牌元素带窄白边；顶点按（横轴位置、能力升序）连接，等成本点自下而上）；品牌前沿模型圆点同样使用品牌颜色。模型名称/思考程度标注优先骑在连线之上（点的左/右两侧皆可，同一条线段可容纳两个标签——各贴各的点；文字与连线平行、中轴线重合，连线仅在文字两侧绘制）；骑线位被其他标签占据时自动「让位」——占用者挪到自己的另一个骑线位，双方都保持骑线；实在骑不上线时按四级优先依次退让（V16）：离点最近位置的上方/下方平行偏移 → 点的两条连线延长线上就近 → 两连线夹角扇区内就近。标签规则（V13/V15）：品牌前沿模型共享的前导块按「最长有效切点」剔除 —— 切点止于分界符，或止于字母且其后紧跟数字（如 Claude Opus 5 → Opus 5、GPT-5.6 Sol → 5.6 Sol、Kimi K2.6 → 2.6、Qwen3.8 Max → 3.8 Max、MiMo-V2.5 → 2.5、MiniMax-M2.1 → 2.1）；(non-reasoning) 简写为 (non)；同一模型在品牌连线上相邻出现 2 次以上时仅性能最低者保留全名、相邻较高者只标思考程度，不相邻的重复出现保留全名（每次重新计算）；标签位置与序列同向（V15）——品牌前沿上越靠右上的模型，其标签重心必须同时更靠右且更靠上（两分量都 >= 0，至少是 (0,0)，仅其一非负不算合格；初始放置违反时自动就近重摆，单标签无解（被前后邻居夹死）时按窗口级联重排整体挪动，均不产生新的重叠）。纵轴 y = 0 = 总体帕累托前沿第一级（y0 = 0.5020，前沿左端点 Gemma 4 31B 恰为 (0,0)），能力低于该级的 350 个模型与缺少成本数据的 41 个模型不出现在图中；横轴为分位数等密度映射（见上文「横轴映射」节），10^x 数量级指示位于 x(10^x)，同一倍率区间的宽度与该区间内模型数成正比。
