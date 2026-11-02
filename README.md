# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

## 全部模型（综合能力从高到低，最优 = 1，最差 = 0）

共收录 **Status: All**（含已弃用）的全部模型；按重新归一化后的综合能力排序。「帕累托」列：✅ = 总体帕累托前沿模型，❌ = 被支配，— = 无成本数据无法判定。图表纵轴以总体帕累托前沿第一级（y0 = 0.5561，即前沿左端点 K2 Horizon 375B A23B）为 0：综合能力 ≥ 该级且有成本数据的 180 个模型入图，389 个能力低于第一级、41 个缺少成本数据的模型不出现在图中，成本高于品牌前沿最大值的模型同样不入图（本表不受影响，仍完整列出全部模型）。

| # | 品牌 | 模型 | 综合能力 | 单请求成本 | 横轴位置 | 帕累托 |
|---|------|------|---------|-----------|-----------|------|
| 1 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Carbon (high) | 1.0000 | 274,597.72 | 0.8049 | ✅ |
| 2 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Carbon (medium) | 0.9759 | — | — | — |
| 3 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (max with fallback) | 0.9665 | 1,407,033.73 | 1.0000 | ❌ |
| 4 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (xhigh with fallback) | 0.9516 | 226,416.85 | 0.7819 | ✅ |
| 5 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (max) | 0.9449 | 100,035.47 | 0.6846 | ✅ |
| 6 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (max) | 0.9423 | 309,669.26 | 0.8193 | ❌ |
| 7 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (max with fallback) | 0.9416 | 956,155.18 | 0.9539 | ❌ |
| 8 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (xhigh) | 0.9411 | 714,673.19 | 0.9191 | ❌ |
| 9 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (max) | 0.9349 | 1,356,815.92 | 0.9957 | ❌ |
| 10 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (xhigh) | 0.9335 | 63,184.49 | 0.6299 | ✅ |
| 11 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (xhigh with fallback) | 0.9317 | 263,783.03 | 0.8002 | ❌ |
| 12 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (max with fallback) | 0.9277 | 711,846.24 | 0.9186 | ❌ |
| 13 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Argon (high) | 0.9255 | 81,654.03 | 0.6604 | ❌ |
| 14 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (high) | 0.9254 | 42,101.45 | 0.5817 | ✅ |
| 15 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (high) | 0.9215 | 336,823.79 | 0.8293 | ❌ |
| 16 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5 (with fallback) | 0.9187 | 387,606.96 | 0.8461 | ❌ |
| 17 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Wonder Full (max) | 0.9178 | — | — | — |
| 18 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (high with fallback) | 0.9146 | 90,407.62 | 0.6725 | ❌ |
| 19 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (max) | 0.9077 | 294,621.88 | 0.8133 | ❌ |
| 20 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (max) | 0.9032 | 167,896.97 | 0.7463 | ❌ |
| 21 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (xhigh) | 0.9012 | 118,332.97 | 0.7046 | ❌ |
| 22 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (high with fallback) | 0.8960 | 83,815.25 | 0.6635 | ❌ |
| 23 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (medium) | 0.8923 | 56,168.20 | 0.6159 | ❌ |
| 24 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (xhigh) | 0.8865 | 137,231.61 | 0.7222 | ❌ |
| 25 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (high) | 0.8844 | 53,648.79 | 0.6105 | ❌ |
| 26 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (medium with fallback) | 0.8784 | 46,511.89 | 0.5935 | ❌ |
| 27 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3.1 Pro | 0.8775 | 28,060.33 | 0.5337 | ✅ |
| 28 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (medium) | 0.8708 | 30,914.76 | 0.5452 | ❌ |
| 29 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (xhigh) | 0.8693 | 332,231.62 | 0.8277 | ❌ |
| 30 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (xhigh) | 0.8653 | 208,169.51 | 0.7719 | ❌ |
| 31 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.3 Codex (xhigh) | 0.8618 | 113,017.86 | 0.6991 | ❌ |
| 32 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (high) | 0.8616 | 46,271.32 | 0.5929 | ❌ |
| 33 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Terra (max) | 0.8589 | 144,828.75 | 0.7287 | ❌ |
| 34 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (medium with fallback) | 0.8568 | 71,792.76 | 0.6451 | ❌ |
| 35 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (medium) | 0.8540 | 12,506.31 | 0.4389 | ✅ |
| 36 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3 (max) | 0.8505 | 42,090.50 | 0.5817 | ❌ |
| 37 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Wonder (max) | 0.8482 | 54,238.48 | 0.6118 | ❌ |
| 38 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (low) | 0.8476 | 49,010.23 | 0.5998 | ❌ |
| 39 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (xhigh with fallback) | 0.8399 | 43,000.62 | 0.5842 | ❌ |
| 40 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.3 (xhigh) | 0.8392 | 12,772.98 | 0.4414 | ❌ |
| 41 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (high) | 0.8388 | 120,216.25 | 0.7065 | ❌ |
| 42 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 Max | 0.8345 | 18,530.88 | 0.4849 | ❌ |
| 43 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (medium) | 0.8335 | 33,386.26 | 0.5543 | ❌ |
| 44 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (xhigh) | 0.8330 | 93,387.00 | 0.6764 | ❌ |
| 45 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (low with fallback) | 0.8241 | 42,565.43 | 0.5830 | ❌ |
| 46 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (high) | 0.8230 | 25,607.63 | 0.5229 | ❌ |
| 47 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.8 (max) | 0.8189 | 88,727.89 | 0.6703 | ❌ |
| 48 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (medium) | 0.8169 | — | — | — |
| 49 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Terra (xhigh) | 0.8156 | 38,591.44 | 0.5714 | ❌ |
| 50 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (high) | 0.8146 | — | — | — |
| 51 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (xhigh) | 0.8144 | 31,898.00 | 0.5489 | ❌ |
| 52 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (medium) | 0.8136 | 30,676.83 | 0.5443 | ❌ |
| 53 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.7 (max) | 0.8118 | 63,726.73 | 0.6309 | ❌ |
| 54 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.3 (max) | 0.8068 | 12,772.98 | 0.4414 | ❌ |
| 55 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (max) | 0.8049 | 242,129.08 | 0.7899 | ❌ |
| 56 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (high) | 0.8031 | 35,536.51 | 0.5617 | ❌ |
| 57 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (medium) | 0.7969 | 24,042.23 | 0.5155 | ❌ |
| 58 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 Max (0902) | 0.7967 | 18,530.88 | 0.4849 | ❌ |
| 59 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (xhigh) | 0.7966 | 182,610.89 | 0.7563 | ❌ |
| 60 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (high) | 0.7959 | 15,226.30 | 0.4619 | ❌ |
| 61 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Terra (high) | 0.7933 | 13,657.44 | 0.4492 | ❌ |
| 62 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark | 0.7901 | — | — | — |
| 63 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (medium) | 0.7891 | 43,050.61 | 0.5844 | ❌ |
| 64 | <img src="https://artificialanalysis.ai/img/logos/sapiens.svg" width="18" alt="Sapiens AI" /> Sapiens AI | Agnes 2.5 Pro Beta | 0.7842 | — | — | — |
| 65 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (low) | 0.7827 | 8,926.05 | 0.3998 | ✅ |
| 66 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 Codex (xhigh) | 0.7825 | 212,207.71 | 0.7742 | ❌ |
| 67 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3 Pro Preview (high) | 0.7810 | — | — | — |
| 68 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (high) | 0.7798 | 35,226.30 | 0.5606 | ❌ |
| 69 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (low) | 0.7794 | 23,573.68 | 0.5132 | ❌ |
| 70 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (max) | 0.7750 | 142,337.53 | 0.7266 | ❌ |
| 71 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3 (max) | 0.7745 | 14,271.54 | 0.4543 | ❌ |
| 72 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.2 (max) | 0.7733 | 14,271.54 | 0.4543 | ❌ |
| 73 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (max) | 0.7679 | 22,317.38 | 0.5067 | ❌ |
| 74 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.6 (max) | 0.7670 | 44,971.08 | 0.5896 | ❌ |
| 75 | <img src="https://artificialanalysis.ai/img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step 5 Preview | 0.7641 | 8,280.17 | 0.3912 | ✅ |
| 76 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (low) | 0.7630 | — | — | — |
| 77 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (medium) | 0.7605 | — | — | — |
| 78 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.7 (xhigh) | 0.7603 | 58,123.22 | 0.6200 | ❌ |
| 79 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.5 (high) | 0.7600 | 11,353.32 | 0.4276 | ❌ |
| 80 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.7 (high) | 0.7593 | 28,649.26 | 0.5362 | ❌ |
| 81 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 v2 | 0.7585 | 9,026.09 | 0.4011 | ❌ |
| 82 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (low with fallback) | 0.7574 | 31,153.71 | 0.5461 | ❌ |
| 83 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (medium) | 0.7547 | — | — | — |
| 84 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.1 Flash | 0.7541 | 2,991.38 | 0.2773 | ✅ |
| 85 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.2 (xhigh) | 0.7522 | 12,772.98 | 0.4414 | ❌ |
| 86 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 2.4T A95B | 0.7493 | 18,530.88 | 0.4849 | ❌ |
| 87 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (high with fallback) | 0.7491 | 20,901.82 | 0.4990 | ❌ |
| 88 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.1 Pro Preview | 0.7480 | 39,413.94 | 0.5739 | ❌ |
| 89 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (low) | 0.7475 | 22,367.74 | 0.5070 | ❌ |
| 90 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 Max Preview | 0.7471 | — | — | — |
| 91 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Terra (medium) | 0.7448 | 5,932.34 | 0.3531 | ❌ |
| 92 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash 0731 (max) | 0.7367 | 1,045.98 | 0.1718 | ✅ |
| 93 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (low) | 0.7360 | 26,616.41 | 0.5275 | ❌ |
| 94 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash (max) | 0.7348 | 3,233.19 | 0.2857 | ❌ |
| 95 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (medium) | 0.7347 | 6,801.86 | 0.3687 | ❌ |
| 96 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Haiku 5.5 (max) | 0.7335 | 43,971.94 | 0.5869 | ❌ |
| 97 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash Vision (max) | 0.7268 | 3,690.95 | 0.3002 | ❌ |
| 98 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (high) | 0.7268 | — | — | — |
| 99 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (xhigh) | 0.7257 | 10,944.72 | 0.4234 | ❌ |
| 100 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark Open (xhigh) | 0.7216 | 12,772.98 | 0.4414 | ❌ |
| 101 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (xhigh) | 0.7213 | 37,856.97 | 0.5691 | ❌ |
| 102 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (low) | 0.7208 | 13,115.27 | 0.4444 | ❌ |
| 103 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3 Flash | 0.7180 | 6,072.96 | 0.3558 | ❌ |
| 104 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.1 (xhigh) | 0.7174 | 12,772.98 | 0.4414 | ❌ |
| 105 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.6 Flash (high) | 0.7160 | 15,815.80 | 0.4663 | ❌ |
| 106 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3-Flash | 0.7158 | 1,620.69 | 0.2136 | ❌ |
| 107 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash 1017 (max) | 0.7144 | 3,233.19 | 0.2857 | ❌ |
| 108 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.5 | 0.7133 | 42,970.81 | 0.5842 | ❌ |
| 109 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8-Flash-Next | 0.7067 | 1,413.94 | 0.2002 | ❌ |
| 110 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 Plus | 0.7057 | 18,915.08 | 0.4873 | ❌ |
| 111 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 Codex (high) | 0.7054 | 27,884.78 | 0.5330 | ❌ |
| 112 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.6-Pro | 0.7041 | 2,465.13 | 0.2567 | ❌ |
| 113 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 | 0.7039 | — | — | — |
| 114 | <img src="https://artificialanalysis.ai/img/logos/motif.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif 3 (Beta) | 0.7006 | — | — | — |
| 115 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.1 Flash 1019 | 0.6963 | — | — | — |
| 116 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.7 (low) | 0.6958 | 11,454.71 | 0.4287 | ❌ |
| 117 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.7 (non-reasoning, high) | 0.6941 | 21,793.43 | 0.5039 | ❌ |
| 118 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (medium) | 0.6938 | — | — | — |
| 119 | <img src="https://artificialanalysis.ai/img/logos/motif.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif 3 | 0.6905 | — | — | — |
| 120 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 27B | 0.6901 | 6,176.72 | 0.3577 | ❌ |
| 121 | <img src="https://artificialanalysis.ai/img/logos/nex.svg" width="18" alt="Nex AGI" /> Nex AGI | Nex-N2-Pro | 0.6890 | — | — | — |
| 122 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.6 | 0.6849 | 21,869.37 | 0.5043 | ❌ |
| 123 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Haiku 5.5 (xhigh) | 0.6830 | 7,582.42 | 0.3811 | ❌ |
| 124 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (high) | 0.6814 | 3,819.89 | 0.3039 | ❌ |
| 125 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 Codex (high) | 0.6804 | 20,389.08 | 0.4961 | ❌ |
| 126 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.7 Max | 0.6802 | 27,995.65 | 0.5335 | ❌ |
| 127 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (high) | 0.6801 | 15,874.09 | 0.4667 | ❌ |
| 128 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (max) | 0.6795 | 17,375.47 | 0.4773 | ❌ |
| 129 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (medium) | 0.6790 | 48,127.62 | 0.5976 | ❌ |
| 130 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Pro | 0.6780 | — | — | — |
| 131 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5-Turbo | 0.6698 | — | — | — |
| 132 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 (high) | 0.6662 | 61,061.34 | 0.6259 | ❌ |
| 133 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Omni-0327 | 0.6641 | — | — | — |
| 134 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Terra (low) | 0.6641 | 4,358.10 | 0.3185 | ❌ |
| 135 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (medium with fallback) | 0.6605 | 8,679.71 | 0.3966 | ❌ |
| 136 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (low) | 0.6589 | 5,135.04 | 0.3368 | ❌ |
| 137 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (low) | 0.6556 | 10,674.08 | 0.4205 | ❌ |
| 138 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (low) | 0.6544 | — | — | — |
| 139 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5 | 0.6532 | 14,007.26 | 0.4521 | ❌ |
| 140 | <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.5 | 0.6531 | 3,503.23 | 0.2944 | ❌ |
| 141 | <img src="https://artificialanalysis.ai/img/logos/tencent.svg" width="18" alt="Tencent" /> Tencent | Hy3-preview | 0.6515 | — | — | — |
| 142 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o3 | 0.6509 | 18,536.72 | 0.4849 | ❌ |
| 143 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.7 Plus | 0.6502 | 4,988.50 | 0.3336 | ❌ |
| 144 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (max) | 0.6501 | 153,741.36 | 0.7358 | ❌ |
| 145 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.7 Code | 0.6480 | 13,263.70 | 0.4457 | ❌ |
| 146 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok Build 0.1 0616 | 0.6479 | 7,471.26 | 0.3794 | ❌ |
| 147 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash (Feb 2026) | 0.6475 | — | — | — |
| 148 | <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M3.1-Flash | 0.6467 | 1,729.52 | 0.2201 | ❌ |
| 149 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 Thinking | 0.6436 | 12,250.00 | 0.4365 | ❌ |
| 150 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (high) | 0.6435 | 84,837.16 | 0.6650 | ❌ |
| 151 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (low) | 0.6430 | 12,058.90 | 0.4347 | ❌ |
| 152 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro 0813 (max) | 0.6407 | 11,091.66 | 0.4249 | ❌ |
| 153 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (xhigh) | 0.6387 | 123,192.86 | 0.7094 | ❌ |
| 154 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash | 0.6357 | — | — | — |
| 155 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (max) | 0.6349 | 1,716.29 | 0.2193 | ❌ |
| 156 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max Thinking | 0.6332 | — | — | — |
| 157 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM 5V Turbo | 0.6323 | — | — | — |
| 158 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Omni | 0.6310 | — | — | — |
| 159 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (xhigh) | 0.6309 | 25,438.41 | 0.5222 | ❌ |
| 160 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.1 | 0.6305 | 20,668.17 | 0.4977 | ❌ |
| 161 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (xhigh) | 0.6296 | 8,735.63 | 0.3973 | ❌ |
| 162 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.6 (non-reasoning, high) | 0.6279 | 22,749.92 | 0.5090 | ❌ |
| 163 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (max) | 0.6239 | 7,023.43 | 0.3723 | ❌ |
| 164 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 | 0.6237 | 21,423.44 | 0.5019 | ❌ |
| 165 | <img src="https://artificialanalysis.ai/img/logos/apodex.svg" width="18" alt="Apodex" /> Apodex | Apodex 1.1 | 0.6233 | — | — | — |
| 166 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Haiku 5.5 (high) | 0.6205 | 3,279.69 | 0.2872 | ❌ |
| 167 | <img src="https://artificialanalysis.ai/img/logos/china-mobile.png" width="18" alt="China Mobile" /> China Mobile | JT-4.1 Flash 236B A21B | 0.6202 | — | — | — |
| 168 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Opus | 0.6194 | — | — | — |
| 169 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 35B A3B | 0.6170 | 5,147.27 | 0.3371 | ❌ |
| 170 | <img src="https://artificialanalysis.ai/img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step 3.5 Flash 2603 | 0.6168 | 997.13 | 0.1675 | ✅ |
| 171 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (medium) | 0.6148 | 11,317.95 | 0.4273 | ❌ |
| 172 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (xhigh) | 0.6127 | 26,082.57 | 0.5251 | ❌ |
| 173 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (high) | 0.6110 | — | — | — |
| 174 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.5 | 0.6110 | 11,698.54 | 0.4311 | ❌ |
| 175 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (non-reasoning) | 0.6103 | 18,630.91 | 0.4855 | ❌ |
| 176 | <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.1 | 0.6078 | 3,503.23 | 0.2944 | ❌ |
| 177 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (high) | 0.6058 | 15,713.42 | 0.4655 | ❌ |
| 178 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Large 4 Preview | 0.6031 | 6,709.90 | 0.3671 | ❌ |
| 179 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (medium) | 0.6010 | 4,643.28 | 0.3256 | ❌ |
| 180 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.1 Fast | 0.6007 | — | — | — |
| 181 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (low with fallback) | 0.6007 | 8,633.80 | 0.3960 | ❌ |
| 182 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (minimal) | 0.6005 | 8,081.25 | 0.3884 | ❌ |
| 183 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7 | 0.5978 | 8,194.32 | 0.3900 | ❌ |
| 184 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5 | 0.5964 | 769.70 | 0.1449 | ✅ |
| 185 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3 (low) | 0.5962 | 42,090.50 | 0.5817 | ❌ |
| 186 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 Instant (May 2026) | 0.5941 | — | — | — |
| 187 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-3.0-flash-VL | 0.5939 | — | — | — |
| 188 | <img src="https://artificialanalysis.ai/img/logos/kwaikat.svg" width="18" alt="KwaiKAT" /> KwaiKAT | KAT-Coder-Pro V2 | 0.5933 | — | — | — |
| 189 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 397B A17B | 0.5923 | 13,623.04 | 0.4489 | ❌ |
| 190 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.1 (non-reasoning) | 0.5902 | 6,027.35 | 0.3549 | ❌ |
| 191 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 27B | 0.5898 | 22,587.04 | 0.5081 | ❌ |
| 192 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (non-reasoning) | 0.5889 | 8,930.30 | 0.3999 | ❌ |
| 193 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (low) | 0.5883 | 16,737.74 | 0.4729 | ❌ |
| 194 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 Codex mini (high) | 0.5856 | 7,593.88 | 0.3812 | ❌ |
| 195 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.6-Flash | 0.5854 | 808.82 | 0.1491 | ❌ |
| 196 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3 Pro Preview (low) | 0.5847 | — | — | — |
| 197 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.5 (non-reasoning) | 0.5846 | 22,103.09 | 0.5056 | ❌ |
| 198 | <img src="https://artificialanalysis.ai/img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Open2 250B | 0.5844 | — | — | — |
| 199 | <img src="https://artificialanalysis.ai/img/logos/china-mobile.png" width="18" alt="China Mobile" /> China Mobile | JT-4.1 Flash 236B A21B (non-reasoning) | 0.5826 | — | — | — |
| 200 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (high) | 0.5821 | 9,368.82 | 0.4054 | ❌ |
| 201 | <img src="https://artificialanalysis.ai/img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step 3.7 Flash | 0.5812 | 3,369.25 | 0.2902 | ❌ |
| 202 | <img src="https://artificialanalysis.ai/img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step 3.5 Flash | 0.5805 | 997.13 | 0.1675 | ❌ |
| 203 | <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M3 | 0.5803 | 3,785.56 | 0.3029 | ❌ |
| 204 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 | 0.5794 | — | — | — |
| 205 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (non-reasoning, high) | 0.5790 | 13,151.43 | 0.4448 | ❌ |
| 206 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5-Pro | 0.5782 | 2,904.04 | 0.2741 | ❌ |
| 207 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.6 (non-reasoning) | 0.5779 | 4,501.16 | 0.3221 | ❌ |
| 208 | <img src="https://artificialanalysis.ai/img/logos/tencent.svg" width="18" alt="Tencent" /> Tencent | Hy3 | 0.5751 | 1,787.59 | 0.2234 | ❌ |
| 209 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.1 Opus | 0.5734 | — | — | — |
| 210 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 122B A10B | 0.5709 | 8,235.63 | 0.3906 | ❌ |
| 211 | <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2 | 0.5701 | 3,176.72 | 0.2838 | ❌ |
| 212 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 27B (non-reasoning) | 0.5686 | 2,507.71 | 0.2585 | ❌ |
| 213 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 397B A17B (non-reasoning) | 0.5684 | 2,628.61 | 0.2635 | ❌ |
| 214 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (non-reasoning, low) | 0.5663 | 13,178.74 | 0.4450 | ❌ |
| 215 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Haiku 5.5 (medium) | 0.5644 | 1,603.38 | 0.2125 | ❌ |
| 216 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (medium) | 0.5626 | 12,379.11 | 0.4377 | ❌ |
| 217 | <img src="https://artificialanalysis.ai/img/logos/multiversecomputing.svg" width="18" alt="Multiverse Computing" /> Multiverse Computing | Quasar 438B (max) | 0.5617 | 982.97 | 0.1662 | ❌ |
| 218 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (xhigh) | 0.5609 | 2,991.62 | 0.2773 | ❌ |
| 219 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (low) | 0.5590 | 11,333.54 | 0.4274 | ❌ |
| 220 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 Omni Plus | 0.5572 | 3,938.52 | 0.3073 | ❌ |
| 221 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 375B A23B | 0.5561 | 0.00 | 0.0000 | ✅ |
| 222 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash 1017 (high) | 0.5553 | — | — | — |
| 223 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (medium) | 0.5553 | 1,378.76 | 0.1978 | ❌ |
| 224 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (medium) | 0.5553 | 2,104.80 | 0.2401 | ❌ |
| 225 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Sonnet | 0.5543 | 23,397.77 | 0.5123 | ❌ |
| 226 | <img src="https://artificialanalysis.ai/img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 4 | 0.5516 | 3,741.38 | 0.3016 | ❌ |
| 227 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3 (low) | 0.5476 | 14,271.54 | 0.4543 | ❌ |
| 228 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (medium) | 0.5440 | 28,672.55 | 0.5363 | ❌ |
| 229 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 Fast | 0.5419 | — | — | — |
| 230 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 35B A3B | 0.5387 | 13,484.65 | 0.4477 | ❌ |
| 231 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (high) | 0.5364 | 2,145.07 | 0.2421 | ❌ |
| 232 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 27B (non-reasoning) | 0.5336 | 2,920.27 | 0.2747 | ❌ |
| 233 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Speciale | 0.5328 | — | — | — |
| 234 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Terra (non-reasoning) | 0.5287 | 4,143.08 | 0.3129 | ❌ |
| 235 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.5 (non-reasoning) | 0.5285 | 7,826.02 | 0.3847 | ❌ |
| 236 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3 Flash (non-reasoning) | 0.5275 | 2,733.40 | 0.2676 | ❌ |
| 237 | <img src="https://artificialanalysis.ai/img/logos/thinking-machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling (xhigh) | 0.5267 | 12,313.93 | 0.4371 | ❌ |
| 238 | <img src="https://artificialanalysis.ai/img/logos/reflection.svg" width="18" alt="Reflection" /> Reflection | Beam 1.0 | 0.5242 | 3,612.07 | 0.2978 | ❌ |
| 239 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 122B A10B (non-reasoning) | 0.5237 | 2,891.02 | 0.2736 | ❌ |
| 240 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon MoVA 36B A4B | 0.5234 | — | — | — |
| 241 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o4-mini (high) | 0.5232 | 18,784.50 | 0.4865 | ❌ |
| 242 | <img src="https://artificialanalysis.ai/img/logos/kwaikat.svg" width="18" alt="KwaiKAT" /> KwaiKAT | KAT-Coder-Pro V1 | 0.5229 | — | — | — |
| 243 | <img src="https://artificialanalysis.ai/img/logos/thinking-machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling Small | 0.5227 | 3,741.38 | 0.3016 | ❌ |
| 244 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (non-reasoning) | 0.5227 | 24,604.30 | 0.5182 | ❌ |
| 245 | <img src="https://artificialanalysis.ai/img/logos/bytedance.svg" width="18" alt="ByteDance Seed" /> ByteDance Seed | Doubao Seed Code | 0.5216 | — | — | — |
| 246 | <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.7 | 0.5211 | 4,339.96 | 0.3180 | ❌ |
| 247 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Ultra | 0.5204 | 8,975.26 | 0.4005 | ❌ |
| 248 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (medium) | 0.5201 | 10,664.39 | 0.4204 | ❌ |
| 249 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (medium) | 0.5194 | 6,426.72 | 0.3622 | ❌ |
| 250 | <img src="https://artificialanalysis.ai/img/logos/china-mobile.png" width="18" alt="China Mobile" /> China Mobile | JT-35B-Flash | 0.5182 | — | — | — |
| 251 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (non-reasoning) | 0.5095 | 9,405.91 | 0.4059 | ❌ |
| 252 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.0 Flash | 0.5062 | 735.34 | 0.1411 | ❌ |
| 253 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Haiku 5.5 (low) | 0.5053 | 1,155.37 | 0.1810 | ❌ |
| 254 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5 (non-reasoning) | 0.5039 | 4,433.30 | 0.3204 | ❌ |
| 255 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (low) | 0.5030 | 25,736.34 | 0.5235 | ❌ |
| 256 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (medium) | 0.5008 | 8,735.63 | 0.3973 | ❌ |
| 257 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash-Lite | 0.5006 | 8,290.82 | 0.3913 | ❌ |
| 258 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (medium) | 0.5002 | — | — | — |
| 259 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (non-reasoning) | 0.4978 | 12,448.08 | 0.4384 | ❌ |
| 260 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Sep) | 0.4972 | — | — | — |
| 261 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (low) | 0.4961 | 8,735.63 | 0.3973 | ❌ |
| 262 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (low) | 0.4957 | — | — | — |
| 263 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Sonnet | 0.4934 | — | — | — |
| 264 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (low) | 0.4930 | 1,144.09 | 0.1801 | ❌ |
| 265 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max Thinking (Preview) | 0.4922 | — | — | — |
| 266 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-2.6-1T | 0.4918 | — | — | — |
| 267 | <img src="https://artificialanalysis.ai/img/logos/sktelecom.svg" width="18" alt="SK Telecom" /> SK Telecom | A.X-K2 | 0.4905 | — | — | — |
| 268 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-3.0-flash-Fin | 0.4895 | — | — | — |
| 269 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (high) | 0.4890 | 20,172.19 | 0.4948 | ❌ |
| 270 | <img src="https://artificialanalysis.ai/img/logos/baidu.svg" width="18" alt="Baidu" /> Baidu | ERNIE 5.0 Thinking Preview | 0.4871 | — | — | — |
| 271 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (medium) | 0.4865 | — | — | — |
| 272 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 35B A3B (non-reasoning) | 0.4850 | 2,023.21 | 0.2361 | ❌ |
| 273 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (non-reasoning) | 0.4844 | 12,057.68 | 0.4346 | ❌ |
| 274 | <img src="https://artificialanalysis.ai/img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | G9v3-39A5B | 0.4829 | — | — | — |
| 275 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Exp | 0.4813 | — | — | — |
| 276 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 26B A4B | 0.4809 | 1,379.45 | 0.1978 | ❌ |
| 277 | <img src="https://artificialanalysis.ai/img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE | 0.4806 | — | — | — |
| 278 | <img src="https://artificialanalysis.ai/img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.5 33B | 0.4790 | — | — | — |
| 279 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 235B A22B | 0.4773 | — | — | — |
| 280 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (high) | 0.4770 | 6,426.72 | 0.3622 | ❌ |
| 281 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 (non-reasoning) | 0.4770 | — | — | — |
| 282 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (non-reasoning) | 0.4761 | — | — | — |
| 283 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 3 mini Reasoning (high) | 0.4744 | 2,132.54 | 0.2415 | ❌ |
| 284 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 31B | 0.4743 | 0.00 | 0.0000 | ❌ |
| 285 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3.5 Super VL | 0.4720 | 1,838.36 | 0.2263 | ❌ |
| 286 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 12B | 0.4715 | 808.91 | 0.1491 | ❌ |
| 287 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o1 | 0.4710 | — | — | — |
| 288 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Sonnet (non-reasoning) | 0.4704 | 13,139.58 | 0.4446 | ❌ |
| 289 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 (non-reasoning) | 0.4669 | — | — | — |
| 290 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7 (non-reasoning) | 0.4665 | 4,167.25 | 0.3135 | ❌ |
| 291 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5-Pro (non-reasoning) | 0.4655 | 1,064.27 | 0.1734 | ❌ |
| 292 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Large 4 (high) | 0.4625 | — | — | — |
| 293 | <img src="https://artificialanalysis.ai/img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE 2.0 | 0.4608 | — | — | — |
| 294 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Pro | 0.4599 | 33,502.71 | 0.5547 | ❌ |
| 295 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 35B A3B (non-reasoning) | 0.4596 | 1,850.09 | 0.2269 | ❌ |
| 296 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7-Flash | 0.4588 | 1,135.34 | 0.1793 | ❌ |
| 297 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6 | 0.4570 | 6,859.19 | 0.3696 | ❌ |
| 298 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 4B | 0.4565 | 392.67 | 0.0945 | ❌ |
| 299 | <img src="https://artificialanalysis.ai/img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Mini 4 | 0.4539 | 1,153.02 | 0.1808 | ❌ |
| 300 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 9B | 0.4523 | 579.52 | 0.1222 | ❌ |
| 301 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 v2 (non-reasoning) | 0.4512 | 4,015.84 | 0.3094 | ❌ |
| 302 | <img src="https://artificialanalysis.ai/img/logos/longcat.svg" width="18" alt="LongCat" /> LongCat | LongCat 2.0 | 0.4509 | 7,957.97 | 0.3866 | ❌ |
| 303 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash | 0.4499 | 8,909.06 | 0.3996 | ❌ |
| 304 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (low) | 0.4487 | 9,184.98 | 0.4031 | ❌ |
| 305 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Large 4 (medium) | 0.4484 | — | — | — |
| 306 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-2.6-1T | 0.4467 | 6,426.72 | 0.3622 | ❌ |
| 307 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 31B (non-reasoning) | 0.4454 | 1,658.18 | 0.2159 | ❌ |
| 308 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 Terminus | 0.4448 | — | — | — |
| 309 | <img src="https://artificialanalysis.ai/img/logos/nanbeige.png" width="18" alt="Nanbeige" /> Nanbeige | Nanbeige4.3-33B | 0.4445 | 0.00 | 0.0000 | ❌ |
| 310 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash (non-reasoning) | 0.4438 | — | — | — |
| 311 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Medium 3.5 | 0.4435 | 21,045.25 | 0.4998 | ❌ |
| 312 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (non-reasoning) | 0.4430 | 3,280.26 | 0.2873 | ❌ |
| 313 | <img src="https://artificialanalysis.ai/img/logos/servicenow.svg" width="18" alt="ServiceNow" /> ServiceNow | Apriel-v1.6-15B-Thinker | 0.4429 | — | — | — |
| 314 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 Instant (June 2026) | 0.4389 | 82,650.83 | 0.6619 | ❌ |
| 315 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 9B (non-reasoning) | 0.4384 | 238.65 | 0.0657 | ❌ |
| 316 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max | 0.4371 | — | — | — |
| 317 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 Omni Flash | 0.4370 | 809.19 | 0.1492 | ❌ |
| 318 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.2 (non-reasoning) | 0.4358 | 6,094.91 | 0.3562 | ❌ |
| 319 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 7B | 0.4317 | — | — | — |
| 320 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (low) | 0.4308 | 6,426.72 | 0.3622 | ❌ |
| 321 | <img src="https://artificialanalysis.ai/img/logos/tencent.svg" width="18" alt="Tencent" /> Tencent | Hy3-preview (non-reasoning) | 0.4304 | — | — | — |
| 322 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 32B | 0.4298 | — | — | — |
| 323 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 0905 | 0.4289 | 1,787.29 | 0.2234 | ❌ |
| 324 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Glimmer (high) | 0.4288 | 3,553.16 | 0.2960 | ❌ |
| 325 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.1 Flash-Lite | 0.4222 | 3,792.20 | 0.3031 | ❌ |
| 326 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Haiku | 0.4217 | 14,301.11 | 0.4545 | ❌ |
| 327 | <img src="https://artificialanalysis.ai/img/logos/cohere.svg" width="18" alt="Cohere" /> Cohere | Command A+ | 0.4213 | 0.00 | 0.0000 | ❌ |
| 328 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron Cascade 2 30B A3B | 0.4196 | — | — | — |
| 329 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 26B A4B (non-reasoning) | 0.4177 | 879.57 | 0.1564 | ❌ |
| 330 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Sonnet (non-reasoning) | 0.4168 | — | — | — |
| 331 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (non-reasoning) | 0.4147 | 10,490.12 | 0.4185 | ❌ |
| 332 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok Code Fast 1 | 0.4143 | — | — | — |
| 333 | <img src="https://artificialanalysis.ai/img/logos/servicenow.svg" width="18" alt="ServiceNow" /> ServiceNow | Apriel-v1.5-15B-Thinker | 0.4137 | — | — | — |
| 334 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 | 0.4136 | 10,000.00 | 0.4129 | ❌ |
| 335 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3.5 Bolt 74B-A9B | 0.4132 | — | — | — |
| 336 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Sep) | 0.4130 | — | — | — |
| 337 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (high) | 0.4111 | 5,490.18 | 0.3444 | ❌ |
| 338 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash 1017 (non-reasoning) | 0.4111 | 1,141.02 | 0.1798 | ❌ |
| 339 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Sep) (non-reasoning) | 0.4109 | — | — | — |
| 340 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (low) | 0.4107 | 587.47 | 0.1232 | ❌ |
| 341 | <img src="https://artificialanalysis.ai/img/logos/inceptionlabs.svg" width="18" alt="Inception" /> Inception | Mercury 2 | 0.4090 | — | — | — |
| 342 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (non-reasoning) | 0.4085 | 10,422.82 | 0.4177 | ❌ |
| 343 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 | 0.4042 | 11,124.24 | 0.4253 | ❌ |
| 344 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash (non-reasoning) | 0.4030 | 1,153.59 | 0.1808 | ❌ |
| 345 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (minimal) | 0.4023 | 7,963.63 | 0.3867 | ❌ |
| 346 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5 | 0.4013 | — | — | — |
| 347 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (medium) | 0.4004 | 2,832.85 | 0.2714 | ❌ |
| 348 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.7 Sonnet (non-reasoning) | 0.3963 | — | — | — |
| 349 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 | 0.3929 | 1,708.27 | 0.2189 | ❌ |
| 350 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 0528 | 0.3919 | 23,728.09 | 0.5139 | ❌ |
| 351 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Super | 0.3911 | 3,226.65 | 0.2855 | ❌ |
| 352 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.7 Sonnet | 0.3884 | — | — | — |
| 353 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 (non-reasoning) | 0.3875 | 8,049.99 | 0.3879 | ❌ |
| 354 | <img src="https://artificialanalysis.ai/img/logos/arcee.svg" width="18" alt="Arcee AI" /> Arcee AI | Trinity Large Thinking | 0.3793 | — | — | — |
| 355 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 Terminus (non-reasoning) | 0.3789 | 1,979.85 | 0.2338 | ❌ |
| 356 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (non-reasoning) | 0.3750 | 3,986.33 | 0.3086 | ❌ |
| 357 | <img src="https://artificialanalysis.ai/img/logos/bytedance.svg" width="18" alt="ByteDance Seed" /> ByteDance Seed | Seed-OSS-36B-Instruct | 0.3672 | 1,548.71 | 0.2091 | ❌ |
| 358 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Haiku (non-reasoning) | 0.3669 | 4,402.14 | 0.3196 | ❌ |
| 359 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Exp (non-reasoning) | 0.3660 | — | — | — |
| 360 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max (Preview) | 0.3641 | — | — | — |
| 361 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-120b (high) | 0.3628 | 2,529.45 | 0.2594 | ❌ |
| 362 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 3 | 0.3612 | 18,176.44 | 0.4826 | ❌ |
| 363 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6 (non-reasoning) | 0.3611 | 5,204.74 | 0.3384 | ❌ |
| 364 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (non-reasoning) | 0.3580 | 1,036.58 | 0.1710 | ❌ |
| 365 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (ChatGPT) | 0.3575 | — | — | — |
| 366 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B A22B 2507 | 0.3574 | 7,767.67 | 0.3838 | ❌ |
| 367 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | DiffusionGemma 26B A4B | 0.3557 | — | — | — |
| 368 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5-Air | 0.3532 | 2,550.14 | 0.2602 | ❌ |
| 369 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder Next | 0.3493 | 3,437.58 | 0.2924 | ❌ |
| 370 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 4B (non-reasoning) | 0.3481 | 95.23 | 0.0307 | ❌ |
| 371 | <img src="https://artificialanalysis.ai/img/logos/china-mobile.png" width="18" alt="China Mobile" /> China Mobile | JT-MINI | 0.3478 | — | — | — |
| 372 | <img src="https://artificialanalysis.ai/img/logos/multiversecomputing.svg" width="18" alt="Multiverse Computing" /> Multiverse Computing | HyperNova 60B 2605 (high) | 0.3474 | — | — | — |
| 373 | <img src="https://artificialanalysis.ai/img/logos/cohere.svg" width="18" alt="Cohere" /> Cohere | North Mini Code | 0.3468 | 0.00 | 0.0000 | ❌ |
| 374 | <img src="https://artificialanalysis.ai/img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE (non-reasoning) | 0.3464 | — | — | — |
| 375 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 (non-reasoning) | 0.3442 | 6,674.79 | 0.3665 | ❌ |
| 376 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (minimal) | 0.3440 | 1,570.28 | 0.2105 | ❌ |
| 377 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 2.6 Flash | 0.3432 | — | — | — |
| 378 | <img src="https://artificialanalysis.ai/img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Open 100B | 0.3418 | — | — | — |
| 379 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 235B A22B | 0.3412 | 2,385.24 | 0.2532 | ❌ |
| 380 | <img src="https://artificialanalysis.ai/img/logos/longcat.svg" width="18" alt="LongCat" /> LongCat | LongCat Flash Lite | 0.3409 | — | — | — |
| 381 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 3.7B | 0.3406 | — | — | — |
| 382 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.2 30B | 0.3403 | — | — | — |
| 383 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Sep) (non-reasoning) | 0.3401 | — | — | — |
| 384 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-1T | 0.3389 | — | — | — |
| 385 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (non-reasoning) | 0.3370 | 1,901.39 | 0.2297 | ❌ |
| 386 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Magistral Medium 1.2 | 0.3361 | — | — | — |
| 387 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 12B (non-reasoning) | 0.3355 | 286.27 | 0.0754 | ❌ |
| 388 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (non-reasoning) | 0.3346 | 7,075.41 | 0.3732 | ❌ |
| 389 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite | 0.3322 | 2,457.81 | 0.2563 | ❌ |
| 390 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B 2507 | 0.3297 | 2,574.20 | 0.2612 | ❌ |
| 391 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (non-reasoning) | 0.3293 | 4,175.23 | 0.3138 | ❌ |
| 392 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Next 80B A3B | 0.3291 | — | — | — |
| 393 | <img src="https://artificialanalysis.ai/img/logos/korea-telecom.png" width="18" alt="Korea Telecom" /> Korea Telecom | Mi:dm K 2.5 Pro | 0.3291 | — | — | — |
| 394 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.1 Fast (non-reasoning) | 0.3288 | — | — | — |
| 395 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.0 Tiny | 0.3275 | 0.00 | 0.0000 | ❌ |
| 396 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Pixtral Large | 0.3268 | — | — | — |
| 397 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (high) | 0.3266 | — | — | — |
| 398 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6V | 0.3254 | 4,097.16 | 0.3117 | ❌ |
| 399 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Think V2 | 0.3244 | — | — | — |
| 400 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder 480B | 0.3218 | 3,622.05 | 0.2981 | ❌ |
| 401 | <img src="https://artificialanalysis.ai/img/logos/trillionlabs.svg" width="18" alt="Trillion Labs" /> Trillion Labs | Tri-21B-think Preview | 0.3218 | — | — | — |
| 402 | <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax M1 80k | 0.3188 | 5,823.99 | 0.3510 | ❌ |
| 403 | <img src="https://artificialanalysis.ai/img/logos/trillionlabs.svg" width="18" alt="Trillion Labs" /> Trillion Labs | Tri-21B-Think | 0.3176 | — | — | — |
| 404 | <img src="https://artificialanalysis.ai/img/logos/deepcogito.png" width="18" alt="Deep Cogito" /> Deep Cogito | Cogito v2.1 | 0.3168 | — | — | — |
| 405 | <img src="https://artificialanalysis.ai/img/logos/naver.webp" width="18" alt="Naver" /> Naver | HyperCLOVA X SEED Think (32B) | 0.3144 | — | — | — |
| 406 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (non-reasoning) | 0.3133 | 462.84 | 0.1057 | ❌ |
| 407 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3.5 Lightning | 0.3131 | 864.73 | 0.1549 | ❌ |
| 408 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro 0813 (non-reasoning) | 0.3127 | 3,832.81 | 0.3043 | ❌ |
| 409 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 Fast (non-reasoning) | 0.3111 | — | — | — |
| 410 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-20b (low) | 0.3109 | 791.24 | 0.1473 | ❌ |
| 411 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 30B A3B | 0.3104 | — | — | — |
| 412 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 32B | 0.3099 | — | — | — |
| 413 | <img src="https://artificialanalysis.ai/img/logos/inceptionlabs.svg" width="18" alt="Inception" /> Inception | Mercury 2.5 | 0.3091 | — | — | — |
| 414 | <img src="https://artificialanalysis.ai/img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-2B | 0.3048 | — | — | — |
| 415 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano Omni 30B A3B | 0.3025 | 3,485.63 | 0.2939 | ❌ |
| 416 | <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax M1 40k | 0.3010 | — | — | — |
| 417 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7-Flash (non-reasoning) | 0.3005 | 695.88 | 0.1366 | ❌ |
| 418 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Next 80B A3B | 0.3002 | 1,625.47 | 0.2139 | ❌ |
| 419 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano | 0.3001 | 1,000.00 | 0.1677 | ❌ |
| 420 | <img src="https://artificialanalysis.ai/img/logos/motif.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif-2-12.7B | 0.2964 | — | — | — |
| 421 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o3-mini (high) | 0.2958 | 36,055.76 | 0.5634 | ❌ |
| 422 | <img src="https://artificialanalysis.ai/img/logos/prime-intellect.svg" width="18" alt="Prime Intellect" /> Prime Intellect | INTELLECT-3 | 0.2956 | — | — | — |
| 423 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 mini | 0.2936 | 2,197.40 | 0.2446 | ❌ |
| 424 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-20b (high) | 0.2936 | 579.45 | 0.1221 | ❌ |
| 425 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (non-reasoning) | 0.2920 | 1,879.88 | 0.2285 | ❌ |
| 426 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.2 8B | 0.2904 | 801.51 | 0.1484 | ❌ |
| 427 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Small 4 | 0.2855 | 1,729.52 | 0.2201 | ❌ |
| 428 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-1T | 0.2840 | — | — | — |
| 429 | <img src="https://artificialanalysis.ai/img/logos/korea-telecom.png" width="18" alt="Korea Telecom" /> Korea Telecom | Mi:dm K 2.5 Pro Preview | 0.2796 | — | — | — |
| 430 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-120b (low) | 0.2795 | 2,737.50 | 0.2678 | ❌ |
| 431 | <img src="https://artificialanalysis.ai/img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 3 | 0.2783 | 1,729.52 | 0.2201 | ❌ |
| 432 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (non-reasoning) | 0.2743 | — | — | — |
| 433 | <img src="https://artificialanalysis.ai/img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step3 VL 10B | 0.2742 | — | — | — |
| 434 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o (Aug) | 0.2741 | 19,813.64 | 0.4927 | ❌ |
| 435 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 30B A3B | 0.2730 | 570.66 | 0.1210 | ❌ |
| 436 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Medium 3.1 | 0.2713 | — | — | — |
| 437 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (non-reasoning) | 0.2699 | 1,102.47 | 0.1766 | ❌ |
| 438 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B 2507 | 0.2696 | — | — | — |
| 439 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 8B | 0.2656 | — | — | — |
| 440 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Large 3 | 0.2650 | 1,675.10 | 0.2169 | ❌ |
| 441 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (medium) | 0.2628 | — | — | — |
| 442 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Devstral 2 | 0.2591 | — | — | — |
| 443 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3 0324 | 0.2584 | 1,965.38 | 0.2331 | ❌ |
| 444 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 (Jan) | 0.2570 | 12,566.15 | 0.4394 | ❌ |
| 445 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 12B v2 VL | 0.2565 | — | — | — |
| 446 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Omni 30B A3B | 0.2561 | 2,572.27 | 0.2612 | ❌ |
| 447 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Medium 3 | 0.2560 | 1,428.34 | 0.2012 | ❌ |
| 448 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B A3B 2507 | 0.2551 | — | — | — |
| 449 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 E4B (non-reasoning) | 0.2526 | 65.91 | 0.0220 | ❌ |
| 450 | <img src="https://artificialanalysis.ai/img/logos/tii.svg" width="18" alt="TII UAE" /> TII UAE | Falcon-H1R-7B | 0.2512 | — | — | — |
| 451 | <img src="https://artificialanalysis.ai/img/logos/nousresearch.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 405B | 0.2482 | 8,089.07 | 0.3885 | ❌ |
| 452 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Super 49B v1.5 | 0.2471 | — | — | — |
| 453 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Devstral Small 2 | 0.2458 | — | — | — |
| 454 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova Premier | 0.2440 | — | — | — |
| 455 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder 30B A3B | 0.2366 | 680.49 | 0.1348 | ❌ |
| 456 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.0 Flash | 0.2364 | — | — | — |
| 457 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 4 Maverick | 0.2361 | 2,731.49 | 0.2675 | ❌ |
| 458 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Small 4 (non-reasoning) | 0.2322 | 601.52 | 0.1250 | ❌ |
| 459 | <img src="https://artificialanalysis.ai/img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.0 32B | 0.2316 | — | — | — |
| 460 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o (Nov) | 0.2285 | 22,216.90 | 0.5062 | ❌ |
| 461 | <img src="https://artificialanalysis.ai/img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam 105B (high) | 0.2284 | 694.43 | 0.1364 | ❌ |
| 462 | <img src="https://artificialanalysis.ai/img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-1B | 0.2271 | — | — | — |
| 463 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Magistral Small 1.2 | 0.2226 | 4,044.54 | 0.3102 | ❌ |
| 464 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-flash-2.0 | 0.2208 | — | — | — |
| 465 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (non-reasoning) | 0.2154 | 387.32 | 0.0936 | ❌ |
| 466 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5V | 0.2152 | 5,888.65 | 0.3523 | ❌ |
| 467 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-flash-2.0 | 0.2125 | 377.42 | 0.0920 | ❌ |
| 468 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 E4B | 0.2093 | 261.78 | 0.0705 | ❌ |
| 469 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 2B | 0.2093 | — | — | — |
| 470 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.2 3B | 0.2062 | — | — | — |
| 471 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Ultra | 0.2062 | — | — | — |
| 472 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B | 0.2052 | — | — | — |
| 473 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 4B | 0.2039 | — | — | — |
| 474 | <img src="https://artificialanalysis.ai/img/logos/baidu.svg" width="18" alt="Baidu" /> Baidu | ERNIE 4.5 300B A47B | 0.2033 | — | — | — |
| 475 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.5 Haiku | 0.2033 | — | — | — |
| 476 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.3 Nemotron Super 49B | 0.2023 | — | — | — |
| 477 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Devstral Small (May) | 0.2022 | — | — | — |
| 478 | <img src="https://artificialanalysis.ai/img/logos/nousresearch.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 405B (non-reasoning) | 0.2013 | 2,389.16 | 0.2534 | ❌ |
| 479 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B A3B 2507 (non-reasoning) | 0.1994 | 264.93 | 0.0711 | ❌ |
| 480 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Large 2 (Jul) | 0.1993 | — | — | — |
| 481 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.1 30B | 0.1989 | — | — | — |
| 482 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova Pro | 0.1971 | 4,389.41 | 0.3193 | ❌ |
| 483 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Ministral 3 14B | 0.1959 | 420.38 | 0.0990 | ❌ |
| 484 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6V (non-reasoning) | 0.1957 | 2,546.87 | 0.2601 | ❌ |
| 485 | <img src="https://artificialanalysis.ai/img/logos/nousresearch.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 70B | 0.1940 | — | — | — |
| 486 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 2B (non-reasoning) | 0.1931 | — | — | — |
| 487 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.1 405B | 0.1928 | — | — | — |
| 488 | <img src="https://artificialanalysis.ai/img/logos/celeris.svg" width="18" alt="Celeris" /> Celeris | Celeris-1 | 0.1903 | 1,295.23 | 0.1918 | ❌ |
| 489 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen2.5 72B | 0.1897 | 581.98 | 0.1225 | ❌ |
| 490 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (low) | 0.1893 | — | — | — |
| 491 | <img src="https://artificialanalysis.ai/img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-1B (non-reasoning) | 0.1892 | — | — | — |
| 492 | <img src="https://artificialanalysis.ai/img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 2 | 0.1889 | — | — | — |
| 493 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Omni 30B A3B | 0.1878 | 804.24 | 0.1486 | ❌ |
| 494 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Devstral Medium | 0.1864 | — | — | — |
| 495 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 8B | 0.1852 | — | — | — |
| 496 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3 (Dec) | 0.1845 | 716.13 | 0.1389 | ❌ |
| 497 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B | 0.1840 | — | — | — |
| 498 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Small 3.1 | 0.1839 | 119.75 | 0.0374 | ❌ |
| 499 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-8B-A1B | 0.1815 | — | — | — |
| 500 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3.1 32B Think | 0.1805 | — | — | — |
| 501 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B | 0.1774 | 1,454.52 | 0.2029 | ❌ |
| 502 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Magistral Medium 1 | 0.1751 | — | — | — |
| 503 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Super 49B v1.5 (non-reasoning) | 0.1750 | — | — | — |
| 504 | <img src="https://artificialanalysis.ai/img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | G9v3-3B | 0.1745 | — | — | — |
| 505 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Small 3.2 | 0.1731 | 152.07 | 0.0458 | ❌ |
| 506 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B (non-reasoning) | 0.1717 | — | — | — |
| 507 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Large 2 (Nov) | 0.1704 | — | — | — |
| 508 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (minimal) | 0.1697 | 341.39 | 0.0857 | ❌ |
| 509 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o mini | 0.1692 | 1,156.93 | 0.1811 | ❌ |
| 510 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 32B | 0.1690 | 1,491.38 | 0.2054 | ❌ |
| 511 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 E2B (non-reasoning) | 0.1681 | — | — | — |
| 512 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 9B V2 | 0.1667 | 423.56 | 0.0996 | ❌ |
| 513 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 4 Scout | 0.1657 | 497.41 | 0.1108 | ❌ |
| 514 | <img src="https://artificialanalysis.ai/img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam 30B (high) | 0.1655 | — | — | — |
| 515 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 9B V2 (non-reasoning) | 0.1654 | 160.54 | 0.0479 | ❌ |
| 516 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Devstral Small | 0.1648 | — | — | — |
| 517 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5V (non-reasoning) | 0.1646 | 2,707.02 | 0.2666 | ❌ |
| 518 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B 2507 (non-reasoning) | 0.1638 | — | — | — |
| 519 | <img src="https://artificialanalysis.ai/img/logos/cohere.svg" width="18" alt="Cohere" /> Cohere | Command A | 0.1615 | 6,784.87 | 0.3684 | ❌ |
| 520 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 12B v2 VL (non-reasoning) | 0.1604 | 537.53 | 0.1165 | ❌ |
| 521 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Ministral 3 8B | 0.1603 | 316.28 | 0.0811 | ❌ |
| 522 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi Linear 48B A3B Instruct | 0.1597 | — | — | — |
| 523 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova Lite | 0.1597 | 334.85 | 0.0845 | ❌ |
| 524 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3 Haiku | 0.1590 | — | — | — |
| 525 | <img src="https://artificialanalysis.ai/img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 2 (non-reasoning) | 0.1583 | — | — | — |
| 526 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 14B | 0.1572 | 670.69 | 0.1336 | ❌ |
| 527 | <img src="https://artificialanalysis.ai/img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM-V 4.6 1.3B | 0.1568 | — | — | — |
| 528 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Magistral Small 1 | 0.1548 | — | — | — |
| 529 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 4B | 0.1536 | — | — | — |
| 530 | <img src="https://artificialanalysis.ai/img/logos/nanbeige.png" width="18" alt="Nanbeige" /> Nanbeige | Nanbeige4.1-3B | 0.1528 | — | — | — |
| 531 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 E2B | 0.1514 | — | — | — |
| 532 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.3 Nemotron Super 49B (non-reasoning) | 0.1505 | — | — | — |
| 533 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 32B Think | 0.1504 | — | — | — |
| 534 | <img src="https://artificialanalysis.ai/img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.0 32B (non-reasoning) | 0.1493 | — | — | — |
| 535 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Small 3 | 0.1480 | 73.14 | 0.0242 | ❌ |
| 536 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano (non-reasoning) | 0.1432 | 627.59 | 0.1283 | ❌ |
| 537 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3.1 32B Instruct | 0.1420 | — | — | — |
| 538 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.3 70B | 0.1387 | 6,469.51 | 0.3630 | ❌ |
| 539 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B (non-reasoning) | 0.1381 | 355.22 | 0.0881 | ❌ |
| 540 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 nano | 0.1378 | 612.22 | 0.1264 | ❌ |
| 541 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.1 Nemotron 70B | 0.1360 | — | — | — |
| 542 | <img src="https://artificialanalysis.ai/img/logos/ai21.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba Reasoning 3B | 0.1347 | — | — | — |
| 543 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.1 8B | 0.1329 | — | — | — |
| 544 | <img src="https://artificialanalysis.ai/img/logos/ai21.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba 1.7 Large | 0.1295 | — | — | — |
| 545 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.1 70B | 0.1281 | 652.90 | 0.1315 | ❌ |
| 546 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 8B | 0.1275 | — | — | — |
| 547 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 24B A2B | 0.1263 | — | — | — |
| 548 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-mini-2.0 | 0.1242 | — | — | — |
| 549 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 14B (non-reasoning) | 0.1229 | 205.88 | 0.0585 | ❌ |
| 550 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano 4B | 0.1226 | — | — | — |
| 551 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.1 Nemotron Nano 4B v1.1 | 0.1190 | — | — | — |
| 552 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H Small | 0.1182 | — | — | — |
| 553 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-2.6B | 0.1182 | — | — | — |
| 554 | <img src="https://artificialanalysis.ai/img/logos/nousresearch.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 70B (non-reasoning) | 0.1153 | — | — | — |
| 555 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.2 3B | 0.1140 | — | — | — |
| 556 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Llama 70B | 0.1136 | — | — | — |
| 557 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 7B Think | 0.1130 | — | — | — |
| 558 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-1.2B-Thinking | 0.1115 | — | — | — |
| 559 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 0528 Qwen3 8B | 0.1110 | — | — | — |
| 560 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Ministral 3 3B | 0.1062 | 217.16 | 0.0611 | ❌ |
| 561 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 8B (non-reasoning) | 0.1052 | — | — | — |
| 562 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 27B | 0.1050 | — | — | — |
| 563 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova Micro | 0.1009 | 204.08 | 0.0581 | ❌ |
| 564 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-1.2B-Instruct | 0.1007 | — | — | — |
| 565 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 0.8B (non-reasoning) | 0.0980 | — | — | — |
| 566 | <img src="https://artificialanalysis.ai/img/logos/ai21.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba 1.7 Mini | 0.0977 | — | — | — |
| 567 | <img src="https://artificialanalysis.ai/img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | Exaone 4.0 1.2B | 0.0959 | — | — | — |
| 568 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.2 11B (Vision) | 0.0911 | 388.05 | 0.0938 | ❌ |
| 569 | <img src="https://artificialanalysis.ai/img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | Exaone 4.0 1.2B (non-reasoning) | 0.0902 | — | — | — |
| 570 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 7B | 0.0900 | — | — | — |
| 571 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Molmo2-8B | 0.0874 | — | — | — |
| 572 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 1.7B | 0.0872 | — | — | — |
| 573 | <img src="https://artificialanalysis.ai/img/logos/microsoft.svg" width="18" alt="Microsoft" /> Microsoft | Phi-4 | 0.0851 | 374.35 | 0.0914 | ❌ |
| 574 | <img src="https://artificialanalysis.ai/img/logos/reka.svg" width="18" alt="Reka AI" /> Reka AI | Reka Flash 3 | 0.0848 | 558.91 | 0.1194 | ❌ |
| 575 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.1 3B | 0.0819 | — | — | — |
| 576 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | OLMo 2 32B | 0.0806 | — | — | — |
| 577 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 8B A1B | 0.0769 | — | — | — |
| 578 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 Micro | 0.0745 | — | — | — |
| 579 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 12B | 0.0740 | — | — | — |
| 580 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3 70B | 0.0740 | — | — | — |
| 581 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H 1B | 0.0717 | — | — | — |
| 582 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-VL-1.6B | 0.0710 | — | — | — |
| 583 | <img src="https://artificialanalysis.ai/img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam M | 0.0691 | — | — | — |
| 584 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.1 8B | 0.0661 | 61.05 | 0.0205 | ❌ |
| 585 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 1B | 0.0653 | — | — | — |
| 586 | <img src="https://artificialanalysis.ai/img/logos/microsoft.svg" width="18" alt="Microsoft" /> Microsoft | Phi-3 Mini | 0.0638 | — | — | — |
| 587 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 3.3 8B (non-reasoning) | 0.0634 | — | — | — |
| 588 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 1.7B (non-reasoning) | 0.0556 | — | — | — |
| 589 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 0.8B | 0.0547 | — | — | — |
| 590 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 4B | 0.0527 | — | — | — |
| 591 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 0.6B | 0.0525 | — | — | — |
| 592 | <img src="https://artificialanalysis.ai/img/logos/swiss-ai-initiative.png" width="18" alt="Swiss AI Initiative" /> Swiss AI Initiative | Apertus 70B Instruct | 0.0505 | — | — | — |
| 593 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 2.6B | 0.0454 | — | — | — |
| 594 | <img src="https://artificialanalysis.ai/img/logos/microsoft.svg" width="18" alt="Microsoft" /> Microsoft | Phi-4 Mini | 0.0437 | 205.35 | 0.0584 | ❌ |
| 595 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | OLMo 2 7B | 0.0417 | — | — | — |
| 596 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3n E4B | 0.0399 | — | — | — |
| 597 | <img src="https://artificialanalysis.ai/img/logos/swiss-ai-initiative.png" width="18" alt="Swiss AI Initiative" /> Swiss AI Initiative | Apertus 8B Instruct | 0.0361 | 247.28 | 0.0675 | ❌ |
| 598 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 0.6B (non-reasoning) | 0.0356 | — | — | — |
| 599 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H 350M | 0.0345 | — | — | — |
| 600 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 1.2B | 0.0336 | — | — | — |
| 601 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Molmo 7B-D | 0.0307 | — | — | — |
| 602 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3 8B | 0.0303 | — | — | — |
| 603 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 350M | 0.0268 | — | — | — |
| 604 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 1B | 0.0268 | — | — | — |
| 605 | <img src="https://artificialanalysis.ai/img/logos/cohere.svg" width="18" alt="Cohere" /> Cohere | Tiny Aya Global | 0.0226 | — | — | — |
| 606 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.2 1B | 0.0210 | — | — | — |
| 607 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 0.9B | 0.0141 | — | — | — |
| 608 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3n E2B | 0.0119 | — | — | — |
| 609 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral 7B | 0.0035 | — | — | — |
| 610 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 270M | 0.0000 | — | — | — |

## 品牌帕累托前沿连线（仅体现在图中）

以下 13 个品牌在图中拥有单独的帕累托连线（较窄宽度，品牌主题色，图层高于总体灰色连线）。表中数量为**入图顶点数**——品牌前沿上低于总体前沿第一级的顶点同样不入图（本表与图例一致）：

| 品牌 | 主题色 | 品牌前沿模型数（入图） |
|------|--------|--------------|
| <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | `#34A853` | 5 |
| <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | `#cc785c` | 11 |
| <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | `#047AFE` | 6 |
| <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | `#1f1f1f` | 12 |
| <img src="https://artificialanalysis.ai/img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | `#00F5E7` | 2 |
| <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | `#4fb5ff` | 1 |
| <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | `#2243e6` | 1 |
| <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | `#ff6900` | 2 |
| <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | `#1521a9` | 1 |
| <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | `#0089f4` | 4 |
| <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | `#ff7018` | 4 |
| <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | `#736cd3` | 6 |
| <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | `#1c7ff8` | 3 |

## 基准测试动态标定（Leave-One-Out Calibration）

不同基准测试的参测模型群体能力分布存在差异（例如部分高难度或专业领域基准测试仅覆盖头部高能力模型）。系统在标准归一化之后执行了**留一交叉动态映射标定流程**：

1. **排除单项基准**：暂时排除某项基准测试，计算各模型在其余测试项上的平均能力；
2. **全域归一化评估**：将排除后的平均能力归一化至 `[0, 1]`；
3. **锁定参测区间**：提取实际参测该基准测试的所有模型，以它们排除该项后的能力最高值和最低值分别作为该项的新映射上界和下界；
4. **并行同步迭代**：所有基准测试以 `[0, 1]` 为初值同步更新，完成一轮后以新上下界作为输入进入下一轮，重复迭代直至收敛。

> 标定状态：已完成 **14** 轮并行迭代收敛（容差阈值 $\Delta < 1e-05$）。标定得到的数据作为新指标独立保存，不覆盖原始基准测试归一化与综合能力。

| 基准测试项 | 英文标识 | 参测模型数 | 标定映射下界 | 标定映射上界 | 映射跨度 |
| :--- | :--- | :---: | :---: | :---: | :---: |
| AA Intelligence Index | `intelligenceIndex` | 92 | `0.1771` | `1.0000` | `0.8229` |
| GPQA Diamond | `gpqa` | 535 | `0.0000` | `0.9178` | `0.9178` |
| Humanity's Last Exam | `hle` | 603 | `0.0000` | `0.9501` | `0.9501` |
| MMMU Pro | `mmmuPro` | 294 | `0.0168` | `0.9667` | `0.9499` |
| IFBench Instruction Following | `ifbench` | 442 | `0.0000` | `0.8958` | `0.8958` |
| SciCode Coding | `scicode` | 244 | `0.0406` | `0.9501` | `0.9095` |
| CritPt Physics | `critpt` | 591 | `0.0000` | `0.9526` | `0.9526` |
| AA-LCR Long Context | `lcr` | 582 | `0.0000` | `1.0000` | `1.0000` |
| AA Omniscience Index | `omniscience` | 110 | `0.1771` | `1.0000` | `0.8229` |
| AA-Omniscience Accuracy | `omniscienceAccuracy` | 110 | `0.1719` | `1.0000` | `0.8281` |
| AA-Omniscience Non-Hallucination | `omniscienceNonHallucination` | 110 | `0.1707` | `1.0000` | `0.8293` |
| GDPval-AA Normalized | `gdpvalNormalized` | 307 | `0.0406` | `1.0000` | `0.9594` |
| AA Analyst Agent | `analystAgent` | 51 | `0.3326` | `0.9534` | `0.6209` |
| APEX-Agents-AA | `apexAgents` | 33 | `0.3099` | `0.8183` | `0.5084` |
| ITBench-SRE | `itbenchSre` | 45 | `0.1541` | `0.9723` | `0.8182` |
| τ²-Bench Telecom | `tau2` | 438 | `0.0000` | `0.8950` | `0.8950` |
| τ³-Bench Banking | `tauBanking` | 209 | `0.0306` | `0.9225` | `0.8919` |
| Terminal-Bench Hard | `terminalbenchHard` | 431 | `0.0035` | `0.8847` | `0.8812` |
| Terminal-Bench 2.1 | `terminalbenchV21` | 242 | `0.0393` | `0.9144` | `0.8751` |
| Terminal-Bench 4.0 | `terminalbenchV40` | 239 | `0.0408` | `1.0000` | `0.9592` |


## 评分方法

1. **20项评估指标**各自线性归一化到 [0,1]
   （AA Intelligence Index、GPQA Diamond、Humanity's Last Exam、MMMU Pro、IFBench Instruction Following、SciCode Coding、CritPt Physics、AA-LCR Long Context、AA Omniscience Index、AA-Omniscience Accuracy、AA-Omniscience Non-Hallucination、GDPval-AA Normalized、AA Analyst Agent、APEX-Agents-AA、ITBench-SRE、τ²-Bench Telecom、τ³-Bench Banking、Terminal-Bench Hard、Terminal-Bench 2.1、Terminal-Bench 4.0）
   > V18（2026-09-12）：AA 更新了基准列——新增 AA Analyst Agent、τ³-Bench Banking、Terminal-Bench 2.1 / 4.0 四项；AA Agentic Index 与 AA Coding Index 已从 AA 的数据源中移除，相应剔除。指标数由 18 → 20。
2. **综合能力值** = 所有有效归一化分数的算术平均
3. **综合能力再归一化**：线性映射到 [0,1]，性能最好的模型 = 1，最差的模型 = 0
4. **Pareto前沿** = 不被任何其他模型支配的模型（综合能力 ≥ 且成本 ≤，且至少一项严格更优；成本为 0 的免费模型同样参与——横轴左端恒为 0，免费模型是合法前沿候选）
5. **模型范围** = Status: All（含已弃用模型；缺少足够评估数据者不参与排名）
6. **图表纵轴基线（V17）**：图表的 y = 0 取总体帕累托前沿的第一级（最低能力；本例 y0 = 0.5561，即前沿左端点 K2 Horizon 375B A23B）；综合能力低于该级的模型不出现在图表中（表格不受影响）。图中纵坐标 chart_y = (能力 - y0)/(1 - y0)，因此前沿左端点恰好落在 (0, 0)、最优模型恰好为 y = 1。该过滤在横轴映射构建之前完成


## 横轴映射（对数映射，真零点，V21）与分布分析

横轴（单请求成本）为 **Y = A·ln(B·c+C)+D 对数映射**（B = 1；A、D 由端点解出；C = 325.48，r = B/C = 0.00307241 经网格搜索确定）：

```
x = 0                            当 c = 0（免费模型，真零点）
x = A·ln(c+C)+D                  当 c > 0（B = 1 并入；A、D 由端点解出）
```

其中 C = 325.48（r = B/C = 0.00307241），拟合集为 11 品牌前沿入图正成本模型（综合能力 ≥ 前沿第一级）的成本分布，目标为组内名次分位数（最小二乘误差 mse = 0.017074，最大偏离 0.2094）。该映射在 **y 基线过滤之后**构建（V17：先以帕累托前沿第一级为 y = 0、剔除低性能模型，再对入图模型建映射）。

**该映射保证：**

- **函数端点严格钉死**：c = 0 → x = 0；最大成本 → x = 1——函数经过 (0,0) 与 (1,1)；
- 各数量级区间的入图模型数：1–10: 0，10–100: 0，100–1k: 5，1k–10k: 51，10k–100k: 96，100k–1M: 25，1M–1.407M: 1
- **同倍率区间宽度相近**（对数轴性质）：1k→10k 与 100k→1M 同为 10 倍率，宽度相近（前者 51 个模型、后者 25 个）；与 V17 分位数映射不同，本图不追求均匀密度——密度不等如实显示；
- **左端恒为 0**（c = 0；1 个免费模型位于最左缘）
- 前沿最低正成本 769.70 → x = 0.1449（真实对数位置，不再钉 0；x = 0 恒为 c = 0 免费模型）；前沿最大成本 1,407,034 → x = 1.0000（= 1；高于前沿最大成本的模型不入图，仅表格保留）
- 中位数位置 0.485（≈ 0.5 居中）；左右两半模型数：左 98 / 右 82
- 横轴十分位模型数：1，6，19，29，43，41，16，13，7，5（对数映射下各十分位模型数自然不等）
- **10^x 数量级指示**（位置 = x(10^x)）：10^0 → 0.000，10^1 → 0.004，10^2 → 0.032，10^3 → 0.168，10^4 → 0.413，10^5 → 0.685，10^6 → 0.959

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
| CacheHitRate | [AA Coding Agents](https://artificialanalysis.ai/agents/coding-agents) | 全部模型-Agent搭配的 `cacheHitRate` 求平均（34 个有效值，均值 = 0.9411），对所有模型统一使用 |
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
**模型总数（Status: All）**: 610 个参与排名（另有模型因评估数据不足未列入；总体帕累托前沿 14 个；图表入图 180 个——综合能力 ≥ 前沿第一级）  

## 图表说明（黑底）

（V17 起本说明置于文末，图表之后直接跟随模型表格。）

图表说明：**灰色实线** = 总体帕累托前沿；**彩色细线** = 选定品牌的单独帕累托前沿（共 13 个品牌，（品牌主题色，图层高于总体连线；暗色品牌元素带窄白边；顶点按（横轴位置、能力升序）连接，等成本点自下而上）；品牌前沿模型圆点同样使用品牌颜色。模型名称/思考程度标注优先骑在连线之上（点的左/右两侧皆可，同一条线段可容纳两个标签——各贴各的点；文字与连线平行、中轴线重合，连线仅在文字两侧绘制）；骑线位被其他标签占据时自动「让位」——占用者挪到自己的另一个骑线位，双方都保持骑线；实在骑不上线时按四级优先依次退让（V16）：离点最近位置的上方/下方平行偏移 → 点的两条连线延长线上就近 → 两连线夹角扇区内就近。标签规则（V13/V15）：品牌前沿模型共享的前导块按「最长有效切点」剔除 —— 切点止于分界符，或止于字母且其后紧跟数字（如 Claude Opus 5 → Opus 5、GPT-5.6 Sol → 5.6 Sol、Kimi K2.6 → 2.6、Qwen3.8 Max → 3.8 Max、MiMo-V2.5 → 2.5、MiniMax-M2.1 → 2.1）；(non-reasoning) 简写为 (non)；同一模型在品牌连线上相邻出现 2 次以上时仅性能最低者保留全名、相邻较高者只标思考程度，不相邻的重复出现保留全名（每次重新计算）；标签位置与序列同向（V15）——品牌前沿上越靠右上的模型，其标签重心必须同时更靠右且更靠上（两分量都 >= 0，至少是 (0,0)，仅其一非负不算合格；初始放置违反时自动就近重摆，单标签无解（被前后邻居夹死）时按窗口级联重排整体挪动，均不产生新的重叠）。纵轴 y = 0 = 总体帕累托前沿第一级（y0 = 0.5561，前沿左端点 K2 Horizon 375B A23B 恰为 (0,0)），能力低于该级的 389 个模型、缺少成本数据的 41 个模型与成本高于品牌前沿最大值的模型不出现在图中；横轴为对数映射（见上文「横轴映射」节），10^x 数量级指示位于 x(10^x)，同一倍率区间的宽度相近（对数轴性质；本图不追求均匀密度）。
