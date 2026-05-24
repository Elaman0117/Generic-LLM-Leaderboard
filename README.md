# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

## Pareto 前沿模型（综合能力从高到低）

| # | 模型 | 综合能力 | 单次价格 (USD) | 推理 |
|---|------|---------|---------------|------|
| 1 | GPT-5.5 (xhigh) | 0.8839 | $4.3659 | 🧠 |
| 2 | Gemini 3.1 Pro Preview | 0.8807 | $1.2061 | 🧠 |
| 3 | Gemini 3.5 Flash | 0.8407 | $0.7459 | 🧠 |
| 4 | GPT-5.5 (medium) | 0.8300 | $0.4783 | 🧠 |
| 5 | Grok 4.3 (high) | 0.7474 | $0.3453 | 🧠 |
| 6 | DeepSeek V4 Pro (Max) | 0.7369 | $0.2131 | 🧠 |
| 7 | DeepSeek V4 Pro (High) | 0.7254 | $0.1079 | 🧠 |
| 8 | MiMo-V2.5 | 0.7000 | $0.0469 | 🧠 |
| 9 | Qwen3.6 27B | 0.6562 | $0.0224 | 🧠 |
| 10 | Qwen3.6 35B A3B | 0.6231 | $0.0095 | 🧠 |
| 11 | Hy3-preview | 0.5976 | $0.0054 | 🧠 |
| 12 | Qwen3.5 Omni Plus | 0.5622 | $0.0042 | — |
| 13 | Qwen3.5 122B A10B | 0.5139 | $0.0034 | — |
| 14 | Qwen3.5 9B | 0.4841 | $0.0014 | 🧠 |
| 15 | Gemma 4 31B | 0.4608 | $0.0007 | — |
| 16 | Gemma 4 26B A4B | 0.3939 | $0.0007 | — |
| 17 | MiMo-V2-Flash | 0.3916 | $0.0006 | — |
| 18 | Qwen3.5 4B | 0.3150 | $0.0002 | — |
| 19 | Qwen3.5 2B | 0.1861 | $0.0001 | — |

### 评分方法

1. **15项Intelligence子指标**各自线性归一化到 [0,1]（最低→0，最高→1，"--"忽略）
2. **综合能力值** = 所有有效归一化分数的算术平均
3. **Pareto前沿** = 不被任何其他模型支配的模型（不存在单次更便宜且更强的选择）

### 单次请求价格计算

```
输入输出比 r = (Blended - Output_Price) / (Input_Price - Output_Price)

# 非推理模型 & 推理模型（有 Reasoning Time）：
输出tokens = (Total_Response - TTFT) × Speed
# 对推理模型：TTFT=首CoT token时间，(Total-TTFT)已含reasoning+可见输出，不加倍

# 推理模型（无 Reasoning Time）：
输出tokens = Total_Response × Speed
# CoT不可见→first chunk无意义，假设全程都在生成token

输入tokens = 输出tokens × r / (1-r)
单次价格 = (输入tokens × Input_Price + 输出tokens × Output_Price) / 1,000,000
```

**数据来源**: [Artificial Analysis](https://artificialanalysis.ai/leaderboards/models)  
**模型总数**: 147  