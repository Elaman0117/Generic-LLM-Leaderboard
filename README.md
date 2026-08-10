# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

## Pareto 前沿模型（综合能力从高到低）

| # | 模型 | 综合能力 | 单请求成本 | 归一化成本 | 推理 |
|---|------|---------|-----------|-----------|------|
| 1 | Claude Opus 5 (Adaptive Reasoning, Max Effort) | 0.9215 | 69973.59 | 1.0000 | N |
| 2 | Claude Opus 5 (Adaptive Reasoning, Xhigh Effort) | 0.9111 | 59009.96 | 0.8433 | N |
| 3 | Claude Opus 5 (Adaptive Reasoning, High Effort) | 0.8949 | 39042.16 | 0.5580 | N |
| 4 | Claude Opus 5 (Adaptive Reasoning, Medium Effort) | 0.8617 | 31557.16 | 0.4510 | N |
| 5 | Qwen3.8 Max | 0.8169 | 19107.19 | 0.2731 | N |
| 6 | Grok 4.5 (high) | 0.8043 | 11132.52 | 0.1591 | N |
| 7 | GPT-5.6 Luna (xhigh) | 0.7188 | 8955.62 | 0.1280 | N |
| 8 | MiniMax-M3 | 0.7157 | 3889.29 | 0.0556 | N |
| 9 | DeepSeek V4 Flash 0731 (Reasoning, Max Effort) | 0.7031 | 854.00 | 0.0122 | N |
| 10 | MiMo-V2.5 | 0.6224 | 854.00 | 0.0122 | N |
| 11 | Ling 3.0 Flash | 0.5340 | 755.10 | 0.0108 | N |
| 12 | Qwen3.5 9B (Reasoning) | 0.4204 | 623.98 | 0.0089 | N |
| 13 | Qwen3.5 4B (Reasoning) | 0.4020 | 402.55 | 0.0058 | N |
| 14 | Qwen3.5 9B (Non-reasoning) | 0.3704 | 301.27 | 0.0043 | N |
| 15 | Qwen3.5 4B (Non-reasoning) | 0.3136 | 106.40 | 0.0015 | N |
| 16 | Gemma 4 E4B (Non-reasoning) | 0.2542 | 74.16 | 0.0011 | N |

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
| CacheHitRate | [AA Coding Agents](https://artificialanalysis.ai/agents/coding-agents) | 全部模型-Agent搭配的 `cacheHitRate` 求平均（53 个有效值，均值 = 0.9082），对所有模型统一使用 |
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
**模型总数**: 240  