# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-07
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, developed by Mistral AI and released on 2025-04-17, is a mid-tier model that offers a balance between performance and cost. As a non-open source model, it is designed to provide a robust set of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, Mistral Medium 3 is well-suited for a variety of tasks, including coding, analysis, and content generation.

### Architecture and Strengths
The architecture of Mistral Medium 3 is not explicitly stated, but its capabilities and benchmarks suggest a sophisticated design. With a high MMLU score of 80.0 and a HumanEval score of 77.5, Mistral Medium 3 demonstrates strong performance in natural language processing and coding tasks. Additionally, its LMSYS Arena ELO score of 1200 indicates a high level of competence in a competitive environment. The model's strengths are further reflected in its pricing, with input costs of $0.4 per 1M tokens and output costs of $2.0 per 1M tokens, making it a competitive option for developers who require a balance between performance and cost.

### Use Cases and Cost Considerations
Mistral Medium 3 is best suited for tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling. However, it is not recommended for frontier reasoning, bulk cheap tasks, simple classification, or real-time tasks that require sub-100ms response times. In terms of cost, Mistral Medium 3 offers a competitive pricing model, with estimated costs of $1.2 for 1,000 calls (avg 500 tokens), $12.0 for 10,000 calls, and $120.0 for 100,

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for repeated input sequences. If your application involves frequent reuse of input tokens, utilizing cached tokens can significantly reduce costs.

#### Batch API Savings
Batch input is also free, allowing for cost-effective processing of large input batches. By leveraging batch API calls, you can minimize the cost per token, making it an ideal choice for applications with high input volumes.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: **$1.2**
* **10,000 calls**: **$12.0**
* **100,000 calls**: **$120.0**

To put these costs into perspective, let's calculate the cost per token:
* Assuming an average of 500 tokens per call, the cost per token for 1,000 calls is: **$1.2 / (1,000 \* 500) = $0.0024 per token**
* For 10,000 calls, the cost per token is: **$12.0 / (10,000 \* 500) = $0.0024 per token**
* For 100,000 calls, the

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
The model's performance is measured by the following benchmark scores:
* **MMLU (80.0)**: The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to perform a wide range of natural language processing tasks. A higher MMLU score indicates better performance. With a score of 80.0, Mistral Medium 3 demonstrates strong language understanding capabilities.
* **HumanEval (77.5)**: The HumanEval benchmark assesses a model's ability to generate code that is correct and functional. A higher HumanEval score indicates better coding capabilities. With a score of 77.5, Mistral Medium 3 shows promising coding abilities.
* **LMSYS Arena ELO (1200)**: The LMSYS Arena ELO benchmark measures a model's performance in a competitive environment, evaluating its ability to respond to a wide range of questions and prompts. A higher ELO score indicates better performance. With a score of 1200, Mistral Medium 3 demonstrates moderate performance in this area.

#### Real-World Implications
The benchmark scores suggest that Mistral Medium 3 is suitable for tasks that require:
* Strong language understanding (e.g., text analysis, summarization

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

#### Performance Trade-offs
The performance of each model can be evaluated using the following benchmarks:
* Mistral Medium 3:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* Claude 3.5 Haiku: Not provided
* GPT-4o Mini: Not provided

While the exact performance of Claude 3.5 Haiku and GPT-4o Mini is not available, the pricing suggests that GPT-4o Mini may be a more budget-friendly option, while Claude 3.5 Haiku may offer higher performance at a premium price.

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
*

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful language model released on 2025-04-17. With its mid-tier pricing and extensive capabilities, it's an attractive choice for various applications. This guide will explore the top 5 best use cases for Mistral Medium 3, along with code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Medium 3
#### 1. **Coding and Analysis**
Mistral Medium 3 excels in coding tasks, such as code completion, debugging, and optimization. Its high MMLU score of 80.0 and HumanEval score of 77.5 demonstrate its proficiency in these areas.
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Example coding task: code completion
input_code = "def greet(name: str) -> None:"
output = model.generate(input_code, max_tokens=100)
print(output)
```
#### 2. **Summarization and Content Generation**
With its strong capabilities in text processing, Mistral Medium 3 is well-suited for summarization and content generation tasks. Its context window of 131,072 tokens allows for processing large documents.
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Example summarization task: summarize a long document
input_text = "..."  # long document text
output = model.summarize(input_text, max_tokens=200)
print(output)
```
#### 3. **Vision Tasks**
Mistral Medium 3 supports vision tasks, such as image classification and object detection. Its ability to process visual data makes it a versatile model for various applications.
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.Mistral

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
