# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

## 全部模型（综合能力从高到低，最优 = 1，最差 = 0）

共收录 **Status: All**（含已弃用）的全部模型；按重新归一化后的综合能力排序。「帕累托」列：✅ = 总体帕累托前沿模型，❌ = 被支配，— = 无成本数据无法判定。图表纵轴以总体帕累托前沿第一级（y0 = 0.4990，即前沿左端点 Gemma 4 31B）为 0：综合能力 ≥ 该级且有成本数据的 161 个模型入图，363 个能力低于第一级、44 个缺少成本数据的模型不出现在图中，成本高于品牌前沿最大值的模型同样不入图（本表不受影响，仍完整列出全部模型）。

| # | 品牌 | 模型 | 综合能力 | 单请求成本 | 横轴位置 | 帕累托 |
|---|------|------|---------|-----------|-----------|------|
| 1 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (max with fallback) | 1.0000 | — | — | — |
| 2 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (xhigh with fallback) | 0.9702 | 311,565.23 | 0.9086 | ✅ |
| 3 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (max with fallback) | 0.9556 | 1,056,224.17 | 1.0000 | ❌ |
| 4 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (xhigh with fallback) | 0.9419 | 426,057.01 | 0.9518 | ❌ |
| 5 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (xhigh) | 0.9331 | 604,195.41 | 1.0000 | ❌ |
| 6 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (max) | 0.9322 | 1,034,876.57 | 1.0000 | ❌ |
| 7 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (high with fallback) | 0.9312 | 86,409.53 | 0.7320 | ✅ |
| 8 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (max) | 0.9168 | 96,305.25 | 0.7469 | ❌ |
| 9 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (high) | 0.9144 | 239,882.64 | 0.8726 | ❌ |
| 10 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (high with fallback) | 0.9105 | 106,885.58 | 0.7612 | ❌ |
| 11 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5 (with fallback) | 0.9101 | 412,047.36 | 0.9472 | ❌ |
| 12 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (xhigh) | 0.9047 | 60,662.11 | 0.6834 | ✅ |
| 13 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (medium with fallback) | 0.9034 | 50,910.77 | 0.6594 | ✅ |
| 14 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (max) | 0.8953 | 220,195.99 | 0.8607 | ❌ |
| 15 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (medium) | 0.8947 | 55,758.75 | 0.6718 | ❌ |
| 16 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.3 (max) | 0.8910 | 12,678.34 | 0.4708 | ✅ |
| 17 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (high) | 0.8902 | 47,639.37 | 0.6503 | ❌ |
| 18 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.3 (xhigh) | 0.8857 | 12,678.34 | 0.4708 | ✅ |
| 19 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (medium with fallback) | 0.8789 | 61,519.42 | 0.6853 | ❌ |
| 20 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (max) | 0.8616 | 204,976.10 | 0.8509 | ❌ |
| 21 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (low) | 0.8575 | 47,482.50 | 0.6498 | ❌ |
| 22 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3 (max) | 0.8514 | 41,858.20 | 0.6326 | ❌ |
| 23 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (medium) | 0.8504 | 27,277.50 | 0.5742 | ❌ |
| 24 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (xhigh) | 0.8502 | 71,424.66 | 0.7058 | ❌ |
| 25 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (low with fallback) | 0.8461 | 53,229.28 | 0.6655 | ❌ |
| 26 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (xhigh) | 0.8427 | 26,268.02 | 0.5691 | ❌ |
| 27 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (xhigh) | 0.8420 | 205,154.43 | 0.8510 | ❌ |
| 28 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (high) | 0.8397 | 23,791.22 | 0.5556 | ❌ |
| 29 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (high) | 0.8378 | 18,300.69 | 0.5201 | ❌ |
| 30 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (medium) | 0.8330 | 19,065.60 | 0.5256 | ❌ |
| 31 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (high) | 0.8309 | 41,976.63 | 0.6330 | ❌ |
| 32 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3 (max) | 0.8297 | 14,173.46 | 0.4857 | ❌ |
| 33 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (xhigh) | 0.8290 | 67,046.34 | 0.6971 | ❌ |
| 34 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.6-Pro | 0.8283 | 2,428.01 | 0.2606 | ✅ |
| 35 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (max) | 0.8266 | 245,876.41 | 0.8760 | ❌ |
| 36 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 Max (0902) | 0.8266 | 18,380.31 | 0.5207 | ❌ |
| 37 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.8 (max) | 0.8256 | 73,906.55 | 0.7105 | ❌ |
| 38 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.7 (xhigh) | 0.8225 | 8,959.79 | 0.4247 | ❌ |
| 39 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (high) | 0.8188 | 79,330.75 | 0.7202 | ❌ |
| 40 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.7 (high) | 0.8185 | 9,022.72 | 0.4257 | ❌ |
| 41 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (high) | 0.8112 | 15,197.66 | 0.4951 | ❌ |
| 42 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step 5 Preview | 0.8108 | 7,727.88 | 0.4053 | ❌ |
| 43 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (high) | 0.8102 | 19,160.49 | 0.5263 | ❌ |
| 44 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (medium) | 0.8086 | — | — | — |
| 45 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (medium) | 0.8077 | 22,537.80 | 0.5483 | ❌ |
| 46 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 Max | 0.8069 | 18,380.31 | 0.5207 | ❌ |
| 47 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (low with fallback) | 0.8016 | 25,305.94 | 0.5640 | ❌ |
| 48 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.2 (xhigh) | 0.7966 | 12,678.34 | 0.4708 | ❌ |
| 49 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 2.4T A95B | 0.7911 | 18,380.31 | 0.5207 | ❌ |
| 50 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (medium) | 0.7877 | 10,402.52 | 0.4445 | ❌ |
| 51 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.7 (max) | 0.7847 | 53,037.34 | 0.6650 | ❌ |
| 52 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (xhigh) | 0.7809 | 316,674.04 | 0.9109 | ❌ |
| 53 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (max) | 0.7796 | 127,191.49 | 0.7851 | ❌ |
| 54 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash | 0.7796 | 44,823.39 | 0.6419 | ❌ |
| 55 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (low) | 0.7773 | 24,204.31 | 0.5579 | ❌ |
| 56 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3-Flash | 0.7773 | 1,572.38 | 0.2115 | ✅ |
| 57 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.5 (high) | 0.7768 | 10,472.14 | 0.4454 | ❌ |
| 58 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (medium) | 0.7725 | 38,308.94 | 0.6205 | ❌ |
| 59 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.2 (max) | 0.7724 | 14,173.46 | 0.4857 | ❌ |
| 60 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (medium) | 0.7704 | 30,777.30 | 0.5906 | ❌ |
| 61 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.3 Codex (xhigh) | 0.7703 | 120,693.92 | 0.7779 | ❌ |
| 62 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (xhigh) | 0.7681 | 48,679.29 | 0.6532 | ❌ |
| 63 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (medium) | 0.7626 | 8,426.08 | 0.4167 | ❌ |
| 64 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.1 Pro Preview | 0.7619 | 48,554.82 | 0.6529 | ❌ |
| 65 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.1 (xhigh) | 0.7464 | — | — | — |
| 66 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (low) | 0.7463 | 20,738.10 | 0.5370 | ❌ |
| 67 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8-Flash-Next | 0.7355 | 1,402.41 | 0.1993 | ✅ |
| 68 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.6 Flash | 0.7331 | 15,940.71 | 0.5015 | ❌ |
| 69 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (high) | 0.7317 | 12,368.24 | 0.4675 | ❌ |
| 70 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.6 (max) | 0.7291 | 43,194.79 | 0.6369 | ❌ |
| 71 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 v2 | 0.7257 | 10,051.33 | 0.4399 | ❌ |
| 72 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sapiens.svg" width="18" alt="Sapiens AI" /> Sapiens AI | Agnes 3.0 Flash | 0.7216 | — | — | — |
| 73 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (max) | 0.7200 | 20,771.39 | 0.5372 | ❌ |
| 74 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (low) | 0.7147 | 10,198.62 | 0.4419 | ❌ |
| 75 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3 Pro Preview (high) | 0.7140 | — | — | — |
| 76 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (low) | 0.7138 | — | — | — |
| 77 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (low) | 0.7125 | 4,066.82 | 0.3231 | ❌ |
| 78 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (medium) | 0.7121 | 7,158.50 | 0.3953 | ❌ |
| 79 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark | 0.7085 | — | — | — |
| 80 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (low) | 0.7066 | 11,363.55 | 0.4562 | ❌ |
| 81 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro 0813 (max) | 0.7066 | 10,981.87 | 0.4517 | ❌ |
| 82 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (xhigh) | 0.7014 | 200,946.46 | 0.8481 | ❌ |
| 83 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 Codex (xhigh) | 0.7009 | — | — | — |
| 84 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 Max Preview | 0.6999 | 21,388.55 | 0.5412 | ❌ |
| 85 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (max) | 0.6999 | 12,392.34 | 0.4678 | ❌ |
| 86 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sapiens.svg" width="18" alt="Sapiens AI" /> Sapiens AI | Agnes 2.5 Pro Beta | 0.6963 | — | — | — |
| 87 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.7 Max | 0.6956 | 27,823.57 | 0.5769 | ❌ |
| 88 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.6 | 0.6904 | 21,801.40 | 0.5438 | ❌ |
| 89 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 | 0.6872 | — | — | — |
| 90 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.5 | 0.6864 | 44,235.48 | 0.6401 | ❌ |
| 91 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (xhigh) | 0.6856 | 8,701.21 | 0.4209 | ❌ |
| 92 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (xhigh) | 0.6832 | 7,810.87 | 0.4067 | ❌ |
| 93 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash (max) | 0.6823 | 3,207.89 | 0.2939 | ❌ |
| 94 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.7 (Non-reasoning, high) | 0.6814 | 21,880.11 | 0.5443 | ❌ |
| 95 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (low) | 0.6778 | 26,113.30 | 0.5682 | ❌ |
| 96 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash Vision (max) | 0.6714 | 3,654.29 | 0.3098 | ❌ |
| 97 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3 Flash | 0.6711 | 6,261.38 | 0.3780 | ❌ |
| 98 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash 0731 (max) | 0.6684 | 3,654.29 | 0.3098 | ❌ |
| 99 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (max) | 0.6667 | 111,246.86 | 0.7667 | ❌ |
| 100 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (low) | 0.6642 | 13,871.34 | 0.4828 | ❌ |
| 101 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (xhigh) | 0.6618 | 31,615.16 | 0.5943 | ❌ |
| 102 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (medium) | 0.6609 | 11,065.62 | 0.4527 | ❌ |
| 103 | <img src="https://artificialanalysis.ai/img/logos//img/logos/motif_small.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif 3 | 0.6603 | — | — | — |
| 104 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3 (low) | 0.6598 | 41,858.20 | 0.6326 | ❌ |
| 105 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M3 | 0.6561 | 3,758.46 | 0.3133 | ❌ |
| 106 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (low) | 0.6561 | 5,728.35 | 0.3665 | ❌ |
| 107 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (xhigh) | 0.6553 | 2,117.06 | 0.2447 | ❌ |
| 108 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Pro | 0.6534 | — | — | — |
| 109 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 Plus | 0.6524 | 18,876.37 | 0.5243 | ❌ |
| 110 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.7 Plus | 0.6522 | 4,960.97 | 0.3481 | ❌ |
| 111 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (high) | 0.6489 | 3,262.35 | 0.2959 | ❌ |
| 112 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (medium) | 0.6482 | — | — | — |
| 113 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (max) | 0.6455 | 4,494.26 | 0.3356 | ❌ |
| 114 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.1 | 0.6399 | 20,579.98 | 0.5360 | ❌ |
| 115 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 Codex (high) | 0.6352 | — | — | — |
| 116 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (high) | 0.6333 | 2,421.05 | 0.2602 | ❌ |
| 117 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (high) | 0.6311 | 10,148.77 | 0.4412 | ❌ |
| 118 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5 | 0.6303 | 13,938.43 | 0.4835 | ❌ |
| 119 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (high) | 0.6298 | 990.54 | 0.1642 | ✅ |
| 120 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 (high) | 0.6245 | 48,599.01 | 0.6530 | ❌ |
| 121 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm_small.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 375B A23B | 0.6242 | — | — | — |
| 122 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (high) | 0.6217 | 14,613.53 | 0.4898 | ❌ |
| 123 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.7 Code | 0.6191 | 13,198.31 | 0.4762 | ❌ |
| 124 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 Codex (high) | 0.6175 | — | — | — |
| 125 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (xhigh) | 0.6119 | 139,475.72 | 0.7978 | ❌ |
| 126 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Omni-0327 | 0.6079 | — | — | — |
| 127 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (medium) | 0.6058 | 31,053.42 | 0.5918 | ❌ |
| 128 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-3.0-flash-VL | 0.6015 | 730.18 | 0.1363 | ✅ |
| 129 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (low) | 0.5995 | 10,791.41 | 0.4494 | ❌ |
| 130 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.6 (Non-reasoning, high) | 0.5987 | 22,563.94 | 0.5484 | ❌ |
| 131 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5-Turbo | 0.5983 | — | — | — |
| 132 | <img src="https://artificialanalysis.ai/img/logos//img/logos/thinking_machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling Small | 0.5978 | 3,720.73 | 0.3121 | ❌ |
| 133 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5-Pro | 0.5974 | 2,428.01 | 0.2606 | ❌ |
| 134 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 | 0.5965 | — | — | — |
| 135 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5 | 0.5942 | 797.02 | 0.1440 | ❌ |
| 136 | <img src="https://artificialanalysis.ai/img/logos//img/logos/apodex.svg" width="18" alt="Apodex" /> Apodex | Apodex 1.1 | 0.5939 | — | — | — |
| 137 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (max) | 0.5935 | — | — | — |
| 138 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 4 | 0.5920 | 3,720.73 | 0.3121 | ❌ |
| 139 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (high) | 0.5919 | 74,652.87 | 0.7119 | ❌ |
| 140 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (medium) | 0.5917 | 784.60 | 0.1426 | ❌ |
| 141 | <img src="https://artificialanalysis.ai/img/logos//img/logos/thinking_machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling | 0.5913 | 12,242.52 | 0.4661 | ❌ |
| 142 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (high) | 0.5909 | — | — | — |
| 143 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok Build 0.1 0616 | 0.5889 | 7,402.43 | 0.3997 | ❌ |
| 144 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 Instant (May 2026) | 0.5879 | — | — | — |
| 145 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Opus | 0.5863 | — | — | — |
| 146 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Open2 250B | 0.5784 | — | — | — |
| 147 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (minimal) | 0.5771 | 8,389.00 | 0.4161 | ❌ |
| 148 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 27B | 0.5769 | 6,150.91 | 0.3757 | ❌ |
| 149 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash (Feb 2026) | 0.5765 | — | — | — |
| 150 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (xhigh) | 0.5765 | 24,364.14 | 0.5588 | ❌ |
| 151 | <img src="https://artificialanalysis.ai/img/logos//img/logos/multiversecomputing_small.svg" width="18" alt="Multiverse Computing" /> Multiverse Computing | Quasar 438B (max) | 0.5747 | 4,801.82 | 0.3440 | ❌ |
| 152 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Omni | 0.5744 | — | — | — |
| 153 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o3 | 0.5738 | 17,331.67 | 0.5128 | ❌ |
| 154 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nex_small.svg" width="18" alt="Nex AGI" /> Nex AGI | Nex-N2-Pro | 0.5737 | — | — | — |
| 155 | <img src="https://artificialanalysis.ai/img/logos//img/logos/motif_small.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif 3 (Beta) | 0.5714 | — | — | — |
| 156 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM 5V Turbo | 0.5701 | — | — | — |
| 157 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 27B | 0.5701 | 22,535.42 | 0.5483 | ❌ |
| 158 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.5 | 0.5682 | — | — | — |
| 159 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Sonnet | 0.5661 | 20,870.25 | 0.5379 | ❌ |
| 160 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (medium) | 0.5647 | 4,244.64 | 0.3285 | ❌ |
| 161 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Ultra | 0.5642 | 8,758.84 | 0.4218 | ❌ |
| 162 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.1 Opus | 0.5623 | — | — | — |
| 163 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (Non-reasoning, high) | 0.5606 | 13,036.46 | 0.4745 | ❌ |
| 164 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 Thinking | 0.5602 | 6,551.82 | 0.3838 | ❌ |
| 165 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.5 (Non-reasoning) | 0.5581 | 21,785.68 | 0.5437 | ❌ |
| 166 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (Non-reasoning, low) | 0.5553 | 13,249.65 | 0.4767 | ❌ |
| 167 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (medium) | 0.5548 | 8,701.21 | 0.4209 | ❌ |
| 168 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 397B A17B | 0.5545 | 13,571.42 | 0.4799 | ❌ |
| 169 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.6 (Non-reasoning) | 0.5532 | 4,450.79 | 0.3344 | ❌ |
| 170 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3 Pro Preview (low) | 0.5521 | — | — | — |
| 171 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash-Lite | 0.5509 | 9,358.60 | 0.4305 | ❌ |
| 172 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (medium) | 0.5497 | 9,713.71 | 0.4354 | ❌ |
| 173 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sktelecom_small.svg" width="18" alt="SK Telecom" /> SK Telecom | A.X-K2 | 0.5457 | — | — | — |
| 174 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (medium) | 0.5454 | 1,316.63 | 0.1927 | ❌ |
| 175 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.7 | 0.5446 | 4,312.86 | 0.3305 | ❌ |
| 176 | <img src="https://artificialanalysis.ai/img/logos//img/logos/tencent_small.svg" width="18" alt="Tencent" /> Tencent | Hy3 | 0.5441 | 1,852.82 | 0.2296 | ❌ |
| 177 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (Non-reasoning) | 0.5439 | 17,848.62 | 0.5167 | ❌ |
| 178 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 Codex mini (high) | 0.5439 | — | — | — |
| 179 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm_small.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon MoVA 36B A4B | 0.5412 | — | — | — |
| 180 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (low) | 0.5401 | 14,530.14 | 0.4891 | ❌ |
| 181 | <img src="https://artificialanalysis.ai/img/logos//img/logos/tencent_small.svg" width="18" alt="Tencent" /> Tencent | Hy3-preview | 0.5400 | — | — | — |
| 182 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (low) | 0.5398 | 8,701.21 | 0.4209 | ❌ |
| 183 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.5 | 0.5348 | 3,473.55 | 0.3036 | ❌ |
| 184 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.1 (Non-reasoning) | 0.5337 | 5,697.16 | 0.3658 | ❌ |
| 185 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 Omni Plus | 0.5334 | 3,372.47 | 0.3000 | ❌ |
| 186 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 35B A3B | 0.5297 | 13,452.39 | 0.4787 | ❌ |
| 187 | <img src="https://artificialanalysis.ai/img/logos//img/logos/china_mobile_small.png" width="18" alt="China Mobile" /> China Mobile | JT-4.1 Flash 236B A21B | 0.5285 | — | — | — |
| 188 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (Non-reasoning) | 0.5284 | 8,843.98 | 0.4230 | ❌ |
| 189 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.1 Fast | 0.5267 | — | — | — |
| 190 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (Non-reasoning) | 0.5252 | 9,170.11 | 0.4278 | ❌ |
| 191 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.0 Flash | 0.5234 | 730.18 | 0.1363 | ❌ |
| 192 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sapiens.svg" width="18" alt="Sapiens AI" /> Sapiens AI | Agnes 2.5 Pro Alpha | 0.5217 | 2,571.34 | 0.2673 | ❌ |
| 193 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano | 0.5209 | 1,809.56 | 0.2269 | ❌ |
| 194 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (high) | 0.5204 | 21,871.02 | 0.5442 | ❌ |
| 195 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.1 | 0.5200 | 3,150.91 | 0.2917 | ❌ |
| 196 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max Thinking | 0.5199 | — | — | — |
| 197 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 122B A10B | 0.5180 | 8,201.21 | 0.4131 | ❌ |
| 198 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 35B A3B | 0.5147 | 5,125.76 | 0.3523 | ❌ |
| 199 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step 3.7 Flash | 0.5143 | 3,355.49 | 0.2993 | ❌ |
| 200 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | G9v3-39A5B | 0.5117 | — | — | — |
| 201 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.5 (Non-reasoning) | 0.5095 | — | — | — |
| 202 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash | 0.5083 | — | — | — |
| 203 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (medium) | 0.5072 | 9,484.85 | 0.4323 | ❌ |
| 204 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3 Flash (Non-reasoning) | 0.5027 | 2,824.48 | 0.2785 | ❌ |
| 205 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7 | 0.5022 | 11,500.00 | 0.4578 | ❌ |
| 206 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 | 0.5000 | — | — | — |
| 207 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 31B | 0.4990 | 0.00 | 0.0000 | ✅ |
| 208 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kwaikat_small.svg" width="18" alt="KwaiKAT" /> KwaiKAT | KAT-Coder-Pro V2 | 0.4988 | — | — | — |
| 209 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5 (Non-reasoning) | 0.4986 | 4,314.39 | 0.3305 | ❌ |
| 210 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B | 0.4980 | 3,272.45 | 0.2963 | ❌ |
| 211 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-3.0-flash-Fin | 0.4929 | 730.18 | 0.1363 | ❌ |
| 212 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (low) | 0.4929 | 1,181.60 | 0.1816 | ❌ |
| 213 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 397B A17B (Non-reasoning) | 0.4920 | 2,772.28 | 0.2763 | ❌ |
| 214 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step 3.5 Flash 2603 | 0.4919 | 990.24 | 0.1642 | ❌ |
| 215 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (low) | 0.4908 | 574.82 | 0.1165 | ❌ |
| 216 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Sonnet | 0.4903 | — | — | — |
| 217 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (low) | 0.4859 | 9,308.59 | 0.4298 | ❌ |
| 218 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 Fast | 0.4857 | — | — | — |
| 219 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Glimmer (high) | 0.4856 | 4,305.94 | 0.3303 | ❌ |
| 220 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (Non-reasoning) | 0.4813 | 24,782.47 | 0.5611 | ❌ |
| 221 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 3 mini Reasoning (high) | 0.4788 | 2,113.18 | 0.2445 | ❌ |
| 222 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 27B (Non-reasoning) | 0.4775 | 2,446.13 | 0.2614 | ❌ |
| 223 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Sonnet (Non-reasoning) | 0.4772 | 12,967.93 | 0.4738 | ❌ |
| 224 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Speciale | 0.4763 | — | — | — |
| 225 | <img src="https://artificialanalysis.ai/img/logos//img/logos/china_mobile_small.png" width="18" alt="China Mobile" /> China Mobile | JT-35B-Flash | 0.4754 | — | — | — |
| 226 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step 3.5 Flash | 0.4746 | 800.30 | 0.1444 | ❌ |
| 227 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE 2.0 | 0.4727 | — | — | — |
| 228 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 Instant (June 2026) | 0.4695 | 82,263.66 | 0.7252 | ❌ |
| 229 | <img src="https://artificialanalysis.ai/img/logos//img/logos/cohere_small.svg" width="18" alt="Cohere" /> Cohere | Command A+ | 0.4675 | 0.00 | 0.0000 | ❌ |
| 230 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-2.6-1T | 0.4651 | 6,400.91 | 0.3808 | ❌ |
| 231 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (Non-reasoning) | 0.4625 | 12,232.30 | 0.4660 | ❌ |
| 232 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2 | 0.4622 | 3,150.91 | 0.2917 | ❌ |
| 233 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Pro | 0.4613 | 37,139.57 | 0.6162 | ❌ |
| 234 | <img src="https://artificialanalysis.ai/img/logos//img/logos/bytedance_small.svg" width="18" alt="ByteDance Seed" /> ByteDance Seed | Doubao Seed Code | 0.4590 | — | — | — |
| 235 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o4-mini (high) | 0.4587 | 24,683.71 | 0.5606 | ❌ |
| 236 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o1 | 0.4587 | — | — | — |
| 237 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3.5 | 0.4578 | 20,929.10 | 0.5382 | ❌ |
| 238 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm_small.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 7B | 0.4549 | — | — | — |
| 239 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Haiku | 0.4490 | 16,663.14 | 0.5075 | ❌ |
| 240 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (Non-reasoning) | 0.4478 | 801.40 | 0.1445 | ❌ |
| 241 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (Non-reasoning) | 0.4442 | 10,016.62 | 0.4395 | ❌ |
| 242 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.7 Sonnet | 0.4437 | — | — | — |
| 243 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Sonnet (Non-reasoning) | 0.4409 | — | — | — |
| 244 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (medium) | 0.4381 | 28,591.85 | 0.5806 | ❌ |
| 245 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.2 (Non-reasoning) | 0.4358 | 6,225.70 | 0.3772 | ❌ |
| 246 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Sep) | 0.4354 | — | — | — |
| 247 | <img src="https://artificialanalysis.ai/img/logos//img/logos/longcat_small.svg" width="18" alt="LongCat" /> LongCat | LongCat 2.0 | 0.4350 | — | — | — |
| 248 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 27B (Non-reasoning) | 0.4345 | 2,864.28 | 0.2802 | ❌ |
| 249 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Exp | 0.4312 | — | — | — |
| 250 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kwaikat_small.svg" width="18" alt="KwaiKAT" /> KwaiKAT | KAT-Coder-Pro V1 | 0.4304 | — | — | — |
| 251 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.1 Flash-Lite | 0.4303 | 3,731.12 | 0.3124 | ❌ |
| 252 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (Non-reasoning) | 0.4289 | 10,551.52 | 0.4464 | ❌ |
| 253 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 Terminus | 0.4269 | — | — | — |
| 254 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.7 Sonnet (Non-reasoning) | 0.4210 | — | — | — |
| 255 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max Thinking (Preview) | 0.4201 | 17,882.91 | 0.5170 | ❌ |
| 256 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (low) | 0.4198 | 25,628.79 | 0.5657 | ❌ |
| 257 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 122B A10B (Non-reasoning) | 0.4169 | 2,878.87 | 0.2808 | ❌ |
| 258 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash | 0.4151 | 11,225.09 | 0.4546 | ❌ |
| 259 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (medium) | 0.4149 | 6,400.91 | 0.3808 | ❌ |
| 260 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 9B | 0.4137 | 567.91 | 0.1156 | ❌ |
| 261 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5-Pro (Non-reasoning) | 0.4101 | 884.03 | 0.1535 | ❌ |
| 262 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Haiku (Non-reasoning) | 0.4099 | 4,354.94 | 0.3317 | ❌ |
| 263 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 0905 | 0.4073 | 1,684.97 | 0.2190 | ❌ |
| 264 | <img src="https://artificialanalysis.ai/img/logos//img/logos/baidu_small.svg" width="18" alt="Baidu" /> Baidu | ERNIE 5.0 Thinking Preview | 0.4067 | — | — | — |
| 265 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (Non-reasoning) | 0.4060 | — | — | — |
| 266 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 235B A22B (Reasoning) | 0.4060 | 10,201.21 | 0.4419 | ❌ |
| 267 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 26B A4B | 0.4049 | — | — | — |
| 268 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 (Non-reasoning) | 0.4036 | — | — | — |
| 269 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-2.6-1T | 0.4032 | — | — | — |
| 270 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (low) | 0.3998 | — | — | — |
| 271 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 (Non-reasoning) | 0.3976 | — | — | — |
| 272 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.5 33B | 0.3966 | — | — | — |
| 273 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 4B | 0.3959 | 390.09 | 0.0886 | ❌ |
| 274 | <img src="https://artificialanalysis.ai/img/logos//img/logos/tencent_small.svg" width="18" alt="Tencent" /> Tencent | Hy3-preview (Non-reasoning) | 0.3958 | — | — | — |
| 275 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (high) | 0.3958 | 6,914.55 | 0.3908 | ❌ |
| 276 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (high) | 0.3947 | 6,400.91 | 0.3808 | ❌ |
| 277 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (medium) | 0.3938 | 2,987.70 | 0.2852 | ❌ |
| 278 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.0 Tiny | 0.3930 | 0.00 | 0.0000 | ❌ |
| 279 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7 (Non-reasoning) | 0.3929 | 6,632.65 | 0.3854 | ❌ |
| 280 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (medium) | 0.3918 | — | — | — |
| 281 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 v2 (Non-reasoning) | 0.3879 | 3,939.93 | 0.3192 | ❌ |
| 282 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 35B A3B (Non-reasoning) | 0.3854 | 1,948.74 | 0.2353 | ❌ |
| 283 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 12B | 0.3854 | 800.30 | 0.1444 | ❌ |
| 284 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 | 0.3845 | — | — | — |
| 285 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5 | 0.3839 | — | — | — |
| 286 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max | 0.3783 | 4,326.33 | 0.3309 | ❌ |
| 287 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openbmb_small.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-2B | 0.3774 | — | — | — |
| 288 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok Code Fast 1 | 0.3755 | — | — | — |
| 289 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (Non-reasoning) | 0.3754 | 3,982.44 | 0.3205 | ❌ |
| 290 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 | 0.3745 | 1,598.88 | 0.2133 | ❌ |
| 291 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 0528 | 0.3732 | — | — | — |
| 292 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE | 0.3724 | — | — | — |
| 293 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6 | 0.3723 | 11,000.00 | 0.4519 | ❌ |
| 294 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inceptionlabs_small.svg" width="18" alt="Inception" /> Inception | Mercury 2 | 0.3713 | 3,412.11 | 0.3014 | ❌ |
| 295 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 31B (Non-reasoning) | 0.3692 | 1,634.37 | 0.2157 | ❌ |
| 296 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (Non-reasoning) | 0.3687 | 458.64 | 0.0996 | ❌ |
| 297 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Sep) (Non-reasoning) | 0.3676 | — | — | — |
| 298 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (Non-reasoning) | 0.3653 | 1,045.00 | 0.1694 | ❌ |
| 299 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (minimal) | 0.3650 | 7,825.89 | 0.4070 | ❌ |
| 300 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 32B (Reasoning) | 0.3641 | 1,680.49 | 0.2188 | ❌ |
| 301 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm_small.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 3.7B | 0.3640 | — | — | — |
| 302 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Super | 0.3636 | 3,825.46 | 0.3155 | ❌ |
| 303 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 | 0.3630 | 10,897.19 | 0.4506 | ❌ |
| 304 | <img src="https://artificialanalysis.ai/img/logos//img/logos/arcee_small.svg" width="18" alt="Arcee AI" /> Arcee AI | Trinity Large Thinking | 0.3624 | 2,375.76 | 0.2580 | ❌ |
| 305 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.2 30B | 0.3621 | 2,085.36 | 0.2430 | ❌ |
| 306 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 (Non-reasoning) | 0.3615 | 7,917.07 | 0.4085 | ❌ |
| 307 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (low) | 0.3611 | 6,400.91 | 0.3808 | ❌ |
| 308 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 9B (Non-reasoning) | 0.3602 | 227.71 | 0.0583 | ❌ |
| 309 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7-Flash | 0.3601 | 1,700.00 | 0.2200 | ❌ |
| 310 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6 (Non-reasoning) | 0.3566 | 1,710.47 | 0.2207 | ❌ |
| 311 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 35B A3B (Non-reasoning) | 0.3564 | 1,773.29 | 0.2247 | ❌ |
| 312 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3.5 Lightning | 0.3554 | 1,060.06 | 0.1708 | ❌ |
| 313 | <img src="https://artificialanalysis.ai/img/logos//img/logos/servicenow_small.svg" width="18" alt="ServiceNow" /> ServiceNow | Apriel-v1.5-15B-Thinker | 0.3529 | — | — | — |
| 314 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B A22B 2507 | 0.3511 | 5,865.70 | 0.3696 | ❌ |
| 315 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 Omni Flash | 0.3490 | 809.08 | 0.1454 | ❌ |
| 316 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder 480B | 0.3481 | 5,761.54 | 0.3673 | ❌ |
| 317 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Sep) | 0.3471 | — | — | — |
| 318 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron Cascade 2 30B A3B | 0.3470 | — | — | — |
| 319 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepcogito_small.png" width="18" alt="Deep Cogito" /> Deep Cogito | Cogito v2.1 | 0.3468 | — | — | — |
| 320 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Magistral Medium 1.2 | 0.3439 | — | — | — |
| 321 | <img src="https://artificialanalysis.ai/img/logos//img/logos/servicenow_small.svg" width="18" alt="ServiceNow" /> ServiceNow | Apriel-v1.6-15B-Thinker | 0.3429 | — | — | — |
| 322 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 26B A4B (Non-reasoning) | 0.3418 | 1,488.78 | 0.2056 | ❌ |
| 323 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | G9v3-3B | 0.3417 | — | — | — |
| 324 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 3 | 0.3413 | — | — | — |
| 325 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6V | 0.3406 | 2,400.91 | 0.2593 | ❌ |
| 326 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 Terminus (Non-reasoning) | 0.3399 | — | — | — |
| 327 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-120b (high) | 0.3390 | 2,750.08 | 0.2753 | ❌ |
| 328 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (ChatGPT) | 0.3359 | — | — | — |
| 329 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash (Non-reasoning) | 0.3313 | — | — | — |
| 330 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max (Preview) | 0.3289 | 7,196.63 | 0.3960 | ❌ |
| 331 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 4 | 0.3260 | 1,575.46 | 0.2117 | ❌ |
| 332 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Exp (Non-reasoning) | 0.3227 | — | — | — |
| 333 | <img src="https://artificialanalysis.ai/img/logos//img/logos/multiversecomputing_small.svg" width="18" alt="Multiverse Computing" /> Multiverse Computing | HyperNova 60B 2605 (high) | 0.3210 | — | — | — |
| 334 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Sep) (Non-reasoning) | 0.3204 | — | — | — |
| 335 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 (Non-reasoning) | 0.3196 | — | — | — |
| 336 | <img src="https://artificialanalysis.ai/img/logos//img/logos/cohere_small.svg" width="18" alt="Cohere" /> Cohere | North Mini Code | 0.3169 | 0.00 | 0.0000 | ❌ |
| 337 | <img src="https://artificialanalysis.ai/img/logos//img/logos/bytedance_small.svg" width="18" alt="ByteDance Seed" /> ByteDance Seed | Seed-OSS-36B-Instruct | 0.3159 | 1,530.64 | 0.2086 | ❌ |
| 338 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o3-mini (high) | 0.3135 | 30,002.37 | 0.5871 | ❌ |
| 339 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o (Nov) | 0.3125 | 21,952.44 | 0.5447 | ❌ |
| 340 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Non-reasoning) | 0.3104 | 1,907.14 | 0.2328 | ❌ |
| 341 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.2 8B | 0.3101 | 797.64 | 0.1441 | ❌ |
| 342 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 3 | 0.3093 | 1,717.91 | 0.2212 | ❌ |
| 343 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o (Aug) | 0.3091 | 19,361.10 | 0.5277 | ❌ |
| 344 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B 2507 | 0.3086 | 681.43 | 0.1304 | ❌ |
| 345 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm_small.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Think V2 | 0.3079 | — | — | — |
| 346 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite | 0.3062 | 3,235.43 | 0.2949 | ❌ |
| 347 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.1 Fast (Non-reasoning) | 0.3025 | — | — | — |
| 348 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Next 80B A3B (Reasoning) | 0.3017 | 3,075.46 | 0.2887 | ❌ |
| 349 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (minimal) | 0.3017 | 1,570.17 | 0.2114 | ❌ |
| 350 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 12B (Non-reasoning) | 0.3005 | 277.90 | 0.0684 | ❌ |
| 351 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 235B A22B | 0.2998 | 1,220.45 | 0.1849 | ❌ |
| 352 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano | 0.2997 | 525.15 | 0.1096 | ❌ |
| 353 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | QwQ-32B | 0.2980 | — | — | — |
| 354 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-1T | 0.2970 | — | — | — |
| 355 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openbmb_small.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-1B | 0.2970 | — | — | — |
| 356 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openbmb_small.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-1B (Non-reasoning) | 0.2968 | — | — | — |
| 357 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Pixtral Large | 0.2957 | — | — | — |
| 358 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Open 100B | 0.2924 | — | — | — |
| 359 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 4B (Non-reasoning) | 0.2902 | 91.99 | 0.0266 | ❌ |
| 360 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder Next | 0.2897 | 4,279.65 | 0.3295 | ❌ |
| 361 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o3-mini | 0.2896 | 13,315.34 | 0.4774 | ❌ |
| 362 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5-Air | 0.2890 | 2,535.52 | 0.2657 | ❌ |
| 363 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax M1 80k | 0.2888 | — | — | — |
| 364 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 E4B | 0.2881 | 260.06 | 0.0649 | ❌ |
| 365 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (Non-reasoning) | 0.2866 | 6,664.09 | 0.3860 | ❌ |
| 366 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (Non-reasoning) | 0.2863 | 1,062.90 | 0.1710 | ❌ |
| 367 | <img src="https://artificialanalysis.ai/img/logos//img/logos/china_mobile_small.png" width="18" alt="China Mobile" /> China Mobile | JT-MINI | 0.2844 | — | — | — |
| 368 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | DiffusionGemma 26B A4B | 0.2835 | — | — | — |
| 369 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3 | 0.2825 | 1,844.31 | 0.2291 | ❌ |
| 370 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax M1 40k | 0.2821 | — | — | — |
| 371 | <img src="https://artificialanalysis.ai/img/logos//img/logos/naver_small.webp" width="18" alt="Naver" /> Naver | HyperCLOVA X SEED Think (32B) | 0.2820 | — | — | — |
| 372 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 Fast (Non-reasoning) | 0.2804 | — | — | — |
| 373 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm_small.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (high) | 0.2798 | — | — | — |
| 374 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE (Non-reasoning) | 0.2796 | — | — | — |
| 375 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3 0324 | 0.2784 | — | — | — |
| 376 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (Non-reasoning) | 0.2781 | 3,917.54 | 0.3185 | ❌ |
| 377 | <img src="https://artificialanalysis.ai/img/logos//img/logos/korea-telecom_small.png" width="18" alt="Korea Telecom" /> Korea Telecom | Mi:dm K 2.5 Pro | 0.2769 | — | — | — |
| 378 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 (Jan) | 0.2760 | — | — | — |
| 379 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Large 3 | 0.2753 | 1,123.26 | 0.1765 | ❌ |
| 380 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 4 Maverick | 0.2740 | 3,004.13 | 0.2859 | ❌ |
| 381 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3.1 | 0.2730 | 1,839.52 | 0.2288 | ❌ |
| 382 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-20b (high) | 0.2710 | 485.21 | 0.1037 | ❌ |
| 383 | <img src="https://artificialanalysis.ai/img/logos//img/logos/prime-intellect_small.svg" width="18" alt="Prime Intellect" /> Prime Intellect | INTELLECT-3 | 0.2703 | — | — | — |
| 384 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano Omni 30B A3B | 0.2698 | 4,687.50 | 0.3410 | ❌ |
| 385 | <img src="https://artificialanalysis.ai/img/logos//img/logos/trillionlabs_small.svg" width="18" alt="Trillion Labs" /> Trillion Labs | Tri-21B-think Preview | 0.2695 | — | — | — |
| 386 | <img src="https://artificialanalysis.ai/img/logos//img/logos/longcat_small.svg" width="18" alt="LongCat" /> LongCat | LongCat Flash Lite | 0.2679 | — | — | — |
| 387 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 30B A3B (Reasoning) | 0.2676 | 6,100.61 | 0.3746 | ❌ |
| 388 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B A3B 2507 | 0.2676 | 6,100.61 | 0.3746 | ❌ |
| 389 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-20b (low) | 0.2672 | 572.71 | 0.1162 | ❌ |
| 390 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.1 405B | 0.2661 | — | — | — |
| 391 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova Premier | 0.2652 | — | — | — |
| 392 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 2.6 Flash | 0.2646 | — | — | — |
| 393 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 mini | 0.2645 | 2,143.05 | 0.2461 | ❌ |
| 394 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 E4B (Non-reasoning) | 0.2641 | 63.71 | 0.0189 | ❌ |
| 395 | <img src="https://artificialanalysis.ai/img/logos//img/logos/trillionlabs_small.svg" width="18" alt="Trillion Labs" /> Trillion Labs | Tri-21B-Think | 0.2639 | — | — | — |
| 396 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.2 3B | 0.2591 | 386.32 | 0.0880 | ❌ |
| 397 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (Non-reasoning) | 0.2570 | 1,815.37 | 0.2273 | ❌ |
| 398 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Next 80B A3B | 0.2562 | 1,121.10 | 0.1763 | ❌ |
| 399 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 32B | 0.2560 | 527.13 | 0.1098 | ❌ |
| 400 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nousresearch_small.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 405B | 0.2543 | 8,003.04 | 0.4099 | ❌ |
| 401 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm_small.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (medium) | 0.2519 | — | — | — |
| 402 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-1T | 0.2511 | — | — | — |
| 403 | <img src="https://artificialanalysis.ai/img/logos//img/logos/korea-telecom_small.png" width="18" alt="Korea Telecom" /> Korea Telecom | Mi:dm K 2.5 Pro Preview | 0.2507 | — | — | — |
| 404 | <img src="https://artificialanalysis.ai/img/logos//img/logos/motif_small.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif-2-12.7B | 0.2506 | — | — | — |
| 405 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-120b (low) | 0.2503 | 2,862.50 | 0.2801 | ❌ |
| 406 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.5 Haiku | 0.2479 | — | — | — |
| 407 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 8B (Reasoning) | 0.2475 | 5,340.55 | 0.3575 | ❌ |
| 408 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step3 VL 10B | 0.2458 | — | — | — |
| 409 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Super 49B v1.5 | 0.2437 | 1,201.21 | 0.1833 | ❌ |
| 410 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.0 Flash | 0.2435 | — | — | — |
| 411 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7-Flash (Non-reasoning) | 0.2433 | 318.25 | 0.0760 | ❌ |
| 412 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral 2 | 0.2415 | 0.00 | 0.0000 | ❌ |
| 413 | <img src="https://artificialanalysis.ai/img/logos//img/logos/baidu_small.svg" width="18" alt="Baidu" /> Baidu | ERNIE 4.5 300B A47B | 0.2407 | — | — | — |
| 414 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Magistral Medium 1 | 0.2397 | — | — | — |
| 415 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral Medium | 0.2381 | — | — | — |
| 416 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B 2507 | 0.2377 | — | — | — |
| 417 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (Non-reasoning) | 0.2371 | — | — | — |
| 418 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4 | 0.2371 | — | — | — |
| 419 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 4 (Non-reasoning) | 0.2366 | 444.19 | 0.0974 | ❌ |
| 420 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nousresearch_small.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 405B (Non-reasoning) | 0.2355 | 2,288.68 | 0.2537 | ❌ |
| 421 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder 30B A3B | 0.2342 | 1,815.12 | 0.2273 | ❌ |
| 422 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-8B-A1B | 0.2320 | — | — | — |
| 423 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 30B A3B | 0.2312 | 693.36 | 0.1319 | ❌ |
| 424 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6V (Non-reasoning) | 0.2306 | 797.35 | 0.1441 | ❌ |
| 425 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 E2B | 0.2293 | — | — | — |
| 426 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Omni 30B A3B (Reasoning) | 0.2288 | 2,550.76 | 0.2664 | ❌ |
| 427 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-2.6B | 0.2272 | — | — | — |
| 428 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B | 0.2248 | 21,352.12 | 0.5409 | ❌ |
| 429 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5V | 0.2241 | 4,801.82 | 0.3440 | ❌ |
| 430 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 12B v2 VL | 0.2234 | 1,600.61 | 0.2134 | ❌ |
| 431 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Large 2 (Nov) | 0.2224 | — | — | — |
| 432 | <img src="https://artificialanalysis.ai/img/logos//img/logos/tii_small.svg" width="18" alt="TII UAE" /> TII UAE | Falcon-H1R-7B | 0.2210 | — | — | — |
| 433 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Ultra | 0.2201 | — | — | — |
| 434 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral Small 2 | 0.2189 | 0.00 | 0.0000 | ❌ |
| 435 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3 (Dec) | 0.2125 | — | — | — |
| 436 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova Pro | 0.2113 | — | — | — |
| 437 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nanbeige_small.png" width="18" alt="Nanbeige" /> Nanbeige | Nanbeige4.1-3B | 0.2111 | — | — | — |
| 438 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3.1 32B Think | 0.2105 | — | — | — |
| 439 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3.2 | 0.2102 | 237.33 | 0.0603 | ❌ |
| 440 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam 105B (high) | 0.2096 | — | — | — |
| 441 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.0 32B | 0.2087 | — | — | — |
| 442 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Magistral Small 1.2 | 0.2082 | — | — | — |
| 443 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm_small.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (low) | 0.2073 | — | — | — |
| 444 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 9B V2 | 0.2067 | 420.12 | 0.0935 | ❌ |
| 445 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 2B | 0.2067 | — | — | — |
| 446 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-flash-2.0 | 0.2043 | — | — | — |
| 447 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Non-reasoning) | 0.2042 | 377.58 | 0.0865 | ❌ |
| 448 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Super 49B v1.5 (Non-reasoning) | 0.2026 | 561.05 | 0.1146 | ❌ |
| 449 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 4 Scout | 0.2018 | 496.45 | 0.1054 | ❌ |
| 450 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nousresearch_small.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 70B | 0.2007 | — | — | — |
| 451 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral Small (May) | 0.1997 | — | — | — |
| 452 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 32B | 0.1993 | 1,680.49 | 0.2188 | ❌ |
| 453 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova Lite | 0.1991 | 333.24 | 0.0787 | ❌ |
| 454 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.3 Nemotron Super 49B | 0.1961 | — | — | — |
| 455 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 32B | 0.1957 | — | — | — |
| 456 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen2.5 72B | 0.1951 | — | — | — |
| 457 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 14B | 0.1944 | 10,676.06 | 0.4479 | ❌ |
| 458 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-flash-2.0 | 0.1943 | 367.50 | 0.0847 | ❌ |
| 459 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 8B | 0.1937 | 619.47 | 0.1225 | ❌ |
| 460 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B | 0.1923 | 6,100.61 | 0.3746 | ❌ |
| 461 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Magistral Small 1 | 0.1918 | — | — | — |
| 462 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Large 2 (Jul) | 0.1880 | — | — | — |
| 463 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Ministral 3 14B | 0.1874 | 218.11 | 0.0563 | ❌ |
| 464 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 2 | 0.1872 | — | — | — |
| 465 | <img src="https://artificialanalysis.ai/img/logos//img/logos/cohere_small.svg" width="18" alt="Cohere" /> Cohere | Command A | 0.1872 | 7,279.10 | 0.3975 | ❌ |
| 466 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral Small | 0.1866 | — | — | — |
| 467 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B (Non-reasoning) | 0.1863 | 2,191.37 | 0.2487 | ❌ |
| 468 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.1 Nemotron 70B | 0.1850 | 1,483.08 | 0.2052 | ❌ |
| 469 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano 4B | 0.1837 | — | — | — |
| 470 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 4B (Reasoning) | 0.1825 | — | — | — |
| 471 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3 Haiku | 0.1814 | — | — | — |
| 472 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3.1 | 0.1806 | 233.36 | 0.0594 | ❌ |
| 473 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.3 Nemotron Super 49B (Non-reasoning) | 0.1800 | — | — | — |
| 474 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B A3B 2507 (Non-reasoning) | 0.1782 | 718.62 | 0.1349 | ❌ |
| 475 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B | 0.1768 | — | — | — |
| 476 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.1 70B | 0.1763 | 621.58 | 0.1228 | ❌ |
| 477 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 9B V2 (Non-reasoning) | 0.1761 | 192.09 | 0.0506 | ❌ |
| 478 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 32B (Non-reasoning) | 0.1746 | 565.60 | 0.1153 | ❌ |
| 479 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5V (Non-reasoning) | 0.1742 | 1,397.07 | 0.1989 | ❌ |
| 480 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 E2B (Non-reasoning) | 0.1742 | — | — | — |
| 481 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 2B (Non-reasoning) | 0.1724 | — | — | — |
| 482 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.1 30B | 0.1719 | — | — | — |
| 483 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3.1 32B Instruct | 0.1689 | — | — | — |
| 484 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Omni 30B A3B | 0.1672 | 787.21 | 0.1429 | ❌ |
| 485 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (minimal) | 0.1666 | 329.79 | 0.0781 | ❌ |
| 486 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B 2507 (Non-reasoning) | 0.1655 | — | — | — |
| 487 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.1 8B | 0.1637 | 41.21 | 0.0125 | ❌ |
| 488 | <img src="https://artificialanalysis.ai/img/logos//img/logos/celeris.svg" width="18" alt="Celeris" /> Celeris | Celeris-1 | 0.1615 | 1,061.87 | 0.1709 | ❌ |
| 489 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 32B Think | 0.1614 | — | — | — |
| 490 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o mini | 0.1610 | 1,152.20 | 0.1790 | ❌ |
| 491 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Llama 70B | 0.1606 | — | — | — |
| 492 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 nano | 0.1605 | 534.75 | 0.1109 | ❌ |
| 493 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.3 70B | 0.1604 | 7,554.99 | 0.4024 | ❌ |
| 494 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 14B | 0.1602 | — | — | — |
| 495 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi Linear 48B A3B Instruct | 0.1599 | — | — | — |
| 496 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Ministral 3 8B | 0.1586 | 160.30 | 0.0434 | ❌ |
| 497 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 2 (Non-reasoning) | 0.1585 | — | — | — |
| 498 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nousresearch_small.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 70B (Non-reasoning) | 0.1554 | — | — | — |
| 499 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai21_small.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba Reasoning 3B | 0.1552 | — | — | — |
| 500 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.0 32B (Non-reasoning) | 0.1530 | — | — | — |
| 501 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.1 8B | 0.1530 | 83.37 | 0.0243 | ❌ |
| 502 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova Micro | 0.1502 | 203.06 | 0.0530 | ❌ |
| 503 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 24B A2B | 0.1498 | — | — | — |
| 504 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai21_small.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba 1.7 Large | 0.1487 | — | — | — |
| 505 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 8B | 0.1480 | 5,340.55 | 0.3575 | ❌ |
| 506 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam 30B (high) | 0.1469 | — | — | — |
| 507 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3 | 0.1455 | 234.05 | 0.0596 | ❌ |
| 508 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 12B v2 VL (Non-reasoning) | 0.1452 | 658.95 | 0.1276 | ❌ |
| 509 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openbmb_small.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM-V 4.6 1.3B | 0.1450 | — | — | — |
| 510 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B (Non-reasoning) | 0.1408 | 694.65 | 0.1320 | ❌ |
| 511 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano (Non-reasoning) | 0.1382 | 158.71 | 0.0431 | ❌ |
| 512 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H Small | 0.1351 | — | — | — |
| 513 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 4B | 0.1347 | — | — | — |
| 514 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 27B | 0.1328 | — | — | — |
| 515 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 0528 Qwen3 8B | 0.1308 | — | — | — |
| 516 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Ministral 3 3B | 0.1294 | 115.83 | 0.0327 | ❌ |
| 517 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 14B (Non-reasoning) | 0.1291 | 1,101.35 | 0.1745 | ❌ |
| 518 | <img src="https://artificialanalysis.ai/img/logos//img/logos/microsoft_small.svg" width="18" alt="Microsoft" /> Microsoft | Phi-4 | 0.1246 | 365.84 | 0.0845 | ❌ |
| 519 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.1 Nemotron Nano 4B v1.1 | 0.1238 | — | — | — |
| 520 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 270M | 0.1216 | — | — | — |
| 521 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3 70B | 0.1167 | — | — | — |
| 522 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.2 11B (Vision) | 0.1162 | 355.81 | 0.0827 | ❌ |
| 523 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.2 3B | 0.1143 | — | — | — |
| 524 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 0.8B | 0.1134 | — | — | — |
| 525 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 7B Think | 0.1129 | — | — | — |
| 526 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-1.2B-Instruct | 0.1064 | — | — | — |
| 527 | <img src="https://artificialanalysis.ai/img/logos//img/logos/reka_small.svg" width="18" alt="Reka AI" /> Reka AI | Reka Flash 3 | 0.1059 | — | — | — |
| 528 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-mini-2.0 | 0.1055 | — | — | — |
| 529 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 2.6B | 0.1055 | — | — | — |
| 530 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 8B (Non-reasoning) | 0.1046 | 547.74 | 0.1128 | ❌ |
| 531 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Molmo2-8B | 0.1013 | — | — | — |
| 532 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam M | 0.1011 | — | — | — |
| 533 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai21_small.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba 1.7 Mini | 0.0999 | — | — | — |
| 534 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-1.2B-Thinking | 0.0985 | — | — | — |
| 535 | <img src="https://artificialanalysis.ai/img/logos//img/logos/microsoft_small.svg" width="18" alt="Microsoft" /> Microsoft | Phi-4 Mini | 0.0962 | 0.00 | 0.0000 | ❌ |
| 536 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 12B | 0.0960 | — | — | — |
| 537 | <img src="https://artificialanalysis.ai/img/logos//img/logos/swiss-ai-initiative_small.png" width="18" alt="Swiss AI Initiative" /> Swiss AI Initiative | Apertus 70B Instruct | 0.0918 | — | — | — |
| 538 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 0.8B (Non-reasoning) | 0.0915 | — | — | — |
| 539 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 7B | 0.0904 | — | — | — |
| 540 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | Exaone 4.0 1.2B | 0.0895 | — | — | — |
| 541 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | OLMo 2 32B | 0.0893 | — | — | — |
| 542 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H 1B | 0.0889 | — | — | — |
| 543 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.2 1B | 0.0878 | — | — | — |
| 544 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 1.7B | 0.0867 | — | — | — |
| 545 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.1 3B | 0.0851 | — | — | — |
| 546 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | Exaone 4.0 1.2B (Non-reasoning) | 0.0827 | — | — | — |
| 547 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 8B A1B | 0.0809 | — | — | — |
| 548 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 Micro | 0.0783 | — | — | — |
| 549 | <img src="https://artificialanalysis.ai/img/logos//img/logos/microsoft_small.svg" width="18" alt="Microsoft" /> Microsoft | Phi-3 Mini | 0.0735 | — | — | — |
| 550 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 3.3 8B | 0.0702 | 246.59 | 0.0622 | ❌ |
| 551 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-VL-1.6B | 0.0676 | — | — | — |
| 552 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 1B | 0.0670 | — | — | — |
| 553 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 350M | 0.0659 | — | — | — |
| 554 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 4B | 0.0651 | — | — | — |
| 555 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 1.2B | 0.0641 | — | — | — |
| 556 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 0.6B | 0.0635 | — | — | — |
| 557 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3 8B | 0.0633 | — | — | — |
| 558 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral 7B | 0.0609 | 267.12 | 0.0663 | ❌ |
| 559 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3n E4B | 0.0573 | — | — | — |
| 560 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm_small.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 0.9B | 0.0562 | — | — | — |
| 561 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 1.7B (Non-reasoning) | 0.0555 | — | — | — |
| 562 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | OLMo 2 7B | 0.0553 | — | — | — |
| 563 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 1B | 0.0550 | — | — | — |
| 564 | <img src="https://artificialanalysis.ai/img/logos//img/logos/swiss-ai-initiative_small.png" width="18" alt="Swiss AI Initiative" /> Swiss AI Initiative | Apertus 8B Instruct | 0.0540 | — | — | — |
| 565 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H 350M | 0.0499 | — | — | — |
| 566 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Molmo 7B-D | 0.0468 | — | — | — |
| 567 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 0.6B (Non-reasoning) | 0.0429 | — | — | — |
| 568 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3n E2B | 0.0354 | — | — | — |
| 569 | <img src="https://artificialanalysis.ai/img/logos//img/logos/cohere_small.svg" width="18" alt="Cohere" /> Cohere | Tiny Aya Global | 0.0350 | — | — | — |
| 570 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 1.5B | 0.0000 | — | — | — |

## 品牌帕累托前沿连线（仅体现在图中）

以下十一个品牌在图中拥有单独的帕累托连线（较窄宽度，品牌主题色，图层高于总体灰色连线）。表中数量为**入图顶点数**——品牌前沿上低于总体前沿第一级的顶点同样不入图（本表与图例一致）：

| 品牌 | 主题色 | 品牌前沿模型数（入图） |
|------|--------|--------------|
| <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | `#cc785c` | 13 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | `#1f1f1f` | 13 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | `#0089f4` | 2 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | `#1c7ff8` | 2 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | `#34A853` | 6 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | `#736cd3` | 6 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | `#047AFE` | 5 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | `#ff7018` | 3 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | `#2243e6` | 3 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | `#EB3568` | 3 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | `#ff6900` | 2 |

## 评分方法

1. **20项评估指标**各自线性归一化到 [0,1]
   （AA Intelligence Index、GPQA Diamond、Humanity's Last Exam、MMMU Pro、IFBench Instruction Following、SciCode Coding、CritPt Physics、AA-LCR Long Context、AA Omniscience Index、AA-Omniscience Accuracy、AA-Omniscience Non-Hallucination、GDPval-AA Normalized、AA Analyst Agent、APEX-Agents-AA、ITBench-SRE、τ²-Bench Telecom、τ³-Bench Banking、Terminal-Bench Hard、Terminal-Bench 2.1、Terminal-Bench 4.0）
   > V18（2026-09-12）：AA 更新了基准列——新增 AA Analyst Agent、τ³-Bench Banking、Terminal-Bench 2.1 / 4.0 四项；AA Agentic Index 与 AA Coding Index 已从 AA 的数据源中移除，相应剔除。指标数由 18 → 20。
2. **综合能力值** = 所有有效归一化分数的算术平均
3. **综合能力再归一化**：线性映射到 [0,1]，性能最好的模型 = 1，最差的模型 = 0
4. **Pareto前沿** = 不被任何其他模型支配的模型（综合能力 ≥ 且成本 ≤，且至少一项严格更优；成本为 0 的免费模型同样参与——横轴左端恒为 0，免费模型是合法前沿候选）
5. **模型范围** = Status: All（含已弃用模型；缺少足够评估数据者不参与排名）
6. **图表纵轴基线（V17）**：图表的 y = 0 取总体帕累托前沿的第一级（最低能力；本例 y0 = 0.4990，即前沿左端点 Gemma 4 31B）；综合能力低于该级的模型不出现在图表中（表格不受影响）。图中纵坐标 chart_y = (能力 - y0)/(1 - y0)，因此前沿左端点恰好落在 (0, 0)、最优模型恰好为 y = 1。该过滤在横轴映射构建之前完成


## 横轴映射（对数映射，真零点，V21）与分布分析

横轴（单请求成本）为 **Y = A·ln(B·c+C)+D 对数映射**（B = 1；A、D 由端点解出；C = 433.90，r = B/C = 0.00230468 经网格搜索确定）：

```
x = 0                            当 c = 0（免费模型，真零点）
x = A·ln(c+C)+D                  当 c > 0（B = 1 并入；A、D 由端点解出）
```

其中 C = 433.90（r = B/C = 0.00230468），拟合集为 11 品牌前沿入图正成本模型（综合能力 ≥ 前沿第一级）的成本分布，目标为组内名次分位数（最小二乘误差 mse = 0.016345，最大偏离 0.2273）。该映射在 **y 基线过滤之后**构建（V17：先以帕累托前沿第一级为 y = 0、剔除低性能模型，再对入图模型建映射）。

**该映射保证：**

- **函数端点严格钉死**：c = 0 → x = 0；最大成本 → x = 1——函数经过 (0,0) 与 (1,1)；
- 各数量级区间的入图模型数：1–10: 0，10–100: 0，100–1k: 5，1k–10k: 53，10k–100k: 86，100k–604k: 15
- **同倍率区间宽度相近**（对数轴性质）：1k→10k 与 100k→1M 同为 10 倍率，宽度相近（前者 53 个模型、后者 16 个）；与 V17 分位数映射不同，本图不追求均匀密度——密度不等如实显示；
- **左端恒为 0**（c = 0；1 个免费模型位于最左缘）
- 前沿最低正成本 784.60 → x = 0.1426（真实对数位置，不再钉 0；x = 0 恒为 c = 0 免费模型）；前沿最大成本 604,195 → x = 1.0000（= 1；高于前沿最大成本的模型不入图，仅表格保留）
- 中位数位置 0.483（≈ 0.5 居中）；左右两半模型数：左 87 / 右 74
- 横轴十分位模型数：1，7，14，21，44，33，19，11，6，5（对数映射下各十分位模型数自然不等）
- **10^x 数量级指示**（位置 = x(10^x)）：10^0 → 0.000，10^1 → 0.003，10^2 → 0.029，10^3 → 0.165，10^4 → 0.439，10^5 → 0.752

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
| CacheHitRate | [AA Coding Agents](https://artificialanalysis.ai/agents/coding-agents) | 全部模型-Agent搭配的 `cacheHitRate` 求平均（19 个有效值，均值 = 0.9497），对所有模型统一使用 |
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
**模型总数（Status: All）**: 570 个参与排名（另有模型因评估数据不足未列入；总体帕累托前沿 12 个；图表入图 161 个——综合能力 ≥ 前沿第一级）  

## 图表说明（黑底）

（V17 起本说明置于文末，图表之后直接跟随模型表格。）

图表说明：**灰色实线** = 总体帕累托前沿；**彩色细线** = 十一个品牌的单独帕累托前沿（品牌主题色，图层高于总体连线；暗色品牌元素带窄白边；顶点按（横轴位置、能力升序）连接，等成本点自下而上）；品牌前沿模型圆点同样使用品牌颜色。模型名称/思考程度标注优先骑在连线之上（点的左/右两侧皆可，同一条线段可容纳两个标签——各贴各的点；文字与连线平行、中轴线重合，连线仅在文字两侧绘制）；骑线位被其他标签占据时自动「让位」——占用者挪到自己的另一个骑线位，双方都保持骑线；实在骑不上线时按四级优先依次退让（V16）：离点最近位置的上方/下方平行偏移 → 点的两条连线延长线上就近 → 两连线夹角扇区内就近。标签规则（V13/V15）：品牌前沿模型共享的前导块按「最长有效切点」剔除 —— 切点止于分界符，或止于字母且其后紧跟数字（如 Claude Opus 5 → Opus 5、GPT-5.6 Sol → 5.6 Sol、Kimi K2.6 → 2.6、Qwen3.8 Max → 3.8 Max、MiMo-V2.5 → 2.5、MiniMax-M2.1 → 2.1）；(non-reasoning) 简写为 (non)；同一模型在品牌连线上相邻出现 2 次以上时仅性能最低者保留全名、相邻较高者只标思考程度，不相邻的重复出现保留全名（每次重新计算）；标签位置与序列同向（V15）——品牌前沿上越靠右上的模型，其标签重心必须同时更靠右且更靠上（两分量都 >= 0，至少是 (0,0)，仅其一非负不算合格；初始放置违反时自动就近重摆，单标签无解（被前后邻居夹死）时按窗口级联重排整体挪动，均不产生新的重叠）。纵轴 y = 0 = 总体帕累托前沿第一级（y0 = 0.4990，前沿左端点 Gemma 4 31B 恰为 (0,0)），能力低于该级的 363 个模型、缺少成本数据的 44 个模型与成本高于品牌前沿最大值的模型不出现在图中；横轴为对数映射（见上文「横轴映射」节），10^x 数量级指示位于 x(10^x)，同一倍率区间的宽度相近（对数轴性质；本图不追求均匀密度）。
