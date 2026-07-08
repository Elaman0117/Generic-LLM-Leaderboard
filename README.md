# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

## Pareto 前沿模型（综合能力从高到低）

| # | 模型 | 综合能力 | Intelligence Index成本 (USD) | 归一化成本 | 推理 |
|---|------|---------|---------------------------|-----------|------|
| 1 | Claude Fable 5 (Adaptive Reasoning, Max Effort, Opus 4.8 Fallback) | 0.9348 | $5630.52 | 1.0000 | N |
| 2 | GPT-5.5 (xhigh) | 0.8667 | $2630.04 | 0.4671 | N |
| 3 | GPT-5.5 (high) | 0.8443 | $1654.59 | 0.2939 | N |
| 4 | Gemini 3.5 Flash (high) | 0.8107 | $1040.88 | 0.1849 | N |
| 5 | GLM-5.2 (max) | 0.8047 | $820.38 | 0.1457 | N |
| 6 | Gemini 3.1 Pro Preview | 0.7879 | $815.11 | 0.1448 | N |
| 7 | MiniMax-M3 | 0.7311 | $203.86 | 0.0362 | N |
| 8 | DeepSeek V4 Pro (Reasoning, Max Effort) | 0.6991 | $176.34 | 0.0313 | N |
| 9 | Qwen3.7 Plus | 0.6735 | $149.47 | 0.0265 | N |
| 10 | MiMo-V2.5-Pro | 0.6714 | $98.47 | 0.0175 | N |
| 11 | DeepSeek V4 Flash (Reasoning, Max Effort) | 0.6363 | $74.31 | 0.0132 | N |
| 12 | Gemma 4 26B A4B (Reasoning) | 0.4403 | $51.92 | 0.0092 | N |
| 13 | HyperNova 60B 2605 | 0.3514 | $30.18 | 0.0054 | N |
| 14 | gpt-oss-20b (high) | 0.2817 | $29.87 | 0.0053 | N |
| 15 | Llama 4 Scout | 0.2114 | $11.39 | 0.0020 | N |

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
**模型总数**: 236  