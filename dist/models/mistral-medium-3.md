# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-23
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance of performance and cost. As a non-open source model, it is designed to provide a robust set of capabilities for developers, including text, vision, function calling, JSON mode, streaming, and system prompts. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, Mistral Medium 3 is well-suited for a variety of tasks, including coding, analysis, and content generation.

### Architecture and Strengths
The architecture of Mistral Medium 3 is not publicly disclosed, but its performance can be measured through various benchmarks. It achieves a score of 80.0 on the MMLU benchmark, 77.5 on HumanEval, and 1200 on the LMSYS Arena ELO. These scores indicate that Mistral Medium 3 is a capable model, particularly in tasks that require coding and analysis. Its primary strengths lie in its ability to handle complex tasks, such as function calling and vision tasks, making it a popular choice for developers who need a reliable and versatile model. The pricing for Mistral Medium 3 is set at $0.4 per 1M input tokens and $2.0 per 1M output tokens, making it a competitive option in the mid-tier market.

### Use Cases and Cost Examples
Mistral Medium 3 is best suited for tasks such as coding, analysis, summarization, and content generation. It is not recommended for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms. The cost of using Mistral Medium 3 can be estimated using the provided cost examples: 1,000 calls with an average of 500 tokens cost $1.2, while 10,000 calls cost $12.0,

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This analysis will delve into the cost structure, usage scenarios, and cost-effectiveness at scale for this model.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option when possible. This can significantly reduce costs for repeated or similar inputs. However, the effectiveness of cached tokens depends on the specific use case and the model's ability to leverage cached inputs efficiently.

#### Batch API Savings
Batching API calls can lead to significant savings, especially since batch input is free. By batching inputs, users can minimize the number of API calls, thereby reducing the overall cost. However, the actual savings will depend on the specific implementation and the average size of the input batches.

#### Cost at Scale
To understand the cost-effectiveness of Mistral Medium 3 at scale, let's examine the provided cost examples:
* **1,000 calls (avg 500 tokens)**: **$1.2**
* **10,000 calls**: **$12.0**
* **100,000 calls**: **$120.0**

These examples illustrate a linear cost increase with the number of API calls, indicating that the cost per call remains constant regardless of the scale.

#### Comparison with Top Competitors
Mistral Medium 3's pricing is competitive, especially considering its capabilities and performance benchmarks. For comparison:
* **Claude 3.5 Haiku**: $0

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Mistral Medium 3 Benchmark Performance
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
The benchmark performance of Mistral Medium 3 is as follows:
* **MMLU: 80.0**: The MMLU (Massive Multitask Language Understanding) benchmark measures a model's ability to perform a wide range of natural language processing tasks. A higher MMLU score indicates better performance. With a score of 80.0, Mistral Medium 3 demonstrates strong language understanding capabilities.
* **HumanEval: 77.5**: The HumanEval benchmark evaluates a model's ability to generate code that is correct and similar to human-written code. A higher HumanEval score indicates better code generation capabilities. With a score of 77.5, Mistral Medium 3 shows strong code generation abilities.
* **LMSYS Arena ELO: 1200**: The LMSYS Arena ELO benchmark measures a model's performance in a competitive environment, where models are p

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. Here's a detailed comparison with its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

#### Pricing Comparison
The pricing for each model is as follows:
* **Mistral Medium 3**:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* **Claude 3.5 Haiku**:
	+ Input: $0.8 per 1M tokens (100% more than Mistral Medium 3)
	+ Output: $4.0 per 1M tokens (100% more than Mistral Medium 3)
* **GPT-4o Mini**:
	+ Input: $0.15 per 1M tokens (62.5% less than Mistral Medium 3)
	+ Output: $0.6 per 1M tokens (70% less than Mistral Medium 3)

#### Performance Trade-offs
The performance of each model can be evaluated based on the provided benchmarks:
* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

However, based on the pricing, we can infer that:
* **Claude 3.5 Haiku** is likely to be a more powerful model, given its higher pricing.
* **GPT-4o Mini** is likely to be a more budget-friendly option, given its lower pricing.

#### When to Choose Each Model
Based on the pricing and performance, here are some guidelines on when to choose each model:
* **Mistral Medium 3**:
	+ Best for: coding, analysis, RAG, summarization, vision tasks, content generation, and function calling.
	+ Not good for: frontier reasoning, bulk cheap tasks, simple classification, and real-time sub-100ms tasks.
* **Claude 3.5 Ha

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful language model released on 2025-04-17. With its mid-tier pricing and extensive capabilities, it's an attractive option for various applications. This guide will explore the top 5 best use cases for Mistral Medium 3, along with code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Medium 3
#### 1. Coding and Analysis
Mistral Medium 3 excels in coding and analysis tasks, making it an excellent choice for:
* Code review and optimization
* Bug detection and debugging
* Code generation and completion

Example code integration with OpenRouter:
```python
import openrouter

# Initialize OpenRouter with Mistral Medium 3
model = openrouter.MistralMedium3()

# Define a coding task
code = "def add(a, b): return a + b"

# Use Mistral Medium 3 for code analysis
analysis = model.analyze_code(code)

# Print the analysis results
print(analysis)
```

#### 2. Summarization and Content Generation
Mistral Medium 3 is well-suited for summarization and content generation tasks, such as:
* Article summarization
* Content creation (e.g., blog posts, product descriptions)
* Text rewriting and editing

Example code integration with OpenRouter:
```python
import openrouter

# Initialize OpenRouter with Mistral Medium 3
model = openrouter.MistralMedium3()

# Define a summarization task
text = "This is a long article about a new technology..."

# Use Mistral Medium 3 for summarization
summary = model.summarize_text(text)

# Print the summary
print(summary)
```

#### 3. Vision Tasks
Mistral Medium 3 supports vision tasks, including:
* Image classification
* Object detection
* Image generation



## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
