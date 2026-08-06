# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

## Pareto 前沿模型（综合能力从高到低）

| # | 模型 | 综合能力 | 单请求成本 | 归一化成本 | 推理 |
|---|------|---------|-----------|-----------|------|
| 1 | Claude Opus 5 (Adaptive Reasoning, Max Effort) | 0.9264 | 98868.52 | 1.0000 | N |
| 2 | Claude Opus 5 (Adaptive Reasoning, Xhigh Effort) | 0.9136 | 77809.28 | 0.7870 | N |
| 3 | Claude Opus 5 (Adaptive Reasoning, High Effort) | 0.8946 | 52479.93 | 0.5308 | N |
| 4 | Kimi K3 (max) | 0.8630 | 42943.11 | 0.4343 | N |
| 5 | Claude Opus 5 (Adaptive Reasoning, Medium Effort) | 0.8617 | 32931.83 | 0.3331 | N |
| 6 | Qwen3.8 Max | 0.8232 | 19083.49 | 0.1930 | N |
| 7 | Grok 4.5 (high) | 0.8119 | 11018.26 | 0.1114 | N |
| 8 | GPT-5.6 Luna (xhigh) | 0.7301 | 9918.23 | 0.1003 | N |
| 9 | MiniMax-M3 | 0.7212 | 3885.03 | 0.0393 | N |
| 10 | DeepSeek V4 Flash 0731 (Reasoning, Max Effort) | 0.7078 | 852.15 | 0.0086 | N |
| 11 | MiMo-V2.5 | 0.6264 | 852.15 | 0.0086 | N |
| 12 | Ling-3.0-flash | 0.5414 | 754.29 | 0.0076 | N |
| 13 | DeepSeek V4 Flash (Non-reasoning) | 0.4292 | 337.75 | 0.0034 | N |
| 14 | Gemma 4 12B (Non-reasoning) | 0.3257 | 314.53 | 0.0032 | N |
| 15 | Qwen3.5 4B (Non-reasoning) | 0.3129 | 105.13 | 0.0011 | N |
| 16 | Gemma 4 E4B (Non-reasoning) | 0.2537 | 74.73 | 0.0008 | N |

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
| CacheHitRate | [AA Coding Agents](https://artificialanalysis.ai/agents/coding-agents) | 全部模型-Agent搭配的 `cacheHitRate` 求平均（52 个有效值，均值 = 0.9095），对所有模型统一使用 |
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
**模型总数**: 254  