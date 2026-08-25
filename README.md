# LLM Leaderboard Pareto Analysis

![Pareto Analysis](output/pareto_analysis.png)

## Pareto 前沿模型（综合能力从高到低）

| # | 模型 | 综合能力 | 单请求成本 | 归一化成本 | 推理 |
|---|------|---------|-----------|-----------|------|
| 1 | Claude Opus 5 (Adaptive Reasoning, Max Effort) | 0.9199 | 102451.19 | 1.0000 | N |
| 2 | Claude Opus 5 (Adaptive Reasoning, Xhigh Effort) | 0.9097 | 76347.10 | 0.7452 | N |
| 3 | Claude Opus 5 (Adaptive Reasoning, High Effort) | 0.8934 | 52917.35 | 0.5165 | N |
| 4 | Kimi K3 (max) | 0.8682 | 42884.25 | 0.4186 | N |
| 5 | Claude Opus 5 (Adaptive Reasoning, Medium Effort) | 0.8600 | 31308.26 | 0.3056 | N |
| 6 | Grok 4.6 (xhigh) | 0.8570 | 27131.10 | 0.2648 | N |
| 7 | Grok 4.6 (high) | 0.8547 | 25543.62 | 0.2493 | N |
| 8 | Grok 4.6 (medium) | 0.8432 | 21513.42 | 0.2100 | N |
| 9 | GLM-5.3 (max) | 0.8345 | 14606.68 | 0.1426 | N |
| 10 | Grok 4.5 (high) | 0.8027 | 11163.31 | 0.1090 | N |
| 11 | Gemini 3.7 Flash (medium) | 0.7809 | 9516.57 | 0.0929 | N |
| 12 | Gemini 3.7 Flash (low) | 0.7434 | 4633.52 | 0.0452 | N |
| 13 | MiniMax-M3 | 0.7142 | 3878.16 | 0.0379 | N |
| 14 | DeepSeek V4 Flash 0731 (Reasoning, Max Effort) | 0.7027 | 3816.18 | 0.0372 | N |
| 15 | DeepSeek V4 Flash Vision (Reasoning, Max Effort) | 0.6986 | 3816.18 | 0.0372 | N |
| 16 | GPT-5.6 Luna (high) | 0.6846 | 3083.46 | 0.0301 | N |
| 17 | DeepSeek V4 Pro (Reasoning, High Effort) | 0.6545 | 2584.99 | 0.0252 | N |
| 18 | MiMo-V2.5 | 0.6209 | 849.15 | 0.0083 | N |
| 19 | Ling 3.0 Flash | 0.5328 | 752.98 | 0.0073 | N |
| 20 | Qwen3.5 9B (Reasoning) | 0.4186 | 619.21 | 0.0060 | N |
| 21 | Qwen3.5 4B (Reasoning) | 0.4009 | 401.49 | 0.0039 | N |
| 22 | Qwen3.5 9B (Non-reasoning) | 0.3693 | 292.39 | 0.0029 | N |
| 23 | Qwen3.5 4B (Non-reasoning) | 0.3126 | 103.54 | 0.0010 | N |
| 24 | Gemma 4 E4B (Non-reasoning) | 0.2534 | 71.19 | 0.0007 | N |

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
**模型总数**: 263  