# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-20
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly in coding, analysis, and function calling. This model boasts an impressive architecture that supports capabilities such as text and vision processing, function calling, JSON mode, streaming, and system prompts. With a context window of 131,072 tokens and a maximum output of 4,096 tokens, Mistral Large 2 is well-suited for handling complex and lengthy inputs.

### Technical Strengths and Use Cases
The technical strengths of Mistral Large 2 are reflected in its benchmark scores: MMLU at 84.0, HumanEval at 92.0, LMSYS Arena ELO at 1225, and GSM8K at 93.0. These scores indicate the model's high performance in various tasks, making it an ideal choice for applications that require advanced language understanding and generation. The primary use cases for Mistral Large 2 include coding, analysis, retrieval-augmented generation (RAG), and agents, among others. However, it is not recommended for tasks that require embeddings, bulk processing at a low cost, real-time responses under 100ms, or vision-heavy applications.

### Pricing and Cost Considerations
The pricing for Mistral Large 2 is structured as follows: $3.0 per 1M input tokens and $9.0 per 1M output tokens. For example, 1,000 calls with an average of 500 tokens would cost $6.0, while 10,000 calls would cost $60.0, and 100,000 calls would cost $600.0. In comparison to its top competitor, GPT-4o, which charges $2.5/1M input and $10.0/1M output, Mistral Large

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

#### Optimal Usage Scenarios
To minimize costs, consider the following:
* **Cached Tokens**: Use cached input tokens whenever possible, as they are **free**. This can significantly reduce costs for repeated or similar input sequences.
* **Batch API Calls**: Take advantage of batch input, which is also **free**. This can lead to substantial savings when processing large volumes of data.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* **1,000 API calls** (avg 500 tokens): **$6.0**
* **10,000 API calls**: **$60.0**
* **100,000 API calls**: **$600.0**

These costs can be broken down into input and output costs. Assuming an average of 500 tokens per call, the total input tokens for each scenario would be:
* 1,000 calls: 500,000 tokens (0.5M)
* 10,000 calls: 5,000,000 tokens (5M)
* 100,000 calls: 50,000,000 tokens (50M)

Using the pricing structure, the estimated costs would be:
* 1,000 calls: (0.5M input tokens \* $3.0/1M)

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
The Mistral Large 2 model, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. It has a context window of 131,072 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2024-07.

#### Pricing
The pricing for Mistral Large 2 is as follows:
* Input: **$3.0 per 1M tokens**
* Output: **$9.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Benchmark Performance
The model's benchmark performance is as follows:
* **MMLU: 84.0** - The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to perform a wide range of natural language processing tasks. A higher MMLU score indicates better performance. In this case, Mistral Large 2 has a score of 84.0, indicating strong language understanding capabilities.
* **HumanEval: 92.0** - The HumanEval benchmark assesses a model's ability to generate code that is correct and functional. A higher HumanEval score indicates better coding abilities. With a score of 92.0, Mistral Large 2 demonstrates excellent coding capabilities.
* **LMSYS Arena ELO: 1225** - The LMSYS Arena ELO benchmark evaluates a model's performance in a competitive environment, where models are pitted against each other to complete tasks. A higher ELO score indicates better performance. Mistral

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, a premium model by Mistral AI, offers a unique set of capabilities, including text, vision, function calling, and more. Released on 2024-07-24, it has a context window of 131,072 tokens and a max output of 4,096 tokens. This comparison will focus on its top competitor, GPT-4o, highlighting price differences, performance trade-offs, and use cases for each model.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, while GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. For input-heavy workloads, GPT-4o is 16.67% cheaper, but for output-heavy workloads, Mistral Large 2 is 10% cheaper.

#### Performance Comparison
| Model | MMLU | HumanEval | LMSYS Arena ELO | GSM8K |
| --- | --- | --- | --- | --- |
| Mistral Large 2 | 84.0 | 92.0 | 1225 | 93.0 |
| GPT-4o | Not available | Not available | Not available | Not available |

Since performance metrics for GPT-4o are not provided, a direct comparison is not possible. However, Mistral Large 2's benchmarks indicate strong performance across various tasks, with an MMLU score of 84.0, HumanEval score of 92.0, LMSYS Arena ELO of 1225, and GSM8K score of 93.0.

#### Capabilities and Use Cases
Mistral Large 2 is best suited for:
* Coding
* Analysis
* RAG (Retrieve, Augment, Generate)
* Agents
* Multilingual tasks
* Function calling

It is not recommended for:
* Embeddings
* Bulk cheap processing


## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium model released on 2024-07-24. With its robust capabilities, including text, vision, function calling, and more, it is best suited for tasks such as coding, analysis, and multilingual applications. Here, we will explore the top 5 best use cases for Mistral Large 2, along with specific code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Large 2
1. **Coding and Development**: Mistral Large 2 excels in coding tasks, making it an excellent choice for developers. Its high score in HumanEval (92.0) demonstrates its proficiency in generating correct and functional code.
2. **Analysis and Research**: With its large context window (131,072 tokens) and high MMLU score (84.0), Mistral Large 2 is well-suited for in-depth analysis and research tasks, such as text analysis, sentiment analysis, and data analysis.
3. **RAG (Retrieval-Augmented Generation) Tasks**: Mistral Large 2's ability to handle function calling and its high score in LMSYS Arena ELO (1225) make it an excellent choice for RAG tasks, which involve retrieving information from external sources and generating text based on that information.
4. **Multilingual Applications**: Mistral Large 2's support for multilingual tasks makes it an ideal choice for applications that require text generation or analysis in multiple languages.
5. **Agent-Based Systems**: With its capabilities in function calling and system prompts, Mistral Large 2 can be used to build sophisticated agent-based systems that can interact with users and perform complex tasks.

### Code Integration Example with OpenRouter
To integrate Mistral Large 2 with OpenRouter, you can use the following example code:
```python
import openrouter

# Initialize the Mistral Large 2

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
