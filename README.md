# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

## 全部模型（综合能力从高到低，最优 = 1，最差 = 0）

共收录 **Status: All**（含已弃用）的全部模型；按重新归一化后的综合能力排序。「帕累托」列：✅ = 总体帕累托前沿模型，❌ = 被支配，— = 无成本数据无法判定。图表纵轴以总体帕累托前沿第一级（y0 = 0.6215，即前沿左端点 Ling-3.0-flash-VL）为 0：综合能力 ≥ 该级且有成本数据的 104 个模型入图，421 个能力低于第一级、18 个缺少成本数据的模型不出现在图中（本表不受影响，仍完整列出全部模型）。

| # | 品牌 | 模型 | 综合能力 | 单请求成本 | 横轴位置 | 帕累托 |
|---|------|------|---------|-----------|-----------|------|
| 1 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (max with fallback) | 1.0000 | 1,041,480.37 | 1.0000 | ✅ |
| 2 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (xhigh with fallback) | 0.9934 | 411,832.99 | 0.9706 | ✅ |
| 3 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (max) | 0.9902 | 965,212.39 | 0.9902 | ❌ |
| 4 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (xhigh) | 0.9854 | 629,850.29 | 0.9804 | ❌ |
| 5 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (high) | 0.9706 | 263,766.32 | 0.9510 | ✅ |
| 6 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5 (with fallback) | 0.9681 | 399,876.48 | 0.9608 | ❌ |
| 7 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (max) | 0.9650 | 159,848.84 | 0.8922 | ✅ |
| 8 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (high with fallback) | 0.9627 | 89,270.86 | 0.8333 | ✅ |
| 9 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (medium) | 0.9558 | 55,744.17 | 0.7647 | ✅ |
| 10 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (xhigh) | 0.9526 | 57,585.71 | 0.7745 | ❌ |
| 11 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (max) | 0.9375 | 211,191.46 | 0.9314 | ❌ |
| 12 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (high) | 0.9341 | 51,244.76 | 0.7549 | ✅ |
| 13 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (medium with fallback) | 0.9307 | 74,401.92 | 0.8137 | ❌ |
| 14 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.3 (xhigh) | 0.9238 | 12,691.41 | 0.3431 | ✅ |
| 15 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.3 (max) | 0.9232 | 12,691.41 | 0.3431 | ❌ |
| 16 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (low) | 0.9217 | 47,093.90 | 0.7059 | ❌ |
| 17 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3 (max) | 0.9004 | 41,890.27 | 0.6765 | ❌ |
| 18 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (medium) | 0.8996 | 34,239.27 | 0.6078 | ❌ |
| 19 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (low with fallback) | 0.8984 | 50,838.07 | 0.7451 | ❌ |
| 20 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (xhigh) | 0.8946 | 108,695.34 | 0.8431 | ❌ |
| 21 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (xhigh) | 0.8810 | 23,328.84 | 0.5490 | ❌ |
| 22 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (xhigh) | 0.8782 | 180,229.09 | 0.9118 | ❌ |
| 23 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.8 (max) | 0.8772 | 68,744.36 | 0.8039 | ❌ |
| 24 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (high) | 0.8758 | 65,810.16 | 0.7941 | ❌ |
| 25 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (high) | 0.8753 | 22,003.49 | 0.5294 | ❌ |
| 26 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (high) | 0.8738 | 14,512.59 | 0.4118 | ❌ |
| 27 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (medium) | 0.8694 | 19,380.36 | 0.4706 | ❌ |
| 28 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (max) | 0.8620 | 211,157.82 | 0.9216 | ❌ |
| 29 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (high) | 0.8619 | 75,077.84 | 0.8235 | ❌ |
| 30 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3 (max) | 0.8526 | 14,187.00 | 0.3922 | ❌ |
| 31 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (medium) | 0.8504 | 26,892.43 | 0.5784 | ❌ |
| 32 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.2 (xhigh) | 0.8493 | 12,691.41 | 0.3431 | ✅ |
| 33 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (high) | 0.8447 | 12,344.38 | 0.3137 | ✅ |
| 34 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (medium) | 0.8379 | — | — | — |
| 35 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (low) | 0.8339 | 24,011.27 | 0.5588 | ❌ |
| 36 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (Non-reasoning) | 0.8319 | — | — | — |
| 37 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.5 (high) | 0.8263 | 11,555.39 | 0.2941 | ✅ |
| 38 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.7 (max) | 0.8258 | 43,909.29 | 0.6863 | ❌ |
| 39 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 Max | 0.8237 | 18,401.10 | 0.4461 | ❌ |
| 40 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.1 Pro Preview | 0.8229 | 48,399.99 | 0.7255 | ❌ |
| 41 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash | 0.8210 | 39,611.02 | 0.6275 | ❌ |
| 42 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (medium) | 0.8209 | 41,782.48 | 0.6569 | ❌ |
| 43 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (max) | 0.8186 | 163,826.44 | 0.9020 | ❌ |
| 44 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.2 (max) | 0.8168 | 14,187.00 | 0.3922 | ❌ |
| 45 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (xhigh) | 0.8155 | 47,909.71 | 0.7157 | ❌ |
| 46 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (xhigh) | 0.8129 | 258,481.17 | 0.9412 | ❌ |
| 47 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (medium) | 0.8096 | 7,714.34 | 0.1961 | ✅ |
| 48 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 2.4T A95B | 0.8094 | 18,401.10 | 0.4461 | ❌ |
| 49 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.1 (xhigh) | 0.8023 | — | — | — |
| 50 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (medium) | 0.7981 | 36,973.43 | 0.6176 | ❌ |
| 51 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.3 Codex (xhigh) | 0.7977 | 120,046.31 | 0.8627 | ❌ |
| 52 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3-Flash | 0.7971 | 1,573.85 | 0.0196 | ✅ |
| 53 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (low) | 0.7939 | 19,775.32 | 0.4804 | ❌ |
| 54 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.7 Max | 0.7908 | 27,847.33 | 0.5882 | ❌ |
| 55 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.6 Flash | 0.7846 | 16,003.33 | 0.4216 | ❌ |
| 56 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (high) | 0.7765 | 14,398.84 | 0.4020 | ❌ |
| 57 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (max) | 0.7620 | 20,591.86 | 0.4902 | ❌ |
| 58 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (low) | 0.7617 | 3,654.32 | 0.0686 | ❌ |
| 59 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (low) | 0.7567 | — | — | — |
| 60 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.6 (max) | 0.7548 | 45,664.99 | 0.6961 | ❌ |
| 61 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8-Flash-Next | 0.7543 | 1,404.00 | 0.0098 | ✅ |
| 62 | <img src="https://artificialanalysis.ai/img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M3 | 0.7512 | 3,762.20 | 0.1176 | ❌ |
| 63 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 v2 | 0.7505 | 10,241.48 | 0.2451 | ❌ |
| 64 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark | 0.7418 | — | — | — |
| 65 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.6 | 0.7412 | 21,810.78 | 0.5098 | ❌ |
| 66 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3 Pro Preview (high) | 0.7393 | — | — | — |
| 67 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (low) | 0.7365 | 10,869.54 | 0.2549 | ❌ |
| 68 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (medium) | 0.7362 | 7,200.81 | 0.1765 | ❌ |
| 69 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (xhigh) | 0.7358 | 28,485.95 | 0.5980 | ❌ |
| 70 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro 0813 (max) | 0.7343 | 10,997.03 | 0.2745 | ❌ |
| 71 | <img src="https://artificialanalysis.ai/img/logos/sapiens.svg" width="18" alt="Sapiens AI" /> Sapiens AI | Agnes 2.5 Pro Beta | 0.7290 | — | — | — |
| 72 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (xhigh) | 0.7282 | 8,443.88 | 0.2157 | ❌ |
| 73 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (xhigh) | 0.7262 | 141,737.23 | 0.8824 | ❌ |
| 74 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 Codex (xhigh) | 0.7255 | — | — | — |
| 75 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 Max Preview | 0.7240 | 21,569.80 | 0.5000 | ❌ |
| 76 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (low) | 0.7230 | 25,912.16 | 0.5686 | ❌ |
| 77 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash (max) | 0.7217 | 3,211.38 | 0.0490 | ❌ |
| 78 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (high) | 0.7183 | 9,969.71 | 0.2353 | ❌ |
| 79 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (max) | 0.7162 | 115,421.83 | 0.8529 | ❌ |
| 80 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3 Flash | 0.7142 | 5,511.25 | 0.1667 | ❌ |
| 81 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.5 | 0.7106 | 39,984.92 | 0.6373 | ❌ |
| 82 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 | 0.7103 | — | — | — |
| 83 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.7 (Non-reasoning, high) | 0.7061 | 22,054.50 | 0.5392 | ❌ |
| 84 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (medium) | 0.7046 | 11,197.00 | 0.2843 | ❌ |
| 85 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.7 Plus | 0.7042 | 4,636.86 | 0.1471 | ❌ |
| 86 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 Plus | 0.7013 | 18,946.08 | 0.4608 | ❌ |
| 87 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (max) | 0.7012 | 4,499.38 | 0.1373 | ❌ |
| 88 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (high) | 0.6974 | 3,406.51 | 0.0588 | ❌ |
| 89 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.1 | 0.6955 | 21,964.42 | 0.5196 | ❌ |
| 90 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (xhigh) | 0.6912 | 8,231.71 | 0.2059 | ❌ |
| 91 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash Vision (max) | 0.6902 | 3,659.35 | 0.0882 | ❌ |
| 92 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash 0731 (max) | 0.6894 | 3,659.35 | 0.0784 | ❌ |
| 93 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (low) | 0.6876 | 13,492.98 | 0.3627 | ❌ |
| 94 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 (high) | 0.6798 | 49,214.33 | 0.7353 | ❌ |
| 95 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (low) | 0.6781 | 5,307.80 | 0.1569 | ❌ |
| 96 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Pro | 0.6764 | — | — | — |
| 97 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (high) | 0.6728 | 2,426.17 | 0.0294 | ❌ |
| 98 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5-Pro | 0.6727 | 2,433.13 | 0.0392 | ❌ |
| 99 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (xhigh) | 0.6708 | 134,341.49 | 0.8725 | ❌ |
| 100 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (medium) | 0.6707 | — | — | — |
| 101 | <img src="https://artificialanalysis.ai/img/logos/motif_small.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif 3 | 0.6690 | — | — | — |
| 102 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.7 Code | 0.6663 | 13,207.33 | 0.3529 | ❌ |
| 103 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (high) | 0.6618 | 16,269.62 | 0.4314 | ❌ |
| 104 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3 (low) | 0.6606 | 41,890.27 | 0.6765 | ❌ |
| 105 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 Codex (high) | 0.6571 | — | — | — |
| 106 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok Build 0.1 0616 | 0.6569 | 7,411.93 | 0.1863 | ❌ |
| 107 | <img src="https://artificialanalysis.ai/img/logos/mbzuai_small.svg" width="18" alt="MBZUAI Institute of Foundation Models" /> MBZUAI Institute of Foundation Models | K2 Horizon 375B A23B | 0.6550 | — | — | — |
| 108 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5 | 0.6520 | 13,947.93 | 0.3725 | ❌ |
| 109 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Ultra | 0.6518 | 9,420.97 | 0.2255 | ❌ |
| 110 | <img src="https://artificialanalysis.ai/img/logos/thinking_machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling Small | 0.6491 | 3,723.58 | 0.1029 | ❌ |
| 111 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5 | 0.6487 | 798.65 | 0.0000 | ✅ |
| 112 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (low) | 0.6460 | 10,896.45 | 0.2647 | ❌ |
| 113 | <img src="https://artificialanalysis.ai/img/logos/thinking_machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling | 0.6434 | 12,252.38 | 0.3039 | ❌ |
| 114 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 Codex (high) | 0.6387 | — | — | — |
| 115 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (high) | 0.6329 | 62,703.78 | 0.7843 | ❌ |
| 116 | <img src="https://artificialanalysis.ai/img/logos/apodex.svg" width="18" alt="Apodex" /> Apodex | Apodex 1.1 | 0.6322 | — | — | — |
| 117 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (max) | 0.6310 | — | — | — |
| 118 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Omni-0327 | 0.6288 | — | — | — |
| 119 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (medium) | 0.6266 | 40,467.40 | 0.6471 | ❌ |
| 120 | <img src="https://artificialanalysis.ai/img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 4 | 0.6242 | 3,723.58 | 0.1029 | ❌ |
| 121 | <img src="https://artificialanalysis.ai/img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.7 | 0.6219 | 4,316.60 | 0.1275 | ❌ |
| 122 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-3.0-flash-VL | 0.6215 | 0.00 | 0.0000 | ✅ |
| 123 | <img src="https://artificialanalysis.ai/img/logos/nex_small.svg" width="18" alt="Nex AGI" /> Nex AGI | Nex-N2-Pro | 0.6211 | 8,878.73 | 0.2202 | ❌ |
| 124 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.6 (Non-reasoning, high) | 0.6196 | 22,601.03 | 0.5435 | ❌ |
| 125 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5-Turbo | 0.6192 | — | — | — |
| 126 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.5 | 0.6174 | — | — | — |
| 127 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 | 0.6172 | — | — | — |
| 128 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 27B | 0.6139 | 22,542.55 | 0.5430 | ❌ |
| 129 | <img src="https://artificialanalysis.ai/img/logos/motif_small.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif 3 (Beta) | 0.6083 | — | — | — |
| 130 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 Instant (May 2026) | 0.6079 | — | — | — |
| 131 | <img src="https://artificialanalysis.ai/img/logos/multiversecomputing_small.svg" width="18" alt="Multiverse Computing" /> Multiverse Computing | Quasar 438B (max) | 0.6062 | 4,808.95 | 0.1497 | ❌ |
| 132 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Opus | 0.6052 | — | — | — |
| 133 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (xhigh) | 0.6037 | 18,122.20 | 0.4443 | ❌ |
| 134 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (high) | 0.6025 | — | — | — |
| 135 | <img src="https://artificialanalysis.ai/img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Open2 250B | 0.6021 | — | — | — |
| 136 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 397B A17B | 0.5995 | 13,578.55 | 0.3646 | ❌ |
| 137 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash-Lite | 0.5985 | 8,650.46 | 0.2179 | ❌ |
| 138 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Sonnet | 0.5978 | 23,082.51 | 0.5472 | ❌ |
| 139 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (minimal) | 0.5976 | 8,305.79 | 0.2093 | ❌ |
| 140 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 27B | 0.5961 | 6,154.47 | 0.1707 | ❌ |
| 141 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash (Feb 2026) | 0.5958 | — | — | — |
| 142 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (medium) | 0.5952 | 1,368.26 | 0.0094 | ❌ |
| 143 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (Non-reasoning) | 0.5951 | 8,889.36 | 0.2203 | ❌ |
| 144 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Omni | 0.5942 | — | — | — |
| 145 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o3 | 0.5929 | 16,452.98 | 0.4327 | ❌ |
| 146 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM 5V Turbo | 0.5896 | — | — | — |
| 147 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (medium) | 0.5865 | 9,262.32 | 0.2240 | ❌ |
| 148 | <img src="https://artificialanalysis.ai/img/logos/tencent_small.svg" width="18" alt="Tencent" /> Tencent | Hy3 | 0.5859 | 1,777.52 | 0.0224 | ❌ |
| 149 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (medium) | 0.5835 | 4,349.54 | 0.1292 | ❌ |
| 150 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.1 Opus | 0.5813 | — | — | — |
| 151 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (Non-reasoning, high) | 0.5800 | 13,847.01 | 0.3704 | ❌ |
| 152 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 35B A3B | 0.5797 | 13,456.84 | 0.3615 | ❌ |
| 153 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 Thinking | 0.5790 | 6,558.95 | 0.1730 | ❌ |
| 154 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.5 (Non-reasoning) | 0.5773 | 21,933.26 | 0.5176 | ❌ |
| 155 | <img src="https://artificialanalysis.ai/img/logos/sktelecom_small.svg" width="18" alt="SK Telecom" /> SK Telecom | A.X-K2 | 0.5766 | — | — | — |
| 156 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (Non-reasoning, low) | 0.5742 | 13,556.18 | 0.3641 | ❌ |
| 157 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (Non-reasoning) | 0.5729 | 17,883.96 | 0.4427 | ❌ |
| 158 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.6 (Non-reasoning) | 0.5721 | 4,511.31 | 0.1381 | ❌ |
| 159 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3 Pro Preview (low) | 0.5716 | — | — | — |
| 160 | <img src="https://artificialanalysis.ai/img/logos/sapiens.svg" width="18" alt="Sapiens AI" /> Sapiens AI | Agnes 2.5 Pro Alpha | 0.5663 | 2,576.56 | 0.0412 | ❌ |
| 161 | <img src="https://artificialanalysis.ai/img/logos/kwaikat_small.svg" width="18" alt="KwaiKAT" /> KwaiKAT | KAT-Coder-Pro V2 | 0.5623 | — | — | — |
| 162 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 Codex mini (high) | 0.5622 | — | — | — |
| 163 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (high) | 0.5609 | 17,012.96 | 0.4367 | ❌ |
| 164 | <img src="https://artificialanalysis.ai/img/logos/china_mobile_small.png" width="18" alt="China Mobile" /> China Mobile | JT-4.1 Flash 236B A21B | 0.5593 | — | — | — |
| 165 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (low) | 0.5591 | 13,867.47 | 0.3708 | ❌ |
| 166 | <img src="https://artificialanalysis.ai/img/logos/tencent_small.svg" width="18" alt="Tencent" /> Tencent | Hy3-preview | 0.5587 | — | — | — |
| 167 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 122B A10B | 0.5585 | 8,205.97 | 0.2054 | ❌ |
| 168 | <img src="https://artificialanalysis.ai/img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step 3.7 Flash | 0.5556 | 3,357.39 | 0.0564 | ❌ |
| 169 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (low) | 0.5550 | 8,231.71 | 0.2059 | ❌ |
| 170 | <img src="https://artificialanalysis.ai/img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.5 | 0.5528 | 3,477.65 | 0.0617 | ❌ |
| 171 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.1 (Non-reasoning) | 0.5526 | 5,716.05 | 0.1680 | ❌ |
| 172 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (Non-reasoning) | 0.5525 | 24,616.74 | 0.5620 | ❌ |
| 173 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7 | 0.5519 | 11,500.00 | 0.2926 | ❌ |
| 174 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 Omni Plus | 0.5514 | 3,516.73 | 0.0633 | ❌ |
| 175 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (low) | 0.5459 | 1,129.47 | 0.0060 | ❌ |
| 176 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.1 Fast | 0.5445 | — | — | — |
| 177 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (medium) | 0.5411 | 8,231.71 | 0.2059 | ❌ |
| 178 | <img src="https://artificialanalysis.ai/img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | G9v3-39A5B | 0.5390 | — | — | — |
| 179 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano | 0.5384 | 2,244.75 | 0.0277 | ❌ |
| 180 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max Thinking | 0.5378 | — | — | — |
| 181 | <img src="https://artificialanalysis.ai/img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.1 | 0.5376 | 3,154.47 | 0.0484 | ❌ |
| 182 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B | 0.5347 | 2,773.93 | 0.0438 | ❌ |
| 183 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 31B | 0.5331 | 0.00 | 0.0000 | ❌ |
| 184 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 Instant (June 2026) | 0.5318 | 82,317.11 | 0.8287 | ❌ |
| 185 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 35B A3B | 0.5318 | 5,128.73 | 0.1544 | ❌ |
| 186 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Sonnet | 0.5295 | — | — | — |
| 187 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.0 Flash | 0.5290 | 730.89 | 0.0000 | ❌ |
| 188 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.5 (Non-reasoning) | 0.5267 | — | — | — |
| 189 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 | 0.5264 | — | — | — |
| 190 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash | 0.5254 | — | — | — |
| 191 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (medium) | 0.5247 | 8,179.65 | 0.2049 | ❌ |
| 192 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3 Flash (Non-reasoning) | 0.5198 | 2,725.89 | 0.0432 | ❌ |
| 193 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (low) | 0.5196 | 9,224.10 | 0.2236 | ❌ |
| 194 | <img src="https://artificialanalysis.ai/img/logos/cohere_small.svg" width="18" alt="Cohere" /> Cohere | Command A+ | 0.5180 | 0.00 | 0.0000 | ❌ |
| 195 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5 (Non-reasoning) | 0.5152 | 4,282.01 | 0.1269 | ❌ |
| 196 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Glimmer (high) | 0.5150 | 4,309.62 | 0.1273 | ❌ |
| 197 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3.5 | 0.5123 | 20,945.13 | 0.4938 | ❌ |
| 198 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 397B A17B (Non-reasoning) | 0.5090 | 2,675.23 | 0.0426 | ❌ |
| 199 | <img src="https://artificialanalysis.ai/img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step 3.5 Flash 2603 | 0.5080 | 991.19 | 0.0038 | ❌ |
| 200 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Haiku | 0.5060 | 11,489.24 | 0.2923 | ❌ |
| 201 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Pro | 0.5057 | 34,617.06 | 0.6092 | ❌ |
| 202 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 Fast | 0.5021 | — | — | — |
| 203 | <img src="https://artificialanalysis.ai/img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE 2.0 | 0.4998 | — | — | — |
| 204 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-2.6-1T | 0.4990 | 6,404.47 | 0.1722 | ❌ |
| 205 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 3 mini Reasoning (high) | 0.4939 | 2,115.86 | 0.0263 | ❌ |
| 206 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 27B (Non-reasoning) | 0.4936 | 2,435.64 | 0.0393 | ❌ |
| 207 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Sonnet (Non-reasoning) | 0.4933 | 13,149.52 | 0.3519 | ❌ |
| 208 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Speciale | 0.4923 | — | — | — |
| 209 | <img src="https://artificialanalysis.ai/img/logos/china_mobile_small.png" width="18" alt="China Mobile" /> China Mobile | JT-35B-Flash | 0.4906 | — | — | — |
| 210 | <img src="https://artificialanalysis.ai/img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step 3.5 Flash | 0.4901 | 801.49 | 0.0001 | ❌ |
| 211 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.1 Flash-Lite | 0.4887 | 3,662.44 | 0.0889 | ❌ |
| 212 | <img src="https://artificialanalysis.ai/img/logos/longcat_small.svg" width="18" alt="LongCat" /> LongCat | LongCat 2.0 | 0.4786 | — | — | — |
| 213 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 27B (Non-reasoning) | 0.4784 | 2,819.23 | 0.0444 | ❌ |
| 214 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (Non-reasoning) | 0.4783 | 12,470.38 | 0.3173 | ❌ |
| 215 | <img src="https://artificialanalysis.ai/img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2 | 0.4773 | 3,154.47 | 0.0484 | ❌ |
| 216 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.2 (Non-reasoning) | 0.4760 | 6,346.68 | 0.1718 | ❌ |
| 217 | <img src="https://artificialanalysis.ai/img/logos/bytedance_small.svg" width="18" alt="ByteDance Seed" /> ByteDance Seed | Doubao Seed Code | 0.4744 | — | — | — |
| 218 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o4-mini (high) | 0.4742 | 19,333.58 | 0.4695 | ❌ |
| 219 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o1 | 0.4731 | — | — | — |
| 220 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (Non-reasoning) | 0.4651 | 10,066.97 | 0.2388 | ❌ |
| 221 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (Non-reasoning) | 0.4628 | 790.90 | 0.0000 | ❌ |
| 222 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (Non-reasoning) | 0.4622 | 10,405.75 | 0.2477 | ❌ |
| 223 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (medium) | 0.4607 | 28,602.99 | 0.5983 | ❌ |
| 224 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 122B A10B (Non-reasoning) | 0.4590 | 2,825.51 | 0.0445 | ❌ |
| 225 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.7 Sonnet | 0.4589 | — | — | — |
| 226 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 9B | 0.4561 | 569.51 | 0.0000 | ❌ |
| 227 | <img src="https://artificialanalysis.ai/img/logos/kwaikat_small.svg" width="18" alt="KwaiKAT" /> KwaiKAT | KAT-Coder-Pro V1 | 0.4561 | — | — | — |
| 228 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Sonnet (Non-reasoning) | 0.4555 | — | — | — |
| 229 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (low) | 0.4534 | 25,643.64 | 0.5673 | ❌ |
| 230 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Sep) | 0.4501 | — | — | — |
| 231 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 Terminus | 0.4486 | — | — | — |
| 232 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Exp | 0.4454 | — | — | — |
| 233 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.7 Sonnet (Non-reasoning) | 0.4349 | — | — | — |
| 234 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max Thinking (Preview) | 0.4338 | 15,617.90 | 0.4191 | ❌ |
| 235 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 4B | 0.4323 | 390.45 | 0.0000 | ❌ |
| 236 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 35B A3B (Non-reasoning) | 0.4313 | 1,916.44 | 0.0241 | ❌ |
| 237 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 26B A4B | 0.4291 | — | — | — |
| 238 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash | 0.4288 | 10,088.57 | 0.2396 | ❌ |
| 239 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (medium) | 0.4279 | 6,404.47 | 0.1722 | ❌ |
| 240 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5-Pro (Non-reasoning) | 0.4241 | 839.96 | 0.0009 | ❌ |
| 241 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Haiku (Non-reasoning) | 0.4236 | 4,393.75 | 0.1316 | ❌ |
| 242 | <img src="https://artificialanalysis.ai/img/logos/baidu_small.svg" width="18" alt="Baidu" /> Baidu | ERNIE 5.0 Thinking Preview | 0.4205 | — | — | — |
| 243 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 0905 | 0.4203 | 1,677.81 | 0.0211 | ❌ |
| 244 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (Non-reasoning) | 0.4195 | — | — | — |
| 245 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 235B A22B (Reasoning) | 0.4193 | 10,205.97 | 0.2438 | ❌ |
| 246 | <img src="https://artificialanalysis.ai/img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.5 33B | 0.4182 | — | — | — |
| 247 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 (Non-reasoning) | 0.4178 | — | — | — |
| 248 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-2.6-1T | 0.4163 | — | — | — |
| 249 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (low) | 0.4119 | — | — | — |
| 250 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (Non-reasoning) | 0.4114 | 3,983.70 | 0.1217 | ❌ |
| 251 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 (Non-reasoning) | 0.4106 | — | — | — |
| 252 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (high) | 0.4099 | 6,404.47 | 0.1722 | ❌ |
| 253 | <img src="https://artificialanalysis.ai/img/logos/tencent_small.svg" width="18" alt="Tencent" /> Tencent | Hy3-preview (Non-reasoning) | 0.4088 | — | — | — |
| 254 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (high) | 0.4088 | 7,023.95 | 0.1756 | ❌ |
| 255 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 31B (Non-reasoning) | 0.4087 | 1,632.15 | 0.0204 | ❌ |
| 256 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (medium) | 0.4066 | 2,812.24 | 0.0443 | ❌ |
| 257 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7 (Non-reasoning) | 0.4057 | 6,645.92 | 0.1735 | ❌ |
| 258 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6 | 0.4054 | 11,000.00 | 0.2747 | ❌ |
| 259 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 12B | 0.4046 | 801.49 | 0.0001 | ❌ |
| 260 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (medium) | 0.4042 | — | — | — |
| 261 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 v2 (Non-reasoning) | 0.4019 | 3,931.32 | 0.1208 | ❌ |
| 262 | <img src="https://artificialanalysis.ai/img/logos/inceptionlabs_small.svg" width="18" alt="Inception" /> Inception | Mercury 2 | 0.4019 | 2,753.85 | 0.0436 | ❌ |
| 263 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 35B A3B (Non-reasoning) | 0.4009 | 1,787.52 | 0.0225 | ❌ |
| 264 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 | 0.3972 | — | — | — |
| 265 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5 | 0.3964 | — | — | — |
| 266 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3.5 Lightning | 0.3962 | 1,005.15 | 0.0040 | ❌ |
| 267 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Super | 0.3937 | 1,724.12 | 0.0217 | ❌ |
| 268 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.2 30B | 0.3937 | 2,086.79 | 0.0260 | ❌ |
| 269 | <img src="https://artificialanalysis.ai/img/logos/arcee_small.svg" width="18" alt="Arcee AI" /> Arcee AI | Trinity Large Thinking | 0.3937 | 2,378.73 | 0.0290 | ❌ |
| 270 | <img src="https://artificialanalysis.ai/img/logos/openbmb_small.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-2B | 0.3914 | — | — | — |
| 271 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max | 0.3908 | 4,285.80 | 0.1269 | ❌ |
| 272 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (Non-reasoning) | 0.3888 | 1,042.06 | 0.0046 | ❌ |
| 273 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok Code Fast 1 | 0.3876 | — | — | — |
| 274 | <img src="https://artificialanalysis.ai/img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE | 0.3873 | — | — | — |
| 275 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 | 0.3864 | 1,598.03 | 0.0200 | ❌ |
| 276 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 0528 | 0.3856 | — | — | — |
| 277 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 4 | 0.3809 | 1,577.24 | 0.0197 | ❌ |
| 278 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Sep) (Non-reasoning) | 0.3799 | — | — | — |
| 279 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B A22B 2507 | 0.3774 | 5,868.43 | 0.1690 | ❌ |
| 280 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (minimal) | 0.3770 | 7,811.54 | 0.1980 | ❌ |
| 281 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 32B (Reasoning) | 0.3759 | 1,682.39 | 0.0211 | ❌ |
| 282 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Magistral Medium 1.2 | 0.3754 | — | — | — |
| 283 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 | 0.3748 | 11,174.66 | 0.2832 | ❌ |
| 284 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 (Non-reasoning) | 0.3735 | 7,947.45 | 0.2006 | ❌ |
| 285 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (low) | 0.3725 | 6,404.47 | 0.1722 | ❌ |
| 286 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 9B (Non-reasoning) | 0.3719 | 231.26 | 0.0000 | ❌ |
| 287 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7-Flash | 0.3715 | 1,700.00 | 0.0214 | ❌ |
| 288 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6 (Non-reasoning) | 0.3683 | 1,721.72 | 0.0216 | ❌ |
| 289 | <img src="https://artificialanalysis.ai/img/logos/servicenow_small.svg" width="18" alt="ServiceNow" /> ServiceNow | Apriel-v1.5-15B-Thinker | 0.3649 | — | — | — |
| 290 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-120b (high) | 0.3629 | 2,750.37 | 0.0435 | ❌ |
| 291 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.0 Tiny | 0.3628 | 0.00 | 0.0000 | ❌ |
| 292 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 Omni Flash | 0.3604 | 774.29 | 0.0000 | ❌ |
| 293 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder 480B | 0.3591 | 5,680.26 | 0.1678 | ❌ |
| 294 | <img src="https://artificialanalysis.ai/img/logos/multiversecomputing_small.svg" width="18" alt="Multiverse Computing" /> Multiverse Computing | HyperNova 60B 2605 (high) | 0.3589 | 370.60 | 0.0000 | ❌ |
| 295 | <img src="https://artificialanalysis.ai/img/logos/deepcogito_small.png" width="18" alt="Deep Cogito" /> Deep Cogito | Cogito v2.1 | 0.3584 | — | — | — |
| 296 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Sep) | 0.3581 | — | — | — |
| 297 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron Cascade 2 30B A3B | 0.3578 | — | — | — |
| 298 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash (Non-reasoning) | 0.3558 | — | — | — |
| 299 | <img src="https://artificialanalysis.ai/img/logos/servicenow_small.svg" width="18" alt="ServiceNow" /> ServiceNow | Apriel-v1.6-15B-Thinker | 0.3541 | — | — | — |
| 300 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 26B A4B (Non-reasoning) | 0.3534 | 1,499.10 | 0.0154 | ❌ |
| 301 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 3 | 0.3521 | — | — | — |
| 302 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6V | 0.3519 | 2,404.47 | 0.0292 | ❌ |
| 303 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 Terminus (Non-reasoning) | 0.3511 | — | — | — |
| 304 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.2 8B | 0.3467 | 798.17 | 0.0000 | ❌ |
| 305 | <img src="https://artificialanalysis.ai/img/logos/cohere_small.svg" width="18" alt="Cohere" /> Cohere | North Mini Code | 0.3457 | 0.00 | 0.0000 | ❌ |
| 306 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (ChatGPT) | 0.3456 | — | — | — |
| 307 | <img src="https://artificialanalysis.ai/img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | G9v3-3B | 0.3417 | — | — | — |
| 308 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o3-mini (high) | 0.3405 | 29,382.18 | 0.5997 | ❌ |
| 309 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max (Preview) | 0.3397 | 5,049.52 | 0.1532 | ❌ |
| 310 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Exp (Non-reasoning) | 0.3334 | — | — | — |
| 311 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Sep) (Non-reasoning) | 0.3307 | — | — | — |
| 312 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 (Non-reasoning) | 0.3302 | — | — | — |
| 313 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Next 80B A3B (Reasoning) | 0.3284 | 3,077.24 | 0.0475 | ❌ |
| 314 | <img src="https://artificialanalysis.ai/img/logos/bytedance_small.svg" width="18" alt="ByteDance Seed" /> ByteDance Seed | Seed-OSS-36B-Instruct | 0.3261 | 1,533.13 | 0.0174 | ❌ |
| 315 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder Next | 0.3238 | 4,262.81 | 0.1266 | ❌ |
| 316 | <img src="https://artificialanalysis.ai/img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 3 | 0.3235 | 1,719.51 | 0.0216 | ❌ |
| 317 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o (Nov) | 0.3221 | 21,878.05 | 0.5141 | ❌ |
| 318 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Non-reasoning) | 0.3206 | 1,897.85 | 0.0238 | ❌ |
| 319 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano | 0.3195 | 525.75 | 0.0000 | ❌ |
| 320 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 4B (Non-reasoning) | 0.3191 | 92.69 | 0.0000 | ❌ |
| 321 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B 2507 (Non-reasoning) | 0.3189 | 705.70 | 0.0000 | ❌ |
| 322 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o (Aug) | 0.3189 | 19,402.34 | 0.4711 | ❌ |
| 323 | <img src="https://artificialanalysis.ai/img/logos/mbzuai_small.svg" width="18" alt="MBZUAI Institute of Foundation Models" /> MBZUAI Institute of Foundation Models | K2 Think V2 | 0.3179 | — | — | — |
| 324 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite | 0.3160 | 3,313.71 | 0.0542 | ❌ |
| 325 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.1 Fast (Non-reasoning) | 0.3123 | — | — | — |
| 326 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (minimal) | 0.3115 | 1,559.86 | 0.0188 | ❌ |
| 327 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 12B (Non-reasoning) | 0.3102 | 274.56 | 0.0000 | ❌ |
| 328 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 235B A22B | 0.3098 | 1,221.70 | 0.0074 | ❌ |
| 329 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | QwQ-32B | 0.3069 | — | — | — |
| 330 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-1T | 0.3067 | — | — | — |
| 331 | <img src="https://artificialanalysis.ai/img/logos/openbmb_small.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-1B | 0.3065 | — | — | — |
| 332 | <img src="https://artificialanalysis.ai/img/logos/openbmb_small.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-1B (Non-reasoning) | 0.3065 | — | — | — |
| 333 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Pixtral Large | 0.3041 | — | — | — |
| 334 | <img src="https://artificialanalysis.ai/img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Open 100B | 0.3018 | — | — | — |
| 335 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3 0324 | 0.3008 | — | — | — |
| 336 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Large 3 | 0.3008 | 1,123.78 | 0.0059 | ❌ |
| 337 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o3-mini | 0.2995 | 13,954.01 | 0.3728 | ❌ |
| 338 | <img src="https://artificialanalysis.ai/img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax M1 80k | 0.2984 | — | — | — |
| 339 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5-Air | 0.2981 | 2,537.54 | 0.0407 | ❌ |
| 340 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (Non-reasoning) | 0.2978 | 3,828.84 | 0.1189 | ❌ |
| 341 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 E4B | 0.2976 | 260.30 | 0.0000 | ❌ |
| 342 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (Non-reasoning) | 0.2960 | 6,665.02 | 0.1736 | ❌ |
| 343 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 (Jan) | 0.2957 | — | — | — |
| 344 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 4 Maverick | 0.2939 | 2,981.40 | 0.0464 | ❌ |
| 345 | <img src="https://artificialanalysis.ai/img/logos/china_mobile_small.png" width="18" alt="China Mobile" /> China Mobile | JT-MINI | 0.2935 | — | — | — |
| 346 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | DiffusionGemma 26B A4B | 0.2934 | — | — | — |
| 347 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 2.6 Flash | 0.2926 | — | — | — |
| 348 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3 | 0.2919 | 1,821.73 | 0.0229 | ❌ |
| 349 | <img src="https://artificialanalysis.ai/img/logos/naver_small.webp" width="18" alt="Naver" /> Naver | HyperCLOVA X SEED Think (32B) | 0.2910 | — | — | — |
| 350 | <img src="https://artificialanalysis.ai/img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax M1 40k | 0.2908 | — | — | — |
| 351 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 Fast (Non-reasoning) | 0.2897 | — | — | — |
| 352 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-20b (high) | 0.2890 | 505.89 | 0.0000 | ❌ |
| 353 | <img src="https://artificialanalysis.ai/img/logos/mbzuai_small.svg" width="18" alt="MBZUAI Institute of Foundation Models" /> MBZUAI Institute of Foundation Models | K2-V2 (high) | 0.2888 | — | — | — |
| 354 | <img src="https://artificialanalysis.ai/img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE (Non-reasoning) | 0.2884 | — | — | — |
| 355 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 mini | 0.2875 | 2,114.35 | 0.0263 | ❌ |
| 356 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B A3B 2507 | 0.2859 | 6,102.98 | 0.1704 | ❌ |
| 357 | <img src="https://artificialanalysis.ai/img/logos/korea-telecom_small.png" width="18" alt="Korea Telecom" /> Korea Telecom | Mi:dm K 2.5 Pro | 0.2859 | — | — | — |
| 358 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (Non-reasoning) | 0.2845 | 1,087.79 | 0.0054 | ❌ |
| 359 | <img src="https://artificialanalysis.ai/img/logos/prime-intellect_small.svg" width="18" alt="Prime Intellect" /> Prime Intellect | INTELLECT-3 | 0.2795 | — | — | — |
| 360 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano Omni 30B A3B | 0.2787 | — | — | — |
| 361 | <img src="https://artificialanalysis.ai/img/logos/trillionlabs_small.svg" width="18" alt="Trillion Labs" /> Trillion Labs | Tri-21B-think Preview | 0.2778 | — | — | — |
| 362 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 30B A3B (Reasoning) | 0.2769 | 6,102.98 | 0.1704 | ❌ |
| 363 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-120b (low) | 0.2769 | 2,862.50 | 0.0450 | ❌ |
| 364 | <img src="https://artificialanalysis.ai/img/logos/longcat_small.svg" width="18" alt="LongCat" /> LongCat | LongCat Flash Lite | 0.2764 | — | — | — |
| 365 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.2 3B | 0.2762 | 386.59 | 0.0000 | ❌ |
| 366 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-20b (low) | 0.2756 | 536.04 | 0.0000 | ❌ |
| 367 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.1 405B | 0.2745 | — | — | — |
| 368 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3.1 | 0.2740 | 1,773.42 | 0.0223 | ❌ |
| 369 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova Premier | 0.2737 | 14,542.80 | 0.4120 | ❌ |
| 370 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 E4B (Non-reasoning) | 0.2727 | 63.58 | 0.0000 | ❌ |
| 371 | <img src="https://artificialanalysis.ai/img/logos/trillionlabs_small.svg" width="18" alt="Trillion Labs" /> Trillion Labs | Tri-21B-Think | 0.2720 | — | — | — |
| 372 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (Non-reasoning) | 0.2652 | 1,801.70 | 0.0227 | ❌ |
| 373 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 32B | 0.2646 | 513.74 | 0.0000 | ❌ |
| 374 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Next 80B A3B | 0.2644 | 1,129.00 | 0.0060 | ❌ |
| 375 | <img src="https://artificialanalysis.ai/img/logos/nousresearch_small.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 405B | 0.2627 | 8,014.91 | 0.2019 | ❌ |
| 376 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral 2 | 0.2603 | 0.00 | 0.0000 | ❌ |
| 377 | <img src="https://artificialanalysis.ai/img/logos/mbzuai_small.svg" width="18" alt="MBZUAI Institute of Foundation Models" /> MBZUAI Institute of Foundation Models | K2-V2 (medium) | 0.2599 | — | — | — |
| 378 | <img src="https://artificialanalysis.ai/img/logos/korea-telecom_small.png" width="18" alt="Korea Telecom" /> Korea Telecom | Mi:dm K 2.5 Pro Preview | 0.2591 | — | — | — |
| 379 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-1T | 0.2591 | — | — | — |
| 380 | <img src="https://artificialanalysis.ai/img/logos/motif_small.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif-2-12.7B | 0.2586 | — | — | — |
| 381 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.5 Haiku | 0.2564 | — | — | — |
| 382 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 8B (Reasoning) | 0.2557 | 5,342.68 | 0.1586 | ❌ |
| 383 | <img src="https://artificialanalysis.ai/img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step3 VL 10B | 0.2543 | — | — | — |
| 384 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Super 49B v1.5 | 0.2518 | 1,205.97 | 0.0072 | ❌ |
| 385 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.0 Flash | 0.2513 | — | — | — |
| 386 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7-Flash (Non-reasoning) | 0.2511 | 304.65 | 0.0000 | ❌ |
| 387 | <img src="https://artificialanalysis.ai/img/logos/baidu_small.svg" width="18" alt="Baidu" /> Baidu | ERNIE 4.5 300B A47B | 0.2483 | — | — | — |
| 388 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Magistral Medium 1 | 0.2481 | — | — | — |
| 389 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral Medium | 0.2460 | — | — | — |
| 390 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B 2507 | 0.2452 | — | — | — |
| 391 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (Non-reasoning) | 0.2448 | — | — | — |
| 392 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 4 (Non-reasoning) | 0.2446 | 443.37 | 0.0000 | ❌ |
| 393 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4 | 0.2443 | — | — | — |
| 394 | <img src="https://artificialanalysis.ai/img/logos/nousresearch_small.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 405B (Non-reasoning) | 0.2430 | 2,327.76 | 0.0285 | ❌ |
| 395 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder 30B A3B | 0.2418 | 1,868.46 | 0.0235 | ❌ |
| 396 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-8B-A1B | 0.2396 | — | — | — |
| 397 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 30B A3B | 0.2391 | 694.86 | 0.0000 | ❌ |
| 398 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6V (Non-reasoning) | 0.2384 | 773.24 | 0.0000 | ❌ |
| 399 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 E2B | 0.2372 | — | — | — |
| 400 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Omni 30B A3B (Reasoning) | 0.2367 | 2,553.73 | 0.0409 | ❌ |
| 401 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral Small 2 | 0.2348 | 0.00 | 0.0000 | ❌ |
| 402 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B | 0.2328 | 21,360.44 | 0.4979 | ❌ |
| 403 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5V | 0.2318 | 4,808.95 | 0.1497 | ❌ |
| 404 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-2.6B | 0.2317 | 0.00 | 0.0000 | ❌ |
| 405 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 12B v2 VL | 0.2308 | 1,602.98 | 0.0200 | ❌ |
| 406 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Large 2 (Nov) | 0.2297 | — | — | — |
| 407 | <img src="https://artificialanalysis.ai/img/logos/tii_small.svg" width="18" alt="TII UAE" /> TII UAE | Falcon-H1R-7B | 0.2283 | — | — | — |
| 408 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Ultra | 0.2273 | — | — | — |
| 409 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3 (Dec) | 0.2269 | — | — | — |
| 410 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Magistral Small 1.2 | 0.2265 | — | — | — |
| 411 | <img src="https://artificialanalysis.ai/img/logos/nanbeige_small.png" width="18" alt="Nanbeige" /> Nanbeige | Nanbeige4.1-3B | 0.2185 | — | — | — |
| 412 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova Pro | 0.2183 | — | — | — |
| 413 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3.2 | 0.2176 | 232.38 | 0.0000 | ❌ |
| 414 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3.1 32B Think | 0.2174 | — | — | — |
| 415 | <img src="https://artificialanalysis.ai/img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam 105B (high) | 0.2168 | — | — | — |
| 416 | <img src="https://artificialanalysis.ai/img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.0 32B | 0.2159 | — | — | — |
| 417 | <img src="https://artificialanalysis.ai/img/logos/mbzuai_small.svg" width="18" alt="MBZUAI Institute of Foundation Models" /> MBZUAI Institute of Foundation Models | K2-V2 (low) | 0.2139 | — | — | — |
| 418 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 9B V2 | 0.2135 | 420.60 | 0.0000 | ❌ |
| 419 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 2B | 0.2134 | — | — | — |
| 420 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Non-reasoning) | 0.2111 | 380.72 | 0.0000 | ❌ |
| 421 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-flash-2.0 | 0.2110 | — | — | — |
| 422 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 4 Scout | 0.2101 | 491.14 | 0.0000 | ❌ |
| 423 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Super 49B v1.5 (Non-reasoning) | 0.2092 | 554.25 | 0.0000 | ❌ |
| 424 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 32B | 0.2091 | 1,682.39 | 0.0211 | ❌ |
| 425 | <img src="https://artificialanalysis.ai/img/logos/nousresearch_small.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 70B | 0.2076 | — | — | — |
| 426 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral Small (May) | 0.2063 | — | — | — |
| 427 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova Lite | 0.2058 | 331.34 | 0.0000 | ❌ |
| 428 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.3 Nemotron Super 49B | 0.2027 | — | — | — |
| 429 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 32B | 0.2014 | — | — | — |
| 430 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen2.5 72B | 0.2014 | — | — | — |
| 431 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 14B | 0.2007 | 10,680.22 | 0.2520 | ❌ |
| 432 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-flash-2.0 | 0.2006 | 364.13 | 0.0000 | ❌ |
| 433 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 8B | 0.2003 | 622.05 | 0.0000 | ❌ |
| 434 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B | 0.1987 | 6,102.98 | 0.1704 | ❌ |
| 435 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Magistral Small 1 | 0.1986 | — | — | — |
| 436 | <img src="https://artificialanalysis.ai/img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 2 | 0.1935 | — | — | — |
| 437 | <img src="https://artificialanalysis.ai/img/logos/cohere_small.svg" width="18" alt="Cohere" /> Cohere | Command A | 0.1933 | 7,383.59 | 0.1850 | ❌ |
| 438 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Large 2 (Jul) | 0.1929 | — | — | — |
| 439 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral Small | 0.1927 | — | — | — |
| 440 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B (Non-reasoning) | 0.1926 | 2,213.76 | 0.0273 | ❌ |
| 441 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Ministral 3 14B | 0.1922 | 217.25 | 0.0000 | ❌ |
| 442 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.1 Nemotron 70B | 0.1912 | 1,865.98 | 0.0235 | ❌ |
| 443 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano 4B | 0.1895 | — | — | — |
| 444 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 4B (Reasoning) | 0.1888 | — | — | — |
| 445 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3.1 | 0.1881 | 233.26 | 0.0000 | ❌ |
| 446 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o mini | 0.1880 | 1,172.17 | 0.0067 | ❌ |
| 447 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3 Haiku | 0.1874 | — | — | — |
| 448 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.3 Nemotron Super 49B (Non-reasoning) | 0.1859 | — | — | — |
| 449 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B A3B 2507 (Non-reasoning) | 0.1841 | 711.19 | 0.0000 | ❌ |
| 450 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.1 70B | 0.1822 | 614.60 | 0.0000 | ❌ |
| 451 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 9B V2 (Non-reasoning) | 0.1818 | 188.33 | 0.0000 | ❌ |
| 452 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B | 0.1818 | — | — | — |
| 453 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5V (Non-reasoning) | 0.1803 | 1,371.56 | 0.0094 | ❌ |
| 454 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 E2B (Non-reasoning) | 0.1802 | — | — | — |
| 455 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 32B (Non-reasoning) | 0.1794 | 565.27 | 0.0000 | ❌ |
| 456 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 2B (Non-reasoning) | 0.1781 | — | — | — |
| 457 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.1 30B | 0.1775 | — | — | — |
| 458 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 nano | 0.1753 | 523.45 | 0.0000 | ❌ |
| 459 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3.1 32B Instruct | 0.1745 | — | — | — |
| 460 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Omni 30B A3B | 0.1730 | 786.40 | 0.0000 | ❌ |
| 461 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (minimal) | 0.1723 | 331.83 | 0.0000 | ❌ |
| 462 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B 2507 (Non-reasoning) | 0.1709 | — | — | — |
| 463 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.1 8B | 0.1696 | 41.60 | 0.0000 | ❌ |
| 464 | <img src="https://artificialanalysis.ai/img/logos/celeris.svg" width="18" alt="Celeris" /> Celeris | Celeris-1 | 0.1669 | 1,041.26 | 0.0046 | ❌ |
| 465 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 32B Think | 0.1668 | — | — | — |
| 466 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Llama 70B | 0.1664 | 3,110.44 | 0.0479 | ❌ |
| 467 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.3 70B | 0.1659 | 7,011.41 | 0.1755 | ❌ |
| 468 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 14B | 0.1649 | — | — | — |
| 469 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi Linear 48B A3B Instruct | 0.1645 | — | — | — |
| 470 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Ministral 3 8B | 0.1639 | 162.16 | 0.0000 | ❌ |
| 471 | <img src="https://artificialanalysis.ai/img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 2 (Non-reasoning) | 0.1638 | — | — | — |
| 472 | <img src="https://artificialanalysis.ai/img/logos/nousresearch_small.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 70B (Non-reasoning) | 0.1608 | — | — | — |
| 473 | <img src="https://artificialanalysis.ai/img/logos/ai21_small.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba Reasoning 3B | 0.1602 | — | — | — |
| 474 | <img src="https://artificialanalysis.ai/img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.0 32B (Non-reasoning) | 0.1581 | — | — | — |
| 475 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.1 8B | 0.1580 | 83.28 | 0.0000 | ❌ |
| 476 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova Micro | 0.1553 | 201.60 | 0.0000 | ❌ |
| 477 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 24B A2B | 0.1548 | — | — | — |
| 478 | <img src="https://artificialanalysis.ai/img/logos/ai21_small.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba 1.7 Large | 0.1537 | — | — | — |
| 479 | <img src="https://artificialanalysis.ai/img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam 30B (high) | 0.1519 | — | — | — |
| 480 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 12B v2 VL (Non-reasoning) | 0.1503 | 477.35 | 0.0000 | ❌ |
| 481 | <img src="https://artificialanalysis.ai/img/logos/openbmb_small.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM-V 4.6 1.3B | 0.1499 | — | — | — |
| 482 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3 | 0.1495 | 235.22 | 0.0000 | ❌ |
| 483 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 8B | 0.1492 | 5,342.68 | 0.1586 | ❌ |
| 484 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B (Non-reasoning) | 0.1456 | 696.04 | 0.0000 | ❌ |
| 485 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano (Non-reasoning) | 0.1430 | 157.62 | 0.0000 | ❌ |
| 486 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 27B | 0.1409 | — | — | — |
| 487 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H Small | 0.1397 | 283.39 | 0.0000 | ❌ |
| 488 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 4B | 0.1394 | — | — | — |
| 489 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 0528 Qwen3 8B | 0.1358 | — | — | — |
| 490 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 14B (Non-reasoning) | 0.1336 | 1,107.36 | 0.0057 | ❌ |
| 491 | <img src="https://artificialanalysis.ai/img/logos/microsoft_small.svg" width="18" alt="Microsoft" /> Microsoft | Phi-4 | 0.1290 | 365.35 | 0.0000 | ❌ |
| 492 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Ministral 3 3B | 0.1286 | 112.64 | 0.0000 | ❌ |
| 493 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.1 Nemotron Nano 4B v1.1 | 0.1277 | — | — | — |
| 494 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 270M | 0.1262 | — | — | — |
| 495 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3 70B | 0.1209 | — | — | — |
| 496 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.2 11B (Vision) | 0.1206 | 356.15 | 0.0000 | ❌ |
| 497 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 0.8B | 0.1176 | — | — | — |
| 498 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.2 3B | 0.1175 | — | — | — |
| 499 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 7B Think | 0.1168 | — | — | — |
| 500 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-1.2B-Instruct | 0.1103 | — | — | — |
| 501 | <img src="https://artificialanalysis.ai/img/logos/reka_small.svg" width="18" alt="Reka AI" /> Reka AI | Reka Flash 3 | 0.1098 | — | — | — |
| 502 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 2.6B | 0.1095 | — | — | — |
| 503 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-mini-2.0 | 0.1091 | — | — | — |
| 504 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 8B (Non-reasoning) | 0.1081 | 543.29 | 0.0000 | ❌ |
| 505 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Molmo2-8B | 0.1052 | — | — | — |
| 506 | <img src="https://artificialanalysis.ai/img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam M | 0.1047 | — | — | — |
| 507 | <img src="https://artificialanalysis.ai/img/logos/ai21_small.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba 1.7 Mini | 0.1034 | — | — | — |
| 508 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-1.2B-Thinking | 0.1020 | — | — | — |
| 509 | <img src="https://artificialanalysis.ai/img/logos/microsoft_small.svg" width="18" alt="Microsoft" /> Microsoft | Phi-4 Mini | 0.1000 | 0.00 | 0.0000 | ❌ |
| 510 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 12B | 0.0982 | — | — | — |
| 511 | <img src="https://artificialanalysis.ai/img/logos/swiss-ai-initiative_small.png" width="18" alt="Swiss AI Initiative" /> Swiss AI Initiative | Apertus 70B Instruct | 0.0953 | — | — | — |
| 512 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 0.8B (Non-reasoning) | 0.0949 | — | — | — |
| 513 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 7B | 0.0938 | — | — | — |
| 514 | <img src="https://artificialanalysis.ai/img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | Exaone 4.0 1.2B | 0.0928 | — | — | — |
| 515 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H 1B | 0.0922 | — | — | — |
| 516 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | OLMo 2 32B | 0.0920 | — | — | — |
| 517 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.2 1B | 0.0913 | — | — | — |
| 518 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 1.7B | 0.0899 | — | — | — |
| 519 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.1 3B | 0.0883 | — | — | — |
| 520 | <img src="https://artificialanalysis.ai/img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | Exaone 4.0 1.2B (Non-reasoning) | 0.0857 | — | — | — |
| 521 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 8B A1B | 0.0838 | — | — | — |
| 522 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 Micro | 0.0813 | — | — | — |
| 523 | <img src="https://artificialanalysis.ai/img/logos/microsoft_small.svg" width="18" alt="Microsoft" /> Microsoft | Phi-3 Mini | 0.0757 | — | — | — |
| 524 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 4B | 0.0752 | — | — | — |
| 525 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 3.3 8B | 0.0728 | 239.74 | 0.0000 | ❌ |
| 526 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-VL-1.6B | 0.0704 | — | — | — |
| 527 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 1B | 0.0696 | — | — | — |
| 528 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 350M | 0.0687 | — | — | — |
| 529 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 1.2B | 0.0669 | — | — | — |
| 530 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3n E4B | 0.0669 | — | — | — |
| 531 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 0.6B | 0.0662 | — | — | — |
| 532 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3 8B | 0.0660 | — | — | — |
| 533 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral 7B | 0.0636 | 268.68 | 0.0000 | ❌ |
| 534 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 1.7B (Non-reasoning) | 0.0579 | — | — | — |
| 535 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 1B | 0.0574 | — | — | — |
| 536 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | OLMo 2 7B | 0.0573 | — | — | — |
| 537 | <img src="https://artificialanalysis.ai/img/logos/swiss-ai-initiative_small.png" width="18" alt="Swiss AI Initiative" /> Swiss AI Initiative | Apertus 8B Instruct | 0.0564 | — | — | — |
| 538 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H 350M | 0.0523 | — | — | — |
| 539 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Molmo 7B-D | 0.0490 | — | — | — |
| 540 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 0.6B (Non-reasoning) | 0.0449 | — | — | — |
| 541 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3n E2B | 0.0372 | — | — | — |
| 542 | <img src="https://artificialanalysis.ai/img/logos/cohere_small.svg" width="18" alt="Cohere" /> Cohere | Tiny Aya Global | 0.0368 | — | — | — |
| 543 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 1.5B | 0.0000 | — | — | — |

## 品牌帕累托前沿连线（仅体现在图中）

以下十一个品牌在图中拥有单独的帕累托连线（较窄宽度，品牌主题色，图层高于总体灰色连线）。表中数量为**入图顶点数**——品牌前沿上低于总体前沿第一级的顶点同样不入图（本表与图例一致）：

| 品牌 | 主题色 | 品牌前沿模型数（入图） |
|------|--------|--------------|
| <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | `#cc785c` | 11 |
| <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | `#1f1f1f` | 10 |
| <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | `#0089f4` | 2 |
| <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | `#1c7ff8` | 2 |
| <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | `#34A853` | 4 |
| <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | `#736cd3` | 7 |
| <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | `#047AFE` | 3 |
| <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | `#ff7018` | 2 |
| <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | `#2243e6` | 3 |
| <img src="https://artificialanalysis.ai/img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | `#EB3568` | 1 |
| <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | `#ff6900` | 2 |

## 评分方法

1. **18项评估指标**各自线性归一化到 [0,1]
2. **综合能力值** = 所有有效归一化分数的算术平均
3. **综合能力再归一化**：线性映射到 [0,1]，性能最好的模型 = 1，最差的模型 = 0
4. **Pareto前沿** = 不被任何其他模型支配的模型（综合能力 ≥ 且成本 ≤，且至少一项严格更优；成本为 0 的免费模型同样参与——横轴左端恒为 0，免费模型是合法前沿候选）
5. **模型范围** = Status: All（含已弃用模型；缺少足够评估数据者不参与排名）
6. **图表纵轴基线（V17）**：图表的 y = 0 取总体帕累托前沿的第一级（最低能力；本例 y0 = 0.6215，即前沿左端点 Ling-3.0-flash-VL）；综合能力低于该级的模型不出现在图表中（表格不受影响）。图中纵坐标 chart_y = (能力 - y0)/(1 - y0)，因此前沿左端点恰好落在 (0, 0)、最优模型恰好为 y = 1。该过滤在横轴映射构建之前完成


## 横轴映射（分位数等密度映射，V17）与分布分析

横轴（单请求成本）按**经验分位数（rank）映射**——以 103 个入图正成本模型（综合能力 ≥ 前沿第一级）的成本分布为基准：

```
x = 0                            当 c ≤ 0（免费模型，钉在最左缘）
x = interp(log10(c); knots)      当 c > 0
```

其中 knots = (log10(c_i), 名次_i/(n-1)) 为入图正成本模型按成本排序后的 101 个锚点（等成本并列取平均名次，保证 x 是成本的单值函数；n-1 归一化使最大成本恰为 x = 1）。该映射在 **y 基线过滤之后**构建（V17：先以帕累托前沿第一级为 y = 0、剔除低性能模型，再对入图模型建映射）。

**该映射保证：**

- **函数端点严格钉死**：c = 0 → x = 0；最大成本 → x = 1——函数经过 (0,0) 与 (1,1)；
- **严格均匀密度**：x 是模型名次的线性函数，因此**任意等宽区段的模型数恒定**（每 0.1 宽度恰为 10 个模型）——无论截取哪一段，模型数 ÷ 宽度都等于全图的模型总数 ÷ 总宽度。V12 的单一 logistic 函数在过滤后的分布上做不到（十分位在 8~24 间摆动），故替换为精确分位数映射；
- 各数量级区间的入图模型数：1–10: 0，10–100: 0，100–1k: 1，1k–10k: 24，10k–100k: 61，100k–1M: 16
- **同一倍率区间的宽度 ∝ 该区间模型数**——均匀密度的必然结果：1k→10k 与 100k→1M 同为 10 倍率，但前者 24 个模型、后者 16 个，前者宽度约为后者的 1.5 倍。若改用「等倍率等距」（纯对数轴），两段的模型密度将相差 1.5 倍，与均匀密度目标冲突——两者数学上不可兼得，本图以均匀密度（最高优先级）为准；
- **左端恒为 0**（c = 0；1 个免费模型位于最左缘）
- 最低正成本 798.65 → x = 0.0000；最高成本 1,041,480 → x = 1.0000（严格 = 1）
- 中位数位置 0.500（≈ 0.5 居中）；左右两半模型数：左 52 / 右 52
- 横轴十分位模型数：11，11，10，10，10，11，10，10，10，11（严格均匀：x 为名次的线性函数，仅等成本并列的边界归属可致 ±1）
- **10^x 数量级指示**（位置 = x(10^x)）：10^0 → 0.000，10^1 → 0.000，10^2 → 0.000，10^3 → 0.004，10^4 → 0.236，10^5 → 0.839，10^6 → 0.995

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
| CacheHitRate | [AA Coding Agents](https://artificialanalysis.ai/agents/coding-agents) | 全部模型-Agent搭配的 `cacheHitRate` 求平均（13 个有效值，均值 = 0.9485），对所有模型统一使用 |
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
**模型总数（Status: All）**: 543 个参与排名（另有模型因评估数据不足未列入；总体帕累托前沿 16 个；图表入图 104 个——综合能力 ≥ 前沿第一级）  

## 图表说明（黑底）

（V17 起本说明置于文末，图表之后直接跟随模型表格。）

图表说明：**灰色实线** = 总体帕累托前沿；**彩色细线** = 十一个品牌的单独帕累托前沿（品牌主题色，图层高于总体连线；暗色品牌元素带窄白边；顶点按（横轴位置、能力升序）连接，等成本点自下而上）；品牌前沿模型圆点同样使用品牌颜色。模型名称/思考程度标注优先骑在连线之上（点的左/右两侧皆可，同一条线段可容纳两个标签——各贴各的点；文字与连线平行、中轴线重合，连线仅在文字两侧绘制）；骑线位被其他标签占据时自动「让位」——占用者挪到自己的另一个骑线位，双方都保持骑线；实在骑不上线时按四级优先依次退让（V16）：离点最近位置的上方/下方平行偏移 → 点的两条连线延长线上就近 → 两连线夹角扇区内就近。标签规则（V13/V15）：品牌前沿模型共享的前导块按「最长有效切点」剔除 —— 切点止于分界符，或止于字母且其后紧跟数字（如 Claude Opus 5 → Opus 5、GPT-5.6 Sol → 5.6 Sol、Kimi K2.6 → 2.6、Qwen3.8 Max → 3.8 Max、MiMo-V2.5 → 2.5、MiniMax-M2.1 → 2.1）；(non-reasoning) 简写为 (non)；同一模型在品牌连线上相邻出现 2 次以上时仅性能最低者保留全名、相邻较高者只标思考程度，不相邻的重复出现保留全名（每次重新计算）；标签位置与序列同向（V15）——品牌前沿上越靠右上的模型，其标签重心必须同时更靠右且更靠上（两分量都 >= 0，至少是 (0,0)，仅其一非负不算合格；初始放置违反时自动就近重摆，单标签无解（被前后邻居夹死）时按窗口级联重排整体挪动，均不产生新的重叠）。纵轴 y = 0 = 总体帕累托前沿第一级（y0 = 0.6215，前沿左端点 Ling-3.0-flash-VL 恰为 (0,0)），能力低于该级的 421 个模型与缺少成本数据的 18 个模型不出现在图中；横轴为分位数等密度映射（见上文「横轴映射」节），10^x 数量级指示位于 x(10^x)，同一倍率区间的宽度与该区间内模型数成正比。
