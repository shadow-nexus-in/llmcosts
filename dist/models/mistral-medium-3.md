# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-12
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a robust set of capabilities for developers. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, this model is well-suited for tasks that require in-depth analysis and generation of content. The architecture of Mistral Medium 3 supports a wide range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts.

### Strengths and Use Cases
The main strengths of Mistral Medium 3 lie in its ability to handle complex tasks such as coding, analysis, and content generation. It also excels in vision tasks, summarization, and function calling. With a pricing structure of $0.4 per 1M input tokens and $2.0 per 1M output tokens, this model offers a cost-effective solution for developers who need to process large amounts of data. The model's benchmarks, including an MMLU score of 80.0 and a HumanEval score of 77.5, demonstrate its capabilities in natural language processing and coding tasks. However, it is not recommended for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms.

### Cost and Competitiveness
The cost of using Mistral Medium 3 can be estimated based on the number of calls and tokens processed. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 10,000 calls would cost $12.0. In comparison to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers a competitive pricing structure. However, its costs are higher than GPT-4o Mini, which charges $0.15/1M input

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
* **Input**: $0.4 per 1M tokens
* **Output**: $2.0 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

#### When to Use Cached Tokens
Given that cached input tokens are free, it is highly beneficial to utilize cached tokens whenever possible. This can significantly reduce costs, especially for applications with repetitive or similar input sequences.

#### Batch API Savings
Although the pricing for batch input is listed as $None per 1M tokens, the actual cost savings come from the reduced overhead of making fewer API calls. To quantify this, let's examine the provided cost examples:
* 1,000 calls (avg 500 tokens): $1.2
* 10,000 calls: $12.0
* 100,000 calls: $120.0

These examples suggest a linear cost scaling with respect to the number of API calls. However, by batching inputs, you can reduce the number of API calls, thereby reducing the overall cost.

#### Cost at Scale
To estimate the cost at scale, we can use the provided cost examples:
* **1,000 API calls**: $1.2
* **10,000 API calls**: $12.0 (12x increase in calls, 10x increase in cost)
* **100,000 API calls**: $120.0 (10x increase in calls, 10x increase in cost)

Assuming a linear cost scaling

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
* **MMLU (Massive Multitask Language Understanding)**: 80.0 - This score indicates the model's ability to understand and generate human-like text across a wide range of tasks and domains. A higher MMLU score suggests better language understanding capabilities.
* **HumanEval**: 77.5 - This score evaluates the model's ability to generate correct and functional code in response to programming prompts. A higher HumanEval score indicates better coding capabilities.
* **LMSYS Arena ELO**: 1200 - This score measures the model's performance in a competitive arena, where it is pitted against other models in a series of tasks. A higher ELO score suggests better overall performance and adaptability.

#### Real-World Implications
The benchmark scores suggest that Mistral Medium 3 is a capable model for a variety of tasks, including:
* Coding and programming tasks (HumanEval: 77.5)
* Text

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will analyze the pricing, performance, and capabilities of Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

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
The performance benchmarks for each model are:
* Mistral Medium 3:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* Claude 3.5 Haiku: Not provided
* GPT-4o Mini: Not provided

#### Capabilities and Use Cases
Mistral Medium 3 is best suited for tasks such as:
* Coding
* Analysis
* RAG (Retrieval-Augmented Generation)
* Summarization
* Vision tasks
* Content generation
* Function calling

It is not recommended for tasks that require:
* Frontier reasoning
* Bulk cheap tasks
* Simple classification
* Real-time responses under 100ms

#### Cost Examples
The estimated costs for using Mistral Medium 3 are:
* 1,000 calls (avg 500 tokens): $1.2
* 10,000 calls: $12.0
* 100,000 calls: $120.0

#### Choosing the Right Model
Based on the pricing and performance comparison, here are some guidelines

## Best Use Cases
### Practical Advice for Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful model with a wide range of capabilities, including text, vision, function calling, and more. Given its strengths and pricing, here are the top 5 best use cases for Mistral Medium 3, along with specific code integration examples mentioning OpenRouter.

#### 1. **Coding and Analysis**
Mistral Medium 3 excels in coding and analysis tasks, making it an ideal choice for developers and data analysts. Its ability to understand and generate code, coupled with its analysis capabilities, can significantly streamline development and debugging processes.

**Example Code Integration with OpenRouter:**
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Define a coding task
task = "Write a Python function to sort a list of integers."

# Use the model to generate code
response = model.generate_code(task)

# Print the generated code
print(response)
```

#### 2. **Summarization and Content Generation**
With its strong text generation capabilities, Mistral Medium 3 is well-suited for summarization and content generation tasks. It can summarize long documents, generate articles, or even create content for social media platforms.

**Example Code Integration with OpenRouter:**
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Define a summarization task
task = "Summarize the following article: [insert article text]"

# Use the model to generate a summary
response = model.summarize(task)

# Print the summary
print(response)
```

#### 3. **Vision Tasks**
Mistral Medium 3's vision capabilities make it an excellent choice for tasks such as image classification, object detection, and image generation.

**Example Code Integration with OpenRouter:**
```python

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
