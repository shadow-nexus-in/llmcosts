# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-21
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, developed by Mistral AI, is a premium, non-open-source language model released on 2024-07-24. This model is part of the Mistral AI suite, offering advanced capabilities such as text, vision, function calling, JSON mode, streaming, and system prompts. With a context window of 131,072 tokens and a maximum output of 4,096 tokens, Mistral Large 2 is designed to handle complex tasks with a knowledge cutoff of 2024-07.

### Architecture and Strengths
The architecture of Mistral Large 2 is not explicitly detailed, but its capabilities suggest a robust and versatile design. Its main strengths are evident in its benchmark scores: MMLU at 84.0, HumanEval at 92.0, LMSYS Arena ELO at 1225, and GSM8K at 93.0. These scores indicate that Mistral Large 2 excels in areas such as coding, analysis, and function calling, making it suitable for applications like agents, multilingual tasks, and RAG (Retrieval-Augmented Generation). The model's pricing is set at $3.0 per 1M input tokens and $9.0 per 1M output tokens, with no specified costs for cached input or batch input.

### Use Cases and Cost Considerations
Mistral Large 2 is best utilized for tasks that require advanced language understanding and generation capabilities, such as coding, analysis, and function calling. However, it is not recommended for tasks that require embeddings, bulk processing at low costs, real-time responses under 100ms, or vision-heavy applications. The cost of using Mistral Large 2 can be estimated based on the number of calls and tokens processed. For example, 1,000 calls with an average of 500 tokens would cost $6.0, while 10,000 calls would amount

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
Mistral Large 2 is a premium model offered by Mistral AI, released on 2024-07-24. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale.

#### Cost Structure
The pricing for Mistral Large 2 is as follows:
* Input: **$3.0 per 1M tokens**
* Output: **$9.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for repeated input sequences. If your application involves frequent reuse of input tokens, utilizing cached tokens can significantly reduce costs.

#### Batch API Savings
Batch input is also free, which means that batching API calls can lead to substantial cost savings. By grouping multiple input sequences into a single API call, you can avoid incurring additional input costs.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* **1,000 calls** (avg 500 tokens): **$6.0**
* **10,000 calls**: **$60.0**
* **100,000 calls**: **$600.0**

These costs demonstrate a linear relationship between the number of API calls and the total cost.

#### Comparison to Top Competitors
Mistral Large 2's pricing is comparable to its top competitor, GPT-4o:
* GPT-4o: **$2.5/1M input**, **$10.0/1M output**
* Mistral Large 2: **$3.0/1M input**, **$9.0/1M output**

While GPT-4o has a lower input cost, Mistral Large 2 has a

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 84.0 |
| HumanEval | 92.0 |
| LMSYS Arena ELO | 1225 |
| ARC | 93.0 |

## Benchmark Analysis
### Mistral Large 2 Benchmark Performance Analysis
#### Overview
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is geared towards coding, analysis, and multilingual applications.

#### Pricing
The pricing structure for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Benchmarks
The model's performance is measured through several benchmarks:
* **MMLU (Massive Multitask Language Understanding)**: 84.0 - This score indicates the model's ability to understand and perform a wide range of language tasks. A higher score suggests better performance in tasks such as text classification, sentiment analysis, and question answering.
* **HumanEval**: 92.0 - This benchmark evaluates the model's ability to generate human-like code. A higher score indicates better coding capabilities, making it suitable for applications such as coding assistance and code review.
* **LMSYS Arena ELO**: 1225 - This score measures the model's performance in a competitive environment, where it is pitted against other models. A higher ELO score suggests better overall performance and adaptability.
* **GSM8K**: 93.0 - This benchmark assesses the model's ability to solve math problems, with a higher score indicating better math reasoning skills.

#### Real-World Implications
The benchmark scores suggest that Mistral Large 2

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. In this comparison, we will evaluate Mistral Large 2 against its top competitor, GPT-4o, focusing on price differences, performance trade-offs, and use cases.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, whereas GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. This indicates that GPT-4o is cheaper for input tokens but more expensive for output tokens.

#### Performance Comparison
Mistral Large 2 has the following benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

In contrast, the benchmark scores for GPT-4o are not provided. However, we can compare the capabilities and limitations of both models to determine their suitability for specific use cases.

#### Capabilities and Limitations
Mistral Large 2 is best suited for:
- Coding
- Analysis
- RAG (Retrieval-Augmented Generation)
- Agents
- Multilingual tasks
- Function calling

It is not recommended for:
- Embeddings
- Bulk cheap processing
- Real-time processing with sub-100ms latency
- Vision-heavy tasks

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100,000 calls: $600.0

#### Choosing the Right Model
Based on the comparison, Mistral Large 2 is

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium model with a wide range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. Released on 2024-07-24, this model excels in coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual tasks, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Given its capabilities and pricing, here are the top 5 best use cases for Mistral Large 2:

1. **Coding and Development**: With its high scores in HumanEval (92.0) and GSM8K (93.0), Mistral Large 2 is ideal for coding tasks, such as code completion, code review, and code generation. Its ability to understand and generate code in multiple languages makes it a valuable tool for developers.
2. **Analysis and Research**: The model's high MMLU score (84.0) and large context window (131,072 tokens) make it suitable for in-depth analysis and research tasks, such as text analysis, sentiment analysis, and information retrieval.
3. **RAG and Knowledge Retrieval**: Mistral Large 2's capabilities in RAG and knowledge retrieval make it an excellent choice for applications that require retrieving and generating text based on a large knowledge base.
4. **Multilingual Support**: With its support for multiple languages, Mistral Large 2 is ideal for applications that require language translation, language understanding, and multilingual text generation.
5. **Function Calling and Automation**: The model's ability to call functions and automate tasks makes it a great choice for automating workflows, data processing, and other tasks that require function calling.

### Code Integration Examples with OpenRouter
To integrate Mistral Large 2 with OpenRouter, you can use the following code examples:

```python
import openrouter



## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
