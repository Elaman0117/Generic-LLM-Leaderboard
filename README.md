# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

## Pareto 前沿模型（综合能力从高到低）

| # | 模型 | 综合能力 | 单请求成本 | 归一化成本 | 推理 |
|---|------|---------|-----------|-----------|------|
| 1 | Claude Opus 5 (Adaptive Reasoning, Max Effort) | 0.9199 | 121639.49 | 1.0000 | N |
| 2 | Claude Opus 5 (Adaptive Reasoning, Xhigh Effort) | 0.9095 | 56761.35 | 0.4666 | N |
| 3 | Claude Opus 5 (Adaptive Reasoning, High Effort) | 0.8936 | 49173.76 | 0.4043 | N |
| 4 | Kimi K3 (max) | 0.8683 | 42823.02 | 0.3520 | N |
| 5 | Claude Opus 5 (Adaptive Reasoning, Medium Effort) | 0.8604 | 28141.44 | 0.2314 | N |
| 6 | Grok 4.6 (xhigh) | 0.8572 | 23753.17 | 0.1953 | N |
| 7 | Grok 4.6 (medium) | 0.8433 | 21484.86 | 0.1766 | N |
| 8 | GLM-5.3 (max) | 0.8347 | 14580.83 | 0.1199 | N |
| 9 | Grok 4.5 (high) | 0.8031 | 12184.02 | 0.1002 | N |
| 10 | GLM-5.3-Flash | 0.7902 | 1616.69 | 0.0133 | N |
| 11 | Qwen3.8-Flash-Next | 0.7569 | 1450.29 | 0.0119 | N |
| 12 | Agnes 2.5 Pro Beta | 0.7104 | 927.43 | 0.0076 | N |
| 13 | MiMo-V2.5 | 0.6210 | 846.04 | 0.0070 | N |
| 14 | Ling 3.0 Flash | 0.5331 | 751.62 | 0.0062 | N |
| 15 | Qwen3.5 9B (Reasoning) | 0.4187 | 616.15 | 0.0051 | N |
| 16 | Qwen3.5 4B (Reasoning) | 0.4009 | 400.81 | 0.0033 | N |
| 17 | Qwen3.5 9B (Non-reasoning) | 0.3693 | 289.75 | 0.0024 | N |
| 18 | Qwen3.5 4B (Non-reasoning) | 0.3126 | 104.03 | 0.0009 | N |
| 19 | Gemma 4 E4B (Non-reasoning) | 0.2534 | 70.86 | 0.0006 | N |

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
**模型总数**: 269  