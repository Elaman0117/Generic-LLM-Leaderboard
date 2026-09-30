# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

## 全部模型（综合能力从高到低，最优 = 1，最差 = 0）

共收录 **Status: All**（含已弃用）的全部模型；按重新归一化后的综合能力排序。「帕累托」列：✅ = 总体帕累托前沿模型，❌ = 被支配，— = 无成本数据无法判定。图表纵轴以总体帕累托前沿第一级（y0 = 0.5121，即前沿左端点 Gemma 4 31B）为 0：综合能力 ≥ 该级且有成本数据的 172 个模型入图，366 个能力低于第一级、43 个缺少成本数据的模型不出现在图中，成本高于品牌前沿最大值的模型同样不入图（本表不受影响，仍完整列出全部模型）。

| # | 品牌 | 模型 | 综合能力 | 单请求成本 | 横轴位置 | 帕累托 |
|---|------|------|---------|-----------|-----------|------|
| 1 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (max with fallback) | 1.0000 | 1,294,035.03 | 1.0000 | ✅ |
| 2 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (xhigh with fallback) | 0.9956 | 227,178.17 | 0.7998 | ✅ |
| 3 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (max with fallback) | 0.9796 | 998,194.18 | 0.9701 | ❌ |
| 4 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (xhigh with fallback) | 0.9667 | 352,084.25 | 0.8502 | ❌ |
| 5 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (max with fallback) | 0.9633 | 568,608.60 | 0.9053 | ❌ |
| 6 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (xhigh) | 0.9576 | 417,112.22 | 0.8697 | ❌ |
| 7 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (max) | 0.9560 | 933,046.64 | 0.9624 | ❌ |
| 8 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (high with fallback) | 0.9556 | 63,661.71 | 0.6536 | ✅ |
| 9 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (max) | 0.9411 | 209,087.61 | 0.7902 | ❌ |
| 10 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (max) | 0.9408 | 112,707.09 | 0.7192 | ❌ |
| 11 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (high) | 0.9384 | 158,738.73 | 0.7586 | ❌ |
| 12 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (high with fallback) | 0.9344 | 101,812.61 | 0.7075 | ❌ |
| 13 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5 (with fallback) | 0.9340 | 366,091.02 | 0.8547 | ❌ |
| 14 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (xhigh) | 0.9320 | 51,083.15 | 0.6284 | ✅ |
| 15 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (xhigh) | 0.9284 | 80,668.22 | 0.6808 | ❌ |
| 16 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (medium with fallback) | 0.9272 | 49,000.72 | 0.6236 | ✅ |
| 17 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (high) | 0.9256 | 44,777.06 | 0.6133 | ✅ |
| 18 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (max) | 0.9188 | 187,307.46 | 0.7776 | ❌ |
| 19 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (medium) | 0.9182 | 54,995.44 | 0.6368 | ❌ |
| 20 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (high) | 0.9136 | 51,269.06 | 0.6288 | ❌ |
| 21 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.3 (xhigh) | 0.9083 | 12,733.17 | 0.4699 | ✅ |
| 22 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (medium with fallback) | 0.9019 | 55,299.37 | 0.6374 | ❌ |
| 23 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (medium) | 0.8956 | 10,723.92 | 0.4505 | ✅ |
| 24 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (max) | 0.8915 | 158,182.47 | 0.7582 | ❌ |
| 25 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.3 (max) | 0.8911 | 12,733.17 | 0.4699 | ❌ |
| 26 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (xhigh with fallback) | 0.8891 | 42,789.24 | 0.6081 | ❌ |
| 27 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (low) | 0.8800 | 48,046.46 | 0.6213 | ❌ |
| 28 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3 (max) | 0.8737 | 41,992.79 | 0.6059 | ❌ |
| 29 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (medium) | 0.8727 | 35,015.72 | 0.5851 | ❌ |
| 30 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (high) | 0.8727 | 20,284.16 | 0.5228 | ❌ |
| 31 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (xhigh) | 0.8725 | 81,006.54 | 0.6813 | ❌ |
| 32 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (low with fallback) | 0.8683 | 45,115.94 | 0.6141 | ❌ |
| 33 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (xhigh) | 0.8648 | 22,060.68 | 0.5323 | ❌ |
| 34 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (xhigh) | 0.8641 | 144,409.65 | 0.7477 | ❌ |
| 35 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (high) | 0.8617 | 22,794.84 | 0.5361 | ❌ |
| 36 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3 (max) | 0.8551 | 14,230.29 | 0.4825 | ❌ |
| 37 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (medium) | 0.8549 | 19,370.98 | 0.5175 | ❌ |
| 38 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (low) | 0.8529 | 8,579.89 | 0.4254 | ✅ |
| 39 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (high) | 0.8527 | 34,098.66 | 0.5821 | ❌ |
| 40 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (xhigh) | 0.8508 | 47,927.13 | 0.6210 | ❌ |
| 41 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.6-Pro | 0.8505 | 2,449.51 | 0.2880 | ✅ |
| 42 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 Max (0902) | 0.8505 | 18,467.55 | 0.5121 | ❌ |
| 43 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (max) | 0.8483 | 200,484.67 | 0.7854 | ❌ |
| 44 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.8 (max) | 0.8473 | 96,233.46 | 0.7010 | ❌ |
| 45 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.7 (xhigh) | 0.8413 | 38,398.20 | 0.5957 | ❌ |
| 46 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (high) | 0.8403 | 76,097.39 | 0.6741 | ❌ |
| 47 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.7 (high) | 0.8400 | 27,321.95 | 0.5567 | ❌ |
| 48 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (high) | 0.8325 | 19,271.09 | 0.5169 | ❌ |
| 49 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step 5 Preview | 0.8321 | 7,775.24 | 0.4143 | ❌ |
| 50 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (high) | 0.8315 | 19,054.62 | 0.5156 | ❌ |
| 51 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (medium) | 0.8298 | — | — | — |
| 52 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (medium) | 0.8289 | 26,064.06 | 0.5514 | ❌ |
| 53 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 Max | 0.8281 | 18,467.55 | 0.5121 | ❌ |
| 54 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (low with fallback) | 0.8227 | 34,196.44 | 0.5824 | ❌ |
| 55 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.2 (xhigh) | 0.8175 | 12,733.17 | 0.4699 | ❌ |
| 56 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3-Flash | 0.8146 | 1,578.56 | 0.2425 | ✅ |
| 57 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 2.4T A95B | 0.8119 | 18,467.55 | 0.5121 | ❌ |
| 58 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (medium) | 0.8084 | — | — | — |
| 59 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (high with fallback) | 0.8075 | 22,802.53 | 0.5361 | ❌ |
| 60 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.7 (max) | 0.8053 | 48,255.55 | 0.6218 | ❌ |
| 61 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (xhigh) | 0.8014 | 283,021.16 | 0.8251 | ❌ |
| 62 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (max) | 0.8001 | 163,519.45 | 0.7620 | ❌ |
| 63 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash | 0.8001 | 36,738.12 | 0.5906 | ❌ |
| 64 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (low) | 0.7977 | 24,556.51 | 0.5446 | ❌ |
| 65 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.5 (high) | 0.7972 | 9,821.53 | 0.4406 | ❌ |
| 66 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (medium) | 0.7927 | 39,625.70 | 0.5993 | ❌ |
| 67 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.2 (max) | 0.7927 | 14,230.29 | 0.4825 | ❌ |
| 68 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (medium) | 0.7906 | 32,442.14 | 0.5764 | ❌ |
| 69 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.3 Codex (xhigh) | 0.7905 | 103,636.41 | 0.7096 | ❌ |
| 70 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (xhigh) | 0.7883 | 35,322.13 | 0.5861 | ❌ |
| 71 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (medium) | 0.7826 | 9,754.33 | 0.4398 | ❌ |
| 72 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.1 Pro Preview | 0.7819 | 47,058.68 | 0.6189 | ❌ |
| 73 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.1 (xhigh) | 0.7660 | — | — | — |
| 74 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (low) | 0.7659 | 19,827.73 | 0.5202 | ❌ |
| 75 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8-Flash-Next | 0.7548 | 1,409.09 | 0.2311 | ✅ |
| 76 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.6 Flash | 0.7523 | 15,932.62 | 0.4953 | ❌ |
| 77 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (high) | 0.7509 | 11,754.14 | 0.4608 | ❌ |
| 78 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.6 (max) | 0.7483 | 36,790.86 | 0.5908 | ❌ |
| 79 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 v2 | 0.7448 | 9,208.91 | 0.4333 | ❌ |
| 80 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (max) | 0.7389 | 15,710.60 | 0.4937 | ❌ |
| 81 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (medium with fallback) | 0.7337 | 9,466.35 | 0.4364 | ❌ |
| 82 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (low) | 0.7335 | 9,740.91 | 0.4396 | ❌ |
| 83 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3 Pro Preview (high) | 0.7328 | — | — | — |
| 84 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (low) | 0.7326 | — | — | — |
| 85 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (low) | 0.7312 | 4,313.64 | 0.3490 | ❌ |
| 86 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (medium) | 0.7308 | 7,582.08 | 0.4115 | ❌ |
| 87 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark | 0.7271 | — | — | — |
| 88 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (low) | 0.7252 | 12,015.64 | 0.4633 | ❌ |
| 89 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro 0813 (max) | 0.7251 | 11,045.48 | 0.4538 | ❌ |
| 90 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (xhigh) | 0.7199 | 130,661.59 | 0.7362 | ❌ |
| 91 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash (max) | 0.7196 | 3,222.55 | 0.3173 | ❌ |
| 92 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 Codex (xhigh) | 0.7194 | — | — | — |
| 93 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 Max Preview | 0.7183 | 21,446.88 | 0.5291 | ❌ |
| 94 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (max) | 0.7182 | 8,004.03 | 0.4176 | ❌ |
| 95 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.7 Max | 0.7139 | 27,923.27 | 0.5592 | ❌ |
| 96 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.6 | 0.7085 | 21,840.78 | 0.5312 | ❌ |
| 97 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 | 0.7052 | — | — | — |
| 98 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.5 | 0.7044 | 39,395.56 | 0.5986 | ❌ |
| 99 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (xhigh) | 0.7036 | 8,721.15 | 0.4272 | ❌ |
| 100 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (xhigh) | 0.7012 | 6,926.68 | 0.4014 | ❌ |
| 101 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.7 (Non-reasoning, high) | 0.6993 | 22,003.64 | 0.5320 | ❌ |
| 102 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (low) | 0.6956 | 26,671.52 | 0.5540 | ❌ |
| 103 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash Vision (max) | 0.6890 | 3,675.53 | 0.3315 | ❌ |
| 104 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3 Flash | 0.6887 | 5,992.26 | 0.3853 | ❌ |
| 105 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash 0731 (max) | 0.6859 | 3,675.53 | 0.3315 | ❌ |
| 106 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (max) | 0.6842 | 92,779.67 | 0.6968 | ❌ |
| 107 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (low) | 0.6816 | 13,378.14 | 0.4755 | ❌ |
| 108 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (xhigh) | 0.6792 | 21,054.72 | 0.5270 | ❌ |
| 109 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (medium) | 0.6782 | 10,922.80 | 0.4525 | ❌ |
| 110 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3 (low) | 0.6772 | 41,992.79 | 0.6059 | ❌ |
| 111 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (low with fallback) | 0.6757 | 9,202.99 | 0.4332 | ❌ |
| 112 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M3 | 0.6733 | 3,774.16 | 0.3344 | ❌ |
| 113 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (low) | 0.6733 | 5,414.05 | 0.3740 | ❌ |
| 114 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (xhigh) | 0.6725 | 1,754.26 | 0.2532 | ❌ |
| 115 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.6-Flash | 0.6716 | 803.86 | 0.1776 | ✅ |
| 116 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Pro | 0.6705 | — | — | — |
| 117 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 Plus | 0.6695 | 18,898.80 | 0.5147 | ❌ |
| 118 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.7 Plus | 0.6694 | 4,976.92 | 0.3647 | ❌ |
| 119 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (high) | 0.6659 | 2,756.22 | 0.3005 | ❌ |
| 120 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (medium) | 0.6652 | — | — | — |
| 121 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (max) | 0.6625 | 4,515.76 | 0.3540 | ❌ |
| 122 | <img src="https://artificialanalysis.ai/img/logos//img/logos/motif.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif 3 | 0.6608 | — | — | — |
| 123 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.1 | 0.6567 | 20,631.08 | 0.5247 | ❌ |
| 124 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 Codex (high) | 0.6519 | — | — | — |
| 125 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (high) | 0.6499 | 2,442.55 | 0.2877 | ❌ |
| 126 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (high) | 0.6477 | 11,787.34 | 0.4611 | ❌ |
| 127 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5 | 0.6469 | 13,978.31 | 0.4804 | ❌ |
| 128 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (high) | 0.6463 | 1,340.38 | 0.2261 | ❌ |
| 129 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 (high) | 0.6409 | 48,625.80 | 0.6227 | ❌ |
| 130 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 375B A23B | 0.6406 | — | — | — |
| 131 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (high) | 0.6380 | 16,387.67 | 0.4985 | ❌ |
| 132 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.7 Code | 0.6353 | 13,236.19 | 0.4743 | ❌ |
| 133 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 Codex (high) | 0.6337 | — | — | — |
| 134 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (xhigh) | 0.6279 | 132,665.33 | 0.7379 | ❌ |
| 135 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Omni-0327 | 0.6239 | — | — | — |
| 136 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (medium) | 0.6217 | 38,531.69 | 0.5961 | ❌ |
| 137 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-3.0-flash-VL | 0.6173 | 733.17 | 0.1693 | ✅ |
| 138 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (low) | 0.6152 | 10,949.12 | 0.4528 | ❌ |
| 139 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.6 (Non-reasoning, high) | 0.6144 | 22,586.52 | 0.5350 | ❌ |
| 140 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5-Turbo | 0.6140 | — | — | — |
| 141 | <img src="https://artificialanalysis.ai/img/logos//img/logos/thinking-machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling Small | 0.6135 | 3,732.69 | 0.3332 | ❌ |
| 142 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5-Pro | 0.6131 | 2,449.51 | 0.2880 | ❌ |
| 143 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 | 0.6122 | — | — | — |
| 144 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5 | 0.6098 | 803.86 | 0.1776 | ❌ |
| 145 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (max) | 0.6091 | — | — | — |
| 146 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3 (low) | 0.6090 | 14,230.29 | 0.4825 | ❌ |
| 147 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 4 | 0.6076 | 3,732.69 | 0.3332 | ❌ |
| 148 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (high) | 0.6075 | 69,825.13 | 0.6642 | ❌ |
| 149 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (medium) | 0.6073 | — | — | — |
| 150 | <img src="https://artificialanalysis.ai/img/logos//img/logos/thinking-machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling | 0.6069 | 12,283.89 | 0.4658 | ❌ |
| 151 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (high) | 0.6064 | — | — | — |
| 152 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok Build 0.1 0616 | 0.6043 | 7,442.31 | 0.4094 | ❌ |
| 153 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 Instant (May 2026) | 0.6033 | — | — | — |
| 154 | <img src="https://artificialanalysis.ai/img/logos//img/logos/apodex.svg" width="18" alt="Apodex" /> Apodex | Apodex 1.1 | 0.6032 | — | — | — |
| 155 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Opus | 0.6017 | — | — | — |
| 156 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Open2 250B | 0.5936 | — | — | — |
| 157 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (minimal) | 0.5923 | 8,379.20 | 0.4227 | ❌ |
| 158 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 27B | 0.5920 | 6,165.87 | 0.3884 | ❌ |
| 159 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash (Feb 2026) | 0.5917 | — | — | — |
| 160 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (xhigh) | 0.5916 | 18,933.96 | 0.5149 | ❌ |
| 161 | <img src="https://artificialanalysis.ai/img/logos//img/logos/multiversecomputing.svg" width="18" alt="Multiverse Computing" /> Multiverse Computing | Quasar 438B (max) | 0.5898 | 4,831.73 | 0.3614 | ❌ |
| 162 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Omni | 0.5895 | — | — | — |
| 163 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o3 | 0.5889 | 15,652.25 | 0.4933 | ❌ |
| 164 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nex.svg" width="18" alt="Nex AGI" /> Nex AGI | Nex-N2-Pro | 0.5887 | — | — | — |
| 165 | <img src="https://artificialanalysis.ai/img/logos//img/logos/motif.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif 3 (Beta) | 0.5864 | — | — | — |
| 166 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM 5V Turbo | 0.5851 | — | — | — |
| 167 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 27B | 0.5851 | 22,565.33 | 0.5349 | ❌ |
| 168 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.5 | 0.5831 | — | — | — |
| 169 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Sonnet | 0.5810 | 20,673.29 | 0.5249 | ❌ |
| 170 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (medium) | 0.5795 | 4,134.80 | 0.3444 | ❌ |
| 171 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Ultra | 0.5790 | 8,780.77 | 0.4280 | ❌ |
| 172 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.1 Opus | 0.5770 | — | — | — |
| 173 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (Non-reasoning, high) | 0.5753 | 13,395.43 | 0.4756 | ❌ |
| 174 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 Thinking | 0.5749 | 12,250.00 | 0.4655 | ❌ |
| 175 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.5 (Non-reasoning) | 0.5728 | 22,075.31 | 0.5324 | ❌ |
| 176 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (Non-reasoning, low) | 0.5699 | 13,175.81 | 0.4737 | ❌ |
| 177 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (medium) | 0.5693 | 8,721.15 | 0.4272 | ❌ |
| 178 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 397B A17B | 0.5690 | 13,601.33 | 0.4773 | ❌ |
| 179 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.6 (Non-reasoning) | 0.5677 | 4,809.17 | 0.3609 | ❌ |
| 180 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3 Pro Preview (low) | 0.5666 | — | — | — |
| 181 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash-Lite | 0.5654 | 8,551.06 | 0.4250 | ❌ |
| 182 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (medium) | 0.5642 | 9,042.09 | 0.4313 | ❌ |
| 183 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (medium) | 0.5601 | 1,268.93 | 0.2207 | ❌ |
| 184 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.7 | 0.5589 | 4,328.56 | 0.3494 | ❌ |
| 185 | <img src="https://artificialanalysis.ai/img/logos//img/logos/tencent.svg" width="18" alt="Tencent" /> Tencent | Hy3 | 0.5584 | 1,783.89 | 0.2549 | ❌ |
| 186 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (Non-reasoning) | 0.5582 | 17,902.34 | 0.5085 | ❌ |
| 187 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 Codex mini (high) | 0.5581 | — | — | — |
| 188 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon MoVA 36B A4B | 0.5554 | — | — | — |
| 189 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (low) | 0.5542 | 11,518.34 | 0.4585 | ❌ |
| 190 | <img src="https://artificialanalysis.ai/img/logos//img/logos/tencent.svg" width="18" alt="Tencent" /> Tencent | Hy3-preview | 0.5542 | — | — | — |
| 191 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (low) | 0.5539 | 8,721.15 | 0.4272 | ❌ |
| 192 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.5 | 0.5488 | 3,490.75 | 0.3259 | ❌ |
| 193 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.1 (Non-reasoning) | 0.5477 | 5,893.53 | 0.3834 | ❌ |
| 194 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 Omni Plus | 0.5474 | 3,407.73 | 0.3233 | ❌ |
| 195 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 35B A3B | 0.5436 | 13,471.08 | 0.4763 | ❌ |
| 196 | <img src="https://artificialanalysis.ai/img/logos//img/logos/china-mobile.png" width="18" alt="China Mobile" /> China Mobile | JT-4.1 Flash 236B A21B | 0.5424 | — | — | — |
| 197 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (Non-reasoning) | 0.5423 | 8,925.12 | 0.4298 | ❌ |
| 198 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sktelecom.svg" width="18" alt="SK Telecom" /> SK Telecom | A.X-K2 | 0.5413 | — | — | — |
| 199 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.1 Fast | 0.5405 | — | — | — |
| 200 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (Non-reasoning) | 0.5390 | 8,977.47 | 0.4304 | ❌ |
| 201 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano | 0.5346 | 2,138.27 | 0.2737 | ❌ |
| 202 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (high) | 0.5341 | 14,178.01 | 0.4821 | ❌ |
| 203 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.1 | 0.5336 | 3,490.75 | 0.3259 | ❌ |
| 204 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max Thinking | 0.5336 | — | — | — |
| 205 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 122B A10B | 0.5316 | 8,221.15 | 0.4206 | ❌ |
| 206 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 35B A3B | 0.5283 | 5,138.22 | 0.3682 | ❌ |
| 207 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step 3.7 Flash | 0.5278 | 3,363.46 | 0.3219 | ❌ |
| 208 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | G9v3-39A5B | 0.5252 | — | — | — |
| 209 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.5 (Non-reasoning) | 0.5229 | — | — | — |
| 210 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash | 0.5216 | — | — | — |
| 211 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (medium) | 0.5205 | 10,316.85 | 0.4461 | ❌ |
| 212 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3 Flash (Non-reasoning) | 0.5159 | 2,803.60 | 0.3023 | ❌ |
| 213 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7 | 0.5154 | 10,082.93 | 0.4435 | ❌ |
| 214 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 | 0.5131 | — | — | — |
| 215 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 31B | 0.5121 | 0.00 | 0.0000 | ✅ |
| 216 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kwaikat.svg" width="18" alt="KwaiKAT" /> KwaiKAT | KAT-Coder-Pro V2 | 0.5119 | — | — | — |
| 217 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5 (Non-reasoning) | 0.5117 | 4,420.88 | 0.3517 | ❌ |
| 218 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B | 0.5111 | 3,309.94 | 0.3202 | ❌ |
| 219 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.0 Flash | 0.5106 | 733.17 | 0.1693 | ❌ |
| 220 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-3.0-flash-Fin | 0.5059 | 733.17 | 0.1693 | ❌ |
| 221 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (low) | 0.5058 | 1,135.52 | 0.2099 | ❌ |
| 222 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 397B A17B (Non-reasoning) | 0.5049 | 2,860.60 | 0.3045 | ❌ |
| 223 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step 3.5 Flash 2603 | 0.5048 | 994.23 | 0.1972 | ❌ |
| 224 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (low) | 0.5037 | 548.91 | 0.1445 | ❌ |
| 225 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Sonnet | 0.5032 | — | — | — |
| 226 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (low) | 0.4986 | 9,007.20 | 0.4308 | ❌ |
| 227 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 Fast | 0.4984 | — | — | — |
| 228 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Glimmer (high) | 0.4983 | 3,932.57 | 0.3389 | ❌ |
| 229 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (Non-reasoning) | 0.4939 | 24,650.74 | 0.5450 | ❌ |
| 230 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 3 mini Reasoning (high) | 0.4914 | 2,124.40 | 0.2730 | ❌ |
| 231 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 27B (Non-reasoning) | 0.4901 | 2,492.27 | 0.2898 | ❌ |
| 232 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Sonnet (Non-reasoning) | 0.4897 | 13,104.74 | 0.4731 | ❌ |
| 233 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Speciale | 0.4888 | — | — | — |
| 234 | <img src="https://artificialanalysis.ai/img/logos//img/logos/china-mobile.png" width="18" alt="China Mobile" /> China Mobile | JT-35B-Flash | 0.4879 | — | — | — |
| 235 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step 3.5 Flash | 0.4870 | 994.23 | 0.1972 | ❌ |
| 236 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE 2.0 | 0.4851 | — | — | — |
| 237 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 Instant (June 2026) | 0.4819 | 82,487.98 | 0.6833 | ❌ |
| 238 | <img src="https://artificialanalysis.ai/img/logos//img/logos/cohere.svg" width="18" alt="Cohere" /> Cohere | Command A+ | 0.4798 | 0.00 | 0.0000 | ❌ |
| 239 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-2.6-1T | 0.4773 | 6,415.87 | 0.3929 | ❌ |
| 240 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash (Non-reasoning) | 0.4750 | 1,099.74 | 0.2068 | ❌ |
| 241 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (Non-reasoning) | 0.4747 | 12,244.00 | 0.4654 | ❌ |
| 242 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2 | 0.4744 | 3,165.87 | 0.3154 | ❌ |
| 243 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Pro | 0.4734 | 34,031.16 | 0.5818 | ❌ |
| 244 | <img src="https://artificialanalysis.ai/img/logos//img/logos/bytedance.svg" width="18" alt="ByteDance Seed" /> ByteDance Seed | Doubao Seed Code | 0.4710 | — | — | — |
| 245 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o4-mini (high) | 0.4707 | 19,124.38 | 0.5161 | ❌ |
| 246 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o1 | 0.4707 | — | — | — |
| 247 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3.5 | 0.4698 | 20,996.39 | 0.5267 | ❌ |
| 248 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 7B | 0.4668 | — | — | — |
| 249 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Haiku | 0.4608 | 11,168.41 | 0.4551 | ❌ |
| 250 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (Non-reasoning) | 0.4595 | 823.65 | 0.1798 | ❌ |
| 251 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (Non-reasoning) | 0.4558 | 10,059.36 | 0.4433 | ❌ |
| 252 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.7 Sonnet | 0.4553 | — | — | — |
| 253 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Sonnet (Non-reasoning) | 0.4524 | — | — | — |
| 254 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (medium) | 0.4497 | 28,638.61 | 0.5621 | ❌ |
| 255 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.2 (Non-reasoning) | 0.4473 | 6,309.34 | 0.3910 | ❌ |
| 256 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Sep) | 0.4469 | — | — | — |
| 257 | <img src="https://artificialanalysis.ai/img/logos//img/logos/longcat.svg" width="18" alt="LongCat" /> LongCat | LongCat 2.0 | 0.4464 | — | — | — |
| 258 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 27B (Non-reasoning) | 0.4459 | 2,886.52 | 0.3055 | ❌ |
| 259 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Exp | 0.4425 | — | — | — |
| 260 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kwaikat.svg" width="18" alt="KwaiKAT" /> KwaiKAT | KAT-Coder-Pro V1 | 0.4417 | — | — | — |
| 261 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.1 Flash-Lite | 0.4416 | 3,375.76 | 0.3223 | ❌ |
| 262 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (Non-reasoning) | 0.4402 | 10,405.55 | 0.4471 | ❌ |
| 263 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 Terminus | 0.4381 | — | — | — |
| 264 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.7 Sonnet (Non-reasoning) | 0.4320 | — | — | — |
| 265 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max Thinking (Preview) | 0.4311 | 17,930.77 | 0.5087 | ❌ |
| 266 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (low) | 0.4308 | 25,691.11 | 0.5497 | ❌ |
| 267 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 122B A10B (Non-reasoning) | 0.4278 | 2,869.96 | 0.3048 | ❌ |
| 268 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash | 0.4260 | 11,962.54 | 0.4628 | ❌ |
| 269 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (medium) | 0.4258 | 6,415.87 | 0.3929 | ❌ |
| 270 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5-Pro (Non-reasoning) | 0.4209 | 765.26 | 0.1731 | ❌ |
| 271 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Haiku (Non-reasoning) | 0.4207 | 4,397.88 | 0.3511 | ❌ |
| 272 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 9B | 0.4195 | 574.64 | 0.1483 | ❌ |
| 273 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 0905 | 0.4180 | 1,753.83 | 0.2532 | ❌ |
| 274 | <img src="https://artificialanalysis.ai/img/logos//img/logos/baidu.svg" width="18" alt="Baidu" /> Baidu | ERNIE 5.0 Thinking Preview | 0.4174 | — | — | — |
| 275 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (Non-reasoning) | 0.4167 | — | — | — |
| 276 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 235B A22B (Reasoning) | 0.4166 | 10,221.15 | 0.4451 | ❌ |
| 277 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 26B A4B | 0.4155 | — | — | — |
| 278 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 (Non-reasoning) | 0.4142 | — | — | — |
| 279 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-2.6-1T | 0.4138 | — | — | — |
| 280 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (low) | 0.4103 | — | — | — |
| 281 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 (Non-reasoning) | 0.4081 | — | — | — |
| 282 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.5 33B | 0.4070 | — | — | — |
| 283 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 4B | 0.4063 | 391.59 | 0.1181 | ❌ |
| 284 | <img src="https://artificialanalysis.ai/img/logos//img/logos/tencent.svg" width="18" alt="Tencent" /> Tencent | Hy3-preview (Non-reasoning) | 0.4062 | — | — | — |
| 285 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (high) | 0.4062 | 5,001.98 | 0.3653 | ❌ |
| 286 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (high) | 0.4051 | 6,415.87 | 0.3929 | ❌ |
| 287 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (medium) | 0.4041 | 2,711.17 | 0.2988 | ❌ |
| 288 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7 (Non-reasoning) | 0.4032 | 4,291.36 | 0.3484 | ❌ |
| 289 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (medium) | 0.4020 | — | — | — |
| 290 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 v2 (Non-reasoning) | 0.3981 | 3,965.11 | 0.3398 | ❌ |
| 291 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 35B A3B (Non-reasoning) | 0.3956 | 2,008.59 | 0.2672 | ❌ |
| 292 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 12B | 0.3955 | 805.29 | 0.1777 | ❌ |
| 293 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 | 0.3946 | — | — | — |
| 294 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5 | 0.3940 | — | — | — |
| 295 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max | 0.3882 | 4,383.35 | 0.3507 | ❌ |
| 296 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-2B | 0.3874 | — | — | — |
| 297 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok Code Fast 1 | 0.3854 | — | — | — |
| 298 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (Non-reasoning) | 0.3853 | 4,050.98 | 0.3421 | ❌ |
| 299 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 | 0.3844 | 1,644.19 | 0.2466 | ❌ |
| 300 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 0528 | 0.3830 | — | — | — |
| 301 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE | 0.3822 | — | — | — |
| 302 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6 | 0.3820 | 6,843.27 | 0.4000 | ❌ |
| 303 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inceptionlabs.svg" width="18" alt="Inception" /> Inception | Mercury 2 | 0.3811 | 3,264.51 | 0.3187 | ❌ |
| 304 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 31B (Non-reasoning) | 0.3789 | 1,632.08 | 0.2459 | ❌ |
| 305 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (Non-reasoning) | 0.3783 | 468.81 | 0.1319 | ❌ |
| 306 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Sep) (Non-reasoning) | 0.3773 | — | — | — |
| 307 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (Non-reasoning) | 0.3749 | 1,016.65 | 0.1993 | ❌ |
| 308 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (minimal) | 0.3746 | 7,898.35 | 0.4161 | ❌ |
| 309 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 32B (Reasoning) | 0.3736 | 1,688.46 | 0.2493 | ❌ |
| 310 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 3.7B | 0.3735 | — | — | — |
| 311 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Super | 0.3732 | 3,832.93 | 0.3361 | ❌ |
| 312 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 | 0.3726 | 10,883.60 | 0.4521 | ❌ |
| 313 | <img src="https://artificialanalysis.ai/img/logos//img/logos/arcee.svg" width="18" alt="Arcee AI" /> Arcee AI | Trinity Large Thinking | 0.3719 | 2,705.05 | 0.2985 | ❌ |
| 314 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.2 30B | 0.3716 | 2,091.35 | 0.2714 | ❌ |
| 315 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 (Non-reasoning) | 0.3709 | 7,886.50 | 0.4159 | ❌ |
| 316 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (low) | 0.3706 | 6,415.87 | 0.3929 | ❌ |
| 317 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 9B (Non-reasoning) | 0.3696 | — | — | — |
| 318 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7-Flash | 0.3695 | 1,133.17 | 0.2097 | ❌ |
| 319 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6 (Non-reasoning) | 0.3660 | 5,126.91 | 0.3680 | ❌ |
| 320 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 35B A3B (Non-reasoning) | 0.3658 | 1,790.19 | 0.2553 | ❌ |
| 321 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3.5 Lightning | 0.3647 | 1,061.06 | 0.2034 | ❌ |
| 322 | <img src="https://artificialanalysis.ai/img/logos//img/logos/servicenow.svg" width="18" alt="ServiceNow" /> ServiceNow | Apriel-v1.5-15B-Thinker | 0.3622 | — | — | — |
| 323 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.0 Tiny | 0.3606 | 0.00 | 0.0000 | ❌ |
| 324 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B A22B 2507 | 0.3603 | 5,877.16 | 0.3831 | ❌ |
| 325 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 Omni Flash | 0.3582 | 776.69 | 0.1745 | ❌ |
| 326 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder 480B | 0.3572 | 5,846.69 | 0.3825 | ❌ |
| 327 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Sep) | 0.3562 | — | — | — |
| 328 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron Cascade 2 30B A3B | 0.3561 | — | — | — |
| 329 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepcogito.png" width="18" alt="Deep Cogito" /> Deep Cogito | Cogito v2.1 | 0.3559 | — | — | — |
| 330 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Magistral Medium 1.2 | 0.3529 | — | — | — |
| 331 | <img src="https://artificialanalysis.ai/img/logos//img/logos/servicenow.svg" width="18" alt="ServiceNow" /> ServiceNow | Apriel-v1.6-15B-Thinker | 0.3519 | — | — | — |
| 332 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 26B A4B (Non-reasoning) | 0.3508 | 1,259.21 | 0.2200 | ❌ |
| 333 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | G9v3-3B | 0.3506 | — | — | — |
| 334 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 3 | 0.3503 | — | — | — |
| 335 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6V | 0.3495 | 4,092.73 | 0.3432 | ❌ |
| 336 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 Terminus (Non-reasoning) | 0.3488 | — | — | — |
| 337 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-120b (high) | 0.3479 | 2,751.32 | 0.3003 | ❌ |
| 338 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (ChatGPT) | 0.3447 | — | — | — |
| 339 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash (Non-reasoning) | 0.3400 | — | — | — |
| 340 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max (Preview) | 0.3376 | 7,304.76 | 0.4073 | ❌ |
| 341 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Small 4 | 0.3346 | 1,724.64 | 0.2515 | ❌ |
| 342 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Exp (Non-reasoning) | 0.3312 | — | — | — |
| 343 | <img src="https://artificialanalysis.ai/img/logos//img/logos/multiversecomputing.svg" width="18" alt="Multiverse Computing" /> Multiverse Computing | HyperNova 60B 2605 (high) | 0.3294 | — | — | — |
| 344 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Sep) (Non-reasoning) | 0.3288 | — | — | — |
| 345 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 (Non-reasoning) | 0.3280 | — | — | — |
| 346 | <img src="https://artificialanalysis.ai/img/logos//img/logos/cohere.svg" width="18" alt="Cohere" /> Cohere | North Mini Code | 0.3252 | 0.00 | 0.0000 | ❌ |
| 347 | <img src="https://artificialanalysis.ai/img/logos//img/logos/bytedance.svg" width="18" alt="ByteDance Seed" /> ByteDance Seed | Seed-OSS-36B-Instruct | 0.3242 | 1,541.11 | 0.2401 | ❌ |
| 348 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o3-mini (high) | 0.3217 | 26,492.09 | 0.5532 | ❌ |
| 349 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o (Nov) | 0.3207 | 21,819.00 | 0.5311 | ❌ |
| 350 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Non-reasoning) | 0.3185 | 1,918.54 | 0.2624 | ❌ |
| 351 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.2 8B | 0.3183 | 799.88 | 0.1771 | ❌ |
| 352 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 3 | 0.3174 | 1,724.64 | 0.2515 | ❌ |
| 353 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o (Aug) | 0.3172 | 19,336.55 | 0.5173 | ❌ |
| 354 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B 2507 | 0.3167 | 718.99 | 0.1676 | ❌ |
| 355 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Think V2 | 0.3160 | — | — | — |
| 356 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite | 0.3142 | 3,189.55 | 0.3162 | ❌ |
| 357 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.1 Fast (Non-reasoning) | 0.3105 | — | — | — |
| 358 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Next 80B A3B (Reasoning) | 0.3096 | 3,082.93 | 0.3125 | ❌ |
| 359 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (minimal) | 0.3096 | 1,575.32 | 0.2423 | ❌ |
| 360 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 12B (Non-reasoning) | 0.3083 | 291.67 | 0.0976 | ❌ |
| 361 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 235B A22B | 0.3077 | 1,245.34 | 0.2189 | ❌ |
| 362 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano | 0.3076 | 1,000.00 | 0.1978 | ❌ |
| 363 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | QwQ-32B | 0.3059 | — | — | — |
| 364 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-1T | 0.3048 | — | — | — |
| 365 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-1B | 0.3048 | — | — | — |
| 366 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-1B (Non-reasoning) | 0.3046 | — | — | — |
| 367 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Pixtral Large | 0.3034 | — | — | — |
| 368 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Open 100B | 0.3001 | — | — | — |
| 369 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 4B (Non-reasoning) | 0.2979 | 94.60 | 0.0414 | ❌ |
| 370 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder Next | 0.2973 | 4,265.99 | 0.3478 | ❌ |
| 371 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o3-mini | 0.2972 | 13,826.10 | 0.4792 | ❌ |
| 372 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5-Air | 0.2966 | 2,543.99 | 0.2920 | ❌ |
| 373 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax M1 80k | 0.2964 | — | — | — |
| 374 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inceptionlabs.svg" width="18" alt="Inception" /> Inception | Mercury 2.5 | 0.2963 | 2,437.19 | 0.2875 | ❌ |
| 375 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 E4B | 0.2956 | 261.06 | 0.0904 | ❌ |
| 376 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (Non-reasoning) | 0.2941 | 6,849.49 | 0.4001 | ❌ |
| 377 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (Non-reasoning) | 0.2938 | 1,075.86 | 0.2047 | ❌ |
| 378 | <img src="https://artificialanalysis.ai/img/logos//img/logos/china-mobile.png" width="18" alt="China Mobile" /> China Mobile | JT-MINI | 0.2918 | — | — | — |
| 379 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | DiffusionGemma 26B A4B | 0.2910 | — | — | — |
| 380 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3 | 0.2900 | — | — | — |
| 381 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax M1 40k | 0.2895 | — | — | — |
| 382 | <img src="https://artificialanalysis.ai/img/logos//img/logos/naver.webp" width="18" alt="Naver" /> Naver | HyperCLOVA X SEED Think (32B) | 0.2894 | — | — | — |
| 383 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 Fast (Non-reasoning) | 0.2877 | — | — | — |
| 384 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (high) | 0.2872 | — | — | — |
| 385 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE (Non-reasoning) | 0.2869 | — | — | — |
| 386 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3 0324 | 0.2857 | — | — | — |
| 387 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (Non-reasoning) | 0.2854 | 4,022.66 | 0.3413 | ❌ |
| 388 | <img src="https://artificialanalysis.ai/img/logos//img/logos/korea-telecom.png" width="18" alt="Korea Telecom" /> Korea Telecom | Mi:dm K 2.5 Pro | 0.2842 | — | — | — |
| 389 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 (Jan) | 0.2832 | — | — | — |
| 390 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Large 3 | 0.2826 | 1,621.64 | 0.2452 | ❌ |
| 391 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 4 Maverick | 0.2812 | 2,998.66 | 0.3095 | ❌ |
| 392 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3.1 | 0.2802 | — | — | — |
| 393 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-20b (high) | 0.2781 | 488.70 | 0.1351 | ❌ |
| 394 | <img src="https://artificialanalysis.ai/img/logos//img/logos/prime-intellect.svg" width="18" alt="Prime Intellect" /> Prime Intellect | INTELLECT-3 | 0.2774 | — | — | — |
| 395 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano Omni 30B A3B | 0.2769 | 4,687.50 | 0.3581 | ❌ |
| 396 | <img src="https://artificialanalysis.ai/img/logos//img/logos/trillionlabs.svg" width="18" alt="Trillion Labs" /> Trillion Labs | Tri-21B-think Preview | 0.2766 | — | — | — |
| 397 | <img src="https://artificialanalysis.ai/img/logos//img/logos/longcat.svg" width="18" alt="LongCat" /> LongCat | LongCat Flash Lite | 0.2749 | — | — | — |
| 398 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 30B A3B (Reasoning) | 0.2746 | 6,110.58 | 0.3874 | ❌ |
| 399 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B A3B 2507 | 0.2746 | 6,110.58 | 0.3874 | ❌ |
| 400 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-20b (low) | 0.2742 | 576.20 | 0.1486 | ❌ |
| 401 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.1 405B | 0.2731 | — | — | — |
| 402 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova Premier | 0.2722 | — | — | — |
| 403 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 2.6 Flash | 0.2716 | — | — | — |
| 404 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 mini | 0.2715 | 2,155.34 | 0.2745 | ❌ |
| 405 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 E4B (Non-reasoning) | 0.2711 | 65.89 | 0.0303 | ❌ |
| 406 | <img src="https://artificialanalysis.ai/img/logos//img/logos/trillionlabs.svg" width="18" alt="Trillion Labs" /> Trillion Labs | Tri-21B-Think | 0.2709 | — | — | — |
| 407 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.2 3B | 0.2659 | 387.44 | 0.1174 | ❌ |
| 408 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (Non-reasoning) | 0.2637 | 1,871.65 | 0.2599 | ❌ |
| 409 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Next 80B A3B | 0.2630 | 1,133.34 | 0.2097 | ❌ |
| 410 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 32B | 0.2627 | 519.77 | 0.1401 | ❌ |
| 411 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nousresearch.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 405B | 0.2610 | 8,052.88 | 0.4182 | ❌ |
| 412 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (medium) | 0.2585 | — | — | — |
| 413 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-1T | 0.2577 | — | — | — |
| 414 | <img src="https://artificialanalysis.ai/img/logos//img/logos/korea-telecom.png" width="18" alt="Korea Telecom" /> Korea Telecom | Mi:dm K 2.5 Pro Preview | 0.2573 | — | — | — |
| 415 | <img src="https://artificialanalysis.ai/img/logos//img/logos/motif.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif-2-12.7B | 0.2571 | — | — | — |
| 416 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-120b (low) | 0.2568 | 2,862.50 | 0.3046 | ❌ |
| 417 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.5 Haiku | 0.2544 | — | — | — |
| 418 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 8B (Reasoning) | 0.2540 | 5,349.52 | 0.3727 | ❌ |
| 419 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step3 VL 10B | 0.2523 | — | — | — |
| 420 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Super 49B v1.5 | 0.2501 | — | — | — |
| 421 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.0 Flash | 0.2499 | — | — | — |
| 422 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7-Flash (Non-reasoning) | 0.2497 | 671.12 | 0.1616 | ❌ |
| 423 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Devstral 2 | 0.2479 | — | — | — |
| 424 | <img src="https://artificialanalysis.ai/img/logos//img/logos/baidu.svg" width="18" alt="Baidu" /> Baidu | ERNIE 4.5 300B A47B | 0.2470 | — | — | — |
| 425 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Magistral Medium 1 | 0.2460 | — | — | — |
| 426 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Devstral Medium | 0.2444 | — | — | — |
| 427 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B 2507 | 0.2439 | — | — | — |
| 428 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (Non-reasoning) | 0.2433 | — | — | — |
| 429 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4 | 0.2433 | — | — | — |
| 430 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Small 4 (Non-reasoning) | 0.2428 | 599.88 | 0.1520 | ❌ |
| 431 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nousresearch.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 405B (Non-reasoning) | 0.2417 | 2,358.32 | 0.2840 | ❌ |
| 432 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder 30B A3B | 0.2404 | 1,844.26 | 0.2584 | ❌ |
| 433 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-8B-A1B | 0.2381 | — | — | — |
| 434 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 30B A3B | 0.2372 | 710.02 | 0.1665 | ❌ |
| 435 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6V (Non-reasoning) | 0.2367 | 2,519.77 | 0.2910 | ❌ |
| 436 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 E2B | 0.2353 | — | — | — |
| 437 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Omni 30B A3B (Reasoning) | 0.2348 | 2,563.22 | 0.2928 | ❌ |
| 438 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-2.6B | 0.2331 | — | — | — |
| 439 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B | 0.2307 | 21,387.02 | 0.5288 | ❌ |
| 440 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5V | 0.2300 | 5,870.91 | 0.3830 | ❌ |
| 441 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 12B v2 VL | 0.2293 | — | — | — |
| 442 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Large 2 (Nov) | 0.2283 | — | — | — |
| 443 | <img src="https://artificialanalysis.ai/img/logos//img/logos/tii.svg" width="18" alt="TII UAE" /> TII UAE | Falcon-H1R-7B | 0.2268 | — | — | — |
| 444 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Ultra | 0.2258 | — | — | — |
| 445 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Devstral Small 2 | 0.2246 | — | — | — |
| 446 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3 (Dec) | 0.2181 | — | — | — |
| 447 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova Pro | 0.2168 | — | — | — |
| 448 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nanbeige.png" width="18" alt="Nanbeige" /> Nanbeige | Nanbeige4.1-3B | 0.2166 | — | — | — |
| 449 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3.1 32B Think | 0.2160 | — | — | — |
| 450 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3.2 | 0.2157 | — | — | — |
| 451 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam 105B (high) | 0.2151 | — | — | — |
| 452 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.0 32B | 0.2142 | — | — | — |
| 453 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Magistral Small 1.2 | 0.2137 | — | — | — |
| 454 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (low) | 0.2127 | — | — | — |
| 455 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 9B V2 | 0.2122 | 422.12 | 0.1238 | ❌ |
| 456 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 2B | 0.2122 | — | — | — |
| 457 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-flash-2.0 | 0.2096 | — | — | — |
| 458 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Non-reasoning) | 0.2096 | 384.28 | 0.1168 | ❌ |
| 459 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Super 49B v1.5 (Non-reasoning) | 0.2080 | — | — | — |
| 460 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 4 Scout | 0.2071 | 521.72 | 0.1404 | ❌ |
| 461 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nousresearch.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 70B | 0.2059 | — | — | — |
| 462 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Devstral Small (May) | 0.2049 | — | — | — |
| 463 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 32B | 0.2045 | 1,688.46 | 0.2493 | ❌ |
| 464 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova Lite | 0.2043 | 333.15 | 0.1066 | ❌ |
| 465 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.3 Nemotron Super 49B | 0.2012 | — | — | — |
| 466 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 32B | 0.2009 | — | — | — |
| 467 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen2.5 72B | 0.2002 | — | — | — |
| 468 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 14B | 0.1995 | 10,693.51 | 0.4501 | ❌ |
| 469 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-flash-2.0 | 0.1994 | 369.40 | 0.1139 | ❌ |
| 470 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 8B | 0.1988 | 630.29 | 0.1561 | ❌ |
| 471 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B | 0.1973 | 6,110.58 | 0.3874 | ❌ |
| 472 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Magistral Small 1 | 0.1969 | — | — | — |
| 473 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Large 2 (Jul) | 0.1929 | — | — | — |
| 474 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Ministral 3 14B | 0.1924 | 414.39 | 0.1224 | ❌ |
| 475 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 2 | 0.1921 | — | — | — |
| 476 | <img src="https://artificialanalysis.ai/img/logos//img/logos/cohere.svg" width="18" alt="Cohere" /> Cohere | Command A | 0.1921 | 7,407.30 | 0.4089 | ❌ |
| 477 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Devstral Small | 0.1914 | — | — | — |
| 478 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B (Non-reasoning) | 0.1912 | 2,234.64 | 0.2783 | ❌ |
| 479 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.1 Nemotron 70B | 0.1899 | — | — | — |
| 480 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano 4B | 0.1885 | — | — | — |
| 481 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 4B (Reasoning) | 0.1873 | — | — | — |
| 482 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3 Haiku | 0.1862 | — | — | — |
| 483 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3.1 | 0.1853 | — | — | — |
| 484 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.3 Nemotron Super 49B (Non-reasoning) | 0.1847 | — | — | — |
| 485 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B A3B 2507 (Non-reasoning) | 0.1829 | 721.92 | 0.1679 | ❌ |
| 486 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B | 0.1815 | — | — | — |
| 487 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.1 70B | 0.1809 | 655.85 | 0.1596 | ❌ |
| 488 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 9B V2 (Non-reasoning) | 0.1807 | 185.05 | 0.0706 | ❌ |
| 489 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 32B (Non-reasoning) | 0.1792 | 579.68 | 0.1491 | ❌ |
| 490 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5V (Non-reasoning) | 0.1788 | 2,520.06 | 0.2910 | ❌ |
| 491 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 E2B (Non-reasoning) | 0.1787 | — | — | — |
| 492 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 2B (Non-reasoning) | 0.1770 | — | — | — |
| 493 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.1 30B | 0.1765 | — | — | — |
| 494 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3.1 32B Instruct | 0.1733 | — | — | — |
| 495 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Omni 30B A3B | 0.1716 | 804.37 | 0.1776 | ❌ |
| 496 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (minimal) | 0.1709 | 326.44 | 0.1051 | ❌ |
| 497 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B 2507 (Non-reasoning) | 0.1698 | — | — | — |
| 498 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.1 8B | 0.1680 | 42.43 | 0.0204 | ❌ |
| 499 | <img src="https://artificialanalysis.ai/img/logos//img/logos/celeris.svg" width="18" alt="Celeris" /> Celeris | Celeris-1 | 0.1658 | 1,056.01 | 0.2029 | ❌ |
| 500 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 32B Think | 0.1656 | — | — | — |
| 501 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o mini | 0.1652 | 1,151.88 | 0.2113 | ❌ |
| 502 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Llama 70B | 0.1648 | — | — | — |
| 503 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 nano | 0.1647 | 543.78 | 0.1438 | ❌ |
| 504 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.3 70B | 0.1646 | 7,563.43 | 0.4112 | ❌ |
| 505 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 14B | 0.1644 | — | — | — |
| 506 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi Linear 48B A3B Instruct | 0.1641 | — | — | — |
| 507 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Ministral 3 8B | 0.1627 | 311.79 | 0.1020 | ❌ |
| 508 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 2 (Non-reasoning) | 0.1627 | — | — | — |
| 509 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nousresearch.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 70B (Non-reasoning) | 0.1595 | — | — | — |
| 510 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai21.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba Reasoning 3B | 0.1592 | — | — | — |
| 511 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.0 32B (Non-reasoning) | 0.1570 | — | — | — |
| 512 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.1 8B | 0.1570 | — | — | — |
| 513 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova Micro | 0.1541 | 201.94 | 0.0753 | ❌ |
| 514 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 24B A2B | 0.1537 | — | — | — |
| 515 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai21.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba 1.7 Large | 0.1526 | — | — | — |
| 516 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 8B | 0.1519 | 5,349.52 | 0.3727 | ❌ |
| 517 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam 30B (high) | 0.1507 | — | — | — |
| 518 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3 | 0.1493 | — | — | — |
| 519 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 12B v2 VL (Non-reasoning) | 0.1490 | 546.74 | 0.1442 | ❌ |
| 520 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM-V 4.6 1.3B | 0.1488 | — | — | — |
| 521 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B (Non-reasoning) | 0.1445 | 702.25 | 0.1655 | ❌ |
| 522 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano (Non-reasoning) | 0.1418 | 631.58 | 0.1563 | ❌ |
| 523 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H Small | 0.1387 | 285.67 | 0.0962 | ❌ |
| 524 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 4B | 0.1383 | — | — | — |
| 525 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 27B | 0.1363 | — | — | — |
| 526 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 0528 Qwen3 8B | 0.1342 | — | — | — |
| 527 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Ministral 3 3B | 0.1328 | 215.13 | 0.0789 | ❌ |
| 528 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 14B (Non-reasoning) | 0.1325 | 1,135.76 | 0.2099 | ❌ |
| 529 | <img src="https://artificialanalysis.ai/img/logos//img/logos/microsoft.svg" width="18" alt="Microsoft" /> Microsoft | Phi-4 | 0.1278 | 371.08 | 0.1142 | ❌ |
| 530 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.1 Nemotron Nano 4B v1.1 | 0.1270 | — | — | — |
| 531 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 270M | 0.1248 | — | — | — |
| 532 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3 70B | 0.1197 | — | — | — |
| 533 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.2 11B (Vision) | 0.1192 | 375.91 | 0.1151 | ❌ |
| 534 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.2 3B | 0.1173 | — | — | — |
| 535 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 0.8B | 0.1164 | — | — | — |
| 536 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 7B Think | 0.1158 | — | — | — |
| 537 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-1.2B-Instruct | 0.1092 | — | — | — |
| 538 | <img src="https://artificialanalysis.ai/img/logos//img/logos/reka.svg" width="18" alt="Reka AI" /> Reka AI | Reka Flash 3 | 0.1087 | — | — | — |
| 539 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-mini-2.0 | 0.1083 | — | — | — |
| 540 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 2.6B | 0.1082 | — | — | — |
| 541 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 8B (Non-reasoning) | 0.1073 | 565.48 | 0.1470 | ❌ |
| 542 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Molmo2-8B | 0.1040 | — | — | — |
| 543 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam M | 0.1037 | — | — | — |
| 544 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai21.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba 1.7 Mini | 0.1025 | — | — | — |
| 545 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-1.2B-Thinking | 0.1011 | — | — | — |
| 546 | <img src="https://artificialanalysis.ai/img/logos//img/logos/microsoft.svg" width="18" alt="Microsoft" /> Microsoft | Phi-4 Mini | 0.0987 | 0.00 | 0.0000 | ❌ |
| 547 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 12B | 0.0985 | — | — | — |
| 548 | <img src="https://artificialanalysis.ai/img/logos//img/logos/swiss-ai-initiative.png" width="18" alt="Swiss AI Initiative" /> Swiss AI Initiative | Apertus 70B Instruct | 0.0942 | — | — | — |
| 549 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 0.8B (Non-reasoning) | 0.0939 | — | — | — |
| 550 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 7B | 0.0928 | — | — | — |
| 551 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | Exaone 4.0 1.2B | 0.0918 | — | — | — |
| 552 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | OLMo 2 32B | 0.0917 | — | — | — |
| 553 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H 1B | 0.0912 | — | — | — |
| 554 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.2 1B | 0.0901 | — | — | — |
| 555 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 1.7B | 0.0890 | — | — | — |
| 556 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.1 3B | 0.0873 | — | — | — |
| 557 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | Exaone 4.0 1.2B (Non-reasoning) | 0.0848 | — | — | — |
| 558 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 8B A1B | 0.0830 | — | — | — |
| 559 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 Micro | 0.0804 | — | — | — |
| 560 | <img src="https://artificialanalysis.ai/img/logos//img/logos/microsoft.svg" width="18" alt="Microsoft" /> Microsoft | Phi-3 Mini | 0.0754 | — | — | — |
| 561 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 3.3 8B | 0.0720 | — | — | — |
| 562 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-VL-1.6B | 0.0694 | — | — | — |
| 563 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 1B | 0.0687 | — | — | — |
| 564 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 350M | 0.0677 | — | — | — |
| 565 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 4B | 0.0668 | — | — | — |
| 566 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 1.2B | 0.0658 | — | — | — |
| 567 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 0.6B | 0.0652 | — | — | — |
| 568 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3 8B | 0.0649 | — | — | — |
| 569 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral 7B | 0.0625 | — | — | — |
| 570 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3n E4B | 0.0588 | — | — | — |
| 571 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 0.9B | 0.0577 | — | — | — |
| 572 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 1.7B (Non-reasoning) | 0.0570 | — | — | — |
| 573 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | OLMo 2 7B | 0.0568 | — | — | — |
| 574 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 1B | 0.0564 | — | — | — |
| 575 | <img src="https://artificialanalysis.ai/img/logos//img/logos/swiss-ai-initiative.png" width="18" alt="Swiss AI Initiative" /> Swiss AI Initiative | Apertus 8B Instruct | 0.0555 | — | — | — |
| 576 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H 350M | 0.0512 | — | — | — |
| 577 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Molmo 7B-D | 0.0480 | — | — | — |
| 578 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 0.6B (Non-reasoning) | 0.0440 | — | — | — |
| 579 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3n E2B | 0.0363 | — | — | — |
| 580 | <img src="https://artificialanalysis.ai/img/logos//img/logos/cohere.svg" width="18" alt="Cohere" /> Cohere | Tiny Aya Global | 0.0359 | — | — | — |
| 581 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 1.5B | 0.0000 | — | — | — |

## 品牌帕累托前沿连线（仅体现在图中）

以下十一个品牌在图中拥有单独的帕累托连线（较窄宽度，品牌主题色，图层高于总体灰色连线）。表中数量为**入图顶点数**——品牌前沿上低于总体前沿第一级的顶点同样不入图（本表与图例一致）：

| 品牌 | 主题色 | 品牌前沿模型数（入图） |
|------|--------|--------------|
| <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | `#cc785c` | 12 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | `#1f1f1f` | 12 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | `#0089f4` | 2 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | `#1c7ff8` | 2 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | `#34A853` | 6 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | `#736cd3` | 6 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | `#047AFE` | 5 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | `#ff7018` | 2 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | `#2243e6` | 3 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | `#EB3568` | 2 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | `#ff6900` | 2 |

## 评分方法

1. **20项评估指标**各自线性归一化到 [0,1]
   （AA Intelligence Index、GPQA Diamond、Humanity's Last Exam、MMMU Pro、IFBench Instruction Following、SciCode Coding、CritPt Physics、AA-LCR Long Context、AA Omniscience Index、AA-Omniscience Accuracy、AA-Omniscience Non-Hallucination、GDPval-AA Normalized、AA Analyst Agent、APEX-Agents-AA、ITBench-SRE、τ²-Bench Telecom、τ³-Bench Banking、Terminal-Bench Hard、Terminal-Bench 2.1、Terminal-Bench 4.0）
   > V18（2026-09-12）：AA 更新了基准列——新增 AA Analyst Agent、τ³-Bench Banking、Terminal-Bench 2.1 / 4.0 四项；AA Agentic Index 与 AA Coding Index 已从 AA 的数据源中移除，相应剔除。指标数由 18 → 20。
2. **综合能力值** = 所有有效归一化分数的算术平均
3. **综合能力再归一化**：线性映射到 [0,1]，性能最好的模型 = 1，最差的模型 = 0
4. **Pareto前沿** = 不被任何其他模型支配的模型（综合能力 ≥ 且成本 ≤，且至少一项严格更优；成本为 0 的免费模型同样参与——横轴左端恒为 0，免费模型是合法前沿候选）
5. **模型范围** = Status: All（含已弃用模型；缺少足够评估数据者不参与排名）
6. **图表纵轴基线（V17）**：图表的 y = 0 取总体帕累托前沿的第一级（最低能力；本例 y0 = 0.5121，即前沿左端点 Gemma 4 31B）；综合能力低于该级的模型不出现在图表中（表格不受影响）。图中纵坐标 chart_y = (能力 - y0)/(1 - y0)，因此前沿左端点恰好落在 (0, 0)、最优模型恰好为 y = 1。该过滤在横轴映射构建之前完成


## 横轴映射（对数映射，真零点，V21）与分布分析

横轴（单请求成本）为 **Y = A·ln(B·c+C)+D 对数映射**（B = 1；A、D 由端点解出；C = 218.73，r = B/C = 0.0045719 经网格搜索确定）：

```
x = 0                            当 c = 0（免费模型，真零点）
x = A·ln(c+C)+D                  当 c > 0（B = 1 并入；A、D 由端点解出）
```

其中 C = 218.73（r = B/C = 0.0045719），拟合集为 11 品牌前沿入图正成本模型（综合能力 ≥ 前沿第一级）的成本分布，目标为组内名次分位数（最小二乘误差 mse = 0.021995，最大偏离 0.2563）。该映射在 **y 基线过滤之后**构建（V17：先以帕累托前沿第一级为 y = 0、剔除低性能模型，再对入图模型建映射）。

**该映射保证：**

- **函数端点严格钉死**：c = 0 → x = 0；最大成本 → x = 1——函数经过 (0,0) 与 (1,1)；
- 各数量级区间的入图模型数：1–10: 0，10–100: 0，100–1k: 3，1k–10k: 56，10k–100k: 91，100k–1M: 20，1M–1.294M: 0
- **同倍率区间宽度相近**（对数轴性质）：1k→10k 与 100k→1M 同为 10 倍率，宽度相近（前者 56 个模型、后者 20 个）；与 V17 分位数映射不同，本图不追求均匀密度——密度不等如实显示；
- **左端恒为 0**（c = 0；1 个免费模型位于最左缘）
- 前沿最低正成本 803.86 → x = 0.1776（真实对数位置，不再钉 0；x = 0 恒为 c = 0 免费模型）；前沿最大成本 1,294,035 → x = 1.0000（= 1；高于前沿最大成本的模型不入图，仅表格保留）
- 中位数位置 0.493（≈ 0.5 居中）；左右两半模型数：左 90 / 右 82
- 横轴十分位模型数：1，3，10，24，52，39，21，14，4，4（对数映射下各十分位模型数自然不等）
- **10^x 数量级指示**（位置 = x(10^x)）：10^0 → 0.001，10^1 → 0.005，10^2 → 0.043，10^3 → 0.198，10^4 → 0.443，10^5 → 0.705，10^6 → 0.970

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
**模型总数（Status: All）**: 581 个参与排名（另有模型因评估数据不足未列入；总体帕累托前沿 15 个；图表入图 172 个——综合能力 ≥ 前沿第一级）  

## 图表说明（黑底）

（V17 起本说明置于文末，图表之后直接跟随模型表格。）

图表说明：**灰色实线** = 总体帕累托前沿；**彩色细线** = 十一个品牌的单独帕累托前沿（品牌主题色，图层高于总体连线；暗色品牌元素带窄白边；顶点按（横轴位置、能力升序）连接，等成本点自下而上）；品牌前沿模型圆点同样使用品牌颜色。模型名称/思考程度标注优先骑在连线之上（点的左/右两侧皆可，同一条线段可容纳两个标签——各贴各的点；文字与连线平行、中轴线重合，连线仅在文字两侧绘制）；骑线位被其他标签占据时自动「让位」——占用者挪到自己的另一个骑线位，双方都保持骑线；实在骑不上线时按四级优先依次退让（V16）：离点最近位置的上方/下方平行偏移 → 点的两条连线延长线上就近 → 两连线夹角扇区内就近。标签规则（V13/V15）：品牌前沿模型共享的前导块按「最长有效切点」剔除 —— 切点止于分界符，或止于字母且其后紧跟数字（如 Claude Opus 5 → Opus 5、GPT-5.6 Sol → 5.6 Sol、Kimi K2.6 → 2.6、Qwen3.8 Max → 3.8 Max、MiMo-V2.5 → 2.5、MiniMax-M2.1 → 2.1）；(non-reasoning) 简写为 (non)；同一模型在品牌连线上相邻出现 2 次以上时仅性能最低者保留全名、相邻较高者只标思考程度，不相邻的重复出现保留全名（每次重新计算）；标签位置与序列同向（V15）——品牌前沿上越靠右上的模型，其标签重心必须同时更靠右且更靠上（两分量都 >= 0，至少是 (0,0)，仅其一非负不算合格；初始放置违反时自动就近重摆，单标签无解（被前后邻居夹死）时按窗口级联重排整体挪动，均不产生新的重叠）。纵轴 y = 0 = 总体帕累托前沿第一级（y0 = 0.5121，前沿左端点 Gemma 4 31B 恰为 (0,0)），能力低于该级的 366 个模型、缺少成本数据的 43 个模型与成本高于品牌前沿最大值的模型不出现在图中；横轴为对数映射（见上文「横轴映射」节），10^x 数量级指示位于 x(10^x)，同一倍率区间的宽度相近（对数轴性质；本图不追求均匀密度）。
