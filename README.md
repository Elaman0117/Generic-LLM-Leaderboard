# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

## Pareto 前沿模型（综合能力从高到低）

| # | 模型 | 综合能力 | 单请求成本 | 归一化成本 | 推理 |
|---|------|---------|-----------|-----------|------|
| 1 | Claude Opus 5 (Adaptive Reasoning, Max Effort) | 0.9199 | 110560.80 | 1.0000 | N |
| 2 | Claude Opus 5 (Adaptive Reasoning, Xhigh Effort) | 0.9093 | 59256.46 | 0.5360 | N |
| 3 | Claude Opus 5 (Adaptive Reasoning, High Effort) | 0.8932 | 39716.03 | 0.3592 | N |
| 4 | Claude Opus 5 (Adaptive Reasoning, Medium Effort) | 0.8597 | 33372.59 | 0.3018 | N |
| 5 | Grok 4.6 (high) | 0.8544 | 21990.64 | 0.1989 | N |
| 6 | Gemini 3.7 Flash (high) | 0.8189 | 15781.70 | 0.1427 | N |
| 7 | Grok 4.5 (high) | 0.8025 | 10934.56 | 0.0989 | N |
| 8 | Gemini 3.7 Flash (medium) | 0.7804 | 7568.94 | 0.0685 | N |
| 9 | Gemini 3.7 Flash (low) | 0.7428 | 3944.92 | 0.0357 | N |
| 10 | DeepSeek V4 Pro 0813 (Reasoning, Max Effort) | 0.7347 | 2605.17 | 0.0236 | N |
| 11 | DeepSeek V4 Flash 0731 (Reasoning, Max Effort) | 0.7020 | 853.29 | 0.0077 | N |
| 12 | MiMo-V2.5 | 0.6206 | 853.29 | 0.0077 | N |
| 13 | Ling 3.0 Flash | 0.5325 | 754.79 | 0.0068 | N |
| 14 | Qwen3.5 9B (Reasoning) | 0.4185 | 623.28 | 0.0056 | N |
| 15 | Qwen3.5 4B (Reasoning) | 0.4009 | 402.40 | 0.0036 | N |
| 16 | Qwen3.5 9B (Non-reasoning) | 0.3693 | 298.53 | 0.0027 | N |
| 17 | Qwen3.5 4B (Non-reasoning) | 0.3126 | 104.97 | 0.0009 | N |
| 18 | Gemma 4 E4B (Non-reasoning) | 0.2534 | 73.54 | 0.0007 | N |

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
| CacheHitRate | [AA Coding Agents](https://artificialanalysis.ai/agents/coding-agents) | 全部模型-Agent搭配的 `cacheHitRate` 求平均（55 个有效值，均值 = 0.9087），对所有模型统一使用 |
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
**模型总数**: 252  