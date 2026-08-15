# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

## Pareto 前沿模型（综合能力从高到低）

| # | 模型 | 综合能力 | 单请求成本 | 归一化成本 | 推理 |
|---|------|---------|-----------|-----------|------|
| 1 | Claude Opus 5 (Adaptive Reasoning, Max Effort) | 0.9199 | 100714.90 | 1.0000 | N |
| 2 | Claude Opus 5 (Adaptive Reasoning, Xhigh Effort) | 0.9093 | 74320.96 | 0.7379 | N |
| 3 | Claude Opus 5 (Adaptive Reasoning, High Effort) | 0.8932 | 50446.15 | 0.5009 | N |
| 4 | Kimi K3 (max) | 0.8679 | 42969.66 | 0.4266 | N |
| 5 | Claude Opus 5 (Adaptive Reasoning, Medium Effort) | 0.8597 | 31216.81 | 0.3100 | N |
| 6 | Grok 4.6 (high) | 0.8542 | 24514.39 | 0.2434 | N |
| 7 | Gemini 3.7 Flash (high) | 0.8189 | 15782.72 | 0.1567 | N |
| 8 | Grok 4.5 (high) | 0.8025 | 12267.65 | 0.1218 | N |
| 9 | Gemini 3.7 Flash (medium) | 0.7804 | 7569.97 | 0.0752 | N |
| 10 | Gemini 3.7 Flash (low) | 0.7428 | 3945.94 | 0.0392 | N |
| 11 | MiniMax-M3 | 0.7140 | 3888.13 | 0.0386 | N |
| 12 | DeepSeek V4 Flash 0731 (Reasoning, Max Effort) | 0.7020 | 3829.66 | 0.0380 | N |
| 13 | DeepSeek V4 Pro (Reasoning, High Effort) | 0.6541 | 2598.64 | 0.0258 | N |
| 14 | MiMo-V2.5 | 0.6206 | 853.50 | 0.0085 | N |
| 15 | Ling 3.0 Flash | 0.5325 | 754.88 | 0.0075 | N |
| 16 | Qwen3.5 9B (Reasoning) | 0.4185 | 623.48 | 0.0062 | N |
| 17 | Qwen3.5 4B (Reasoning) | 0.4009 | 402.44 | 0.0040 | N |
| 18 | Qwen3.5 9B (Non-reasoning) | 0.3693 | 301.12 | 0.0030 | N |
| 19 | Qwen3.5 4B (Non-reasoning) | 0.3126 | 105.48 | 0.0010 | N |
| 20 | Gemma 4 E4B (Non-reasoning) | 0.2534 | 73.27 | 0.0007 | N |

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
| CacheHitRate | [AA Coding Agents](https://artificialanalysis.ai/agents/coding-agents) | 全部模型-Agent搭配的 `cacheHitRate` 求平均（59 个有效值，均值 = 0.9085），对所有模型统一使用 |
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
**模型总数**: 253  