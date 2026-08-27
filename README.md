# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

## Pareto 前沿模型（综合能力从高到低）

| # | 模型 | 综合能力 | 单请求成本 | 归一化成本 | 推理 |
|---|------|---------|-----------|-----------|------|
| 1 | Claude Opus 5 (Adaptive Reasoning, Max Effort) | 0.9199 | 81162.87 | 1.0000 | N |
| 2 | Claude Opus 5 (Adaptive Reasoning, Xhigh Effort) | 0.9091 | 66406.05 | 0.8182 | N |
| 3 | Claude Opus 5 (Adaptive Reasoning, High Effort) | 0.8932 | 44950.16 | 0.5538 | N |
| 4 | Kimi K3 (max) | 0.8684 | 42823.02 | 0.5276 | N |
| 5 | Claude Opus 5 (Adaptive Reasoning, Medium Effort) | 0.8601 | 29355.96 | 0.3617 | N |
| 6 | Grok 4.6 (xhigh) | 0.8569 | 25519.55 | 0.3144 | N |
| 7 | Grok 4.6 (high) | 0.8544 | 24141.91 | 0.2975 | N |
| 8 | Grok 4.6 (medium) | 0.8431 | 21359.99 | 0.2632 | N |
| 9 | GLM-5.3 (max) | 0.8345 | 14580.83 | 0.1796 | N |
| 10 | Grok 4.5 (high) | 0.8028 | 12246.75 | 0.1509 | N |
| 11 | GLM-5.3-Flash | 0.7901 | 1616.69 | 0.0199 | N |
| 12 | Agnes 2.5 Pro Beta | 0.7101 | 927.43 | 0.0114 | N |
| 13 | MiMo-V2.5 | 0.6209 | 846.04 | 0.0104 | N |
| 14 | Ling 3.0 Flash | 0.5329 | 751.62 | 0.0093 | N |
| 15 | Qwen3.5 9B (Reasoning) | 0.4186 | 616.15 | 0.0076 | N |
| 16 | Qwen3.5 4B (Reasoning) | 0.4009 | 400.81 | 0.0049 | N |
| 17 | Qwen3.5 9B (Non-reasoning) | 0.3693 | 291.11 | 0.0036 | N |
| 18 | Qwen3.5 4B (Non-reasoning) | 0.3126 | 104.24 | 0.0013 | N |
| 19 | Gemma 4 E4B (Non-reasoning) | 0.2534 | 71.08 | 0.0009 | N |

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
| CacheHitRate | [AA Coding Agents](https://artificialanalysis.ai/agents/coding-agents) | 全部模型-Agent搭配的 `cacheHitRate` 求平均（57 个有效值，均值 = 0.9140），对所有模型统一使用 |
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
**模型总数**: 267  