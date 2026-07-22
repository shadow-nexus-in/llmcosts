# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-22
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance between performance and cost. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, this model is well-suited for a variety of tasks, including coding, analysis, and content generation. The model's architecture supports multiple capabilities, such as text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Specifications and Pricing
From a technical standpoint, Mistral Medium 3 has a knowledge cutoff of 2024-11 and has been benchmarked on several datasets, including MMLU (80.0), HumanEval (77.5), and LMSYS Arena ELO (1200). The pricing model for Mistral Medium 3 is as follows: $0.4 per 1M input tokens and $2.0 per 1M output tokens. There are no additional costs for cached input or batch input. To give developers a better understanding of the costs involved, some examples are provided: 1,000 calls (avg 500 tokens) cost $1.2, 10,000 calls cost $12.0, and 100,000 calls cost $120.0.

### Use Cases and Competitors
Mistral Medium 3 is best suited for tasks that require a balance between performance and cost, such as coding, analysis, and content generation. However, it may not be the best choice for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms. In comparison to its competitors, such as Claude 3.5 Haiku ($0.8/1M input, $4.0/1M output) and GPT-4o Mini ($0.15/1

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale for this model.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
- **Input**: $0.4 per 1M tokens
- **Output**: $2.0 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

This indicates that using cached input and batch processing can significantly reduce costs, as they are provided at no additional charge.

#### Optimal Usage Scenarios
- **Cached Tokens**: Since cached input is free, it is highly beneficial to utilize cached tokens whenever possible. This can significantly reduce the overall cost, especially for repeated or similar inputs.
- **Batch API Savings**: Batch processing is also free, making it an attractive option for processing large volumes of data. This can lead to substantial cost savings, especially when compared to processing individual requests.

#### Cost at Scale
The cost of using Mistral Medium 3 at different scales is as follows:
- **1,000 calls (avg 500 tokens)**: $1.2
- **10,000 calls**: $12.0
- **100,000 calls**: $120.0

These costs demonstrate a linear scaling of expenses with the number of API calls, indicating that the cost per call remains constant regardless of the volume.

#### Comparison with Competitors
Mistral Medium 3's pricing can be compared to its top competitors:
- **Claude 3.5 Haiku**: $0.8/1M input, $4.0/1M output
- **GPT-4o Mini**: $

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Mistral Medium 3 Benchmark Performance
#### Overview
Mistral Medium 3, a mid-tier model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on April 17, 2025, this model is not open source.

#### Pricing
The pricing for Mistral Medium 3 is as follows:
- Input: **$0.4 per 1M tokens**
- Output: **$2.0 per 1M tokens**
- Cached Input: **$None per 1M tokens**
- Batch Input: **$None per 1M tokens**

#### Context and Limits
Key context and limit specifications include:
- Context Window: **131,072 tokens**
- Max Output: **16,384 tokens**
- Knowledge Cutoff: **2024-11**

#### Benchmarks
The model's performance is benchmarked across several metrics:
- **MMLU (Massive Multitask Language Understanding)**: 80.0
  - MMLU measures a model's ability to understand and perform a wide range of natural language tasks. A higher score indicates better performance across these tasks.
- **HumanEval**: 77.5
  - HumanEval assesses a model's ability to understand and generate human-like code. This score suggests Mistral Medium 3 has a strong capability in coding tasks.
- **LMSYS Arena ELO**: 1200
  - The LMSYS Arena ELO score is a measure of a model's competitive performance in a variety of tasks, similar to a chess ELO rating. A score of 1200 places Mistral Medium 3 in a competitive range,

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will evaluate Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini, in terms of pricing, performance, and use cases.

#### Pricing Comparison
The pricing for each model is as follows:
* Mistral Medium 3:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* Claude 3.5 Haiku:
	+ Input: $0.8 per 1M tokens
	+ Output: $4.0 per 1M tokens
* GPT-4o Mini:
	+ Input: $0.15 per 1M tokens
	+ Output: $0.6 per 1M tokens

Mistral Medium 3 is more expensive than GPT-4o Mini but cheaper than Claude 3.5 Haiku in terms of input and output costs.

#### Performance Comparison
The performance of each model can be evaluated based on the provided benchmarks:
* Mistral Medium 3:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* Claude 3.5 Haiku and GPT-4o Mini benchmarks are not provided for direct comparison.

However, based on the available data, Mistral Medium 3 demonstrates strong performance in coding, analysis, and other tasks, with a high MMLU score and a moderate LMSYS Arena ELO rating.

#### Capabilities and Use Cases
Mistral Medium 3 supports a range of capabilities, including:
* Text
* Vision
* Function calling
* JSON mode
* Streaming
* System prompts

It is best suited for tasks such as:
* Coding
* Analysis
* RAG
* Summarization
* Vision tasks
* Content generation
* Function calling

On the other hand, it is not recommended for:
* Frontier reasoning
* Bulk cheap tasks
* Simple classification
* Real-time sub-100ms tasks

#### Cost Examples
The cost

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. It offers a balance of capabilities and pricing, making it suitable for a variety of applications. This guide will explore the top 5 best use cases for Mistral Medium 3, along with practical advice and code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Medium 3
Based on its capabilities and limitations, the top 5 use cases for Mistral Medium 3 are:

1. **Coding and Analysis**: With its strong performance in HumanEval (77.5) and MMLU (80.0), Mistral Medium 3 is well-suited for coding tasks, such as code completion, code review, and code analysis.
2. **Summarization and Content Generation**: Its capabilities in text and vision tasks make it an excellent choice for summarization, content generation, and text-based applications.
3. **RAG (Retrieval-Augmented Generation) Tasks**: Mistral Medium 3's ability to handle large context windows (131,072 tokens) and its performance in LMSYS Arena ELO (1200) make it suitable for RAG tasks, such as question answering and text retrieval.
4. **Vision Tasks**: With its support for vision tasks, Mistral Medium 3 can be used for image analysis, object detection, and image generation.
5. **Function Calling and JSON Mode**: Its ability to handle function calling and JSON mode makes it a good fit for applications that require interacting with external APIs or processing JSON data.

### Code Integration Examples with OpenRouter
To integrate Mistral Medium 3 with OpenRouter, you can use the following code examples:
```python
import openrouter

# Initialize the Mistral Medium 3 model
model = openrouter.Model("mistralai/mistral-medium-3")

# Example 

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
