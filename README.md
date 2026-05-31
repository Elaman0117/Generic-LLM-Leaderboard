# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

## Pareto 前沿模型（综合能力从高到低）

| # | 模型 | 综合能力 | 单次价格 (USD) | 归一化价格 | 推理 |
|---|------|---------|---------------|-----------|------|
| 1 | Claude Opus 4.8 (max) | 0.8873 | $0.9726 | 1.0000 | Y |
| 2 | GPT-5.5 (high) | 0.8595 | $0.7213 | 0.7416 | Y |
| 3 | Gemini 3.1 Pro Preview | 0.8591 | $0.6591 | 0.6777 | Y |
| 4 | Claude Opus 4.7 (max) | 0.8416 | $0.6347 | 0.6526 | Y |
| 5 | Gemini 3.5 Flash | 0.8338 | $0.6203 | 0.6377 | Y |
| 6 | GPT-5.5 (medium) | 0.8216 | $0.4439 | 0.4564 | Y |
| 7 | Grok 4.3 (high) | 0.7378 | $0.2634 | 0.2708 | Y |
| 8 | DeepSeek V4 Pro (Max) | 0.7342 | $0.2134 | 0.2194 | Y |
| 9 | DeepSeek V4 Pro (High) | 0.7167 | $0.1077 | 0.1107 | Y |
| 10 | GPT-5.4 mini (xhigh) | 0.7022 | $0.1050 | 0.1080 | Y |
| 11 | MiMo-V2.5 | 0.6912 | $0.0354 | 0.0364 | Y |
| 12 | Qwen3.5 397B A17B | 0.6371 | $0.0334 | 0.0343 | Y |
| 13 | GPT-5.4 nano (xhigh) | 0.6271 | $0.0241 | 0.0248 | Y |
| 14 | Qwen3.6 35B A3B | 0.6171 | $0.0096 | 0.0098 | Y |
| 15 | Qwen3.5 Omni Plus | 0.5572 | $0.0042 | 0.0043 | N |
| 16 | Qwen3.5 122B A10B | 0.5093 | $0.0034 | 0.0035 | N |
| 17 | Qwen3.5 9B | 0.4818 | $0.0014 | 0.0014 | Y |
| 18 | Gemma 4 31B | 0.4571 | $0.0008 | 0.0008 | N |
| 19 | Gemma 4 26B A4B | 0.3906 | $0.0007 | 0.0007 | N |
| 20 | MiMo-V2-Flash | 0.3874 | $0.0006 | 0.0006 | N |
| 21 | Qwen3.5 4B | 0.3123 | $0.0002 | 0.0002 | N |
| 22 | Qwen3.5 2B | 0.1857 | $0.0001 | 0.0001 | N |

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
**模型总数**: 139  