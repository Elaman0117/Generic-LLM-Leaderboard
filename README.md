# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

图表说明（黑底）：**灰色实线** = 总体帕累托前沿；**彩色细线** = 十一个品牌的单独帕累托前沿（品牌主题色，图层高于总体连线；暗色品牌元素带窄白边；顶点按（横轴位置、能力升序）连接，等成本点自下而上）；品牌前沿模型圆点同样使用品牌颜色。模型名称/思考程度标注优先骑在连线之上（点的左/右侧皆可，同一条线段可容纳两个标签——各贴各的点；文字与连线平行、中轴线重合，连线仅在文字两侧绘制）；骑线位被其他标签占据时自动「让位」——占用者挪到自己的另一个骑线位，双方都保持骑线；实在骑不上线时按四级优先依次退让（V16）：离点最近位置的上方/下方平行偏移 → 点的两条连线延长线上就近 → 两连线夹角扇区内就近。标签规则（V13/V15）：品牌前沿模型共享的前导块按「最长有效切点」剔除 —— 切点止于分界符，或止于字母且其后紧跟数字（如 Claude Opus 5 → Opus 5、GPT-5.6 Sol → 5.6 Sol、Kimi K2.6 → 2.6、Qwen3.8 Max → 3.8 Max、MiMo-V2.5 → 2.5、MiniMax-M2.1 → 2.1）；(non-reasoning) 简写为 (non)；同一模型在品牌连线上相邻出现 2 次以上时仅性能最低者保留全名、相邻较高者只标思考程度，不相邻的重复出现保留全名（每次重新计算）；标签位置与序列同向（V15）——品牌前沿上越靠右上的模型，其标签重心必须同时更靠右且更靠上（两分量都 >= 0，至少是 (0,0)，仅其一非负不算合格；初始放置违反时自动就近重摆，单标签无解（被前后邻居夹死）时按窗口级联重排整体挪动，均不产生新的重叠）。横轴为 logistic 单函数映射（函数式见下文），10^x 数量级指示位于 x(10^x)。

## 全部模型（综合能力从高到低，最优 = 1，最差 = 0）

共收录 **Status: All**（含已弃用）的全部模型；按重新归一化后的综合能力排序。「帕累托」列：✅ = 总体帕累托前沿模型，❌ = 被支配，— = 无成本数据无法判定。

| # | 品牌 | 模型 | 综合能力 | 单请求成本 | 横轴位置 | 帕累托 |
|---|------|------|---------|-----------|-----------|------|
| 1 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (max with fallback) | 1.0000 | 1,002,731.22 | 0.9938 | ✅ |
| 2 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (xhigh with fallback) | 0.9934 | 399,102.29 | 0.9850 | ✅ |
| 3 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (max) | 0.9902 | 939,824.86 | 0.9934 | ❌ |
| 4 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (xhigh) | 0.9854 | 471,868.99 | 0.9872 | ❌ |
| 5 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (high) | 0.9706 | 180,084.33 | 0.9684 | ✅ |
| 6 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5 (with fallback) | 0.9681 | 286,480.11 | 0.9795 | ❌ |
| 7 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (max) | 0.9650 | 144,452.29 | 0.9612 | ✅ |
| 8 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (high with fallback) | 0.9627 | 97,943.37 | 0.9445 | ✅ |
| 9 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (medium) | 0.9558 | 54,946.18 | 0.9071 | ✅ |
| 10 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (xhigh) | 0.9526 | 58,222.52 | 0.9117 | ❌ |
| 11 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (max) | 0.9375 | 213,536.12 | 0.9730 | ❌ |
| 12 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (high) | 0.9341 | 49,251.23 | 0.8978 | ✅ |
| 13 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (medium with fallback) | 0.9307 | 61,307.78 | 0.9156 | ❌ |
| 14 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.3 (xhigh) | 0.9238 | 12,935.13 | 0.7080 | ✅ |
| 15 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.3 (max) | 0.9232 | 12,935.13 | 0.7080 | ❌ |
| 16 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (low) | 0.9217 | 49,610.44 | 0.8984 | ❌ |
| 17 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3 (max) | 0.9004 | 42,488.50 | 0.8840 | ❌ |
| 18 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (medium) | 0.8996 | 29,799.80 | 0.8441 | ❌ |
| 19 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (low with fallback) | 0.8984 | 53,049.44 | 0.9042 | ❌ |
| 20 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (xhigh) | 0.8946 | 81,294.98 | 0.9343 | ❌ |
| 21 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (xhigh) | 0.8810 | 23,544.28 | 0.8119 | ❌ |
| 22 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (xhigh) | 0.8782 | 180,181.64 | 0.9684 | ❌ |
| 23 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.8 (max) | 0.8772 | 52,078.41 | 0.9026 | ❌ |
| 24 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (high) | 0.8758 | 29,881.17 | 0.8445 | ❌ |
| 25 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (high) | 0.8753 | 22,425.70 | 0.8046 | ❌ |
| 26 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (high) | 0.8738 | 17,676.75 | 0.7661 | ❌ |
| 27 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (medium) | 0.8694 | 20,219.89 | 0.7885 | ❌ |
| 28 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (max) | 0.8620 | 221,409.41 | 0.9739 | ❌ |
| 29 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (high) | 0.8619 | 53,807.82 | 0.9054 | ❌ |
| 30 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3 (max) | 0.8534 | 14,439.59 | 0.7294 | ❌ |
| 31 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (medium) | 0.8504 | 24,124.68 | 0.8155 | ❌ |
| 32 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.2 (xhigh) | 0.8493 | 12,935.13 | 0.7080 | ❌ |
| 33 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (high) | 0.8447 | 13,899.17 | 0.7221 | ❌ |
| 34 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (medium) | 0.8379 | — | — | — |
| 35 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (low) | 0.8339 | 25,046.96 | 0.8208 | ❌ |
| 36 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (Non-reasoning) | 0.8319 | — | — | — |
| 37 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.5 (high) | 0.8263 | 10,763.82 | 0.6702 | ✅ |
| 38 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.7 (max) | 0.8258 | 44,966.82 | 0.8895 | ❌ |
| 39 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 Max | 0.8237 | 18,788.84 | 0.7765 | ❌ |
| 40 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.1 Pro Preview | 0.8229 | 48,652.75 | 0.8967 | ❌ |
| 41 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash | 0.8210 | 38,963.77 | 0.8752 | ❌ |
| 42 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (medium) | 0.8209 | 40,533.90 | 0.8793 | ❌ |
| 43 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (max) | 0.8186 | 150,559.31 | 0.9626 | ❌ |
| 44 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.2 (max) | 0.8168 | 14,439.59 | 0.7294 | ❌ |
| 45 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (xhigh) | 0.8155 | 39,625.25 | 0.8769 | ❌ |
| 46 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (xhigh) | 0.8129 | 265,769.10 | 0.9780 | ❌ |
| 47 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (medium) | 0.8096 | 8,399.36 | 0.6154 | ✅ |
| 48 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 2.4T A95B | 0.8094 | 18,788.84 | 0.7765 | ❌ |
| 49 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.1 (xhigh) | 0.8023 | — | — | — |
| 50 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (medium) | 0.7981 | 36,094.32 | 0.8669 | ❌ |
| 51 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.3 Codex (xhigh) | 0.7977 | 130,438.30 | 0.9573 | ❌ |
| 52 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3-Flash | 0.7971 | 1,601.32 | 0.2450 | ✅ |
| 53 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (low) | 0.7939 | 20,750.03 | 0.7926 | ❌ |
| 54 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.7 Max | 0.7908 | 28,290.47 | 0.8374 | ❌ |
| 55 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.6 Flash | 0.7846 | 15,621.02 | 0.7441 | ❌ |
| 56 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (high) | 0.7765 | 12,562.04 | 0.7022 | ❌ |
| 57 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (max) | 0.7620 | 23,543.09 | 0.8119 | ❌ |
| 58 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (low) | 0.7617 | 3,799.97 | 0.4272 | ❌ |
| 59 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8-Flash-Next | 0.7592 | 1,433.69 | 0.2258 | ✅ |
| 60 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (low) | 0.7567 | — | — | — |
| 61 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.6 (max) | 0.7548 | 44,431.44 | 0.8883 | ❌ |
| 62 | <img src="https://artificialanalysis.ai/img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M3 | 0.7512 | 3,831.99 | 0.4291 | ❌ |
| 63 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 v2 | 0.7505 | 9,065.60 | 0.6327 | ❌ |
| 64 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark | 0.7418 | — | — | — |
| 65 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.6 | 0.7412 | 21,985.82 | 0.8016 | ❌ |
| 66 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3 Pro Preview (high) | 0.7393 | — | — | — |
| 67 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (low) | 0.7365 | 11,606.02 | 0.6860 | ❌ |
| 68 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (medium) | 0.7362 | 7,372.20 | 0.5853 | ❌ |
| 69 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (xhigh) | 0.7358 | 32,282.29 | 0.8540 | ❌ |
| 70 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro 0813 (max) | 0.7343 | 11,279.75 | 0.6800 | ❌ |
| 71 | <img src="https://artificialanalysis.ai/img/logos/sapiens.svg" width="18" alt="Sapiens AI" /> Sapiens AI | Agnes 2.5 Pro Beta | 0.7290 | — | — | — |
| 72 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (xhigh) | 0.7282 | 8,373.02 | 0.6147 | ❌ |
| 73 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (xhigh) | 0.7262 | 102,669.39 | 0.9469 | ❌ |
| 74 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 Codex (xhigh) | 0.7255 | — | — | — |
| 75 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 Max Preview | 0.7240 | 21,901.04 | 0.8010 | ❌ |
| 76 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (low) | 0.7230 | 26,917.05 | 0.8308 | ❌ |
| 77 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (high) | 0.7183 | 10,293.39 | 0.6606 | ❌ |
| 78 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (max) | 0.7162 | 105,636.73 | 0.9482 | ❌ |
| 79 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3 Flash | 0.7142 | 5,872.75 | 0.5314 | ❌ |
| 80 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.5 | 0.7106 | 41,756.94 | 0.8823 | ❌ |
| 81 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 | 0.7103 | — | — | — |
| 82 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (medium) | 0.7087 | 11,753.75 | 0.6886 | ❌ |
| 83 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.7 (Non-reasoning, high) | 0.7061 | 23,234.06 | 0.8099 | ❌ |
| 84 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.7 Plus | 0.7042 | 4,738.78 | 0.4798 | ❌ |
| 85 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 Plus | 0.7013 | 19,073.48 | 0.7790 | ❌ |
| 86 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (max) | 0.7012 | 4,594.97 | 0.4724 | ❌ |
| 87 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (high) | 0.6984 | 3,270.38 | 0.3922 | ❌ |
| 88 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.1 | 0.6955 | 22,172.69 | 0.8029 | ❌ |
| 89 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (high) | 0.6918 | 13,684.23 | 0.7191 | ❌ |
| 90 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (xhigh) | 0.6912 | 8,331.42 | 0.6136 | ❌ |
| 91 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash Vision (max) | 0.6902 | 3,753.74 | 0.4243 | ❌ |
| 92 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash 0731 (max) | 0.6894 | 3,753.74 | 0.4243 | ❌ |
| 93 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (low) | 0.6876 | 14,334.88 | 0.7281 | ❌ |
| 94 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 (high) | 0.6798 | 54,031.25 | 0.9057 | ❌ |
| 95 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (low) | 0.6781 | 5,476.56 | 0.5146 | ❌ |
| 96 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Pro | 0.6764 | — | — | — |
| 97 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (high) | 0.6728 | 2,521.76 | 0.3344 | ❌ |
| 98 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5-Pro | 0.6727 | 2,528.72 | 0.3350 | ❌ |
| 99 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (xhigh) | 0.6708 | 141,123.86 | 0.9603 | ❌ |
| 100 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (medium) | 0.6707 | — | — | — |
| 101 | <img src="https://artificialanalysis.ai/img/logos/motif_small.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif 3 | 0.6690 | — | — | — |
| 102 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.7 Code | 0.6663 | 13,375.73 | 0.7147 | ❌ |
| 103 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3 (low) | 0.6606 | 42,488.50 | 0.8840 | ❌ |
| 104 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 Codex (high) | 0.6571 | — | — | — |
| 105 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok Build 0.1 0616 | 0.6569 | 7,589.19 | 0.5921 | ❌ |
| 106 | <img src="https://artificialanalysis.ai/img/logos/mbzuai_small.svg" width="18" alt="MBZUAI Institute of Foundation Models" /> MBZUAI Institute of Foundation Models | K2 Horizon 375B A23B | 0.6555 | — | — | — |
| 107 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5 | 0.6520 | 14,125.19 | 0.7252 | ❌ |
| 108 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Ultra | 0.6518 | 9,509.59 | 0.6433 | ❌ |
| 109 | <img src="https://artificialanalysis.ai/img/logos/thinking_machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling Small | 0.6491 | 3,776.76 | 0.4257 | ❌ |
| 110 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5 | 0.6487 | 829.05 | 0.1469 | ✅ |
| 111 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (low) | 0.6460 | 11,481.24 | 0.6837 | ❌ |
| 112 | <img src="https://artificialanalysis.ai/img/logos/thinking_machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling | 0.6434 | 12,436.28 | 0.7001 | ❌ |
| 113 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 Codex (high) | 0.6387 | — | — | — |
| 114 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (high) | 0.6329 | 69,117.88 | 0.9241 | ❌ |
| 115 | <img src="https://artificialanalysis.ai/img/logos/apodex.svg" width="18" alt="Apodex" /> Apodex | Apodex 1.1 | 0.6322 | — | — | — |
| 116 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (max) | 0.6310 | — | — | — |
| 117 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Omni-0327 | 0.6288 | — | — | — |
| 118 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (medium) | 0.6266 | 34,134.77 | 0.8606 | ❌ |
| 119 | <img src="https://artificialanalysis.ai/img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 4 | 0.6242 | 3,776.76 | 0.4257 | ❌ |
| 120 | <img src="https://artificialanalysis.ai/img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.7 | 0.6219 | 4,386.39 | 0.4613 | ❌ |
| 121 | <img src="https://artificialanalysis.ai/img/logos/nex_small.svg" width="18" alt="Nex AGI" /> Nex AGI | Nex-N2-Pro | 0.6211 | 8,934.12 | 0.6294 | ❌ |
| 122 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.6 (Non-reasoning, high) | 0.6196 | 23,705.34 | 0.8129 | ❌ |
| 123 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5-Turbo | 0.6192 | — | — | — |
| 124 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.5 | 0.6174 | — | — | — |
| 125 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 | 0.6172 | — | — | — |
| 126 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 27B | 0.6139 | 22,675.49 | 0.8063 | ❌ |
| 127 | <img src="https://artificialanalysis.ai/img/logos/motif_small.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif 3 (Beta) | 0.6083 | — | — | — |
| 128 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 Instant (May 2026) | 0.6079 | — | — | — |
| 129 | <img src="https://artificialanalysis.ai/img/logos/multiversecomputing_small.svg" width="18" alt="Multiverse Computing" /> Multiverse Computing | Quasar 438B (max) | 0.6062 | 4,941.89 | 0.4899 | ❌ |
| 130 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Opus | 0.6052 | — | — | — |
| 131 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (xhigh) | 0.6037 | 14,644.55 | 0.7321 | ❌ |
| 132 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (high) | 0.6025 | — | — | — |
| 133 | <img src="https://artificialanalysis.ai/img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Open2 250B | 0.6021 | — | — | — |
| 134 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 397B A17B | 0.5995 | 13,711.49 | 0.7195 | ❌ |
| 135 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash-Lite | 0.5985 | 9,618.65 | 0.6458 | ❌ |
| 136 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Sonnet | 0.5978 | 20,524.46 | 0.7909 | ❌ |
| 137 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (minimal) | 0.5976 | 8,661.29 | 0.6224 | ❌ |
| 138 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 27B | 0.5961 | 6,220.94 | 0.5451 | ❌ |
| 139 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash (Feb 2026) | 0.5958 | — | — | — |
| 140 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (medium) | 0.5952 | 1,275.76 | 0.2068 | ❌ |
| 141 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (Non-reasoning) | 0.5951 | 9,230.49 | 0.6367 | ❌ |
| 142 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Omni | 0.5942 | — | — | — |
| 143 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o3 | 0.5929 | 17,137.70 | 0.7607 | ❌ |
| 144 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM 5V Turbo | 0.5896 | — | — | — |
| 145 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (medium) | 0.5865 | 9,463.53 | 0.6422 | ❌ |
| 146 | <img src="https://artificialanalysis.ai/img/logos/tencent_small.svg" width="18" alt="Tencent" /> Tencent | Hy3 | 0.5859 | 1,800.12 | 0.2664 | ❌ |
| 147 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 35B A3B | 0.5854 | 13,539.93 | 0.7170 | ❌ |
| 148 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (medium) | 0.5835 | 3,683.91 | 0.4199 | ❌ |
| 149 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.1 Opus | 0.5813 | — | — | — |
| 150 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (Non-reasoning, high) | 0.5800 | 14,238.78 | 0.7268 | ❌ |
| 151 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 Thinking | 0.5790 | 6,691.89 | 0.5625 | ❌ |
| 152 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.5 (Non-reasoning) | 0.5773 | 23,243.69 | 0.8100 | ❌ |
| 153 | <img src="https://artificialanalysis.ai/img/logos/sktelecom_small.svg" width="18" alt="SK Telecom" /> SK Telecom | A.X-K2 | 0.5766 | — | — | — |
| 154 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (Non-reasoning, low) | 0.5742 | 14,037.88 | 0.7240 | ❌ |
| 155 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (Non-reasoning) | 0.5729 | 19,044.70 | 0.7787 | ❌ |
| 156 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.6 (Non-reasoning) | 0.5721 | 4,710.23 | 0.4783 | ❌ |
| 157 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3 Pro Preview (low) | 0.5716 | — | — | — |
| 158 | <img src="https://artificialanalysis.ai/img/logos/sapiens.svg" width="18" alt="Sapiens AI" /> Sapiens AI | Agnes 2.5 Pro Alpha | 0.5663 | 2,674.05 | 0.3471 | ❌ |
| 159 | <img src="https://artificialanalysis.ai/img/logos/kwaikat_small.svg" width="18" alt="KwaiKAT" /> KwaiKAT | KAT-Coder-Pro V2 | 0.5623 | — | — | — |
| 160 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 Codex mini (high) | 0.5622 | — | — | — |
| 161 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (high) | 0.5609 | 15,420.95 | 0.7417 | ❌ |
| 162 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (low) | 0.5607 | 8,331.42 | 0.6136 | ❌ |
| 163 | <img src="https://artificialanalysis.ai/img/logos/china_mobile_small.png" width="18" alt="China Mobile" /> China Mobile | JT-4.1 Flash 236B A21B | 0.5593 | — | — | — |
| 164 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (low) | 0.5591 | 12,585.77 | 0.7026 | ❌ |
| 165 | <img src="https://artificialanalysis.ai/img/logos/tencent_small.svg" width="18" alt="Tencent" /> Tencent | Hy3-preview | 0.5587 | — | — | — |
| 166 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 122B A10B | 0.5585 | 8,294.59 | 0.6126 | ❌ |
| 167 | <img src="https://artificialanalysis.ai/img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step 3.7 Flash | 0.5556 | 3,392.84 | 0.4007 | ❌ |
| 168 | <img src="https://artificialanalysis.ai/img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.5 | 0.5528 | 3,554.09 | 0.4115 | ❌ |
| 169 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.1 (Non-reasoning) | 0.5526 | 5,958.33 | 0.5348 | ❌ |
| 170 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (Non-reasoning) | 0.5525 | 25,542.19 | 0.8236 | ❌ |
| 171 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7 | 0.5519 | 11,500.00 | 0.6841 | ❌ |
| 172 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 Omni Plus | 0.5514 | 3,631.85 | 0.4165 | ❌ |
| 173 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (medium) | 0.5471 | 8,331.42 | 0.6136 | ❌ |
| 174 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (low) | 0.5459 | 1,207.32 | 0.1982 | ❌ |
| 175 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.1 Fast | 0.5445 | — | — | — |
| 176 | <img src="https://artificialanalysis.ai/img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | G9v3-39A5B | 0.5390 | — | — | — |
| 177 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano | 0.5384 | 2,047.98 | 0.2914 | ❌ |
| 178 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max Thinking | 0.5378 | — | — | — |
| 179 | <img src="https://artificialanalysis.ai/img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.1 | 0.5376 | 3,220.94 | 0.3887 | ❌ |
| 180 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B | 0.5347 | 2,955.61 | 0.3693 | ❌ |
| 181 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 31B | 0.5331 | 0.00 | 0.0000 | ✅ |
| 182 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 Instant (June 2026) | 0.5318 | 83,314.17 | 0.9358 | ❌ |
| 183 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 35B A3B | 0.5318 | 5,184.12 | 0.5014 | ❌ |
| 184 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Sonnet | 0.5295 | — | — | — |
| 185 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.0 Flash | 0.5290 | 744.19 | 0.1343 | ❌ |
| 186 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.5 (Non-reasoning) | 0.5267 | — | — | — |
| 187 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 | 0.5264 | — | — | — |
| 188 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash | 0.5254 | — | — | — |
| 189 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (medium) | 0.5247 | 8,382.02 | 0.6149 | ❌ |
| 190 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3 Flash (Non-reasoning) | 0.5198 | 2,859.12 | 0.3618 | ❌ |
| 191 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (low) | 0.5196 | 9,444.50 | 0.6418 | ❌ |
| 192 | <img src="https://artificialanalysis.ai/img/logos/cohere_small.svg" width="18" alt="Cohere" /> Cohere | Command A+ | 0.5180 | 0.00 | 0.0000 | ❌ |
| 193 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5 (Non-reasoning) | 0.5152 | 4,453.24 | 0.4649 | ❌ |
| 194 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Glimmer (high) | 0.5150 | 4,378.31 | 0.4608 | ❌ |
| 195 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3.5 | 0.5123 | 21,244.25 | 0.7963 | ❌ |
| 196 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 397B A17B (Non-reasoning) | 0.5090 | 2,824.94 | 0.3592 | ❌ |
| 197 | <img src="https://artificialanalysis.ai/img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step 3.5 Flash 2603 | 0.5080 | 1,008.92 | 0.1722 | ❌ |
| 198 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Haiku | 0.5060 | 13,353.13 | 0.7143 | ❌ |
| 199 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Pro | 0.5057 | 34,953.27 | 0.8633 | ❌ |
| 200 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 Fast | 0.5021 | — | — | — |
| 201 | <img src="https://artificialanalysis.ai/img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE 2.0 | 0.4998 | — | — | — |
| 202 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-2.6-1T | 0.4990 | 6,470.94 | 0.5545 | ❌ |
| 203 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 3 mini Reasoning (high) | 0.4939 | 2,165.71 | 0.3026 | ❌ |
| 204 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 27B (Non-reasoning) | 0.4936 | 2,515.07 | 0.3339 | ❌ |
| 205 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Sonnet (Non-reasoning) | 0.4933 | 13,855.93 | 0.7215 | ❌ |
| 206 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Speciale | 0.4923 | — | — | — |
| 207 | <img src="https://artificialanalysis.ai/img/logos/china_mobile_small.png" width="18" alt="China Mobile" /> China Mobile | JT-35B-Flash | 0.4906 | — | — | — |
| 208 | <img src="https://artificialanalysis.ai/img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step 3.5 Flash | 0.4901 | 823.65 | 0.1461 | ❌ |
| 209 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.1 Flash-Lite | 0.4887 | 3,576.73 | 0.4130 | ❌ |
| 210 | <img src="https://artificialanalysis.ai/img/logos/longcat_small.svg" width="18" alt="LongCat" /> LongCat | LongCat 2.0 | 0.4786 | 8,066.31 | 0.6062 | ❌ |
| 211 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 27B (Non-reasoning) | 0.4784 | 2,963.56 | 0.3699 | ❌ |
| 212 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (Non-reasoning) | 0.4783 | 12,853.95 | 0.7068 | ❌ |
| 213 | <img src="https://artificialanalysis.ai/img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2 | 0.4773 | 3,220.94 | 0.3887 | ❌ |
| 214 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.2 (Non-reasoning) | 0.4760 | 6,598.28 | 0.5592 | ❌ |
| 215 | <img src="https://artificialanalysis.ai/img/logos/bytedance_small.svg" width="18" alt="ByteDance Seed" /> ByteDance Seed | Doubao Seed Code | 0.4744 | — | — | — |
| 216 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o4-mini (high) | 0.4742 | 20,131.41 | 0.7878 | ❌ |
| 217 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o1 | 0.4731 | — | — | — |
| 218 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (Non-reasoning) | 0.4651 | 10,687.75 | 0.6687 | ❌ |
| 219 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (Non-reasoning) | 0.4628 | 894.77 | 0.1563 | ❌ |
| 220 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (Non-reasoning) | 0.4622 | 10,764.21 | 0.6702 | ❌ |
| 221 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (medium) | 0.4607 | 28,810.82 | 0.8398 | ❌ |
| 222 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 122B A10B (Non-reasoning) | 0.4590 | 2,973.39 | 0.3706 | ❌ |
| 223 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.7 Sonnet | 0.4589 | — | — | — |
| 224 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 9B | 0.4561 | 599.43 | 0.1119 | ❌ |
| 225 | <img src="https://artificialanalysis.ai/img/logos/kwaikat_small.svg" width="18" alt="KwaiKAT" /> KwaiKAT | KAT-Coder-Pro V1 | 0.4561 | — | — | — |
| 226 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Sonnet (Non-reasoning) | 0.4555 | — | — | — |
| 227 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (low) | 0.4534 | 25,920.60 | 0.8256 | ❌ |
| 228 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Sep) | 0.4501 | — | — | — |
| 229 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 Terminus | 0.4486 | — | — | — |
| 230 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Exp | 0.4454 | — | — | — |
| 231 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.7 Sonnet (Non-reasoning) | 0.4349 | — | — | — |
| 232 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max Thinking (Preview) | 0.4338 | 15,883.78 | 0.7472 | ❌ |
| 233 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 4B | 0.4323 | 397.09 | 0.0781 | ❌ |
| 234 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 35B A3B (Non-reasoning) | 0.4313 | 2,013.38 | 0.2880 | ❌ |
| 235 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 26B A4B | 0.4291 | — | — | — |
| 236 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash | 0.4288 | 11,436.48 | 0.6829 | ❌ |
| 237 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (medium) | 0.4279 | 6,470.94 | 0.5545 | ❌ |
| 238 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5-Pro (Non-reasoning) | 0.4241 | 907.97 | 0.1582 | ❌ |
| 239 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Haiku (Non-reasoning) | 0.4236 | 4,651.11 | 0.4753 | ❌ |
| 240 | <img src="https://artificialanalysis.ai/img/logos/baidu_small.svg" width="18" alt="Baidu" /> Baidu | ERNIE 5.0 Thinking Preview | 0.4205 | — | — | — |
| 241 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 0905 | 0.4203 | 1,804.74 | 0.2669 | ❌ |
| 242 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (Non-reasoning) | 0.4195 | — | — | — |
| 243 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 235B A22B (Reasoning) | 0.4193 | 10,294.59 | 0.6606 | ❌ |
| 244 | <img src="https://artificialanalysis.ai/img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.5 33B | 0.4182 | — | — | — |
| 245 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 (Non-reasoning) | 0.4178 | — | — | — |
| 246 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-2.6-1T | 0.4163 | — | — | — |
| 247 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (low) | 0.4119 | — | — | — |
| 248 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (Non-reasoning) | 0.4114 | 4,233.78 | 0.4528 | ❌ |
| 249 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 (Non-reasoning) | 0.4106 | — | — | — |
| 250 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (high) | 0.4099 | 6,470.94 | 0.5545 | ❌ |
| 251 | <img src="https://artificialanalysis.ai/img/logos/tencent_small.svg" width="18" alt="Tencent" /> Tencent | Hy3-preview (Non-reasoning) | 0.4088 | — | — | — |
| 252 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (high) | 0.4088 | 4,725.71 | 0.4791 | ❌ |
| 253 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 31B (Non-reasoning) | 0.4087 | 1,634.94 | 0.2487 | ❌ |
| 254 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (medium) | 0.4066 | 2,226.44 | 0.3083 | ❌ |
| 255 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7 (Non-reasoning) | 0.4057 | 6,717.52 | 0.5634 | ❌ |
| 256 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6 | 0.4054 | 11,000.00 | 0.6748 | ❌ |
| 257 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 12B | 0.4046 | 823.65 | 0.1461 | ❌ |
| 258 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (medium) | 0.4042 | — | — | — |
| 259 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 v2 (Non-reasoning) | 0.4019 | 4,152.18 | 0.4482 | ❌ |
| 260 | <img src="https://artificialanalysis.ai/img/logos/inceptionlabs_small.svg" width="18" alt="Inception" /> Inception | Mercury 2 | 0.4019 | 2,973.92 | 0.3706 | ❌ |
| 261 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 35B A3B (Non-reasoning) | 0.4009 | 1,874.38 | 0.2741 | ❌ |
| 262 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 | 0.3972 | — | — | — |
| 263 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5 | 0.3964 | — | — | — |
| 264 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3.5 Lightning | 0.3962 | 1,007.36 | 0.1720 | ❌ |
| 265 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Super | 0.3937 | 1,766.77 | 0.2629 | ❌ |
| 266 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.2 30B | 0.3937 | 2,113.38 | 0.2977 | ❌ |
| 267 | <img src="https://artificialanalysis.ai/img/logos/arcee_small.svg" width="18" alt="Arcee AI" /> Arcee AI | Trinity Large Thinking | 0.3937 | 2,434.12 | 0.3269 | ❌ |
| 268 | <img src="https://artificialanalysis.ai/img/logos/openbmb_small.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-2B | 0.3914 | — | — | — |
| 269 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max | 0.3908 | 4,575.94 | 0.4714 | ❌ |
| 270 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (Non-reasoning) | 0.3888 | 1,076.88 | 0.1813 | ❌ |
| 271 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok Code Fast 1 | 0.3876 | — | — | — |
| 272 | <img src="https://artificialanalysis.ai/img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE | 0.3873 | — | — | — |
| 273 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 | 0.3864 | 1,701.33 | 0.2560 | ❌ |
| 274 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 0528 | 0.3856 | — | — | — |
| 275 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 4 | 0.3809 | 1,610.47 | 0.2460 | ❌ |
| 276 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Sep) (Non-reasoning) | 0.3799 | — | — | — |
| 277 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B A22B 2507 | 0.3774 | 5,919.39 | 0.5333 | ❌ |
| 278 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (minimal) | 0.3770 | 8,099.95 | 0.6071 | ❌ |
| 279 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 32B (Reasoning) | 0.3759 | 1,717.84 | 0.2577 | ❌ |
| 280 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Magistral Medium 1.2 | 0.3754 | — | — | — |
| 281 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 | 0.3748 | 11,211.67 | 0.6788 | ❌ |
| 282 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 (Non-reasoning) | 0.3735 | 8,295.88 | 0.6126 | ❌ |
| 283 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (low) | 0.3725 | 6,470.94 | 0.5545 | ❌ |
| 284 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 9B (Non-reasoning) | 0.3719 | 266.24 | 0.0545 | ❌ |
| 285 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7-Flash | 0.3715 | 1,700.00 | 0.2558 | ❌ |
| 286 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6 (Non-reasoning) | 0.3683 | 1,931.47 | 0.2799 | ❌ |
| 287 | <img src="https://artificialanalysis.ai/img/logos/servicenow_small.svg" width="18" alt="ServiceNow" /> ServiceNow | Apriel-v1.5-15B-Thinker | 0.3649 | — | — | — |
| 288 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-120b (high) | 0.3629 | 2,755.91 | 0.3537 | ❌ |
| 289 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.0 Tiny | 0.3628 | 0.00 | 0.0000 | ❌ |
| 290 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 Omni Flash | 0.3604 | 809.52 | 0.1440 | ❌ |
| 291 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder 480B | 0.3591 | 6,029.56 | 0.5377 | ❌ |
| 292 | <img src="https://artificialanalysis.ai/img/logos/multiversecomputing_small.svg" width="18" alt="Multiverse Computing" /> Multiverse Computing | HyperNova 60B 2605 (high) | 0.3589 | 379.46 | 0.0750 | ❌ |
| 293 | <img src="https://artificialanalysis.ai/img/logos/deepcogito_small.png" width="18" alt="Deep Cogito" /> Deep Cogito | Cogito v2.1 | 0.3584 | — | — | — |
| 294 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Sep) | 0.3581 | — | — | — |
| 295 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron Cascade 2 30B A3B | 0.3578 | — | — | — |
| 296 | <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash (Non-reasoning) | 0.3558 | — | — | — |
| 297 | <img src="https://artificialanalysis.ai/img/logos/servicenow_small.svg" width="18" alt="ServiceNow" /> ServiceNow | Apriel-v1.6-15B-Thinker | 0.3541 | — | — | — |
| 298 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 26B A4B (Non-reasoning) | 0.3534 | 1,494.18 | 0.2329 | ❌ |
| 299 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 3 | 0.3521 | — | — | — |
| 300 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6V | 0.3519 | 2,470.94 | 0.3301 | ❌ |
| 301 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 Terminus (Non-reasoning) | 0.3511 | — | — | — |
| 302 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.2 8B | 0.3482 | 808.14 | 0.1438 | ❌ |
| 303 | <img src="https://artificialanalysis.ai/img/logos/cohere_small.svg" width="18" alt="Cohere" /> Cohere | North Mini Code | 0.3457 | 0.00 | 0.0000 | ❌ |
| 304 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (ChatGPT) | 0.3456 | — | — | — |
| 305 | <img src="https://artificialanalysis.ai/img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | G9v3-3B | 0.3417 | — | — | — |
| 306 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o3-mini (high) | 0.3405 | 25,136.17 | 0.8213 | ❌ |
| 307 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max (Preview) | 0.3397 | 5,366.79 | 0.5097 | ❌ |
| 308 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Exp (Non-reasoning) | 0.3334 | — | — | — |
| 309 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Sep) (Non-reasoning) | 0.3307 | — | — | — |
| 310 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 (Non-reasoning) | 0.3302 | — | — | — |
| 311 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Next 80B A3B (Reasoning) | 0.3284 | 3,110.47 | 0.3808 | ❌ |
| 312 | <img src="https://artificialanalysis.ai/img/logos/bytedance_small.svg" width="18" alt="ByteDance Seed" /> ByteDance Seed | Seed-OSS-36B-Instruct | 0.3261 | 1,579.66 | 0.2426 | ❌ |
| 313 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder Next | 0.3238 | 4,271.56 | 0.4549 | ❌ |
| 314 | <img src="https://artificialanalysis.ai/img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 3 | 0.3235 | 1,749.43 | 0.2611 | ❌ |
| 315 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o (Nov) | 0.3221 | 22,157.27 | 0.8028 | ❌ |
| 316 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Non-reasoning) | 0.3206 | 1,963.02 | 0.2831 | ❌ |
| 317 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano | 0.3195 | 536.82 | 0.1018 | ❌ |
| 318 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 4B (Non-reasoning) | 0.3191 | 99.61 | 0.0219 | ❌ |
| 319 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B 2507 (Non-reasoning) | 0.3189 | 757.12 | 0.1363 | ❌ |
| 320 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o (Aug) | 0.3189 | 19,622.34 | 0.7836 | ❌ |
| 321 | <img src="https://artificialanalysis.ai/img/logos/mbzuai_small.svg" width="18" alt="MBZUAI Institute of Foundation Models" /> MBZUAI Institute of Foundation Models | K2 Think V2 | 0.3179 | — | — | — |
| 322 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite | 0.3160 | 4,250.81 | 0.4537 | ❌ |
| 323 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.1 Fast (Non-reasoning) | 0.3123 | — | — | — |
| 324 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (minimal) | 0.3115 | 1,614.12 | 0.2464 | ❌ |
| 325 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 12B (Non-reasoning) | 0.3102 | 296.11 | 0.0601 | ❌ |
| 326 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 235B A22B | 0.3098 | 1,324.67 | 0.2128 | ❌ |
| 327 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | QwQ-32B | 0.3069 | — | — | — |
| 328 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-1T | 0.3067 | — | — | — |
| 329 | <img src="https://artificialanalysis.ai/img/logos/openbmb_small.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-1B | 0.3065 | — | — | — |
| 330 | <img src="https://artificialanalysis.ai/img/logos/openbmb_small.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-1B (Non-reasoning) | 0.3065 | — | — | — |
| 331 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Pixtral Large | 0.3041 | — | — | — |
| 332 | <img src="https://artificialanalysis.ai/img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Open 100B | 0.3018 | — | — | — |
| 333 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3 0324 | 0.3008 | — | — | — |
| 334 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Large 3 | 0.3008 | 1,239.92 | 0.2023 | ❌ |
| 335 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o3-mini | 0.2995 | 13,323.41 | 0.7139 | ❌ |
| 336 | <img src="https://artificialanalysis.ai/img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax M1 80k | 0.2984 | — | — | — |
| 337 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5-Air | 0.2981 | 2,575.20 | 0.3389 | ❌ |
| 338 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (Non-reasoning) | 0.2978 | 4,013.42 | 0.4401 | ❌ |
| 339 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 E4B | 0.2976 | 264.73 | 0.0543 | ❌ |
| 340 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (Non-reasoning) | 0.2960 | 6,968.82 | 0.5721 | ❌ |
| 341 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 (Jan) | 0.2957 | — | — | — |
| 342 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 4 Maverick | 0.2939 | 2,988.66 | 0.3718 | ❌ |
| 343 | <img src="https://artificialanalysis.ai/img/logos/china_mobile_small.png" width="18" alt="China Mobile" /> China Mobile | JT-MINI | 0.2935 | — | — | — |
| 344 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | DiffusionGemma 26B A4B | 0.2934 | — | — | — |
| 345 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 2.6 Flash | 0.2926 | — | — | — |
| 346 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3 | 0.2919 | 1,933.51 | 0.2801 | ❌ |
| 347 | <img src="https://artificialanalysis.ai/img/logos/naver_small.webp" width="18" alt="Naver" /> Naver | HyperCLOVA X SEED Think (32B) | 0.2910 | — | — | — |
| 348 | <img src="https://artificialanalysis.ai/img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax M1 40k | 0.2908 | — | — | — |
| 349 | <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 Fast (Non-reasoning) | 0.2897 | — | — | — |
| 350 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-20b (high) | 0.2890 | 519.19 | 0.0989 | ❌ |
| 351 | <img src="https://artificialanalysis.ai/img/logos/mbzuai_small.svg" width="18" alt="MBZUAI Institute of Foundation Models" /> MBZUAI Institute of Foundation Models | K2-V2 (high) | 0.2888 | — | — | — |
| 352 | <img src="https://artificialanalysis.ai/img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE (Non-reasoning) | 0.2884 | — | — | — |
| 353 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 mini | 0.2875 | 2,182.49 | 0.3042 | ❌ |
| 354 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B A3B 2507 | 0.2859 | 6,147.30 | 0.5423 | ❌ |
| 355 | <img src="https://artificialanalysis.ai/img/logos/korea-telecom_small.png" width="18" alt="Korea Telecom" /> Korea Telecom | Mi:dm K 2.5 Pro | 0.2859 | — | — | — |
| 356 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (Non-reasoning) | 0.2845 | 1,117.78 | 0.1867 | ❌ |
| 357 | <img src="https://artificialanalysis.ai/img/logos/prime-intellect_small.svg" width="18" alt="Prime Intellect" /> Prime Intellect | INTELLECT-3 | 0.2795 | — | — | — |
| 358 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano Omni 30B A3B | 0.2787 | — | — | — |
| 359 | <img src="https://artificialanalysis.ai/img/logos/trillionlabs_small.svg" width="18" alt="Trillion Labs" /> Trillion Labs | Tri-21B-think Preview | 0.2778 | — | — | — |
| 360 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 30B A3B (Reasoning) | 0.2769 | 6,147.30 | 0.5423 | ❌ |
| 361 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-120b (low) | 0.2769 | 2,862.50 | 0.3621 | ❌ |
| 362 | <img src="https://artificialanalysis.ai/img/logos/longcat_small.svg" width="18" alt="LongCat" /> LongCat | LongCat Flash Lite | 0.2764 | — | — | — |
| 363 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.2 3B | 0.2762 | 391.57 | 0.0772 | ❌ |
| 364 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-20b (low) | 0.2756 | 551.55 | 0.1042 | ❌ |
| 365 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.1 405B | 0.2745 | — | — | — |
| 366 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3.1 | 0.2740 | 1,908.75 | 0.2776 | ❌ |
| 367 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova Premier | 0.2737 | 15,034.25 | 0.7370 | ❌ |
| 368 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 E4B (Non-reasoning) | 0.2727 | 67.91 | 0.0152 | ❌ |
| 369 | <img src="https://artificialanalysis.ai/img/logos/trillionlabs_small.svg" width="18" alt="Trillion Labs" /> Trillion Labs | Tri-21B-Think | 0.2720 | — | — | — |
| 370 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (Non-reasoning) | 0.2652 | 1,859.72 | 0.2726 | ❌ |
| 371 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 32B | 0.2646 | 549.63 | 0.1039 | ❌ |
| 372 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Next 80B A3B | 0.2644 | 1,163.13 | 0.1926 | ❌ |
| 373 | <img src="https://artificialanalysis.ai/img/logos/nousresearch_small.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 405B | 0.2627 | 8,236.48 | 0.6109 | ❌ |
| 374 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral 2 | 0.2603 | 0.00 | 0.0000 | ❌ |
| 375 | <img src="https://artificialanalysis.ai/img/logos/mbzuai_small.svg" width="18" alt="MBZUAI Institute of Foundation Models" /> MBZUAI Institute of Foundation Models | K2-V2 (medium) | 0.2599 | — | — | — |
| 376 | <img src="https://artificialanalysis.ai/img/logos/korea-telecom_small.png" width="18" alt="Korea Telecom" /> Korea Telecom | Mi:dm K 2.5 Pro Preview | 0.2591 | — | — | — |
| 377 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-1T | 0.2591 | — | — | — |
| 378 | <img src="https://artificialanalysis.ai/img/logos/motif_small.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif-2-12.7B | 0.2586 | — | — | — |
| 379 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.5 Haiku | 0.2564 | — | — | — |
| 380 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 8B (Reasoning) | 0.2557 | 5,382.57 | 0.5104 | ❌ |
| 381 | <img src="https://artificialanalysis.ai/img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step3 VL 10B | 0.2543 | — | — | — |
| 382 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Super 49B v1.5 | 0.2518 | 1,294.59 | 0.2091 | ❌ |
| 383 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.0 Flash | 0.2513 | — | — | — |
| 384 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7-Flash (Non-reasoning) | 0.2511 | 324.41 | 0.0652 | ❌ |
| 385 | <img src="https://artificialanalysis.ai/img/logos/baidu_small.svg" width="18" alt="Baidu" /> Baidu | ERNIE 4.5 300B A47B | 0.2483 | — | — | — |
| 386 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Magistral Medium 1 | 0.2481 | — | — | — |
| 387 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral Medium | 0.2460 | — | — | — |
| 388 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B 2507 | 0.2452 | — | — | — |
| 389 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (Non-reasoning) | 0.2448 | — | — | — |
| 390 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 4 (Non-reasoning) | 0.2446 | 477.97 | 0.0920 | ❌ |
| 391 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4 | 0.2443 | — | — | — |
| 392 | <img src="https://artificialanalysis.ai/img/logos/nousresearch_small.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 405B (Non-reasoning) | 0.2430 | 2,541.04 | 0.3361 | ❌ |
| 393 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder 30B A3B | 0.2418 | 1,961.22 | 0.2829 | ❌ |
| 394 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-8B-A1B | 0.2396 | — | — | — |
| 395 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 30B A3B | 0.2391 | 732.88 | 0.1326 | ❌ |
| 396 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6V (Non-reasoning) | 0.2384 | 818.14 | 0.1453 | ❌ |
| 397 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 E2B | 0.2372 | — | — | — |
| 398 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Omni 30B A3B (Reasoning) | 0.2367 | 2,609.12 | 0.3418 | ❌ |
| 399 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral Small 2 | 0.2348 | 0.00 | 0.0000 | ❌ |
| 400 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B | 0.2328 | 21,515.54 | 0.7983 | ❌ |
| 401 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5V | 0.2318 | 4,941.89 | 0.4899 | ❌ |
| 402 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-2.6B | 0.2317 | 0.00 | 0.0000 | ❌ |
| 403 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 12B v2 VL | 0.2308 | 1,647.30 | 0.2501 | ❌ |
| 404 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Large 2 (Nov) | 0.2297 | — | — | — |
| 405 | <img src="https://artificialanalysis.ai/img/logos/tii_small.svg" width="18" alt="TII UAE" /> TII UAE | Falcon-H1R-7B | 0.2283 | — | — | — |
| 406 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Ultra | 0.2273 | — | — | — |
| 407 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3 (Dec) | 0.2269 | — | — | — |
| 408 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Magistral Small 1.2 | 0.2265 | — | — | — |
| 409 | <img src="https://artificialanalysis.ai/img/logos/nanbeige_small.png" width="18" alt="Nanbeige" /> Nanbeige | Nanbeige4.1-3B | 0.2185 | — | — | — |
| 410 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova Pro | 0.2183 | — | — | — |
| 411 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3.2 | 0.2176 | 257.10 | 0.0528 | ❌ |
| 412 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3.1 32B Think | 0.2174 | — | — | — |
| 413 | <img src="https://artificialanalysis.ai/img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam 105B (high) | 0.2168 | — | — | — |
| 414 | <img src="https://artificialanalysis.ai/img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.0 32B | 0.2159 | — | — | — |
| 415 | <img src="https://artificialanalysis.ai/img/logos/mbzuai_small.svg" width="18" alt="MBZUAI Institute of Foundation Models" /> MBZUAI Institute of Foundation Models | K2-V2 (low) | 0.2139 | — | — | — |
| 416 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 9B V2 | 0.2135 | 429.46 | 0.0837 | ❌ |
| 417 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 2B | 0.2134 | — | — | — |
| 418 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Non-reasoning) | 0.2111 | 400.95 | 0.0788 | ❌ |
| 419 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-flash-2.0 | 0.2110 | — | — | — |
| 420 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 4 Scout | 0.2101 | 528.27 | 0.1004 | ❌ |
| 421 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Super 49B v1.5 (Non-reasoning) | 0.2092 | 663.79 | 0.1220 | ❌ |
| 422 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 32B | 0.2091 | 1,717.84 | 0.2577 | ❌ |
| 423 | <img src="https://artificialanalysis.ai/img/logos/nousresearch_small.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 70B | 0.2076 | — | — | — |
| 424 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral Small (May) | 0.2063 | — | — | — |
| 425 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova Lite | 0.2058 | 342.05 | 0.0684 | ❌ |
| 426 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.3 Nemotron Super 49B | 0.2027 | — | — | — |
| 427 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 32B | 0.2014 | — | — | — |
| 428 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen2.5 72B | 0.2014 | — | — | — |
| 429 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 14B | 0.2007 | 10,757.77 | 0.6700 | ❌ |
| 430 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-flash-2.0 | 0.2006 | 399.23 | 0.0785 | ❌ |
| 431 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 8B | 0.2003 | 677.93 | 0.1242 | ❌ |
| 432 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B | 0.1987 | 6,147.30 | 0.5423 | ❌ |
| 433 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Magistral Small 1 | 0.1986 | — | — | — |
| 434 | <img src="https://artificialanalysis.ai/img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 2 | 0.1935 | — | — | — |
| 435 | <img src="https://artificialanalysis.ai/img/logos/cohere_small.svg" width="18" alt="Cohere" /> Cohere | Command A | 0.1933 | 7,924.67 | 0.6021 | ❌ |
| 436 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Large 2 (Jul) | 0.1929 | — | — | — |
| 437 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral Small | 0.1927 | — | — | — |
| 438 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B (Non-reasoning) | 0.1926 | 2,367.59 | 0.3210 | ❌ |
| 439 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Ministral 3 14B | 0.1922 | 262.66 | 0.0539 | ❌ |
| 440 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.1 Nemotron 70B | 0.1912 | 1,980.91 | 0.2848 | ❌ |
| 441 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano 4B | 0.1895 | — | — | — |
| 442 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 4B (Reasoning) | 0.1888 | — | — | — |
| 443 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3.1 | 0.1881 | 257.92 | 0.0530 | ❌ |
| 444 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o mini | 0.1880 | 1,185.41 | 0.1955 | ❌ |
| 445 | <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3 Haiku | 0.1874 | — | — | — |
| 446 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.3 Nemotron Super 49B (Non-reasoning) | 0.1859 | — | — | — |
| 447 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B A3B 2507 (Non-reasoning) | 0.1841 | 775.16 | 0.1390 | ❌ |
| 448 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.1 70B | 0.1822 | 748.35 | 0.1350 | ❌ |
| 449 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 9B V2 (Non-reasoning) | 0.1818 | 199.16 | 0.0418 | ❌ |
| 450 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B | 0.1818 | — | — | — |
| 451 | <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5V (Non-reasoning) | 0.1803 | 1,539.73 | 0.2381 | ❌ |
| 452 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 E2B (Non-reasoning) | 0.1802 | — | — | — |
| 453 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 32B (Non-reasoning) | 0.1794 | 609.62 | 0.1135 | ❌ |
| 454 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 2B (Non-reasoning) | 0.1781 | — | — | — |
| 455 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.1 30B | 0.1775 | — | — | — |
| 456 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 nano | 0.1753 | 540.51 | 0.1024 | ❌ |
| 457 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3.1 32B Instruct | 0.1745 | — | — | — |
| 458 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Omni 30B A3B | 0.1730 | 841.00 | 0.1486 | ❌ |
| 459 | <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (minimal) | 0.1723 | 346.91 | 0.0693 | ❌ |
| 460 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B 2507 (Non-reasoning) | 0.1709 | — | — | — |
| 461 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.1 8B | 0.1696 | 46.04 | 0.0105 | ❌ |
| 462 | <img src="https://artificialanalysis.ai/img/logos/celeris.svg" width="18" alt="Celeris" /> Celeris | Celeris-1 | 0.1669 | 1,022.66 | 0.1741 | ❌ |
| 463 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 32B Think | 0.1668 | — | — | — |
| 464 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Llama 70B | 0.1664 | 3,265.54 | 0.3919 | ❌ |
| 465 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.3 70B | 0.1659 | 7,011.81 | 0.5735 | ❌ |
| 466 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 14B | 0.1649 | — | — | — |
| 467 | <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi Linear 48B A3B Instruct | 0.1645 | — | — | — |
| 468 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Ministral 3 8B | 0.1639 | 195.69 | 0.0411 | ❌ |
| 469 | <img src="https://artificialanalysis.ai/img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 2 (Non-reasoning) | 0.1638 | — | — | — |
| 470 | <img src="https://artificialanalysis.ai/img/logos/nousresearch_small.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 70B (Non-reasoning) | 0.1608 | — | — | — |
| 471 | <img src="https://artificialanalysis.ai/img/logos/ai21_small.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba Reasoning 3B | 0.1602 | — | — | — |
| 472 | <img src="https://artificialanalysis.ai/img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.0 32B (Non-reasoning) | 0.1581 | — | — | — |
| 473 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.1 8B | 0.1580 | 93.22 | 0.0206 | ❌ |
| 474 | <img src="https://artificialanalysis.ai/img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova Micro | 0.1553 | 208.27 | 0.0436 | ❌ |
| 475 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 24B A2B | 0.1548 | — | — | — |
| 476 | <img src="https://artificialanalysis.ai/img/logos/ai21_small.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba 1.7 Large | 0.1537 | — | — | — |
| 477 | <img src="https://artificialanalysis.ai/img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam 30B (high) | 0.1519 | — | — | — |
| 478 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 12B v2 VL (Non-reasoning) | 0.1503 | 521.86 | 0.0993 | ❌ |
| 479 | <img src="https://artificialanalysis.ai/img/logos/openbmb_small.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM-V 4.6 1.3B | 0.1499 | — | — | — |
| 480 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3 | 0.1495 | 259.73 | 0.0533 | ❌ |
| 481 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 8B | 0.1492 | 5,382.57 | 0.5104 | ❌ |
| 482 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B (Non-reasoning) | 0.1456 | 742.03 | 0.1340 | ❌ |
| 483 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano (Non-reasoning) | 0.1430 | 172.43 | 0.0366 | ❌ |
| 484 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 27B | 0.1409 | — | — | — |
| 485 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H Small | 0.1397 | 304.12 | 0.0615 | ❌ |
| 486 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 4B | 0.1394 | — | — | — |
| 487 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 0528 Qwen3 8B | 0.1358 | — | — | — |
| 488 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 14B (Non-reasoning) | 0.1336 | 1,176.68 | 0.1943 | ❌ |
| 489 | <img src="https://artificialanalysis.ai/img/logos/microsoft_small.svg" width="18" alt="Microsoft" /> Microsoft | Phi-4 | 0.1290 | 393.88 | 0.0776 | ❌ |
| 490 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Ministral 3 3B | 0.1286 | 135.69 | 0.0293 | ❌ |
| 491 | <img src="https://artificialanalysis.ai/img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.1 Nemotron Nano 4B v1.1 | 0.1277 | — | — | — |
| 492 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 270M | 0.1262 | — | — | — |
| 493 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3 70B | 0.1209 | — | — | — |
| 494 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.2 11B (Vision) | 0.1206 | 431.98 | 0.0842 | ❌ |
| 495 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 0.8B | 0.1176 | — | — | — |
| 496 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.2 3B | 0.1175 | — | — | — |
| 497 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 7B Think | 0.1168 | — | — | — |
| 498 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-1.2B-Instruct | 0.1103 | — | — | — |
| 499 | <img src="https://artificialanalysis.ai/img/logos/reka_small.svg" width="18" alt="Reka AI" /> Reka AI | Reka Flash 3 | 0.1098 | — | — | — |
| 500 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 2.6B | 0.1095 | — | — | — |
| 501 | <img src="https://artificialanalysis.ai/img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-mini-2.0 | 0.1091 | — | — | — |
| 502 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 8B (Non-reasoning) | 0.1081 | 582.94 | 0.1093 | ❌ |
| 503 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Molmo2-8B | 0.1052 | — | — | — |
| 504 | <img src="https://artificialanalysis.ai/img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam M | 0.1047 | — | — | — |
| 505 | <img src="https://artificialanalysis.ai/img/logos/ai21_small.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba 1.7 Mini | 0.1034 | — | — | — |
| 506 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-1.2B-Thinking | 0.1020 | — | — | — |
| 507 | <img src="https://artificialanalysis.ai/img/logos/microsoft_small.svg" width="18" alt="Microsoft" /> Microsoft | Phi-4 Mini | 0.1000 | 0.00 | 0.0000 | ❌ |
| 508 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 12B | 0.0982 | — | — | — |
| 509 | <img src="https://artificialanalysis.ai/img/logos/swiss-ai-initiative_small.png" width="18" alt="Swiss AI Initiative" /> Swiss AI Initiative | Apertus 70B Instruct | 0.0953 | — | — | — |
| 510 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 0.8B (Non-reasoning) | 0.0949 | — | — | — |
| 511 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 7B | 0.0938 | — | — | — |
| 512 | <img src="https://artificialanalysis.ai/img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | Exaone 4.0 1.2B | 0.0928 | — | — | — |
| 513 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H 1B | 0.0922 | — | — | — |
| 514 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | OLMo 2 32B | 0.0920 | — | — | — |
| 515 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.2 1B | 0.0913 | — | — | — |
| 516 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 1.7B | 0.0899 | — | — | — |
| 517 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.1 3B | 0.0883 | — | — | — |
| 518 | <img src="https://artificialanalysis.ai/img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | Exaone 4.0 1.2B (Non-reasoning) | 0.0857 | — | — | — |
| 519 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 8B A1B | 0.0838 | — | — | — |
| 520 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 Micro | 0.0813 | — | — | — |
| 521 | <img src="https://artificialanalysis.ai/img/logos/microsoft_small.svg" width="18" alt="Microsoft" /> Microsoft | Phi-3 Mini | 0.0757 | — | — | — |
| 522 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 4B | 0.0752 | — | — | — |
| 523 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 3.3 8B | 0.0728 | 249.75 | 0.0514 | ❌ |
| 524 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-VL-1.6B | 0.0704 | — | — | — |
| 525 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 1B | 0.0696 | — | — | — |
| 526 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 350M | 0.0687 | — | — | — |
| 527 | <img src="https://artificialanalysis.ai/img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 1.2B | 0.0669 | — | — | — |
| 528 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3n E4B | 0.0669 | — | — | — |
| 529 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 0.6B | 0.0662 | — | — | — |
| 530 | <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3 8B | 0.0660 | — | — | — |
| 531 | <img src="https://artificialanalysis.ai/img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral 7B | 0.0636 | 324.05 | 0.0652 | ❌ |
| 532 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 1.7B (Non-reasoning) | 0.0579 | — | — | — |
| 533 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 1B | 0.0574 | — | — | — |
| 534 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | OLMo 2 7B | 0.0573 | — | — | — |
| 535 | <img src="https://artificialanalysis.ai/img/logos/swiss-ai-initiative_small.png" width="18" alt="Swiss AI Initiative" /> Swiss AI Initiative | Apertus 8B Instruct | 0.0564 | — | — | — |
| 536 | <img src="https://artificialanalysis.ai/img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H 350M | 0.0523 | — | — | — |
| 537 | <img src="https://artificialanalysis.ai/img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Molmo 7B-D | 0.0490 | — | — | — |
| 538 | <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 0.6B (Non-reasoning) | 0.0449 | — | — | — |
| 539 | <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3n E2B | 0.0372 | — | — | — |
| 540 | <img src="https://artificialanalysis.ai/img/logos/cohere_small.svg" width="18" alt="Cohere" /> Cohere | Tiny Aya Global | 0.0368 | — | — | — |
| 541 | <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 1.5B | 0.0000 | — | — | — |

## 品牌帕累托前沿连线（仅体现在图中）

以下十一个品牌在图中拥有单独的帕累托连线（较窄宽度，品牌主题色，图层高于总体灰色连线）：

| 品牌 | 主题色 | 品牌前沿模型数 |
|------|--------|--------------|
| <img src="https://artificialanalysis.ai/img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | `#cc785c` | 13 |
| <img src="https://artificialanalysis.ai/img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | `#1f1f1f` | 16 |
| <img src="https://artificialanalysis.ai/img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | `#0089f4` | 5 |
| <img src="https://artificialanalysis.ai/img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | `#1c7ff8` | 4 |
| <img src="https://artificialanalysis.ai/img/logos/google_small.svg" width="18" alt="Google" /> Google | `#34A853` | 5 |
| <img src="https://artificialanalysis.ai/img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | `#736cd3` | 8 |
| <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | `#047AFE` | 7 |
| <img src="https://artificialanalysis.ai/img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | `#ff7018` | 7 |
| <img src="https://artificialanalysis.ai/img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | `#2243e6` | 5 |
| <img src="https://artificialanalysis.ai/img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | `#EB3568` | 4 |
| <img src="https://artificialanalysis.ai/img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | `#ff6900` | 2 |

## 评分方法

1. **18项评估指标**各自线性归一化到 [0,1]
2. **综合能力值** = 所有有效归一化分数的算术平均
3. **综合能力再归一化**：线性映射到 [0,1]，性能最好的模型 = 1，最差的模型 = 0
4. **Pareto前沿** = 不被任何其他模型支配的模型（综合能力 ≥ 且成本 ≤，且至少一项严格更优；成本为 0 的免费模型同样参与——横轴左端恒为 0，免费模型是合法前沿候选）
5. **模型范围** = Status: All（含已弃用模型；缺少足够评估数据者不参与排名）

## 横轴映射（logistic 单函数拟合）与分布分析

横轴（单请求成本）按**单一 logistic 函数**映射（非分段、非分区锚点）：

```
x = 0                          当 c = 0（免费模型，钉在最左缘）
x = 1 / (1 + e^(-(z - mu)/s))  当 c > 0，其中 z = log10(c)
```
本例拟合值：**mu = 3.7122，s = 0.4511** —— 该函数拟合映射前的所有模型（313 个正成本模型的经验分布，加权最小二乘；|F-ECDF| 最大偏差 0.0359，平均偏差 0.0118）。

- **左端恒为 0**（成本 0；8 个免费模型位于最左缘）
- 最低正成本 46.04 → x = 0.0105；最高成本 1,002,731 → x = 0.9938
- 中位数位置 0.490（≈ 0.5 居中）；左右两半模型数：左 161 / 右 160
- 横轴十分位模型数：41，34，32，27，27，24，34，39，36，27（每一格均有模型，覆盖全轴）
- **10^x 数量级指示**（位置 = x(10^x)）：10^0 → 0.000，10^1 → 0.002，10^2 → 0.022，10^3 → 0.171，10^4 → 0.654，10^5 → 0.946，10^6 → 0.994

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
**模型总数（Status: All）**: 541 个参与排名（另有模型因评估数据不足未列入；总体帕累托前沿 14 个）  