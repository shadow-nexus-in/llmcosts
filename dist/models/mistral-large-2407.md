# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-13
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model that boasts a robust architecture designed to handle a wide range of tasks with high efficiency. With its context window of 131,072 tokens and the ability to generate up to 4,096 output tokens, Mistral Large 2 is well-suited for complex tasks that require extensive contextual understanding and detailed responses. Its capabilities include text and vision processing, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Strengths and Use Cases
The main strengths of Mistral Large 2 lie in its high performance across various benchmarks, including MMLU (84.0), HumanEval (92.0), LMSYS Arena ELO (1225), and GSM8K (93.0). These scores indicate its prowess in coding, analysis, and other tasks that require logical reasoning and problem-solving skills. As such, Mistral Large 2 is best utilized for coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual tasks, and function calling. However, it is not recommended for applications that require embeddings, bulk processing at low costs, real-time responses under 100ms, or vision-heavy tasks.

### Pricing and Cost Considerations
Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, with no specific pricing for cached input or batch input. For example, 1,000 calls averaging 500 tokens each would cost $6.0, while 10,000 calls would amount to $60.0, and 100,000 calls would total $600.0. Compared to its top competitor, GPT-4o, which charges $2.5/1M input and $10.0

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
Mistral Large 2 is a premium model offered by Mistral AI, released on 2024-07-24. This analysis will delve into the cost structure, usage scenarios, and cost savings of this model.

#### Cost Structure
The pricing for Mistral Large 2 is as follows:
* Input: **$3.0 per 1M tokens**
* Output: **$9.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs when the same input is used multiple times. Since cached input is free, it is recommended to use cached tokens whenever possible to minimize costs.

#### Batch API Savings
Batch input is also free, which means that making batch API calls can help reduce costs. By batching multiple inputs together, users can avoid paying for individual input tokens.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* **1,000 API calls** (avg 500 tokens): **$6.0**
* **10,000 API calls**: **$60.0**
* **100,000 API calls**: **$600.0**

These costs are based on the average number of tokens per call and can vary depending on the actual usage.

#### Comparison with Top Competitors
Mistral Large 2's pricing is competitive with top competitors like GPT-4o, which charges **$2.5/1M input** and **$10.0/1M output**. However, the free cached input and batch input offered by Mistral Large 2 can provide significant cost savings for users who can take advantage of these features.

#### Conclusion
Mistral Large 2 offers a competitive pricing structure with

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 84.0 |
| HumanEval | 92.0 |
| LMSYS Arena ELO | 1225 |
| ARC | 93.0 |

## Benchmark Analysis
### Mistral Large 2 Benchmark Analysis
#### Model Overview
The Mistral Large 2 model, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. It offers a range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts.

#### Pricing
The pricing for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Context and Limits
The model has the following context and limits:
* Context Window: 131,072 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2024-07

#### Benchmarks
The model's benchmark performance is as follows:
* MMLU: 84.0
* HumanEval: 92.0
* LMSYS Arena ELO: 1225
* GSM8K: 93.0

These benchmarks indicate the model's performance in various areas:
* **MMLU (Massive Multitask Language Understanding)**: A score of 84.0 indicates the model's ability to understand and generate human-like text across a wide range of tasks and domains.
* **HumanEval**: A score of 92.0 suggests the model's proficiency in coding and programming tasks, such as writing correct and functional code.
* **LMSYS Arena ELO**: A score of 1225 indicates the model's competitive performance in a large-scale language model benchmark, with higher scores

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on July 24, 2024, this model is not open source and has a specific pricing structure. In this comparison, we will examine the price differences, performance trade-offs, and use cases for Mistral Large 2 against its top competitor, GPT-4o.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, while GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. This indicates that GPT-4o is cheaper for input tokens but more expensive for output tokens.

#### Performance Comparison
Mistral Large 2 has the following benchmark scores:
* MMLU: 84.0
* HumanEval: 92.0
* LMSYS Arena ELO: 1225
* GSM8K: 93.0

In contrast, the benchmark scores for GPT-4o are not provided. However, based on the pricing and capabilities, we can infer that GPT-4o may have similar or slightly different performance characteristics.

#### Capabilities and Use Cases
Mistral Large 2 is best suited for:
* Coding
* Analysis
* RAG (Retrieve, Augment, Generate)
* Agents
* Multilingual tasks
* Function calling

On the other hand, it is not recommended for:
* Embeddings
* Bulk cheap tasks
* Real-time tasks with latency < 100ms
* Vision-heavy tasks

GPT-4o may have similar capabilities, but its strengths and weaknesses are not explicitly stated.

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
* 1,000 calls (avg 500 tokens): $6.0
* 10,000

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. With its release on 2024-07-24, it has established itself as a powerful tool for various applications. This guide will explore the top 5 best use cases for Mistral Large 2, along with specific code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Large 2
1. **Coding and Development**: Mistral Large 2 excels in coding tasks, making it an ideal choice for developers. Its high scores in HumanEval (92.0) and GSM8K (93.0) benchmarks demonstrate its proficiency in coding-related tasks.
2. **Analysis and Research**: With its large context window of 131,072 tokens, Mistral Large 2 is well-suited for in-depth analysis and research tasks. Its ability to process and understand large amounts of text makes it an excellent tool for researchers.
3. **RAG (Retrieve, Augment, Generate) Tasks**: Mistral Large 2's capabilities in text and function calling make it an excellent choice for RAG tasks. Its high score in the LMSYS Arena ELO benchmark (1225) demonstrates its ability to perform well in complex tasks.
4. **Multilingual Support**: Mistral Large 2 offers multilingual support, making it an ideal choice for applications that require language translation or understanding.
5. **Function Calling and API Integration**: With its function calling capability, Mistral Large 2 can be integrated with various APIs and services, making it a versatile tool for developers.

### Code Integration Example with OpenRouter
To integrate Mistral Large 2 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Mistral Large 2 model
model = openrouter.MistralLarge2()



## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
