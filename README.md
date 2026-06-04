# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

## Pareto 前沿模型（综合能力从高到低）

| # | 模型 | 综合能力 | 单次价格 (USD) | 归一化价格 | 推理 |
|---|------|---------|---------------|-----------|------|
| 1 | Claude Opus 4.8 (max) | 0.8866 | $0.7376 | 1.0000 | Y |
| 2 | GPT-5.5 (medium) | 0.8209 | $0.5497 | 0.7453 | Y |
| 3 | Grok 4.3 (high) | 0.7372 | $0.4323 | 0.5861 | Y |
| 4 | DeepSeek V4 Pro (Max) | 0.7335 | $0.2107 | 0.2857 | Y |
| 5 | DeepSeek V4 Pro (High) | 0.7159 | $0.1082 | 0.1467 | Y |
| 6 | MiMo-V2.5 | 0.6916 | $0.0353 | 0.0479 | Y |
| 7 | Qwen3.5 397B A17B | 0.6364 | $0.0334 | 0.0453 | Y |
| 8 | GPT-5.4 nano (xhigh) | 0.6265 | $0.0291 | 0.0395 | Y |
| 9 | Qwen3.6 35B A3B | 0.6164 | $0.0226 | 0.0306 | Y |
| 10 | Qwen3.5 122B A10B | 0.6106 | $0.0170 | 0.0231 | Y |
| 11 | Qwen3.5 Omni Plus | 0.5565 | $0.0042 | 0.0057 | N |
| 12 | Qwen3.5 122B A10B | 0.5086 | $0.0034 | 0.0046 | N |
| 13 | Qwen3.5 9B | 0.4811 | $0.0014 | 0.0019 | Y |
| 14 | Gemma 4 31B | 0.4566 | $0.0007 | 0.0010 | N |
| 15 | Gemma 4 26B A4B | 0.3903 | $0.0007 | 0.0010 | N |
| 16 | MiMo-V2-Flash | 0.3867 | $0.0006 | 0.0008 | N |
| 17 | Qwen3.5 4B | 0.3116 | $0.0002 | 0.0003 | N |
| 18 | Qwen3.5 2B | 0.1850 | $0.0001 | 0.0002 | N |

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
**模型总数**: 142  