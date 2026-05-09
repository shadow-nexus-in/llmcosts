# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-09
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance of performance and cost. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, this model is well-suited for a variety of tasks, including coding, analysis, and content generation. The model's architecture supports multiple capabilities, such as text, vision, function calling, JSON mode, streaming, and system prompts.

### Technical Specifications and Pricing
From a technical standpoint, Mistral Medium 3 has a knowledge cutoff of 2024-11 and has achieved notable benchmarks, including an MMLU score of 80.0 and a HumanEval score of 77.5. The model's pricing is as follows: $0.4 per 1M input tokens and $2.0 per 1M output tokens. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 10,000 calls would cost $12.0, and 100,000 calls would cost $120.0. In comparison to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers competitive pricing for its input and output tokens.

### Use Cases and Limitations
Mistral Medium 3 is best suited for tasks that require a balance of complexity and cost-effectiveness, such as coding, analysis, and vision tasks. However, it is not recommended for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms. With its robust capabilities and competitive pricing, Mistral Medium 3 is a viable option for developers looking for a mid-tier model that can handle a variety of tasks. By understanding the model's strengths, limitations, and pricing, developers can make informed

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
* **Input**: $0.4 per 1M tokens
* **Output**: $2.0 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
* **Cached Tokens**: Since cached input tokens are free, it's advisable to utilize cached tokens whenever possible to minimize costs.
* **Batch API Savings**: Although batch input is free, the primary cost savings come from minimizing output tokens, as output is significantly more expensive than input.

#### Cost at Scale
The cost examples provided are as follows:
* **1,000 calls (avg 500 tokens)**: $1.2
* **10,000 calls**: $12.0
* **100,000 calls**: $120.0

To understand the cost structure better, let's calculate the cost per call based on the average tokens per call:
* Assuming an average of 500 tokens per call, the total tokens for 1,000 calls would be 500,000 tokens.
* Given the input cost is $0.4 per 1M tokens, the input cost for 500,000 tokens would be $0.2.
* Since output is $2.0 per 1M tokens and assuming the average output is significantly less than the input (due to the context window and max output limits), the output cost will dominate the total cost.

#### Comparison with Competitors
Mistral Medium 3's pricing is compared to its

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
The Mistral Medium 3 model, released by Mistral AI on 2025-04-17, is a mid-tier model with the following key characteristics:
* **Tier**: Mid
* **Open Source**: False
* **Context Window**: 131,072 tokens
* **Max Output**: 16,384 tokens
* **Knowledge Cutoff**: 2024-11

#### Pricing
The pricing for Mistral Medium 3 is as follows:
* **Input**: $0.4 per 1M tokens
* **Output**: $2.0 per 1M tokens
* **Cached Input**: $None per 1M tokens
* **Batch Input**: $None per 1M tokens

#### Benchmark Performance
The model's benchmark performance is measured by the following metrics:
* **MMLU (Massive Multitask Language Understanding)**: 80.0
* **HumanEval**: 77.5
* **LMSYS Arena ELO**: 1200
* **GSM8K**: None

These benchmarks indicate the model's performance in various tasks:
* **MMLU**: Measures the model's ability to understand and generate human-like text. A higher score indicates better performance. With a score of 80.0, Mistral Medium 3 demonstrates strong language understanding capabilities.
* **HumanEval**: Evaluates the model's ability to write correct and functional code. A higher score indicates better performance. With a score of 77.5, Mistral Medium 3 shows promising code generation capabilities.
* **LMSYS Arena ELO**: Measures the model's performance in a competitive

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will examine the pricing, performance, and capabilities of Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

#### Pricing Comparison
The pricing for each model is as follows:
* Mistral Medium 3:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* Claude 3.5 Haiku:
	+ Input: $0.8 per 1M tokens (100% more than Mistral Medium 3)
	+ Output: $4.0 per 1M tokens (100% more than Mistral Medium 3)
* GPT-4o Mini:
	+ Input: $0.15 per 1M tokens (62.5% less than Mistral Medium 3)
	+ Output: $0.6 per 1M tokens (70% less than Mistral Medium 3)

#### Performance Comparison
The performance benchmarks for each model are:
* Mistral Medium 3:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* Claude 3.5 Haiku: Not provided
* GPT-4o Mini: Not provided

#### Capabilities and Use Cases
Mistral Medium 3 supports the following capabilities:
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
However, it is not recommended for:
* Frontier reasoning
* Bulk cheap tasks
* Simple classification
* Real-time sub-100ms tasks

#### Cost Examples
The estimated costs for using Mistral Medium 3 are:
* 1,000 calls (avg 500 tokens): $1.2
* 10,000 calls: $12.0
* 100,000 calls: $120.0

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful language model released on 2025-04-17. With its mid-tier pricing and extensive capabilities, it's an attractive option for various applications. This guide will explore the top 5 best use cases for Mistral Medium 3, along with code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Medium 3
Based on its capabilities and pricing, the top 5 use cases for Mistral Medium 3 are:

1. **Coding and Analysis**: Mistral Medium 3 excels in coding tasks, making it ideal for code review, code completion, and analysis.
2. **Summarization and Content Generation**: With its strong text generation capabilities, Mistral Medium 3 is well-suited for summarization, content generation, and text-based tasks.
3. **Vision Tasks**: Mistral Medium 3's vision capabilities make it a great choice for image-based tasks, such as image classification, object detection, and image generation.
4. **RAG (Retrieve, Augment, Generate) Tasks**: Mistral Medium 3's ability to retrieve information, augment existing text, and generate new content makes it a strong candidate for RAG tasks.
5. **Function Calling and API Integration**: With its function_calling capability, Mistral Medium 3 can be used to integrate with external APIs, making it a great choice for tasks that require API calls.

### Code Integration Examples with OpenRouter
To integrate Mistral Medium 3 with OpenRouter, you can use the following code examples:
```python
import openrouter

# Initialize the Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Example 1: Coding Task
def code_completion(prompt):
    response = model.generate(prompt, max_tokens=512)
    return response

# Example 2: Summarization Task


## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
