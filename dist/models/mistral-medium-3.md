# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-28
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance of performance and cost. As a non-open source model, its architecture is not publicly disclosed, but its capabilities and benchmarks provide insight into its strengths. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, Mistral Medium 3 is suitable for a wide range of tasks, including coding, analysis, and content generation.

### Technical Specifications and Pricing
Mistral Medium 3 has a pricing structure that reflects its mid-tier positioning. The model costs $0.4 per 1M input tokens and $2.0 per 1M output tokens. Notably, there are no pricing options for cached input or batch input. The model's capabilities include text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers. Its benchmarks, such as an MMLU score of 80.0 and a HumanEval score of 77.5, demonstrate its performance in various tasks. For example, the cost of using Mistral Medium 3 can be estimated as follows: 1,000 calls with an average of 500 tokens would cost $1.2, while 10,000 calls would cost $12.0, and 100,000 calls would cost $120.0.

### Use Cases and Competitors
Mistral Medium 3 is best suited for tasks that require a balance of complexity and cost-effectiveness, such as coding, analysis, and content generation. However, it may not be the best choice for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms. In comparison to its competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3

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
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$None per 1M tokens** (free)
* Batch Input: **$None per 1M tokens** (free)

#### When to Use Cached Tokens
Given that cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs. This can be particularly beneficial for applications where the input data does not change frequently or can be pre-processed and stored.

#### Batch API Savings
Although the pricing does not explicitly mention a discount for batch API calls, the fact that batch input is listed as **$None per 1M tokens** suggests that there might be cost savings or efficiency gains from making batch requests. However, without explicit pricing or discounts mentioned for batch output, the primary cost savings in batch processing would come from the input side, which is already free.

#### Cost at Scale
To understand the cost-effectiveness of Mistral Medium 3 at different scales, let's examine the provided cost examples:
* **1,000 calls (avg 500 tokens): $1.2**
* **10,000 calls: $12.0**
* **100,000 calls: $120.0**

These examples suggest a linear scaling of costs with the number of API calls. To estimate costs for different scenarios, we can use the average cost per call. For instance, the cost per 1,000 calls averages to $1.2, which translates to $0.

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
* MMLU: **80.0** - This score indicates the model's ability to understand and process mathematical and logical concepts. A higher score suggests better performance in tasks that require mathematical reasoning.
* HumanEval: **77.5** - This score evaluates the model's ability to write and execute code. A higher score indicates better coding skills and problem-solving abilities.
* LMSYS Arena ELO: **1200** - This score represents the model's overall performance in a competitive arena, where it is pitted against other models. A higher score suggests better overall performance and adaptability.

#### Real-World Implications
The benchmark scores suggest that Mistral Medium 3 is a capable model for tasks that require:
* Mathematical and logical reasoning (MMLU: 80.0)
* Coding and problem-solving skills (HumanEval: 77

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will analyze its pricing, performance, and capabilities against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

#### Pricing Comparison
The pricing for each model is as follows:
* **Mistral Medium 3**:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* **Claude 3.5 Haiku**:
	+ Input: $0.8 per 1M tokens
	+ Output: $4.0 per 1M tokens
* **GPT-4o Mini**:
	+ Input: $0.15 per 1M tokens
	+ Output: $0.6 per 1M tokens

Mistral Medium 3 is priced lower than Claude 3.5 Haiku but higher than GPT-4o Mini for both input and output.

#### Performance Trade-offs
The performance of each model can be evaluated using the following benchmarks:
* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

While the benchmark scores for Claude 3.5 Haiku and GPT-4o Mini are not available, Mistral Medium 3 has a high MMLU score of 80.0 and a HumanEval score of 77.5, indicating strong performance in these areas.

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
* Real-time

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful language model released on 2025-04-17. With its mid-tier pricing and extensive capabilities, it's an attractive option for various applications. This guide will explore the top 5 best use cases for Mistral Medium 3, along with code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Medium 3
Based on its capabilities and limitations, the top 5 use cases for Mistral Medium 3 are:

1. **Coding and Analysis**: Mistral Medium 3 excels in coding tasks, making it suitable for code generation, review, and optimization. Its `function_calling` capability allows for seamless integration with external libraries and tools.
2. **Summarization and Content Generation**: With its high MMLU benchmark score (80.0), Mistral Medium 3 is well-suited for summarization and content generation tasks, such as generating articles, product descriptions, or social media posts.
3. **Vision Tasks**: Mistral Medium 3's `vision` capability enables it to process and understand visual data, making it suitable for tasks like image classification, object detection, and image generation.
4. **RAG (Retrieve, Augment, Generate) Tasks**: Mistral Medium 3's `rag` capability allows it to retrieve relevant information, augment it, and generate new content, making it suitable for tasks like question answering, text completion, and dialogue generation.
5. **JSON Mode and Streaming**: Mistral Medium 3's `json_mode` and `streaming` capabilities enable it to process and generate JSON data in real-time, making it suitable for tasks like data processing, API integration, and real-time analytics.

### Code Integration Examples with OpenRouter
To integrate Mistral Medium 3 with OpenRouter, you can use the following code examples:
```python
import openrouter



## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
