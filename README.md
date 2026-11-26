# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

## 全部模型（综合能力从高到低，最优 = 1，最差 = 0）

共收录 **Status: All**（含已弃用）的全部模型；按重新归一化后的综合能力排序。「帕累托」列：✅ = 总体帕累托前沿模型，❌ = 被支配，— = 无成本数据无法判定。图表纵轴以总体帕累托前沿第一级（y0 = 0.5684，即前沿左端点 K2 Horizon 375B A23B）为 0：综合能力 ≥ 该级且有成本数据的 158 个模型入图，490 个能力低于第一级、12 个缺少成本数据的模型不出现在图中，成本高于品牌前沿最大值的模型同样不入图（本表不受影响，仍完整列出全部模型）。

| # | 品牌 | 模型 | 综合能力 | 单请求成本 | 横轴位置 | 帕累托 |
|---|------|------|---------|-----------|-----------|------|
| 1 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.2 (max) | 1.0000 | 1,061,350.58 | 1.0000 | ✅ |
| 2 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.2 Astra (max) | 0.9829 | 380,906.67 | 0.8741 | ✅ |
| 3 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.2 (xhigh) | 0.9663 | 285,212.98 | 0.8385 | ✅ |
| 4 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Neon (xhigh) | 0.9640 | 80,605.66 | 0.6835 | ✅ |
| 5 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.2 Astra (xhigh) | 0.9615 | 148,371.68 | 0.7583 | ❌ |
| 6 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Neon (high) | 0.9557 | 72,931.77 | 0.6713 | ✅ |
| 7 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.2 Astra (high) | 0.9516 | 77,649.40 | 0.6789 | ❌ |
| 8 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.2 (high) | 0.9497 | 134,680.37 | 0.7464 | ❌ |
| 9 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.2 Sol (max) | 0.9472 | 55,008.32 | 0.6368 | ✅ |
| 10 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Carbon (high) | 0.9441 | 85,872.33 | 0.6913 | ❌ |
| 11 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Carbon (medium) | 0.9260 | 51,762.77 | 0.6293 | ✅ |
| 12 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Neon (medium) | 0.9253 | 39,217.48 | 0.5954 | ✅ |
| 13 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (max) | 0.9212 | 851,369.43 | 0.9729 | ❌ |
| 14 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.2 Astra (medium) | 0.9164 | 35,082.90 | 0.5818 | ✅ |
| 15 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.2 Sol (xhigh) | 0.9158 | 25,319.49 | 0.5422 | ✅ |
| 16 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Hydrogen (xhigh) | 0.9151 | 66,820.11 | 0.6605 | ❌ |
| 17 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.2 (medium) | 0.9133 | 71,826.16 | 0.6694 | ❌ |
| 18 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.2 Sol (high) | 0.9087 | 13,455.90 | 0.4658 | ✅ |
| 19 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (xhigh) | 0.9007 | 157,121.13 | 0.7653 | ❌ |
| 20 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (max) | 0.8936 | 446,220.87 | 0.8935 | ❌ |
| 21 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.2 Sol (medium) | 0.8932 | 9,058.31 | 0.4184 | ✅ |
| 22 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.2 (low) | 0.8931 | 61,521.16 | 0.6504 | ❌ |
| 23 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (max) | 0.8929 | 66,422.16 | 0.6598 | ❌ |
| 24 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Carbon (low) | 0.8917 | 23,097.67 | 0.5310 | ❌ |
| 25 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Hydrogen (high) | 0.8908 | 31,015.81 | 0.5668 | ❌ |
| 26 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (max) | 0.8761 | 443,008.71 | 0.8926 | ❌ |
| 27 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (high) | 0.8649 | 61,929.65 | 0.6512 | ❌ |
| 28 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (xhigh) | 0.8639 | 35,260.06 | 0.5825 | ❌ |
| 29 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Wonder Full (max) | 0.8600 | — | — | — |
| 30 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Neon (low) | 0.8582 | 30,535.70 | 0.5649 | ❌ |
| 31 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.2 Astra (low) | 0.8570 | 31,870.51 | 0.5702 | ❌ |
| 32 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (max) | 0.8530 | 745,111.08 | 0.9565 | ❌ |
| 33 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (high) | 0.8474 | 20,113.20 | 0.5143 | ❌ |
| 34 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Argon (high) | 0.8474 | 92,390.31 | 0.7002 | ❌ |
| 35 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (xhigh) | 0.8472 | 223,279.41 | 0.8085 | ❌ |
| 36 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (xhigh) | 0.8399 | 319,711.31 | 0.8526 | ❌ |
| 37 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (medium) | 0.8361 | 41,892.07 | 0.6035 | ❌ |
| 38 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Hydrogen (medium) | 0.8349 | 22,486.14 | 0.5278 | ❌ |
| 39 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (high) | 0.8329 | 142,108.73 | 0.7530 | ❌ |
| 40 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3.1 Pro | 0.8276 | 65,044.37 | 0.6573 | ❌ |
| 41 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (xhigh) | 0.8271 | 50,003.89 | 0.6251 | ❌ |
| 42 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen4 Max | 0.8218 | 73,603.36 | 0.6724 | ❌ |
| 43 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Terra (max) | 0.8175 | 52,319.64 | 0.6306 | ❌ |
| 44 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (medium) | 0.8164 | 56,051.19 | 0.6391 | ❌ |
| 45 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (medium) | 0.8163 | 9,672.47 | 0.4262 | ❌ |
| 46 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Wonder (max) | 0.8154 | 48,956.24 | 0.6225 | ❌ |
| 47 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.2 Sol (low) | 0.8154 | 8,288.05 | 0.4079 | ✅ |
| 48 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (high) | 0.8127 | 79,402.11 | 0.6817 | ❌ |
| 49 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (max) | 0.8105 | 49,700.06 | 0.6244 | ❌ |
| 50 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Argon (medium) | 0.8052 | 35,939.36 | 0.5848 | ❌ |
| 51 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Wonder (high) | 0.8009 | 29,225.52 | 0.5596 | ❌ |
| 52 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (max) | 0.7859 | 96,572.15 | 0.7057 | ❌ |
| 53 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (medium) | 0.7845 | 56,783.78 | 0.6406 | ❌ |
| 54 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Terra (xhigh) | 0.7842 | 13,506.46 | 0.4662 | ❌ |
| 55 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (high) | 0.7722 | 21,019.53 | 0.5196 | ❌ |
| 56 | <img src="https://artificialanalysis.ai/img/logos/tencent-hy.svg" width="18" alt="Tencent" /> Tencent | Tencent Hy4 | 0.7709 | 30,262.88 | 0.5638 | ❌ |
| 57 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (low) | 0.7649 | 51,109.86 | 0.6278 | ❌ |
| 58 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Terra (high) | 0.7627 | 7,144.39 | 0.3904 | ✅ |
| 59 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Haiku 5.5 (max) | 0.7612 | 23,838.31 | 0.5348 | ❌ |
| 60 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Ember (max) | 0.7609 | 1,259.48 | 0.1989 | ✅ |
| 61 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.3 (max) | 0.7566 | 19,643.82 | 0.5114 | ❌ |
| 62 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.7 (xhigh) | 0.7557 | 33,699.89 | 0.5769 | ❌ |
| 63 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (max) | 0.7536 | 92,296.68 | 0.7001 | ❌ |
| 64 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (low) | 0.7495 | 48,620.76 | 0.6217 | ❌ |
| 65 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Ember (xhigh) | 0.7474 | 1,033.37 | 0.1798 | ✅ |
| 66 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.6-Pro | 0.7431 | 1,872.99 | 0.2394 | ❌ |
| 67 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.7 (high) | 0.7413 | 27,515.71 | 0.5523 | ❌ |
| 68 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Terra (medium) | 0.7403 | 5,343.70 | 0.3564 | ❌ |
| 69 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5 | 0.7380 | 319,874.07 | 0.8526 | ❌ |
| 70 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (low) | 0.7362 | 8,781.48 | 0.4148 | ❌ |
| 71 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (low) | 0.7349 | 26,660.10 | 0.5484 | ❌ |
| 72 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3 (max) | 0.7328 | 31,011.52 | 0.5668 | ❌ |
| 73 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (xhigh) | 0.7275 | 63,659.03 | 0.6546 | ❌ |
| 74 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (high) | 0.7252 | 11,200.05 | 0.4438 | ❌ |
| 75 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash 1017 (max) | 0.7243 | 9,483.87 | 0.4239 | ❌ |
| 76 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Hydrogen (low) | 0.7238 | 12,270.48 | 0.4547 | ❌ |
| 77 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (xhigh) | 0.7199 | 24,430.53 | 0.5378 | ❌ |
| 78 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 Max (0902) | 0.7195 | 33,278.21 | 0.5754 | ❌ |
| 79 | <img src="https://artificialanalysis.ai/img/logos/thinking-machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling 2 Small | 0.7170 | 4,765.73 | 0.3431 | ❌ |
| 80 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (high) | 0.7145 | 45,296.68 | 0.6130 | ❌ |
| 81 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (max) | 0.7132 | 4,595.22 | 0.3389 | ❌ |
| 82 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3 (max) | 0.7119 | 26,091.31 | 0.5458 | ❌ |
| 83 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Haiku 5.5 (xhigh) | 0.7116 | 5,655.06 | 0.3630 | ❌ |
| 84 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.3 (xhigh) | 0.7102 | 15,591.75 | 0.4835 | ❌ |
| 85 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (xhigh) | 0.7058 | 50,588.06 | 0.6265 | ❌ |
| 86 | <img src="https://artificialanalysis.ai/img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step 5 Preview | 0.7054 | 2,470.71 | 0.2692 | ❌ |
| 87 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.7 (low) | 0.7046 | 15,283.75 | 0.4811 | ❌ |
| 88 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (max) | 0.7041 | 81,040.47 | 0.6842 | ❌ |
| 89 | <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M3.1-Flash | 0.7035 | 4,213.81 | 0.3290 | ❌ |
| 90 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (xhigh) | 0.7016 | 21,252.13 | 0.5209 | ❌ |
| 91 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (high) | 0.7001 | 14,425.83 | 0.4741 | ❌ |
| 92 | <img src="https://artificialanalysis.ai/img/logos/joy-ai.svg" width="18" alt="Joy Future Academy" /> Joy Future Academy | JoyAI-VL-Preview | 0.6993 | — | — | — |
| 93 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.1 Flash 1019 | 0.6980 | — | — | — |
| 94 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (high) | 0.6916 | 37,104.93 | 0.5887 | ❌ |
| 95 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (medium) | 0.6895 | 8,440.02 | 0.4101 | ❌ |
| 96 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (medium) | 0.6892 | 30,774.59 | 0.5659 | ❌ |
| 97 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (high) | 0.6889 | 16,917.15 | 0.4933 | ❌ |
| 98 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash (max) | 0.6883 | 9,887.53 | 0.4289 | ❌ |
| 99 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash 1017 (high) | 0.6832 | 4,694.96 | 0.3414 | ❌ |
| 100 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (medium) | 0.6824 | 14,698.98 | 0.4764 | ❌ |
| 101 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3-Flash (max) | 0.6814 | 2,430.85 | 0.2674 | ❌ |
| 102 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Terra (low) | 0.6805 | 4,827.89 | 0.3446 | ❌ |
| 103 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (xhigh) | 0.6787 | 94,032.72 | 0.7024 | ❌ |
| 104 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (medium) | 0.6770 | 15,821.77 | 0.4853 | ❌ |
| 105 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 Max | 0.6745 | 41,292.31 | 0.6017 | ❌ |
| 106 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.8 (max) | 0.6744 | 78,666.70 | 0.6805 | ❌ |
| 107 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Haiku 5.5 (high) | 0.6712 | 2,714.86 | 0.2795 | ❌ |
| 108 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.1 Flash | 0.6711 | 3,023.06 | 0.2914 | ❌ |
| 109 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (high) | 0.6706 | — | — | — |
| 110 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (medium) | 0.6679 | 29,240.63 | 0.5597 | ❌ |
| 111 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Large 4 (high) | 0.6677 | 14,068.58 | 0.4711 | ❌ |
| 112 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 2.4T A95B | 0.6659 | 34,414.42 | 0.5795 | ❌ |
| 113 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (medium) | 0.6657 | — | — | — |
| 114 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-3.2-air | 0.6563 | — | — | — |
| 115 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Large 4 Preview | 0.6560 | 11,445.38 | 0.4463 | ❌ |
| 116 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Terra (non-reasoning) | 0.6553 | 4,618.66 | 0.3395 | ❌ |
| 117 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8-Flash-Next | 0.6538 | 3,151.84 | 0.2961 | ❌ |
| 118 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.5 (high) | 0.6527 | 12,179.71 | 0.4538 | ❌ |
| 119 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (max) | 0.6516 | 5,644.72 | 0.3627 | ❌ |
| 120 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (high) | 0.6504 | 48,869.86 | 0.6223 | ❌ |
| 121 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.6-Flash | 0.6472 | 516.29 | 0.1201 | ✅ |
| 122 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark Open (xhigh) | 0.6468 | 10,944.43 | 0.4410 | ❌ |
| 123 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Large 4 (medium) | 0.6457 | 9,615.28 | 0.4255 | ❌ |
| 124 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (xhigh) | 0.6440 | 1,432.72 | 0.2118 | ❌ |
| 125 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro 0813 (max) | 0.6430 | 19,658.19 | 0.5115 | ❌ |
| 126 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.2 (xhigh) | 0.6428 | 10,914.15 | 0.4407 | ❌ |
| 127 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (xhigh) | 0.6415 | 28,277.90 | 0.5556 | ❌ |
| 128 | <img src="https://artificialanalysis.ai/img/logos/sapiens.svg" width="18" alt="Sapiens AI" /> Sapiens AI | Agnes 2.5 Pro Theta | 0.6361 | 583.49 | 0.1297 | ❌ |
| 129 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (low) | 0.6341 | 10,791.94 | 0.4393 | ❌ |
| 130 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (max) | 0.6329 | 141,451.59 | 0.7525 | ❌ |
| 131 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (low) | 0.6320 | 3,786.71 | 0.3168 | ❌ |
| 132 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro 0813 (high) | 0.6313 | 23,408.31 | 0.5326 | ❌ |
| 133 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Haiku 5.5 (medium) | 0.6300 | 1,477.71 | 0.2149 | ❌ |
| 134 | <img src="https://artificialanalysis.ai/img/logos/thinking-machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling 2 Mini | 0.6300 | 1,045.06 | 0.1809 | ❌ |
| 135 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (low) | 0.6289 | 27,195.70 | 0.5509 | ❌ |
| 136 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (high) | 0.6266 | 1,117.14 | 0.1872 | ❌ |
| 137 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (medium) | 0.6246 | — | — | — |
| 138 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (xhigh) | 0.6236 | 123,919.52 | 0.7362 | ❌ |
| 139 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (medium) | 0.6230 | 29,809.88 | 0.5620 | ❌ |
| 140 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.7 (max) | 0.6203 | 60,666.52 | 0.6487 | ❌ |
| 141 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash 0731 (max) | 0.6168 | 1,109.83 | 0.1866 | ❌ |
| 142 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (xhigh) | 0.6144 | 3,765.86 | 0.3161 | ❌ |
| 143 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (high) | 0.6133 | 15,705.03 | 0.4844 | ❌ |
| 144 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3 (low) | 0.6127 | 7,881.10 | 0.4019 | ❌ |
| 145 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.1 Pro Preview | 0.6106 | 29,040.67 | 0.5588 | ❌ |
| 146 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (low) | 0.6097 | 25,645.59 | 0.5437 | ❌ |
| 147 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (xhigh) | 0.6096 | 25,035.93 | 0.5408 | ❌ |
| 148 | <img src="https://artificialanalysis.ai/img/logos/nanbeige.png" width="18" alt="Nanbeige" /> Nanbeige | Nanbeige4.3-33B | 0.6089 | — | — | — |
| 149 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (high) | 0.6082 | 22,952.47 | 0.5303 | ❌ |
| 150 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.6 Flash (high) | 0.6066 | 10,765.64 | 0.4390 | ❌ |
| 151 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (low) | 0.6054 | 10,401.15 | 0.4349 | ❌ |
| 152 | <img src="https://artificialanalysis.ai/img/logos/china-mobile.png" width="18" alt="China Mobile" /> China Mobile | JT-4.1 Flash 236B A21B 0709 | 0.6053 | — | — | — |
| 153 | <img src="https://artificialanalysis.ai/img/logos/china-mobile.png" width="18" alt="China Mobile" /> China Mobile | JT-4.1 Flash 236B A21B | 0.6040 | — | — | — |
| 154 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (xhigh) | 0.6028 | 31,599.17 | 0.5691 | ❌ |
| 155 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.2 (max) | 0.6026 | 14,330.56 | 0.4733 | ❌ |
| 156 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash Vision (max) | 0.5985 | 10,231.52 | 0.4329 | ❌ |
| 157 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (medium) | 0.5970 | 752.97 | 0.1510 | ❌ |
| 158 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (low) | 0.5952 | 12,542.87 | 0.4573 | ❌ |
| 159 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.1 (xhigh) | 0.5952 | 14,095.84 | 0.4713 | ❌ |
| 160 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (low) | 0.5937 | — | — | — |
| 161 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.3 Codex (xhigh) | 0.5897 | 62,177.58 | 0.6517 | ❌ |
| 162 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3 (low) | 0.5891 | 12,144.43 | 0.4534 | ❌ |
| 163 | <img src="https://artificialanalysis.ai/img/logos/reflection.svg" width="18" alt="Reflection" /> Reflection | Beam 1.0 | 0.5868 | 4,609.86 | 0.3393 | ❌ |
| 164 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (high) | 0.5858 | 2,067.27 | 0.2499 | ❌ |
| 165 | <img src="https://artificialanalysis.ai/img/logos/sapiens.svg" width="18" alt="Sapiens AI" /> Sapiens AI | Agnes 2.5 Pro Beta | 0.5814 | — | — | — |
| 166 | <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M3 | 0.5807 | 12,619.85 | 0.4581 | ❌ |
| 167 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Haiku 5.5 (low) | 0.5768 | 1,053.71 | 0.1816 | ❌ |
| 168 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (high) | 0.5736 | 24,374.02 | 0.5375 | ❌ |
| 169 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (max) | 0.5710 | 11,872.31 | 0.4507 | ❌ |
| 170 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 375B A23B | 0.5684 | 0.00 | 0.0000 | ✅ |
| 171 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (medium) | 0.5655 | 12,479.95 | 0.4567 | ❌ |
| 172 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.7 Max | 0.5648 | 22,783.81 | 0.5294 | ❌ |
| 173 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (max) | 0.5605 | 123,791.82 | 0.7361 | ❌ |
| 174 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.6 (max) | 0.5534 | 44,289.36 | 0.6103 | ❌ |
| 175 | <img src="https://artificialanalysis.ai/img/logos/apodex.svg" width="18" alt="Apodex" /> Apodex | Apodex 1.1 | 0.5496 | 9,370.47 | 0.4225 | ❌ |
| 176 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (medium) | 0.5495 | 20,702.95 | 0.5178 | ❌ |
| 177 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (medium) | 0.5492 | 7,248.19 | 0.3921 | ❌ |
| 178 | <img src="https://artificialanalysis.ai/img/logos/motif.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif 3 (Beta) | 0.5437 | — | — | — |
| 179 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (non-reasoning) | 0.5428 | 9,951.88 | 0.4296 | ❌ |
| 180 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.6 | 0.5412 | 17,257.72 | 0.4957 | ❌ |
| 181 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3.5 Super VL | 0.5383 | 2,701.39 | 0.2790 | ❌ |
| 182 | <img src="https://artificialanalysis.ai/img/logos/thinking-machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling (xhigh) | 0.5380 | 10,242.65 | 0.4331 | ❌ |
| 183 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (medium) | 0.5349 | 12,313.29 | 0.4551 | ❌ |
| 184 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark | 0.5346 | — | — | — |
| 185 | <img src="https://artificialanalysis.ai/img/logos/thinking-machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling Small | 0.5344 | 3,697.14 | 0.3141 | ❌ |
| 186 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (low) | 0.5341 | 25,056.70 | 0.5409 | ❌ |
| 187 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 32B | 0.5340 | — | — | — |
| 188 | <img src="https://artificialanalysis.ai/img/logos/motif.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif 3 | 0.5335 | — | — | — |
| 189 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (xhigh) | 0.5310 | 96,304.49 | 0.7053 | ❌ |
| 190 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (xhigh) | 0.5307 | 92,925.05 | 0.7009 | ❌ |
| 191 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (low) | 0.5306 | 4,327.83 | 0.3320 | ❌ |
| 192 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (low) | 0.5293 | 13,467.64 | 0.4659 | ❌ |
| 193 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.7 (non-reasoning, high) | 0.5286 | 23,974.70 | 0.5355 | ❌ |
| 194 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.7 Code | 0.5281 | 10,269.34 | 0.4334 | ❌ |
| 195 | <img src="https://artificialanalysis.ai/img/logos/thinking-machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling (high) | 0.5262 | 9,065.28 | 0.4185 | ❌ |
| 196 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (high) | 0.5255 | — | — | — |
| 197 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 Codex (xhigh) | 0.5244 | 58,854.95 | 0.6450 | ❌ |
| 198 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (max) | 0.5232 | 446.23 | 0.1093 | ❌ |
| 199 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.7 Plus | 0.5227 | 5,776.35 | 0.3654 | ❌ |
| 200 | <img src="https://artificialanalysis.ai/img/logos/tencent-hy.svg" width="18" alt="Tencent" /> Tencent | Hy3 | 0.5207 | 1,981.67 | 0.2454 | ❌ |
| 201 | <img src="https://artificialanalysis.ai/img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 4 | 0.5195 | 4,386.31 | 0.3336 | ❌ |
| 202 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3 Pro Preview (high) | 0.5181 | — | — | — |
| 203 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash 1017 (non-reasoning) | 0.5162 | 1,179.04 | 0.1924 | ❌ |
| 204 | <img src="https://artificialanalysis.ai/img/logos/nex.svg" width="18" alt="Nex AGI" /> Nex AGI | Nex-N2-Pro | 0.5148 | — | — | — |
| 205 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3 Flash | 0.5138 | 4,981.08 | 0.3482 | ❌ |
| 206 | <img src="https://artificialanalysis.ai/img/logos/multiversecomputing.svg" width="18" alt="Multiverse Computing" /> Multiverse Computing | Quasar 438B (max) | 0.5136 | — | — | — |
| 207 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 Max Preview | 0.5130 | — | — | — |
| 208 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5-Pro | 0.5107 | — | — | — |
| 209 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok Build 0.1 0616 | 0.5107 | — | — | — |
| 210 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash-Lite | 0.5084 | 5,178.12 | 0.3527 | ❌ |
| 211 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 v2 | 0.5074 | 8,094.78 | 0.4051 | ❌ |
| 212 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon MoVA 36B A4B | 0.5057 | — | — | — |
| 213 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (low) | 0.5034 | 16,294.05 | 0.4888 | ❌ |
| 214 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (low) | 0.5032 | 590.03 | 0.1306 | ❌ |
| 215 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro 0813 (non-reasoning) | 0.5031 | 4,045.53 | 0.3243 | ❌ |
| 216 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 Plus | 0.5030 | 7,391.99 | 0.3944 | ❌ |
| 217 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.1 | 0.5025 | 11,305.48 | 0.4449 | ❌ |
| 218 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (medium) | 0.5023 | 1,305.83 | 0.2025 | ❌ |
| 219 | <img src="https://artificialanalysis.ai/img/logos/thinking-machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling Small (high) | 0.5022 | 3,011.25 | 0.2910 | ❌ |
| 220 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-3.0-flash-VL | 0.4998 | — | — | — |
| 221 | <img src="https://artificialanalysis.ai/img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Mini 4 | 0.4994 | 1,780.64 | 0.2341 | ❌ |
| 222 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (non-reasoning) | 0.4984 | 23,982.83 | 0.5356 | ❌ |
| 223 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (high) | 0.4970 | — | — | — |
| 224 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Ultra | 0.4955 | 5,377.40 | 0.3571 | ❌ |
| 225 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 | 0.4946 | — | — | — |
| 226 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (high) | 0.4920 | 6,757.88 | 0.3838 | ❌ |
| 227 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (low) | 0.4910 | 10,495.70 | 0.4360 | ❌ |
| 228 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (medium) | 0.4872 | 5,956.00 | 0.3690 | ❌ |
| 229 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-3.0-flash-Fin | 0.4861 | — | — | — |
| 230 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (xhigh) | 0.4843 | 10,983.54 | 0.4414 | ❌ |
| 231 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 397B A17B | 0.4834 | 9,519.51 | 0.4244 | ❌ |
| 232 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 Instant (June 2026) | 0.4830 | 30,553.05 | 0.5650 | ❌ |
| 233 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5 | 0.4787 | 10,609.72 | 0.4373 | ❌ |
| 234 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Pro | 0.4778 | — | — | — |
| 235 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Glimmer (high) | 0.4746 | 3,100.96 | 0.2943 | ❌ |
| 236 | <img src="https://artificialanalysis.ai/img/logos/sktelecom.svg" width="18" alt="SK Telecom" /> SK Telecom | A.X-K2 | 0.4740 | — | — | — |
| 237 | <img src="https://artificialanalysis.ai/img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Open2 250B | 0.4725 | — | — | — |
| 238 | <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.7 | 0.4719 | 1,961.06 | 0.2443 | ❌ |
| 239 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5 | 0.4705 | — | — | — |
| 240 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 27B | 0.4679 | 8,640.85 | 0.4128 | ❌ |
| 241 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.5 | 0.4652 | 42,382.78 | 0.6049 | ❌ |
| 242 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (non-reasoning) | 0.4648 | 523.56 | 0.1212 | ❌ |
| 243 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 27B | 0.4639 | 3,170.56 | 0.2967 | ❌ |
| 244 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 (high) | 0.4629 | 50,792.49 | 0.6270 | ❌ |
| 245 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 7B | 0.4617 | — | — | — |
| 246 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.5 | 0.4591 | 7,854.05 | 0.4015 | ❌ |
| 247 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash (non-reasoning) | 0.4576 | 1,103.56 | 0.1860 | ❌ |
| 248 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (medium) | 0.4573 | 14,631.92 | 0.4758 | ❌ |
| 249 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.0 Flash | 0.4560 | 665.91 | 0.1406 | ❌ |
| 250 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (non-reasoning) | 0.4558 | 4,264.83 | 0.3303 | ❌ |
| 251 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (low) | 0.4554 | 1,206.85 | 0.1947 | ❌ |
| 252 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (high) | 0.4548 | 60,670.38 | 0.6487 | ❌ |
| 253 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5-Turbo | 0.4540 | — | — | — |
| 254 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (non-reasoning) | 0.4515 | 9,789.47 | 0.4277 | ❌ |
| 255 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 Codex (high) | 0.4511 | 23,666.05 | 0.5340 | ❌ |
| 256 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (non-reasoning) | 0.4504 | 12,258.88 | 0.4546 | ❌ |
| 257 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM3-1.7B | 0.4481 | 1,501.82 | 0.2165 | ❌ |
| 258 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 31B | 0.4465 | 0.00 | 0.0000 | ❌ |
| 259 | <img src="https://artificialanalysis.ai/img/logos/kwaikat.svg" width="18" alt="KwaiKAT" /> KwaiKAT | KAT-Coder-Pro V2 | 0.4461 | — | — | — |
| 260 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3.5 Bolt 74B-A9B | 0.4460 | — | — | — |
| 261 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Omni-0327 | 0.4445 | — | — | — |
| 262 | <img src="https://artificialanalysis.ai/img/logos/tencent-hy.svg" width="18" alt="Tencent" /> Tencent | Hy3-preview | 0.4438 | — | — | — |
| 263 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.1 Flash-Lite | 0.4417 | 6,897.27 | 0.3862 | ❌ |
| 264 | <img src="https://artificialanalysis.ai/img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step 3.7 Flash | 0.4400 | 2,863.37 | 0.2854 | ❌ |
| 265 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 Instant (May 2026) | 0.4394 | — | — | — |
| 266 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max Thinking | 0.4390 | — | — | — |
| 267 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (medium) | 0.4386 | 24,711.25 | 0.5392 | ❌ |
| 268 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Speciale | 0.4383 | — | — | — |
| 269 | <img src="https://artificialanalysis.ai/img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE 2.0 | 0.4370 | — | — | — |
| 270 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 Codex (high) | 0.4360 | 20,099.30 | 0.5142 | ❌ |
| 271 | <img src="https://artificialanalysis.ai/img/logos/china-mobile.png" width="18" alt="China Mobile" /> China Mobile | JT-4.1 Flash 236B A21B 0709 (non-reasoning) | 0.4352 | — | — | — |
| 272 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (minimal) | 0.4348 | 10,682.78 | 0.4381 | ❌ |
| 273 | <img src="https://artificialanalysis.ai/img/logos/longcat.svg" width="18" alt="LongCat" /> LongCat | LongCat 2.0 | 0.4344 | 9,234.70 | 0.4207 | ❌ |
| 274 | <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.5 | 0.4337 | 2,691.50 | 0.2785 | ❌ |
| 275 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Sonnet | 0.4335 | 26,893.79 | 0.5495 | ❌ |
| 276 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 122B A10B | 0.4309 | 6,867.85 | 0.3857 | ❌ |
| 277 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Medium 3.5 | 0.4302 | 24,223.39 | 0.5368 | ❌ |
| 278 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 35B A3B | 0.4302 | 4,945.82 | 0.3474 | ❌ |
| 279 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (non-reasoning) | 0.4285 | 24,302.43 | 0.5372 | ❌ |
| 280 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 3.7B | 0.4279 | — | — | — |
| 281 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7 | 0.4267 | 10,703.10 | 0.4383 | ❌ |
| 282 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.6 (non-reasoning, high) | 0.4245 | 24,380.09 | 0.5376 | ❌ |
| 283 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash (Feb 2026) | 0.4233 | — | — | — |
| 284 | <img src="https://artificialanalysis.ai/img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step 3.5 Flash 2603 | 0.4195 | 1,187.50 | 0.1931 | ❌ |
| 285 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 | 0.4193 | 750.56 | 0.1508 | ❌ |
| 286 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.1 (non-reasoning) | 0.4185 | 6,721.84 | 0.3832 | ❌ |
| 287 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3 Pro Preview (low) | 0.4174 | — | — | — |
| 288 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 35B A3B | 0.4161 | 3,579.28 | 0.3104 | ❌ |
| 289 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-2.6-1T | 0.4160 | — | — | — |
| 290 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 | 0.4149 | 26,196.83 | 0.5463 | ❌ |
| 291 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (low) | 0.4145 | 5,167.90 | 0.3525 | ❌ |
| 292 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Omni | 0.4135 | — | — | — |
| 293 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Haiku | 0.4130 | 15,625.65 | 0.4837 | ❌ |
| 294 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 Thinking | 0.4104 | 12,492.57 | 0.4568 | ❌ |
| 295 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o3 | 0.4076 | 15,220.20 | 0.4806 | ❌ |
| 296 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (medium) | 0.4071 | 6,554.26 | 0.3802 | ❌ |
| 297 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM 5V Turbo | 0.4061 | — | — | — |
| 298 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash | 0.4022 | — | — | — |
| 299 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (high) | 0.3998 | 8,781.51 | 0.4148 | ❌ |
| 300 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3.5 Lightning | 0.3980 | 1,393.71 | 0.2090 | ❌ |
| 301 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM3-VL-2B | 0.3928 | 1,506.83 | 0.2169 | ❌ |
| 302 | <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.1 | 0.3925 | — | — | — |
| 303 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.6 (non-reasoning) | 0.3910 | 5,015.79 | 0.3490 | ❌ |
| 304 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (non-reasoning, high) | 0.3861 | 14,844.86 | 0.4776 | ❌ |
| 305 | <img src="https://artificialanalysis.ai/img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | G9v3-39A5B | 0.3859 | — | — | — |
| 306 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 27B (non-reasoning) | 0.3849 | 3,841.48 | 0.3184 | ❌ |
| 307 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 Codex mini (high) | 0.3847 | 5,085.47 | 0.3506 | ❌ |
| 308 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 26B A4B | 0.3836 | 1,643.33 | 0.2258 | ❌ |
| 309 | <img src="https://artificialanalysis.ai/img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step 3.5 Flash | 0.3817 | 1,098.36 | 0.1856 | ❌ |
| 310 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 122B A10B (non-reasoning) | 0.3815 | 3,499.18 | 0.3078 | ❌ |
| 311 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 Terminus | 0.3804 | — | — | — |
| 312 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Pro | 0.3786 | 29,398.12 | 0.5603 | ❌ |
| 313 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 397B A17B (non-reasoning) | 0.3770 | 2,664.26 | 0.2774 | ❌ |
| 314 | <img src="https://artificialanalysis.ai/img/logos/cohere.svg" width="18" alt="Cohere" /> Cohere | Command A+ | 0.3766 | 0.00 | 0.0000 | ❌ |
| 315 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 27B (non-reasoning) | 0.3760 | 1,545.38 | 0.2194 | ❌ |
| 316 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-120b (high) | 0.3760 | 2,560.37 | 0.2731 | ❌ |
| 317 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (non-reasoning, low) | 0.3749 | 14,032.04 | 0.4708 | ❌ |
| 318 | <img src="https://artificialanalysis.ai/img/logos/kwaikat.svg" width="18" alt="KwaiKAT" /> KwaiKAT | KAT-Coder-Pro V1 | 0.3727 | — | — | — |
| 319 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (low) | 0.3711 | 13,563.30 | 0.4667 | ❌ |
| 320 | <img src="https://artificialanalysis.ai/img/logos/cohere.svg" width="18" alt="Cohere" /> Cohere | North Mini Code | 0.3700 | 0.00 | 0.0000 | ❌ |
| 321 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (medium) | 0.3664 | 1,814.71 | 0.2361 | ❌ |
| 322 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (medium) | 0.3664 | 3,282.64 | 0.3006 | ❌ |
| 323 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Super | 0.3658 | 7,051.46 | 0.3888 | ❌ |
| 324 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.2 30B | 0.3620 | — | — | — |
| 325 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.5 (non-reasoning) | 0.3616 | 25,044.19 | 0.5408 | ❌ |
| 326 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 35B A3B (non-reasoning) | 0.3615 | 1,961.89 | 0.2443 | ❌ |
| 327 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.2 (non-reasoning) | 0.3604 | 5,711.18 | 0.3641 | ❌ |
| 328 | <img src="https://artificialanalysis.ai/img/logos/inceptionlabs.svg" width="18" alt="Inception" /> Inception | Mercury 2.5 | 0.3603 | 1,517.24 | 0.2176 | ❌ |
| 329 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (non-reasoning) | 0.3575 | 1,178.93 | 0.1924 | ❌ |
| 330 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.1 Fast | 0.3573 | — | — | — |
| 331 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3 Flash (non-reasoning) | 0.3567 | 2,734.08 | 0.2803 | ❌ |
| 332 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Small 4 | 0.3560 | 1,779.68 | 0.2341 | ❌ |
| 333 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.1 Opus | 0.3543 | — | — | — |
| 334 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.0 Tiny | 0.3543 | 0.00 | 0.0000 | ❌ |
| 335 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 9B | 0.3529 | 843.64 | 0.1611 | ❌ |
| 336 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 Omni Plus | 0.3505 | 3,399.42 | 0.3046 | ❌ |
| 337 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Exp | 0.3490 | — | — | — |
| 338 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 12B | 0.3479 | — | — | — |
| 339 | <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2 | 0.3474 | 1,427.99 | 0.2114 | ❌ |
| 340 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6 | 0.3467 | 7,469.95 | 0.3956 | ❌ |
| 341 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o4-mini (high) | 0.3457 | 12,389.50 | 0.4558 | ❌ |
| 342 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (non-reasoning) | 0.3450 | 15,229.34 | 0.4807 | ❌ |
| 343 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Opus | 0.3450 | — | — | — |
| 344 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Sonnet | 0.3430 | — | — | — |
| 345 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 Fast | 0.3404 | — | — | — |
| 346 | <img src="https://artificialanalysis.ai/img/logos/inceptionlabs.svg" width="18" alt="Inception" /> Inception | Mercury 2 | 0.3401 | 1,850.19 | 0.2381 | ❌ |
| 347 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 35B A3B (non-reasoning) | 0.3353 | 2,090.55 | 0.2511 | ❌ |
| 348 | <img src="https://artificialanalysis.ai/img/logos/bytedance.svg" width="18" alt="ByteDance Seed" /> ByteDance Seed | Doubao Seed Code | 0.3341 | — | — | — |
| 349 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 31B (non-reasoning) | 0.3309 | 1,674.14 | 0.2277 | ❌ |
| 350 | <img src="https://artificialanalysis.ai/img/logos/china-mobile.png" width="18" alt="China Mobile" /> China Mobile | JT-35B-Flash | 0.3309 | — | — | — |
| 351 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (medium) | 0.3297 | 25,463.88 | 0.5429 | ❌ |
| 352 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.5 (non-reasoning) | 0.3294 | 8,004.40 | 0.4038 | ❌ |
| 353 | <img src="https://artificialanalysis.ai/img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE | 0.3281 | — | — | — |
| 354 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.2 8B | 0.3275 | 1,354.03 | 0.2061 | ❌ |
| 355 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (non-reasoning) | 0.3260 | 4,274.91 | 0.3306 | ❌ |
| 356 | <img src="https://artificialanalysis.ai/img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-2B | 0.3259 | — | — | — |
| 357 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5-Pro (non-reasoning) | 0.3237 | — | — | — |
| 358 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder Next | 0.3233 | 3,638.02 | 0.3122 | ❌ |
| 359 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B A22B 2507 | 0.3233 | — | — | — |
| 360 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 (non-reasoning) | 0.3223 | — | — | — |
| 361 | <img src="https://artificialanalysis.ai/img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.5 33B | 0.3214 | — | — | — |
| 362 | <img src="https://artificialanalysis.ai/img/logos/arcee.svg" width="18" alt="Arcee AI" /> Arcee AI | Trinity Large Thinking | 0.3208 | — | — | — |
| 363 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Sep) | 0.3200 | — | — | — |
| 364 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 | 0.3191 | 4,635.95 | 0.3399 | ❌ |
| 365 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-2.6-1T | 0.3186 | — | — | — |
| 366 | <img src="https://artificialanalysis.ai/img/logos/baidu.svg" width="18" alt="Baidu" /> Baidu | ERNIE 5.0 Thinking Preview | 0.3164 | — | — | — |
| 367 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 v2 (non-reasoning) | 0.3160 | 4,307.20 | 0.3315 | ❌ |
| 368 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (non-reasoning) | 0.3152 | 5,387.99 | 0.3573 | ❌ |
| 369 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 235B A22B | 0.3076 | — | — | — |
| 370 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (high) | 0.3041 | 10,487.35 | 0.4359 | ❌ |
| 371 | <img src="https://artificialanalysis.ai/img/logos/multiversecomputing.svg" width="18" alt="Multiverse Computing" /> Multiverse Computing | HyperNova 60B 2605 (high) | 0.3037 | — | — | — |
| 372 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash | 0.3033 | 7,293.37 | 0.3928 | ❌ |
| 373 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 (non-reasoning) | 0.3021 | 446.25 | 0.1093 | ❌ |
| 374 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (medium) | 0.3013 | 7,819.74 | 0.4010 | ❌ |
| 375 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-20b (high) | 0.3011 | 1,393.77 | 0.2090 | ❌ |
| 376 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 0528 | 0.3005 | 21,594.67 | 0.5229 | ❌ |
| 377 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5 (non-reasoning) | 0.2999 | 4,563.20 | 0.3381 | ❌ |
| 378 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max Thinking (Preview) | 0.2996 | — | — | — |
| 379 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max | 0.2968 | — | — | — |
| 380 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5 | 0.2962 | — | — | — |
| 381 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (non-reasoning) | 0.2959 | — | — | — |
| 382 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 4B | 0.2956 | — | — | — |
| 383 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 3 mini Reasoning (high) | 0.2954 | — | — | — |
| 384 | <img src="https://artificialanalysis.ai/img/logos/servicenow.svg" width="18" alt="ServiceNow" /> ServiceNow | Apriel-v1.6-15B-Thinker | 0.2954 | — | — | — |
| 385 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (non-reasoning) | 0.2946 | 10,346.98 | 0.4343 | ❌ |
| 386 | <img src="https://artificialanalysis.ai/img/logos/tencent-hy.svg" width="18" alt="Tencent" /> Tencent | Hy3-preview (non-reasoning) | 0.2941 | — | — | — |
| 387 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 26B A4B (non-reasoning) | 0.2918 | 1,048.05 | 0.1811 | ❌ |
| 388 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash (non-reasoning) | 0.2890 | — | — | — |
| 389 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o3-mini (high) | 0.2890 | 21,574.78 | 0.5227 | ❌ |
| 390 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (low) | 0.2873 | 12,230.97 | 0.4543 | ❌ |
| 391 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Sonnet (non-reasoning) | 0.2873 | 14,851.42 | 0.4776 | ❌ |
| 392 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 32B | 0.2868 | — | — | — |
| 393 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron Cascade 2 30B A3B | 0.2861 | — | — | — |
| 394 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (medium) | 0.2842 | — | — | — |
| 395 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o1 | 0.2839 | — | — | — |
| 396 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano | 0.2812 | 924.13 | 0.1694 | ❌ |
| 397 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.2 3B | 0.2793 | — | — | — |
| 398 | <img src="https://artificialanalysis.ai/img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 3 | 0.2789 | 1,299.14 | 0.2020 | ❌ |
| 399 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 E4B | 0.2773 | — | — | — |
| 400 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max (Preview) | 0.2766 | — | — | — |
| 401 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 0905 | 0.2759 | 1,588.66 | 0.2223 | ❌ |
| 402 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 9B (non-reasoning) | 0.2757 | 290.79 | 0.0810 | ❌ |
| 403 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Devstral 2 | 0.2728 | — | — | — |
| 404 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Sep) | 0.2724 | — | — | — |
| 405 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Exp (non-reasoning) | 0.2709 | — | — | — |
| 406 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Sep) (non-reasoning) | 0.2709 | — | — | — |
| 407 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 (Jan) | 0.2709 | 7,388.87 | 0.3943 | ❌ |
| 408 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (high) | 0.2694 | 4,125.35 | 0.3265 | ❌ |
| 409 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-1T | 0.2693 | — | — | — |
| 410 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7 (non-reasoning) | 0.2691 | 5,287.49 | 0.3551 | ❌ |
| 411 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Next 80B A3B | 0.2686 | — | — | — |
| 412 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 Terminus (non-reasoning) | 0.2686 | — | — | — |
| 413 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.7 Sonnet | 0.2684 | — | — | — |
| 414 | <img src="https://artificialanalysis.ai/img/logos/bytedance.svg" width="18" alt="ByteDance Seed" /> ByteDance Seed | Seed-OSS-36B-Instruct | 0.2679 | 1,644.57 | 0.2258 | ❌ |
| 415 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (low) | 0.2676 | — | — | — |
| 416 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 0.9B | 0.2671 | — | — | — |
| 417 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5-Air | 0.2659 | 1,895.39 | 0.2407 | ❌ |
| 418 | <img src="https://artificialanalysis.ai/img/logos/servicenow.svg" width="18" alt="ServiceNow" /> ServiceNow | Apriel-v1.5-15B-Thinker | 0.2659 | — | — | — |
| 419 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | DiffusionGemma 26B A4B | 0.2653 | — | — | — |
| 420 | <img src="https://artificialanalysis.ai/img/logos/deepcogito.png" width="18" alt="Deep Cogito" /> Deep Cogito | Cogito v2.1 | 0.2651 | — | — | — |
| 421 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (medium) | 0.2639 | 1,983.57 | 0.2455 | ❌ |
| 422 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano 4B | 0.2630 | — | — | — |
| 423 | <img src="https://artificialanalysis.ai/img/logos/prime-intellect.svg" width="18" alt="Prime Intellect" /> Prime Intellect | INTELLECT-3 | 0.2621 | — | — | — |
| 424 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7-Flash | 0.2615 | 835.63 | 0.1602 | ❌ |
| 425 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok Code Fast 1 | 0.2608 | — | — | — |
| 426 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Sonnet (non-reasoning) | 0.2593 | — | — | — |
| 427 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B A3B 2507 | 0.2585 | — | — | — |
| 428 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Large 3 | 0.2579 | 1,884.33 | 0.2401 | ❌ |
| 429 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 Omni Flash | 0.2578 | 955.72 | 0.1725 | ❌ |
| 430 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Magistral Medium 1.2 | 0.2564 | — | — | — |
| 431 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 (non-reasoning) | 0.2552 | 4,956.45 | 0.3476 | ❌ |
| 432 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (high) | 0.2539 | — | — | — |
| 433 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 | 0.2536 | 1,727.70 | 0.2310 | ❌ |
| 434 | <img src="https://artificialanalysis.ai/img/logos/celeris.svg" width="18" alt="Celeris" /> Celeris | Celeris-1 | 0.2532 | 1,287.02 | 0.2010 | ❌ |
| 435 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 2.6 Flash | 0.2516 | — | — | — |
| 436 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B 2507 | 0.2505 | 2,820.79 | 0.2837 | ❌ |
| 437 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 30B A3B | 0.2502 | — | — | — |
| 438 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Medium 3.1 | 0.2482 | — | — | — |
| 439 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (non-reasoning) | 0.2464 | 4,237.57 | 0.3296 | ❌ |
| 440 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Devstral Small 2 | 0.2459 | — | — | — |
| 441 | <img src="https://artificialanalysis.ai/img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.0 32B | 0.2455 | — | — | — |
| 442 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 (non-reasoning) | 0.2451 | 11,090.11 | 0.4426 | ❌ |
| 443 | <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax M1 80k | 0.2451 | 2,015.62 | 0.2472 | ❌ |
| 444 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (minimal) | 0.2447 | 11,327.27 | 0.4451 | ❌ |
| 445 | <img src="https://artificialanalysis.ai/img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Open 100B | 0.2435 | — | — | — |
| 446 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Next 80B A3B | 0.2417 | 1,610.72 | 0.2237 | ❌ |
| 447 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3 0324 | 0.2392 | — | — | — |
| 448 | <img src="https://artificialanalysis.ai/img/logos/tii.svg" width="18" alt="TII UAE" /> TII UAE | Falcon-H1R-7B | 0.2391 | — | — | — |
| 449 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 235B A22B | 0.2375 | 2,299.59 | 0.2614 | ❌ |
| 450 | <img src="https://artificialanalysis.ai/img/logos/motif.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif-2-12.7B | 0.2372 | — | — | — |
| 451 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.7 Sonnet (non-reasoning) | 0.2364 | — | — | — |
| 452 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-120b (low) | 0.2363 | 1,647.02 | 0.2260 | ❌ |
| 453 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Think V2 | 0.2355 | — | — | — |
| 454 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (non-reasoning) | 0.2354 | 1,919.68 | 0.2420 | ❌ |
| 455 | <img src="https://artificialanalysis.ai/img/logos/korea-telecom.png" width="18" alt="Korea Telecom" /> Korea Telecom | Mi:dm K 2.5 Pro | 0.2348 | — | — | — |
| 456 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 4B (non-reasoning) | 0.2339 | — | — | — |
| 457 | <img src="https://artificialanalysis.ai/img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step3 VL 10B | 0.2332 | — | — | — |
| 458 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (ChatGPT) | 0.2325 | — | — | — |
| 459 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-1T | 0.2313 | — | — | — |
| 460 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Haiku (non-reasoning) | 0.2312 | 4,534.55 | 0.3374 | ❌ |
| 461 | <img src="https://artificialanalysis.ai/img/logos/nousresearch.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 405B | 0.2312 | 4,406.43 | 0.3341 | ❌ |
| 462 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-flash-2.0 | 0.2308 | — | — | — |
| 463 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Sep) (non-reasoning) | 0.2307 | — | — | — |
| 464 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 | 0.2302 | 12,435.65 | 0.4563 | ❌ |
| 465 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (non-reasoning) | 0.2296 | 7,491.42 | 0.3959 | ❌ |
| 466 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 3 | 0.2296 | — | — | — |
| 467 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6 (non-reasoning) | 0.2295 | 6,672.01 | 0.3823 | ❌ |
| 468 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder 480B | 0.2295 | 3,640.03 | 0.3123 | ❌ |
| 469 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o3-mini | 0.2294 | 12,693.83 | 0.4588 | ❌ |
| 470 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B 2507 | 0.2291 | — | — | — |
| 471 | <img src="https://artificialanalysis.ai/img/logos/korea-telecom.png" width="18" alt="Korea Telecom" /> Korea Telecom | Mi:dm K 2.5 Pro Preview | 0.2291 | — | — | — |
| 472 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Super 49B v1.5 | 0.2291 | — | — | — |
| 473 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (low) | 0.2280 | 4,557.83 | 0.3380 | ❌ |
| 474 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (minimal) | 0.2276 | 1,627.65 | 0.2248 | ❌ |
| 475 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 12B (non-reasoning) | 0.2276 | — | — | — |
| 476 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Opus (non-reasoning) | 0.2276 | — | — | — |
| 477 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite | 0.2243 | 2,522.89 | 0.2714 | ❌ |
| 478 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 32B | 0.2241 | — | — | — |
| 479 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 32B | 0.2233 | 832.47 | 0.1599 | ❌ |
| 480 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Omni 30B A3B | 0.2233 | 2,900.78 | 0.2868 | ❌ |
| 481 | <img src="https://artificialanalysis.ai/img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE (non-reasoning) | 0.2229 | — | — | — |
| 482 | <img src="https://artificialanalysis.ai/img/logos/china-mobile.png" width="18" alt="China Mobile" /> China Mobile | JT-MINI | 0.2223 | — | — | — |
| 483 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B | 0.2222 | — | — | — |
| 484 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Small 3.1 | 0.2220 | — | — | — |
| 485 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 mini | 0.2180 | 2,210.75 | 0.2571 | ❌ |
| 486 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-20b (low) | 0.2175 | 236.22 | 0.0694 | ❌ |
| 487 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Ultra | 0.2173 | — | — | — |
| 488 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 4 Maverick | 0.2144 | 3,006.32 | 0.2908 | ❌ |
| 489 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6V | 0.2129 | 2,738.42 | 0.2805 | ❌ |
| 490 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Magistral Small 1.2 | 0.2117 | 1,204.14 | 0.1945 | ❌ |
| 491 | <img src="https://artificialanalysis.ai/img/logos/longcat.svg" width="18" alt="LongCat" /> LongCat | LongCat Flash Lite | 0.2103 | — | — | — |
| 492 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 30B A3B | 0.2099 | 467.33 | 0.1126 | ❌ |
| 493 | <img src="https://artificialanalysis.ai/img/logos/naver.webp" width="18" alt="Naver" /> Naver | HyperCLOVA X SEED Think (32B) | 0.2070 | — | — | — |
| 494 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Ministral 3 14B | 0.2060 | 480.86 | 0.1148 | ❌ |
| 495 | <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax M1 40k | 0.2054 | — | — | — |
| 496 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 14B | 0.2049 | 318.45 | 0.0866 | ❌ |
| 497 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3 (Dec) | 0.2047 | 798.69 | 0.1562 | ❌ |
| 498 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | QwQ-32B | 0.2041 | — | — | — |
| 499 | <img src="https://artificialanalysis.ai/img/logos/nousresearch.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 70B | 0.2032 | — | — | — |
| 500 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (medium) | 0.2013 | — | — | — |
| 501 | <img src="https://artificialanalysis.ai/img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam 105B (high) | 0.2001 | 728.98 | 0.1482 | ❌ |
| 502 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-flash-2.0 | 0.1994 | 400.45 | 0.1016 | ❌ |
| 503 | <img src="https://artificialanalysis.ai/img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 2 | 0.1987 | — | — | — |
| 504 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.1 Fast (non-reasoning) | 0.1982 | — | — | — |
| 505 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 32B Think | 0.1969 | — | — | — |
| 506 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3.1 32B Think | 0.1959 | — | — | — |
| 507 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B A3B 2507 (non-reasoning) | 0.1937 | 261.30 | 0.0749 | ❌ |
| 508 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Magistral Medium 1 | 0.1925 | — | — | — |
| 509 | <img src="https://artificialanalysis.ai/img/logos/baidu.svg" width="18" alt="Baidu" /> Baidu | ERNIE 4.5 300B A47B | 0.1886 | — | — | — |
| 510 | <img src="https://artificialanalysis.ai/img/logos/trillionlabs.svg" width="18" alt="Trillion Labs" /> Trillion Labs | Tri-21B-Think | 0.1885 | — | — | — |
| 511 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (non-reasoning) | 0.1884 | 1,174.61 | 0.1921 | ❌ |
| 512 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano Omni 30B A3B | 0.1881 | — | — | — |
| 513 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 12B v2 VL | 0.1871 | — | — | — |
| 514 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B | 0.1863 | 824.76 | 0.1591 | ❌ |
| 515 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Ministral 3 8B | 0.1829 | 348.68 | 0.0923 | ❌ |
| 516 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 Fast (non-reasoning) | 0.1795 | — | — | — |
| 517 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 8B | 0.1794 | — | — | — |
| 518 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5V | 0.1786 | 4,044.97 | 0.3243 | ❌ |
| 519 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder 30B A3B | 0.1776 | 1,334.98 | 0.2047 | ❌ |
| 520 | <img src="https://artificialanalysis.ai/img/logos/trillionlabs.svg" width="18" alt="Trillion Labs" /> Trillion Labs | Tri-21B-think Preview | 0.1756 | — | — | — |
| 521 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 8B | 0.1733 | — | — | — |
| 522 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Magistral Small 1 | 0.1731 | — | — | — |
| 523 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.0 Flash | 0.1728 | — | — | — |
| 524 | <img src="https://artificialanalysis.ai/img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.0 32B (non-reasoning) | 0.1721 | — | — | — |
| 525 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 9B V2 | 0.1712 | 140.30 | 0.0457 | ❌ |
| 526 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 4 Scout | 0.1680 | 514.40 | 0.1198 | ❌ |
| 527 | <img src="https://artificialanalysis.ai/img/logos/nousresearch.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 405B (non-reasoning) | 0.1677 | 2,688.75 | 0.2784 | ❌ |
| 528 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Small 3.2 | 0.1675 | 135.49 | 0.0444 | ❌ |
| 529 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Medium 3 | 0.1673 | 1,878.99 | 0.2398 | ❌ |
| 530 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 9B V2 (non-reasoning) | 0.1673 | 178.91 | 0.0558 | ❌ |
| 531 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.3 Nemotron Super 49B | 0.1670 | — | — | — |
| 532 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova Premier | 0.1666 | — | — | — |
| 533 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 7B Think | 0.1663 | — | — | — |
| 534 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-2.6B | 0.1654 | — | — | — |
| 535 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o (Aug) | 0.1646 | 19,412.08 | 0.5100 | ❌ |
| 536 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o (Nov) | 0.1646 | 23,026.87 | 0.5306 | ❌ |
| 537 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 E4B (non-reasoning) | 0.1634 | — | — | — |
| 538 | <img src="https://artificialanalysis.ai/img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | G9v3-3B | 0.1633 | — | — | — |
| 539 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.1 30B | 0.1628 | — | — | — |
| 540 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 0528 Qwen3 8B | 0.1615 | — | — | — |
| 541 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Omni 30B A3B | 0.1585 | 736.71 | 0.1492 | ❌ |
| 542 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (non-reasoning) | 0.1583 | 1,709.90 | 0.2299 | ❌ |
| 543 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (low) | 0.1583 | — | — | — |
| 544 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (non-reasoning) | 0.1583 | — | — | — |
| 545 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Small 4 (non-reasoning) | 0.1580 | 677.37 | 0.1420 | ❌ |
| 546 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Ministral 3 3B | 0.1573 | 249.72 | 0.0724 | ❌ |
| 547 | <img src="https://artificialanalysis.ai/img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam 30B (high) | 0.1564 | — | — | — |
| 548 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7-Flash (non-reasoning) | 0.1563 | 901.01 | 0.1671 | ❌ |
| 549 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-8B-A1B | 0.1558 | — | — | — |
| 550 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B (non-reasoning) | 0.1547 | — | — | — |
| 551 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-mini-2.0 | 0.1533 | — | — | — |
| 552 | <img src="https://artificialanalysis.ai/img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 2 (non-reasoning) | 0.1504 | — | — | — |
| 553 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.5 Haiku | 0.1495 | — | — | — |
| 554 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B 2507 (non-reasoning) | 0.1481 | — | — | — |
| 555 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.1 405B | 0.1479 | — | — | — |
| 556 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (non-reasoning) | 0.1472 | 383.85 | 0.0987 | ❌ |
| 557 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Devstral Medium | 0.1461 | — | — | — |
| 558 | <img src="https://artificialanalysis.ai/img/logos/nanbeige.png" width="18" alt="Nanbeige" /> Nanbeige | Nanbeige4.1-3B | 0.1460 | — | — | — |
| 559 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B | 0.1437 | — | — | — |
| 560 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 32B | 0.1430 | — | — | — |
| 561 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3.1 32B Instruct | 0.1412 | — | — | — |
| 562 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano (non-reasoning) | 0.1394 | 507.24 | 0.1188 | ❌ |
| 563 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen2.5 72B | 0.1380 | 598.33 | 0.1317 | ❌ |
| 564 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Devstral Small (May) | 0.1379 | — | — | — |
| 565 | <img src="https://artificialanalysis.ai/img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | Exaone 4.0 1.2B | 0.1377 | — | — | — |
| 566 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 4B | 0.1377 | — | — | — |
| 567 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.3 70B | 0.1366 | 6,925.09 | 0.3867 | ❌ |
| 568 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B (non-reasoning) | 0.1363 | 334.67 | 0.0897 | ❌ |
| 569 | <img src="https://artificialanalysis.ai/img/logos/cohere.svg" width="18" alt="Cohere" /> Cohere | Command A | 0.1361 | 8,648.96 | 0.4130 | ❌ |
| 570 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi Linear 48B A3B Instruct | 0.1348 | — | — | — |
| 571 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Super 49B v1.5 (non-reasoning) | 0.1337 | — | — | — |
| 572 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Large 2 (Nov) | 0.1334 | — | — | — |
| 573 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 nano | 0.1326 | 551.69 | 0.1253 | ❌ |
| 574 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6V (non-reasoning) | 0.1323 | 2,501.28 | 0.2705 | ❌ |
| 575 | <img src="https://artificialanalysis.ai/img/logos/reka.svg" width="18" alt="Reka AI" /> Reka AI | Reka Flash 3 | 0.1322 | 251.09 | 0.0727 | ❌ |
| 576 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 27B | 0.1316 | 0.00 | 0.0000 | ❌ |
| 577 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Devstral Small | 0.1303 | — | — | — |
| 578 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (minimal) | 0.1303 | 342.41 | 0.0911 | ❌ |
| 579 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 14B | 0.1278 | — | — | — |
| 580 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 32B (non-reasoning) | 0.1276 | 324.24 | 0.0877 | ❌ |
| 581 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 2B | 0.1272 | — | — | — |
| 582 | <img src="https://artificialanalysis.ai/img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-1B | 0.1272 | — | — | — |
| 583 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o mini | 0.1271 | 1,196.42 | 0.1939 | ❌ |
| 584 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.3 Nemotron Super 49B (non-reasoning) | 0.1270 | — | — | — |
| 585 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Pixtral Large | 0.1258 | — | — | — |
| 586 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5V (non-reasoning) | 0.1241 | 2,894.58 | 0.2866 | ❌ |
| 587 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.1 8B | 0.1224 | — | — | — |
| 588 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova Pro | 0.1216 | 4,684.46 | 0.3411 | ❌ |
| 589 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.1 Nemotron Nano 4B v1.1 | 0.1209 | — | — | — |
| 590 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 24B A2B | 0.1207 | — | — | — |
| 591 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 14B (non-reasoning) | 0.1204 | 342.17 | 0.0911 | ❌ |
| 592 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 E2B | 0.1196 | — | — | — |
| 593 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 12B | 0.1160 | 0.00 | 0.0000 | ❌ |
| 594 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 8B | 0.1147 | — | — | — |
| 595 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.1 3B | 0.1134 | — | — | — |
| 596 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.1 70B | 0.1123 | — | — | — |
| 597 | <img src="https://artificialanalysis.ai/img/logos/microsoft.svg" width="18" alt="Microsoft" /> Microsoft | Phi-4 | 0.1112 | 494.12 | 0.1168 | ❌ |
| 598 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.1 Nemotron 70B | 0.1101 | — | — | — |
| 599 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Llama 70B | 0.1095 | — | — | — |
| 600 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-1.2B-Thinking | 0.1080 | — | — | — |
| 601 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 12B v2 VL (non-reasoning) | 0.1080 | 528.82 | 0.1220 | ❌ |
| 602 | <img src="https://artificialanalysis.ai/img/logos/nousresearch.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 70B (non-reasoning) | 0.1078 | — | — | — |
| 603 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 7B | 0.1076 | — | — | — |
| 604 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Large 2 (Jul) | 0.1073 | — | — | — |
| 605 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H Small | 0.1065 | — | — | — |
| 606 | <img src="https://artificialanalysis.ai/img/logos/ai21.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba 1.7 Large | 0.1048 | — | — | — |
| 607 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 2B (non-reasoning) | 0.1045 | — | — | — |
| 608 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-1.2B-Instruct | 0.1038 | — | — | — |
| 609 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 E2B (non-reasoning) | 0.1031 | — | — | — |
| 610 | <img src="https://artificialanalysis.ai/img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-1B (non-reasoning) | 0.1024 | — | — | — |
| 611 | <img src="https://artificialanalysis.ai/img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | Exaone 4.0 1.2B (non-reasoning) | 0.1007 | — | — | — |
| 612 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 4B | 0.0996 | — | — | — |
| 613 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 1.7B | 0.0993 | — | — | — |
| 614 | <img src="https://artificialanalysis.ai/img/logos/ai21.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba Reasoning 3B | 0.0979 | — | — | — |
| 615 | <img src="https://artificialanalysis.ai/img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam M | 0.0977 | — | — | — |
| 616 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 8B (non-reasoning) | 0.0967 | — | — | — |
| 617 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Small 3 | 0.0953 | 73.58 | 0.0261 | ❌ |
| 618 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova Lite | 0.0929 | 337.35 | 0.0902 | ❌ |
| 619 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.1 8B | 0.0912 | 93.13 | 0.0321 | ❌ |
| 620 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3 Haiku | 0.0892 | — | — | — |
| 621 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova Micro | 0.0879 | 217.50 | 0.0651 | ❌ |
| 622 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3 70B | 0.0860 | 1,890.76 | 0.2404 | ❌ |
| 623 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 8B A1B | 0.0843 | — | — | — |
| 624 | <img src="https://artificialanalysis.ai/img/logos/ai21.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba 1.7 Mini | 0.0813 | — | — | — |
| 625 | <img src="https://artificialanalysis.ai/img/logos/microsoft.svg" width="18" alt="Microsoft" /> Microsoft | Phi-4 Mini | 0.0792 | 208.44 | 0.0630 | ❌ |
| 626 | <img src="https://artificialanalysis.ai/img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM-V 4.6 1.3B | 0.0788 | — | — | — |
| 627 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 Micro | 0.0770 | — | — | — |
| 628 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3n E4B | 0.0736 | — | — | — |
| 629 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 4B | 0.0728 | 0.00 | 0.0000 | ❌ |
| 630 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 0.8B (non-reasoning) | 0.0683 | — | — | — |
| 631 | <img src="https://artificialanalysis.ai/img/logos/swiss-ai-initiative.png" width="18" alt="Swiss AI Initiative" /> Swiss AI Initiative | Apertus 70B Instruct | 0.0678 | — | — | — |
| 632 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 3.3 8B (non-reasoning) | 0.0677 | — | — | — |
| 633 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H 1B | 0.0675 | — | — | — |
| 634 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Molmo2-8B | 0.0620 | — | — | — |
| 635 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 0.6B | 0.0598 | — | — | — |
| 636 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.2 11B (Vision) | 0.0587 | — | — | — |
| 637 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 0.8B | 0.0585 | — | — | — |
| 638 | <img src="https://artificialanalysis.ai/img/logos/swiss-ai-initiative.png" width="18" alt="Swiss AI Initiative" /> Swiss AI Initiative | Apertus 8B Instruct | 0.0568 | — | — | — |
| 639 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 1.7B (non-reasoning) | 0.0557 | — | — | — |
| 640 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.2 3B | 0.0546 | — | — | — |
| 641 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 1B | 0.0534 | — | — | — |
| 642 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 2.6B | 0.0527 | — | — | — |
| 643 | <img src="https://artificialanalysis.ai/img/logos/cohere.svg" width="18" alt="Cohere" /> Cohere | Tiny Aya Global | 0.0516 | 0.00 | 0.0000 | ❌ |
| 644 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | OLMo 2 32B | 0.0507 | — | — | — |
| 645 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-VL-1.6B | 0.0503 | — | — | — |
| 646 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 0.6B (non-reasoning) | 0.0484 | — | — | — |
| 647 | <img src="https://artificialanalysis.ai/img/logos/microsoft.svg" width="18" alt="Microsoft" /> Microsoft | Phi-3 Mini | 0.0476 | — | — | — |
| 648 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3n E2B | 0.0475 | — | — | — |
| 649 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3 8B | 0.0475 | 168.07 | 0.0530 | ❌ |
| 650 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.2 1B | 0.0450 | — | — | — |
| 651 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 1.2B | 0.0428 | — | — | — |
| 652 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 1B | 0.0388 | — | — | — |
| 653 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H 350M | 0.0384 | — | — | — |
| 654 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 350M | 0.0358 | — | — | — |
| 655 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | OLMo 2 7B | 0.0328 | — | — | — |
| 656 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral 7B | 0.0276 | 210.54 | 0.0635 | ❌ |
| 657 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 270M | 0.0274 | — | — | — |
| 658 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Llama 8B | 0.0165 | — | — | — |
| 659 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 1.5B | 0.0056 | — | — | — |
| 660 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Molmo 7B-D | 0.0000 | — | — | — |

## 品牌帕累托前沿连线（仅体现在图中）

以下 12 个品牌在图中拥有单独的帕累托连线（较窄宽度，品牌主题色，图层高于总体灰色连线）。表中数量为**入图顶点数**——品牌前沿上低于总体前沿第一级的顶点同样不入图（本表与图例一致）：

| 品牌 | 主题色 | 品牌前沿模型数（入图） |
|------|--------|--------------|
| <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | `#cc785c` | 11 |
| <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | `#1f1f1f` | 15 |
| <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | `#34A853` | 9 |
| <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | `#0089f4` | 4 |
| <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | `#ff6900` | 2 |
| <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | `#1521a9` | 1 |
| <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | `#047AFE` | 3 |
| <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | `#ff7018` | 3 |
| <img src="https://artificialanalysis.ai/img/logos/tencent-hy.svg" width="18" alt="Tencent" /> Tencent | `#5CB9FF` | 1 |
| <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | `#736cd3` | 4 |
| <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | `#2243e6` | 3 |
| <img src="https://artificialanalysis.ai/img/logos/thinking-machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | `#676767` | 2 |

## 多轮单调基准映射与留一交叉验证（Multi-Round Monotone Benchmark Mapping & LOVO Cross-Validation）

为解决不同基准测试覆盖群体差异及个别基准噪声导致的排序倒挂，系统在 `src/mapping.py` 中实现了**零标签泄漏（Zero Label Leakage）的多轮单调基准映射引擎 (`MonotoneBenchmarkMapper`)**：
- **纯特征函数推理**：`score_model(parsed_metrics)` 仅读取各模型在 38 项基准上的原始分数，经自适应分位分段线性单调曲线 $g_b: [0,1] \to \mathbb{R}$（每段斜率严格约束 $s_{b,r} \ge \varepsilon_{\min} > 0$）、有界正则化权重 $w_b$ 与 Pseudo-Huber IRLS 稳健 M-估计聚合输出综合能力；**绝不读取模型名称、厂商、等级、版本或思考标签，也绝不执行 Dykstra 标签硬夹逼**。

- **严格单调性校验**：`all_strictly_monotone = True`，全部 38 条曲线最小观测斜率 = `0.0500`（要求 $\ge 0.05$）。

### 多轮优化收敛进程（Multi-Round Optimization Progression）

| 轮次 | 优化方法 | 满足 / 总约束 | 序一致性 (Concordance) | 违背数 | Rule 1 (Tier) | Rule 2 (Version) | Rule 3 (Thinking) | Rule 4 (Date) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `round_0a` | Raw Min-Max Mean | 2,686 / 3,139 | **85.57%** | 453 | 89.95% | 84.58% | 86.76% | 63.27% |
| `round_0b` | LOO Linear Calibration | 2,898 / 3,139 | **92.32%** | 241 | 93.41% | 92.67% | 92.65% | 61.22% |
| `round_1` | Stage-1 Unsupervised Monotone Calibration | 3,075 / 3,139 | **97.96%** | 64 | 95.06% | 98.80% | 99.02% | 89.80% |
| `round_2` | Regularized Benchmark Weight Optimization | 3,081 / 3,139 | **98.15%** | 58 | 95.39% | 98.89% | 99.26% | 91.84% |
| `round_3` | Joint Monotone Curve + Weight Optimization | 3,085 / 3,139 | **98.28%** | 54 | 96.05% | 98.80% | 99.51% | 93.88% |
| `round_4a` | Pseudo-Huber IRLS Robust Aggregation | 3,077 / 3,139 | **98.02%** | 62 | 95.06% | 98.70% | 99.75% | 91.84% |
| `round_4b` | Huber/IRLS + Margin-Annealed Refinement | 3,087 / 3,139 | **98.34%** | 52 | 96.54% | 98.75% | 99.75% | 91.84% |

### 留一厂商交叉验证（Leave-One-Vendor-Out Generalization）

Stage 1（单调 IRT 初始化）全程无监督（0 条约束标签）；针对每个主流厂商，Stage 2 严格剔除该厂商全部模型的约束后进行联合训练，再在被完全留出的该厂商约束集上评估泛化序一致性：

| 留出厂商 (Held-out Vendor) | 模型数 | 留出约束数 | R0 Raw | R0 LOO | R1 无监督 | R4 Held-out | 相对 R0 LOO | 相对 R1 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| OpenAI | 113 | 948 | 89.03% | 95.04% | 99.05% | **99.26%** | +4.22% | +0.21% |
| Google | 74 | 482 | 86.72% | 92.95% | 98.96% | **98.76%** | +5.81% | -0.21% |
| Anthropic | 65 | 410 | 90.73% | 96.59% | 99.27% | **99.02%** | +2.44% | -0.24% |
| Alibaba | 87 | 449 | 88.86% | 92.87% | 96.88% | **97.77%** | +4.90% | +0.89% |
| DeepSeek | 36 | 143 | 72.03% | 79.72% | 97.20% | **97.20%** | +17.48% | +0.00% |
| Meta | 27 | 46 | 84.78% | 91.30% | 95.65% | **95.65%** | +4.35% | +0.00% |
| SpaceXAI | 27 | 146 | 72.60% | 87.67% | 96.58% | **96.58%** | +8.90% | +0.00% |
| Z AI | 23 | 63 | 76.19% | 92.06% | 98.41% | **98.41%** | +6.35% | +0.00% |
| **TOTAL LOVO** | — | **2,687** | **86.68%** | **93.19%** | **98.40%** | **98.55%** | **+5.36%** | **+0.15%** |

### 学习到的基准权重分布（高信噪比增权 vs 噪声降权）

优化器在有界单纯形约束下自动识别高信噪比基准并抑制反单调/高噪声基准（如 `healthbench`、`omniscienceNonHallucination`、`enterpriseOps` 等），同时限制单项权重上限以保持评估多样性：

| 高权重基准 (Top Informative) | 权重 $w_b$ (占比) | 低权重/降权基准 (Downweighted) | 权重 $w_b$ (占比) |
| :--- | :---: | :--- | :---: |
| AA Intelligence Index (`intelligenceIndex`) | `2.1151` (5.57%) | AA-Omniscience Non-Hallucination (`omniscienceNonHallucination`) | `0.2817` (0.74%) |
| Humanity's Last Exam (`hle`) | `1.7342` (4.56%) | EnterpriseOps-Gym-AA (`enterpriseOps`) | `0.3179` (0.84%) |
| Terminal-Bench 2.1 (`terminalbenchV21`) | `1.6548` (4.35%) | HealthBench (`healthbench`) | `0.3313` (0.87%) |
| GDPval-AA Normalized (`gdpvalNormalized`) | `1.5635` (4.11%) | τ²-Bench Telecom (`tau2`) | `0.4109` (1.08%) |
| CritPt v2 Hard (`critptV2Hard`) | `1.4567` (3.83%) | Harvey LAB-AA (`harveyLab`) | `0.5401` (1.42%) |
| Terminal-Bench Hard (`terminalbenchHard`) | `1.4035` (3.69%) | MLCR Medical Long Context (`mlcr`) | `0.6478` (1.70%) |
| FrontierCode 2.0 (`frontiercode20`) | `1.3518` (3.56%) | AIME 2025 (`aime2025`) | `0.6630` (1.74%) |
| GPQA Diamond (`gpqa`) | `1.2585` (3.31%) | HealthBench Professional (`healthbenchProfessional`) | `0.6753` (1.78%) |


## 基准测试动态标定与 38 项权重汇总

> Leave-One-Out 线性标定作为参考字段（`composite_ability_calibrated`）同步保留，已完成 **24** 轮并行迭代收敛（容差阈值 $\Delta < 1e-05$）；主综合能力 `composite_ability` 由 `src/mapping.py` 的单调样条与学习权重计算得到。

| 基准测试项 | 英文标识 | 参测模型数 | 学习权重 $w_b$ | 权重占比 | LOO 下界 | LOO 上界 | LOO 跨度 |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| AA Intelligence Index | `intelligenceIndex` | 155 | `2.1151` | 5.57% | `0.0868` | `1.0000` | `0.9132` |
| GPQA Diamond | `gpqa` | 543 | `1.2585` | 3.31% | `0.0000` | `0.9106` | `0.9106` |
| Humanity's Last Exam | `hle` | 619 | `1.7342` | 4.56% | `0.0000` | `1.0000` | `1.0000` |
| HLE Diamond | `hleDiamond` | 198 | `1.1738` | 3.09% | `0.0855` | `1.0000` | `0.9145` |
| CritPt Physics | `critpt` | 599 | `0.8337` | 2.19% | `0.0000` | `1.0000` | `1.0000` |
| CritPt v2 Hard | `critptV2Hard` | 161 | `1.4567` | 3.83% | `0.0876` | `1.0000` | `0.9124` |
| AIME 2025 | `aime2025` | 268 | `0.6630` | 1.74% | `0.0000` | `0.7182` | `0.7182` |
| SciCode Coding | `scicode` | 253 | `1.1062` | 2.91% | `0.0876` | `1.0000` | `0.9124` |
| LiveCodeBench | `livecodebench` | 278 | `1.1373` | 2.99% | `0.0000` | `0.7181` | `0.7181` |
| FrontierCode 1.1 | `frontiercode` | 83 | `0.8900` | 2.34% | `0.1349` | `1.0000` | `0.8651` |
| FrontierCode 2.0 | `frontiercode20` | 157 | `1.3518` | 3.56% | `0.0876` | `1.0000` | `0.9124` |
| Terminal-Bench Hard | `terminalbenchHard` | 432 | `1.4035` | 3.69% | `0.0000` | `0.8436` | `0.8436` |
| Terminal-Bench 2.1 | `terminalbenchV21` | 243 | `1.6548` | 4.35% | `0.0621` | `0.9103` | `0.8482` |
| Terminal-Bench 4.0 | `terminalbenchV40` | 284 | `0.8891` | 2.34% | `0.0872` | `1.0000` | `0.9128` |
| Terminal-Bench Science | `terminalbenchScience` | 171 | `0.7381` | 1.94% | `0.0874` | `1.0000` | `0.9126` |
| τ²-Bench Telecom | `tau2` | 439 | `0.4109` | 1.08% | `0.0000` | `0.8512` | `0.8512` |
| τ³-Bench Banking | `tauBanking` | 210 | `0.9675` | 2.55% | `0.0645` | `0.9152` | `0.8506` |
| AutomationBench-AA | `automationbench` | 286 | `1.1987` | 3.15% | `0.0875` | `1.0000` | `0.9125` |
| AA-Briefcase v1.1 | `briefcase` | 293 | `1.1985` | 3.15% | `0.0875` | `1.0000` | `0.9125` |
| GDPval-AA Normalized | `gdpvalNormalized` | 319 | `1.5635` | 4.11% | `0.0626` | `1.0000` | `0.9374` |
| GDP.pdf | `gdpPdf` | 286 | `1.2135` | 3.19% | `0.0854` | `1.0000` | `0.9146` |
| AA-LCR Long Context | `lcr` | 596 | `0.9180` | 2.42% | `0.0000` | `1.0000` | `1.0000` |
| MLCR Medical Long Context | `mlcr` | 203 | `0.6478` | 1.70% | `0.1255` | `1.0000` | `0.8745` |
| MMMU Pro | `mmmuPro` | 306 | `1.1467` | 3.02% | `0.0127` | `0.9416` | `0.9289` |
| Code2Video-AA | `code2video` | 29 | `0.9688` | 2.55% | `0.4242` | `0.9121` | `0.4880` |
| AA-3D | `aa3d` | 30 | `1.1963` | 3.15% | `0.4249` | `1.0000` | `0.5751` |
| AA Omniscience Index | `omniscience` | 172 | `1.0087` | 2.65% | `0.0821` | `1.0000` | `0.9179` |
| AA-Omniscience Accuracy | `omniscienceAccuracy` | 172 | `0.7981` | 2.10% | `0.0873` | `1.0000` | `0.9127` |
| AA-Omniscience Non-Hallucination | `omniscienceNonHallucination` | 172 | `0.2817` | 0.74% | `0.0729` | `1.0000` | `0.9271` |
| IFBench Instruction Following | `ifbench` | 449 | `0.8505` | 2.24% | `0.0000` | `0.8566` | `0.8566` |
| AA Analyst Agent | `analystAgent` | 65 | `0.9209` | 2.42% | `0.2533` | `0.9416` | `0.6884` |
| APEX-Agents-AA | `apexAgents` | 34 | `0.9359` | 2.46% | `0.3008` | `0.8077` | `0.5069` |
| EnterpriseOps-Gym-AA | `enterpriseOps` | 63 | `0.3179` | 0.84% | `0.2682` | `0.9666` | `0.6984` |
| ITBench-SRE | `itbenchSre` | 45 | `0.6908` | 1.82% | `0.1560` | `0.9219` | `0.7659` |
| Harvey LAB-AA | `harveyLab` | 47 | `0.5401` | 1.42% | `0.4371` | `1.0000` | `0.5629` |
| HealthBench | `healthbench` | 29 | `0.3313` | 0.87% | `0.6407` | `1.0000` | `0.3593` |
| HealthBench Professional | `healthbenchProfessional` | 19 | `0.6753` | 1.78% | `0.6395` | `1.0000` | `0.3605` |
| VIALS-AA / MKA | `vials` | 28 | `0.8128` | 2.14% | `0.4905` | `1.0000` | `0.5095` |


## 评分方法

1. **38项全域评估指标**各自线性归一化到 [0,1]
   （AA Intelligence Index、GPQA Diamond、Humanity's Last Exam、HLE Diamond、CritPt Physics、CritPt v2 Hard、AIME 2025、SciCode Coding、LiveCodeBench、FrontierCode 1.1、FrontierCode 2.0、Terminal-Bench Hard、Terminal-Bench 2.1、Terminal-Bench 4.0、Terminal-Bench Science、τ²-Bench Telecom、τ³-Bench Banking、AutomationBench-AA、AA-Briefcase v1.1、GDPval-AA Normalized、GDP.pdf、AA-LCR Long Context、MLCR Medical Long Context、MMMU Pro、Code2Video-AA、AA-3D、AA Omniscience Index、AA-Omniscience Accuracy、AA-Omniscience Non-Hallucination、IFBench Instruction Following、AA Analyst Agent、APEX-Agents-AA、EnterpriseOps-Gym-AA、ITBench-SRE、Harvey LAB-AA、HealthBench、HealthBench Professional、VIALS-AA / MKA）
   > 全域基准升级：收录全部 38 项基准测试，涵盖通用推理 (AA Intelligence Index, HLE, HLE Diamond, GPQA Diamond)、数理逻辑 (CritPt, CritPt v2 Hard, AIME 2025)、代码编程 (LiveCodeBench, SciCode, FrontierCode 1.1/2.0)、Agent 智能体 (Terminal-Bench 系列, τ-Bench 系列, AutomationBench, Briefcase, ITBench-SRE, Harvey LAB, HealthBench)、多模态 (MMMU Pro, Code2Video, AA-3D, VIALS)、长上下文 (AA-LCR, MLCR, GDP.pdf) 及事实性 (Omniscience 系列, IFBench) 等核心维度。
2. **综合能力值（零标签泄漏单调映射）**：通过 `src/mapping.py` (`MonotoneBenchmarkMapper`) 对每项已测基准分数经严格单调分段曲线 $g_b(x)$ 校准后，按学习到的稳健权重 $w_b$ 执行 Pseudo-Huber IRLS M-估计聚合；原始等权平均 (`composite_ability_raw_uncalibrated`) 与留一线性标定 (`composite_ability_calibrated`) 同步保留在 `output/analysis_results.json` 中供对照。
3. **综合能力再归一化**：线性映射到 [0,1]，性能最好的模型 = 1，最差的模型 = 0
4. **Pareto前沿** = 不被任何其他模型支配的模型（综合能力 ≥ 且成本 ≤，且至少一项严格更优；成本为 0 的免费模型同样参与——横轴左端恒为 0，免费模型是合法前沿候选）
5. **模型范围** = Status: All（含已弃用模型；缺少足够评估数据者不参与排名）
6. **图表纵轴基线（V17）**：图表的 y = 0 取总体帕累托前沿的第一级（最低能力；本例 y0 = 0.5684，即前沿左端点 K2 Horizon 375B A23B）；综合能力低于该级的模型不出现在图表中（表格不受影响）。图中纵坐标 chart_y = (能力 - y0)/(1 - y0)，因此前沿左端点恰好落在 (0, 0)、最优模型恰好为 y = 1。该过滤在横轴映射构建之前完成


## 模型系列层级与单调性评分引擎（Model Hierarchy & Monotonic Scoring Engine）

为解决多基准评估中由于各模型参测项不齐、评测噪声以及偶然波动导致的反直觉能力倒挂（例如同一系列同版本高阶模型得分低于低阶模型、同一系列同等级新版本低于旧版本、同一模型高思考程度低于低思考程度、同代更新快照后出版本低于先出版本），系统在 `src/hierarchy.py` 中实现了**分厂商系列层级网格（Vendor Series Hierarchy Grids）**并与 `src/mapping.py` 的纯特征单调映射引擎协同工作：

### 1. 厂商与系列隔离（Series Isolation）
系统维护了覆盖全部主流与新兴厂商的 **99 个系列层级网格**（保存在 `output/model_hierarchy/` 目录下的 CSV 文件中），每个系列维护二维网格：
- **行（Tiers）**：性能层级（如 Tier 1 Flagship / Large、Tier 2 Medium / MoE、Tier 3 Small / Fast、Tier 4 Compact / Nano）
- **列（Versions）**：架构代际与版本演进（从旧到新按时间列排布）
- **严格系列隔离**：不同系列（例如 OpenAI 的 `GPT` 系列与 `o` 推理系列、Google 的 `Gemini` 与 `Gemma` 开源系列、Meta 的 `Llama` 与 `Muse` 系列）物理隔离，绝不产生跨系列强行绑定的单调性约束。

### 2. 四大严格单调序规则（Strict Monotonic Ordering Rules）
在系列网格与模型元数据基础上，自动生成 **3,139 条**有向无环约束（DAG，$S(u) \ge S(v)$：Rule 1 = 607，Rule 2 = 2,075，Rule 3 = 408，Rule 4 = 49）：
- **Rule 1（同系列同版本，高等级 $\ge$ 低等级）**：同一系列、同一版本列内，高行 Tier 模型能力必须大于等于低行 Tier 模型的所有快照与变体（支持思考程度对齐匹配）。
- **Rule 2（同系列同等级，新版本 $\ge$ 旧版本）**：同一系列、同一等级行内，新版本列模型能力必须大于等于旧版本列模型。
- **Rule 3（同模型基座，高思考程度 $\ge$ 低思考程度）**：同一基座模型，高思考算力档位能力必须大于等于低思考算力档位（$\text{max} > \text{xhigh} > \text{high} > \text{medium} > \text{low} > \text{minimal} > \text{non-reasoning}$）。
- **Rule 4（同模型主干，新日期快照 $\ge$ 旧日期快照）**：同一模型主干内，后发布的日期快照能力大于等于先发布的快照（如 GPT-4o Nov $\ge$ Aug $\ge$ May，Claude 3.5 Sonnet Oct $\ge$ June，DeepSeek V4 Pro 0813 $\ge$ 0424）。

### 3. 零标签泄漏纯特征映射评估（Zero-Clamping Pure Benchmark Mapping）
- **纯函数无硬夹逼原则**：主评分完全由 `MonotoneBenchmarkMapper.score_model(parsed_metrics)` 根据模型基准得分直接计算，**不在推理时读取模型身份，也不使用 Dykstra 等保投影对模型分数进行标签硬夹逼（Zero Label Clamping）**；
- **实测序一致性**：在 725 个参测模型、3,139 条清洁约束条件下，纯特征映射直接达成 **98.34% 序一致性（满足 3,087/3,139，52 项真实数据级倒挂）**；可选 Dykstra 等保投影仅作为离线理论诊断上界保留于诊断报告。详见 [层级诊断报告](output/model_hierarchy/hierarchy_score_report.md) 与 [层级分析结果](output/hierarchy_analysis_results.json)。

### 4. 人工校验与 CSV 双向工作流（Calibration & Diff Workflow）
全部 99 个系列层级网格均以易于阅读与编辑的标准 2D CSV 存储于 `output/model_hierarchy/`。
- **导出与查看**：运行 `python src/hierarchy.py` 会导出全部单独 CSV 及汇总表 `all_vendors_hierarchy.csv`；
- **自定义层级微调**：用户可直接用 Excel 或文本编辑器修改任意系列 CSV（例如调整某些新模型的归属代际或层级）；
- **差异审查与校验**：运行 `python src/hierarchy.py --diff <SeriesName>` 或 `--diff all`，系统会自动将本地修改与默认预置层级进行三向比对，报告所有变更并校验单调性。


## 横轴映射（对数映射，真零点，V21）与分布分析

横轴（单请求成本）为 **Y = A·ln(B·c+C)+D 对数映射**（B = 1；A、D 由端点解出；C = 311.64，r = B/C = 0.00320882 经网格搜索确定）：

```
x = 0                            当 c = 0（免费模型，真零点）
x = A·ln(c+C)+D                  当 c > 0（B = 1 并入；A、D 由端点解出）
```

其中 C = 311.64（r = B/C = 0.00320882），拟合集为 11 品牌前沿入图正成本模型（综合能力 ≥ 前沿第一级）的成本分布，目标为组内名次分位数（最小二乘误差 mse = 0.011334，最大偏离 0.2272）。该映射在 **y 基线过滤之后**构建（V17：先以帕累托前沿第一级为 y = 0、剔除低性能模型，再对入图模型建映射）。

**该映射保证：**

- **函数端点严格钉死**：c = 0 → x = 0；最大成本 → x = 1——函数经过 (0,0) 与 (1,1)；
- 各数量级区间的入图模型数：1–10: 0，10–100: 0，100–1k: 3，1k–10k: 37，10k–100k: 101，100k–1M: 15，1M–1.061M: 0
- **同倍率区间宽度相近**（对数轴性质）：1k→10k 与 100k→1M 同为 10 倍率，宽度相近（前者 37 个模型、后者 15 个）；与 V17 分位数映射不同，本图不追求均匀密度——密度不等如实显示；
- **左端恒为 0**（c = 0；1 个免费模型位于最左缘）
- 前沿最低正成本 516.29 → x = 0.1201（真实对数位置，不再钉 0；x = 0 恒为 c = 0 免费模型）；前沿最大成本 1,061,351 → x = 1.0000（= 1；高于前沿最大成本的模型不入图，仅表格保留）
- 中位数位置 0.541（≈ 0.5 居中）；左右两半模型数：左 67 / 右 91
- 横轴十分位模型数：1，9，9，13，35，39，32，10，7，3（对数映射下各十分位模型数自然不等）
- **10^x 数量级指示**（位置 = x(10^x)）：10^0 → 0.000，10^1 → 0.004，10^2 → 0.034，10^3 → 0.177，10^4 → 0.430，10^5 → 0.710，10^6 → 0.993

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
| CacheHitRate | [AA Coding Agents](https://artificialanalysis.ai/agents/coding-agents) | 全部模型-Agent搭配的 `cacheHitRate` 求平均（66 个有效值，均值 = 0.9334），对所有模型统一使用 |
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

### 数据来源与自动化流程

**主数据源**: [Artificial Analysis Leaderboard](https://artificialanalysis.ai/leaderboards/models)（Status: All）  
**Cache Hit Rate 数据源**: [AA Coding Agents](https://artificialanalysis.ai/agents/coding-agents)  
**性能方法论**: [AA Performance Benchmarking](https://artificialanalysis.ai/methodology/performance-benchmarking)  
**模型总数（Status: All）**: 660 个参与排名（共抓取 766 个模型，另有模型因评估数据不足未列入；总体帕累托前沿 18 个；图表入图 158 个——综合能力 ≥ 前沿第一级）  

**技术架构与更新流程：**
1. **高速数据抓取 (`src/scrape.py`)**：解析 Artificial Analysis 的 Next.js RSC 动态清单（Manifest），通过 AES-GCM 快速解密全量模型数据集，解压缩 GZip 流并解析嵌套的 38 项基准维度分数与发布时间；
2. **缓存命中率抓取 (`src/cache_hit_rate.py`)**：通过 Playwright 抓取 Coding Agents 页面的全局均值作为成本公式参数；
3. **单调基准映射引擎 (`src/mapping.py`)**：在无模型身份泄漏、无 Dykstra 标签夹逼的前提下，通过 38 项严格单调分段样条 $g_b$、有界权重 $w_b$ 与 Pseudo-Huber IRLS 聚合拟合能力映射并执行 LOVO 交叉验证；
4. **模型层级约束与诊断 (`src/hierarchy.py`)**：基于 99 个系列层级网格（Tiers x Versions）生成 3,139 条 DAG 单调约束，记录纯映射序一致性（98.34%）并导出诊断报告；
5. **帕累托与图表分析 (`src/analyze.py`)**：基于 `src/mapping.py` 映射的综合能力执行成本计算、真零点对数坐标映射与多品牌前沿图表绘制；
6. **自动化 GitHub Actions (`.github/workflows/update-leaderboard.yml`)**：每日定时及手动触发运行抓取、层级与映射计算、单元测试验证与看板自动更新。


## 图表说明（黑底）

（V17 起本说明置于文末，图表之后直接跟随模型表格。）

图表说明：**灰色实线** = 总体帕累托前沿；**彩色细线** = 选定品牌的单独帕累托前沿（共 12 个品牌，（品牌主题色，图层高于总体连线；暗色品牌元素带窄白边；顶点按（横轴位置、能力升序）连接，等成本点自下而上）；品牌前沿模型圆点同样使用品牌颜色。模型名称/思考程度标注优先骑在连线之上（点的左/右两侧皆可，同一条线段可容纳两个标签——各贴各的点；文字与连线平行、中轴线重合，连线仅在文字两侧绘制）；骑线位被其他标签占据时自动「让位」——占用者挪到自己的另一个骑线位，双方都保持骑线；实在骑不上线时按四级优先依次退让（V16）：离点最近位置的上方/下方平行偏移 → 点的两条连线延长线上就近 → 两连线夹角扇区内就近。标签规则（V13/V15）：品牌前沿模型共享的前导块按「最长有效切点」剔除 —— 切点止于分界符，或止于字母且其后紧跟数字（如 Claude Opus 5 → Opus 5、GPT-5.6 Sol → 5.6 Sol、Kimi K2.6 → 2.6、Qwen3.8 Max → 3.8 Max、MiMo-V2.5 → 2.5、MiniMax-M2.1 → 2.1）；(non-reasoning) 简写为 (non)；同一模型在品牌连线上相邻出现 2 次以上时仅性能最低者保留全名、相邻较高者只标思考程度，不相邻的重复出现保留全名（每次重新计算）；标签位置与序列同向（V15）——品牌前沿上越靠右上的模型，其标签重心必须同时更靠右且更靠上（两分量都 >= 0，至少是 (0,0)，仅其一非负不算合格；初始放置违反时自动就近重摆，单标签无解（被前后邻居夹死）时按窗口级联重排整体挪动，均不产生新的重叠）。纵轴 y = 0 = 总体帕累托前沿第一级（y0 = 0.5684，前沿左端点 K2 Horizon 375B A23B 恰为 (0,0)），能力低于该级的 490 个模型、缺少成本数据的 12 个模型与成本高于品牌前沿最大值的模型不出现在图中；横轴为对数映射（见上文「横轴映射」节），10^x 数量级指示位于 x(10^x)，同一倍率区间的宽度相近（对数轴性质；本图不追求均匀密度）。
