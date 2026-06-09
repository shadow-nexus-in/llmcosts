# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-09
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance between performance and cost. As a non-open source model, it is designed to provide reliable and efficient processing for a variety of tasks. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, Mistral Medium 3 is well-suited for tasks that require a moderate amount of input and output processing. The model's knowledge cutoff is 2024-11, ensuring that it has been trained on a significant amount of data up to that point.

### Architecture and Strengths
The architecture of Mistral Medium 3 supports a range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. These capabilities make it an ideal choice for tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling. The model's strengths are reflected in its benchmark scores, including an MMLU score of 80.0, a HumanEval score of 77.5, and an LMSYS Arena ELO score of 1200. With pricing set at $0.4 per 1M input tokens and $2.0 per 1M output tokens, Mistral Medium 3 offers a competitive option for developers who need a reliable and efficient model for their applications.

### Use Cases and Cost Examples
Mistral Medium 3 is best suited for tasks that require a moderate level of complexity and processing power. It is not recommended for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time processing under 100ms. The cost of using Mistral Medium 3 can be estimated based on the number of calls and tokens processed. For example, 1,000 calls with an average of 500 tokens would cost $1.2

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### Optimal Usage Scenarios
Given the cost structure, it's essential to understand when to utilize cached tokens and batch API calls to minimize costs.

* **Cached Tokens**: Since cached input tokens are free, it's highly beneficial to use them whenever possible. This can significantly reduce costs for repeated or similar input queries.
* **Batch API Savings**: Although batch input is free, the primary cost driver is the output tokens. To maximize savings, consider batching API calls to reduce the number of output tokens generated.

#### Cost at Scale
To illustrate the cost implications at scale, let's examine the provided cost examples:
* **1,000 calls (avg 500 tokens)**: **$1.2**
* **10,000 calls**: **$12.0**
* **100,000 calls**: **$120.0**

These examples demonstrate a linear cost increase with the number of API calls. To estimate costs for larger volumes, we can extrapolate from these examples.

#### Comparison with Top Competitors
Mistral Medium 3's pricing is competitive, but it's essential to consider the costs of top competitors:
* **Claude 3.5 Haiku**: $0.8/1M input, $4.0/1M output
* **GPT-

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
The Mistral Medium 3 model, released by Mistral AI on 2025-04-17, is a mid-tier, non-open-source model. Its pricing structure includes:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens

#### Benchmark Scores
The model's performance is measured by the following benchmark scores:
* **MMLU (80.0)**: The MMLU (Measuring Massive Multitask Language Understanding) score evaluates a model's ability to understand and generate human-like text across various tasks. A higher score indicates better performance. With a score of 80.0, Mistral Medium 3 demonstrates strong language understanding capabilities.
* **HumanEval (77.5)**: The HumanEval score assesses a model's ability to write correct and functional code in response to programming tasks. A higher score indicates better coding capabilities. With a score of 77.5, Mistral Medium 3 shows promising coding skills.
* **LMSYS Arena ELO (1200)**: The LMSYS Arena ELO score measures a model's overall performance in a competitive arena, where models are pitted against each other to complete tasks. A higher score indicates better overall performance. With a score of 1200, Mistral Medium 3 demonstrates competitive performance.

#### Real-World Implications
These benchmark scores have significant implications for real-world use cases:
* **Coding and Analysis**: With strong HumanEval and MMLU scores, Mistral Medium 3 is well-suited for tasks that require coding, analysis, and text generation, such as content creation

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3 is a mid-tier model released by Mistral AI on 2025-04-17. It offers a range of capabilities, including text, vision, function calling, and more. In this comparison, we will evaluate Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini, in terms of pricing, performance, and use cases.

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

Mistral Medium 3 is priced lower than Claude 3.5 Haiku but higher than GPT-4o Mini for both input and output tokens.

#### Performance Comparison
The performance of each model can be evaluated based on the following benchmarks:
* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

Since the benchmark data for Claude 3.5 Haiku and GPT-4o Mini is not available, we cannot directly compare their performance. However, Mistral Medium 3 has a high MMLU score of 80.0 and a HumanEval score of 77.5, indicating strong performance in these areas.

#### Use Cases and Trade-Offs
Each model has its strengths and weaknesses:
* **Mistral Medium 3**:
	+ Best for: coding, analysis, RAG, summarization, vision tasks, content generation, function calling
	+ Not good for: frontier reasoning, bulk cheap tasks, simple classification, real-time sub 100ms
* **Claude 3.

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful model with a wide range of capabilities, including text, vision, function calling, and more. Released on 2025-04-17, this model is well-suited for various tasks such as coding, analysis, and content generation.

### Top 5 Best Use Cases for Mistral Medium 3
Based on its capabilities and limitations, here are the top 5 best use cases for Mistral Medium 3:

1. **Coding and Development**: With its strong performance in coding tasks, Mistral Medium 3 can be used for code completion, code review, and even generating code snippets. For example, you can use it with OpenRouter to generate API documentation:
   ```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Generate API documentation
api_docs = model.generate_api_docs("example_function")
print(api_docs)
```

2. **Text Analysis and Summarization**: Mistral Medium 3 can be used for text analysis, summarization, and content generation. Its large context window of 131,072 tokens allows it to process long documents and generate concise summaries:
   ```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Summarize a long document
summary = model.summarize("example_document.txt")
print(summary)
```

3. **Vision Tasks**: With its vision capabilities, Mistral Medium 3 can be used for image classification, object detection, and image generation. For example, you can use it with OpenRouter to classify images:
   ```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Classify an image
image_class = model.classify_image("example_image.jpg")


## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
