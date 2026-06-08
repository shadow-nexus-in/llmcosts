# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-08
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, developed by Mistral AI, is a mid-tier language model released on 2025-04-17. This model is not open source. From an architectural standpoint, Mistral Medium 3 is designed to handle a wide range of tasks, including but not limited to coding, analysis, and vision tasks. Its capabilities extend to text and vision processing, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Strengths and Use Cases
The main strengths of Mistral Medium 3 lie in its ability to perform complex tasks such as coding, summarization, and content generation. It has a context window of 131,072 tokens and can generate up to 16,384 tokens as output. The model's performance is benchmarked with an MMLU score of 80.0, HumanEval score of 77.5, and an LMSYS Arena ELO of 1200. However, it is not suited for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms. The pricing model for Mistral Medium 3 includes $0.4 per 1M input tokens and $2.0 per 1M output tokens, with no specified costs for cached input or batch input.

### Cost Considerations and Competitors
For developers considering the cost of integrating Mistral Medium 3 into their projects, the pricing can be broken down into examples such as $1.2 for 1,000 calls averaging 500 tokens, $12.0 for 10,000 calls, and $120.0 for 100,000 calls. In comparison to its top competitors, Mistral Medium 3 is priced competitively, with Claude 3.5 Haiku charging $0.8/1M input and $4.0/1M output, and GPT-

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.4 |
| Output | $2.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Mistral Medium 3
#### Overview
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. It is not open source. The pricing structure is based on input and output tokens.

#### Cost Structure
The cost structure for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for repeated input queries. If your application involves frequent queries with the same or similar input, utilizing cached tokens can significantly reduce costs.

#### Batch API Savings
Batch input is also free, which means that batching API calls can help reduce the overall cost. By grouping multiple input queries into a single batch, you can take advantage of the free batch input pricing.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* 1,000 calls (avg 500 tokens): $1.2
* 10,000 calls: $12.0
* 100,000 calls: $120.0

To put these numbers into perspective, let's calculate the cost per call:
* 1,000 calls: $1.2 / 1,000 = $0.0012 per call
* 10,000 calls: $12.0 / 10,000 = $0.0012 per call
* 100,000 calls: $120.0 / 100,000 = $0.0012 per call

As shown, the cost per call remains constant at $0.0012, indicating a linear pricing model.

#### Comparison to Top Competitors
Mistral

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Medium 3 Benchmark Analysis
#### Overview
Mistral Medium 3, developed by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This analysis will delve into its benchmark performance, focusing on MMLU, HumanEval, and Arena ELO scores, to understand its capabilities and limitations in real-world applications.

#### Pricing Structure
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Context and Limits
Key context and limit specifications include:
* Context Window: **131,072 tokens**
* Max Output: **16,384 tokens**
* Knowledge Cutoff: **2024-11**

#### Benchmark Performance
The model's benchmark performance is highlighted by the following scores:
* **MMLU: 80.0** - The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to understand and generate human-like text across a wide range of tasks. A score of 80.0 indicates strong language understanding capabilities.
* **HumanEval: 77.5** - HumanEval assesses a model's ability to generate code that passes unit tests, reflecting its coding and problem-solving skills. A score of 77.5 suggests the model is proficient in coding tasks.
* **LMSYS Arena ELO: 1200** - The LMSYS Arena ELO score measures a model's performance in a competitive environment, where it

## Competitor Comparison
### Mistral Medium 3 Comparison
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This model is not open source and has a knowledge cutoff of 2024-11.

#### Pricing Comparison
The pricing for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens

In comparison to its top competitors:
* Claude 3.5 Haiku: $0.8/1M input, $4.0/1M output (2x input, 2x output)
* GPT-4o Mini: $0.15/1M input, $0.6/1M output (0.375x input, 0.3x output)

Mistral Medium 3 is more expensive than GPT-4o Mini but cheaper than Claude 3.5 Haiku in terms of input costs. However, the output cost of Mistral Medium 3 is higher than GPT-4o Mini but lower than Claude 3.5 Haiku.

#### Performance Trade-offs
The performance of Mistral Medium 3 is measured by the following benchmarks:
* MMLU: 80.0
* HumanEval: 77.5
* LMSYS Arena ELO: 1200

While the exact benchmarks for Claude 3.5 Haiku and GPT-4o Mini are not provided, the performance of Mistral Medium 3 can be considered in the context of its capabilities and limitations.

#### Capabilities and Limitations
Mistral Medium 3 supports the following capabilities:
* text
* vision
* function_calling
* json_mode
* streaming
* system_prompts

It is best suited for tasks such as:
* coding
* analysis
* rag
* summarization
* vision_tasks
* content_generation
* function_calling

However, it is not recommended for tasks that require:
* frontier_reasoning
* bulk_cheap_tasks
* simple_classification
* real_time_sub_100ms

#### Cost Examples
The cost of using Mistral Medium 3 can be estimated as follows:
* 1,000 calls (avg 500 tokens): $1

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful language model with a wide range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. Released on 2025-04-17, this model is best suited for tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling.

### Top 5 Best Use Cases for Mistral Medium 3
Based on its capabilities and limitations, here are the top 5 best use cases for Mistral Medium 3:

1. **Coding and Software Development**: With its high MMLU score of 80.0 and HumanEval score of 77.5, Mistral Medium 3 is well-suited for coding tasks, such as code completion, code review, and bug detection.
2. **Text Analysis and Summarization**: Mistral Medium 3's context window of 131,072 tokens and max output of 16,384 tokens make it ideal for text analysis and summarization tasks, such as summarizing long documents or analyzing large datasets.
3. **Vision Tasks**: With its vision capabilities, Mistral Medium 3 can be used for tasks such as image classification, object detection, and image generation.
4. **Content Generation**: Mistral Medium 3's content generation capabilities make it suitable for tasks such as writing articles, generating product descriptions, and creating social media posts.
5. **Function Calling and API Integration**: Mistral Medium 3's function calling capabilities allow it to integrate with external APIs and services, making it ideal for tasks such as data processing, data analysis, and automation.

### Code Integration Examples with OpenRouter
To integrate Mistral Medium 3 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Mistral Medium 3 model
model = openrouter.Mistral

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
