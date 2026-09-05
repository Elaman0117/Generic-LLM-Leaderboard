# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

## Pareto 前沿模型（综合能力从高到低）

| # | 模型 | 综合能力 | 单请求成本 | 归一化成本 | 推理 |
|---|------|---------|-----------|-----------|------|
| 1 | Claude Fable 5.1 (Adaptive Reasoning, Max Effort, Default Fallback) | 0.9264 | 952166.50 | 1.0000 | N |
| 2 | Claude Fable 5.1 (Adaptive Reasoning, Xhigh Effort, Default Fallback) | 0.9153 | 532817.54 | 0.5596 | N |
| 3 | Claude Opus 5 (Adaptive Reasoning, Max Effort) | 0.8935 | 156444.96 | 0.1643 | N |
| 4 | Claude Fable 5.1 (Adaptive Reasoning, High Effort, Default Fallback) | 0.8855 | 124594.18 | 0.1309 | N |
| 5 | Claude Opus 5 (Adaptive Reasoning, Xhigh Effort) | 0.8829 | 69647.69 | 0.0731 | N |
| 6 | Claude Opus 5 (Adaptive Reasoning, High Effort) | 0.8652 | 54070.35 | 0.0568 | N |
| 7 | Muse Spark 1.3 (max) | 0.8649 | 12935.13 | 0.0136 | N |
| 8 | Muse Spark 1.3 (xhigh) | 0.8604 | 12935.13 | 0.0136 | N |
| 9 | Muse Spark 1.2 (xhigh) | 0.7926 | 12935.13 | 0.0136 | N |
| 10 | Grok 4.5 (high) | 0.7712 | 11214.93 | 0.0118 | N |
| 11 | GLM-5.3-Flash | 0.7592 | 1601.32 | 0.0017 | N |
| 12 | Qwen3.8-Flash-Next | 0.7156 | 1433.69 | 0.0015 | N |
| 13 | MiMo-V2.5 | 0.6150 | 829.05 | 0.0009 | N |
| 14 | Ling 3.0 Flash | 0.4953 | 744.19 | 0.0008 | N |
| 15 | Qwen3.5 9B (Reasoning) | 0.4251 | 599.43 | 0.0006 | N |
| 16 | Qwen3.5 4B (Reasoning) | 0.3991 | 397.09 | 0.0004 | N |
| 17 | Qwen3.5 9B (Non-reasoning) | 0.3503 | 268.20 | 0.0003 | N |
| 18 | Qwen3.5 4B (Non-reasoning) | 0.3020 | 99.25 | 0.0001 | N |
| 19 | Gemma 4 E4B (Non-reasoning) | 0.2603 | 67.99 | 0.0001 | N |

### 评分方法

1. **18项评估指标**各自线性归一化到 [0,1]
2. **综合能力值** = 所有有效归一化分数的算术平均
3. **Pareto前沿** = 不被任何其他模型支配的模型

### 成本计算公式

**X轴成本 = 单请求估算成本（公式）**

```
cost = (CacheHitRate × CacheHitPrice × InputTokens)
     + ((1 − CacheHitRate) × CacheWritePrice × InputTokens)
     + (SpeedMedian × RealTime × OutputPrice)
```

**参数来源与处理逻辑：**

| 参数 | 来源 | 说明 |
|------|------|------|
| CacheHitRate | [AA Coding Agents](https://artificialanalysis.ai/agents/coding-agents) | 全部模型-Agent搭配的 `cacheHitRate` 求平均（68 个有效值，均值 = 0.9264），对所有模型统一使用 |
| CacheHitPrice | AA `cacheHitPrice` | 缓存命中的输入价格 (USD / 1M tokens) |
| CacheWritePrice | AA `cacheWritePrice` | 若缺失，回退到 `price1mInputTokens` (普通输入价格) |
| InputTokens | `10000` | AA 默认的 10k input-token 工作负载（[方法论](https://artificialanalysis.ai/methodology/performance-benchmarking)） |
| SpeedMedian | AA `medianOutputTokensPerSecond` | 输出速度中位数 (tokens/sec)，10k input-token 工作负载下测量 |
| OutputPrice | AA `price1mOutputTokens` | 输出价格 (USD / 1M tokens) |
| RealTime | 见下 | 生成输出 token 的实际耗时（秒） |

**RealTime 计算逻辑：**

- 如果存在 Reasoning Time（推理模型）：
  `RealTime = End-to-End Response Time Total − Latency First Chunk`
  = `medianEndToEndResponseTimeSeconds − medianTimeToFirstTokenSeconds`
- 如果 Reasoning Time 为 `--`（非推理模型）：
  `RealTime = End-to-End Response Time Total`
  = `medianEndToEndResponseTimeSeconds`

**单位说明：** AA 价格以 USD / 1M tokens 为单位，InputTokens 为原始计数（10000），Speed 为 tokens/sec，RealTime 为秒。公式按原样计算，不做单位换算。最终成本是一个相对得分（用于 Pareto 比较和线性归一化），不是真实的美元金额。

### 数据来源

**主数据源**: [Artificial Analysis Leaderboard](https://artificialanalysis.ai/leaderboards/models)  
**Cache Hit Rate 数据源**: [AA Coding Agents](https://artificialanalysis.ai/agents/coding-agents)  
**性能方法论**: [AA Performance Benchmarking](https://artificialanalysis.ai/methodology/performance-benchmarking)  
**模型总数**: 286  