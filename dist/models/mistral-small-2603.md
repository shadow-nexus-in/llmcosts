# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-22
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral: Mistral Small 4 is designed to handle a wide range of natural language processing tasks with its context window of 262,144 tokens and a maximum output of 4,096 tokens. Its knowledge cutoff is 2023-12, indicating that its training data includes information up to December 2023.

### Strengths and Use Cases
The main strengths of Mistral: Mistral Small 4 lie in its capabilities, which include text processing, function calling, JSON mode, streaming, and structured outputs. These capabilities make it best suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization. With a pricing model that charges $0.15 per 1M tokens for input and $0.6 per 1M tokens for output, it offers a cost-effective solution for developers looking to integrate advanced language processing into their applications. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, demonstrating its competence in various linguistic tasks.

### Pricing and Cost Considerations
To plan the integration of Mistral: Mistral Small 4 into a project, developers should consider the pricing structure. The cost of using this model can be estimated based on the number of calls and the average number of tokens per call. For example, 1,000 calls with an average of 500 tokens per call would cost $0.375, scaling up to $3.75 for 10,000 calls and $37.5 for 100,000 calls. Given that there are no direct competitors listed, Mistral: Mistral Small 4 presents a unique

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.15 |
| Output | $0.6 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Mistral Small 4 Pricing Analysis
#### Overview
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. This analysis will delve into the cost structure, usage scenarios, and cost savings opportunities for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$0.00 per 1M tokens** (free)
* Batch Input: **$0.00 per 1M tokens** (free)

#### Usage Scenarios
To optimize costs, consider the following scenarios:
* **Cached Tokens**: Use cached input tokens when possible, as they are **free**. This can significantly reduce costs for repeated input sequences.
* **Batch API**: Utilize batch input for multiple requests, as it is also **free**. This can lead to substantial savings for large-scale API calls.

#### Cost at Scale
The costs for Mistral Small 4 at various scales are:
* **1,000 calls (avg 500 tokens)**: **$0.375**
* **10,000 calls**: **$3.75**
* **100,000 calls**: **$37.5**

These costs are based on the average token count per call and can be adjusted according to specific use cases.

#### Context and Limits
Keep in mind the following context and limits when using Mistral Small 4:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12

#### Conclusion
Mistral Small 4 offers a competitive pricing structure, with opportunities for cost savings through cached input tokens and batch API calls. By understanding the cost structure and optimizing usage scenarios, developers can effectively

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Analysis
#### Overview
The Mistral Small 4 model, provided by Mistralai, is a standard-tier language model released on January 1, 2024. This model is not open source.

#### Pricing
The pricing for Mistral Small 4 is as follows:
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Context and Limits
The model has the following context and limits:
* Context Window: **262,144 tokens**
* Max Output: **4,096 tokens**
* Knowledge Cutoff: **2023-12**

#### Benchmarks
The benchmark performance of Mistral Small 4 is:
* MMLU: **80.0** - This score indicates the model's performance on a set of tasks that measure its ability to understand and generate human-like language. A higher MMLU score generally corresponds to better language understanding and generation capabilities.
* HumanEval: **None** - This benchmark evaluates a model's ability to generate correct code in response to a set of programming prompts. The lack of a HumanEval score makes it difficult to assess the model's coding abilities.
* LMSYS Arena ELO: **1200** - This score represents the model's performance in a competitive arena, where it is pitted against other models in a series of tasks. A higher ELO score indicates better overall performance.
* GSM8K: **None** - This benchmark assesses a model's ability to reason about mathematical concepts and solve problems. The

## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral Small 4 model, we will provide a general comparison framework that can be applied to other models in the market. This framework will cover price differences, performance trade-offs, and scenarios where one might choose the Mistral Small 4 over other models.

#### Pricing Comparison
The pricing for the Mistral Small 4 is as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens

To compare, let's consider hypothetical competitors:
- **Competitor A**: Input at $0.10 per 1M tokens, Output at $0.55 per 1M tokens
- **Competitor B**: Input at $0.20 per 1M tokens, Output at $0.65 per 1M tokens

The Mistral Small 4 is more expensive than Competitor A but cheaper than Competitor B in terms of input costs. For output costs, it is more expensive than Competitor A but cheaper than Competitor B.

#### Performance Trade-offs
Given the benchmarks:
- MMLU: 80.0
- LMSYS Arena ELO: 1200

Without direct competitors, we'll discuss general trade-offs:
- **Performance vs. Cost**: Higher performance models might cost more per token but offer better results. If a task requires high accuracy, a more expensive model might be preferable.
- **Context Window and Max Output**: The Mistral Small 4 has a context window of 262,144 tokens and a max output of 4,096 tokens. Models with larger context windows or higher max output capabilities might be more suitable for tasks requiring longer input or output sequences.

#### Choosing the Mistral Small 4
Consider the Mistral Small 4 for the following scenarios:
- **Balanced Performance and Cost**: When you need a model that offers a good balance between performance and cost. The Mistral Small 4's pricing and benchmarks suggest it can handle a variety of tasks without being overly expensive.
- **Specific Capabilities**: The model supports text, function calling, JSON mode, streaming, and structured outputs, making it versatile for chat, text generation, coding, analysis, and summarization tasks.

#### Conclusion
The Mistral Small 4, with its unique set of capabilities and pricing, can be a valuable choice for many applications

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on 2024-01-01, this model is part of the standard tier and is not open source.

### Pricing Model
The pricing model for Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its ability to generate human-like text, Mistral Small 4 is ideal for chat applications, content generation, and language translation.
2. **Coding and Analysis**: Mistral Small 4's function calling and structured outputs capabilities make it suitable for coding tasks, such as code completion, code review, and data analysis.
3. **Summarization and RAG Pipelines**: The model's ability to process large amounts of text and generate concise summaries makes it a good fit for summarization tasks and RAG (Retrieve, Augment, Generate) pipelines.
4. **Text-Based Applications**: Mistral Small 4 can be used to build text-based applications, such as text-based games, interactive stories, and conversational interfaces.
5. **Data Processing and Streaming**: With its support for streaming and structured outputs, Mistral Small 4 can be used for real-time data processing, data streaming, and event-driven applications.

### Code Integration Example with OpenRouter
Here is an example of how to integrate Mistral Small 4 with OpenRouter:
```python
import openrouter

# Initialize

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
