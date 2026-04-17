# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-17
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Overview of Mistral Medium 3
Mistral Medium 3, developed by Mistral AI, is a mid-tier language model released on 2025-04-17. This model is not open source. From an architectural standpoint, Mistral Medium 3 boasts a context window of 131,072 tokens and can generate up to 16,384 tokens as output. Its knowledge cutoff is 2024-11, indicating that it may not be aware of events or developments after this date. The model's capabilities include text and vision processing, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for various applications.

### Strengths and Use Cases
Mistral Medium 3 demonstrates its strengths through its benchmark scores: 80.0 on MMLU, 77.5 on HumanEval, and an LMSYS Arena ELO of 1200. These scores suggest the model's proficiency in coding, analysis, and other complex tasks. It is best suited for tasks such as coding, analysis, RAG (Retrieve, Augment, Generate), summarization, vision tasks, content generation, and function calling. However, it may not be the optimal choice for frontier reasoning, bulk cheap tasks, simple classification, or real-time applications requiring responses under 100ms. The model's pricing is $0.4 per 1M input tokens and $2.0 per 1M output tokens, with no specified costs for cached input or batch input.

### Pricing and Competitors
The cost of using Mistral Medium 3 can be estimated based on the number of calls and tokens. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 10,000 calls would amount to $12.0, and 100,000 calls would total $120.0. In comparison to its competitors, Mistral Medium 3 is priced lower than Claude 3

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.4 |
| Output | $2.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Detailed Pricing Analysis for Mistral Medium 3
#### Overview
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This model is not open source.

#### Cost Structure
The cost structure for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs when the same input is used multiple times. Since cached input is free, it is recommended to use cached tokens whenever possible to minimize costs.

#### Batch API Savings
Batching API calls can also help reduce costs. However, the pricing data does not provide a specific discount for batch API calls. The cost of batch input is **$0 per 1M tokens**, which is the same as cached input.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: **$1.2**
* **10,000 calls**: **$12.0**
* **100,000 calls**: **$120.0**

To calculate the cost at scale, we can use the following formula:
Cost = (Number of calls \* Average tokens per call) \* (Input cost per 1M tokens + Output cost per 1M tokens) / 1,000,000

For example, for 1,000 calls with an average of 500 tokens per call:
Cost = (1,000 \* 500) \* (0.4 + 2.0) / 1,000,000 = $1.2



## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Medium 3 Benchmark Performance Analysis
#### Model Overview
The Mistral Medium 3 model, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. The model's knowledge cutoff is 2024-11.

#### Pricing
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Benchmark Scores
The model's benchmark performance is measured by the following scores:
* **MMLU: 80.0** - The MMLU (Massive Multitask Language Understanding) score measures the model's ability to perform a wide range of natural language processing tasks. A higher score indicates better performance.
* **HumanEval: 77.5** - The HumanEval score measures the model's ability to evaluate and execute human-written code. A higher score indicates better performance.
* **LMSYS Arena ELO: 1200** - The LMSYS Arena ELO score measures the model's performance in a competitive arena, where models are pitted against each other to complete tasks. A higher score indicates better performance.

#### Real-World Implications
The benchmark scores indicate that Mistral Medium 3 is a capable model for a variety of tasks, including:
* Coding: The model's high HumanEval score suggests that it is well-suited for tasks that involve evaluating and executing human-written code

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a unique set of capabilities and pricing. This comparison will delve into the details of Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini, highlighting price differences, performance trade-offs, and scenarios where each model is the best choice.

#### Pricing Comparison
The pricing for each model is as follows:
- **Mistral Medium 3**:
  - Input: $0.4 per 1M tokens
  - Output: $2.0 per 1M tokens
- **Claude 3.5 Haiku**:
  - Input: $0.8 per 1M tokens
  - Output: $4.0 per 1M tokens
- **GPT-4o Mini**:
  - Input: $0.15 per 1M tokens
  - Output: $0.6 per 1M tokens

#### Performance Trade-offs
- **Mistral Medium 3**: Offers a balance between input and output costs, with a context window of 131,072 tokens and max output of 16,384 tokens. Its benchmarks include MMLU: 80.0, HumanEval: 77.5, and LMSYS Arena ELO: 1200.
- **Claude 3.5 Haiku**: Has higher input and output costs compared to Mistral Medium 3 but may offer superior performance in certain tasks, given its higher pricing.
- **GPT-4o Mini**: Significantly cheaper for both input and output, making it an attractive option for bulk or cost-sensitive tasks, but its performance might not match that of Mistral Medium 3 or Claude 3.5 Haiku in complex tasks.

#### Capabilities and Best Use Cases
- **Mistral Medium 3**: Suitable for coding, analysis, RAG, summarization, vision tasks, content generation, and function calling, thanks to its capabilities in text, vision, function calling, JSON mode, streaming, and system prompts.
- **Claude 3.5 Haiku** and **GPT-4o Mini**: While specific capabilities are not listed, their pricing suggests Claude 3.5 Haiku might be geared towards high-end applications

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. This model is best suited for tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling.

### Top 5 Best Use Cases for Mistral Medium 3
Based on its capabilities and limitations, here are the top 5 best use cases for Mistral Medium 3:

1. **Coding and Development**: With its strong coding capabilities, Mistral Medium 3 can be used for code generation, code completion, and code review. For example, you can use it to generate boilerplate code for a new project or to complete partially written code.
2. **Text Analysis and Summarization**: Mistral Medium 3 can be used for text analysis, summarization, and RAG (Retrieve, Augment, Generate) tasks. It can summarize long documents, extract key points, and even generate new content based on the input text.
3. **Vision Tasks**: With its vision capabilities, Mistral Medium 3 can be used for image classification, object detection, and image generation. For example, you can use it to classify images into different categories or to detect objects within an image.
4. **Content Generation**: Mistral Medium 3 can be used for content generation, such as generating articles, blog posts, or social media posts. It can also be used to generate creative content, such as stories or poems.
5. **Function Calling and API Integration**: With its function calling capabilities, Mistral Medium 3 can be used to integrate with external APIs and services. For example, you can use it to call APIs to retrieve data or to send data to external services.

### Code Integration Examples with OpenRouter
Here are

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
