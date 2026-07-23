# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-23
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance between performance and cost. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, this model is well-suited for a variety of tasks, including coding, analysis, and content generation. The model's architecture supports multiple capabilities, such as text, vision, function calling, JSON mode, streaming, and system prompts.

### Technical Specifications and Pricing
From a technical standpoint, Mistral Medium 3 has a knowledge cutoff of 2024-11 and has achieved notable benchmarks, including an MMLU score of 80.0 and a HumanEval score of 77.5. The model's pricing is as follows: $0.4 per 1M input tokens and $2.0 per 1M output tokens. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 100,000 calls would cost $120.0. Compared to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers competitive pricing, with Claude 3.5 Haiku costing $0.8/1M input and $4.0/1M output, and GPT-4o Mini costing $0.15/1M input and $0.6/1M output.

### Use Cases and Limitations
Mistral Medium 3 is best suited for tasks that require a balance between performance and cost, such as coding, analysis, and content generation. However, it may not be the best choice for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms. With its robust capabilities and competitive pricing, Mistral Medium 3 is a

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. It is not open source. This analysis will delve into the cost structure, optimal usage scenarios, and scalability of Mistral Medium 3.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
- **Input**: $0.4 per 1M tokens
- **Output**: $2.0 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
- **Cached Tokens**: Since cached input tokens are free, it is highly beneficial to utilize cached tokens whenever possible. This can significantly reduce costs, especially for applications with repetitive or similar input sequences.
- **Batch API Savings**: Although batch input is free, the primary cost savings come from reducing the number of API calls. By batching inputs, users can minimize the overhead costs associated with individual API calls, leading to more efficient and cost-effective usage.

#### Cost at Scale
The cost of using Mistral Medium 3 at different scales is as follows:
- **1,000 calls (avg 500 tokens)**: $1.2
- **10,000 calls**: $12.0
- **100,000 calls**: $120.0

These costs indicate a linear scaling of expenses with the number of API calls, suggesting that the cost per call remains constant regardless of the scale.

#### Competitor Comparison
Mistral Medium 3's pricing is competitive, especially considering its capabilities and performance benchmarks. For comparison:
- **Claude 3.5 Haiku**: $0.8/1M input, $4.0/1M output
- **GPT-4o Mini**: $0.15/

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
The Mistral Medium 3 model, provided by Mistral AI, is a mid-tier model released on 2025-04-17. It is not open source.

#### Pricing
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Context and Limits
The model has the following context and limits:
* Context Window: **131,072 tokens**
* Max Output: **16,384 tokens**
* Knowledge Cutoff: **2024-11**

#### Benchmarks
The model's benchmark performance is as follows:
* MMLU: **80.0**
* HumanEval: **77.5**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

#### Capabilities and Use Cases
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

However, it is not recommended for:
* frontier_reasoning
* bulk_cheap_tasks
* simple_classification
* real_time_sub_100ms

#### Cost Examples
The estimated costs for using Mistral Medium 3 are:
* 1,000 calls (avg 500 tokens):

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will delve into the pricing, performance, and capabilities of Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

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

Mistral Medium 3 is more expensive than GPT-4o Mini but cheaper than Claude 3.5 Haiku in terms of both input and output costs.

#### Performance Trade-offs
The performance of each model can be evaluated based on the provided benchmarks:
- **Mistral Medium 3**:
  - MMLU: 80.0
  - HumanEval: 77.5
  - LMSYS Arena ELO: 1200
- **Claude 3.5 Haiku** and **GPT-4o Mini** benchmarks are not provided for direct comparison.

Given the available data, Mistral Medium 3 demonstrates strong performance in coding and analysis tasks, as indicated by its HumanEval score. However, without direct comparisons for Claude 3.5 Haiku and GPT-4o Mini, the performance trade-offs are difficult to assess comprehensively.

#### Capabilities and Use Cases
Mistral Medium 3 supports a wide range of capabilities, including:
- Text
- Vision
- Function calling
- JSON mode
- Streaming
- System prompts

It is best suited for tasks such as:
- Coding
- Analysis
- RAG (Retrieval-Augmented Generation)
- Summarization
- Vision tasks
- Content generation
- Function calling

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful language model with a wide range of capabilities, including text and vision processing, function calling, and more. Released on 2025-04-17, this model is classified as mid-tier and is not open-source. In this guide, we will explore the top 5 best use cases for Mistral Medium 3, along with practical advice and code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Medium 3
Based on the capabilities and limitations of Mistral Medium 3, the following are the top 5 use cases for this model:

1. **Coding and Analysis**: With its strong performance in coding tasks, Mistral Medium 3 is ideal for code generation, analysis, and review. For example, you can use it to generate code snippets or analyze existing code for errors or improvements.
2. **Summarization and Content Generation**: Mistral Medium 3 excels in summarization and content generation tasks, making it suitable for applications such as text summarization, article generation, and chatbots.
3. **RAG (Retrieve, Augment, Generate) Tasks**: The model's ability to retrieve and generate text makes it well-suited for RAG tasks, such as answering complex questions or generating text based on a given prompt.
4. **Vision Tasks**: With its vision capabilities, Mistral Medium 3 can be used for tasks such as image classification, object detection, and image generation.
5. **Function Calling and JSON Mode**: The model's ability to call functions and process JSON data makes it ideal for applications such as data processing, API integration, and automation.

### Code Integration Examples with OpenRouter
To integrate Mistral Medium 3 with OpenRouter, you can use the following code examples:

```python
import openrouter

# Initialize the Mistral Medium 3 model
model = openrouter

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
