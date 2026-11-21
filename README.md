# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

## 全部模型（综合能力从高到低，最优 = 1，最差 = 0）

共收录 **Status: All**（含已弃用）的全部模型；按重新归一化后的综合能力排序。「帕累托」列：✅ = 总体帕累托前沿模型，❌ = 被支配，— = 无成本数据无法判定。图表纵轴以总体帕累托前沿第一级（y0 = 0.5660，即前沿左端点 K2 Horizon 375B A23B）为 0：综合能力 ≥ 该级且有成本数据的 158 个模型入图，490 个能力低于第一级、11 个缺少成本数据的模型不出现在图中，成本高于品牌前沿最大值的模型同样不入图（本表不受影响，仍完整列出全部模型）。

| # | 品牌 | 模型 | 综合能力 | 单请求成本 | 横轴位置 | 帕累托 |
|---|------|------|---------|-----------|-----------|------|
| 1 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.2 (max) | 1.0000 | 1,018,638.01 | 1.0000 | ✅ |
| 2 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.2 Astra (max) | 0.9823 | 410,571.78 | 0.8879 | ✅ |
| 3 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.2 (xhigh) | 0.9684 | 280,645.13 | 0.8410 | ✅ |
| 4 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.2 Astra (xhigh) | 0.9615 | 159,382.15 | 0.7712 | ✅ |
| 5 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Neon (xhigh) | 0.9612 | 100,350.39 | 0.7142 | ✅ |
| 6 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Neon (high) | 0.9557 | 74,900.93 | 0.6783 | ✅ |
| 7 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.2 (high) | 0.9514 | 131,430.43 | 0.7475 | ❌ |
| 8 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.2 Astra (high) | 0.9514 | 80,966.34 | 0.6878 | ❌ |
| 9 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.2 Sol (max) | 0.9454 | 58,907.90 | 0.6487 | ✅ |
| 10 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Carbon (high) | 0.9323 | 98,114.16 | 0.7115 | ❌ |
| 11 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Carbon (medium) | 0.9259 | 56,525.95 | 0.6437 | ✅ |
| 12 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Neon (medium) | 0.9249 | 40,655.23 | 0.6033 | ✅ |
| 13 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (max) | 0.9209 | 824,586.60 | 0.9739 | ❌ |
| 14 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.2 Astra (medium) | 0.9153 | 35,023.23 | 0.5850 | ✅ |
| 15 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.2 Sol (xhigh) | 0.9145 | 26,917.41 | 0.5528 | ✅ |
| 16 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.2 (medium) | 0.9142 | 71,702.72 | 0.6729 | ❌ |
| 17 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.2 Sol (high) | 0.9072 | 14,111.96 | 0.4744 | ✅ |
| 18 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Hydrogen (xhigh) | 0.9066 | 62,516.91 | 0.6561 | ❌ |
| 19 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (xhigh) | 0.9019 | 155,216.64 | 0.7680 | ❌ |
| 20 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.2 (low) | 0.8933 | 59,872.02 | 0.6507 | ❌ |
| 21 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (max) | 0.8923 | 428,550.71 | 0.8932 | ❌ |
| 22 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.2 Sol (medium) | 0.8916 | 9,122.69 | 0.4220 | ✅ |
| 23 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (max) | 0.8908 | 71,705.62 | 0.6729 | ❌ |
| 24 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Carbon (low) | 0.8899 | 24,971.59 | 0.5437 | ❌ |
| 25 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Hydrogen (high) | 0.8894 | 27,373.61 | 0.5549 | ❌ |
| 26 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (max) | 0.8747 | 426,606.33 | 0.8926 | ❌ |
| 27 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (high) | 0.8652 | 61,722.19 | 0.6545 | ❌ |
| 28 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (xhigh) | 0.8644 | 35,993.83 | 0.5883 | ❌ |
| 29 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Wonder Full (max) | 0.8608 | — | — | — |
| 30 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Neon (low) | 0.8570 | 31,446.37 | 0.5718 | ❌ |
| 31 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.2 Astra (low) | 0.8550 | 32,908.05 | 0.5774 | ❌ |
| 32 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (max) | 0.8519 | 793,891.15 | 0.9692 | ❌ |
| 33 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (xhigh) | 0.8482 | 236,342.54 | 0.8198 | ❌ |
| 34 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (high) | 0.8478 | 21,049.99 | 0.5229 | ❌ |
| 35 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Argon (high) | 0.8459 | 84,814.68 | 0.6935 | ❌ |
| 36 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (xhigh) | 0.8407 | 328,539.49 | 0.8604 | ❌ |
| 37 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (medium) | 0.8360 | 42,911.22 | 0.6099 | ❌ |
| 38 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Hydrogen (medium) | 0.8342 | 21,528.14 | 0.5256 | ❌ |
| 39 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (high) | 0.8338 | 142,176.71 | 0.7571 | ❌ |
| 40 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (xhigh) | 0.8278 | 47,772.23 | 0.6230 | ❌ |
| 41 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3.1 Pro | 0.8272 | 55,958.98 | 0.6424 | ❌ |
| 42 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen4 Max | 0.8204 | 42,846.40 | 0.6097 | ❌ |
| 43 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Terra (max) | 0.8177 | 49,452.88 | 0.6273 | ❌ |
| 44 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (medium) | 0.8172 | 56,021.30 | 0.6426 | ❌ |
| 45 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (medium) | 0.8164 | 10,120.04 | 0.4344 | ❌ |
| 46 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Wonder (max) | 0.8154 | 58,567.27 | 0.6480 | ❌ |
| 47 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (high) | 0.8130 | 79,573.16 | 0.6857 | ❌ |
| 48 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.2 Sol (low) | 0.8124 | 8,388.08 | 0.4119 | ✅ |
| 49 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (max) | 0.8084 | 51,218.50 | 0.6316 | ❌ |
| 50 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Argon (medium) | 0.8047 | 32,583.72 | 0.5762 | ❌ |
| 51 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Wonder (high) | 0.7985 | 35,490.77 | 0.5866 | ❌ |
| 52 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (max) | 0.7863 | 98,924.29 | 0.7125 | ❌ |
| 53 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (medium) | 0.7845 | 56,806.29 | 0.6443 | ❌ |
| 54 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Terra (xhigh) | 0.7839 | 12,787.62 | 0.4625 | ❌ |
| 55 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (high) | 0.7721 | 20,231.47 | 0.5180 | ❌ |
| 56 | <img src="https://artificialanalysis.ai/img/logos/tencent-hy.svg" width="18" alt="Tencent" /> Tencent | Tencent Hy4 | 0.7678 | 28,387.00 | 0.5593 | ❌ |
| 57 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (low) | 0.7653 | 51,288.11 | 0.6317 | ❌ |
| 58 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Terra (high) | 0.7625 | 6,889.14 | 0.3886 | ✅ |
| 59 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Haiku 5.5 (max) | 0.7583 | 23,653.29 | 0.5371 | ❌ |
| 60 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Ember (max) | 0.7574 | 1,541.85 | 0.2209 | ✅ |
| 61 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.3 (max) | 0.7554 | 18,653.17 | 0.5082 | ❌ |
| 62 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.7 (xhigh) | 0.7548 | 30,996.08 | 0.5701 | ❌ |
| 63 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (max) | 0.7530 | 91,317.39 | 0.7026 | ❌ |
| 64 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (low) | 0.7494 | 47,740.10 | 0.6229 | ❌ |
| 65 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Ember (xhigh) | 0.7432 | 1,142.85 | 0.1910 | ✅ |
| 66 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.7 (high) | 0.7411 | 25,844.92 | 0.5479 | ❌ |
| 67 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.6-Pro | 0.7408 | 2,386.20 | 0.2673 | ❌ |
| 68 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Terra (medium) | 0.7399 | 5,054.92 | 0.3523 | ❌ |
| 69 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5 | 0.7378 | 326,152.59 | 0.8595 | ❌ |
| 70 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (low) | 0.7353 | 9,213.63 | 0.4231 | ❌ |
| 71 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (low) | 0.7331 | 26,116.88 | 0.5491 | ❌ |
| 72 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3 (max) | 0.7308 | 36,474.53 | 0.5900 | ❌ |
| 73 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (xhigh) | 0.7277 | 66,032.16 | 0.6628 | ❌ |
| 74 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash 1017 (max) | 0.7243 | 8,676.35 | 0.4160 | ❌ |
| 75 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (high) | 0.7225 | 11,844.64 | 0.4533 | ❌ |
| 76 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Hydrogen (low) | 0.7196 | 12,941.38 | 0.4639 | ❌ |
| 77 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (xhigh) | 0.7194 | 24,560.13 | 0.5416 | ❌ |
| 78 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 Max (0902) | 0.7175 | 38,926.36 | 0.5979 | ❌ |
| 79 | <img src="https://artificialanalysis.ai/img/logos/thinking-machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling 2 Small | 0.7151 | 5,104.58 | 0.3534 | ❌ |
| 80 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (high) | 0.7148 | 47,032.29 | 0.6211 | ❌ |
| 81 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Haiku 5.5 (xhigh) | 0.7108 | 5,716.19 | 0.3666 | ❌ |
| 82 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.3 (xhigh) | 0.7103 | 14,831.25 | 0.4804 | ❌ |
| 83 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (max) | 0.7099 | 3,946.35 | 0.3237 | ❌ |
| 84 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3 (max) | 0.7097 | 25,987.14 | 0.5485 | ❌ |
| 85 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (xhigh) | 0.7058 | 47,776.29 | 0.6230 | ❌ |
| 86 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.7 (low) | 0.7042 | 14,506.55 | 0.4777 | ❌ |
| 87 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (max) | 0.7032 | 70,802.85 | 0.6713 | ❌ |
| 88 | <img src="https://artificialanalysis.ai/img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step 5 Preview | 0.7032 | 6,984.56 | 0.3902 | ❌ |
| 89 | <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M3.1-Flash | 0.7019 | 4,097.05 | 0.3280 | ❌ |
| 90 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (xhigh) | 0.7010 | 22,786.85 | 0.5325 | ❌ |
| 91 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (high) | 0.6996 | 14,755.64 | 0.4798 | ❌ |
| 92 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.1 Flash 1019 | 0.6969 | — | — | — |
| 93 | <img src="https://artificialanalysis.ai/img/logos/joy-ai.svg" width="18" alt="Joy Future Academy" /> Joy Future Academy | JoyAI-VL-Preview | 0.6957 | — | — | — |
| 94 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (high) | 0.6914 | 35,040.35 | 0.5851 | ❌ |
| 95 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (medium) | 0.6886 | 30,694.38 | 0.5689 | ❌ |
| 96 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (high) | 0.6884 | 18,275.78 | 0.5057 | ❌ |
| 97 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (medium) | 0.6883 | 9,315.47 | 0.4245 | ❌ |
| 98 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash (max) | 0.6876 | 10,344.23 | 0.4370 | ❌ |
| 99 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (medium) | 0.6806 | 14,231.72 | 0.4754 | ❌ |
| 100 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Terra (low) | 0.6795 | 4,435.38 | 0.3371 | ❌ |
| 101 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash 1017 (high) | 0.6793 | 4,310.17 | 0.3338 | ❌ |
| 102 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3-Flash | 0.6786 | 2,954.04 | 0.2909 | ❌ |
| 103 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (xhigh) | 0.6776 | 98,975.13 | 0.7125 | ❌ |
| 104 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (medium) | 0.6769 | 16,214.99 | 0.4912 | ❌ |
| 105 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 Max | 0.6740 | 44,047.84 | 0.6131 | ❌ |
| 106 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.8 (max) | 0.6739 | 80,564.91 | 0.6872 | ❌ |
| 107 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.1 Flash | 0.6735 | 3,513.01 | 0.3104 | ❌ |
| 108 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Haiku 5.5 (high) | 0.6697 | 2,702.01 | 0.2810 | ❌ |
| 109 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (high) | 0.6697 | — | — | — |
| 110 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (medium) | 0.6673 | 28,308.35 | 0.5590 | ❌ |
| 111 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 2.4T A95B | 0.6655 | 35,501.21 | 0.5867 | ❌ |
| 112 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (medium) | 0.6654 | — | — | — |
| 113 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Large 4 (high) | 0.6630 | 11,372.22 | 0.4484 | ❌ |
| 114 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Terra (non-reasoning) | 0.6540 | 4,416.30 | 0.3366 | ❌ |
| 115 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Large 4 Preview | 0.6529 | 8,442.06 | 0.4127 | ❌ |
| 116 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8-Flash-Next | 0.6516 | 2,904.75 | 0.2890 | ❌ |
| 117 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.5 (high) | 0.6516 | 11,211.48 | 0.4467 | ❌ |
| 118 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (max) | 0.6502 | 5,949.42 | 0.3713 | ❌ |
| 119 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (high) | 0.6495 | 50,102.92 | 0.6289 | ❌ |
| 120 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.6-Flash | 0.6458 | 603.23 | 0.1336 | ✅ |
| 121 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark Open (xhigh) | 0.6447 | 9,924.02 | 0.4320 | ❌ |
| 122 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (xhigh) | 0.6421 | 1,246.91 | 0.1995 | ❌ |
| 123 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.2 (xhigh) | 0.6421 | 12,349.56 | 0.4583 | ❌ |
| 124 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (xhigh) | 0.6414 | 24,434.41 | 0.5410 | ❌ |
| 125 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro 0813 (max) | 0.6413 | 20,302.40 | 0.5185 | ❌ |
| 126 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Large 4 (medium) | 0.6407 | 6,992.67 | 0.3904 | ❌ |
| 127 | <img src="https://artificialanalysis.ai/img/logos/sapiens.svg" width="18" alt="Sapiens AI" /> Sapiens AI | Agnes 2.5 Pro Theta | 0.6340 | 552.73 | 0.1266 | ✅ |
| 128 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (max) | 0.6330 | 144,249.92 | 0.7589 | ❌ |
| 129 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (low) | 0.6316 | 10,808.47 | 0.4423 | ❌ |
| 130 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (low) | 0.6298 | 4,567.97 | 0.3405 | ❌ |
| 131 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro 0813 (high) | 0.6298 | 23,743.53 | 0.5375 | ❌ |
| 132 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (low) | 0.6281 | 26,565.83 | 0.5512 | ❌ |
| 133 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Haiku 5.5 (medium) | 0.6279 | 1,494.37 | 0.2177 | ❌ |
| 134 | <img src="https://artificialanalysis.ai/img/logos/thinking-machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling 2 Mini | 0.6258 | 1,637.87 | 0.2272 | ❌ |
| 135 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (medium) | 0.6250 | — | — | — |
| 136 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (high) | 0.6244 | 933.10 | 0.1717 | ❌ |
| 137 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (xhigh) | 0.6235 | 112,789.02 | 0.7286 | ❌ |
| 138 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (medium) | 0.6220 | 30,507.04 | 0.5681 | ❌ |
| 139 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.7 (max) | 0.6197 | 63,239.99 | 0.6575 | ❌ |
| 140 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash 0731 (max) | 0.6169 | 1,082.20 | 0.1857 | ❌ |
| 141 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (xhigh) | 0.6142 | 3,408.38 | 0.3070 | ❌ |
| 142 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (high) | 0.6128 | 14,390.08 | 0.4767 | ❌ |
| 143 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3 (low) | 0.6111 | 6,919.50 | 0.3891 | ❌ |
| 144 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (low) | 0.6088 | 23,484.28 | 0.5362 | ❌ |
| 145 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.1 Pro Preview | 0.6088 | 28,663.59 | 0.5605 | ❌ |
| 146 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (high) | 0.6072 | 21,574.20 | 0.5259 | ❌ |
| 147 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (xhigh) | 0.6068 | 23,972.72 | 0.5387 | ❌ |
| 148 | <img src="https://artificialanalysis.ai/img/logos/china-mobile.png" width="18" alt="China Mobile" /> China Mobile | JT-4.1 Flash 236B A21B 0709 | 0.6059 | — | — | — |
| 149 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.6 Flash (high) | 0.6058 | 11,051.60 | 0.4449 | ❌ |
| 150 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (low) | 0.6051 | 10,543.67 | 0.4393 | ❌ |
| 151 | <img src="https://artificialanalysis.ai/img/logos/nanbeige.png" width="18" alt="Nanbeige" /> Nanbeige | Nanbeige4.3-33B | 0.6035 | — | — | — |
| 152 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (xhigh) | 0.6032 | 31,953.40 | 0.5738 | ❌ |
| 153 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.2 (max) | 0.6023 | 13,606.31 | 0.4700 | ❌ |
| 154 | <img src="https://artificialanalysis.ai/img/logos/china-mobile.png" width="18" alt="China Mobile" /> China Mobile | JT-4.1 Flash 236B A21B | 0.5993 | — | — | — |
| 155 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash Vision (max) | 0.5979 | 9,641.93 | 0.4286 | ❌ |
| 156 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (medium) | 0.5945 | 667.00 | 0.1419 | ❌ |
| 157 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (low) | 0.5942 | 13,077.36 | 0.4652 | ❌ |
| 158 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (low) | 0.5940 | — | — | — |
| 159 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.1 (xhigh) | 0.5940 | 14,263.85 | 0.4757 | ❌ |
| 160 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.3 Codex (xhigh) | 0.5885 | 51,897.99 | 0.6332 | ❌ |
| 161 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3 (low) | 0.5864 | 13,119.27 | 0.4656 | ❌ |
| 162 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (high) | 0.5853 | 1,823.96 | 0.2384 | ❌ |
| 163 | <img src="https://artificialanalysis.ai/img/logos/reflection.svg" width="18" alt="Reflection" /> Reflection | Beam 1.0 | 0.5844 | 3,358.34 | 0.3053 | ❌ |
| 164 | <img src="https://artificialanalysis.ai/img/logos/sapiens.svg" width="18" alt="Sapiens AI" /> Sapiens AI | Agnes 2.5 Pro Beta | 0.5817 | — | — | — |
| 165 | <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M3 | 0.5782 | 9,445.28 | 0.4261 | ❌ |
| 166 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Haiku 5.5 (low) | 0.5744 | 1,034.10 | 0.1814 | ❌ |
| 167 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (high) | 0.5741 | 23,713.12 | 0.5374 | ❌ |
| 168 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (max) | 0.5699 | 11,456.78 | 0.4493 | ❌ |
| 169 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 375B A23B | 0.5660 | 0.00 | 0.0000 | ✅ |
| 170 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (medium) | 0.5647 | 11,556.08 | 0.4503 | ❌ |
| 171 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.7 Max | 0.5636 | 21,176.05 | 0.5236 | ❌ |
| 172 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (max) | 0.5592 | 122,068.49 | 0.7384 | ❌ |
| 173 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.6 (max) | 0.5526 | 43,220.04 | 0.6108 | ❌ |
| 174 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (medium) | 0.5481 | 19,231.45 | 0.5119 | ❌ |
| 175 | <img src="https://artificialanalysis.ai/img/logos/apodex.svg" width="18" alt="Apodex" /> Apodex | Apodex 1.1 | 0.5465 | — | — | — |
| 176 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (medium) | 0.5459 | 6,509.98 | 0.3819 | ❌ |
| 177 | <img src="https://artificialanalysis.ai/img/logos/motif.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif 3 (Beta) | 0.5436 | — | — | — |
| 178 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (non-reasoning) | 0.5426 | 10,526.50 | 0.4391 | ❌ |
| 179 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.6 | 0.5399 | 15,874.37 | 0.4886 | ❌ |
| 180 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3.5 Super VL | 0.5354 | 2,513.96 | 0.2730 | ❌ |
| 181 | <img src="https://artificialanalysis.ai/img/logos/thinking-machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling (xhigh) | 0.5347 | 9,878.33 | 0.4315 | ❌ |
| 182 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (medium) | 0.5344 | 11,912.48 | 0.4539 | ❌ |
| 183 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark | 0.5339 | — | — | — |
| 184 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (low) | 0.5335 | 23,971.07 | 0.5387 | ❌ |
| 185 | <img src="https://artificialanalysis.ai/img/logos/motif.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif 3 | 0.5329 | — | — | — |
| 186 | <img src="https://artificialanalysis.ai/img/logos/thinking-machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling Small | 0.5316 | 2,477.07 | 0.2714 | ❌ |
| 187 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (xhigh) | 0.5301 | 95,444.28 | 0.7081 | ❌ |
| 188 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (xhigh) | 0.5291 | 95,043.35 | 0.7076 | ❌ |
| 189 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (low) | 0.5286 | 11,656.42 | 0.4513 | ❌ |
| 190 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 32B | 0.5284 | — | — | — |
| 191 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (low) | 0.5277 | 5,281.49 | 0.3574 | ❌ |
| 192 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.7 (non-reasoning, high) | 0.5274 | 22,897.82 | 0.5331 | ❌ |
| 193 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.7 Code | 0.5270 | 9,819.83 | 0.4308 | ❌ |
| 194 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (high) | 0.5251 | — | — | — |
| 195 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 Codex (xhigh) | 0.5233 | 59,896.31 | 0.6508 | ❌ |
| 196 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (max) | 0.5219 | 512.96 | 0.1207 | ❌ |
| 197 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.7 Plus | 0.5215 | 5,759.92 | 0.3675 | ❌ |
| 198 | <img src="https://artificialanalysis.ai/img/logos/thinking-machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling (high) | 0.5203 | 10,038.70 | 0.4334 | ❌ |
| 199 | <img src="https://artificialanalysis.ai/img/logos/tencent-hy.svg" width="18" alt="Tencent" /> Tencent | Hy3 | 0.5195 | 2,127.61 | 0.2549 | ❌ |
| 200 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3 Pro Preview (high) | 0.5171 | — | — | — |
| 201 | <img src="https://artificialanalysis.ai/img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 4 | 0.5171 | 4,144.57 | 0.3293 | ❌ |
| 202 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash 1017 (non-reasoning) | 0.5141 | 1,112.45 | 0.1884 | ❌ |
| 203 | <img src="https://artificialanalysis.ai/img/logos/nex.svg" width="18" alt="Nex AGI" /> Nex AGI | Nex-N2-Pro | 0.5134 | — | — | — |
| 204 | <img src="https://artificialanalysis.ai/img/logos/multiversecomputing.svg" width="18" alt="Multiverse Computing" /> Multiverse Computing | Quasar 438B (max) | 0.5134 | — | — | — |
| 205 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3 Flash | 0.5130 | 5,125.99 | 0.3539 | ❌ |
| 206 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 Max Preview | 0.5122 | — | — | — |
| 207 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok Build 0.1 0616 | 0.5104 | 6,414.56 | 0.3802 | ❌ |
| 208 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5-Pro | 0.5096 | — | — | — |
| 209 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 v2 | 0.5066 | 7,342.88 | 0.3961 | ❌ |
| 210 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash-Lite | 0.5055 | 5,414.23 | 0.3603 | ❌ |
| 211 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon MoVA 36B A4B | 0.5029 | — | — | — |
| 212 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (low) | 0.5026 | 13,723.78 | 0.4710 | ❌ |
| 213 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 Plus | 0.5024 | 7,450.30 | 0.3979 | ❌ |
| 214 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.1 | 0.5015 | 13,633.59 | 0.4702 | ❌ |
| 215 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (medium) | 0.5012 | 1,250.77 | 0.1998 | ❌ |
| 216 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro 0813 (non-reasoning) | 0.5007 | 4,049.97 | 0.3267 | ❌ |
| 217 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (low) | 0.4998 | 535.30 | 0.1241 | ❌ |
| 218 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-3.0-flash-VL | 0.4987 | — | — | — |
| 219 | <img src="https://artificialanalysis.ai/img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Mini 4 | 0.4985 | 1,876.40 | 0.2414 | ❌ |
| 220 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (non-reasoning) | 0.4974 | 20,865.36 | 0.5218 | ❌ |
| 221 | <img src="https://artificialanalysis.ai/img/logos/thinking-machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling Small (high) | 0.4970 | 2,387.54 | 0.2674 | ❌ |
| 222 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (high) | 0.4960 | — | — | — |
| 223 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 | 0.4938 | — | — | — |
| 224 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Ultra | 0.4924 | 6,074.16 | 0.3738 | ❌ |
| 225 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (high) | 0.4909 | 6,952.00 | 0.3897 | ❌ |
| 226 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (low) | 0.4902 | 10,301.20 | 0.4365 | ❌ |
| 227 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (medium) | 0.4863 | 6,212.45 | 0.3764 | ❌ |
| 228 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-3.0-flash-Fin | 0.4851 | — | — | — |
| 229 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (xhigh) | 0.4833 | 11,097.44 | 0.4454 | ❌ |
| 230 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 Instant (June 2026) | 0.4828 | 28,129.86 | 0.5582 | ❌ |
| 231 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 397B A17B | 0.4827 | 9,333.91 | 0.4247 | ❌ |
| 232 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5 | 0.4780 | 10,486.88 | 0.4386 | ❌ |
| 233 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Pro | 0.4772 | — | — | — |
| 234 | <img src="https://artificialanalysis.ai/img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Open2 250B | 0.4725 | — | — | — |
| 235 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Glimmer (high) | 0.4712 | 3,285.34 | 0.3029 | ❌ |
| 236 | <img src="https://artificialanalysis.ai/img/logos/sktelecom.svg" width="18" alt="SK Telecom" /> SK Telecom | A.X-K2 | 0.4712 | — | — | — |
| 237 | <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.7 | 0.4706 | 2,015.25 | 0.2490 | ❌ |
| 238 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5 | 0.4696 | — | — | — |
| 239 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 27B | 0.4666 | 8,633.16 | 0.4154 | ❌ |
| 240 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.5 | 0.4641 | 40,839.88 | 0.6038 | ❌ |
| 241 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 27B | 0.4628 | 3,355.02 | 0.3052 | ❌ |
| 242 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 (high) | 0.4622 | 45,118.76 | 0.6160 | ❌ |
| 243 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (non-reasoning) | 0.4621 | 492.04 | 0.1176 | ❌ |
| 244 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 7B | 0.4588 | — | — | — |
| 245 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.5 | 0.4585 | 7,535.79 | 0.3992 | ❌ |
| 246 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash (non-reasoning) | 0.4581 | 1,051.81 | 0.1830 | ❌ |
| 247 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (medium) | 0.4566 | 15,571.91 | 0.4863 | ❌ |
| 248 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.0 Flash | 0.4552 | 547.68 | 0.1258 | ❌ |
| 249 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (low) | 0.4542 | 1,144.60 | 0.1911 | ❌ |
| 250 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (high) | 0.4540 | 65,534.76 | 0.6618 | ❌ |
| 251 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (non-reasoning) | 0.4533 | 3,910.34 | 0.3227 | ❌ |
| 252 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5-Turbo | 0.4532 | — | — | — |
| 253 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (non-reasoning) | 0.4507 | 10,257.05 | 0.4360 | ❌ |
| 254 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 Codex (high) | 0.4503 | 21,757.66 | 0.5269 | ❌ |
| 255 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (non-reasoning) | 0.4495 | 10,321.88 | 0.4367 | ❌ |
| 256 | <img src="https://artificialanalysis.ai/img/logos/kwaikat.svg" width="18" alt="KwaiKAT" /> KwaiKAT | KAT-Coder-Pro V2 | 0.4456 | — | — | — |
| 257 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3.5 Bolt 74B-A9B | 0.4456 | — | — | — |
| 258 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Omni-0327 | 0.4435 | — | — | — |
| 259 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 31B | 0.4434 | 0.00 | 0.0000 | ❌ |
| 260 | <img src="https://artificialanalysis.ai/img/logos/tencent-hy.svg" width="18" alt="Tencent" /> Tencent | Hy3-preview | 0.4433 | — | — | — |
| 261 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM3-1.7B | 0.4429 | 1,101.65 | 0.1874 | ❌ |
| 262 | <img src="https://artificialanalysis.ai/img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step 3.7 Flash | 0.4396 | 2,617.69 | 0.2775 | ❌ |
| 263 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.1 Flash-Lite | 0.4388 | 6,944.92 | 0.3895 | ❌ |
| 264 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 Instant (May 2026) | 0.4388 | — | — | — |
| 265 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max Thinking | 0.4381 | — | — | — |
| 266 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (medium) | 0.4377 | 23,775.98 | 0.5377 | ❌ |
| 267 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Speciale | 0.4376 | — | — | — |
| 268 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 Codex (high) | 0.4352 | 22,513.62 | 0.5310 | ❌ |
| 269 | <img src="https://artificialanalysis.ai/img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE 2.0 | 0.4347 | — | — | — |
| 270 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (minimal) | 0.4345 | 9,984.65 | 0.4328 | ❌ |
| 271 | <img src="https://artificialanalysis.ai/img/logos/china-mobile.png" width="18" alt="China Mobile" /> China Mobile | JT-4.1 Flash 236B A21B 0709 (non-reasoning) | 0.4339 | — | — | — |
| 272 | <img src="https://artificialanalysis.ai/img/logos/longcat.svg" width="18" alt="LongCat" /> LongCat | LongCat 2.0 | 0.4333 | 9,906.81 | 0.4318 | ❌ |
| 273 | <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.5 | 0.4327 | 2,429.23 | 0.2693 | ❌ |
| 274 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Sonnet | 0.4323 | 24,108.57 | 0.5394 | ❌ |
| 275 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 122B A10B | 0.4303 | 6,629.24 | 0.3841 | ❌ |
| 276 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 35B A3B | 0.4292 | 4,954.90 | 0.3500 | ❌ |
| 277 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Medium 3.5 | 0.4276 | 24,311.91 | 0.5404 | ❌ |
| 278 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (non-reasoning) | 0.4273 | 23,365.09 | 0.5356 | ❌ |
| 279 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7 | 0.4260 | 7,884.11 | 0.4046 | ❌ |
| 280 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 3.7B | 0.4255 | — | — | — |
| 281 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.6 (non-reasoning, high) | 0.4235 | 22,699.07 | 0.5320 | ❌ |
| 282 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash (Feb 2026) | 0.4225 | — | — | — |
| 283 | <img src="https://artificialanalysis.ai/img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step 3.5 Flash 2603 | 0.4190 | 1,187.25 | 0.1947 | ❌ |
| 284 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 | 0.4186 | 881.44 | 0.1665 | ❌ |
| 285 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.1 (non-reasoning) | 0.4181 | 7,340.58 | 0.3961 | ❌ |
| 286 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3 Pro Preview (low) | 0.4163 | — | — | — |
| 287 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-2.6-1T | 0.4151 | — | — | — |
| 288 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 35B A3B | 0.4151 | 3,557.54 | 0.3119 | ❌ |
| 289 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 | 0.4140 | 26,602.97 | 0.5514 | ❌ |
| 290 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (low) | 0.4133 | 5,457.72 | 0.3612 | ❌ |
| 291 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Omni | 0.4125 | — | — | — |
| 292 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Haiku | 0.4111 | 13,417.66 | 0.4683 | ❌ |
| 293 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 Thinking | 0.4096 | 13,110.03 | 0.4655 | ❌ |
| 294 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o3 | 0.4066 | 14,377.62 | 0.4766 | ❌ |
| 295 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (medium) | 0.4062 | 6,145.29 | 0.3751 | ❌ |
| 296 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM 5V Turbo | 0.4051 | — | — | — |
| 297 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash | 0.4015 | — | — | — |
| 298 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (high) | 0.3989 | 8,789.34 | 0.4175 | ❌ |
| 299 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3.5 Lightning | 0.3961 | 1,288.98 | 0.2028 | ❌ |
| 300 | <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.1 | 0.3917 | — | — | — |
| 301 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.6 (non-reasoning) | 0.3901 | 5,230.58 | 0.3563 | ❌ |
| 302 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM3-VL-2B | 0.3870 | 1,461.86 | 0.2155 | ❌ |
| 303 | <img src="https://artificialanalysis.ai/img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | G9v3-39A5B | 0.3850 | — | — | — |
| 304 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (non-reasoning, high) | 0.3850 | 14,952.13 | 0.4814 | ❌ |
| 305 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 27B (non-reasoning) | 0.3839 | 3,897.01 | 0.3223 | ❌ |
| 306 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 Codex mini (high) | 0.3838 | 4,754.72 | 0.3452 | ❌ |
| 307 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 26B A4B | 0.3829 | 1,388.70 | 0.2103 | ❌ |
| 308 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.2 30B | 0.3824 | — | — | — |
| 309 | <img src="https://artificialanalysis.ai/img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step 3.5 Flash | 0.3814 | 1,086.04 | 0.1860 | ❌ |
| 310 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 122B A10B (non-reasoning) | 0.3809 | 3,396.88 | 0.3066 | ❌ |
| 311 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 Terminus | 0.3793 | — | — | — |
| 312 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Pro | 0.3778 | 28,890.16 | 0.5615 | ❌ |
| 313 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 397B A17B (non-reasoning) | 0.3762 | 2,630.43 | 0.2780 | ❌ |
| 314 | <img src="https://artificialanalysis.ai/img/logos/cohere.svg" width="18" alt="Cohere" /> Cohere | Command A+ | 0.3756 | 0.00 | 0.0000 | ❌ |
| 315 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 27B (non-reasoning) | 0.3751 | 1,471.89 | 0.2162 | ❌ |
| 316 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-120b (high) | 0.3748 | 2,684.03 | 0.2803 | ❌ |
| 317 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (non-reasoning, low) | 0.3737 | 13,397.43 | 0.4681 | ❌ |
| 318 | <img src="https://artificialanalysis.ai/img/logos/kwaikat.svg" width="18" alt="KwaiKAT" /> KwaiKAT | KAT-Coder-Pro V1 | 0.3718 | — | — | — |
| 319 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (low) | 0.3705 | 12,707.83 | 0.4617 | ❌ |
| 320 | <img src="https://artificialanalysis.ai/img/logos/cohere.svg" width="18" alt="Cohere" /> Cohere | North Mini Code | 0.3687 | 0.00 | 0.0000 | ❌ |
| 321 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (medium) | 0.3657 | 1,819.75 | 0.2382 | ❌ |
| 322 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (medium) | 0.3655 | 3,201.37 | 0.2999 | ❌ |
| 323 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Super | 0.3653 | 3,872.86 | 0.3216 | ❌ |
| 324 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 35B A3B (non-reasoning) | 0.3606 | 1,984.78 | 0.2474 | ❌ |
| 325 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.5 (non-reasoning) | 0.3604 | 22,552.74 | 0.5313 | ❌ |
| 326 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.2 (non-reasoning) | 0.3601 | 5,156.06 | 0.3546 | ❌ |
| 327 | <img src="https://artificialanalysis.ai/img/logos/inceptionlabs.svg" width="18" alt="Inception" /> Inception | Mercury 2.5 | 0.3597 | 1,639.71 | 0.2273 | ❌ |
| 328 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (non-reasoning) | 0.3566 | 1,143.31 | 0.1910 | ❌ |
| 329 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.1 Fast | 0.3564 | — | — | — |
| 330 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3 Flash (non-reasoning) | 0.3563 | 2,615.81 | 0.2774 | ❌ |
| 331 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.2 8B | 0.3560 | 1,447.84 | 0.2145 | ❌ |
| 332 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Small 4 | 0.3551 | 1,681.65 | 0.2299 | ❌ |
| 333 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.0 Tiny | 0.3537 | 0.00 | 0.0000 | ❌ |
| 334 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.1 Opus | 0.3533 | — | — | — |
| 335 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 9B | 0.3521 | 841.61 | 0.1623 | ❌ |
| 336 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 Omni Plus | 0.3496 | 3,497.71 | 0.3100 | ❌ |
| 337 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Exp | 0.3482 | — | — | — |
| 338 | <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2 | 0.3465 | 1,328.62 | 0.2058 | ❌ |
| 339 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6 | 0.3462 | 5,651.52 | 0.3653 | ❌ |
| 340 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o4-mini (high) | 0.3449 | 12,982.65 | 0.4643 | ❌ |
| 341 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (non-reasoning) | 0.3444 | 14,912.83 | 0.4810 | ❌ |
| 342 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Opus | 0.3443 | — | — | — |
| 343 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Sonnet | 0.3421 | — | — | — |
| 344 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 12B | 0.3407 | — | — | — |
| 345 | <img src="https://artificialanalysis.ai/img/logos/inceptionlabs.svg" width="18" alt="Inception" /> Inception | Mercury 2 | 0.3397 | 1,885.93 | 0.2420 | ❌ |
| 346 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 Fast | 0.3395 | — | — | — |
| 347 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 35B A3B (non-reasoning) | 0.3345 | 2,163.63 | 0.2567 | ❌ |
| 348 | <img src="https://artificialanalysis.ai/img/logos/bytedance.svg" width="18" alt="ByteDance Seed" /> ByteDance Seed | Doubao Seed Code | 0.3333 | — | — | — |
| 349 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 31B (non-reasoning) | 0.3307 | 1,679.35 | 0.2298 | ❌ |
| 350 | <img src="https://artificialanalysis.ai/img/logos/china-mobile.png" width="18" alt="China Mobile" /> China Mobile | JT-35B-Flash | 0.3298 | — | — | — |
| 351 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (medium) | 0.3290 | 24,672.02 | 0.5422 | ❌ |
| 352 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.5 (non-reasoning) | 0.3285 | 7,649.00 | 0.4010 | ❌ |
| 353 | <img src="https://artificialanalysis.ai/img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE | 0.3274 | — | — | — |
| 354 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (non-reasoning) | 0.3255 | 4,286.79 | 0.3332 | ❌ |
| 355 | <img src="https://artificialanalysis.ai/img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-2B | 0.3252 | — | — | — |
| 356 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5-Pro (non-reasoning) | 0.3234 | — | — | — |
| 357 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder Next | 0.3228 | 3,502.78 | 0.3101 | ❌ |
| 358 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B A22B 2507 | 0.3225 | — | — | — |
| 359 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 (non-reasoning) | 0.3218 | — | — | — |
| 360 | <img src="https://artificialanalysis.ai/img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.5 33B | 0.3209 | — | — | — |
| 361 | <img src="https://artificialanalysis.ai/img/logos/arcee.svg" width="18" alt="Arcee AI" /> Arcee AI | Trinity Large Thinking | 0.3206 | — | — | — |
| 362 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Sep) | 0.3192 | — | — | — |
| 363 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 | 0.3185 | 5,096.49 | 0.3532 | ❌ |
| 364 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-2.6-1T | 0.3183 | — | — | — |
| 365 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.2 3B | 0.3173 | — | — | — |
| 366 | <img src="https://artificialanalysis.ai/img/logos/baidu.svg" width="18" alt="Baidu" /> Baidu | ERNIE 5.0 Thinking Preview | 0.3158 | — | — | — |
| 367 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 v2 (non-reasoning) | 0.3156 | 4,382.65 | 0.3358 | ❌ |
| 368 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (non-reasoning) | 0.3147 | 5,412.92 | 0.3603 | ❌ |
| 369 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 235B A22B | 0.3068 | — | — | — |
| 370 | <img src="https://artificialanalysis.ai/img/logos/multiversecomputing.svg" width="18" alt="Multiverse Computing" /> Multiverse Computing | HyperNova 60B 2605 (high) | 0.3035 | — | — | — |
| 371 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (high) | 0.3034 | 9,839.70 | 0.4310 | ❌ |
| 372 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash | 0.3026 | 7,151.77 | 0.3930 | ❌ |
| 373 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 (non-reasoning) | 0.3017 | 454.45 | 0.1116 | ❌ |
| 374 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-20b (high) | 0.3010 | 1,188.62 | 0.1948 | ❌ |
| 375 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (medium) | 0.3005 | 7,734.58 | 0.4023 | ❌ |
| 376 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 0528 | 0.2998 | 22,434.86 | 0.5306 | ❌ |
| 377 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5 (non-reasoning) | 0.2996 | 4,453.34 | 0.3376 | ❌ |
| 378 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max Thinking (Preview) | 0.2988 | — | — | — |
| 379 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max | 0.2962 | — | — | — |
| 380 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (non-reasoning) | 0.2957 | — | — | — |
| 381 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5 | 0.2956 | — | — | — |
| 382 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 4B | 0.2949 | — | — | — |
| 383 | <img src="https://artificialanalysis.ai/img/logos/servicenow.svg" width="18" alt="ServiceNow" /> ServiceNow | Apriel-v1.6-15B-Thinker | 0.2948 | — | — | — |
| 384 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 3 mini Reasoning (high) | 0.2947 | — | — | — |
| 385 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (non-reasoning) | 0.2942 | 11,281.40 | 0.4474 | ❌ |
| 386 | <img src="https://artificialanalysis.ai/img/logos/tencent-hy.svg" width="18" alt="Tencent" /> Tencent | Hy3-preview (non-reasoning) | 0.2938 | — | — | — |
| 387 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 26B A4B (non-reasoning) | 0.2914 | 1,010.58 | 0.1792 | ❌ |
| 388 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash (non-reasoning) | 0.2888 | — | — | — |
| 389 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o3-mini (high) | 0.2885 | 20,992.00 | 0.5225 | ❌ |
| 390 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Sonnet (non-reasoning) | 0.2866 | 13,636.50 | 0.4702 | ❌ |
| 391 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (low) | 0.2866 | 11,774.62 | 0.4525 | ❌ |
| 392 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 32B | 0.2860 | — | — | — |
| 393 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron Cascade 2 30B A3B | 0.2858 | — | — | — |
| 394 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (medium) | 0.2833 | — | — | — |
| 395 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o1 | 0.2830 | — | — | — |
| 396 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano | 0.2811 | 901.52 | 0.1685 | ❌ |
| 397 | <img src="https://artificialanalysis.ai/img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 3 | 0.2784 | 1,256.47 | 0.2003 | ❌ |
| 398 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 E4B | 0.2778 | — | — | — |
| 399 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max (Preview) | 0.2762 | — | — | — |
| 400 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 0905 | 0.2753 | 1,579.91 | 0.2234 | ❌ |
| 401 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 9B (non-reasoning) | 0.2752 | 282.70 | 0.0802 | ❌ |
| 402 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Devstral 2 | 0.2724 | — | — | — |
| 403 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Sep) | 0.2717 | — | — | — |
| 404 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Exp (non-reasoning) | 0.2706 | — | — | — |
| 405 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 (Jan) | 0.2704 | 6,565.50 | 0.3829 | ❌ |
| 406 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Sep) (non-reasoning) | 0.2702 | — | — | — |
| 407 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (high) | 0.2688 | 3,553.17 | 0.3117 | ❌ |
| 408 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7 (non-reasoning) | 0.2688 | 4,743.28 | 0.3449 | ❌ |
| 409 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-1T | 0.2687 | — | — | — |
| 410 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 Terminus (non-reasoning) | 0.2682 | — | — | — |
| 411 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.7 Sonnet | 0.2681 | — | — | — |
| 412 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Next 80B A3B | 0.2681 | — | — | — |
| 413 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 0.9B | 0.2672 | — | — | — |
| 414 | <img src="https://artificialanalysis.ai/img/logos/bytedance.svg" width="18" alt="ByteDance Seed" /> ByteDance Seed | Seed-OSS-36B-Instruct | 0.2671 | 1,545.04 | 0.2211 | ❌ |
| 415 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (low) | 0.2667 | — | — | — |
| 416 | <img src="https://artificialanalysis.ai/img/logos/servicenow.svg" width="18" alt="ServiceNow" /> ServiceNow | Apriel-v1.5-15B-Thinker | 0.2656 | — | — | — |
| 417 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5-Air | 0.2655 | 2,159.15 | 0.2565 | ❌ |
| 418 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | DiffusionGemma 26B A4B | 0.2652 | — | — | — |
| 419 | <img src="https://artificialanalysis.ai/img/logos/deepcogito.png" width="18" alt="Deep Cogito" /> Deep Cogito | Cogito v2.1 | 0.2649 | — | — | — |
| 420 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (medium) | 0.2634 | 1,662.10 | 0.2287 | ❌ |
| 421 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano 4B | 0.2629 | — | — | — |
| 422 | <img src="https://artificialanalysis.ai/img/logos/prime-intellect.svg" width="18" alt="Prime Intellect" /> Prime Intellect | INTELLECT-3 | 0.2617 | — | — | — |
| 423 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7-Flash | 0.2612 | 746.60 | 0.1516 | ❌ |
| 424 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok Code Fast 1 | 0.2602 | — | — | — |
| 425 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Sonnet (non-reasoning) | 0.2590 | — | — | — |
| 426 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B A3B 2507 | 0.2580 | — | — | — |
| 427 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Large 3 | 0.2578 | 1,784.19 | 0.2361 | ❌ |
| 428 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 Omni Flash | 0.2571 | 658.56 | 0.1409 | ❌ |
| 429 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Magistral Medium 1.2 | 0.2560 | — | — | — |
| 430 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 (non-reasoning) | 0.2547 | 4,925.43 | 0.3493 | ❌ |
| 431 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (high) | 0.2535 | — | — | — |
| 432 | <img src="https://artificialanalysis.ai/img/logos/celeris.svg" width="18" alt="Celeris" /> Celeris | Celeris-1 | 0.2532 | 1,252.49 | 0.2000 | ❌ |
| 433 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 | 0.2531 | 1,718.35 | 0.2322 | ❌ |
| 434 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 2.6 Flash | 0.2515 | — | — | — |
| 435 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B 2507 | 0.2503 | 2,785.54 | 0.2844 | ❌ |
| 436 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 30B A3B | 0.2497 | — | — | — |
| 437 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Medium 3.1 | 0.2478 | — | — | — |
| 438 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (non-reasoning) | 0.2462 | 4,532.81 | 0.3396 | ❌ |
| 439 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Devstral Small 2 | 0.2456 | — | — | — |
| 440 | <img src="https://artificialanalysis.ai/img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.0 32B | 0.2450 | — | — | — |
| 441 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 (non-reasoning) | 0.2448 | 8,058.03 | 0.4072 | ❌ |
| 442 | <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax M1 80k | 0.2444 | 2,012.62 | 0.2489 | ❌ |
| 443 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (minimal) | 0.2444 | 9,327.74 | 0.4246 | ❌ |
| 444 | <img src="https://artificialanalysis.ai/img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Open 100B | 0.2431 | — | — | — |
| 445 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Next 80B A3B | 0.2410 | 1,575.24 | 0.2231 | ❌ |
| 446 | <img src="https://artificialanalysis.ai/img/logos/tii.svg" width="18" alt="TII UAE" /> TII UAE | Falcon-H1R-7B | 0.2390 | — | — | — |
| 447 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3 0324 | 0.2389 | — | — | — |
| 448 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 235B A22B | 0.2373 | 2,363.14 | 0.2663 | ❌ |
| 449 | <img src="https://artificialanalysis.ai/img/logos/motif.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif-2-12.7B | 0.2371 | — | — | — |
| 450 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-120b (low) | 0.2359 | 1,639.38 | 0.2273 | ❌ |
| 451 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.7 Sonnet (non-reasoning) | 0.2359 | — | — | — |
| 452 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (non-reasoning) | 0.2349 | 2,027.79 | 0.2497 | ❌ |
| 453 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Think V2 | 0.2347 | — | — | — |
| 454 | <img src="https://artificialanalysis.ai/img/logos/korea-telecom.png" width="18" alt="Korea Telecom" /> Korea Telecom | Mi:dm K 2.5 Pro | 0.2347 | — | — | — |
| 455 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 4B (non-reasoning) | 0.2337 | — | — | — |
| 456 | <img src="https://artificialanalysis.ai/img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step3 VL 10B | 0.2333 | — | — | — |
| 457 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (ChatGPT) | 0.2318 | — | — | — |
| 458 | <img src="https://artificialanalysis.ai/img/logos/nousresearch.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 405B | 0.2310 | 4,101.63 | 0.3281 | ❌ |
| 459 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-1T | 0.2310 | — | — | — |
| 460 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Haiku (non-reasoning) | 0.2307 | 4,608.18 | 0.3416 | ❌ |
| 461 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-flash-2.0 | 0.2307 | — | — | — |
| 462 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Sep) (non-reasoning) | 0.2302 | — | — | — |
| 463 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 | 0.2297 | 12,736.59 | 0.4620 | ❌ |
| 464 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6 (non-reasoning) | 0.2294 | 5,800.01 | 0.3683 | ❌ |
| 465 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (non-reasoning) | 0.2294 | 7,560.36 | 0.3996 | ❌ |
| 466 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder 480B | 0.2291 | 3,627.27 | 0.3141 | ❌ |
| 467 | <img src="https://artificialanalysis.ai/img/logos/korea-telecom.png" width="18" alt="Korea Telecom" /> Korea Telecom | Mi:dm K 2.5 Pro Preview | 0.2290 | — | — | — |
| 468 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 3 | 0.2290 | — | — | — |
| 469 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o3-mini | 0.2289 | 12,368.12 | 0.4585 | ❌ |
| 470 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B 2507 | 0.2288 | — | — | — |
| 471 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Super 49B v1.5 | 0.2287 | — | — | — |
| 472 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 12B (non-reasoning) | 0.2274 | — | — | — |
| 473 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (low) | 0.2274 | 4,578.11 | 0.3408 | ❌ |
| 474 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (minimal) | 0.2273 | 1,625.07 | 0.2264 | ❌ |
| 475 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Opus (non-reasoning) | 0.2273 | — | — | — |
| 476 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite | 0.2238 | 2,483.30 | 0.2717 | ❌ |
| 477 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 32B | 0.2238 | — | — | — |
| 478 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Omni 30B A3B | 0.2232 | 2,835.87 | 0.2864 | ❌ |
| 479 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 32B | 0.2232 | 926.15 | 0.1710 | ❌ |
| 480 | <img src="https://artificialanalysis.ai/img/logos/china-mobile.png" width="18" alt="China Mobile" /> China Mobile | JT-MINI | 0.2224 | — | — | — |
| 481 | <img src="https://artificialanalysis.ai/img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE (non-reasoning) | 0.2223 | — | — | — |
| 482 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B | 0.2222 | — | — | — |
| 483 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Small 3.1 | 0.2216 | — | — | — |
| 484 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 mini | 0.2177 | 2,222.18 | 0.2596 | ❌ |
| 485 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-20b (low) | 0.2173 | 140.86 | 0.0464 | ❌ |
| 486 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Ultra | 0.2169 | — | — | — |
| 487 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 4 Maverick | 0.2141 | 3,787.54 | 0.3190 | ❌ |
| 488 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6V | 0.2123 | 2,649.31 | 0.2788 | ❌ |
| 489 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Magistral Small 1.2 | 0.2116 | 873.82 | 0.1657 | ❌ |
| 490 | <img src="https://artificialanalysis.ai/img/logos/longcat.svg" width="18" alt="LongCat" /> LongCat | LongCat Flash Lite | 0.2102 | — | — | — |
| 491 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 30B A3B | 0.2096 | 517.58 | 0.1214 | ❌ |
| 492 | <img src="https://artificialanalysis.ai/img/logos/naver.webp" width="18" alt="Naver" /> Naver | HyperCLOVA X SEED Think (32B) | 0.2069 | — | — | — |
| 493 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Ministral 3 14B | 0.2058 | 448.43 | 0.1107 | ❌ |
| 494 | <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax M1 40k | 0.2050 | — | — | — |
| 495 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 14B | 0.2047 | 307.68 | 0.0853 | ❌ |
| 496 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3 (Dec) | 0.2044 | 679.55 | 0.1435 | ❌ |
| 497 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | QwQ-32B | 0.2039 | — | — | — |
| 498 | <img src="https://artificialanalysis.ai/img/logos/nousresearch.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 70B | 0.2032 | — | — | — |
| 499 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (medium) | 0.2012 | — | — | — |
| 500 | <img src="https://artificialanalysis.ai/img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam 105B (high) | 0.2003 | 712.65 | 0.1476 | ❌ |
| 501 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-flash-2.0 | 0.1994 | 500.94 | 0.1189 | ❌ |
| 502 | <img src="https://artificialanalysis.ai/img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 2 | 0.1988 | — | — | — |
| 503 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.1 Fast (non-reasoning) | 0.1979 | — | — | — |
| 504 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 32B Think | 0.1970 | — | — | — |
| 505 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3.1 32B Think | 0.1961 | — | — | — |
| 506 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B A3B 2507 (non-reasoning) | 0.1935 | 239.68 | 0.0709 | ❌ |
| 507 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Magistral Medium 1 | 0.1925 | — | — | — |
| 508 | <img src="https://artificialanalysis.ai/img/logos/trillionlabs.svg" width="18" alt="Trillion Labs" /> Trillion Labs | Tri-21B-Think | 0.1886 | — | — | — |
| 509 | <img src="https://artificialanalysis.ai/img/logos/baidu.svg" width="18" alt="Baidu" /> Baidu | ERNIE 4.5 300B A47B | 0.1884 | — | — | — |
| 510 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (non-reasoning) | 0.1882 | 1,043.07 | 0.1822 | ❌ |
| 511 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano Omni 30B A3B | 0.1877 | — | — | — |
| 512 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 12B v2 VL | 0.1867 | — | — | — |
| 513 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B | 0.1864 | 1,360.94 | 0.2082 | ❌ |
| 514 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Ministral 3 8B | 0.1829 | 337.59 | 0.0911 | ❌ |
| 515 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 Fast (non-reasoning) | 0.1794 | — | — | — |
| 516 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 8B | 0.1792 | — | — | — |
| 517 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5V | 0.1786 | 3,342.36 | 0.3048 | ❌ |
| 518 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder 30B A3B | 0.1774 | 1,411.46 | 0.2119 | ❌ |
| 519 | <img src="https://artificialanalysis.ai/img/logos/trillionlabs.svg" width="18" alt="Trillion Labs" /> Trillion Labs | Tri-21B-think Preview | 0.1756 | — | — | — |
| 520 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Magistral Small 1 | 0.1732 | — | — | — |
| 521 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 8B | 0.1730 | — | — | — |
| 522 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.0 Flash | 0.1725 | — | — | — |
| 523 | <img src="https://artificialanalysis.ai/img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.0 32B (non-reasoning) | 0.1719 | — | — | — |
| 524 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 9B V2 | 0.1711 | — | — | — |
| 525 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 4 Scout | 0.1677 | 516.98 | 0.1213 | ❌ |
| 526 | <img src="https://artificialanalysis.ai/img/logos/nousresearch.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 405B (non-reasoning) | 0.1676 | 2,639.05 | 0.2784 | ❌ |
| 527 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Small 3.2 | 0.1673 | 185.74 | 0.0581 | ❌ |
| 528 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 9B V2 (non-reasoning) | 0.1671 | 159.68 | 0.0514 | ❌ |
| 529 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Medium 3 | 0.1671 | 1,630.78 | 0.2267 | ❌ |
| 530 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.3 Nemotron Super 49B | 0.1669 | — | — | — |
| 531 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 7B Think | 0.1665 | — | — | — |
| 532 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova Premier | 0.1664 | — | — | — |
| 533 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-2.6B | 0.1653 | — | — | — |
| 534 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o (Aug) | 0.1644 | 19,726.99 | 0.5150 | ❌ |
| 535 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o (Nov) | 0.1641 | 24,349.65 | 0.5406 | ❌ |
| 536 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 E4B (non-reasoning) | 0.1633 | — | — | — |
| 537 | <img src="https://artificialanalysis.ai/img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | G9v3-3B | 0.1629 | — | — | — |
| 538 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.1 30B | 0.1627 | — | — | — |
| 539 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 0528 Qwen3 8B | 0.1615 | — | — | — |
| 540 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Omni 30B A3B | 0.1586 | 725.51 | 0.1491 | ❌ |
| 541 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (non-reasoning) | 0.1583 | 1,940.01 | 0.2450 | ❌ |
| 542 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (low) | 0.1582 | — | — | — |
| 543 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (non-reasoning) | 0.1581 | — | — | — |
| 544 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Small 4 (non-reasoning) | 0.1578 | 660.09 | 0.1411 | ❌ |
| 545 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Ministral 3 3B | 0.1573 | 240.58 | 0.0711 | ❌ |
| 546 | <img src="https://artificialanalysis.ai/img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam 30B (high) | 0.1566 | — | — | — |
| 547 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7-Flash (non-reasoning) | 0.1563 | 829.55 | 0.1610 | ❌ |
| 548 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-8B-A1B | 0.1561 | — | — | — |
| 549 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B (non-reasoning) | 0.1548 | — | — | — |
| 550 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-mini-2.0 | 0.1530 | — | — | — |
| 551 | <img src="https://artificialanalysis.ai/img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 2 (non-reasoning) | 0.1505 | — | — | — |
| 552 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.5 Haiku | 0.1492 | — | — | — |
| 553 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B 2507 (non-reasoning) | 0.1481 | — | — | — |
| 554 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.1 405B | 0.1478 | — | — | — |
| 555 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (non-reasoning) | 0.1470 | 357.86 | 0.0949 | ❌ |
| 556 | <img src="https://artificialanalysis.ai/img/logos/nanbeige.png" width="18" alt="Nanbeige" /> Nanbeige | Nanbeige4.1-3B | 0.1460 | — | — | — |
| 557 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Devstral Medium | 0.1459 | — | — | — |
| 558 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B | 0.1437 | — | — | — |
| 559 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 32B | 0.1430 | — | — | — |
| 560 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3.1 32B Instruct | 0.1415 | — | — | — |
| 561 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano (non-reasoning) | 0.1392 | 530.54 | 0.1234 | ❌ |
| 562 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen2.5 72B | 0.1379 | 548.20 | 0.1259 | ❌ |
| 563 | <img src="https://artificialanalysis.ai/img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | Exaone 4.0 1.2B | 0.1378 | — | — | — |
| 564 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Devstral Small (May) | 0.1377 | — | — | — |
| 565 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 4B | 0.1376 | — | — | — |
| 566 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B (non-reasoning) | 0.1364 | 373.80 | 0.0978 | ❌ |
| 567 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.3 70B | 0.1363 | 6,950.45 | 0.3896 | ❌ |
| 568 | <img src="https://artificialanalysis.ai/img/logos/cohere.svg" width="18" alt="Cohere" /> Cohere | Command A | 0.1360 | 8,105.88 | 0.4079 | ❌ |
| 569 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi Linear 48B A3B Instruct | 0.1345 | — | — | — |
| 570 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Super 49B v1.5 (non-reasoning) | 0.1335 | — | — | — |
| 571 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Large 2 (Nov) | 0.1333 | — | — | — |
| 572 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 nano | 0.1324 | 536.03 | 0.1242 | ❌ |
| 573 | <img src="https://artificialanalysis.ai/img/logos/reka.svg" width="18" alt="Reka AI" /> Reka AI | Reka Flash 3 | 0.1323 | 258.37 | 0.0750 | ❌ |
| 574 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6V (non-reasoning) | 0.1322 | 2,520.86 | 0.2733 | ❌ |
| 575 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 27B | 0.1314 | 0.00 | 0.0000 | ❌ |
| 576 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Devstral Small | 0.1303 | — | — | — |
| 577 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (minimal) | 0.1302 | 349.97 | 0.0935 | ❌ |
| 578 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 14B | 0.1279 | — | — | — |
| 579 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 32B (non-reasoning) | 0.1277 | 376.81 | 0.0984 | ❌ |
| 580 | <img src="https://artificialanalysis.ai/img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-1B | 0.1277 | — | — | — |
| 581 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.3 Nemotron Super 49B (non-reasoning) | 0.1270 | — | — | — |
| 582 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 2B | 0.1270 | — | — | — |
| 583 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o mini | 0.1269 | 1,209.01 | 0.1965 | ❌ |
| 584 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Pixtral Large | 0.1257 | — | — | — |
| 585 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5V (non-reasoning) | 0.1241 | 2,850.82 | 0.2870 | ❌ |
| 586 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.1 8B | 0.1225 | — | — | — |
| 587 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova Pro | 0.1215 | 4,844.63 | 0.3473 | ❌ |
| 588 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.1 Nemotron Nano 4B v1.1 | 0.1211 | — | — | — |
| 589 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 24B A2B | 0.1211 | — | — | — |
| 590 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 14B (non-reasoning) | 0.1206 | 250.03 | 0.0732 | ❌ |
| 591 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 E2B | 0.1195 | — | — | — |
| 592 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 12B | 0.1159 | 0.00 | 0.0000 | ❌ |
| 593 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 8B | 0.1147 | — | — | — |
| 594 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.1 3B | 0.1133 | — | — | — |
| 595 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.1 70B | 0.1123 | — | — | — |
| 596 | <img src="https://artificialanalysis.ai/img/logos/microsoft.svg" width="18" alt="Microsoft" /> Microsoft | Phi-4 | 0.1113 | 447.98 | 0.1106 | ❌ |
| 597 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.1 Nemotron 70B | 0.1102 | — | — | — |
| 598 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Llama 70B | 0.1096 | — | — | — |
| 599 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-1.2B-Thinking | 0.1086 | — | — | — |
| 600 | <img src="https://artificialanalysis.ai/img/logos/nousresearch.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 70B (non-reasoning) | 0.1080 | — | — | — |
| 601 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 12B v2 VL (non-reasoning) | 0.1079 | 516.65 | 0.1213 | ❌ |
| 602 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 7B | 0.1078 | — | — | — |
| 603 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Large 2 (Jul) | 0.1074 | — | — | — |
| 604 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H Small | 0.1066 | — | — | — |
| 605 | <img src="https://artificialanalysis.ai/img/logos/ai21.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba 1.7 Large | 0.1047 | — | — | — |
| 606 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-1.2B-Instruct | 0.1044 | — | — | — |
| 607 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 2B (non-reasoning) | 0.1042 | — | — | — |
| 608 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 E2B (non-reasoning) | 0.1030 | — | — | — |
| 609 | <img src="https://artificialanalysis.ai/img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-1B (non-reasoning) | 0.1028 | — | — | — |
| 610 | <img src="https://artificialanalysis.ai/img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | Exaone 4.0 1.2B (non-reasoning) | 0.1009 | — | — | — |
| 611 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 4B | 0.0996 | — | — | — |
| 612 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 1.7B | 0.0995 | — | — | — |
| 613 | <img src="https://artificialanalysis.ai/img/logos/ai21.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba Reasoning 3B | 0.0981 | — | — | — |
| 614 | <img src="https://artificialanalysis.ai/img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam M | 0.0980 | — | — | — |
| 615 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 8B (non-reasoning) | 0.0969 | — | — | — |
| 616 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Small 3 | 0.0954 | 66.06 | 0.0239 | ❌ |
| 617 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova Lite | 0.0928 | 325.96 | 0.0889 | ❌ |
| 618 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.1 8B | 0.0908 | 91.55 | 0.0320 | ❌ |
| 619 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3 Haiku | 0.0889 | — | — | — |
| 620 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova Micro | 0.0879 | 215.16 | 0.0652 | ❌ |
| 621 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3 70B | 0.0864 | 1,856.36 | 0.2403 | ❌ |
| 622 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 8B A1B | 0.0843 | — | — | — |
| 623 | <img src="https://artificialanalysis.ai/img/logos/ai21.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba 1.7 Mini | 0.0811 | — | — | — |
| 624 | <img src="https://artificialanalysis.ai/img/logos/microsoft.svg" width="18" alt="Microsoft" /> Microsoft | Phi-4 Mini | 0.0788 | 216.07 | 0.0654 | ❌ |
| 625 | <img src="https://artificialanalysis.ai/img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM-V 4.6 1.3B | 0.0785 | — | — | — |
| 626 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 Micro | 0.0771 | — | — | — |
| 627 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3n E4B | 0.0738 | — | — | — |
| 628 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 4B | 0.0730 | 0.00 | 0.0000 | ❌ |
| 629 | <img src="https://artificialanalysis.ai/img/logos/swiss-ai-initiative.png" width="18" alt="Swiss AI Initiative" /> Swiss AI Initiative | Apertus 70B Instruct | 0.0681 | — | — | — |
| 630 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 0.8B (non-reasoning) | 0.0679 | — | — | — |
| 631 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 3.3 8B (non-reasoning) | 0.0677 | — | — | — |
| 632 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H 1B | 0.0676 | — | — | — |
| 633 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Molmo2-8B | 0.0623 | — | — | — |
| 634 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 0.6B | 0.0601 | — | — | — |
| 635 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.2 11B (Vision) | 0.0585 | — | — | — |
| 636 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 0.8B | 0.0581 | — | — | — |
| 637 | <img src="https://artificialanalysis.ai/img/logos/swiss-ai-initiative.png" width="18" alt="Swiss AI Initiative" /> Swiss AI Initiative | Apertus 8B Instruct | 0.0571 | — | — | — |
| 638 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 1.7B (non-reasoning) | 0.0560 | — | — | — |
| 639 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.2 3B | 0.0546 | — | — | — |
| 640 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 1B | 0.0535 | — | — | — |
| 641 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 2.6B | 0.0529 | — | — | — |
| 642 | <img src="https://artificialanalysis.ai/img/logos/cohere.svg" width="18" alt="Cohere" /> Cohere | Tiny Aya Global | 0.0519 | 0.00 | 0.0000 | ❌ |
| 643 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | OLMo 2 32B | 0.0508 | — | — | — |
| 644 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-VL-1.6B | 0.0505 | — | — | — |
| 645 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 0.6B (non-reasoning) | 0.0486 | — | — | — |
| 646 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3 8B | 0.0478 | 167.19 | 0.0534 | ❌ |
| 647 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3n E2B | 0.0477 | — | — | — |
| 648 | <img src="https://artificialanalysis.ai/img/logos/microsoft.svg" width="18" alt="Microsoft" /> Microsoft | Phi-3 Mini | 0.0475 | — | — | — |
| 649 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.2 1B | 0.0449 | — | — | — |
| 650 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 1.2B | 0.0429 | — | — | — |
| 651 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 1B | 0.0390 | — | — | — |
| 652 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H 350M | 0.0385 | — | — | — |
| 653 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 350M | 0.0360 | — | — | — |
| 654 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | OLMo 2 7B | 0.0328 | — | — | — |
| 655 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral 7B | 0.0279 | 202.51 | 0.0622 | ❌ |
| 656 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 270M | 0.0275 | — | — | — |
| 657 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Llama 8B | 0.0170 | — | — | — |
| 658 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 1.5B | 0.0055 | — | — | — |
| 659 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Molmo 7B-D | 0.0000 | — | — | — |

## 品牌帕累托前沿连线（仅体现在图中）

以下 13 个品牌在图中拥有单独的帕累托连线（较窄宽度，品牌主题色，图层高于总体灰色连线）。表中数量为**入图顶点数**——品牌前沿上低于总体前沿第一级的顶点同样不入图（本表与图例一致）：

| 品牌 | 主题色 | 品牌前沿模型数（入图） |
|------|--------|--------------|
| <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | `#cc785c` | 11 |
| <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | `#1f1f1f` | 15 |
| <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | `#34A853` | 9 |
| <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | `#0089f4` | 4 |
| <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | `#ff6900` | 2 |
| <img src="https://artificialanalysis.ai/img/logos/sapiens.svg" width="18" alt="Sapiens AI" /> Sapiens AI | `#1521a9` | 1 |
| <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | `#1521a9` | 1 |
| <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | `#047AFE` | 3 |
| <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | `#ff7018` | 4 |
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
| `round_0a` | Raw Min-Max Mean | 2,685 / 3,134 | **85.67%** | 449 | 89.95% | 84.64% | 87.25% | 63.27% |
| `round_0b` | LOO Linear Calibration | 2,895 / 3,134 | **92.37%** | 239 | 93.25% | 92.75% | 92.89% | 61.22% |
| `round_1` | Stage-1 Unsupervised Monotone Calibration | 3,071 / 3,134 | **97.99%** | 63 | 95.06% | 98.89% | 98.77% | 89.80% |
| `round_2` | Regularized Benchmark Weight Optimization | 3,079 / 3,134 | **98.25%** | 55 | 95.39% | 99.03% | 99.26% | 91.84% |
| `round_3` | Joint Monotone Curve + Weight Optimization | 3,082 / 3,134 | **98.34%** | 52 | 96.05% | 98.89% | 99.51% | 93.88% |
| `round_4a` | Pseudo-Huber IRLS Robust Aggregation | 3,076 / 3,134 | **98.15%** | 58 | 95.39% | 98.79% | 99.75% | 91.84% |
| `round_4b` | Huber/IRLS + Margin-Annealed Refinement | 3,084 / 3,134 | **98.40%** | 50 | 96.54% | 98.84% | 99.75% | 91.84% |

### 留一厂商交叉验证（Leave-One-Vendor-Out Generalization）

Stage 1（单调 IRT 初始化）全程无监督（0 条约束标签）；针对每个主流厂商，Stage 2 严格剔除该厂商全部模型的约束后进行联合训练，再在被完全留出的该厂商约束集上评估泛化序一致性：

| 留出厂商 (Held-out Vendor) | 模型数 | 留出约束数 | R0 Raw | R0 LOO | R1 无监督 | R4 Held-out | 相对 R0 LOO | 相对 R1 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| OpenAI | 113 | 948 | 89.03% | 95.04% | 99.05% | **99.26%** | +4.22% | +0.21% |
| Google | 74 | 482 | 87.14% | 92.95% | 98.76% | **98.76%** | +5.81% | +0.00% |
| Anthropic | 65 | 410 | 90.73% | 96.59% | 99.27% | **99.02%** | +2.44% | -0.24% |
| Alibaba | 87 | 449 | 88.86% | 92.87% | 96.88% | **97.77%** | +4.90% | +0.89% |
| DeepSeek | 36 | 143 | 72.03% | 79.72% | 97.20% | **97.20%** | +17.48% | +0.00% |
| Meta | 27 | 46 | 84.78% | 91.30% | 95.65% | **95.65%** | +4.35% | +0.00% |
| SpaceXAI | 27 | 146 | 72.60% | 87.67% | 96.58% | **96.58%** | +8.90% | +0.00% |
| Z AI | 23 | 63 | 76.19% | 92.06% | 98.41% | **98.41%** | +6.35% | +0.00% |
| **TOTAL LOVO** | — | **2,687** | **86.75%** | **93.19%** | **98.36%** | **98.55%** | **+5.36%** | **+0.19%** |

### 学习到的基准权重分布（高信噪比增权 vs 噪声降权）

优化器在有界单纯形约束下自动识别高信噪比基准并抑制反单调/高噪声基准（如 `healthbench`、`omniscienceNonHallucination`、`enterpriseOps` 等），同时限制单项权重上限以保持评估多样性：

| 高权重基准 (Top Informative) | 权重 $w_b$ (占比) | 低权重/降权基准 (Downweighted) | 权重 $w_b$ (占比) |
| :--- | :---: | :--- | :---: |
| AA Intelligence Index (`intelligenceIndex`) | `2.1252` (5.59%) | AA-Omniscience Non-Hallucination (`omniscienceNonHallucination`) | `0.2776` (0.73%) |
| Humanity's Last Exam (`hle`) | `1.7198` (4.53%) | EnterpriseOps-Gym-AA (`enterpriseOps`) | `0.3174` (0.84%) |
| Terminal-Bench 2.1 (`terminalbenchV21`) | `1.6500` (4.34%) | HealthBench (`healthbench`) | `0.3324` (0.87%) |
| GDPval-AA Normalized (`gdpvalNormalized`) | `1.5530` (4.09%) | τ²-Bench Telecom (`tau2`) | `0.4088` (1.08%) |
| CritPt v2 Hard (`critptV2Hard`) | `1.4605` (3.84%) | Harvey LAB-AA (`harveyLab`) | `0.5454` (1.44%) |
| FrontierCode 2.0 (`frontiercode20`) | `1.4075` (3.70%) | MLCR Medical Long Context (`mlcr`) | `0.6369` (1.68%) |
| Terminal-Bench Hard (`terminalbenchHard`) | `1.4024` (3.69%) | AIME 2025 (`aime2025`) | `0.6591` (1.73%) |
| GPQA Diamond (`gpqa`) | `1.2548` (3.30%) | HealthBench Professional (`healthbenchProfessional`) | `0.6769` (1.78%) |


## 基准测试动态标定与 38 项权重汇总

> Leave-One-Out 线性标定作为参考字段（`composite_ability_calibrated`）同步保留，已完成 **24** 轮并行迭代收敛（容差阈值 $\Delta < 1e-05$）；主综合能力 `composite_ability` 由 `src/mapping.py` 的单调样条与学习权重计算得到。

| 基准测试项 | 英文标识 | 参测模型数 | 学习权重 $w_b$ | 权重占比 | LOO 下界 | LOO 上界 | LOO 跨度 |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| AA Intelligence Index | `intelligenceIndex` | 157 | `2.1252` | 5.59% | `0.0868` | `1.0000` | `0.9132` |
| GPQA Diamond | `gpqa` | 543 | `1.2548` | 3.30% | `0.0000` | `0.9107` | `0.9107` |
| Humanity's Last Exam | `hle` | 619 | `1.7198` | 4.53% | `0.0000` | `1.0000` | `1.0000` |
| HLE Diamond | `hleDiamond` | 197 | `1.1980` | 3.15% | `0.0855` | `1.0000` | `0.9145` |
| CritPt Physics | `critpt` | 599 | `0.8405` | 2.21% | `0.0000` | `1.0000` | `1.0000` |
| CritPt v2 Hard | `critptV2Hard` | 160 | `1.4605` | 3.84% | `0.0876` | `1.0000` | `0.9124` |
| AIME 2025 | `aime2025` | 268 | `0.6591` | 1.73% | `0.0000` | `0.7182` | `0.7182` |
| SciCode Coding | `scicode` | 253 | `1.1070` | 2.91% | `0.0876` | `1.0000` | `0.9124` |
| LiveCodeBench | `livecodebench` | 278 | `1.1359` | 2.99% | `0.0000` | `0.7181` | `0.7181` |
| FrontierCode 1.1 | `frontiercode` | 83 | `0.8894` | 2.34% | `0.1349` | `1.0000` | `0.8651` |
| FrontierCode 2.0 | `frontiercode20` | 159 | `1.4075` | 3.70% | `0.0876` | `1.0000` | `0.9124` |
| Terminal-Bench Hard | `terminalbenchHard` | 432 | `1.4024` | 3.69% | `0.0000` | `0.8436` | `0.8436` |
| Terminal-Bench 2.1 | `terminalbenchV21` | 243 | `1.6500` | 4.34% | `0.0621` | `0.9104` | `0.8483` |
| Terminal-Bench 4.0 | `terminalbenchV40` | 282 | `0.9020` | 2.37% | `0.0872` | `1.0000` | `0.9128` |
| Terminal-Bench Science | `terminalbenchScience` | 170 | `0.7438` | 1.96% | `0.0874` | `1.0000` | `0.9126` |
| τ²-Bench Telecom | `tau2` | 439 | `0.4088` | 1.08% | `0.0000` | `0.8512` | `0.8512` |
| τ³-Bench Banking | `tauBanking` | 210 | `0.9620` | 2.53% | `0.0645` | `0.9153` | `0.8507` |
| AutomationBench-AA | `automationbench` | 285 | `1.1999` | 3.16% | `0.0875` | `1.0000` | `0.9125` |
| AA-Briefcase v1.1 | `briefcase` | 292 | `1.1990` | 3.16% | `0.0876` | `1.0000` | `0.9124` |
| GDPval-AA Normalized | `gdpvalNormalized` | 319 | `1.5530` | 4.09% | `0.0626` | `1.0000` | `0.9374` |
| GDP.pdf | `gdpPdf` | 285 | `1.2024` | 3.16% | `0.0854` | `1.0000` | `0.9146` |
| AA-LCR Long Context | `lcr` | 597 | `0.8943` | 2.35% | `0.0000` | `1.0000` | `1.0000` |
| MLCR Medical Long Context | `mlcr` | 203 | `0.6369` | 1.68% | `0.1255` | `1.0000` | `0.8745` |
| MMMU Pro | `mmmuPro` | 306 | `1.1493` | 3.02% | `0.0127` | `0.9417` | `0.9290` |
| Code2Video-AA | `code2video` | 29 | `0.9692` | 2.55% | `0.4242` | `0.9119` | `0.4877` |
| AA-3D | `aa3d` | 27 | `1.1357` | 2.99% | `0.4249` | `1.0000` | `0.5751` |
| AA Omniscience Index | `omniscience` | 171 | `1.0347` | 2.72% | `0.0821` | `1.0000` | `0.9179` |
| AA-Omniscience Accuracy | `omniscienceAccuracy` | 171 | `0.8164` | 2.15% | `0.0873` | `1.0000` | `0.9127` |
| AA-Omniscience Non-Hallucination | `omniscienceNonHallucination` | 171 | `0.2776` | 0.73% | `0.0729` | `1.0000` | `0.9271` |
| IFBench Instruction Following | `ifbench` | 449 | `0.8495` | 2.24% | `0.0000` | `0.8566` | `0.8566` |
| AA Analyst Agent | `analystAgent` | 64 | `0.9024` | 2.37% | `0.2533` | `0.9417` | `0.6885` |
| APEX-Agents-AA | `apexAgents` | 34 | `0.9348` | 2.46% | `0.3008` | `0.8078` | `0.5069` |
| EnterpriseOps-Gym-AA | `enterpriseOps` | 63 | `0.3174` | 0.84% | `0.2682` | `0.9667` | `0.6985` |
| ITBench-SRE | `itbenchSre` | 45 | `0.6894` | 1.81% | `0.1560` | `0.9217` | `0.7656` |
| Harvey LAB-AA | `harveyLab` | 44 | `0.5454` | 1.44% | `0.4371` | `1.0000` | `0.5629` |
| HealthBench | `healthbench` | 29 | `0.3324` | 0.87% | `0.6408` | `1.0000` | `0.3592` |
| HealthBench Professional | `healthbenchProfessional` | 19 | `0.6769` | 1.78% | `0.6396` | `1.0000` | `0.3604` |
| VIALS-AA / MKA | `vials` | 28 | `0.8167` | 2.15% | `0.4906` | `1.0000` | `0.5094` |


## 评分方法

1. **38项全域评估指标**各自线性归一化到 [0,1]
   （AA Intelligence Index、GPQA Diamond、Humanity's Last Exam、HLE Diamond、CritPt Physics、CritPt v2 Hard、AIME 2025、SciCode Coding、LiveCodeBench、FrontierCode 1.1、FrontierCode 2.0、Terminal-Bench Hard、Terminal-Bench 2.1、Terminal-Bench 4.0、Terminal-Bench Science、τ²-Bench Telecom、τ³-Bench Banking、AutomationBench-AA、AA-Briefcase v1.1、GDPval-AA Normalized、GDP.pdf、AA-LCR Long Context、MLCR Medical Long Context、MMMU Pro、Code2Video-AA、AA-3D、AA Omniscience Index、AA-Omniscience Accuracy、AA-Omniscience Non-Hallucination、IFBench Instruction Following、AA Analyst Agent、APEX-Agents-AA、EnterpriseOps-Gym-AA、ITBench-SRE、Harvey LAB-AA、HealthBench、HealthBench Professional、VIALS-AA / MKA）
   > 全域基准升级：收录全部 38 项基准测试，涵盖通用推理 (AA Intelligence Index, HLE, HLE Diamond, GPQA Diamond)、数理逻辑 (CritPt, CritPt v2 Hard, AIME 2025)、代码编程 (LiveCodeBench, SciCode, FrontierCode 1.1/2.0)、Agent 智能体 (Terminal-Bench 系列, τ-Bench 系列, AutomationBench, Briefcase, ITBench-SRE, Harvey LAB, HealthBench)、多模态 (MMMU Pro, Code2Video, AA-3D, VIALS)、长上下文 (AA-LCR, MLCR, GDP.pdf) 及事实性 (Omniscience 系列, IFBench) 等核心维度。
2. **综合能力值（零标签泄漏单调映射）**：通过 `src/mapping.py` (`MonotoneBenchmarkMapper`) 对每项已测基准分数经严格单调分段曲线 $g_b(x)$ 校准后，按学习到的稳健权重 $w_b$ 执行 Pseudo-Huber IRLS M-估计聚合；原始等权平均 (`composite_ability_raw_uncalibrated`) 与留一线性标定 (`composite_ability_calibrated`) 同步保留在 `output/analysis_results.json` 中供对照。
3. **综合能力再归一化**：线性映射到 [0,1]，性能最好的模型 = 1，最差的模型 = 0
4. **Pareto前沿** = 不被任何其他模型支配的模型（综合能力 ≥ 且成本 ≤，且至少一项严格更优；成本为 0 的免费模型同样参与——横轴左端恒为 0，免费模型是合法前沿候选）
5. **模型范围** = Status: All（含已弃用模型；缺少足够评估数据者不参与排名）
6. **图表纵轴基线（V17）**：图表的 y = 0 取总体帕累托前沿的第一级（最低能力；本例 y0 = 0.5660，即前沿左端点 K2 Horizon 375B A23B）；综合能力低于该级的模型不出现在图表中（表格不受影响）。图中纵坐标 chart_y = (能力 - y0)/(1 - y0)，因此前沿左端点恰好落在 (0, 0)、最优模型恰好为 y = 1。该过滤在横轴映射构建之前完成


## 模型系列层级与单调性评分引擎（Model Hierarchy & Monotonic Scoring Engine）

为解决多基准评估中由于各模型参测项不齐、评测噪声以及偶然波动导致的反直觉能力倒挂（例如同一系列同版本高阶模型得分低于低阶模型、同一系列同等级新版本低于旧版本、同一模型高思考程度低于低思考程度、同代更新快照后出版本低于先出版本），系统在 `src/hierarchy.py` 中实现了**分厂商系列层级网格（Vendor Series Hierarchy Grids）**并与 `src/mapping.py` 的纯特征单调映射引擎协同工作：

### 1. 厂商与系列隔离（Series Isolation）
系统维护了覆盖全部主流与新兴厂商的 **99 个系列层级网格**（保存在 `output/model_hierarchy/` 目录下的 CSV 文件中），每个系列维护二维网格：
- **行（Tiers）**：性能层级（如 Tier 1 Flagship / Large、Tier 2 Medium / MoE、Tier 3 Small / Fast、Tier 4 Compact / Nano）
- **列（Versions）**：架构代际与版本演进（从旧到新按时间列排布）
- **严格系列隔离**：不同系列（例如 OpenAI 的 `GPT` 系列与 `o` 推理系列、Google 的 `Gemini` 与 `Gemma` 开源系列、Meta 的 `Llama` 与 `Muse` 系列）物理隔离，绝不产生跨系列强行绑定的单调性约束。

### 2. 四大严格单调序规则（Strict Monotonic Ordering Rules）
在系列网格与模型元数据基础上，自动生成 **3,134 条**有向无环约束（DAG，$S(u) \ge S(v)$：Rule 1 = 607，Rule 2 = 2,070，Rule 3 = 408，Rule 4 = 49）：
- **Rule 1（同系列同版本，高等级 $\ge$ 低等级）**：同一系列、同一版本列内，高行 Tier 模型能力必须大于等于低行 Tier 模型的所有快照与变体（支持思考程度对齐匹配）。
- **Rule 2（同系列同等级，新版本 $\ge$ 旧版本）**：同一系列、同一等级行内，新版本列模型能力必须大于等于旧版本列模型。
- **Rule 3（同模型基座，高思考程度 $\ge$ 低思考程度）**：同一基座模型，高思考算力档位能力必须大于等于低思考算力档位（$\text{max} > \text{xhigh} > \text{high} > \text{medium} > \text{low} > \text{minimal} > \text{non-reasoning}$）。
- **Rule 4（同模型主干，新日期快照 $\ge$ 旧日期快照）**：同一模型主干内，后发布的日期快照能力大于等于先发布的快照（如 GPT-4o Nov $\ge$ Aug $\ge$ May，Claude 3.5 Sonnet Oct $\ge$ June，DeepSeek V4 Pro 0813 $\ge$ 0424）。

### 3. 零标签泄漏纯特征映射评估（Zero-Clamping Pure Benchmark Mapping）
- **纯函数无硬夹逼原则**：主评分完全由 `MonotoneBenchmarkMapper.score_model(parsed_metrics)` 根据模型基准得分直接计算，**不在推理时读取模型身份，也不使用 Dykstra 等保投影对模型分数进行标签硬夹逼（Zero Label Clamping）**；
- **实测序一致性**：在 724 个参测模型、3,134 条清洁约束条件下，纯特征映射直接达成 **98.40% 序一致性（满足 3,084/3,134，50 项真实数据级倒挂）**；可选 Dykstra 等保投影仅作为离线理论诊断上界保留于诊断报告。详见 [层级诊断报告](output/model_hierarchy/hierarchy_score_report.md) 与 [层级分析结果](output/hierarchy_analysis_results.json)。

### 4. 人工校验与 CSV 双向工作流（Calibration & Diff Workflow）
全部 99 个系列层级网格均以易于阅读与编辑的标准 2D CSV 存储于 `output/model_hierarchy/`。
- **导出与查看**：运行 `python src/hierarchy.py` 会导出全部单独 CSV 及汇总表 `all_vendors_hierarchy.csv`；
- **自定义层级微调**：用户可直接用 Excel 或文本编辑器修改任意系列 CSV（例如调整某些新模型的归属代际或层级）；
- **差异审查与校验**：运行 `python src/hierarchy.py --diff <SeriesName>` 或 `--diff all`，系统会自动将本地修改与默认预置层级进行三向比对，报告所有变更并校验单调性。


## 横轴映射（对数映射，真零点，V21）与分布分析

横轴（单请求成本）为 **Y = A·ln(B·c+C)+D 对数映射**（B = 1；A、D 由端点解出；C = 309.14，r = B/C = 0.00323479 经网格搜索确定）：

```
x = 0                            当 c = 0（免费模型，真零点）
x = A·ln(c+C)+D                  当 c > 0（B = 1 并入；A、D 由端点解出）
```

其中 C = 309.14（r = B/C = 0.00323479），拟合集为 11 品牌前沿入图正成本模型（综合能力 ≥ 前沿第一级）的成本分布，目标为组内名次分位数（最小二乘误差 mse = 0.010753，最大偏离 0.2087）。该映射在 **y 基线过滤之后**构建（V17：先以帕累托前沿第一级为 y = 0、剔除低性能模型，再对入图模型建映射）。

**该映射保证：**

- **函数端点严格钉死**：c = 0 → x = 0；最大成本 → x = 1——函数经过 (0,0) 与 (1,1)；
- 各数量级区间的入图模型数：1–10: 0，10–100: 0，100–1k: 4，1k–10k: 38，10k–100k: 98，100k–1M: 16，1M–1.019M: 1
- **同倍率区间宽度相近**（对数轴性质）：1k→10k 与 100k→1M 同为 10 倍率，宽度相近（前者 38 个模型、后者 16 个）；与 V17 分位数映射不同，本图不追求均匀密度——密度不等如实显示；
- **左端恒为 0**（c = 0；1 个免费模型位于最左缘）
- 前沿最低正成本 552.73 → x = 0.1266（真实对数位置，不再钉 0；x = 0 恒为 c = 0 免费模型）；前沿最大成本 1,018,638 → x = 1.0000（= 1；高于前沿最大成本的模型不入图，仅表格保留）
- 中位数位置 0.541（≈ 0.5 居中）；左右两半模型数：左 66 / 右 92
- 横轴十分位模型数：1，8，8，17，32，39，32，11，7，3（对数映射下各十分位模型数自然不等）
- **10^x 数量级指示**（位置 = x(10^x)）：10^0 → 0.000，10^1 → 0.004，10^2 → 0.035，10^3 → 0.178，10^4 → 0.433，10^5 → 0.714，10^6 → 0.998

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
| CacheHitRate | [AA Coding Agents](https://artificialanalysis.ai/agents/coding-agents) | 全部模型-Agent搭配的 `cacheHitRate` 求平均（41 个有效值，均值 = 0.9371），对所有模型统一使用 |
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
**模型总数（Status: All）**: 659 个参与排名（共抓取 764 个模型，另有模型因评估数据不足未列入；总体帕累托前沿 20 个；图表入图 158 个——综合能力 ≥ 前沿第一级）  

**技术架构与更新流程：**
1. **高速数据抓取 (`src/scrape.py`)**：解析 Artificial Analysis 的 Next.js RSC 动态清单（Manifest），通过 AES-GCM 快速解密全量模型数据集，解压缩 GZip 流并解析嵌套的 38 项基准维度分数与发布时间；
2. **缓存命中率抓取 (`src/cache_hit_rate.py`)**：通过 Playwright 抓取 Coding Agents 页面的全局均值作为成本公式参数；
3. **单调基准映射引擎 (`src/mapping.py`)**：在无模型身份泄漏、无 Dykstra 标签夹逼的前提下，通过 38 项严格单调分段样条 $g_b$、有界权重 $w_b$ 与 Pseudo-Huber IRLS 聚合拟合能力映射并执行 LOVO 交叉验证；
4. **模型层级约束与诊断 (`src/hierarchy.py`)**：基于 99 个系列层级网格（Tiers x Versions）生成 3,134 条 DAG 单调约束，记录纯映射序一致性（98.40%）并导出诊断报告；
5. **帕累托与图表分析 (`src/analyze.py`)**：基于 `src/mapping.py` 映射的综合能力执行成本计算、真零点对数坐标映射与多品牌前沿图表绘制；
6. **自动化 GitHub Actions (`.github/workflows/update-leaderboard.yml`)**：每日定时及手动触发运行抓取、层级与映射计算、单元测试验证与看板自动更新。


## 图表说明（黑底）

（V17 起本说明置于文末，图表之后直接跟随模型表格。）

图表说明：**灰色实线** = 总体帕累托前沿；**彩色细线** = 选定品牌的单独帕累托前沿（共 13 个品牌，（品牌主题色，图层高于总体连线；暗色品牌元素带窄白边；顶点按（横轴位置、能力升序）连接，等成本点自下而上）；品牌前沿模型圆点同样使用品牌颜色。模型名称/思考程度标注优先骑在连线之上（点的左/右两侧皆可，同一条线段可容纳两个标签——各贴各的点；文字与连线平行、中轴线重合，连线仅在文字两侧绘制）；骑线位被其他标签占据时自动「让位」——占用者挪到自己的另一个骑线位，双方都保持骑线；实在骑不上线时按四级优先依次退让（V16）：离点最近位置的上方/下方平行偏移 → 点的两条连线延长线上就近 → 两连线夹角扇区内就近。标签规则（V13/V15）：品牌前沿模型共享的前导块按「最长有效切点」剔除 —— 切点止于分界符，或止于字母且其后紧跟数字（如 Claude Opus 5 → Opus 5、GPT-5.6 Sol → 5.6 Sol、Kimi K2.6 → 2.6、Qwen3.8 Max → 3.8 Max、MiMo-V2.5 → 2.5、MiniMax-M2.1 → 2.1）；(non-reasoning) 简写为 (non)；同一模型在品牌连线上相邻出现 2 次以上时仅性能最低者保留全名、相邻较高者只标思考程度，不相邻的重复出现保留全名（每次重新计算）；标签位置与序列同向（V15）——品牌前沿上越靠右上的模型，其标签重心必须同时更靠右且更靠上（两分量都 >= 0，至少是 (0,0)，仅其一非负不算合格；初始放置违反时自动就近重摆，单标签无解（被前后邻居夹死）时按窗口级联重排整体挪动，均不产生新的重叠）。纵轴 y = 0 = 总体帕累托前沿第一级（y0 = 0.5660，前沿左端点 K2 Horizon 375B A23B 恰为 (0,0)），能力低于该级的 490 个模型、缺少成本数据的 11 个模型与成本高于品牌前沿最大值的模型不出现在图中；横轴为对数映射（见上文「横轴映射」节），10^x 数量级指示位于 x(10^x)，同一倍率区间的宽度相近（对数轴性质；本图不追求均匀密度）。
