# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

## Pareto 前沿模型（综合能力从高到低）

| # | 模型 | 综合能力 | 单次价格 (USD) | 推理 |
|---|------|---------|---------------|------|
| 1 | Gemini 3.1 Pro Preview | 0.8875 | $0.7597 | 🧠 |
| 2 | Gemini 3.5 Flash | 0.8463 | $0.7070 | 🧠 |
| 3 | GPT-5.5 (medium) | 0.8322 | $0.4663 | 🧠 |
| 4 | Grok 4.3 (high) | 0.7409 | $0.1444 | 🧠 |
| 5 | MiMo-V2.5 | 0.7094 | $0.0468 | 🧠 |
| 6 | Qwen3.6 27B | 0.6639 | $0.0225 | 🧠 |
| 7 | Qwen3.6 35B A3B | 0.6304 | $0.0096 | 🧠 |
| 8 | Hy3-preview | 0.6010 | $0.0054 | 🧠 |
| 9 | Qwen3.5 Omni Plus | 0.5705 | $0.0042 | — |
| 10 | Qwen3.5 122B A10B | 0.5163 | $0.0034 | — |
| 11 | Qwen3.5 9B | 0.4880 | $0.0014 | 🧠 |
| 12 | Gemma 4 31B | 0.4640 | $0.0007 | — |
| 13 | Gemma 4 26B A4B | 0.3956 | $0.0007 | — |
| 14 | MiMo-V2-Flash | 0.3954 | $0.0006 | — |
| 15 | Qwen3.5 4B | 0.3145 | $0.0002 | — |
| 16 | Qwen3.5 2B | 0.1866 | $0.0001 | — |

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