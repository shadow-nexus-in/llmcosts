# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-20
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance of performance and cost. As a non-open-source model, it is designed to provide reliable and efficient processing for a wide range of tasks. With its architecture, Mistral Medium 3 supports multiple capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. This versatility makes it suitable for various applications, such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling.

### Technical Specifications and Pricing
Mistral Medium 3 has a context window of 131,072 tokens and a maximum output of 16,384 tokens, with a knowledge cutoff date of 2024-11. The model's pricing is based on input and output tokens, with costs of $0.4 per 1M input tokens and $2.0 per 1M output tokens. There are no additional costs for cached input or batch input. The model's performance is benchmarked at 80.0 on MMLU, 77.5 on HumanEval, and 1200 on LMSYS Arena ELO. For example, using Mistral Medium 3 for 1,000 calls with an average of 500 tokens would cost $1.2, while 10,000 calls would cost $12.0, and 100,000 calls would cost $120.0.

### Comparison and Use Cases
Mistral Medium 3 is best suited for tasks that require a balance of performance and cost, such as coding, analysis, and content generation. However, it may not be the best choice for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms. In comparison to its competitors, such as Claude 3.5 Haiku and GPT

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
Mistral Medium 3, a mid-tier model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2025-04-17, this model is not open source. The pricing structure is based on input and output tokens, with specific considerations for cached and batch inputs.

#### Cost Structure
The cost structure for Mistral Medium 3 is as follows:
- **Input**: $0.4 per 1M tokens
- **Output**: $2.0 per 1M tokens
- **Cached Input**: $0 per 1M tokens (free)
- **Batch Input**: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option when the same input is used multiple times. This can significantly reduce costs in applications where input repetition is common.

#### Batch API Savings
Similar to cached inputs, batch inputs are also free. Utilizing batch API calls can lead to substantial savings, especially in scenarios where a large number of similar requests are made. This makes Mistral Medium 3 particularly cost-effective for batch processing tasks.

#### Cost at Scale
To understand the cost implications of using Mistral Medium 3 at different scales, let's examine the provided cost examples:
- **1,000 calls (avg 500 tokens)**: $1.2
- **10,000 calls**: $12.0
- **100,000 calls**: $120.0

These examples illustrate a linear scaling of costs with the number of API calls, indicating that the cost per call remains constant regardless of the volume.

#### Comparison with Competitors
Mistral Medium 3's pricing can be compared to its top competitors:
- **Claude 3.5 Haiku**: $0.8/1M input, $4.0/1M output

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Medium 3 Benchmark Performance Analysis
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. The model's pricing is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens

#### Benchmark Scores
The model's benchmark performance is measured by the following scores:
* **MMLU (Massive Multitask Language Understanding)**: 80.0
	+ MMLU measures a model's ability to understand and generate text across a wide range of tasks and domains. A higher MMLU score indicates better language understanding capabilities.
* **HumanEval**: 77.5
	+ HumanEval evaluates a model's ability to write correct and functional code in response to programming tasks. A higher HumanEval score indicates better coding capabilities.
* **LMSYS Arena ELO**: 1200
	+ LMSYS Arena ELO measures a model's performance in a competitive environment, where models are pitted against each other to complete tasks. A higher ELO score indicates better overall performance.

#### Real-World Implications
The benchmark scores suggest that Mistral Medium 3 is a capable model for tasks such as:
* Coding and programming (HumanEval: 77.5)
* Text analysis and understanding (MMLU: 80.0)
* General-purpose language tasks (LMSYS Arena ELO: 1200)

However, the model may not be suitable for tasks that require:
* Frontier reasoning or complex problem

## Competitor Comparison
### Mistral Medium 3 Comparison
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This model is not open source and has a knowledge cutoff of 2024-11.

#### Pricing Comparison
The pricing for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens

In comparison to its top competitors:
* **Claude 3.5 Haiku**:
	+ Input: $0.8 per 1M tokens (100% more expensive than Mistral Medium 3)
	+ Output: $4.0 per 1M tokens (100% more expensive than Mistral Medium 3)
* **GPT-4o Mini**:
	+ Input: $0.15 per 1M tokens (62.5% less expensive than Mistral Medium 3)
	+ Output: $0.6 per 1M tokens (70% less expensive than Mistral Medium 3)

#### Performance Trade-offs
Mistral Medium 3 has the following benchmark scores:
* MMLU: 80.0
* HumanEval: 77.5
* LMSYS Arena ELO: 1200

While the exact benchmark scores for Claude 3.5 Haiku and GPT-4o Mini are not provided, the pricing differences suggest that Mistral Medium 3 may offer a balance between cost and performance.

#### Capabilities and Use Cases
Mistral Medium 3 is capable of:
* Text processing
* Vision tasks
* Function calling
* JSON mode
* Streaming
* System prompts

It is best suited for tasks such as:
* Coding
* Analysis
* RAG ( Retrieval-Augmented Generation)
* Summarization
* Vision tasks
* Content generation
* Function calling

However, it is not recommended for:
* Frontier reasoning
* Bulk cheap tasks
* Simple classification
* Real-time tasks with sub-100ms latency

#### Cost Examples
The estimated costs for using Mistral Medium 3 are:
* 1,000 calls (avg 500 tokens): $1.2
* 10,000 calls: $12.0
*

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. This model is best suited for tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling.

### Top 5 Best Use Cases for Mistral Medium 3
Based on its capabilities and pricing, here are the top 5 best use cases for Mistral Medium 3:

1. **Coding and Development**: With its strong performance in coding tasks, Mistral Medium 3 can be used for code completion, code review, and code generation. For example, you can use it to generate boilerplate code or to complete partially written functions.
2. **Text Analysis and Summarization**: Mistral Medium 3 can be used for text analysis, summarization, and RAG (Retrieval-Augmented Generation) tasks. Its large context window of 131,072 tokens makes it suitable for analyzing long documents.
3. **Content Generation**: With its ability to generate high-quality text, Mistral Medium 3 can be used for content generation tasks such as writing articles, creating product descriptions, and generating social media posts.
4. **Vision Tasks**: Mistral Medium 3 supports vision capabilities, making it suitable for tasks such as image classification, object detection, and image generation.
5. **Function Calling and API Integration**: Mistral Medium 3's function calling capability allows it to integrate with external APIs and services, making it suitable for tasks such as data retrieval, API testing, and automation.

### Code Integration Example with OpenRouter
Here's an example of how you can integrate Mistral Medium 3 with OpenRouter to generate code:
```python
import openrouter

# Initialize the Mistral Medium 3 model
model

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
