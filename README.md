# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

## Pareto 前沿模型（综合能力从高到低）

| # | 模型 | 综合能力 | Intelligence Index成本 (USD) | 归一化成本 | 推理 |
|---|------|---------|---------------------------|-----------|------|
| 1 | GPT-5.5 (xhigh) | 0.9019 | $3357.00 | 1.0000 | Y |
| 2 | GPT-5.5 (high) | 0.8863 | $2159.38 | 0.6432 | Y |
| 3 | Gemini 3.1 Pro Preview | 0.8485 | $892.28 | 0.2658 | Y |
| 4 | MiniMax-M3 | 0.7746 | $308.34 | 0.0918 | Y |
| 5 | DeepSeek V4 Pro (Reasoning, Max Effort) | 0.7380 | $267.82 | 0.0798 | Y |
| 6 | MiMo-V2.5-Pro | 0.7215 | $160.82 | 0.0479 | Y |
| 7 | MiMo-V2.5 | 0.6937 | $49.30 | 0.0147 | Y |
| 8 | DeepSeek V4 Flash (Non-reasoning) | 0.4936 | $40.05 | 0.0119 | N |
| 9 | Gemma 4 31B (Non-reasoning) | 0.4652 | $19.43 | 0.0058 | N |
| 10 | gpt-oss-120b (low) | 0.3445 | $15.90 | 0.0047 | Y |
| 11 | gpt-oss-20B (low) | 0.2906 | $7.68 | 0.0023 | Y |
| 12 | Granite 4.1 8B | 0.1723 | $7.48 | 0.0022 | N |
| 13 | Granite 4.0 H Small | 0.1534 | $4.48 | 0.0013 | N |

### 评分方法

1. **18项评估指标**各自线性归一化到 [0,1]
2. **综合能力值** = 所有有效归一化分数的算术平均
3. **Pareto前沿** = 不被任何其他模型支配的模型

### 成本说明

**X轴成本 = AA 实测 Intelligence Index 运行成本**

成本数据来自 Artificial Analysis 的实测数据 (`intelligenceIndexCostTotal`)，
即运行完整的 AA Intelligence Index 基准测试套件的实际费用。
这比自行估算更准确，因为：
- 包含了 reasoning tokens 的实际收费
- 包含了 cache hit/input/output 的实际 token 分配
- 基于标准化的 benchmark 套件，可公平比较

### 数据来源

**数据来源**: [Artificial Analysis](https://artificialanalysis.ai/leaderboards/models)  
**方法论**: [AA Methodology](https://artificialanalysis.ai/methodology)  
**模型总数**: 207  