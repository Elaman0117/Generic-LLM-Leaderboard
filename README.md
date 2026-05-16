# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

## Pareto 前沿模型（综合能力从高到低）

| # | 模型 | 综合能力 | 单次价格 (USD) | 推理 |
|---|------|---------|---------------|------|
| 1 | GPT-5.5 (xhigh) | 0.9024 | $0.2356 | 🧠 |
| 2 | Gemini 3.1 Pro Preview | 0.9007 | $0.0865 | 🧠 |
| 3 | Claude Opus 4.7 (max) | 0.8496 | $0.0707 | 🧠 |
| 4 | GPT-5.5 (medium) | 0.8357 | $0.0503 | 🧠 |
| 5 | Grok 4.3 (high) | 0.7883 | $0.0069 | 🧠 |
| 6 | DeepSeek V4 Flash (Max) | 0.6821 | $0.0039 | 🧠 |
| 7 | GPT-5.4 nano (xhigh) | 0.6558 | $0.0026 | 🧠 |
| 8 | MiMo-V2-Flash (Feb 2026) | 0.6120 | $0.0015 | 🧠 |
| 9 | Qwen3.5 9B | 0.4901 | $0.0014 | 🧠 |
| 10 | DeepSeek V4 Flash | 0.4720 | $0.0003 | — |
| 11 | MiMo-V2-Flash | 0.3954 | $0.0003 | — |
| 12 | Qwen3.5 4B | 0.3163 | $0.0001 | — |
| 13 | Qwen3.5 2B | 0.1874 | $0.0001 | — |
| 14 | Qwen3.5 0.8B | 0.0937 | $0.0000 | — |

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
**模型总数**: 144  