# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-03
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance between performance and cost. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, this model is well-suited for a variety of tasks, including coding, analysis, and content generation. The model's capabilities include text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Architecture and Strengths
The architecture of Mistral Medium 3 is designed to support a wide range of applications, with a focus on performance and efficiency. The model's strengths lie in its ability to handle complex tasks, such as coding and analysis, with a high degree of accuracy. With a MMLU benchmark score of 80.0 and a HumanEval score of 77.5, Mistral Medium 3 demonstrates strong performance in these areas. Additionally, the model's LMSYS Arena ELO score of 1200 indicates its ability to compete with other models in the mid-tier range. The pricing for Mistral Medium 3 is $0.4 per 1M input tokens and $2.0 per 1M output tokens, making it a competitive option for developers.

### Use Cases and Cost Examples
Mistral Medium 3 is best suited for tasks such as coding, analysis, and content generation, where its strengths in performance and efficiency can be fully utilized. The model is not recommended for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms. In terms of cost, Mistral Medium 3 offers a competitive pricing structure, with examples including $1.2 for 1,000 calls (avg 500 tokens), $12.0 for 10,000 calls, and $120.0 for 100,

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.4 |
| Output | $2.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Mistral Medium 3 Pricing Analysis
#### Overview
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. This analysis will delve into the cost structure, usage scenarios, and scalability of this model.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### Usage Scenarios
* **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
* **Batch API Savings**: Although batch input tokens are free, the output tokens are still charged at **$2.0 per 1M tokens**. Therefore, batching can help reduce the input cost to zero but will not affect the output cost.

#### Cost at Scale
The cost of using Mistral Medium 3 at different scales is as follows:
* **1,000 calls (avg 500 tokens)**: **$1.2**
* **10,000 calls**: **$12.0**
* **100,000 calls**: **$120.0**

To estimate the cost at scale, we can use the following calculation:
* Assume an average of 500 tokens per call (input + output).
* For 1,000 calls, the total tokens would be approximately 500,000 tokens.
* Using the pricing structure, the cost would be:
	+ Input: 500,000 tokens / 1,000,000 tokens per unit * $0.4 = $0.2
	+ Output: 500,000 tokens / 1,000,000 tokens per unit * $2.0 = $1.

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Medium 3 Benchmark Analysis
#### Model Overview
The Mistral Medium 3 model, released by Mistral AI on 2025-04-17, is a mid-tier model with the following key characteristics:
* **Pricing**:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* **Context and Limits**:
	+ Context Window: 131,072 tokens
	+ Max Output: 16,384 tokens
	+ Knowledge Cutoff: 2024-11
* **Capabilities**: text, vision, function_calling, json_mode, streaming, system_prompts
* **Best For**: coding, analysis, rag, summarization, vision_tasks, content_generation, function_calling

#### Benchmark Performance
The model's performance is measured by the following benchmarks:
* **MMLU (Massive Multitask Language Understanding)**: 80.0
* **HumanEval**: 77.5
* **LMSYS Arena ELO**: 1200

These benchmarks indicate the model's ability to understand and generate human-like text. The MMLU score measures the model's performance on a wide range of natural language processing tasks, while the HumanEval score evaluates the model's ability to write correct and functional code. The LMSYS Arena ELO score is a measure of the model's overall language understanding and generation capabilities.

#### Real-World Implications
The benchmark scores suggest that the Mistral Medium 3 model is suitable for tasks that require:
* **Coding and analysis**: The model's high HumanEval score indicates that it can generate correct and functional code, making it a

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will examine the pricing, performance, and use cases of Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

#### Pricing Comparison
The pricing models for each competitor are as follows:
* **Mistral Medium 3**:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* **Claude 3.5 Haiku**:
	+ Input: $0.8 per 1M tokens
	+ Output: $4.0 per 1M tokens
* **GPT-4o Mini**:
	+ Input: $0.15 per 1M tokens
	+ Output: $0.6 per 1M tokens

Mistral Medium 3 offers a balance between input and output costs, while Claude 3.5 Haiku is more expensive for both input and output. GPT-4o Mini is the most cost-effective option for both input and output.

#### Performance Comparison
The performance benchmarks for each model are:
* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

Mistral Medium 3 has a higher MMLU score compared to its HumanEval score, indicating stronger performance in certain tasks. However, without benchmark data for Claude 3.5 Haiku and GPT-4o Mini, a direct performance comparison is not possible.

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

However, it

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful language model released on 2025-04-17. With its mid-tier pricing and extensive capabilities, it's an attractive choice for various applications. This guide will explore the top 5 best use cases for Mistral Medium 3, along with code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Medium 3
Based on its capabilities and pricing, the top 5 use cases for Mistral Medium 3 are:

1. **Coding and Analysis**: With its high scores in HumanEval (77.5) and MMLU (80.0), Mistral Medium 3 is well-suited for coding tasks, such as code completion, debugging, and analysis.
2. **Summarization and Content Generation**: Its capabilities in text and vision tasks make it an excellent choice for summarizing long documents, generating content, and creating engaging stories.
3. **RAG (Retrieval-Augmented Generation) Tasks**: Mistral Medium 3's ability to handle function calling and JSON mode makes it suitable for RAG tasks, such as retrieving information from external sources and generating text based on that information.
4. **Vision Tasks**: With its support for vision tasks, Mistral Medium 3 can be used for image classification, object detection, and image generation.
5. **System Prompts and Streaming**: Its ability to handle system prompts and streaming makes it suitable for applications that require real-time processing and generation of text or images.

### Code Integration Examples with OpenRouter
To integrate Mistral Medium 3 with OpenRouter, you can use the following code examples:

```python
import openrouter

# Initialize the Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Example 1: Coding and Analysis
def code_completion(prompt):
    response = model.generate(prompt, max_tokens=100

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
