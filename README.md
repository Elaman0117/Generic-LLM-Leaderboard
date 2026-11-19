# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

## 全部模型（综合能力从高到低，最优 = 1，最差 = 0）

共收录 **Status: All**（含已弃用）的全部模型；按重新归一化后的综合能力排序。「帕累托」列：✅ = 总体帕累托前沿模型，❌ = 被支配，— = 无成本数据无法判定。图表纵轴以总体帕累托前沿第一级（y0 = 0.4575，即前沿左端点 K2 Horizon 375B A23B）为 0：综合能力 ≥ 该级且有成本数据的 259 个模型入图，325 个能力低于第一级、74 个缺少成本数据的模型不出现在图中，成本高于品牌前沿最大值的模型同样不入图（本表不受影响，仍完整列出全部模型）。

| # | 品牌 | 模型 | 综合能力 | 单请求成本 | 横轴位置 | 帕累托 |
|---|------|------|---------|-----------|-----------|------|
| 1 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.2 (max) | 1.0000 | 1,042,888.19 | 1.0000 | ✅ |
| 2 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Neon (high) | 0.9740 | 72,639.08 | 0.7097 | ✅ |
| 3 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Neon (xhigh) | 0.9717 | 103,909.13 | 0.7487 | ❌ |
| 4 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Carbon (medium) | 0.9594 | 25,531.00 | 0.5961 | ✅ |
| 5 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.2 (xhigh) | 0.9522 | 285,182.54 | 0.8587 | ❌ |
| 6 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Carbon (high) | 0.9481 | 50,693.95 | 0.6706 | ❌ |
| 7 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.2 (high) | 0.9387 | 133,037.31 | 0.7756 | ❌ |
| 8 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (xhigh) | 0.9278 | 225,115.72 | 0.8329 | ❌ |
| 9 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (max) | 0.9162 | 448,479.02 | 0.9080 | ❌ |
| 10 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (xhigh) | 0.9134 | 153,923.53 | 0.7915 | ❌ |
| 11 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.2 Astra (max) | 0.9132 | 425,361.18 | 0.9023 | ❌ |
| 12 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (high) | 0.9088 | 130,173.32 | 0.7733 | ❌ |
| 13 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.2 (medium) | 0.9006 | 72,937.48 | 0.7102 | ❌ |
| 14 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Neon (medium) | 0.8970 | 41,224.21 | 0.6481 | ❌ |
| 15 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5 | 0.8952 | 307,909.45 | 0.8670 | ❌ |
| 16 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (max) | 0.8941 | 857,516.35 | 0.9787 | ❌ |
| 17 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (max) | 0.8935 | 86,255.99 | 0.7284 | ❌ |
| 18 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (medium) | 0.8817 | 55,973.40 | 0.6814 | ❌ |
| 19 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.2 Astra (xhigh) | 0.8810 | 168,819.39 | 0.8016 | ❌ |
| 20 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (max) | 0.8787 | 430,656.60 | 0.9036 | ❌ |
| 21 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (xhigh) | 0.8773 | 39,399.12 | 0.6432 | ❌ |
| 22 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (xhigh) | 0.8769 | 49,066.85 | 0.6671 | ❌ |
| 23 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.2 (low) | 0.8732 | 61,170.98 | 0.6910 | ❌ |
| 24 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (max) | 0.8721 | 76,601.08 | 0.7155 | ❌ |
| 25 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Carbon (low) | 0.8701 | 12,283.16 | 0.5168 | ✅ |
| 26 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (xhigh) | 0.8689 | 115,353.16 | 0.7601 | ❌ |
| 27 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (xhigh) | 0.8671 | 103,907.52 | 0.7487 | ❌ |
| 28 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.2 Astra (high) | 0.8648 | 85,973.32 | 0.7281 | ❌ |
| 29 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Hydrogen (xhigh) | 0.8590 | 64,718.05 | 0.6972 | ❌ |
| 30 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (xhigh) | 0.8582 | 64,609.37 | 0.6970 | ❌ |
| 31 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Hydrogen (high) | 0.8545 | 28,979.95 | 0.6098 | ❌ |
| 32 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (medium) | 0.8531 | — | — | — |
| 33 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (high) | 0.8526 | 20,595.17 | 0.5728 | ❌ |
| 34 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (xhigh) | 0.8514 | 312,222.33 | 0.8686 | ❌ |
| 35 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (high) | 0.8509 | 34,619.69 | 0.6291 | ❌ |
| 36 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (high) | 0.8499 | 60,872.40 | 0.6905 | ❌ |
| 37 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3 Pro Preview (high) | 0.8495 | — | — | — |
| 38 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (high) | 0.8495 | 46,921.96 | 0.6622 | ❌ |
| 39 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Wonder Full (max) | 0.8449 | — | — | — |
| 40 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Terra (max) | 0.8365 | 53,255.40 | 0.6760 | ❌ |
| 41 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.2 Sol (max) | 0.8358 | 66,632.98 | 0.7003 | ❌ |
| 42 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.3 Codex (xhigh) | 0.8292 | 57,621.70 | 0.6845 | ❌ |
| 43 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Argon (medium) | 0.8281 | 15,209.35 | 0.5399 | ❌ |
| 44 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (xhigh) | 0.8254 | 126,113.08 | 0.7698 | ❌ |
| 45 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (max) | 0.8233 | 790,475.23 | 0.9698 | ❌ |
| 46 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (medium) | 0.8213 | 27,531.93 | 0.6043 | ❌ |
| 47 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.7 (max) | 0.8201 | 60,193.41 | 0.6893 | ❌ |
| 48 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (medium) | 0.8193 | 42,177.84 | 0.6506 | ❌ |
| 49 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (high) | 0.8186 | 78,380.76 | 0.7180 | ❌ |
| 50 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3.1 Pro | 0.8162 | 55,683.00 | 0.6808 | ❌ |
| 51 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (medium) | 0.8103 | 30,284.91 | 0.6146 | ❌ |
| 52 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (medium) | 0.8103 | 9,997.17 | 0.4946 | ✅ |
| 53 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (max) | 0.8068 | 97,922.11 | 0.7423 | ❌ |
| 54 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (low) | 0.8067 | 49,929.48 | 0.6689 | ❌ |
| 55 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.2 Astra (medium) | 0.8041 | 36,952.12 | 0.6362 | ❌ |
| 56 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (high) | 0.8038 | 52,848.27 | 0.6751 | ❌ |
| 57 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 Max | 0.8028 | 42,211.31 | 0.6507 | ❌ |
| 58 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (xhigh) | 0.7983 | 48,056.43 | 0.6648 | ❌ |
| 59 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 Codex (xhigh) | 0.7934 | 61,696.52 | 0.6920 | ❌ |
| 60 | <img src="https://artificialanalysis.ai/img/logos/sapiens.svg" width="18" alt="Sapiens AI" /> Sapiens AI | Agnes 2.5 Pro Beta | 0.7931 | — | — | — |
| 61 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.8 (max) | 0.7918 | 80,255.70 | 0.7206 | ❌ |
| 62 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (medium) | 0.7882 | 22,398.77 | 0.5819 | ❌ |
| 63 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.5 | 0.7877 | 39,806.52 | 0.6443 | ❌ |
| 64 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 Codex (high) | 0.7864 | 24,175.39 | 0.5901 | ❌ |
| 65 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Terra (xhigh) | 0.7811 | 13,624.51 | 0.5280 | ❌ |
| 66 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (medium) | 0.7810 | 15,704.33 | 0.5434 | ❌ |
| 67 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.2 Sol (xhigh) | 0.7791 | 30,294.65 | 0.6146 | ❌ |
| 68 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3 Flash | 0.7789 | 5,310.74 | 0.4266 | ✅ |
| 69 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (low) | 0.7750 | — | — | — |
| 70 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (xhigh) | 0.7746 | 22,998.05 | 0.5847 | ❌ |
| 71 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (high) | 0.7735 | — | — | — |
| 72 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (medium) | 0.7704 | 15,666.76 | 0.5431 | ❌ |
| 73 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (medium) | 0.7702 | 57,008.22 | 0.6834 | ❌ |
| 74 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 v2 | 0.7700 | 7,156.45 | 0.4586 | ❌ |
| 75 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 Codex (high) | 0.7641 | 22,522.92 | 0.5825 | ❌ |
| 76 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark | 0.7630 | — | — | — |
| 77 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Wonder (max) | 0.7605 | 61,878.10 | 0.6923 | ❌ |
| 78 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.2 Sol (high) | 0.7603 | 15,584.05 | 0.5425 | ❌ |
| 79 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 Max Preview | 0.7593 | — | — | — |
| 80 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.6 (max) | 0.7583 | 44,047.44 | 0.6553 | ❌ |
| 81 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Neon (low) | 0.7581 | 31,078.88 | 0.6174 | ❌ |
| 82 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (high) | 0.7576 | 17,670.59 | 0.5562 | ❌ |
| 83 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (medium) | 0.7574 | 35,166.61 | 0.6308 | ❌ |
| 84 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen4 Max | 0.7539 | 39,091.20 | 0.6423 | ❌ |
| 85 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Terra (high) | 0.7530 | 7,260.17 | 0.4601 | ❌ |
| 86 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (max) | 0.7530 | 51,167.68 | 0.6716 | ❌ |
| 87 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Argon (high) | 0.7525 | 38,043.37 | 0.6394 | ❌ |
| 88 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (low) | 0.7517 | 27,162.88 | 0.6028 | ❌ |
| 89 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (medium) | 0.7481 | 6,039.69 | 0.4404 | ❌ |
| 90 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (high) | 0.7439 | 14,397.37 | 0.5340 | ❌ |
| 91 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Hydrogen (medium) | 0.7439 | 21,402.44 | 0.5769 | ❌ |
| 92 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 Thinking | 0.7423 | 13,562.42 | 0.5275 | ❌ |
| 93 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (medium) | 0.7417 | 25,361.82 | 0.5953 | ❌ |
| 94 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash | 0.7401 | — | — | — |
| 95 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.3 (xhigh) | 0.7401 | 14,403.10 | 0.5340 | ❌ |
| 96 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (high) | 0.7398 | — | — | — |
| 97 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 (high) | 0.7383 | 43,785.59 | 0.6547 | ❌ |
| 98 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (low) | 0.7379 | 47,294.89 | 0.6631 | ❌ |
| 99 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (high) | 0.7376 | 22,301.83 | 0.5814 | ❌ |
| 100 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.5 (high) | 0.7342 | 10,339.07 | 0.4982 | ❌ |
| 101 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (low) | 0.7325 | 14,524.30 | 0.5349 | ❌ |
| 102 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (max) | 0.7317 | 77,865.89 | 0.7173 | ❌ |
| 103 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o3 | 0.7295 | 15,432.09 | 0.5415 | ❌ |
| 104 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 2.4T A95B | 0.7294 | 33,916.01 | 0.6269 | ❌ |
| 105 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.2 Sol (medium) | 0.7277 | 9,768.96 | 0.4921 | ❌ |
| 106 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (low) | 0.7262 | 26,759.59 | 0.6012 | ❌ |
| 107 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (low) | 0.7247 | 23,697.75 | 0.5880 | ❌ |
| 108 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 Plus | 0.7233 | 6,861.98 | 0.4541 | ❌ |
| 109 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Wonder (high) | 0.7162 | 39,380.88 | 0.6431 | ❌ |
| 110 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Terra (medium) | 0.7124 | 5,284.18 | 0.4261 | ✅ |
| 111 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 | 0.7111 | 26,480.57 | 0.6000 | ❌ |
| 112 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.3 (max) | 0.7108 | 18,618.20 | 0.5618 | ❌ |
| 113 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash 0731 (max) | 0.7106 | 1,284.39 | 0.2785 | ✅ |
| 114 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 | 0.7091 | — | — | — |
| 115 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 27B | 0.7074 | 5,204.39 | 0.4245 | ❌ |
| 116 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.2 (xhigh) | 0.7025 | 11,375.35 | 0.5085 | ❌ |
| 117 | <img src="https://artificialanalysis.ai/img/logos/motif.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif 3 (Beta) | 0.7024 | — | — | — |
| 118 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (high) | 0.7018 | 20,421.81 | 0.5718 | ❌ |
| 119 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (xhigh) | 0.7017 | 26,296.41 | 0.5993 | ❌ |
| 120 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (xhigh) | 0.7005 | 3,501.25 | 0.3824 | ❌ |
| 121 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash Vision (max) | 0.6974 | 10,041.84 | 0.4951 | ❌ |
| 122 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (medium) | 0.6974 | — | — | — |
| 123 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.7 (non-reasoning, high) | 0.6972 | 23,598.69 | 0.5875 | ❌ |
| 124 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 Max (0902) | 0.6957 | 39,407.05 | 0.6432 | ❌ |
| 125 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (low) | 0.6952 | 9,023.16 | 0.4835 | ❌ |
| 126 | <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.1 | 0.6932 | — | — | — |
| 127 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3 (max) | 0.6911 | 37,381.23 | 0.6375 | ❌ |
| 128 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.1 Fast | 0.6909 | — | — | — |
| 129 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Pro | 0.6898 | — | — | — |
| 130 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.2 Astra (low) | 0.6898 | 35,650.74 | 0.6323 | ❌ |
| 131 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7 | 0.6886 | 7,023.41 | 0.4566 | ❌ |
| 132 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (max) | 0.6870 | 145,897.56 | 0.7857 | ❌ |
| 133 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3 Pro Preview (low) | 0.6843 | — | — | — |
| 134 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 Codex mini (high) | 0.6840 | 4,980.54 | 0.4198 | ❌ |
| 135 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5-Turbo | 0.6827 | — | — | — |
| 136 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Omni-0327 | 0.6801 | — | — | — |
| 137 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.1 Flash | 0.6783 | 4,533.91 | 0.4098 | ❌ |
| 138 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (low) | 0.6766 | 5,369.51 | 0.4278 | ❌ |
| 139 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (high) | 0.6749 | 63,609.26 | 0.6953 | ❌ |
| 140 | <img src="https://artificialanalysis.ai/img/logos/thinking-machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling 2 Small | 0.6739 | 5,319.96 | 0.4268 | ❌ |
| 141 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Opus | 0.6739 | — | — | — |
| 142 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (low) | 0.6724 | 12,867.64 | 0.5218 | ❌ |
| 143 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (medium) | 0.6714 | 3,398.58 | 0.3792 | ❌ |
| 144 | <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.5 | 0.6686 | 2,184.63 | 0.3329 | ❌ |
| 145 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.7 (high) | 0.6682 | 24,762.75 | 0.5927 | ❌ |
| 146 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (low) | 0.6670 | 25,809.11 | 0.5972 | ❌ |
| 147 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.6 Flash (high) | 0.6661 | 12,027.06 | 0.5145 | ❌ |
| 148 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (xhigh) | 0.6646 | 22,311.07 | 0.5814 | ❌ |
| 149 | <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2 | 0.6633 | 1,526.48 | 0.2960 | ❌ |
| 150 | <img src="https://artificialanalysis.ai/img/logos/tencent-hy.svg" width="18" alt="Tencent" /> Tencent | Hy3-preview | 0.6622 | — | — | — |
| 151 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (medium) | 0.6616 | 9,628.24 | 0.4905 | ❌ |
| 152 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash (Feb 2026) | 0.6615 | — | — | — |
| 153 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 | 0.6612 | 866.33 | 0.2396 | ✅ |
| 154 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.2 (max) | 0.6597 | 14,628.60 | 0.5357 | ❌ |
| 155 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Speciale | 0.6591 | — | — | — |
| 156 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5 | 0.6573 | 12,081.03 | 0.5150 | ❌ |
| 157 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (high) | 0.6572 | 1,905.98 | 0.3188 | ❌ |
| 158 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok Build 0.1 0616 | 0.6539 | 6,397.41 | 0.4466 | ❌ |
| 159 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Haiku 5.5 (max) | 0.6529 | 23,706.47 | 0.5880 | ❌ |
| 160 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM 5V Turbo | 0.6498 | — | — | — |
| 161 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (high) | 0.6496 | 16,078.94 | 0.5459 | ❌ |
| 162 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (max) | 0.6480 | 13,259.22 | 0.5251 | ❌ |
| 163 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Omni | 0.6462 | — | — | — |
| 164 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max Thinking | 0.6444 | — | — | — |
| 165 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 Fast | 0.6443 | — | — | — |
| 166 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.6 (non-reasoning, high) | 0.6437 | 23,987.41 | 0.5893 | ❌ |
| 167 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash 1017 (max) | 0.6408 | 9,174.75 | 0.4853 | ❌ |
| 168 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.1 Opus | 0.6400 | — | — | — |
| 169 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.5 (non-reasoning) | 0.6390 | 23,407.95 | 0.5866 | ❌ |
| 170 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.1 Pro Preview | 0.6387 | 30,325.48 | 0.6147 | ❌ |
| 171 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.7 (xhigh) | 0.6374 | 31,083.44 | 0.6174 | ❌ |
| 172 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (low) | 0.6355 | 13,045.58 | 0.5233 | ❌ |
| 173 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o4-mini (high) | 0.6350 | 12,577.51 | 0.5194 | ❌ |
| 174 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 35B A3B | 0.6334 | 3,378.54 | 0.3786 | ❌ |
| 175 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.7 Max | 0.6324 | 21,179.21 | 0.5758 | ❌ |
| 176 | <img src="https://artificialanalysis.ai/img/logos/motif.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif 3 | 0.6315 | — | — | — |
| 177 | <img src="https://artificialanalysis.ai/img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step 3.5 Flash 2603 | 0.6290 | 1,114.35 | 0.2643 | ❌ |
| 178 | <img src="https://artificialanalysis.ai/img/logos/nex.svg" width="18" alt="Nex AGI" /> Nex AGI | Nex-N2-Pro | 0.6288 | — | — | — |
| 179 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (medium) | 0.6249 | 24,927.29 | 0.5935 | ❌ |
| 180 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.1 (xhigh) | 0.6246 | 13,979.73 | 0.5308 | ❌ |
| 181 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.7 (low) | 0.6214 | 14,488.83 | 0.5347 | ❌ |
| 182 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.5 | 0.6214 | 7,671.62 | 0.4661 | ❌ |
| 183 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8-Flash-Next | 0.6194 | 3,268.67 | 0.3751 | ❌ |
| 184 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.6 | 0.6161 | 16,337.40 | 0.5477 | ❌ |
| 185 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (minimal) | 0.6140 | 9,874.76 | 0.4932 | ❌ |
| 186 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Terra (low) | 0.6139 | 4,634.04 | 0.4121 | ❌ |
| 187 | <img src="https://artificialanalysis.ai/img/logos/kwaikat.svg" width="18" alt="KwaiKAT" /> KwaiKAT | KAT-Coder-Pro V2 | 0.6120 | — | — | — |
| 188 | <img src="https://artificialanalysis.ai/img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step 5 Preview | 0.6115 | 10,983.32 | 0.5047 | ❌ |
| 189 | <img src="https://artificialanalysis.ai/img/logos/bytedance.svg" width="18" alt="ByteDance Seed" /> ByteDance Seed | Doubao Seed Code | 0.6098 | — | — | — |
| 190 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (max) | 0.6092 | 561.77 | 0.1988 | ✅ |
| 191 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (high) | 0.6091 | 12,818.43 | 0.5214 | ❌ |
| 192 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash (max) | 0.6090 | 10,386.25 | 0.4987 | ❌ |
| 193 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.6-Pro | 0.6084 | 2,629.39 | 0.3522 | ❌ |
| 194 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (medium) | 0.6078 | 9,068.48 | 0.4841 | ❌ |
| 195 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (low) | 0.6071 | 10,394.22 | 0.4988 | ❌ |
| 196 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 Instant (May 2026) | 0.6070 | — | — | — |
| 197 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3 (max) | 0.6057 | 30,006.36 | 0.6136 | ❌ |
| 198 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (non-reasoning) | 0.6043 | 9,736.38 | 0.4917 | ❌ |
| 199 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (max) | 0.6036 | 127,934.16 | 0.7714 | ❌ |
| 200 | <img src="https://artificialanalysis.ai/img/logos/baidu.svg" width="18" alt="Baidu" /> Baidu | ERNIE 5.0 Thinking Preview | 0.6032 | — | — | — |
| 201 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.1 (non-reasoning) | 0.6010 | 6,818.24 | 0.4534 | ❌ |
| 202 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (max) | 0.5998 | 6,159.50 | 0.4425 | ❌ |
| 203 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Exp | 0.5986 | — | — | — |
| 204 | <img src="https://artificialanalysis.ai/img/logos/china-mobile.png" width="18" alt="China Mobile" /> China Mobile | JT-4.1 Flash 236B A21B 0709 (non-reasoning) | 0.5977 | — | — | — |
| 205 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (non-reasoning, high) | 0.5966 | 14,025.85 | 0.5311 | ❌ |
| 206 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (xhigh) | 0.5964 | 104,280.61 | 0.7491 | ❌ |
| 207 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Ember (max) | 0.5959 | 1,518.32 | 0.2955 | ❌ |
| 208 | <img src="https://artificialanalysis.ai/img/logos/kwaikat.svg" width="18" alt="KwaiKAT" /> KwaiKAT | KAT-Coder-Pro V1 | 0.5948 | — | — | — |
| 209 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Haiku 5.5 (xhigh) | 0.5935 | 5,635.85 | 0.4330 | ❌ |
| 210 | <img src="https://artificialanalysis.ai/img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step 3.5 Flash | 0.5933 | 1,013.34 | 0.2549 | ❌ |
| 211 | <img src="https://artificialanalysis.ai/img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Open2 250B | 0.5932 | — | — | — |
| 212 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.2 Sol (low) | 0.5929 | 8,826.21 | 0.4811 | ❌ |
| 213 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.1 | 0.5920 | 11,659.34 | 0.5112 | ❌ |
| 214 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.6 (non-reasoning) | 0.5919 | 5,044.18 | 0.4211 | ❌ |
| 215 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3 Flash (non-reasoning) | 0.5905 | 2,940.29 | 0.3639 | ❌ |
| 216 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.1 Flash 1019 | 0.5886 | — | — | — |
| 217 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (high) | 0.5878 | — | — | — |
| 218 | <img src="https://artificialanalysis.ai/img/logos/servicenow.svg" width="18" alt="ServiceNow" /> ServiceNow | Apriel-v1.6-15B-Thinker | 0.5865 | — | — | — |
| 219 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 27B (non-reasoning) | 0.5859 | 2,313.91 | 0.3389 | ❌ |
| 220 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark Open (xhigh) | 0.5846 | 11,096.77 | 0.5058 | ❌ |
| 221 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (non-reasoning, low) | 0.5844 | 13,854.48 | 0.5298 | ❌ |
| 222 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3-Flash | 0.5840 | 2,976.01 | 0.3652 | ❌ |
| 223 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (non-reasoning) | 0.5832 | 20,718.99 | 0.5734 | ❌ |
| 224 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 397B A17B (non-reasoning) | 0.5831 | 2,603.64 | 0.3512 | ❌ |
| 225 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro 0813 (max) | 0.5829 | 22,398.74 | 0.5819 | ❌ |
| 226 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (medium) | 0.5822 | — | — | — |
| 227 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Sep) | 0.5821 | — | — | — |
| 228 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (medium) | 0.5820 | 12,593.81 | 0.5195 | ❌ |
| 229 | <img src="https://artificialanalysis.ai/img/logos/tencent-hy.svg" width="18" alt="Tencent" /> Tencent | Tencent Hy4 | 0.5818 | 29,335.31 | 0.6111 | ❌ |
| 230 | <img src="https://artificialanalysis.ai/img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE | 0.5813 | — | — | — |
| 231 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Ember (xhigh) | 0.5808 | 1,135.43 | 0.2662 | ❌ |
| 232 | <img src="https://artificialanalysis.ai/img/logos/china-mobile.png" width="18" alt="China Mobile" /> China Mobile | JT-4.1 Flash 236B A21B 0709 | 0.5795 | — | — | — |
| 233 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 3 mini Reasoning (high) | 0.5780 | — | — | — |
| 234 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (medium) | 0.5768 | 6,725.91 | 0.4519 | ❌ |
| 235 | <img src="https://artificialanalysis.ai/img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step 3.7 Flash | 0.5761 | 2,722.24 | 0.3559 | ❌ |
| 236 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (xhigh) | 0.5754 | 33,198.95 | 0.6246 | ❌ |
| 237 | <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M3.1-Flash | 0.5739 | 4,323.24 | 0.4047 | ❌ |
| 238 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 Omni Plus | 0.5737 | 3,568.04 | 0.3844 | ❌ |
| 239 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (high) | 0.5701 | 10,917.48 | 0.5041 | ❌ |
| 240 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (medium) | 0.5697 | 1,834.64 | 0.3148 | ❌ |
| 241 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 235B A22B | 0.5696 | — | — | — |
| 242 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (medium) | 0.5695 | 14,091.87 | 0.5317 | ❌ |
| 243 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.7 Plus | 0.5690 | 5,733.04 | 0.4348 | ❌ |
| 244 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.7 Code | 0.5687 | 10,588.66 | 0.5008 | ❌ |
| 245 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max Thinking (Preview) | 0.5664 | — | — | — |
| 246 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (max) | 0.5642 | 3,891.32 | 0.3935 | ❌ |
| 247 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (xhigh) | 0.5599 | 20,333.97 | 0.5714 | ❌ |
| 248 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (low) | 0.5567 | 11,831.48 | 0.5128 | ❌ |
| 249 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Sonnet | 0.5557 | — | — | — |
| 250 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max | 0.5528 | — | — | — |
| 251 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (low) | 0.5520 | 4,651.44 | 0.4125 | ❌ |
| 252 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 27B (non-reasoning) | 0.5510 | 3,377.71 | 0.3786 | ❌ |
| 253 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (low) | 0.5472 | — | — | — |
| 254 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 | 0.5464 | 5,232.21 | 0.4251 | ❌ |
| 255 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.5 (non-reasoning) | 0.5449 | 7,878.68 | 0.4689 | ❌ |
| 256 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5 | 0.5448 | — | — | — |
| 257 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Terra (non-reasoning) | 0.5448 | 4,555.54 | 0.4103 | ❌ |
| 258 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6 | 0.5424 | 4,906.60 | 0.4182 | ❌ |
| 259 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 122B A10B (non-reasoning) | 0.5407 | 3,197.65 | 0.3728 | ❌ |
| 260 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (non-reasoning) | 0.5401 | 26,699.46 | 0.6009 | ❌ |
| 261 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 32B | 0.5384 | — | — | — |
| 262 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (xhigh) | 0.5384 | 10,796.11 | 0.5029 | ❌ |
| 263 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Sonnet | 0.5377 | 25,206.71 | 0.5947 | ❌ |
| 264 | <img src="https://artificialanalysis.ai/img/logos/china-mobile.png" width="18" alt="China Mobile" /> China Mobile | JT-35B-Flash | 0.5374 | — | — | — |
| 265 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Hydrogen (low) | 0.5370 | 12,687.79 | 0.5203 | ❌ |
| 266 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash | 0.5355 | 7,307.21 | 0.4608 | ❌ |
| 267 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (low) | 0.5353 | 11,942.79 | 0.5138 | ❌ |
| 268 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 27B | 0.5329 | 7,898.19 | 0.4692 | ❌ |
| 269 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 (non-reasoning) | 0.5325 | 430.24 | 0.1750 | ✅ |
| 270 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Haiku 5.5 (high) | 0.5321 | 2,673.58 | 0.3540 | ❌ |
| 271 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.6-Flash | 0.5313 | 554.50 | 0.1976 | ❌ |
| 272 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (high) | 0.5286 | 3,592.89 | 0.3851 | ❌ |
| 273 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o1 | 0.5286 | — | — | — |
| 274 | <img src="https://artificialanalysis.ai/img/logos/sapiens.svg" width="18" alt="Sapiens AI" /> Sapiens AI | Agnes 2.5 Pro Theta | 0.5283 | 562.05 | 0.1988 | ❌ |
| 275 | <img src="https://artificialanalysis.ai/img/logos/servicenow.svg" width="18" alt="ServiceNow" /> ServiceNow | Apriel-v1.5-15B-Thinker | 0.5263 | — | — | — |
| 276 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5 (non-reasoning) | 0.5222 | 4,576.23 | 0.4108 | ❌ |
| 277 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (medium) | 0.5220 | 1,251.59 | 0.2759 | ❌ |
| 278 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (xhigh) | 0.5158 | 1,236.20 | 0.2747 | ❌ |
| 279 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (non-reasoning) | 0.5152 | 5,037.16 | 0.4210 | ❌ |
| 280 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5-Pro | 0.5129 | — | — | — |
| 281 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash 1017 (high) | 0.5107 | 4,485.30 | 0.4086 | ❌ |
| 282 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (medium) | 0.5107 | 1,688.51 | 0.3063 | ❌ |
| 283 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5 | 0.5106 | — | — | — |
| 284 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (high) | 0.5100 | 24,731.33 | 0.5926 | ❌ |
| 285 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 0528 | 0.5092 | 23,139.83 | 0.5854 | ❌ |
| 286 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-2.6-1T | 0.5091 | — | — | — |
| 287 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Large 4 Preview | 0.5078 | 11,149.81 | 0.5063 | ❌ |
| 288 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7 (non-reasoning) | 0.5078 | 4,342.47 | 0.4052 | ❌ |
| 289 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (low) | 0.5036 | 10,736.15 | 0.5023 | ❌ |
| 290 | <img src="https://artificialanalysis.ai/img/logos/bytedance.svg" width="18" alt="ByteDance Seed" /> ByteDance Seed | Seed-OSS-36B-Instruct | 0.5026 | 1,557.69 | 0.2981 | ❌ |
| 291 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 35B A3B (non-reasoning) | 0.5018 | 2,048.03 | 0.3262 | ❌ |
| 292 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Sep) | 0.5010 | — | — | — |
| 293 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 397B A17B | 0.5005 | 8,894.06 | 0.4820 | ❌ |
| 294 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (non-reasoning) | 0.5005 | 12,727.56 | 0.5206 | ❌ |
| 295 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Sonnet (non-reasoning) | 0.4992 | 14,000.95 | 0.5310 | ❌ |
| 296 | <img src="https://artificialanalysis.ai/img/logos/tencent-hy.svg" width="18" alt="Tencent" /> Tencent | Hy3 | 0.4982 | 2,158.55 | 0.3316 | ❌ |
| 297 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (high) | 0.4974 | 6,974.89 | 0.4558 | ❌ |
| 298 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 0905 | 0.4964 | 1,732.84 | 0.3090 | ❌ |
| 299 | <img src="https://artificialanalysis.ai/img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | G9v3-39A5B | 0.4958 | — | — | — |
| 300 | <img src="https://artificialanalysis.ai/img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.5 33B | 0.4955 | — | — | — |
| 301 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3 (low) | 0.4940 | 13,105.02 | 0.5238 | ❌ |
| 302 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (non-reasoning) | 0.4934 | — | — | — |
| 303 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (high) | 0.4895 | 9,571.06 | 0.4899 | ❌ |
| 304 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (high) | 0.4892 | 914.15 | 0.2448 | ❌ |
| 305 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash (non-reasoning) | 0.4868 | — | — | — |
| 306 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 Instant (June 2026) | 0.4833 | 29,540.90 | 0.6119 | ❌ |
| 307 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-3.0-flash-VL | 0.4823 | — | — | — |
| 308 | <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5-Pro (non-reasoning) | 0.4788 | — | — | — |
| 309 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 (non-reasoning) | 0.4771 | — | — | — |
| 310 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Sep) (non-reasoning) | 0.4769 | — | — | — |
| 311 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5-Air | 0.4760 | 1,366.30 | 0.2848 | ❌ |
| 312 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7-Flash | 0.4758 | 1,007.14 | 0.2543 | ❌ |
| 313 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 35B A3B (non-reasoning) | 0.4757 | 1,887.29 | 0.3177 | ❌ |
| 314 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (non-reasoning) | 0.4749 | 11,476.81 | 0.5095 | ❌ |
| 315 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 4B | 0.4734 | 533.81 | 0.1941 | ❌ |
| 316 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok Code Fast 1 | 0.4727 | — | — | — |
| 317 | <img src="https://artificialanalysis.ai/img/logos/multiversecomputing.svg" width="18" alt="Multiverse Computing" /> Multiverse Computing | Quasar 438B (max) | 0.4722 | — | — | — |
| 318 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max (Preview) | 0.4714 | — | — | — |
| 319 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-1T | 0.4684 | — | — | — |
| 320 | <img src="https://artificialanalysis.ai/img/logos/joy-ai.svg" width="18" alt="Joy Future Academy" /> Joy Future Academy | JoyAI-VL-Preview | 0.4671 | — | — | — |
| 321 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Haiku 5.5 (medium) | 0.4663 | 1,486.51 | 0.2933 | ❌ |
| 322 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Pro | 0.4644 | 26,101.87 | 0.5985 | ❌ |
| 323 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (low) | 0.4638 | 4,952.50 | 0.4192 | ❌ |
| 324 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 Terminus | 0.4626 | — | — | — |
| 325 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 31B (non-reasoning) | 0.4617 | 1,669.34 | 0.3051 | ❌ |
| 326 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro 0813 (high) | 0.4598 | 20,432.64 | 0.5719 | ❌ |
| 327 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (low) | 0.4595 | 1,174.44 | 0.2696 | ❌ |
| 328 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 v2 (non-reasoning) | 0.4595 | 4,192.55 | 0.4015 | ❌ |
| 329 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 | 0.4593 | 1,669.62 | 0.3052 | ❌ |
| 330 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (non-reasoning) | 0.4582 | 10,000.19 | 0.4946 | ❌ |
| 331 | <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.7 | 0.4575 | 1,842.33 | 0.3153 | ❌ |
| 332 | <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M3 | 0.4575 | 11,531.01 | 0.5100 | ❌ |
| 333 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 375B A23B | 0.4575 | 0.00 | 0.0000 | ✅ |
| 334 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3 (low) | 0.4575 | 7,505.91 | 0.4637 | ❌ |
| 335 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Opus (non-reasoning) | 0.4571 | — | — | — |
| 336 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 122B A10B | 0.4565 | 6,315.99 | 0.4452 | ❌ |
| 337 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (medium) | 0.4564 | 11,733.57 | 0.5119 | ❌ |
| 338 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 9B (non-reasoning) | 0.4545 | 285.57 | 0.1408 | ❌ |
| 339 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 Omni Flash | 0.4535 | 739.79 | 0.2245 | ❌ |
| 340 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (high) | 0.4519 | — | — | — |
| 341 | <img src="https://artificialanalysis.ai/img/logos/prime-intellect.svg" width="18" alt="Prime Intellect" /> Prime Intellect | INTELLECT-3 | 0.4501 | — | — | — |
| 342 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.2 (non-reasoning) | 0.4499 | 5,373.36 | 0.4279 | ❌ |
| 343 | <img src="https://artificialanalysis.ai/img/logos/deepcogito.png" width="18" alt="Deep Cogito" /> Deep Cogito | Cogito v2.1 | 0.4481 | — | — | — |
| 344 | <img src="https://artificialanalysis.ai/img/logos/korea-telecom.png" width="18" alt="Korea Telecom" /> Korea Telecom | Mi:dm K 2.5 Pro | 0.4474 | — | — | — |
| 345 | <img src="https://artificialanalysis.ai/img/logos/tencent-hy.svg" width="18" alt="Tencent" /> Tencent | Hy3-preview (non-reasoning) | 0.4469 | — | — | — |
| 346 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.7 Sonnet | 0.4468 | — | — | — |
| 347 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 30B A3B | 0.4449 | — | — | — |
| 348 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (medium) | 0.4426 | 675.55 | 0.2159 | ❌ |
| 349 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 35B A3B | 0.4423 | 5,428.62 | 0.4290 | ❌ |
| 350 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Next 80B A3B | 0.4415 | — | — | — |
| 351 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 Terminus (non-reasoning) | 0.4398 | 2,046.52 | 0.3261 | ❌ |
| 352 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Sonnet (non-reasoning) | 0.4393 | — | — | — |
| 353 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (medium) | 0.4387 | 5,645.58 | 0.4332 | ❌ |
| 354 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Exp (non-reasoning) | 0.4375 | — | — | — |
| 355 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Magistral Medium 1.2 | 0.4352 | — | — | — |
| 356 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (minimal) | 0.4348 | 8,889.83 | 0.4819 | ❌ |
| 357 | <img src="https://artificialanalysis.ai/img/logos/apodex.svg" width="18" alt="Apodex" /> Apodex | Apodex 1.1 | 0.4347 | — | — | — |
| 358 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron Cascade 2 30B A3B | 0.4345 | — | — | — |
| 359 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 235B A22B | 0.4326 | 2,465.94 | 0.3455 | ❌ |
| 360 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 26B A4B (non-reasoning) | 0.4321 | 987.77 | 0.2524 | ❌ |
| 361 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Large 4 (medium) | 0.4293 | 7,649.61 | 0.4658 | ❌ |
| 362 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 | 0.4265 | 12,385.42 | 0.5177 | ❌ |
| 363 | <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax M1 80k | 0.4263 | 1,861.21 | 0.3163 | ❌ |
| 364 | <img src="https://artificialanalysis.ai/img/logos/motif.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif-2-12.7B | 0.4250 | — | — | — |
| 365 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o3-mini | 0.4247 | 12,511.39 | 0.5188 | ❌ |
| 366 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (ChatGPT) | 0.4239 | — | — | — |
| 367 | <img src="https://artificialanalysis.ai/img/logos/reflection.svg" width="18" alt="Reflection" /> Reflection | Beam 1.0 | 0.4225 | 3,516.34 | 0.3828 | ❌ |
| 368 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B 2507 | 0.4219 | 2,754.68 | 0.3571 | ❌ |
| 369 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 (non-reasoning) | 0.4209 | 9,171.01 | 0.4853 | ❌ |
| 370 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6 (non-reasoning) | 0.4191 | 5,265.92 | 0.4257 | ❌ |
| 371 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 3 | 0.4184 | — | — | — |
| 372 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (low) | 0.4155 | 4,331.87 | 0.4049 | ❌ |
| 373 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Next 80B A3B | 0.4150 | 1,596.47 | 0.3006 | ❌ |
| 374 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-20b (low) | 0.4149 | 217.80 | 0.1202 | ❌ |
| 375 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 (non-reasoning) | 0.4142 | 4,976.19 | 0.4197 | ❌ |
| 376 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Large 4 (high) | 0.4135 | 11,892.96 | 0.5133 | ❌ |
| 377 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 26B A4B | 0.4132 | 1,349.52 | 0.2835 | ❌ |
| 378 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Sep) (non-reasoning) | 0.4105 | — | — | — |
| 379 | <img src="https://artificialanalysis.ai/img/logos/naver.webp" width="18" alt="Naver" /> Naver | HyperCLOVA X SEED Think (32B) | 0.4101 | — | — | — |
| 380 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Super 49B v1.5 | 0.4099 | — | — | — |
| 381 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Haiku (non-reasoning) | 0.4077 | 4,748.63 | 0.4147 | ❌ |
| 382 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-1T | 0.4076 | — | — | — |
| 383 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B 2507 | 0.4063 | — | — | — |
| 384 | <img src="https://artificialanalysis.ai/img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 4 | 0.4057 | 4,013.34 | 0.3968 | ❌ |
| 385 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (non-reasoning) | 0.4052 | 1,968.50 | 0.3221 | ❌ |
| 386 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite | 0.4050 | 2,599.24 | 0.3510 | ❌ |
| 387 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | QwQ-32B | 0.4036 | — | — | — |
| 388 | <img src="https://artificialanalysis.ai/img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.0 32B | 0.4026 | — | — | — |
| 389 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 32B | 0.4019 | — | — | — |
| 390 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (minimal) | 0.4017 | 1,692.26 | 0.3065 | ❌ |
| 391 | <img src="https://artificialanalysis.ai/img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Mini 4 | 0.4004 | 1,991.09 | 0.3233 | ❌ |
| 392 | <img src="https://artificialanalysis.ai/img/logos/korea-telecom.png" width="18" alt="Korea Telecom" /> Korea Telecom | Mi:dm K 2.5 Pro Preview | 0.3989 | — | — | — |
| 393 | <img src="https://artificialanalysis.ai/img/logos/tii.svg" width="18" alt="TII UAE" /> TII UAE | Falcon-H1R-7B | 0.3977 | — | — | — |
| 394 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.7 Sonnet (non-reasoning) | 0.3963 | — | — | — |
| 395 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash-Lite | 0.3924 | 5,568.51 | 0.4317 | ❌ |
| 396 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (low) | 0.3919 | 10,147.22 | 0.4962 | ❌ |
| 397 | <img src="https://artificialanalysis.ai/img/logos/thinking-machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling Small | 0.3889 | 4,126.07 | 0.3998 | ❌ |
| 398 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-2.6-1T | 0.3889 | — | — | — |
| 399 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.0 Flash | 0.3856 | 494.00 | 0.1872 | ❌ |
| 400 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Haiku 5.5 (low) | 0.3856 | 1,015.05 | 0.2551 | ❌ |
| 401 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder 480B | 0.3850 | 3,676.30 | 0.3875 | ❌ |
| 402 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash (non-reasoning) | 0.3836 | 1,091.11 | 0.2622 | ❌ |
| 403 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon MoVA 36B A4B | 0.3824 | — | — | — |
| 404 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6V | 0.3815 | 2,634.62 | 0.3524 | ❌ |
| 405 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 12B v2 VL | 0.3811 | — | — | — |
| 406 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-3.0-flash-Fin | 0.3808 | — | — | — |
| 407 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (non-reasoning) | 0.3794 | 11,098.30 | 0.5058 | ❌ |
| 408 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 9B | 0.3775 | 787.10 | 0.2304 | ❌ |
| 409 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Omni 30B A3B | 0.3771 | 2,863.79 | 0.3612 | ❌ |
| 410 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B A22B 2507 | 0.3768 | 9,871.11 | 0.4932 | ❌ |
| 411 | <img src="https://artificialanalysis.ai/img/logos/nousresearch.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 405B | 0.3767 | 4,237.28 | 0.4026 | ❌ |
| 412 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-120b (low) | 0.3759 | 1,645.83 | 0.3037 | ❌ |
| 413 | <img src="https://artificialanalysis.ai/img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE (non-reasoning) | 0.3751 | — | — | — |
| 414 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash 1017 (non-reasoning) | 0.3749 | 1,056.28 | 0.2590 | ❌ |
| 415 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 30B A3B | 0.3724 | 565.72 | 0.1994 | ❌ |
| 416 | <img src="https://artificialanalysis.ai/img/logos/longcat.svg" width="18" alt="LongCat" /> LongCat | LongCat 2.0 | 0.3723 | 10,298.19 | 0.4978 | ❌ |
| 417 | <img src="https://artificialanalysis.ai/img/logos/nanbeige.png" width="18" alt="Nanbeige" /> Nanbeige | Nanbeige4.3-33B | 0.3714 | — | — | — |
| 418 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | DiffusionGemma 26B A4B | 0.3686 | — | — | — |
| 419 | <img src="https://artificialanalysis.ai/img/logos/thinking-machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling (xhigh) | 0.3667 | 10,645.17 | 0.5013 | ❌ |
| 420 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (non-reasoning) | 0.3656 | 7,327.71 | 0.4611 | ❌ |
| 421 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-flash-2.0 | 0.3652 | — | — | — |
| 422 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (medium) | 0.3644 | — | — | — |
| 423 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3.5 Bolt 74B-A9B | 0.3636 | — | — | — |
| 424 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 4B (non-reasoning) | 0.3628 | 101.54 | 0.0722 | ❌ |
| 425 | <img src="https://artificialanalysis.ai/img/logos/china-mobile.png" width="18" alt="China Mobile" /> China Mobile | JT-MINI | 0.3625 | — | — | — |
| 426 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 2.6 Flash | 0.3586 | — | — | — |
| 427 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Ultra | 0.3581 | 5,401.26 | 0.4285 | ❌ |
| 428 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.1 Fast (non-reasoning) | 0.3557 | — | — | — |
| 429 | <img src="https://artificialanalysis.ai/img/logos/longcat.svg" width="18" alt="LongCat" /> LongCat | LongCat Flash Lite | 0.3556 | — | — | — |
| 430 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Haiku | 0.3547 | 15,506.25 | 0.5420 | ❌ |
| 431 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3.5 Super VL | 0.3546 | 2,521.90 | 0.3478 | ❌ |
| 432 | <img src="https://artificialanalysis.ai/img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Open 100B | 0.3543 | — | — | — |
| 433 | <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax M1 40k | 0.3520 | — | — | — |
| 434 | <img src="https://artificialanalysis.ai/img/logos/inceptionlabs.svg" width="18" alt="Inception" /> Inception | Mercury 2 | 0.3518 | 1,678.48 | 0.3057 | ❌ |
| 435 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 12B | 0.3513 | — | — | — |
| 436 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 Fast (non-reasoning) | 0.3507 | — | — | — |
| 437 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 12B (non-reasoning) | 0.3499 | — | — | — |
| 438 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B | 0.3496 | — | — | — |
| 439 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 31B | 0.3471 | 0.00 | 0.0000 | ❌ |
| 440 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Ultra | 0.3446 | — | — | — |
| 441 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (non-reasoning) | 0.3442 | 4,169.82 | 0.4009 | ❌ |
| 442 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 mini | 0.3422 | 2,233.19 | 0.3352 | ❌ |
| 443 | <img src="https://artificialanalysis.ai/img/logos/multiversecomputing.svg" width="18" alt="Multiverse Computing" /> Multiverse Computing | HyperNova 60B 2605 (high) | 0.3388 | — | — | — |
| 444 | <img src="https://artificialanalysis.ai/img/logos/trillionlabs.svg" width="18" alt="Trillion Labs" /> Trillion Labs | Tri-21B-think Preview | 0.3361 | — | — | — |
| 445 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3.1 32B Think | 0.3357 | — | — | — |
| 446 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Glimmer (high) | 0.3347 | 3,439.10 | 0.3805 | ❌ |
| 447 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5V | 0.3334 | 3,480.09 | 0.3817 | ❌ |
| 448 | <img src="https://artificialanalysis.ai/img/logos/sktelecom.svg" width="18" alt="SK Telecom" /> SK Telecom | A.X-K2 | 0.3319 | — | — | — |
| 449 | <img src="https://artificialanalysis.ai/img/logos/trillionlabs.svg" width="18" alt="Trillion Labs" /> Trillion Labs | Tri-21B-Think | 0.3316 | — | — | — |
| 450 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (non-reasoning) | 0.3315 | 4,139.71 | 0.4001 | ❌ |
| 451 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-flash-2.0 | 0.3311 | 453.44 | 0.1796 | ❌ |
| 452 | <img src="https://artificialanalysis.ai/img/logos/nousresearch.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 70B | 0.3285 | — | — | — |
| 453 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Medium 3.5 | 0.3284 | 25,194.36 | 0.5946 | ❌ |
| 454 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (non-reasoning) | 0.3280 | 3,359.90 | 0.3780 | ❌ |
| 455 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (non-reasoning) | 0.3232 | 1,103.57 | 0.2634 | ❌ |
| 456 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (non-reasoning) | 0.3198 | 1,929.81 | 0.3200 | ❌ |
| 457 | <img src="https://artificialanalysis.ai/img/logos/china-mobile.png" width="18" alt="China Mobile" /> China Mobile | JT-4.1 Flash 236B A21B | 0.3196 | — | — | — |
| 458 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 9B V2 | 0.3193 | 131.03 | 0.0865 | ❌ |
| 459 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano Omni 30B A3B | 0.3171 | — | — | — |
| 460 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7-Flash (non-reasoning) | 0.3146 | 767.77 | 0.2280 | ❌ |
| 461 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B A3B 2507 (non-reasoning) | 0.3115 | 251.46 | 0.1310 | ❌ |
| 462 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano | 0.3114 | 966.95 | 0.2503 | ❌ |
| 463 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (low) | 0.3109 | 531.12 | 0.1937 | ❌ |
| 464 | <img src="https://artificialanalysis.ai/img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 2 | 0.3104 | — | — | — |
| 465 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 32B | 0.3104 | — | — | — |
| 466 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 7B | 0.3095 | — | — | — |
| 467 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Magistral Small 1.2 | 0.3070 | 1,070.22 | 0.2603 | ❌ |
| 468 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 9B V2 (non-reasoning) | 0.3057 | 168.30 | 0.1023 | ❌ |
| 469 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Super | 0.3057 | 6,809.80 | 0.4533 | ❌ |
| 470 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 32B Think | 0.3037 | — | — | — |
| 471 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (non-reasoning) | 0.3037 | — | — | — |
| 472 | <img src="https://artificialanalysis.ai/img/logos/arcee.svg" width="18" alt="Arcee AI" /> Arcee AI | Trinity Large Thinking | 0.3015 | — | — | — |
| 473 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Think V2 | 0.3006 | — | — | — |
| 474 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B | 0.3005 | 1,158.89 | 0.2682 | ❌ |
| 475 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o (Aug) | 0.2961 | 20,066.99 | 0.5699 | ❌ |
| 476 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 8B | 0.2952 | — | — | — |
| 477 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Medium 3 | 0.2928 | 1,606.09 | 0.3012 | ❌ |
| 478 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-20b (high) | 0.2921 | 1,511.88 | 0.2950 | ❌ |
| 479 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.1 Flash-Lite | 0.2920 | 7,661.78 | 0.4659 | ❌ |
| 480 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 14B | 0.2896 | — | — | — |
| 481 | <img src="https://artificialanalysis.ai/img/logos/cohere.svg" width="18" alt="Cohere" /> Cohere | Command A+ | 0.2888 | 0.00 | 0.0000 | ❌ |
| 482 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder Next | 0.2868 | 3,465.16 | 0.3813 | ❌ |
| 483 | <img src="https://artificialanalysis.ai/img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step3 VL 10B | 0.2850 | — | — | — |
| 484 | <img src="https://artificialanalysis.ai/img/logos/baidu.svg" width="18" alt="Baidu" /> Baidu | ERNIE 4.5 300B A47B | 0.2845 | — | — | — |
| 485 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (non-reasoning) | 0.2838 | 1,125.07 | 0.2653 | ❌ |
| 486 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Pixtral Large | 0.2837 | — | — | — |
| 487 | <img src="https://artificialanalysis.ai/img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE 2.0 | 0.2811 | — | — | — |
| 488 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o3-mini (high) | 0.2807 | 20,142.25 | 0.5703 | ❌ |
| 489 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 (Jan) | 0.2799 | 7,758.28 | 0.4673 | ❌ |
| 490 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder 30B A3B | 0.2787 | 1,158.29 | 0.2682 | ❌ |
| 491 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.0 Tiny | 0.2780 | 0.00 | 0.0000 | ❌ |
| 492 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.3 Nemotron Super 49B | 0.2661 | — | — | — |
| 493 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-120b (high) | 0.2657 | 2,761.49 | 0.3574 | ❌ |
| 494 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 E4B (non-reasoning) | 0.2654 | 71.82 | 0.0555 | ❌ |
| 495 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (non-reasoning) | 0.2653 | 408.24 | 0.1704 | ❌ |
| 496 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Omni 30B A3B | 0.2648 | 727.03 | 0.2228 | ❌ |
| 497 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Devstral 2 | 0.2644 | — | — | — |
| 498 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 7B Think | 0.2625 | — | — | — |
| 499 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Medium 3.1 | 0.2596 | — | — | — |
| 500 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.0 Flash | 0.2594 | — | — | — |
| 501 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Magistral Medium 1 | 0.2591 | — | — | — |
| 502 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova Premier | 0.2576 | — | — | — |
| 503 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro 0813 (non-reasoning) | 0.2572 | 4,113.65 | 0.3994 | ❌ |
| 504 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B A3B 2507 | 0.2551 | — | — | — |
| 505 | <img src="https://artificialanalysis.ai/img/logos/nousresearch.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 405B (non-reasoning) | 0.2527 | 2,710.73 | 0.3554 | ❌ |
| 506 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.1 Nemotron Nano 4B v1.1 | 0.2505 | — | — | — |
| 507 | <img src="https://artificialanalysis.ai/img/logos/thinking-machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling (high) | 0.2497 | 10,742.41 | 0.5023 | ❌ |
| 508 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 3.7B | 0.2488 | — | — | — |
| 509 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B | 0.2477 | — | — | — |
| 510 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (low) | 0.2477 | — | — | — |
| 511 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B 2507 (non-reasoning) | 0.2466 | — | — | — |
| 512 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (non-reasoning) | 0.2450 | 489.61 | 0.1864 | ❌ |
| 513 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Small 4 (non-reasoning) | 0.2449 | 650.17 | 0.2123 | ❌ |
| 514 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Devstral Small 2 | 0.2443 | — | — | — |
| 515 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.2 30B | 0.2442 | — | — | — |
| 516 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3 0324 | 0.2440 | 1,974.43 | 0.3224 | ❌ |
| 517 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Magistral Small 1 | 0.2433 | — | — | — |
| 518 | <img src="https://artificialanalysis.ai/img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.0 32B (non-reasoning) | 0.2401 | — | — | — |
| 519 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6V (non-reasoning) | 0.2401 | 2,584.79 | 0.3504 | ❌ |
| 520 | <img src="https://artificialanalysis.ai/img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-1B | 0.2385 | — | — | — |
| 521 | <img src="https://artificialanalysis.ai/img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam 105B (high) | 0.2377 | 587.21 | 0.2028 | ❌ |
| 522 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 0528 Qwen3 8B | 0.2375 | — | — | — |
| 523 | <img src="https://artificialanalysis.ai/img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-2B | 0.2352 | — | — | — |
| 524 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 4B | 0.2343 | — | — | — |
| 525 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 32B | 0.2333 | — | — | — |
| 526 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Large 3 | 0.2316 | 1,871.15 | 0.3169 | ❌ |
| 527 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o (Nov) | 0.2314 | 23,239.93 | 0.5859 | ❌ |
| 528 | <img src="https://artificialanalysis.ai/img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 3 | 0.2307 | 1,255.55 | 0.2763 | ❌ |
| 529 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi Linear 48B A3B Instruct | 0.2302 | — | — | — |
| 530 | <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-mini-2.0 | 0.2285 | — | — | — |
| 531 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.5 Haiku | 0.2281 | — | — | — |
| 532 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (minimal) | 0.2272 | 360.80 | 0.1599 | ❌ |
| 533 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 8B | 0.2231 | — | — | — |
| 534 | <img src="https://artificialanalysis.ai/img/logos/thinking-machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling Small (high) | 0.2231 | 4,114.29 | 0.3995 | ❌ |
| 535 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Devstral Small (May) | 0.2227 | — | — | — |
| 536 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 2B | 0.2222 | — | — | — |
| 537 | <img src="https://artificialanalysis.ai/img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 2 (non-reasoning) | 0.2204 | — | — | — |
| 538 | <img src="https://artificialanalysis.ai/img/logos/inceptionlabs.svg" width="18" alt="Inception" /> Inception | Mercury 2.5 | 0.2184 | 1,597.12 | 0.3006 | ❌ |
| 539 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 32B (non-reasoning) | 0.2161 | 398.41 | 0.1683 | ❌ |
| 540 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B (non-reasoning) | 0.2115 | — | — | — |
| 541 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.1 30B | 0.2110 | — | — | — |
| 542 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 4 Maverick | 0.2105 | 2,972.80 | 0.3651 | ❌ |
| 543 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 32B | 0.2088 | 907.28 | 0.2441 | ❌ |
| 544 | <img src="https://artificialanalysis.ai/img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | Exaone 4.0 1.2B | 0.2087 | — | — | — |
| 545 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 14B (non-reasoning) | 0.2080 | 370.36 | 0.1621 | ❌ |
| 546 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 2B (non-reasoning) | 0.2048 | — | — | — |
| 547 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen2.5 72B | 0.2047 | 576.35 | 0.2011 | ❌ |
| 548 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Small 4 | 0.2036 | 1,642.33 | 0.3035 | ❌ |
| 549 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 12B v2 VL (non-reasoning) | 0.2030 | 548.21 | 0.1965 | ❌ |
| 550 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 4B | 0.2028 | — | — | — |
| 551 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3.5 Lightning | 0.2014 | 1,323.04 | 0.2815 | ❌ |
| 552 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Devstral Small | 0.2011 | — | — | — |
| 553 | <img src="https://artificialanalysis.ai/img/logos/cohere.svg" width="18" alt="Cohere" /> Cohere | North Mini Code | 0.2009 | 0.00 | 0.0000 | ❌ |
| 554 | <img src="https://artificialanalysis.ai/img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-1B (non-reasoning) | 0.2005 | — | — | — |
| 555 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Devstral Medium | 0.1981 | — | — | — |
| 556 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova Pro | 0.1968 | 4,812.76 | 0.4161 | ❌ |
| 557 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.1 405B | 0.1966 | — | — | — |
| 558 | <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5V (non-reasoning) | 0.1946 | 2,738.72 | 0.3565 | ❌ |
| 559 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Llama 70B | 0.1926 | — | — | — |
| 560 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Large 2 (Nov) | 0.1925 | — | — | — |
| 561 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-8B-A1B | 0.1915 | — | — | — |
| 562 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Large 2 (Jul) | 0.1874 | — | — | — |
| 563 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Llama 8B | 0.1871 | — | — | — |
| 564 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Super 49B v1.5 (non-reasoning) | 0.1866 | — | — | — |
| 565 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 14B | 0.1860 | 347.26 | 0.1567 | ❌ |
| 566 | <img src="https://artificialanalysis.ai/img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | G9v3-3B | 0.1849 | — | — | — |
| 567 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.2 8B | 0.1831 | 1,172.11 | 0.2694 | ❌ |
| 568 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o mini | 0.1827 | 1,161.17 | 0.2684 | ❌ |
| 569 | <img src="https://artificialanalysis.ai/img/logos/cohere.svg" width="18" alt="Cohere" /> Cohere | Command A | 0.1819 | 9,863.79 | 0.4931 | ❌ |
| 570 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B (non-reasoning) | 0.1790 | 326.97 | 0.1517 | ❌ |
| 571 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 E2B (non-reasoning) | 0.1789 | — | — | — |
| 572 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3 (Dec) | 0.1762 | 718.93 | 0.2217 | ❌ |
| 573 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano (non-reasoning) | 0.1754 | 627.94 | 0.2090 | ❌ |
| 574 | <img src="https://artificialanalysis.ai/img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam 30B (high) | 0.1747 | — | — | — |
| 575 | <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 nano | 0.1724 | 563.76 | 0.1991 | ❌ |
| 576 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Ministral 3 14B | 0.1715 | 450.56 | 0.1790 | ❌ |
| 577 | <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3 Haiku | 0.1679 | — | — | — |
| 578 | <img src="https://artificialanalysis.ai/img/logos/reka.svg" width="18" alt="Reka AI" /> Reka AI | Reka Flash 3 | 0.1676 | 252.22 | 0.1312 | ❌ |
| 579 | <img src="https://artificialanalysis.ai/img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM-V 4.6 1.3B | 0.1675 | — | — | — |
| 580 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.3 Nemotron Super 49B (non-reasoning) | 0.1659 | — | — | — |
| 581 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 E2B | 0.1620 | — | — | — |
| 582 | <img src="https://artificialanalysis.ai/img/logos/nanbeige.png" width="18" alt="Nanbeige" /> Nanbeige | Nanbeige4.1-3B | 0.1612 | — | — | — |
| 583 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Small 3.2 | 0.1590 | 171.80 | 0.1037 | ❌ |
| 584 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 1.7B | 0.1583 | — | — | — |
| 585 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 7B | 0.1577 | — | — | — |
| 586 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 E4B | 0.1576 | 291.05 | 0.1423 | ❌ |
| 587 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova Lite | 0.1575 | 351.22 | 0.1577 | ❌ |
| 588 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.3 70B | 0.1555 | 6,963.52 | 0.4557 | ❌ |
| 589 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Small 3 | 0.1539 | 74.20 | 0.0569 | ❌ |
| 590 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3.1 32B Instruct | 0.1519 | — | — | — |
| 591 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral Small 3.1 | 0.1515 | 133.86 | 0.0878 | ❌ |
| 592 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 4 Scout | 0.1470 | 514.14 | 0.1907 | ❌ |
| 593 | <img src="https://artificialanalysis.ai/img/logos/ai21.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba Reasoning 3B | 0.1469 | — | — | — |
| 594 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H Small | 0.1433 | — | — | — |
| 595 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.1 8B | 0.1433 | — | — | — |
| 596 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.1 Nemotron 70B | 0.1426 | — | — | — |
| 597 | <img src="https://artificialanalysis.ai/img/logos/celeris.svg" width="18" alt="Celeris" /> Celeris | Celeris-1 | 0.1414 | 1,276.33 | 0.2779 | ❌ |
| 598 | <img src="https://artificialanalysis.ai/img/logos/nousresearch.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 70B (non-reasoning) | 0.1406 | — | — | — |
| 599 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Ministral 3 8B | 0.1405 | 334.65 | 0.1536 | ❌ |
| 600 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 8B (non-reasoning) | 0.1405 | — | — | — |
| 601 | <img src="https://artificialanalysis.ai/img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | Exaone 4.0 1.2B (non-reasoning) | 0.1394 | — | — | — |
| 602 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 24B A2B | 0.1362 | — | — | — |
| 603 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.1 70B | 0.1354 | 709.03 | 0.2204 | ❌ |
| 604 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.2 3B | 0.1327 | — | — | — |
| 605 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM3-1.7B | 0.1321 | 783.66 | 0.2300 | ❌ |
| 606 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 8B | 0.1316 | — | — | — |
| 607 | <img src="https://artificialanalysis.ai/img/logos/ai21.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba 1.7 Large | 0.1281 | — | — | — |
| 608 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-2.6B | 0.1270 | — | — | — |
| 609 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-1.2B-Thinking | 0.1200 | — | — | — |
| 610 | <img src="https://artificialanalysis.ai/img/logos/microsoft.svg" width="18" alt="Microsoft" /> Microsoft | Phi-4 | 0.1197 | 435.15 | 0.1759 | ❌ |
| 611 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 8B A1B | 0.1141 | — | — | — |
| 612 | <img src="https://artificialanalysis.ai/img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam M | 0.1093 | — | — | — |
| 613 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-1.2B-Instruct | 0.1087 | — | — | — |
| 614 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 0.8B (non-reasoning) | 0.1072 | — | — | — |
| 615 | <img src="https://artificialanalysis.ai/img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova Micro | 0.1039 | 212.57 | 0.1185 | ❌ |
| 616 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3 70B | 0.0979 | 1,859.43 | 0.3162 | ❌ |
| 617 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.2 3B | 0.0964 | — | — | — |
| 618 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Molmo2-8B | 0.0962 | — | — | — |
| 619 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 27B | 0.0952 | 0.00 | 0.0000 | ❌ |
| 620 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Ministral 3 3B | 0.0920 | 232.48 | 0.1251 | ❌ |
| 621 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.1 3B | 0.0912 | — | — | — |
| 622 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 Micro | 0.0883 | — | — | — |
| 623 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.2 11B (Vision) | 0.0875 | 429.12 | 0.1747 | ❌ |
| 624 | <img src="https://artificialanalysis.ai/img/logos/ai21.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba 1.7 Mini | 0.0832 | — | — | — |
| 625 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-VL-1.6B | 0.0791 | — | — | — |
| 626 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 0.6B | 0.0776 | — | — | — |
| 627 | <img src="https://artificialanalysis.ai/img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano 4B | 0.0776 | — | — | — |
| 628 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H 1B | 0.0775 | — | — | — |
| 629 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 3.3 8B (non-reasoning) | 0.0732 | — | — | — |
| 630 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | OLMo 2 32B | 0.0726 | — | — | — |
| 631 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 12B | 0.0724 | 0.00 | 0.0000 | ❌ |
| 632 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.1 8B | 0.0714 | 66.50 | 0.0522 | ❌ |
| 633 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 4B | 0.0679 | 0.00 | 0.0000 | ❌ |
| 634 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 1.7B (non-reasoning) | 0.0672 | — | — | — |
| 635 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 0.8B | 0.0641 | — | — | — |
| 636 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 1B | 0.0629 | — | — | — |
| 637 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3n E4B | 0.0623 | — | — | — |
| 638 | <img src="https://artificialanalysis.ai/img/logos/microsoft.svg" width="18" alt="Microsoft" /> Microsoft | Phi-3 Mini | 0.0608 | — | — | — |
| 639 | <img src="https://artificialanalysis.ai/img/logos/swiss-ai-initiative.png" width="18" alt="Swiss AI Initiative" /> Swiss AI Initiative | Apertus 70B Instruct | 0.0577 | — | — | — |
| 640 | <img src="https://artificialanalysis.ai/img/logos/microsoft.svg" width="18" alt="Microsoft" /> Microsoft | Phi-4 Mini | 0.0564 | 218.30 | 0.1204 | ❌ |
| 641 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 2.6B | 0.0542 | — | — | — |
| 642 | <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 0.6B (non-reasoning) | 0.0479 | — | — | — |
| 643 | <img src="https://artificialanalysis.ai/img/logos/swiss-ai-initiative.png" width="18" alt="Swiss AI Initiative" /> Swiss AI Initiative | Apertus 8B Instruct | 0.0431 | — | — | — |
| 644 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3 8B | 0.0425 | 106.88 | 0.0749 | ❌ |
| 645 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | OLMo 2 7B | 0.0339 | — | — | — |
| 646 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3n E2B | 0.0324 | — | — | — |
| 647 | <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 1.5B | 0.0305 | — | — | — |
| 648 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 1.2B | 0.0297 | — | — | — |
| 649 | <img src="https://artificialanalysis.ai/img/logos/cohere.svg" width="18" alt="Cohere" /> Cohere | Tiny Aya Global | 0.0291 | 0.00 | 0.0000 | ❌ |
| 650 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H 350M | 0.0274 | — | — | — |
| 651 | <img src="https://artificialanalysis.ai/img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Molmo 7B-D | 0.0259 | — | — | — |
| 652 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 1B | 0.0240 | — | — | — |
| 653 | <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 350M | 0.0207 | — | — | — |
| 654 | <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.2 1B | 0.0153 | — | — | — |
| 655 | <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 0.9B | 0.0141 | — | — | — |
| 656 | <img src="https://artificialanalysis.ai/img/logos/mistral.svg" width="18" alt="Mistral" /> Mistral | Mistral 7B | 0.0106 | 203.21 | 0.1153 | ❌ |
| 657 | <img src="https://artificialanalysis.ai/img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM3-VL-2B | 0.0083 | 1,550.62 | 0.2976 | ❌ |
| 658 | <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 270M | 0.0000 | — | — | — |

## 品牌帕累托前沿连线（仅体现在图中）

以下 12 个品牌在图中拥有单独的帕累托连线（较窄宽度，品牌主题色，图层高于总体灰色连线）。表中数量为**入图顶点数**——品牌前沿上低于总体前沿第一级的顶点同样不入图（本表与图例一致）：

| 品牌 | 主题色 | 品牌前沿模型数（入图） |
|------|--------|--------------|
| <img src="https://artificialanalysis.ai/img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | `#cc785c` | 15 |
| <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | `#34A853` | 6 |
| <img src="https://artificialanalysis.ai/img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | `#1f1f1f` | 16 |
| <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | `#2243e6` | 4 |
| <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | `#1521a9` | 1 |
| <img src="https://artificialanalysis.ai/img/logos/meta.svg" width="18" alt="Meta" /> Meta | `#0089f4` | 5 |
| <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | `#047AFE` | 6 |
| <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | `#ff7018` | 11 |
| <img src="https://artificialanalysis.ai/img/logos/sapiens.svg" width="18" alt="Sapiens AI" /> Sapiens AI | `#1521a9` | 1 |
| <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | `#736cd3` | 5 |
| <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | `#ff6900` | 2 |
| <img src="https://artificialanalysis.ai/img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | `#EB3568` | 2 |

## 基准测试动态标定（Leave-One-Out Calibration）

不同基准测试的参测模型群体能力分布存在差异（例如部分高难度或专业领域基准测试仅覆盖头部高能力模型）。系统在标准归一化之后执行了**留一交叉动态映射标定流程**：

1. **排除单项基准**：暂时排除某项基准测试，计算各模型在其余测试项上的平均能力；
2. **全域归一化评估**：将排除后的平均能力归一化至 `[0, 1]`；
3. **锁定参测区间**：提取实际参测该基准测试的所有模型，以它们排除该项后的能力最高值和最低值分别作为该项的新映射上界和下界；
4. **并行同步迭代**：所有基准测试以 `[0, 1]` 为初值同步更新，完成一轮后以新上下界作为输入进入下一轮，重复迭代直至收敛。

> 标定状态：已完成 **24** 轮并行迭代收敛（容差阈值 $\Delta < 1e-05$）。标定得到的数据作为新指标独立保存，不覆盖原始基准测试归一化与综合能力。

| 基准测试项 | 英文标识 | 参测模型数 | 标定映射下界 | 标定映射上界 | 映射跨度 |
| :--- | :--- | :---: | :---: | :---: | :---: |
| AA Intelligence Index | `intelligenceIndex` | 155 | `0.0868` | `1.0000` | `0.9132` |
| GPQA Diamond | `gpqa` | 543 | `0.0000` | `0.9101` | `0.9101` |
| Humanity's Last Exam | `hle` | 619 | `0.0000` | `1.0000` | `1.0000` |
| HLE Diamond | `hleDiamond` | 196 | `0.0855` | `1.0000` | `0.9145` |
| CritPt Physics | `critpt` | 599 | `0.0000` | `1.0000` | `1.0000` |
| CritPt v2 Hard | `critptV2Hard` | 159 | `0.0876` | `1.0000` | `0.9124` |
| AIME 2025 | `aime2025` | 268 | `0.0000` | `0.7177` | `0.7177` |
| SciCode Coding | `scicode` | 253 | `0.0876` | `1.0000` | `0.9124` |
| LiveCodeBench | `livecodebench` | 278 | `0.0000` | `0.7175` | `0.7175` |
| FrontierCode 1.1 | `frontiercode` | 83 | `0.1348` | `1.0000` | `0.8652` |
| FrontierCode 2.0 | `frontiercode20` | 156 | `0.0876` | `1.0000` | `0.9124` |
| Terminal-Bench Hard | `terminalbenchHard` | 432 | `0.0000` | `0.8424` | `0.8424` |
| Terminal-Bench 2.1 | `terminalbenchV21` | 243 | `0.0621` | `0.9098` | `0.8477` |
| Terminal-Bench 4.0 | `terminalbenchV40` | 280 | `0.0872` | `1.0000` | `0.9128` |
| Terminal-Bench Science | `terminalbenchScience` | 167 | `0.0874` | `1.0000` | `0.9126` |
| τ²-Bench Telecom | `tau2` | 439 | `0.0000` | `0.8500` | `0.8500` |
| τ³-Bench Banking | `tauBanking` | 210 | `0.0644` | `0.9147` | `0.8503` |
| AutomationBench-AA | `automationbench` | 284 | `0.0875` | `1.0000` | `0.9125` |
| AA-Briefcase v1.1 | `briefcase` | 291 | `0.0876` | `1.0000` | `0.9124` |
| GDPval-AA Normalized | `gdpvalNormalized` | 318 | `0.0625` | `1.0000` | `0.9375` |
| GDP.pdf | `gdpPdf` | 283 | `0.0854` | `1.0000` | `0.9146` |
| AA-LCR Long Context | `lcr` | 597 | `0.0000` | `1.0000` | `1.0000` |
| MLCR Medical Long Context | `mlcr` | 194 | `0.1254` | `1.0000` | `0.8746` |
| MMMU Pro | `mmmuPro` | 306 | `0.0127` | `0.9369` | `0.9242` |
| Code2Video-AA | `code2video` | 28 | `0.4238` | `0.9113` | `0.4875` |
| AA-3D | `aa3d` | 27 | `0.4245` | `1.0000` | `0.5755` |
| AA Omniscience Index | `omniscience` | 169 | `0.0822` | `1.0000` | `0.9178` |
| AA-Omniscience Accuracy | `omniscienceAccuracy` | 169 | `0.0873` | `1.0000` | `0.9127` |
| AA-Omniscience Non-Hallucination | `omniscienceNonHallucination` | 169 | `0.0729` | `1.0000` | `0.9271` |
| IFBench Instruction Following | `ifbench` | 449 | `0.0000` | `0.8552` | `0.8552` |
| AA Analyst Agent | `analystAgent` | 63 | `0.2530` | `0.9328` | `0.6798` |
| APEX-Agents-AA | `apexAgents` | 34 | `0.3007` | `0.8069` | `0.5063` |
| EnterpriseOps-Gym-AA | `enterpriseOps` | 62 | `0.2682` | `0.9575` | `0.6893` |
| ITBench-SRE | `itbenchSre` | 45 | `0.1559` | `0.9211` | `0.7652` |
| Harvey LAB-AA | `harveyLab` | 44 | `0.4365` | `1.0000` | `0.5635` |
| HealthBench | `healthbench` | 29 | `0.6403` | `1.0000` | `0.3597` |
| HealthBench Professional | `healthbenchProfessional` | 19 | `0.6391` | `1.0000` | `0.3609` |
| VIALS-AA / MKA | `vials` | 26 | `0.4905` | `1.0000` | `0.5095` |


## 评分方法

1. **38项全域评估指标**各自线性归一化到 [0,1]
   （AA Intelligence Index、GPQA Diamond、Humanity's Last Exam、HLE Diamond、CritPt Physics、CritPt v2 Hard、AIME 2025、SciCode Coding、LiveCodeBench、FrontierCode 1.1、FrontierCode 2.0、Terminal-Bench Hard、Terminal-Bench 2.1、Terminal-Bench 4.0、Terminal-Bench Science、τ²-Bench Telecom、τ³-Bench Banking、AutomationBench-AA、AA-Briefcase v1.1、GDPval-AA Normalized、GDP.pdf、AA-LCR Long Context、MLCR Medical Long Context、MMMU Pro、Code2Video-AA、AA-3D、AA Omniscience Index、AA-Omniscience Accuracy、AA-Omniscience Non-Hallucination、IFBench Instruction Following、AA Analyst Agent、APEX-Agents-AA、EnterpriseOps-Gym-AA、ITBench-SRE、Harvey LAB-AA、HealthBench、HealthBench Professional、VIALS-AA / MKA）
   > 全域基准升级：收录全部 38 项基准测试，涵盖通用推理 (AA Intelligence Index, HLE, HLE Diamond, GPQA Diamond)、数理逻辑 (CritPt, CritPt v2 Hard, AIME 2025)、代码编程 (LiveCodeBench, SciCode, FrontierCode 1.1/2.0)、Agent 智能体 (Terminal-Bench 系列, τ-Bench 系列, AutomationBench, Briefcase, ITBench-SRE, Harvey LAB, HealthBench)、多模态 (MMMU Pro, Code2Video, AA-3D, VIALS)、长上下文 (AA-LCR, MLCR, GDP.pdf) 及事实性 (Omniscience 系列, IFBench) 等核心维度。
2. **综合能力值** = 所有有效归一化分数的算术平均
3. **综合能力再归一化**：线性映射到 [0,1]，性能最好的模型 = 1，最差的模型 = 0
4. **Pareto前沿** = 不被任何其他模型支配的模型（综合能力 ≥ 且成本 ≤，且至少一项严格更优；成本为 0 的免费模型同样参与——横轴左端恒为 0，免费模型是合法前沿候选）
5. **模型范围** = Status: All（含已弃用模型；缺少足够评估数据者不参与排名）
6. **图表纵轴基线（V17）**：图表的 y = 0 取总体帕累托前沿的第一级（最低能力；本例 y0 = 0.4575，即前沿左端点 K2 Horizon 375B A23B）；综合能力低于该级的模型不出现在图表中（表格不受影响）。图中纵坐标 chart_y = (能力 - y0)/(1 - y0)，因此前沿左端点恰好落在 (0, 0)、最优模型恰好为 y = 1。该过滤在横轴映射构建之前完成


## 模型系列层级与单调性评分引擎（Model Hierarchy & Monotonic Scoring Engine）

为解决多基准评估中由于各模型参测项不齐、评测噪声以及偶然波动导致的反直觉能力倒挂（例如同一系列同版本高阶模型得分低于低阶模型、同一系列同等级新版本低于旧版本、同一模型高思考程度低于低思考程度、同代更新快照后出版本低于先出版本），系统在 `src/hierarchy.py` 中实现了**分厂商系列层级网格（Vendor Series Hierarchy Grids）与严格单调约束 Dykstra 等保投影（Isotonic Projection）评分引擎**：

### 1. 厂商与系列隔离（Series Isolation）
系统维护了覆盖全部主流与新兴厂商的 **84 个系列层级网格**（保存在 `output/model_hierarchy/` 目录下的 CSV 文件中），每个系列维护二维网格：
- **行（Tiers）**：性能层级（如 Tier 1 Flagship / Large、Tier 2 Medium / MoE、Tier 3 Small / Fast、Tier 4 Compact / Nano）
- **列（Versions）**：架构代际与版本演进（从旧到新按时间列排布）
- **严格系列隔离**：不同系列（例如 OpenAI 的 `GPT` 系列与 `o` 推理系列、Google 的 `Gemini` 与 `Gemma` 开源系列、Meta 的 `Llama` 与 `Muse` 系列）物理隔离，绝不产生跨系列强行绑定的单调性约束。

### 2. 四大严格单调序规则（Strict Monotonic Ordering Rules）
在系列网格与模型元数据基础上，自动生成有向无环约束图（DAG，$S(u) \ge S(v)$）：
- **Rule 1（同系列同版本，高等级 $\ge$ 低等级）**：同一系列、同一版本列内，高行 Tier 模型能力必须大于等于低行 Tier 模型的所有快照与变体（支持思考程度对齐匹配）。
- **Rule 2（同系列同等级，新版本 $\ge$ 旧版本）**：同一系列、同一等级行内，新版本列模型能力必须大于等于旧版本列模型。
- **Rule 3（同模型基座，高思考程度 $\ge$ 低思考程度）**：同一基座模型，高思考算力档位能力必须大于等于低思考算力档位（$\text{max} > \text{xhigh} > \text{high} > \text{medium} > \text{low} > \text{minimal} > \text{non-reasoning}$）。
- **Rule 4（同模型主干，新日期快照 $\ge$ 旧日期快照）**：同一模型主干内，后发布的日期快照能力大于等于先发布的快照（如 GPT-4o Nov $\ge$ Aug $\ge$ May，Claude 3.5 Sonnet Oct $\ge$ June，DeepSeek V4 Pro 0813 $\ge$ 0424）。

### 3. 去偏隐能力估计与 Dykstra 等保投影（Isotonic Projection）
- **留一标定动态去偏**：首先通过动态留一交叉标定（Leave-One-Out Scaling）消除不同评测项覆盖群体的难度偏差；
- **Dykstra 凸优化投影**：针对多变量交织的庞大约束集合，采用 Dykstra 循环 Bregman 投影算法寻找满足全部单调性条件的最近凸解：
  $$\min_{\mathbf{s} \in \mathcal{K}} \|\mathbf{s} - \mathbf{s}_0\|_2^2 \quad \text{s.t.} \quad s_u \ge s_v \quad \forall (u,v) \in \mathcal{E}$$
- **实测结果**：在 723 个参测模型、4,579 条强约束条件下，达成 **100.00% 约束满足率（0 违背项）**。详见 [层级诊断报告](output/model_hierarchy/hierarchy_score_report.md) 与 [层级分析结果](output/hierarchy_analysis_results.json)。

### 4. 人工校验与 CSV 双向工作流（Calibration & Diff Workflow）
全部 84 个系列层级网格均以易于阅读与编辑的标准 2D CSV 存储于 `output/model_hierarchy/`。
- **导出与查看**：运行 `python src/hierarchy.py` 会导出全部单独 CSV 及汇总表 `all_vendors_hierarchy.csv`；
- **自定义层级微调**：用户可直接用 Excel 或文本编辑器修改任意系列 CSV（例如调整某些新模型的归属代际或层级）；
- **差异审查与校验**：运行 `python src/hierarchy.py --diff <SeriesName>` 或 `--diff all`，系统会自动将本地修改与默认预置层级进行三向比对，报告所有变更并校验单调性。


## 横轴映射（对数映射，真零点，V21）与分布分析

横轴（单请求成本）为 **Y = A·ln(B·c+C)+D 对数映射**（B = 1；A、D 由端点解出；C = 108.16，r = B/C = 0.00924585 经网格搜索确定）：

```
x = 0                            当 c = 0（免费模型，真零点）
x = A·ln(c+C)+D                  当 c > 0（B = 1 并入；A、D 由端点解出）
```

其中 C = 108.16（r = B/C = 0.00924585），拟合集为 11 品牌前沿入图正成本模型（综合能力 ≥ 前沿第一级）的成本分布，目标为组内名次分位数（最小二乘误差 mse = 0.014781，最大偏离 0.2065）。该映射在 **y 基线过滤之后**构建（V17：先以帕累托前沿第一级为 y = 0、剔除低性能模型，再对入图模型建映射）。

**该映射保证：**

- **函数端点严格钉死**：c = 0 → x = 0；最大成本 → x = 1——函数经过 (0,0) 与 (1,1)；
- 各数量级区间的入图模型数：1–10: 0，10–100: 0，100–1k: 7，1k–10k: 87，10k–100k: 143，100k–1M: 20，1M–1.043M: 1
- **同倍率区间宽度相近**（对数轴性质）：1k→10k 与 100k→1M 同为 10 倍率，宽度相近（前者 87 个模型、后者 20 个）；与 V17 分位数映射不同，本图不追求均匀密度——密度不等如实显示；
- **左端恒为 0**（c = 0；1 个免费模型位于最左缘）
- 前沿最低正成本 430.24 → x = 0.1750（真实对数位置，不再钉 0；x = 0 恒为 c = 0 免费模型）；前沿最大成本 1,042,888 → x = 1.0000（= 1；高于前沿最大成本的模型不入图，仅表格保留）
- 中位数位置 0.531（≈ 0.5 居中）；左右两半模型数：左 100 / 右 159
- 横轴十分位模型数：1，5，15，27，52，75，53，20，5，6（对数映射下各十分位模型数自然不等）
- **10^x 数量级指示**（位置 = x(10^x)）：10^0 → 0.001，10^1 → 0.010，10^2 → 0.071，10^3 → 0.254，10^4 → 0.495，10^5 → 0.745，10^6 → 0.995

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
**模型总数（Status: All）**: 658 个参与排名（共抓取 763 个模型，另有模型因评估数据不足未列入；总体帕累托前沿 12 个；图表入图 259 个——综合能力 ≥ 前沿第一级）  

**技术架构与更新流程：**
1. **高速数据抓取 (`src/scrape.py`)**：解析 Artificial Analysis 的 Next.js RSC 动态清单（Manifest），通过 AES-GCM 快速解密全量模型数据集，解压缩 GZip 流并解析嵌套的 38 项基准维度分数与发布时间；
2. **缓存命中率抓取 (`src/cache_hit_rate.py`)**：通过 Playwright 抓取 Coding Agents 页面的全局均值作为成本公式参数；
3. **帕累托与图表分析 (`src/analyze.py`)**：执行动态留一标定、成本计算、真零点对数坐标映射与多品牌前沿图表绘制；
4. **模型层级单调性引擎 (`src/hierarchy.py`)**：基于 84 个系列层级网格（Tiers x Versions）执行 4 大单调序规则与 Dykstra 等保投影校验；
5. **自动化 GitHub Actions (`.github/workflows/update-leaderboard.yml`)**：每日定时及手动触发运行抓取、层级计算、单元测试验证与看板自动更新。


## 图表说明（黑底）

（V17 起本说明置于文末，图表之后直接跟随模型表格。）

图表说明：**灰色实线** = 总体帕累托前沿；**彩色细线** = 选定品牌的单独帕累托前沿（共 12 个品牌，（品牌主题色，图层高于总体连线；暗色品牌元素带窄白边；顶点按（横轴位置、能力升序）连接，等成本点自下而上）；品牌前沿模型圆点同样使用品牌颜色。模型名称/思考程度标注优先骑在连线之上（点的左/右两侧皆可，同一条线段可容纳两个标签——各贴各的点；文字与连线平行、中轴线重合，连线仅在文字两侧绘制）；骑线位被其他标签占据时自动「让位」——占用者挪到自己的另一个骑线位，双方都保持骑线；实在骑不上线时按四级优先依次退让（V16）：离点最近位置的上方/下方平行偏移 → 点的两条连线延长线上就近 → 两连线夹角扇区内就近。标签规则（V13/V15）：品牌前沿模型共享的前导块按「最长有效切点」剔除 —— 切点止于分界符，或止于字母且其后紧跟数字（如 Claude Opus 5 → Opus 5、GPT-5.6 Sol → 5.6 Sol、Kimi K2.6 → 2.6、Qwen3.8 Max → 3.8 Max、MiMo-V2.5 → 2.5、MiniMax-M2.1 → 2.1）；(non-reasoning) 简写为 (non)；同一模型在品牌连线上相邻出现 2 次以上时仅性能最低者保留全名、相邻较高者只标思考程度，不相邻的重复出现保留全名（每次重新计算）；标签位置与序列同向（V15）——品牌前沿上越靠右上的模型，其标签重心必须同时更靠右且更靠上（两分量都 >= 0，至少是 (0,0)，仅其一非负不算合格；初始放置违反时自动就近重摆，单标签无解（被前后邻居夹死）时按窗口级联重排整体挪动，均不产生新的重叠）。纵轴 y = 0 = 总体帕累托前沿第一级（y0 = 0.4575，前沿左端点 K2 Horizon 375B A23B 恰为 (0,0)），能力低于该级的 325 个模型、缺少成本数据的 74 个模型与成本高于品牌前沿最大值的模型不出现在图中；横轴为对数映射（见上文「横轴映射」节），10^x 数量级指示位于 x(10^x)，同一倍率区间的宽度相近（对数轴性质；本图不追求均匀密度）。
