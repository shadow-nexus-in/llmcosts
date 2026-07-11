# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-11
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance between performance and cost. As a non-open source model, it is designed to provide reliable and efficient processing for a variety of tasks. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, Mistral Medium 3 is well-suited for applications that require in-depth analysis and generation of text.

### Architecture and Strengths
The architecture of Mistral Medium 3 supports multiple capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. Its strengths are reflected in its benchmark scores, with an MMLU score of 80.0, HumanEval score of 77.5, and LMSYS Arena ELO score of 1200. These capabilities and strengths make Mistral Medium 3 a versatile model that can be used for coding, analysis, RAG, summarization, vision tasks, content generation, and function calling. The model's pricing is competitive, with input costs of $0.4 per 1M tokens and output costs of $2.0 per 1M tokens.

### Use Cases and Cost Considerations
Mistral Medium 3 is best suited for tasks that require in-depth analysis, generation, and processing of text and vision data. However, it may not be the best choice for frontier reasoning, bulk cheap tasks, simple classification, or real-time tasks that require sub-100ms response times. The cost of using Mistral Medium 3 can be estimated based on the number of calls and tokens processed. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 10,000 calls would cost $12.0, and 100,000 calls would cost $120.0. Compared to its top

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
Mistral Medium 3 is a mid-tier model offered by Mistral AI, released on 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following scenarios:
* **Cached Tokens**: Use cached input tokens whenever possible, as they are **free**. This is ideal for applications with repetitive or similar input prompts.
* **Batch API Calls**: Take advantage of batch input, which is also **free**. This is suitable for applications that can process multiple inputs simultaneously.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* **1,000 API calls** (avg 500 tokens): **$1.2**
* **10,000 API calls**: **$12.0**
* **100,000 API calls**: **$120.0**

These costs can be broken down into input and output costs. Assuming an average of 500 tokens per call, the total tokens for each scenario would be:
* 1,000 calls: 500,000 tokens
* 10,000 calls: 5,000,000 tokens
* 100,000 calls: 50,000,000 tokens

Using the pricing structure, we can calculate the total cost:
* 1,000 calls: (500,000 tokens / 1,000,000) \* ($0.4 + $2.0) = $

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
The Mistral Medium 3 model, released by Mistral AI on 2025-04-17, is a mid-tier, non-open-source model. It offers a range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts.

#### Pricing
The pricing for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Context and Limits
The model has the following context and limits:
* Context Window: 131,072 tokens
* Max Output: 16,384 tokens
* Knowledge Cutoff: 2024-11

#### Benchmarks
The model's benchmark performance is as follows:
* MMLU: 80.0
* HumanEval: 77.5
* LMSYS Arena ELO: 1200
* GSM8K: None

#### Capabilities and Use Cases
Mistral Medium 3 is best suited for tasks such as:
* Coding
* Analysis
* RAG (Retrieve, Augment, Generate)
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

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance between price and performance. In this comparison, we will evaluate Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini, in terms of pricing, performance, and use cases.

#### Pricing Comparison
The pricing models of the three competitors are as follows:

* **Mistral Medium 3**:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* **Claude 3.5 Haiku**:
	+ Input: $0.8 per 1M tokens
	+ Output: $4.0 per 1M tokens
* **GPT-4o Mini**:
	+ Input: $0.15 per 1M tokens
	+ Output: $0.6 per 1M tokens

Mistral Medium 3 offers a competitive pricing model, with input costs 50% lower than Claude 3.5 Haiku and output costs 66.7% lower. However, GPT-4o Mini has significantly lower input and output costs, making it a more affordable option for large-scale applications.

#### Performance Comparison
The performance of the three models can be evaluated based on their benchmark scores:

* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not available
* **GPT-4o Mini**: Not available

While the benchmark scores for Claude 3.5 Haiku and GPT-4o Mini are not available, Mistral Medium 3 has demonstrated strong performance in various tasks, including coding, analysis, and vision tasks.

#### Context and Limits
The context window and output limits of the three models are as follows:

* **Mistral Medium 3**:
	+ Context Window: 131,072 tokens
	+ Max Output: 16,384 tokens
* **Claude 3.5 Haiku**: Not available
* **GPT-4o Mini**: Not available

Mistral

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful language model released on 2025-04-17. With its mid-tier pricing and extensive capabilities, it's an attractive choice for various applications. This guide will explore the top 5 best use cases for Mistral Medium 3, along with code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Medium 3
Based on its capabilities and limitations, the top 5 use cases for Mistral Medium 3 are:
1. **Coding and Analysis**: With its high MMLU score of 80.0 and HumanEval score of 77.5, Mistral Medium 3 is well-suited for coding tasks, such as code completion, code review, and analysis.
2. **Summarization and Content Generation**: Its capabilities in text and vision tasks make it an excellent choice for summarizing long documents, generating content, and creating engaging articles.
3. **RAG (Retrieve, Augment, Generate) Tasks**: Mistral Medium 3's ability to handle text and vision tasks, along with its function calling capability, makes it suitable for RAG tasks, such as retrieving information, augmenting existing content, and generating new text.
4. **Vision Tasks**: With its support for vision tasks, Mistral Medium 3 can be used for image analysis, object detection, and image generation.
5. **Function Calling and JSON Mode**: Its ability to handle function calls and JSON mode makes it an excellent choice for integrating with external APIs, processing JSON data, and performing complex tasks.

### Code Integration Examples with OpenRouter
To integrate Mistral Medium 3 with OpenRouter, you can use the following code examples:
```python
import openrouter

# Initialize the Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Example 1: Coding and Analysis
def code_completion

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
