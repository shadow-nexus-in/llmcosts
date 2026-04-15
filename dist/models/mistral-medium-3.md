# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-15
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance between performance and cost. As a non-open source model, it provides a unique set of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, Mistral Medium 3 is well-suited for a variety of tasks, including coding, analysis, and content generation.

### Architecture and Strengths
The architecture of Mistral Medium 3 is designed to handle complex tasks with ease. Its main strengths lie in its ability to process large amounts of data, with a knowledge cutoff of 2024-11, and its high performance on benchmarks such as MMLU (80.0) and HumanEval (77.5). Additionally, its LMSYS Arena ELO score of 1200 demonstrates its capability in competitive environments. With pricing set at $0.4 per 1M input tokens and $2.0 per 1M output tokens, Mistral Medium 3 offers a competitive solution for developers looking for a reliable and efficient model.

### Use Cases and Cost Examples
Mistral Medium 3 is best suited for tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling. However, it is not recommended for frontier reasoning, bulk cheap tasks, simple classification, or real-time tasks requiring sub-100ms response times. In terms of cost, developers can expect to pay $1.2 for 1,000 calls (avg 500 tokens), $12.0 for 10,000 calls, and $120.0 for 100,000 calls. Compared to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini,

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
Given that cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs. This is particularly beneficial for applications with repetitive or similar input patterns.

#### Batch API Savings
Although batch input is free, the actual cost savings depend on the output token count. Since output tokens are charged at **$2.0 per 1M tokens**, optimizing batch size to reduce output tokens can lead to significant cost savings.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: **$1.2**
* **10,000 calls**: **$12.0**
* **100,000 calls**: **$120.0**

To put these costs into perspective, let's calculate the cost per call:
* **1,000 calls**: **$1.2 / 1,000 = $0.0012 per call**
* **10,000 calls**: **$12.0 / 10,000 = $0.0012 per call**
* **100,000 calls**: **$120.0 / 100,000 = $0.0012 per call**

The cost per call remains constant at

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
The model's benchmark performance is as follows:
* **MMLU (Massive Multitask Language Understanding)**: 80.0 - This score indicates the model's ability to understand and generate human-like text across a wide range of tasks and topics. A higher MMLU score suggests better language understanding capabilities.
* **HumanEval**: 77.5 - This score evaluates the model's ability to generate correct and functional code in response to programming tasks. A higher HumanEval score indicates better coding capabilities.
* **LMSYS Arena ELO**: 1200 - This score measures the model's performance in a competitive arena, where it is pitted against other models in a variety of tasks. A higher ELO score suggests better overall performance and adaptability.

#### Real-World Implications
The benchmark scores suggest that Mistral Medium 3 is a capable model for a variety of tasks, including:
* Coding and programming tasks (HumanEval: 77.5)
* Text analysis and generation (MMLU: 80.0)
* Vision tasks and content generation (supported capabilities)
However, the model may not be suitable for tasks that require:
* Frontier reasoning and complex problem-solving (NOT GOOD FOR: frontier_reasoning)


## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will examine the pricing, performance, and capabilities of Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

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

#### Performance Comparison
The performance benchmarks for each model are:
* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

Mistral Medium 3 has a higher MMLU score than its competitors, but the lack of benchmark data for Claude 3.5 Haiku and GPT-4o Mini makes a direct comparison challenging.

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
The estimated costs for

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful language model with a wide range of capabilities, including text, vision, function calling, and more. Released on 2025-04-17, this model is well-suited for tasks such as coding, analysis, and content generation. In this guide, we will explore the top 5 best use cases for Mistral Medium 3, along with specific code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Medium 3
#### 1. **Coding and Development**
Mistral Medium 3 excels in coding tasks, making it an ideal choice for developers. With its high MMLU score of 80.0 and HumanEval score of 77.5, this model can provide accurate and efficient coding assistance.

```python
import openrouter

# Initialize the OpenRouter client
client = openrouter.Client(model="mistralai/mistral-medium-3")

# Define a coding task
task = "Write a Python function to sort a list of integers."

# Send the task to the model
response = client.generate(task)

# Print the response
print(response)
```

#### 2. **Text Analysis and Summarization**
Mistral Medium 3 is capable of analyzing and summarizing large amounts of text data. Its high context window of 131,072 tokens allows it to process lengthy documents and provide insightful summaries.

```python
import openrouter

# Initialize the OpenRouter client
client = openrouter.Client(model="mistralai/mistral-medium-3")

# Define a text analysis task
task = "Summarize the following article: [insert article text]"

# Send the task to the model
response = client.generate(task)

# Print the response
print(response)
```

#### 3. **Content Generation**
With its strong capabilities in text generation, Mist

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
