# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

## Pareto 前沿模型（综合能力从高到低）

| # | 模型 | 综合能力 | 单请求成本 | 归一化成本 | 推理 |
|---|------|---------|-----------|-----------|------|
| 1 | Claude Fable 5 (Adaptive Reasoning, Max Effort, Opus 4.8 Fallback) | 0.9254 | 344926.98 | 1.0000 | N |
| 2 | GPT-5.6 Sol (xhigh) | 0.8720 | 124902.89 | 0.3621 | N |
| 3 | GPT-5.6 Sol (high) | 0.8511 | 81665.22 | 0.2368 | N |
| 4 | GPT-5.6 Sol (medium) | 0.8275 | 34328.79 | 0.0995 | N |
| 5 | Grok 4.5 (high) | 0.8203 | 18569.02 | 0.0538 | N |
| 6 | GLM-5.2 (max) | 0.7890 | 14772.21 | 0.0428 | N |
| 7 | Muse Spark 1.1 (xhigh) | 0.7776 | 13256.08 | 0.0384 | N |
| 8 | MiniMax-M3 | 0.7268 | 3923.90 | 0.0114 | N |
| 9 | DeepSeek V4 Pro (Reasoning, High Effort) | 0.6655 | 2647.63 | 0.0077 | N |
| 10 | MiMo-V2.5 | 0.6302 | 869.08 | 0.0025 | N |
| 11 | Gemma 4 12B (Reasoning) | 0.4457 | 852.83 | 0.0025 | N |
| 12 | DeepSeek V4 Flash (Non-reasoning) | 0.4299 | 343.94 | 0.0010 | N |
| 13 | Gemma 4 12B (Non-reasoning) | 0.3264 | 340.02 | 0.0010 | N |
| 14 | Qwen3.5 4B (Non-reasoning) | 0.3136 | 108.66 | 0.0003 | N |

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
| CacheHitRate | [AA Coding Agents](https://artificialanalysis.ai/agents/coding-agents) | 全部模型-Agent搭配的 `cacheHitRate` 求平均（43 个有效值，均值 = 0.8972），对所有模型统一使用 |
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
**模型总数**: 261  