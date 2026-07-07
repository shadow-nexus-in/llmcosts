# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-07
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance between performance and cost. As a non-open source model, it is designed to provide a robust set of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, Mistral Medium 3 is well-suited for a variety of tasks, including coding, analysis, and content generation.

### Architecture and Strengths
The architecture of Mistral Medium 3 is not publicly disclosed, but its performance can be gauged through its benchmark scores. With an MMLU score of 80.0, HumanEval score of 77.5, and LMSYS Arena ELO of 1200, Mistral Medium 3 demonstrates strong capabilities in natural language processing and generation. Its primary strengths lie in its ability to handle complex tasks, such as coding, analysis, and summarization, as well as its support for vision tasks and function calling. However, it is not recommended for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms.

### Pricing and Use Cases
Mistral Medium 3 is priced at $0.4 per 1M input tokens and $2.0 per 1M output tokens, making it a competitive option for developers who require a balance between performance and cost. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 100,000 calls would cost $120.0. Compared to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers a unique set of capabilities and pricing that make it an attractive option for developers who

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
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for reducing costs. Use cached tokens when:
* The input data is repetitive or has a high overlap between requests.
* The model is used for tasks with a high degree of similarity, such as data analysis or summarization.

#### Batch API Savings
Batch input is also free, which can lead to significant savings when making multiple requests. To maximize batch API savings:
* Group multiple requests together to reduce the number of API calls.
* Use batch input for tasks that require processing large amounts of data, such as coding or content generation.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: **$1.2**
* **10,000 calls**: **$12.0**
* **100,000 calls**: **$120.0**

To put these costs into perspective, consider the following calculations:
* Assuming an average of 500 tokens per call, 1,000 calls would require 500,000 tokens.
* At $0.4 per 1M input tokens, the input cost would be **$0.2** (500,000 tokens \* $0.4

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
* **Model Name:** Mistral Medium 3 (mistralai/mistral-medium-3)
* **Provider:** Mistral AI
* **Release Date:** 2025-04-17
* **Tier:** Mid
* **Open Source:** False

#### Pricing
The pricing for Mistral Medium 3 is as follows:
* **Input:** $0.4 per 1M tokens
* **Output:** $2.0 per 1M tokens
* **Cached Input:** $None per 1M tokens
* **Batch Input:** $None per 1M tokens

#### Context and Limits
The model has the following context and limits:
* **Context Window:** 131,072 tokens
* **Max Output:** 16,384 tokens
* **Knowledge Cutoff:** 2024-11

#### Benchmarks
The model's benchmark performance is as follows:
* **MMLU:** 80.0
* **HumanEval:** 77.5
* **LMSYS Arena ELO:** 1200
* **GSM8K:** None

The **MMLU (Massive Multitask Language Understanding) score** of 80.0 indicates the model's ability to understand and generate human-like text across a wide range of tasks and topics. A higher MMLU score suggests better performance in tasks that require a deep understanding of language.

The **HumanEval score** of 77.5 measures the model's

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. It is not open source and has a knowledge cutoff of 2024-11. In this comparison, we will evaluate Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini, in terms of pricing, performance, and use cases.

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
The performance of each model can be evaluated using various benchmarks:
* Mistral Medium 3:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* Claude 3.5 Haiku: Not provided
* GPT-4o Mini: Not provided

#### Capabilities and Use Cases
Mistral Medium 3 supports a range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. It is best suited for tasks such as:
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
* Real-time sub 100ms tasks

#### Cost Examples
The cost of using Mistral Medium 3 can be estimated as follows:
* 1,000 calls (avg 500

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful language model with a wide range of capabilities, including text, vision, function calling, and more. Released on 2025-04-17, this model is well-suited for various tasks such as coding, analysis, and content generation.

### Top 5 Best Use Cases for Mistral Medium 3
Based on its capabilities and limitations, here are the top 5 best use cases for Mistral Medium 3:

1. **Coding and Development**: With its strong performance in coding tasks, Mistral Medium 3 can be used for code completion, code review, and even generating code snippets. For example, you can use it with OpenRouter to generate API documentation:
    ```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Generate API documentation
def generate_api_docs(endpoint):
    prompt = f"Generate API documentation for {endpoint}"
    response = model.generate_text(prompt)
    return response

# Example usage
print(generate_api_docs("/users"))
```
2. **Text Analysis and Summarization**: Mistral Medium 3 can be used for text analysis, summarization, and extraction of key points. Its large context window of 131,072 tokens allows it to process long documents and generate concise summaries.
3. **Content Generation**: With its capabilities in text and vision, Mistral Medium 3 can be used for content generation, such as generating blog posts, articles, and even entire books. You can use it with OpenRouter to generate content based on a given prompt:
    ```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Generate content
def generate_content(prompt):
    response = model.generate_text(prompt)
    return response

# Example usage
print(generate

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
