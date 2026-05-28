# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

## Pareto 前沿模型（综合能力从高到低）

| # | 模型 | 综合能力 | 单次价格 (USD) | 归一化价格 | 推理 |
|---|------|---------|---------------|-----------|------|
| 1 | GPT-5.5 (xhigh) | 0.8898 | $2.5007 | 1.0000 | Y |
| 2 | GPT-5.5 (high) | 0.8685 | $1.1260 | 0.4503 | Y |
| 3 | Gemini 3.1 Pro Preview | 0.8651 | $0.9908 | 0.3962 | Y |
| 4 | Gemini 3.5 Flash | 0.8411 | $0.6087 | 0.2434 | Y |
| 5 | GPT-5.5 (medium) | 0.8300 | $0.5800 | 0.2319 | Y |
| 6 | Gemini 3.5 Flash (medium) | 0.8189 | $0.5475 | 0.2189 | Y |
| 7 | Grok 4.3 (high) | 0.7442 | $0.4668 | 0.1867 | Y |
| 8 | DeepSeek V4 Pro (Max) | 0.7418 | $0.2100 | 0.0840 | Y |
| 9 | DeepSeek V4 Pro (High) | 0.7254 | $0.1078 | 0.0431 | Y |
| 10 | MiMo-V2.5 | 0.7000 | $0.0354 | 0.0141 | Y |
| 11 | Qwen3.6 27B | 0.6562 | $0.0224 | 0.0090 | Y |
| 12 | Qwen3.6 35B A3B | 0.6231 | $0.0096 | 0.0038 | Y |
| 13 | Qwen3.5 Omni Plus | 0.5622 | $0.0042 | 0.0017 | N |
| 14 | Qwen3.5 122B A10B | 0.5139 | $0.0034 | 0.0014 | N |
| 15 | Qwen3.5 9B | 0.4841 | $0.0014 | 0.0006 | Y |
| 16 | Gemma 4 31B | 0.4608 | $0.0007 | 0.0003 | N |
| 17 | Gemma 4 26B A4B | 0.3939 | $0.0007 | 0.0003 | N |
| 18 | MiMo-V2-Flash | 0.3916 | $0.0006 | 0.0002 | N |
| 19 | Qwen3.5 4B | 0.3150 | $0.0002 | 0.0001 | N |
| 20 | Qwen3.5 2B | 0.1861 | $0.0001 | 0.0000 | N |

### 评分方法

1. **15项Intelligence子指标**各自线性归一化到 [0,1]
2. **综合能力值** = 所有有效归一化分数的算术平均
3. **Pareto前沿** = 不被任何其他模型支配的模型

### 坐标说明

**X轴（线性归一化价格）**：
1. 归一化基准 = 帕累托前沿中最贵模型的单次请求价格
2. 归一化价格 = 单次请求价格 / 基准价格
3. 0 = 免费，1 = 最贵的帕累托前沿模型
4. 超出 [0,1] 范围的模型不在图中显示

**Y轴（综合能力）**：
1. 15项Intelligence子指标各自归一化到 [0,1]
2. 综合能力 = 所有有效归一化分数的算术平均（已在 [0,1] 范围内）
3. 0 = 最低，1 = 最高

### 精确分数计算

全程使用 Python `fractions.Fraction` 进行精确有理数运算：
- 所有解析值、归一化、均值、比值、价格计算均使用精确分数
- 仅在绘图坐标传入 matplotlib 及 JSON 序列化时转为浮点数

### 单次请求价格计算

```
输入输出比 r = (Blended - Output_Price) / (Input_Price - Output_Price)
非推理/推理有ReasonT: 输出tokens = (Total_Response - TTFT) × Speed
推理无ReasonT: 输出tokens = Total_Response × Speed
输入tokens = 输出tokens × r / (1-r)
单次价格 = (输入tokens × Input_Price + 输出tokens × Output_Price) / 1,000,000
```

**数据来源**: [Artificial Analysis](https://artificialanalysis.ai/leaderboards/models)  
**模型总数**: 135  