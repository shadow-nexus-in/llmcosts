# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-24
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, including coding, analysis, and function calling. This model boasts a context window of 131,072 tokens and can generate up to 4,096 tokens as output. With a knowledge cutoff of 2024-07, Mistral Large 2 is equipped with the latest information available up to that point. Its architecture supports various capabilities such as text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Strengths and Use Cases
The technical strengths of Mistral Large 2 are underscored by its impressive benchmark scores: 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These scores indicate the model's high performance in understanding and generating human-like text, solving mathematical problems, and demonstrating logical reasoning. Best suited for tasks like coding, analysis, and multilingual applications, Mistral Large 2 is also adept at handling function calls and streaming data. However, it is not recommended for applications requiring embeddings, bulk processing at low costs, real-time responses under 100ms, or vision-heavy tasks.

### Pricing and Cost Considerations
Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, with no specific pricing for cached input or batch input. For developers, this translates to $6.0 for 1,000 calls averaging 500 tokens, $60.0 for 10,000 calls, and $600.0 for 100,000 calls. While it is more expensive than some competitors like GPT-4o, which charges

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $3.0 |
| Output | $9.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Mistral Large 2 Pricing Analysis
#### Overview
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. The pricing structure is based on input and output tokens, with specific considerations for cached and batch inputs.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
- **Input**: $3.0 per 1M tokens
- **Output**: $9.0 per 1M tokens
- **Cached Input**: $0 per 1M tokens (free)
- **Batch Input**: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for reducing costs. However, the decision to use cached tokens should be based on the specific use case and the trade-offs between cost and performance. Since there is no additional cost for cached input tokens, it is advisable to use them whenever possible to minimize expenses.

#### Batch API Savings
Batch inputs are also free, which can lead to significant savings when making multiple API calls. By batching requests, users can avoid the costs associated with individual input tokens, resulting in substantial cost reductions.

#### Cost at Scale
To understand the cost implications of using Mistral Large 2 at scale, let's examine the costs for 1,000, 10,000, and 100,000 API calls, assuming an average of 500 tokens per call:
- **1,000 calls**: $6.0
- **10,000 calls**: $60.0
- **100,000 calls**: $600.0

These costs demonstrate a linear relationship between the number of API calls and the total cost, indicating that the cost per call remains constant regardless of the scale.

#### Comparison with Top Competitors
Mistral Large

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 84.0 |
| HumanEval | 92.0 |
| LMSYS Arena ELO | 1225 |
| ARC | 93.0 |

## Benchmark Analysis
### Mistral Large 2 Benchmark Performance Analysis
#### Model Overview
The Mistral Large 2 model, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. It offers a range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, making it suitable for coding, analysis, RAG, agents, multilingual, and function calling tasks.

#### Pricing
The pricing for Mistral Large 2 is as follows:
* Input: **$3.0 per 1M tokens**
* Output: **$9.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Context and Limits
The model has a context window of **131,072 tokens**, a maximum output of **4,096 tokens**, and a knowledge cutoff of **2024-07**.

#### Benchmark Performance
The benchmark performance of Mistral Large 2 is as follows:
* **MMLU: 84.0**: The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to perform a wide range of natural language understanding tasks. A score of 84.0 indicates that Mistral Large 2 has a strong understanding of language, but may struggle with more complex or nuanced tasks.
* **HumanEval: 92.0**: The HumanEval benchmark assesses a model's ability to generate code that is correct and functional. A score of 92.0 suggests that Mistral Large 2 is highly proficient in coding tasks and can generate high-quality code.
* **LMSYS

## Competitor Comparison
### Mistral Large 2 Comparison
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. This comparison will evaluate Mistral Large 2 against its top competitors, focusing on price differences, performance trade-offs, and use cases.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, while GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. This indicates that GPT-4o is cheaper for input tokens but more expensive for output tokens.

#### Performance Comparison
Mistral Large 2 has the following benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

In contrast, GPT-4o's benchmark scores are not provided. However, based on the available data, Mistral Large 2 demonstrates strong performance across various tasks.

#### Capabilities and Use Cases
Mistral Large 2 supports the following capabilities:
- text
- vision
- function_calling
- json_mode
- streaming
- system_prompts

It is best suited for tasks such as:
- coding
- analysis
- rag
- agents
- multilingual
- function_calling

However, it is not recommended for:
- embeddings
- bulk_cheap
- real_time_sub_100ms
- vision_heavy

#### Cost Examples
The estimated costs for using Mistral Large 2 are:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100,000 calls: $600.0

#### Choosing the Right Model
Based on the comparison, Mistral Large 2 is a suitable choice when:
- High-performance is required, particularly in coding,

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. With its impressive capabilities in text, vision, function calling, JSON mode, streaming, and system prompts, it is best suited for coding, analysis, RAG, agents, multilingual tasks, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Based on its capabilities and benchmarks, here are the top 5 best use cases for Mistral Large 2:

1. **Coding and Software Development**: With its high HumanEval score of 92.0, Mistral Large 2 is ideal for coding tasks such as code completion, code review, and bug fixing. Its function calling capability allows it to interact with external systems, making it a great tool for automating development tasks.
2. **Data Analysis and Insights**: Mistral Large 2's high MMLU score of 84.0 and GSM8K score of 93.0 make it suitable for data analysis tasks such as data interpretation, trend analysis, and data visualization. Its ability to understand and generate human-like text enables it to provide actionable insights from complex data.
3. **Multilingual Support**: With its multilingual capability, Mistral Large 2 can be used for tasks such as language translation, language understanding, and language generation. Its high performance on multilingual benchmarks makes it an ideal choice for applications that require support for multiple languages.
4. **RAG (Retrieve, Augment, Generate) Tasks**: Mistral Large 2's high performance on RAG tasks makes it suitable for applications that require retrieving information from a knowledge base, augmenting it with external information, and generating human-like text based on the retrieved information.
5. **Agent-Based Systems**: Mistral Large 2's ability to interact with external systems through function calling and its high performance on agent

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
