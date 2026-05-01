# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-01
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance between performance and cost. As a non-open source model, it provides a unique set of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, Mistral Medium 3 is well-suited for a variety of tasks, including coding, analysis, and content generation.

### Architecture and Strengths
The architecture of Mistral Medium 3 is designed to handle complex tasks with its large context window and output capabilities. Its main strengths lie in its ability to perform tasks that require a deep understanding of context, such as summarization, RAG, and vision tasks. The model's benchmarks, including an MMLU score of 80.0 and a HumanEval score of 77.5, demonstrate its capabilities in these areas. Additionally, its LMSYS Arena ELO score of 1200 indicates its competitive performance in a variety of tasks. With a knowledge cutoff of 2024-11, Mistral Medium 3 is a reliable choice for tasks that require up-to-date information.

### Pricing and Use Cases
Mistral Medium 3 is priced at $0.4 per 1M input tokens and $2.0 per 1M output tokens, making it a cost-effective option for developers who need to perform complex tasks. The model is best suited for tasks such as coding, analysis, and content generation, but may not be the best choice for frontier reasoning, bulk cheap tasks, or simple classification. With cost examples ranging from $1.2 for 1,000 calls to $120.0 for 100,000 calls, developers can easily estimate the costs of using Mistral Medium 3 for their projects. Compared

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### Optimal Usage Scenarios
Given the cost structure, it's essential to understand when to utilize cached tokens and batch API calls to minimize costs.

* **Cached Tokens**: Since cached input tokens are free, it's highly recommended to use them whenever possible. This can significantly reduce costs for repeated input sequences.
* **Batch API Calls**: With batch input being free, batching API calls can lead to substantial savings, especially for large-scale applications.

#### Cost at Scale
To understand the cost implications of using Mistral Medium 3 at scale, let's examine the provided cost examples:
* **1,000 calls (avg 500 tokens)**: **$1.2**
* **10,000 calls**: **$12.0**
* **100,000 calls**: **$120.0**

These examples illustrate a linear cost increase with the number of API calls, indicating that the cost per call remains constant.

#### Comparison with Competitors
Mistral Medium 3's pricing can be compared to its top competitors:
* **Claude 3.5 Haiku**: $0.8/1M input, $4.0/1M output
* **GPT-4o Mini**: $0.15/1M input, $0.6/

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Medium 3 Benchmark Analysis
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. The model's pricing is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens

#### Benchmark Performance
The model's benchmark performance is as follows:
* **MMLU (Massive Multitask Language Understanding)**: 80.0 - This score indicates the model's ability to understand and perform a wide range of natural language processing tasks. A higher MMLU score suggests better performance in tasks such as text classification, sentiment analysis, and question answering.
* **HumanEval**: 77.5 - This score evaluates the model's ability to generate human-like code and understand programming concepts. A higher HumanEval score indicates better performance in coding tasks, such as code completion and code generation.
* **LMSYS Arena ELO**: 1200 - This score measures the model's overall performance in a competitive arena, where it is pitted against other models in various tasks. A higher ELO score suggests better performance in a wide range of tasks, including coding, analysis, and content generation.

#### Real-World Implications
The benchmark scores suggest that Mistral Medium 3 is a capable model for tasks such as:
* Coding: With a high HumanEval score, the model is well-suited for coding tasks, such as code completion and code generation.
* Analysis: The model's high MMLU score indicates good performance in tasks such as

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a unique set of capabilities and pricing. This comparison will delve into the details of Mistral Medium 3 and its top competitors, Claude 3.5 Haiku and GPT-4o Mini, highlighting their differences in pricing, performance, and use cases.

#### Pricing Comparison
The pricing models of these three competitors are as follows:

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

#### Performance Trade-offs
The performance of these models can be evaluated based on their benchmark scores:

* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

While the benchmark scores for Claude 3.5 Haiku and GPT-4o Mini are not available, Mistral Medium 3's scores indicate its strengths in coding, analysis, and other capabilities.

#### Capabilities and Use Cases
The capabilities and recommended use cases for each model are:

* **Mistral Medium 3**:
	+ Capabilities: text, vision, function_calling, json_mode, streaming, system_prompts
	+ Best for: coding, analysis, rag, summarization, vision_tasks, content_generation, function_calling
	+ Not good for: frontier_reasoning, bulk_cheap_tasks, simple_classification, real_time_sub_100ms
* **Claude 3.5 Haiku**: Not provided

## Best Use Cases
### Practical Advice for Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. With its capabilities in text, vision, function calling, JSON mode, streaming, and system prompts, it is best suited for tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling.

#### Top 5 Best Use Cases for Mistral Medium 3
1. **Coding and Software Development**: Mistral Medium 3 excels in coding tasks, making it an ideal choice for software development, code review, and code generation. Its ability to understand and generate code in various programming languages can significantly enhance developer productivity.
2. **Data Analysis and Summarization**: With its strong analytical capabilities, Mistral Medium 3 can efficiently summarize large datasets, providing insights and trends that might be difficult to discern manually. This makes it suitable for data analysis, report generation, and research papers.
3. **Vision Tasks**: The model's vision capabilities allow it to perform tasks such as image classification, object detection, and image generation. This can be applied in various industries, including healthcare, security, and entertainment.
4. **Content Generation**: Mistral Medium 3 can generate high-quality content, including articles, blog posts, and social media posts. Its ability to understand context and generate coherent text makes it an excellent choice for content creation tasks.
5. **Function Calling and API Integration**: The model's function calling capability enables it to integrate with external APIs and services, allowing for more complex and dynamic applications. This can be particularly useful in tasks such as data processing, automation, and workflow management.

#### Code Integration Example with OpenRouter
To integrate Mistral Medium 3 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Mistral Medium 3 model
model = openrouter.Model("mistral

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
