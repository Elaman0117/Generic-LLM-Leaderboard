# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

## Pareto 前沿模型（综合能力从高到低）

| # | 模型 | 综合能力 | Intelligence Index成本 (USD) | 归一化成本 | 推理 |
|---|------|---------|---------------------------|-----------|------|
| 1 | Claude Fable 5 (Adaptive Reasoning, Max Effort, Opus 4.8 Fallback) | 0.9348 | $9939.80 | 1.0000 | Y |
| 2 | GPT-5.5 (xhigh) | 0.8751 | $3357.00 | 0.3377 | Y |
| 3 | GPT-5.5 (high) | 0.8565 | $2159.38 | 0.2172 | Y |
| 4 | Gemini 3.1 Pro Preview | 0.8228 | $892.28 | 0.0898 | Y |
| 5 | MiniMax-M3 | 0.7521 | $308.34 | 0.0310 | Y |
| 6 | DeepSeek V4 Pro (Reasoning, Max Effort) | 0.7152 | $267.82 | 0.0269 | Y |
| 7 | Grok 4.3 (medium) | 0.7009 | $161.48 | 0.0162 | Y |
| 8 | MiMo-V2.5-Pro | 0.7003 | $160.82 | 0.0162 | Y |
| 9 | MiMo-V2.5 | 0.6743 | $49.30 | 0.0050 | Y |
| 10 | DeepSeek V4 Flash (Non-reasoning) | 0.4796 | $40.05 | 0.0040 | N |
| 11 | Gemma 4 31B (Non-reasoning) | 0.4535 | $19.43 | 0.0020 | N |
| 12 | gpt-oss-120b (low) | 0.3365 | $15.90 | 0.0016 | Y |
| 13 | gpt-oss-20B (low) | 0.2842 | $7.68 | 0.0008 | Y |
| 14 | Granite 4.1 8B | 0.1682 | $7.48 | 0.0008 | N |
| 15 | Granite 4.0 H Small | 0.1492 | $4.48 | 0.0005 | N |

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
**模型总数**: 212  