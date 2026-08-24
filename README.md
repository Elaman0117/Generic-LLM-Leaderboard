# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

## Pareto 前沿模型（综合能力从高到低）

| # | 模型 | 综合能力 | 单请求成本 | 归一化成本 | 推理 |
|---|------|---------|-----------|-----------|------|
| 1 | Claude Opus 5 (Adaptive Reasoning, Max Effort) | 0.9199 | 85109.92 | 1.0000 | N |
| 2 | Claude Opus 5 (Adaptive Reasoning, Xhigh Effort) | 0.9093 | 69765.86 | 0.8197 | N |
| 3 | Claude Opus 5 (Adaptive Reasoning, High Effort) | 0.8933 | 47057.18 | 0.5529 | N |
| 4 | Kimi K3 (max) | 0.8679 | 42884.25 | 0.5039 | N |
| 5 | Claude Opus 5 (Adaptive Reasoning, Medium Effort) | 0.8598 | 29602.07 | 0.3478 | N |
| 6 | Grok 4.6 (xhigh) | 0.8567 | 26873.11 | 0.3157 | N |
| 7 | Grok 4.6 (high) | 0.8545 | 26587.24 | 0.3124 | N |
| 8 | Grok 4.6 (medium) | 0.8428 | 19471.68 | 0.2288 | N |
| 9 | Qwen3.8 Max | 0.8152 | 19045.34 | 0.2238 | N |
| 10 | Grok 4.5 (high) | 0.8026 | 10496.82 | 0.1233 | N |
| 11 | Gemini 3.7 Flash (medium) | 0.7806 | 10403.43 | 0.1222 | N |
| 12 | Gemini 3.7 Flash (low) | 0.7429 | 4399.38 | 0.0517 | N |
| 13 | MiniMax-M3 | 0.7141 | 3878.16 | 0.0456 | N |
| 14 | DeepSeek V4 Flash 0731 (Reasoning, Max Effort) | 0.7022 | 3816.18 | 0.0448 | N |
| 15 | GPT-5.6 Luna (high) | 0.6843 | 2917.34 | 0.0343 | N |
| 16 | DeepSeek V4 Pro (Reasoning, High Effort) | 0.6542 | 2584.99 | 0.0304 | N |
| 17 | MiMo-V2.5 | 0.6207 | 849.15 | 0.0100 | N |
| 18 | Ling 3.0 Flash | 0.5326 | 752.98 | 0.0088 | N |
| 19 | Qwen3.5 9B (Reasoning) | 0.4185 | 619.21 | 0.0073 | N |
| 20 | Qwen3.5 4B (Reasoning) | 0.4009 | 401.49 | 0.0047 | N |
| 21 | Qwen3.5 9B (Non-reasoning) | 0.3693 | 291.80 | 0.0034 | N |
| 22 | Qwen3.5 4B (Non-reasoning) | 0.3126 | 103.76 | 0.0012 | N |
| 23 | Gemma 4 E4B (Non-reasoning) | 0.2534 | 71.11 | 0.0008 | N |

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
| CacheHitRate | [AA Coding Agents](https://artificialanalysis.ai/agents/coding-agents) | 全部模型-Agent搭配的 `cacheHitRate` 求平均（55 个有效值，均值 = 0.9117），对所有模型统一使用 |
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