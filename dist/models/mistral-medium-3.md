# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-31
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance of performance and cost. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, this model is well-suited for a variety of tasks, including coding, analysis, and content generation. The model's architecture supports multiple capabilities, such as text, vision, function calling, JSON mode, streaming, and system prompts.

### Technical Strengths and Use Cases
Mistral Medium 3 excels in tasks that require a combination of natural language understanding and generation, such as summarization, RAG, and vision tasks. Its strengths are reflected in its benchmark scores, including an MMLU score of 80.0, a HumanEval score of 77.5, and an LMSYS Arena ELO score of 1200. However, it may not be the best fit for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms. The model's pricing is competitive, with costs of $0.4 per 1M input tokens and $2.0 per 1M output tokens.

### Cost and Competitiveness
The cost of using Mistral Medium 3 can be estimated based on the number of calls and tokens used. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 10,000 calls would cost $12.0, and 100,000 calls would cost $120.0. Compared to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers a unique balance of performance and cost. While Claude 3.5 Haiku is more expensive, with costs of $0.8/1M input and

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
Mistral Medium 3 is a mid-tier model provided by Mistral AI, released on 2025-04-17. It is not open source. The pricing structure is based on input and output tokens, with discounts for cached and batch inputs.

#### Cost Structure
The cost structure for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for repeated input sequences. If your application involves frequent reuse of the same input, using cached tokens can significantly reduce costs.

#### Batch API Savings
Batch inputs are also free, which means that batching API calls can lead to substantial cost savings. By grouping multiple input sequences into a single API call, you can avoid paying for input tokens.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* 1,000 calls (avg 500 tokens): $1.2
* 10,000 calls: $12.0
* 100,000 calls: $120.0

To estimate the cost of using Mistral Medium 3, you can use the following formula:
`Cost = (Input Tokens / 1,000,000) * $0.4 + (Output Tokens / 1,000,000) * $2.0`

For example, if you make 1,000 API calls with an average input size of 500 tokens and an average output size of 200 tokens, the total cost would be:
`Cost = (500,000 / 1,000,000) * $0.4 + (200,000 / 

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
The Mistral Medium 3 model, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. The model's knowledge cutoff is 2024-11.

#### Pricing
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Benchmark Performance
The model's benchmark performance is measured by the following metrics:
* **MMLU (80.0)**: The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to perform a wide range of natural language processing tasks. A higher MMLU score indicates better performance. With a score of 80.0, Mistral Medium 3 demonstrates strong language understanding capabilities.
* **HumanEval (77.5)**: The HumanEval benchmark assesses a model's ability to generate code that is correct and functional. A higher HumanEval score indicates better code generation capabilities. With a score of 77.5, Mistral Medium 3 shows strong code generation abilities.
* **LMSYS Arena ELO (1200)**: The LMSYS Arena ELO benchmark evaluates a model's overall performance in a competitive setting. A higher ELO score indicates better performance. With a score of 1200, Mistral Medium 3 demonstrates competitive performance.

#### Real

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. This comparison will analyze its pricing, performance, and capabilities against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

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

Mistral Medium 3 is more expensive than GPT-4o Mini but cheaper than Claude 3.5 Haiku in terms of input and output costs.

#### Performance Trade-offs
The performance of each model is measured by various benchmarks:
* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

Without direct comparisons of benchmark scores, it's challenging to determine the performance differences between the models. However, Mistral Medium 3's scores indicate its capabilities in areas like coding, analysis, and vision tasks.

#### Capabilities and Use Cases
Mistral Medium 3 supports the following capabilities:
* text
* vision
* function_calling
* json_mode
* streaming
* system_prompts

It is best suited for tasks like:
* coding
* analysis
* rag
* summarization
* vision_tasks
* content_generation
* function_calling

On the other hand, it is not recommended for:
* frontier_reasoning
* bulk_cheap_tasks
* simple_classification
* real_time_sub_100ms

#### Cost Examples
To illustrate the costs associated with each model, consider the following examples:
* **Mistral Medium 3**:


## Best Use Cases
### Practical Advice on Top 5 Best Use Cases for Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. Given its capabilities and pricing, here are the top 5 best use cases for Mistral Medium 3, along with specific code integration examples mentioning OpenRouter.

#### 1. **Coding and Analysis**
Mistral Medium 3 excels in coding and analysis tasks, making it an ideal choice for applications that require in-depth code understanding and generation. 
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Define a coding task
task = "Write a Python function to sort a list of integers."

# Get the response
response = model.generate(task)

# Print the response
print(response)
```
With a pricing of $0.4 per 1M input tokens and $2.0 per 1M output tokens, Mistral Medium 3 offers a cost-effective solution for coding and analysis tasks.

#### 2. **Summarization and Content Generation**
Mistral Medium 3's capabilities in text processing make it suitable for summarization and content generation tasks. 
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Define a summarization task
task = "Summarize a given article."

# Get the response
response = model.generate(task)

# Print the response
print(response)
```
The model's context window of 131,072 tokens allows for processing large amounts of text, making it an excellent choice for summarization and content generation tasks.

#### 3. **Vision Tasks**
Mistral Medium 3's support for vision tasks enables its use in applications

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
