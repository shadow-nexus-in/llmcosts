# LiquidAI: LFM2-24B-A2B API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-08
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to LiquidAI: LFM2-24B-A2B
The LiquidAI: LFM2-24B-A2B model, released by Liquid on 2024-01-01, is a standard-tier language model that operates on a proprietary architecture. With 24 billion parameters, this model is positioned as a robust solution for various natural language processing tasks. Its primary strengths include a large context window of 32,768 tokens and the ability to generate up to 4,096 output tokens. The model's capabilities extend to text, function calling, JSON mode, streaming, and structured outputs, making it versatile for a wide range of applications.

### Technical Specifications and Use Cases
LiquidAI: LFM2-24B-A2B is best utilized for chat, text generation, coding, analysis, RAG pipelines, and summarization tasks, thanks to its advanced language understanding and generation capabilities. The model's pricing is based on input and output tokens, with costs set at $0.03 per 1M input tokens and $0.12 per 1M output tokens. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its competence in handling complex language tasks. However, it's essential to note the model's knowledge cutoff is 2023-12, which might limit its applicability to very recent events or developments.

### Cost Considerations and Competitors
For developers looking to integrate LiquidAI: LFM2-24B-A2B into their applications, cost considerations are crucial. The pricing model allows for flexible billing based on actual usage, with examples showing that 1,000 calls (avg 500 tokens) would cost approximately $0.0001, scaling up to $0.01 for 100,000 calls. While there are no direct competitors listed for this model, its unique blend of capabilities, such as function

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.03 |
| Output | $0.12 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for LiquidAI: LFM2-24B-A2B
#### Overview
The LiquidAI: LFM2-24B-A2B model is a standard, non-open source model provided by Liquid, released on January 1, 2024. This analysis will break down the cost structure, explain when to use cached tokens, discuss batch API savings, and calculate the cost at scale for 1,000, 10,000, and 100,000 API calls.

#### Cost Structure
The pricing for LiquidAI: LFM2-24B-A2B is as follows:
* Input: $0.03 per 1M tokens
* Output: $0.12 per 1M tokens
* Cached Input: $0.00 per 1M tokens (free)
* Batch Input: $0.00 per 1M tokens (free)

#### Using Cached Tokens
Cached tokens are free, making them an attractive option for reducing costs. If your application can utilize cached inputs, it is highly recommended to do so, as it can significantly lower your expenses.

#### Batch API Savings
Batch inputs are also free, which means that making batch API calls can help reduce costs associated with input tokens. However, the output cost remains the same, at $0.12 per 1M tokens.

#### Cost at Scale
The cost examples provided are:
* 1,000 calls (avg 500 tokens): $0.0001
* 10,000 calls: $0.001
* 100,000 calls: $0.01

To calculate the cost at scale, we need to understand that the cost is primarily driven by the number of tokens processed. However, the provided cost examples do not directly correlate with the token-based pricing. Assuming an average of 500 tokens per call, we can estimate the costs as follows:
* 1,000 calls: 500,000 tokens (input) *

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
See benchmark table for scores.

## Competitor Comparison


## Best Use Cases


## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
