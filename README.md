# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

## Pareto 前沿模型（综合能力从高到低）

| # | 模型 | 综合能力 | 单次价格 (USD) | 归一化价格 | 推理 |
|---|------|---------|---------------|-----------|------|
| 1 | Claude Opus 4.8 (max) | 0.8866 | $1.7192 | 1.0000 | Y |
| 2 | GPT-5.5 (high) | 0.8588 | $1.0311 | 0.5998 | Y |
| 3 | Gemini 3.1 Pro Preview | 0.8584 | $0.7296 | 0.4244 | Y |
| 4 | Gemini 3.5 Flash | 0.8332 | $0.6020 | 0.3501 | Y |
| 5 | GPT-5.5 (medium) | 0.8199 | $0.5192 | 0.3020 | Y |
| 6 | Gemini 3.5 Flash (medium) | 0.8099 | $0.4719 | 0.2745 | Y |
| 7 | Grok 4.3 (high) | 0.7372 | $0.3407 | 0.1982 | Y |
| 8 | DeepSeek V4 Pro (Max) | 0.7335 | $0.2129 | 0.1238 | Y |
| 9 | MiniMax-M3 | 0.7285 | $0.0774 | 0.0450 | Y |
| 10 | MiMo-V2.5 | 0.6916 | $0.0352 | 0.0205 | Y |
| 11 | Qwen3.5 397B A17B | 0.6364 | $0.0330 | 0.0192 | Y |
| 12 | Qwen3.6 35B A3B | 0.6164 | $0.0225 | 0.0131 | Y |
| 13 | Qwen3.5 122B A10B | 0.6106 | $0.0170 | 0.0099 | Y |
| 14 | Qwen3.5 Omni Plus | 0.5565 | $0.0042 | 0.0025 | N |
| 15 | Qwen3.5 122B A10B | 0.5086 | $0.0034 | 0.0020 | N |
| 16 | Qwen3.5 9B | 0.4811 | $0.0014 | 0.0008 | Y |
| 17 | Gemma 4 31B | 0.4566 | $0.0007 | 0.0004 | N |
| 18 | Gemma 4 26B A4B | 0.3903 | $0.0007 | 0.0004 | N |
| 19 | MiMo-V2-Flash | 0.3867 | $0.0006 | 0.0004 | N |
| 20 | Qwen3.5 4B | 0.3116 | $0.0002 | 0.0001 | N |
| 21 | Qwen3.5 2B | 0.1850 | $0.0001 | 0.0001 | N |

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
**模型总数**: 143  