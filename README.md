# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

## 全部模型（综合能力从高到低，最优 = 1，最差 = 0）

共收录 **Status: All**（含已弃用）的全部模型；按重新归一化后的综合能力排序。「帕累托」列：✅ = 总体帕累托前沿模型，❌ = 被支配，— = 无成本数据无法判定。图表纵轴以总体帕累托前沿第一级（y0 = 0.5069，即前沿左端点 Gemma 4 31B）为 0：综合能力 ≥ 该级且有成本数据的 175 个模型入图，363 个能力低于第一级、45 个缺少成本数据的模型不出现在图中，成本高于品牌前沿最大值的模型同样不入图（本表不受影响，仍完整列出全部模型）。

| # | 品牌 | 模型 | 综合能力 | 单请求成本 | 横轴位置 | 帕累托 |
|---|------|------|---------|-----------|-----------|------|
| 1 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (max with fallback) | 1.0000 | 1,278,065.40 | 1.0000 | ✅ |
| 2 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (xhigh with fallback) | 0.9956 | 223,154.99 | 0.7989 | ✅ |
| 3 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (max with fallback) | 0.9796 | 1,007,540.42 | 0.9726 | ❌ |
| 4 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (xhigh with fallback) | 0.9667 | 364,704.16 | 0.8555 | ❌ |
| 5 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (max with fallback) | 0.9633 | 613,773.08 | 0.9155 | ❌ |
| 6 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (xhigh) | 0.9576 | 414,143.01 | 0.8702 | ❌ |
| 7 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (max) | 0.9560 | 837,227.57 | 0.9513 | ❌ |
| 8 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (high with fallback) | 0.9556 | 66,576.47 | 0.6598 | ✅ |
| 9 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (max) | 0.9411 | 169,547.81 | 0.7673 | ❌ |
| 10 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (max) | 0.9408 | 96,560.59 | 0.7025 | ❌ |
| 11 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (high) | 0.9384 | 162,280.28 | 0.7623 | ❌ |
| 12 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (high with fallback) | 0.9344 | 108,114.56 | 0.7155 | ❌ |
| 13 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5 (with fallback) | 0.9340 | 352,377.95 | 0.8515 | ❌ |
| 14 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (xhigh) | 0.9320 | 64,275.56 | 0.6557 | ✅ |
| 15 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (xhigh) | 0.9284 | 80,668.22 | 0.6819 | ❌ |
| 16 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (medium with fallback) | 0.9272 | 50,085.94 | 0.6271 | ✅ |
| 17 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (high) | 0.9256 | 44,624.25 | 0.6139 | ✅ |
| 18 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (max) | 0.9188 | 204,840.17 | 0.7891 | ❌ |
| 19 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (medium) | 0.9182 | 55,153.32 | 0.6382 | ❌ |
| 20 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (high) | 0.9136 | 46,948.96 | 0.6197 | ❌ |
| 21 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.3 (xhigh) | 0.9083 | 12,733.17 | 0.4707 | ✅ |
| 22 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (medium with fallback) | 0.9019 | 55,299.37 | 0.6385 | ❌ |
| 23 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (medium) | 0.8956 | 10,667.74 | 0.4507 | ✅ |
| 24 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (max) | 0.8915 | 149,454.21 | 0.7528 | ❌ |
| 25 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.3 (max) | 0.8911 | 12,733.17 | 0.4707 | ❌ |
| 26 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (xhigh with fallback) | 0.8891 | 42,488.51 | 0.6082 | ❌ |
| 27 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (low) | 0.8800 | 48,113.41 | 0.6225 | ❌ |
| 28 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3 (max) | 0.8737 | 41,992.79 | 0.6069 | ❌ |
| 29 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (medium) | 0.8727 | 34,914.82 | 0.5857 | ❌ |
| 30 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (high) | 0.8727 | 21,848.22 | 0.5321 | ❌ |
| 31 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (xhigh) | 0.8725 | 81,006.54 | 0.6823 | ❌ |
| 32 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (low with fallback) | 0.8683 | 45,115.94 | 0.6151 | ❌ |
| 33 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (xhigh) | 0.8648 | 20,982.90 | 0.5275 | ❌ |
| 34 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (xhigh) | 0.8641 | 154,561.97 | 0.7567 | ❌ |
| 35 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (high) | 0.8620 | 23,694.44 | 0.5414 | ❌ |
| 36 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3 (max) | 0.8551 | 14,230.29 | 0.4833 | ❌ |
| 37 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (medium) | 0.8549 | 19,203.07 | 0.5174 | ❌ |
| 38 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (low) | 0.8529 | 8,734.08 | 0.4281 | ✅ |
| 39 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (high) | 0.8527 | 34,327.52 | 0.5838 | ❌ |
| 40 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (xhigh) | 0.8508 | 43,857.07 | 0.6119 | ❌ |
| 41 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.6-Pro | 0.8505 | 2,449.51 | 0.2886 | ✅ |
| 42 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 Max (0902) | 0.8505 | 18,467.55 | 0.5130 | ❌ |
| 43 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (max) | 0.8483 | 202,556.87 | 0.7878 | ❌ |
| 44 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.8 (max) | 0.8473 | 107,489.27 | 0.7149 | ❌ |
| 45 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.7 (xhigh) | 0.8413 | 45,697.13 | 0.6166 | ❌ |
| 46 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (high) | 0.8407 | 61,936.83 | 0.6515 | ❌ |
| 47 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.7 (high) | 0.8400 | 22,779.63 | 0.5369 | ❌ |
| 48 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step 5 Preview | 0.8360 | 7,775.24 | 0.4151 | ❌ |
| 49 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (high) | 0.8325 | 19,664.90 | 0.5201 | ❌ |
| 50 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (high) | 0.8315 | 20,916.52 | 0.5272 | ❌ |
| 51 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (medium) | 0.8298 | — | — | — |
| 52 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (medium) | 0.8289 | 25,934.50 | 0.5517 | ❌ |
| 53 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 Max | 0.8281 | 18,467.55 | 0.5130 | ❌ |
| 54 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (low with fallback) | 0.8227 | 34,076.24 | 0.5829 | ❌ |
| 55 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.2 (xhigh) | 0.8175 | 12,733.17 | 0.4707 | ❌ |
| 56 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3-Flash | 0.8146 | 1,578.56 | 0.2430 | ✅ |
| 57 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 2.4T A95B | 0.8119 | 18,467.55 | 0.5130 | ❌ |
| 58 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (medium) | 0.8084 | — | — | — |
| 59 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (high with fallback) | 0.8075 | 20,455.63 | 0.5246 | ❌ |
| 60 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.7 (max) | 0.8053 | 51,827.17 | 0.6310 | ❌ |
| 61 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (xhigh) | 0.8014 | 271,145.54 | 0.8214 | ❌ |
| 62 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (max) | 0.8001 | 158,622.91 | 0.7596 | ❌ |
| 63 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash | 0.8001 | 35,811.57 | 0.5886 | ❌ |
| 64 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (low) | 0.7977 | 24,383.95 | 0.5447 | ❌ |
| 65 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.5 (high) | 0.7972 | 10,051.75 | 0.4440 | ❌ |
| 66 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (medium) | 0.7927 | 39,625.70 | 0.6002 | ❌ |
| 67 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.2 (max) | 0.7927 | 14,230.29 | 0.4833 | ❌ |
| 68 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (medium) | 0.7906 | 32,442.14 | 0.5773 | ❌ |
| 69 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.3 Codex (xhigh) | 0.7905 | 103,747.23 | 0.7108 | ❌ |
| 70 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (xhigh) | 0.7883 | 38,332.75 | 0.5964 | ❌ |
| 71 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (medium) | 0.7826 | 10,177.71 | 0.4454 | ❌ |
| 72 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.1 Pro Preview | 0.7819 | 44,361.26 | 0.6132 | ❌ |
| 73 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.1 (xhigh) | 0.7660 | — | — | — |
| 74 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (low) | 0.7659 | 20,033.55 | 0.5222 | ❌ |
| 75 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8-Flash-Next | 0.7548 | 1,409.09 | 0.2316 | ✅ |
| 76 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.6 Flash | 0.7523 | 14,807.92 | 0.4878 | ❌ |
| 77 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (high) | 0.7509 | 11,754.14 | 0.4616 | ❌ |
| 78 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.6 (max) | 0.7483 | 35,474.94 | 0.5876 | ❌ |
| 79 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 v2 | 0.7448 | 9,103.98 | 0.4328 | ❌ |
| 80 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (max) | 0.7389 | 15,710.60 | 0.4946 | ❌ |
| 81 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (medium with fallback) | 0.7337 | 9,499.93 | 0.4376 | ❌ |
| 82 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (low) | 0.7335 | 9,813.54 | 0.4413 | ❌ |
| 83 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3 Pro Preview (high) | 0.7328 | — | — | — |
| 84 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (low) | 0.7326 | — | — | — |
| 85 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (low) | 0.7312 | 4,427.16 | 0.3525 | ❌ |
| 86 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (medium) | 0.7308 | 7,602.19 | 0.4126 | ❌ |
| 87 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark | 0.7271 | — | — | — |
| 88 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (low) | 0.7252 | 11,892.36 | 0.4630 | ❌ |
| 89 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro 0813 (max) | 0.7251 | 11,045.48 | 0.4546 | ❌ |
| 90 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (xhigh) | 0.7199 | 130,661.59 | 0.7373 | ❌ |
| 91 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash (max) | 0.7196 | 3,222.55 | 0.3179 | ❌ |
| 92 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 Codex (xhigh) | 0.7194 | — | — | — |
| 93 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 Max Preview | 0.7183 | 21,446.88 | 0.5300 | ❌ |
| 94 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (max) | 0.7182 | 8,940.47 | 0.4308 | ❌ |
| 95 | <img src="https://artificialanalysis.ai/img/logos//img/logos/china-mobile.png" width="18" alt="China Mobile" /> China Mobile | JT-4.1 Flash 236B A21B | 0.7151 | — | — | — |
| 96 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.7 Max | 0.7139 | 27,923.27 | 0.5602 | ❌ |
| 97 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.6 | 0.7085 | 21,840.78 | 0.5321 | ❌ |
| 98 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 | 0.7052 | — | — | — |
| 99 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.5 | 0.7044 | 41,019.80 | 0.6042 | ❌ |
| 100 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (xhigh) | 0.7036 | 8,721.15 | 0.4280 | ❌ |
| 101 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (xhigh) | 0.7012 | 6,563.78 | 0.3961 | ❌ |
| 102 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.7 (Non-reasoning, high) | 0.6993 | 21,943.72 | 0.5326 | ❌ |
| 103 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (low) | 0.6956 | 26,558.93 | 0.5544 | ❌ |
| 104 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash Vision (max) | 0.6890 | 3,675.53 | 0.3322 | ❌ |
| 105 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3 Flash | 0.6887 | 6,069.87 | 0.3874 | ❌ |
| 106 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash 0731 (max) | 0.6859 | 3,675.53 | 0.3322 | ❌ |
| 107 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (max) | 0.6842 | 97,956.02 | 0.7042 | ❌ |
| 108 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (low) | 0.6816 | 13,310.29 | 0.4757 | ❌ |
| 109 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (xhigh) | 0.6792 | 18,598.44 | 0.5138 | ❌ |
| 110 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (medium) | 0.6782 | 11,002.61 | 0.4542 | ❌ |
| 111 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (low with fallback) | 0.6757 | 9,189.09 | 0.4339 | ❌ |
| 112 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M3 | 0.6733 | 3,774.16 | 0.3351 | ❌ |
| 113 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (low) | 0.6733 | 5,514.28 | 0.3768 | ❌ |
| 114 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (xhigh) | 0.6725 | 1,733.85 | 0.2526 | ❌ |
| 115 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.6-Flash | 0.6716 | 803.86 | 0.1780 | ✅ |
| 116 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Pro | 0.6705 | — | — | — |
| 117 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 Plus | 0.6695 | 18,898.80 | 0.5156 | ❌ |
| 118 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.7 Plus | 0.6694 | 4,976.92 | 0.3654 | ❌ |
| 119 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (high) | 0.6659 | 2,749.58 | 0.3009 | ❌ |
| 120 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (medium) | 0.6652 | — | — | — |
| 121 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (max) | 0.6625 | 4,515.76 | 0.3547 | ❌ |
| 122 | <img src="https://artificialanalysis.ai/img/logos//img/logos/motif.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif 3 | 0.6608 | — | — | — |
| 123 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.1 | 0.6567 | 20,631.08 | 0.5256 | ❌ |
| 124 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3 (low) | 0.6542 | 41,992.79 | 0.6069 | ❌ |
| 125 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 Codex (high) | 0.6519 | — | — | — |
| 126 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (high) | 0.6499 | 2,442.55 | 0.2883 | ❌ |
| 127 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (high) | 0.6477 | 11,787.34 | 0.4620 | ❌ |
| 128 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5 | 0.6469 | 13,978.31 | 0.4813 | ❌ |
| 129 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (high) | 0.6463 | 1,352.61 | 0.2275 | ❌ |
| 130 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 (high) | 0.6409 | 46,821.32 | 0.6194 | ❌ |
| 131 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 375B A23B | 0.6406 | — | — | — |
| 132 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (high) | 0.6380 | 15,642.41 | 0.4941 | ❌ |
| 133 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.7 Code | 0.6353 | 13,236.19 | 0.4751 | ❌ |
| 134 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 Codex (high) | 0.6337 | — | — | — |
| 135 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (xhigh) | 0.6279 | 138,018.15 | 0.7436 | ❌ |
| 136 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Omni-0327 | 0.6239 | — | — | — |
| 137 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (medium) | 0.6217 | 40,313.55 | 0.6022 | ❌ |
| 138 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-3.0-flash-VL | 0.6173 | 733.17 | 0.1697 | ✅ |
| 139 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (low) | 0.6152 | 10,957.40 | 0.4537 | ❌ |
| 140 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.6 (Non-reasoning, high) | 0.6144 | 22,569.26 | 0.5358 | ❌ |
| 141 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5-Turbo | 0.6140 | — | — | — |
| 142 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5-Pro | 0.6131 | 2,449.51 | 0.2886 | ❌ |
| 143 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 | 0.6122 | — | — | — |
| 144 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5 | 0.6098 | 803.86 | 0.1780 | ❌ |
| 145 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (max) | 0.6091 | — | — | — |
| 146 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3 (low) | 0.6090 | 14,230.29 | 0.4833 | ❌ |
| 147 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 4 | 0.6076 | 3,732.69 | 0.3339 | ❌ |
| 148 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (high) | 0.6075 | 64,425.57 | 0.6560 | ❌ |
| 149 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (medium) | 0.6073 | — | — | — |
| 150 | <img src="https://artificialanalysis.ai/img/logos//img/logos/thinking-machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling | 0.6069 | 12,283.89 | 0.4666 | ❌ |
| 151 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok Build 0.1 0616 | 0.6043 | 7,442.31 | 0.4102 | ❌ |
| 152 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 Instant (May 2026) | 0.6033 | — | — | — |
| 153 | <img src="https://artificialanalysis.ai/img/logos//img/logos/apodex.svg" width="18" alt="Apodex" /> Apodex | Apodex 1.1 | 0.6032 | — | — | — |
| 154 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Opus | 0.6017 | — | — | — |
| 155 | <img src="https://artificialanalysis.ai/img/logos//img/logos/thinking-machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling Small | 0.6001 | 3,732.69 | 0.3339 | ❌ |
| 156 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Open2 250B | 0.5936 | — | — | — |
| 157 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (minimal) | 0.5923 | 8,454.93 | 0.4245 | ❌ |
| 158 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 27B | 0.5920 | 6,165.87 | 0.3892 | ❌ |
| 159 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash (Feb 2026) | 0.5917 | — | — | — |
| 160 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (xhigh) | 0.5916 | 18,610.50 | 0.5138 | ❌ |
| 161 | <img src="https://artificialanalysis.ai/img/logos//img/logos/multiversecomputing.svg" width="18" alt="Multiverse Computing" /> Multiverse Computing | Quasar 438B (max) | 0.5898 | 4,831.73 | 0.3622 | ❌ |
| 162 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Omni | 0.5895 | — | — | — |
| 163 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o3 | 0.5889 | 14,940.28 | 0.4888 | ❌ |
| 164 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nex.svg" width="18" alt="Nex AGI" /> Nex AGI | Nex-N2-Pro | 0.5887 | — | — | — |
| 165 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (high) | 0.5885 | — | — | — |
| 166 | <img src="https://artificialanalysis.ai/img/logos//img/logos/motif.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif 3 (Beta) | 0.5864 | — | — | — |
| 167 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM 5V Turbo | 0.5851 | — | — | — |
| 168 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 27B | 0.5851 | 22,565.33 | 0.5358 | ❌ |
| 169 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.5 | 0.5831 | — | — | — |
| 170 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Sonnet | 0.5810 | 20,412.77 | 0.5244 | ❌ |
| 171 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (medium) | 0.5795 | 4,126.07 | 0.3448 | ❌ |
| 172 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Ultra | 0.5790 | 8,780.77 | 0.4287 | ❌ |
| 173 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.1 Opus | 0.5770 | — | — | — |
| 174 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (Non-reasoning, high) | 0.5753 | 13,408.04 | 0.4766 | ❌ |
| 175 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 Thinking | 0.5749 | 12,250.00 | 0.4663 | ❌ |
| 176 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.5 (Non-reasoning) | 0.5728 | 22,094.06 | 0.5334 | ❌ |
| 177 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (Non-reasoning, low) | 0.5699 | 13,177.23 | 0.4746 | ❌ |
| 178 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (medium) | 0.5693 | 8,721.15 | 0.4280 | ❌ |
| 179 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 397B A17B | 0.5690 | 13,601.33 | 0.4782 | ❌ |
| 180 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.6 (Non-reasoning) | 0.5677 | 4,744.99 | 0.3602 | ❌ |
| 181 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3 Pro Preview (low) | 0.5666 | — | — | — |
| 182 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash-Lite | 0.5654 | 9,185.82 | 0.4338 | ❌ |
| 183 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (medium) | 0.5642 | 9,068.37 | 0.4324 | ❌ |
| 184 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (medium) | 0.5601 | 1,258.44 | 0.2204 | ❌ |
| 185 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.7 | 0.5589 | 4,328.56 | 0.3501 | ❌ |
| 186 | <img src="https://artificialanalysis.ai/img/logos//img/logos/tencent.svg" width="18" alt="Tencent" /> Tencent | Hy3 | 0.5584 | 1,783.89 | 0.2555 | ❌ |
| 187 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (Non-reasoning) | 0.5582 | 17,867.61 | 0.5092 | ❌ |
| 188 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 Codex mini (high) | 0.5581 | — | — | — |
| 189 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon MoVA 36B A4B | 0.5554 | — | — | — |
| 190 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (low) | 0.5542 | 11,404.40 | 0.4582 | ❌ |
| 191 | <img src="https://artificialanalysis.ai/img/logos//img/logos/tencent.svg" width="18" alt="Tencent" /> Tencent | Hy3-preview | 0.5542 | — | — | — |
| 192 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (low) | 0.5539 | 8,721.15 | 0.4280 | ❌ |
| 193 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.5 | 0.5488 | 3,490.75 | 0.3266 | ❌ |
| 194 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.1 (Non-reasoning) | 0.5477 | 5,853.32 | 0.3834 | ❌ |
| 195 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 Omni Plus | 0.5474 | 3,377.61 | 0.3230 | ❌ |
| 196 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 35B A3B | 0.5436 | 13,471.08 | 0.4771 | ❌ |
| 197 | <img src="https://artificialanalysis.ai/img/logos//img/logos/china-mobile.png" width="18" alt="China Mobile" /> China Mobile | JT-4.1 Flash 236B A21B (non-reasoning) | 0.5424 | — | — | — |
| 198 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (Non-reasoning) | 0.5423 | 8,900.68 | 0.4303 | ❌ |
| 199 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sktelecom.svg" width="18" alt="SK Telecom" /> SK Telecom | A.X-K2 | 0.5413 | — | — | — |
| 200 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.1 Fast | 0.5405 | — | — | — |
| 201 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (Non-reasoning) | 0.5390 | 8,938.51 | 0.4307 | ❌ |
| 202 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano | 0.5346 | 2,131.88 | 0.2740 | ❌ |
| 203 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (high) | 0.5341 | 14,760.65 | 0.4875 | ❌ |
| 204 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.1 | 0.5336 | 3,490.75 | 0.3266 | ❌ |
| 205 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max Thinking | 0.5336 | — | — | — |
| 206 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 122B A10B | 0.5316 | 8,221.15 | 0.4213 | ❌ |
| 207 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 35B A3B | 0.5283 | 5,138.22 | 0.3689 | ❌ |
| 208 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step 3.7 Flash | 0.5278 | 3,363.46 | 0.3226 | ❌ |
| 209 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | G9v3-39A5B | 0.5252 | — | — | — |
| 210 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.5 (Non-reasoning) | 0.5229 | — | — | — |
| 211 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash | 0.5216 | — | — | — |
| 212 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (medium) | 0.5205 | 10,880.96 | 0.4529 | ❌ |
| 213 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3 Flash (Non-reasoning) | 0.5159 | 2,816.66 | 0.3035 | ❌ |
| 214 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7 | 0.5154 | 10,082.93 | 0.4443 | ❌ |
| 215 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 | 0.5131 | — | — | — |
| 216 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kwaikat.svg" width="18" alt="KwaiKAT" /> KwaiKAT | KAT-Coder-Pro V2 | 0.5119 | — | — | — |
| 217 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5 (Non-reasoning) | 0.5117 | 4,398.14 | 0.3518 | ❌ |
| 218 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B | 0.5111 | 3,303.85 | 0.3206 | ❌ |
| 219 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.0 Flash | 0.5106 | 733.17 | 0.1697 | ❌ |
| 220 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 31B | 0.5069 | 0.00 | 0.0000 | ✅ |
| 221 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-3.0-flash-Fin | 0.5059 | 733.17 | 0.1697 | ❌ |
| 222 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (low) | 0.5058 | 1,129.00 | 0.2098 | ❌ |
| 223 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 397B A17B (Non-reasoning) | 0.5049 | 2,848.39 | 0.3047 | ❌ |
| 224 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step 3.5 Flash 2603 | 0.5048 | 994.23 | 0.1977 | ❌ |
| 225 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (low) | 0.5037 | 538.10 | 0.1433 | ❌ |
| 226 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Sonnet | 0.5032 | — | — | — |
| 227 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (low) | 0.4986 | 9,067.72 | 0.4324 | ❌ |
| 228 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 Fast | 0.4984 | — | — | — |
| 229 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Glimmer (high) | 0.4983 | 3,932.57 | 0.3395 | ❌ |
| 230 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (Non-reasoning) | 0.4939 | 24,728.20 | 0.5463 | ❌ |
| 231 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 3 mini Reasoning (high) | 0.4914 | 2,124.40 | 0.2736 | ❌ |
| 232 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 27B (Non-reasoning) | 0.4901 | 2,492.27 | 0.2904 | ❌ |
| 233 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Sonnet (Non-reasoning) | 0.4897 | 13,117.82 | 0.4741 | ❌ |
| 234 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Speciale | 0.4888 | — | — | — |
| 235 | <img src="https://artificialanalysis.ai/img/logos//img/logos/china-mobile.png" width="18" alt="China Mobile" /> China Mobile | JT-35B-Flash | 0.4879 | — | — | — |
| 236 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step 3.5 Flash | 0.4870 | 994.23 | 0.1977 | ❌ |
| 237 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE 2.0 | 0.4851 | — | — | — |
| 238 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 Instant (June 2026) | 0.4819 | 82,487.98 | 0.6844 | ❌ |
| 239 | <img src="https://artificialanalysis.ai/img/logos//img/logos/cohere.svg" width="18" alt="Cohere" /> Cohere | Command A+ | 0.4798 | 0.00 | 0.0000 | ❌ |
| 240 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-2.6-1T | 0.4773 | 6,415.87 | 0.3936 | ❌ |
| 241 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash (Non-reasoning) | 0.4750 | 1,069.73 | 0.2047 | ❌ |
| 242 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (Non-reasoning) | 0.4747 | 12,175.77 | 0.4656 | ❌ |
| 243 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2 | 0.4744 | 3,165.87 | 0.3160 | ❌ |
| 244 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Pro | 0.4734 | 33,745.21 | 0.5818 | ❌ |
| 245 | <img src="https://artificialanalysis.ai/img/logos//img/logos/bytedance.svg" width="18" alt="ByteDance Seed" /> ByteDance Seed | Doubao Seed Code | 0.4710 | — | — | — |
| 246 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o4-mini (high) | 0.4707 | 22,905.47 | 0.5375 | ❌ |
| 247 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o1 | 0.4707 | — | — | — |
| 248 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3.5 | 0.4698 | 20,996.39 | 0.5276 | ❌ |
| 249 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 7B | 0.4668 | — | — | — |
| 250 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Haiku | 0.4608 | 11,386.82 | 0.4581 | ❌ |
| 251 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (Non-reasoning) | 0.4595 | 825.91 | 0.1805 | ❌ |
| 252 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (Non-reasoning) | 0.4558 | 10,066.02 | 0.4441 | ❌ |
| 253 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.7 Sonnet | 0.4553 | — | — | — |
| 254 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Sonnet (Non-reasoning) | 0.4524 | — | — | — |
| 255 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (medium) | 0.4497 | 28,638.61 | 0.5631 | ❌ |
| 256 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.2 (Non-reasoning) | 0.4473 | 6,325.36 | 0.3920 | ❌ |
| 257 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Sep) | 0.4469 | — | — | — |
| 258 | <img src="https://artificialanalysis.ai/img/logos//img/logos/longcat.svg" width="18" alt="LongCat" /> LongCat | LongCat 2.0 | 0.4464 | — | — | — |
| 259 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 27B (Non-reasoning) | 0.4459 | 2,880.45 | 0.3059 | ❌ |
| 260 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Exp | 0.4425 | — | — | — |
| 261 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kwaikat.svg" width="18" alt="KwaiKAT" /> KwaiKAT | KAT-Coder-Pro V1 | 0.4417 | — | — | — |
| 262 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.1 Flash-Lite | 0.4416 | 3,296.35 | 0.3204 | ❌ |
| 263 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (Non-reasoning) | 0.4402 | 10,399.27 | 0.4478 | ❌ |
| 264 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 Terminus | 0.4381 | — | — | — |
| 265 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.7 Sonnet (Non-reasoning) | 0.4320 | — | — | — |
| 266 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max Thinking (Preview) | 0.4311 | 17,930.77 | 0.5096 | ❌ |
| 267 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (low) | 0.4308 | 25,691.11 | 0.5506 | ❌ |
| 268 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 122B A10B (Non-reasoning) | 0.4278 | 2,863.93 | 0.3052 | ❌ |
| 269 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash | 0.4260 | 11,962.54 | 0.4636 | ❌ |
| 270 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (medium) | 0.4258 | 6,415.87 | 0.3936 | ❌ |
| 271 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5-Pro (Non-reasoning) | 0.4209 | 756.75 | 0.1726 | ❌ |
| 272 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Haiku (Non-reasoning) | 0.4207 | 4,394.86 | 0.3517 | ❌ |
| 273 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 9B | 0.4195 | 574.64 | 0.1487 | ❌ |
| 274 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 0905 | 0.4180 | 1,760.95 | 0.2542 | ❌ |
| 275 | <img src="https://artificialanalysis.ai/img/logos//img/logos/baidu.svg" width="18" alt="Baidu" /> Baidu | ERNIE 5.0 Thinking Preview | 0.4174 | — | — | — |
| 276 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (Non-reasoning) | 0.4167 | — | — | — |
| 277 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 235B A22B (Reasoning) | 0.4166 | 10,221.15 | 0.4459 | ❌ |
| 278 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 26B A4B | 0.4155 | — | — | — |
| 279 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 (Non-reasoning) | 0.4142 | — | — | — |
| 280 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-2.6-1T | 0.4138 | — | — | — |
| 281 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (low) | 0.4103 | — | — | — |
| 282 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 (Non-reasoning) | 0.4081 | — | — | — |
| 283 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.5 33B | 0.4070 | — | — | — |
| 284 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 4B | 0.4063 | 391.59 | 0.1185 | ❌ |
| 285 | <img src="https://artificialanalysis.ai/img/logos//img/logos/tencent.svg" width="18" alt="Tencent" /> Tencent | Hy3-preview (Non-reasoning) | 0.4062 | — | — | — |
| 286 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (high) | 0.4062 | 4,968.76 | 0.3652 | ❌ |
| 287 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (high) | 0.4051 | 6,415.87 | 0.3936 | ❌ |
| 288 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (medium) | 0.4041 | 2,976.03 | 0.3094 | ❌ |
| 289 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7 (Non-reasoning) | 0.4032 | 4,292.22 | 0.3491 | ❌ |
| 290 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (medium) | 0.4020 | — | — | — |
| 291 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 v2 (Non-reasoning) | 0.3981 | 3,973.87 | 0.3407 | ❌ |
| 292 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 35B A3B (Non-reasoning) | 0.3956 | 2,002.10 | 0.2674 | ❌ |
| 293 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 12B | 0.3955 | 805.29 | 0.1782 | ❌ |
| 294 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 | 0.3946 | — | — | — |
| 295 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5 | 0.3940 | — | — | — |
| 296 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max | 0.3882 | 4,381.60 | 0.3514 | ❌ |
| 297 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-2B | 0.3874 | — | — | — |
| 298 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok Code Fast 1 | 0.3854 | — | — | — |
| 299 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (Non-reasoning) | 0.3853 | 4,057.37 | 0.3430 | ❌ |
| 300 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 | 0.3844 | 1,652.49 | 0.2477 | ❌ |
| 301 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 0528 | 0.3830 | — | — | — |
| 302 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE | 0.3822 | — | — | — |
| 303 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro 0813 (Non-reasoning) | 0.3821 | 4,753.42 | 0.3603 | ❌ |
| 304 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6 | 0.3820 | 6,843.27 | 0.4008 | ❌ |
| 305 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inceptionlabs.svg" width="18" alt="Inception" /> Inception | Mercury 2 | 0.3811 | 3,235.64 | 0.3184 | ❌ |
| 306 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 31B (Non-reasoning) | 0.3789 | 1,631.92 | 0.2464 | ❌ |
| 307 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (Non-reasoning) | 0.3783 | 467.81 | 0.1321 | ❌ |
| 308 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Sep) (Non-reasoning) | 0.3773 | — | — | — |
| 309 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (Non-reasoning) | 0.3749 | 1,015.42 | 0.1997 | ❌ |
| 310 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (minimal) | 0.3746 | 7,869.15 | 0.4164 | ❌ |
| 311 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 32B (Reasoning) | 0.3736 | 1,688.46 | 0.2499 | ❌ |
| 312 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 3.7B | 0.3735 | — | — | — |
| 313 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Super | 0.3732 | 3,832.93 | 0.3367 | ❌ |
| 314 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 | 0.3726 | 10,844.22 | 0.4525 | ❌ |
| 315 | <img src="https://artificialanalysis.ai/img/logos//img/logos/arcee.svg" width="18" alt="Arcee AI" /> Arcee AI | Trinity Large Thinking | 0.3719 | 2,705.05 | 0.2991 | ❌ |
| 316 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.2 30B | 0.3716 | 2,091.35 | 0.2720 | ❌ |
| 317 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 (Non-reasoning) | 0.3709 | 7,873.93 | 0.4165 | ❌ |
| 318 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (low) | 0.3706 | 6,415.87 | 0.3936 | ❌ |
| 319 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 9B (Non-reasoning) | 0.3696 | — | — | — |
| 320 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7-Flash | 0.3695 | 1,133.17 | 0.2102 | ❌ |
| 321 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6 (Non-reasoning) | 0.3660 | 5,117.12 | 0.3685 | ❌ |
| 322 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 35B A3B (Non-reasoning) | 0.3658 | 1,798.98 | 0.2564 | ❌ |
| 323 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3.5 Lightning | 0.3647 | 1,061.06 | 0.2039 | ❌ |
| 324 | <img src="https://artificialanalysis.ai/img/logos//img/logos/servicenow.svg" width="18" alt="ServiceNow" /> ServiceNow | Apriel-v1.5-15B-Thinker | 0.3622 | — | — | — |
| 325 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.0 Tiny | 0.3606 | 0.00 | 0.0000 | ❌ |
| 326 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B A22B 2507 | 0.3603 | 5,877.16 | 0.3838 | ❌ |
| 327 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 Omni Flash | 0.3582 | 777.54 | 0.1750 | ❌ |
| 328 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder 480B | 0.3572 | 5,865.16 | 0.3836 | ❌ |
| 329 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Sep) | 0.3562 | — | — | — |
| 330 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron Cascade 2 30B A3B | 0.3561 | — | — | — |
| 331 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepcogito.png" width="18" alt="Deep Cogito" /> Deep Cogito | Cogito v2.1 | 0.3559 | — | — | — |
| 332 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Magistral Medium 1.2 | 0.3529 | — | — | — |
| 333 | <img src="https://artificialanalysis.ai/img/logos//img/logos/servicenow.svg" width="18" alt="ServiceNow" /> ServiceNow | Apriel-v1.6-15B-Thinker | 0.3519 | — | — | — |
| 334 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 26B A4B (Non-reasoning) | 0.3508 | 1,262.17 | 0.2207 | ❌ |
| 335 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | G9v3-3B | 0.3506 | — | — | — |
| 336 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 3 | 0.3503 | — | — | — |
| 337 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6V | 0.3495 | 4,092.73 | 0.3439 | ❌ |
| 338 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 Terminus (Non-reasoning) | 0.3488 | — | — | — |
| 339 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-120b (high) | 0.3479 | 2,751.32 | 0.3009 | ❌ |
| 340 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (ChatGPT) | 0.3447 | — | — | — |
| 341 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash (Non-reasoning) | 0.3400 | — | — | — |
| 342 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max (Preview) | 0.3376 | 7,297.89 | 0.4080 | ❌ |
| 343 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Small 4 | 0.3346 | 1,724.64 | 0.2520 | ❌ |
| 344 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Exp (Non-reasoning) | 0.3312 | — | — | — |
| 345 | <img src="https://artificialanalysis.ai/img/logos//img/logos/multiversecomputing.svg" width="18" alt="Multiverse Computing" /> Multiverse Computing | HyperNova 60B 2605 (high) | 0.3294 | — | — | — |
| 346 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Sep) (Non-reasoning) | 0.3288 | — | — | — |
| 347 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 (Non-reasoning) | 0.3280 | — | — | — |
| 348 | <img src="https://artificialanalysis.ai/img/logos//img/logos/cohere.svg" width="18" alt="Cohere" /> Cohere | North Mini Code | 0.3252 | 0.00 | 0.0000 | ❌ |
| 349 | <img src="https://artificialanalysis.ai/img/logos//img/logos/bytedance.svg" width="18" alt="ByteDance Seed" /> ByteDance Seed | Seed-OSS-36B-Instruct | 0.3242 | 1,541.11 | 0.2406 | ❌ |
| 350 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o3-mini (high) | 0.3217 | 27,876.03 | 0.5600 | ❌ |
| 351 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o (Nov) | 0.3207 | 21,989.44 | 0.5329 | ❌ |
| 352 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Non-reasoning) | 0.3185 | 1,914.51 | 0.2628 | ❌ |
| 353 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.2 8B | 0.3183 | 799.88 | 0.1776 | ❌ |
| 354 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 3 | 0.3174 | 1,724.64 | 0.2520 | ❌ |
| 355 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o (Aug) | 0.3172 | 19,227.99 | 0.5176 | ❌ |
| 356 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B 2507 | 0.3167 | 720.23 | 0.1682 | ❌ |
| 357 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Think V2 | 0.3160 | — | — | — |
| 358 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite | 0.3142 | 3,112.29 | 0.3142 | ❌ |
| 359 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.1 Fast (Non-reasoning) | 0.3105 | — | — | — |
| 360 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Next 80B A3B (Reasoning) | 0.3096 | 3,082.93 | 0.3132 | ❌ |
| 361 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (minimal) | 0.3096 | 1,575.30 | 0.2428 | ❌ |
| 362 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 12B (Non-reasoning) | 0.3083 | 291.30 | 0.0978 | ❌ |
| 363 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 235B A22B | 0.3077 | 1,247.95 | 0.2196 | ❌ |
| 364 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano | 0.3076 | 1,000.00 | 0.1982 | ❌ |
| 365 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | QwQ-32B | 0.3059 | — | — | — |
| 366 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-1T | 0.3048 | — | — | — |
| 367 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-1B | 0.3048 | — | — | — |
| 368 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-1B (Non-reasoning) | 0.3046 | — | — | — |
| 369 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Pixtral Large | 0.3034 | — | — | — |
| 370 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Open 100B | 0.3001 | — | — | — |
| 371 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 4B (Non-reasoning) | 0.2979 | 94.85 | 0.0416 | ❌ |
| 372 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder Next | 0.2973 | 4,225.04 | 0.3474 | ❌ |
| 373 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o3-mini | 0.2972 | 13,344.03 | 0.4760 | ❌ |
| 374 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5-Air | 0.2966 | 2,543.99 | 0.2926 | ❌ |
| 375 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax M1 80k | 0.2964 | — | — | — |
| 376 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inceptionlabs.svg" width="18" alt="Inception" /> Inception | Mercury 2.5 | 0.2963 | 2,466.89 | 0.2893 | ❌ |
| 377 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 E4B | 0.2956 | 261.06 | 0.0907 | ❌ |
| 378 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (Non-reasoning) | 0.2941 | 6,844.76 | 0.4008 | ❌ |
| 379 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (Non-reasoning) | 0.2938 | 1,078.14 | 0.2054 | ❌ |
| 380 | <img src="https://artificialanalysis.ai/img/logos//img/logos/china-mobile.png" width="18" alt="China Mobile" /> China Mobile | JT-MINI | 0.2918 | — | — | — |
| 381 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | DiffusionGemma 26B A4B | 0.2910 | — | — | — |
| 382 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3 | 0.2900 | — | — | — |
| 383 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax M1 40k | 0.2895 | — | — | — |
| 384 | <img src="https://artificialanalysis.ai/img/logos//img/logos/naver.webp" width="18" alt="Naver" /> Naver | HyperCLOVA X SEED Think (32B) | 0.2894 | — | — | — |
| 385 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 Fast (Non-reasoning) | 0.2877 | — | — | — |
| 386 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (high) | 0.2872 | — | — | — |
| 387 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE (Non-reasoning) | 0.2869 | — | — | — |
| 388 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3 0324 | 0.2857 | — | — | — |
| 389 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (Non-reasoning) | 0.2854 | 4,057.13 | 0.3430 | ❌ |
| 390 | <img src="https://artificialanalysis.ai/img/logos//img/logos/korea-telecom.png" width="18" alt="Korea Telecom" /> Korea Telecom | Mi:dm K 2.5 Pro | 0.2842 | — | — | — |
| 391 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 (Jan) | 0.2832 | — | — | — |
| 392 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Large 3 | 0.2826 | 1,621.60 | 0.2458 | ❌ |
| 393 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 4 Maverick | 0.2812 | 2,994.00 | 0.3100 | ❌ |
| 394 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3.1 | 0.2802 | — | — | — |
| 395 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-20b (high) | 0.2781 | 488.70 | 0.1355 | ❌ |
| 396 | <img src="https://artificialanalysis.ai/img/logos//img/logos/prime-intellect.svg" width="18" alt="Prime Intellect" /> Prime Intellect | INTELLECT-3 | 0.2774 | — | — | — |
| 397 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano Omni 30B A3B | 0.2769 | 4,687.50 | 0.3588 | ❌ |
| 398 | <img src="https://artificialanalysis.ai/img/logos//img/logos/trillionlabs.svg" width="18" alt="Trillion Labs" /> Trillion Labs | Tri-21B-think Preview | 0.2766 | — | — | — |
| 399 | <img src="https://artificialanalysis.ai/img/logos//img/logos/longcat.svg" width="18" alt="LongCat" /> LongCat | LongCat Flash Lite | 0.2749 | — | — | — |
| 400 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 30B A3B (Reasoning) | 0.2746 | 6,110.58 | 0.3882 | ❌ |
| 401 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B A3B 2507 | 0.2746 | 6,110.58 | 0.3882 | ❌ |
| 402 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-20b (low) | 0.2742 | 576.20 | 0.1490 | ❌ |
| 403 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.1 405B | 0.2731 | — | — | — |
| 404 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova Premier | 0.2722 | — | — | — |
| 405 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 2.6 Flash | 0.2716 | — | — | — |
| 406 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 mini | 0.2715 | 2,143.50 | 0.2746 | ❌ |
| 407 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 E4B (Non-reasoning) | 0.2711 | 66.45 | 0.0307 | ❌ |
| 408 | <img src="https://artificialanalysis.ai/img/logos//img/logos/trillionlabs.svg" width="18" alt="Trillion Labs" /> Trillion Labs | Tri-21B-Think | 0.2709 | — | — | — |
| 409 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.2 3B | 0.2659 | 387.44 | 0.1177 | ❌ |
| 410 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (Non-reasoning) | 0.2637 | 1,864.33 | 0.2601 | ❌ |
| 411 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Next 80B A3B | 0.2630 | 1,124.55 | 0.2095 | ❌ |
| 412 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 32B | 0.2627 | 519.76 | 0.1405 | ❌ |
| 413 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nousresearch.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 405B | 0.2610 | 8,052.88 | 0.4190 | ❌ |
| 414 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (medium) | 0.2585 | — | — | — |
| 415 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-1T | 0.2577 | — | — | — |
| 416 | <img src="https://artificialanalysis.ai/img/logos//img/logos/korea-telecom.png" width="18" alt="Korea Telecom" /> Korea Telecom | Mi:dm K 2.5 Pro Preview | 0.2573 | — | — | — |
| 417 | <img src="https://artificialanalysis.ai/img/logos//img/logos/motif.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif-2-12.7B | 0.2571 | — | — | — |
| 418 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-120b (low) | 0.2568 | 2,862.50 | 0.3052 | ❌ |
| 419 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.5 Haiku | 0.2544 | — | — | — |
| 420 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 8B (Reasoning) | 0.2540 | 5,349.52 | 0.3734 | ❌ |
| 421 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step3 VL 10B | 0.2523 | — | — | — |
| 422 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Super 49B v1.5 | 0.2501 | — | — | — |
| 423 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.0 Flash | 0.2499 | — | — | — |
| 424 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7-Flash (Non-reasoning) | 0.2497 | 670.45 | 0.1619 | ❌ |
| 425 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Devstral 2 | 0.2479 | — | — | — |
| 426 | <img src="https://artificialanalysis.ai/img/logos//img/logos/baidu.svg" width="18" alt="Baidu" /> Baidu | ERNIE 4.5 300B A47B | 0.2470 | — | — | — |
| 427 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Magistral Medium 1 | 0.2460 | — | — | — |
| 428 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Devstral Medium | 0.2444 | — | — | — |
| 429 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B 2507 | 0.2439 | — | — | — |
| 430 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (Non-reasoning) | 0.2433 | — | — | — |
| 431 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4 | 0.2433 | — | — | — |
| 432 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Small 4 (Non-reasoning) | 0.2428 | 600.76 | 0.1525 | ❌ |
| 433 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nousresearch.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 405B (Non-reasoning) | 0.2417 | 2,343.07 | 0.2839 | ❌ |
| 434 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder 30B A3B | 0.2404 | 1,844.43 | 0.2589 | ❌ |
| 435 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-8B-A1B | 0.2381 | — | — | — |
| 436 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 30B A3B | 0.2372 | 708.61 | 0.1667 | ❌ |
| 437 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6V (Non-reasoning) | 0.2367 | 2,512.66 | 0.2913 | ❌ |
| 438 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 E2B | 0.2353 | — | — | — |
| 439 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Omni 30B A3B (Reasoning) | 0.2348 | 2,563.22 | 0.2934 | ❌ |
| 440 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-2.6B | 0.2331 | — | — | — |
| 441 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B | 0.2307 | 21,387.02 | 0.5297 | ❌ |
| 442 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5V | 0.2300 | 5,870.91 | 0.3837 | ❌ |
| 443 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 12B v2 VL | 0.2293 | — | — | — |
| 444 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Large 2 (Nov) | 0.2283 | — | — | — |
| 445 | <img src="https://artificialanalysis.ai/img/logos//img/logos/tii.svg" width="18" alt="TII UAE" /> TII UAE | Falcon-H1R-7B | 0.2268 | — | — | — |
| 446 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Ultra | 0.2258 | — | — | — |
| 447 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Devstral Small 2 | 0.2246 | — | — | — |
| 448 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3 (Dec) | 0.2181 | — | — | — |
| 449 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova Pro | 0.2168 | — | — | — |
| 450 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nanbeige.png" width="18" alt="Nanbeige" /> Nanbeige | Nanbeige4.1-3B | 0.2166 | — | — | — |
| 451 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3.1 32B Think | 0.2160 | — | — | — |
| 452 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3.2 | 0.2157 | — | — | — |
| 453 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam 105B (high) | 0.2151 | — | — | — |
| 454 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.0 32B | 0.2142 | — | — | — |
| 455 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Magistral Small 1.2 | 0.2137 | — | — | — |
| 456 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (low) | 0.2127 | — | — | — |
| 457 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 9B V2 | 0.2122 | 422.12 | 0.1241 | ❌ |
| 458 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 2B | 0.2122 | — | — | — |
| 459 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-flash-2.0 | 0.2096 | — | — | — |
| 460 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Non-reasoning) | 0.2096 | 384.85 | 0.1172 | ❌ |
| 461 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Super 49B v1.5 (Non-reasoning) | 0.2080 | — | — | — |
| 462 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 4 Scout | 0.2071 | 520.76 | 0.1406 | ❌ |
| 463 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nousresearch.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 70B | 0.2059 | — | — | — |
| 464 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Devstral Small (May) | 0.2049 | — | — | — |
| 465 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 32B | 0.2045 | 1,688.46 | 0.2499 | ❌ |
| 466 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova Lite | 0.2043 | 334.00 | 0.1070 | ❌ |
| 467 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.3 Nemotron Super 49B | 0.2012 | — | — | — |
| 468 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 32B | 0.2009 | — | — | — |
| 469 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen2.5 72B | 0.2002 | — | — | — |
| 470 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 14B | 0.1995 | 10,693.51 | 0.4510 | ❌ |
| 471 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-flash-2.0 | 0.1994 | 369.31 | 0.1142 | ❌ |
| 472 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 8B | 0.1988 | 631.91 | 0.1568 | ❌ |
| 473 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B | 0.1973 | 6,110.58 | 0.3882 | ❌ |
| 474 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Magistral Small 1 | 0.1969 | — | — | — |
| 475 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Large 2 (Jul) | 0.1929 | — | — | — |
| 476 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Ministral 3 14B | 0.1924 | 414.91 | 0.1228 | ❌ |
| 477 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 2 | 0.1921 | — | — | — |
| 478 | <img src="https://artificialanalysis.ai/img/logos//img/logos/cohere.svg" width="18" alt="Cohere" /> Cohere | Command A | 0.1921 | 7,417.22 | 0.4098 | ❌ |
| 479 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Devstral Small | 0.1914 | — | — | — |
| 480 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B (Non-reasoning) | 0.1912 | 2,235.10 | 0.2789 | ❌ |
| 481 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.1 Nemotron 70B | 0.1899 | — | — | — |
| 482 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano 4B | 0.1885 | — | — | — |
| 483 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 4B (Reasoning) | 0.1873 | — | — | — |
| 484 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3 Haiku | 0.1862 | — | — | — |
| 485 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3.1 | 0.1853 | — | — | — |
| 486 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.3 Nemotron Super 49B (Non-reasoning) | 0.1847 | — | — | — |
| 487 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B A3B 2507 (Non-reasoning) | 0.1829 | 728.26 | 0.1692 | ❌ |
| 488 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B | 0.1815 | — | — | — |
| 489 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.1 70B | 0.1809 | 649.85 | 0.1592 | ❌ |
| 490 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 9B V2 (Non-reasoning) | 0.1807 | 193.49 | 0.0732 | ❌ |
| 491 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 32B (Non-reasoning) | 0.1792 | 578.59 | 0.1493 | ❌ |
| 492 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5V (Non-reasoning) | 0.1788 | 2,511.61 | 0.2912 | ❌ |
| 493 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 E2B (Non-reasoning) | 0.1787 | — | — | — |
| 494 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 2B (Non-reasoning) | 0.1770 | — | — | — |
| 495 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.1 30B | 0.1765 | — | — | — |
| 496 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3.1 32B Instruct | 0.1733 | — | — | — |
| 497 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Omni 30B A3B | 0.1716 | 801.41 | 0.1777 | ❌ |
| 498 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (minimal) | 0.1709 | 328.57 | 0.1059 | ❌ |
| 499 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B 2507 (Non-reasoning) | 0.1698 | — | — | — |
| 500 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.1 8B | 0.1680 | 42.39 | 0.0205 | ❌ |
| 501 | <img src="https://artificialanalysis.ai/img/logos//img/logos/celeris.svg" width="18" alt="Celeris" /> Celeris | Celeris-1 | 0.1658 | 1,066.33 | 0.2044 | ❌ |
| 502 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 32B Think | 0.1656 | — | — | — |
| 503 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o mini | 0.1652 | 1,149.56 | 0.2116 | ❌ |
| 504 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Llama 70B | 0.1648 | — | — | — |
| 505 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 nano | 0.1647 | 537.84 | 0.1433 | ❌ |
| 506 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.3 70B | 0.1646 | 7,560.68 | 0.4119 | ❌ |
| 507 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 14B | 0.1644 | — | — | — |
| 508 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi Linear 48B A3B Instruct | 0.1641 | — | — | — |
| 509 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Ministral 3 8B | 0.1627 | 311.47 | 0.1022 | ❌ |
| 510 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 2 (Non-reasoning) | 0.1627 | — | — | — |
| 511 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nousresearch.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 70B (Non-reasoning) | 0.1595 | — | — | — |
| 512 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai21.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba Reasoning 3B | 0.1592 | — | — | — |
| 513 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.0 32B (Non-reasoning) | 0.1570 | — | — | — |
| 514 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.1 8B | 0.1570 | — | — | — |
| 515 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova Micro | 0.1541 | 202.76 | 0.0758 | ❌ |
| 516 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 24B A2B | 0.1537 | — | — | — |
| 517 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai21.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba 1.7 Large | 0.1526 | — | — | — |
| 518 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 8B | 0.1519 | 5,349.52 | 0.3734 | ❌ |
| 519 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam 30B (high) | 0.1507 | — | — | — |
| 520 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3 | 0.1493 | — | — | — |
| 521 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 12B v2 VL (Non-reasoning) | 0.1490 | 546.24 | 0.1445 | ❌ |
| 522 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM-V 4.6 1.3B | 0.1488 | — | — | — |
| 523 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B (Non-reasoning) | 0.1445 | 705.39 | 0.1663 | ❌ |
| 524 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano (Non-reasoning) | 0.1418 | 632.18 | 0.1568 | ❌ |
| 525 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H Small | 0.1387 | 282.67 | 0.0958 | ❌ |
| 526 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 4B | 0.1383 | — | — | — |
| 527 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 27B | 0.1363 | — | — | — |
| 528 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 0528 Qwen3 8B | 0.1342 | — | — | — |
| 529 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Ministral 3 3B | 0.1328 | 214.87 | 0.0790 | ❌ |
| 530 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 14B (Non-reasoning) | 0.1325 | 1,135.83 | 0.2104 | ❌ |
| 531 | <img src="https://artificialanalysis.ai/img/logos//img/logos/microsoft.svg" width="18" alt="Microsoft" /> Microsoft | Phi-4 | 0.1278 | 370.88 | 0.1145 | ❌ |
| 532 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.1 Nemotron Nano 4B v1.1 | 0.1270 | — | — | — |
| 533 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 270M | 0.1248 | — | — | — |
| 534 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3 70B | 0.1197 | — | — | — |
| 535 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.2 11B (Vision) | 0.1192 | 375.09 | 0.1153 | ❌ |
| 536 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.2 3B | 0.1173 | — | — | — |
| 537 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 0.8B | 0.1164 | — | — | — |
| 538 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 7B Think | 0.1158 | — | — | — |
| 539 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-1.2B-Instruct | 0.1092 | — | — | — |
| 540 | <img src="https://artificialanalysis.ai/img/logos//img/logos/reka.svg" width="18" alt="Reka AI" /> Reka AI | Reka Flash 3 | 0.1087 | — | — | — |
| 541 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-mini-2.0 | 0.1083 | — | — | — |
| 542 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 2.6B | 0.1082 | — | — | — |
| 543 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 8B (Non-reasoning) | 0.1073 | 563.68 | 0.1471 | ❌ |
| 544 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Molmo2-8B | 0.1040 | — | — | — |
| 545 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam M | 0.1037 | — | — | — |
| 546 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai21.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba 1.7 Mini | 0.1025 | — | — | — |
| 547 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-1.2B-Thinking | 0.1011 | — | — | — |
| 548 | <img src="https://artificialanalysis.ai/img/logos//img/logos/microsoft.svg" width="18" alt="Microsoft" /> Microsoft | Phi-4 Mini | 0.0987 | 0.00 | 0.0000 | ❌ |
| 549 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 12B | 0.0985 | — | — | — |
| 550 | <img src="https://artificialanalysis.ai/img/logos//img/logos/swiss-ai-initiative.png" width="18" alt="Swiss AI Initiative" /> Swiss AI Initiative | Apertus 70B Instruct | 0.0942 | — | — | — |
| 551 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 0.8B (Non-reasoning) | 0.0939 | — | — | — |
| 552 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 7B | 0.0928 | — | — | — |
| 553 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | Exaone 4.0 1.2B | 0.0918 | — | — | — |
| 554 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | OLMo 2 32B | 0.0917 | — | — | — |
| 555 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H 1B | 0.0912 | — | — | — |
| 556 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.2 1B | 0.0901 | — | — | — |
| 557 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 1.7B | 0.0890 | — | — | — |
| 558 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.1 3B | 0.0873 | — | — | — |
| 559 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | Exaone 4.0 1.2B (Non-reasoning) | 0.0848 | — | — | — |
| 560 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 8B A1B | 0.0830 | — | — | — |
| 561 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 Micro | 0.0804 | — | — | — |
| 562 | <img src="https://artificialanalysis.ai/img/logos//img/logos/microsoft.svg" width="18" alt="Microsoft" /> Microsoft | Phi-3 Mini | 0.0754 | — | — | — |
| 563 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 3.3 8B | 0.0720 | — | — | — |
| 564 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-VL-1.6B | 0.0694 | — | — | — |
| 565 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 1B | 0.0687 | — | — | — |
| 566 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 350M | 0.0677 | — | — | — |
| 567 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 4B | 0.0668 | — | — | — |
| 568 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 1.2B | 0.0658 | — | — | — |
| 569 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 0.6B | 0.0652 | — | — | — |
| 570 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3 8B | 0.0649 | — | — | — |
| 571 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral 7B | 0.0625 | — | — | — |
| 572 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3n E4B | 0.0588 | — | — | — |
| 573 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 0.9B | 0.0577 | — | — | — |
| 574 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 1.7B (Non-reasoning) | 0.0570 | — | — | — |
| 575 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | OLMo 2 7B | 0.0568 | — | — | — |
| 576 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 1B | 0.0564 | — | — | — |
| 577 | <img src="https://artificialanalysis.ai/img/logos//img/logos/swiss-ai-initiative.png" width="18" alt="Swiss AI Initiative" /> Swiss AI Initiative | Apertus 8B Instruct | 0.0555 | — | — | — |
| 578 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H 350M | 0.0512 | — | — | — |
| 579 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Molmo 7B-D | 0.0480 | — | — | — |
| 580 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 0.6B (Non-reasoning) | 0.0440 | — | — | — |
| 581 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3n E2B | 0.0363 | — | — | — |
| 582 | <img src="https://artificialanalysis.ai/img/logos//img/logos/cohere.svg" width="18" alt="Cohere" /> Cohere | Tiny Aya Global | 0.0359 | — | — | — |
| 583 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 1.5B | 0.0000 | — | — | — |

## 品牌帕累托前沿连线（仅体现在图中）

以下十一个品牌在图中拥有单独的帕累托连线（较窄宽度，品牌主题色，图层高于总体灰色连线）。表中数量为**入图顶点数**——品牌前沿上低于总体前沿第一级的顶点同样不入图（本表与图例一致）：

| 品牌 | 主题色 | 品牌前沿模型数（入图） |
|------|--------|--------------|
| <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | `#cc785c` | 13 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | `#1f1f1f` | 11 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | `#0089f4` | 2 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | `#1c7ff8` | 2 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | `#34A853` | 6 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | `#736cd3` | 6 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | `#047AFE` | 5 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | `#ff7018` | 3 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | `#2243e6` | 3 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | `#EB3568` | 2 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | `#ff6900` | 3 |

## 评分方法

1. **20项评估指标**各自线性归一化到 [0,1]
   （AA Intelligence Index、GPQA Diamond、Humanity's Last Exam、MMMU Pro、IFBench Instruction Following、SciCode Coding、CritPt Physics、AA-LCR Long Context、AA Omniscience Index、AA-Omniscience Accuracy、AA-Omniscience Non-Hallucination、GDPval-AA Normalized、AA Analyst Agent、APEX-Agents-AA、ITBench-SRE、τ²-Bench Telecom、τ³-Bench Banking、Terminal-Bench Hard、Terminal-Bench 2.1、Terminal-Bench 4.0）
   > V18（2026-09-12）：AA 更新了基准列——新增 AA Analyst Agent、τ³-Bench Banking、Terminal-Bench 2.1 / 4.0 四项；AA Agentic Index 与 AA Coding Index 已从 AA 的数据源中移除，相应剔除。指标数由 18 → 20。
2. **综合能力值** = 所有有效归一化分数的算术平均
3. **综合能力再归一化**：线性映射到 [0,1]，性能最好的模型 = 1，最差的模型 = 0
4. **Pareto前沿** = 不被任何其他模型支配的模型（综合能力 ≥ 且成本 ≤，且至少一项严格更优；成本为 0 的免费模型同样参与——横轴左端恒为 0，免费模型是合法前沿候选）
5. **模型范围** = Status: All（含已弃用模型；缺少足够评估数据者不参与排名）
6. **图表纵轴基线（V17）**：图表的 y = 0 取总体帕累托前沿的第一级（最低能力；本例 y0 = 0.5069，即前沿左端点 Gemma 4 31B）；综合能力低于该级的模型不出现在图表中（表格不受影响）。图中纵坐标 chart_y = (能力 - y0)/(1 - y0)，因此前沿左端点恰好落在 (0, 0)、最优模型恰好为 y = 1。该过滤在横轴映射构建之前完成


## 横轴映射（对数映射，真零点，V21）与分布分析

横轴（单请求成本）为 **Y = A·ln(B·c+C)+D 对数映射**（B = 1；A、D 由端点解出；C = 218.14，r = B/C = 0.0045842 经网格搜索确定）：

```
x = 0                            当 c = 0（免费模型，真零点）
x = A·ln(c+C)+D                  当 c > 0（B = 1 并入；A、D 由端点解出）
```

其中 C = 218.14（r = B/C = 0.0045842），拟合集为 11 品牌前沿入图正成本模型（综合能力 ≥ 前沿第一级）的成本分布，目标为组内名次分位数（最小二乘误差 mse = 0.020522，最大偏离 0.2476）。该映射在 **y 基线过滤之后**构建（V17：先以帕累托前沿第一级为 y = 0、剔除低性能模型，再对入图模型建映射）。

**该映射保证：**

- **函数端点严格钉死**：c = 0 → x = 0；最大成本 → x = 1——函数经过 (0,0) 与 (1,1)；
- 各数量级区间的入图模型数：1–10: 0，10–100: 0，100–1k: 4，1k–10k: 56，10k–100k: 93，100k–1M: 19，1M–1.278M: 1
- **同倍率区间宽度相近**（对数轴性质）：1k→10k 与 100k→1M 同为 10 倍率，宽度相近（前者 56 个模型、后者 19 个）；与 V17 分位数映射不同，本图不追求均匀密度——密度不等如实显示；
- **左端恒为 0**（c = 0；1 个免费模型位于最左缘）
- 前沿最低正成本 803.86 → x = 0.1780（真实对数位置，不再钉 0；x = 0 恒为 c = 0 免费模型）；前沿最大成本 1,278,065 → x = 1.0000（= 1；高于前沿最大成本的模型不入图，仅表格保留）
- 中位数位置 0.483（≈ 0.5 居中）；左右两半模型数：左 93 / 右 82
- 横轴十分位模型数：1，4，10，27，51，35，24，15，4，4（对数映射下各十分位模型数自然不等）
- **10^x 数量级指示**（位置 = x(10^x)）：10^0 → 0.001，10^1 → 0.005，10^2 → 0.043，10^3 → 0.198，10^4 → 0.443，10^5 → 0.707，10^6 → 0.972

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
| CacheHitRate | [AA Coding Agents](https://artificialanalysis.ai/agents/coding-agents) | 全部模型-Agent搭配的 `cacheHitRate` 求平均（30 个有效值，均值 = 0.9447），对所有模型统一使用 |
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
**模型总数（Status: All）**: 583 个参与排名（另有模型因评估数据不足未列入；总体帕累托前沿 15 个；图表入图 175 个——综合能力 ≥ 前沿第一级）  

## 图表说明（黑底）

（V17 起本说明置于文末，图表之后直接跟随模型表格。）

图表说明：**灰色实线** = 总体帕累托前沿；**彩色细线** = 十一个品牌的单独帕累托前沿（品牌主题色，图层高于总体连线；暗色品牌元素带窄白边；顶点按（横轴位置、能力升序）连接，等成本点自下而上）；品牌前沿模型圆点同样使用品牌颜色。模型名称/思考程度标注优先骑在连线之上（点的左/右两侧皆可，同一条线段可容纳两个标签——各贴各的点；文字与连线平行、中轴线重合，连线仅在文字两侧绘制）；骑线位被其他标签占据时自动「让位」——占用者挪到自己的另一个骑线位，双方都保持骑线；实在骑不上线时按四级优先依次退让（V16）：离点最近位置的上方/下方平行偏移 → 点的两条连线延长线上就近 → 两连线夹角扇区内就近。标签规则（V13/V15）：品牌前沿模型共享的前导块按「最长有效切点」剔除 —— 切点止于分界符，或止于字母且其后紧跟数字（如 Claude Opus 5 → Opus 5、GPT-5.6 Sol → 5.6 Sol、Kimi K2.6 → 2.6、Qwen3.8 Max → 3.8 Max、MiMo-V2.5 → 2.5、MiniMax-M2.1 → 2.1）；(non-reasoning) 简写为 (non)；同一模型在品牌连线上相邻出现 2 次以上时仅性能最低者保留全名、相邻较高者只标思考程度，不相邻的重复出现保留全名（每次重新计算）；标签位置与序列同向（V15）——品牌前沿上越靠右上的模型，其标签重心必须同时更靠右且更靠上（两分量都 >= 0，至少是 (0,0)，仅其一非负不算合格；初始放置违反时自动就近重摆，单标签无解（被前后邻居夹死）时按窗口级联重排整体挪动，均不产生新的重叠）。纵轴 y = 0 = 总体帕累托前沿第一级（y0 = 0.5069，前沿左端点 Gemma 4 31B 恰为 (0,0)），能力低于该级的 363 个模型、缺少成本数据的 45 个模型与成本高于品牌前沿最大值的模型不出现在图中；横轴为对数映射（见上文「横轴映射」节），10^x 数量级指示位于 x(10^x)，同一倍率区间的宽度相近（对数轴性质；本图不追求均匀密度）。
