# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-09
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, including coding, analysis, and function calling. This model boasts a context window of 131,072 tokens and can generate up to 4,096 tokens as output. With a knowledge cutoff of 2024-07, Mistral Large 2 is equipped to handle tasks that require up-to-date information up to that point. Its capabilities extend to text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Strengths and Use Cases
Mistral Large 2 demonstrates its strengths through impressive benchmark scores: 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These scores underscore its potential for coding, analysis, and other tasks that require a deep understanding of context and the ability to generate coherent, informative responses. The model is best utilized for applications such as coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual tasks, and function calling. However, it may not be the most cost-effective option for embeddings, bulk operations seeking cheap rates, real-time applications requiring responses under 100ms, or vision-heavy tasks.

### Pricing and Cost Considerations
The pricing for Mistral Large 2 is structured as follows: $3.0 per 1M tokens for input, $9.0 per 1M tokens for output, with no specified costs for cached input or batch input. For developers, this translates to $6.0 for 1,000 calls averaging 500 tokens, $60.0 for 10,000 calls, and $600.0 for 100,000 calls. In

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
Mistral Large 2, a premium model by Mistral AI, offers a unique set of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. The pricing structure is based on input and output tokens.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for reducing costs. Use cached tokens when:
* The input data is repetitive or has a high degree of similarity.
* The model is being used for tasks that require frequent reuse of input data.

#### Batch API Savings
Batch input is also free, which can lead to significant cost savings when making multiple API calls. To maximize batch API savings:
* Batch similar requests together to minimize the number of API calls.
* Use batch input for tasks that require processing large amounts of data.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* 1,000 calls (avg 500 tokens): $6.0
* 10,000 calls: $60.0
* 100,000 calls: $600.0

These costs can be broken down into input and output costs. Assuming an average of 500 tokens per call, the total number of tokens for each scenario is:
* 1,000 calls: 500,000 tokens
* 10,000 calls: 5,000,000 tokens
* 100,000 calls: 50,000,000 tokens

Using the pricing structure, the estimated costs

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
The Mistral Large 2 model, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. It is capable of handling a wide range of tasks, including coding, analysis, and function calling, with support for text, vision, and other functionalities.

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

#### Benchmark Performance
The benchmark performance of Mistral Large 2 is as follows:
* MMLU: **84.0**
* HumanEval: **92.0**
* LMSYS Arena ELO: **1225**
* GSM8K: **93.0**

These benchmark scores indicate the model's performance in various areas:
* **MMLU (Massive Multitask Language Understanding)**: Measures the model's ability to understand and generate human-like text across a wide range of tasks. A score of 84.0 indicates strong performance in this area.
* **HumanEval**: Evaluates the model's ability to write correct and functional code. A score of 92.0 suggests excellent performance in coding tasks.
* **LMSYS Arena ELO**: Measures the model's

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
Mistral Large 2, a premium model provided by Mistral AI, is a robust language model with a wide range of capabilities, including text, vision, function calling, and more. Released on 2024-07-24, it offers a unique set of features and performance metrics. Here, we compare Mistral Large 2 with its top competitor, GPT-4o, highlighting price differences, performance trade-offs, and scenarios where each model is best suited.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, whereas GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. For input-intensive tasks, GPT-4o might be more cost-effective, but for tasks with a higher output requirement, Mistral Large 2 could offer better value.

#### Performance Comparison
Mistral Large 2 boasts impressive benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

While GPT-4o's benchmark scores are not provided in the data, Mistral Large 2's scores indicate strong performance across various tasks, including coding, analysis, and multilingual capabilities.

#### Capabilities and Limits
Mistral Large 2 supports a wide range of capabilities, including:
- Text
- Vision
- Function calling
- JSON mode
- Streaming
- System prompts

It has a context window of 131,072 tokens and a maximum output of 4,096 tokens. The knowledge cutoff is 2024-07, ensuring that the model is trained on data up to that point.

#### Best Use Cases
Mistral Large 2 is best suited for tasks such as:
- Coding
- Analysis
- RAG (Retrieval-Augmented Generation)
- Agents
- Multilingual

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model that excels in various tasks, including coding, analysis, and function calling. With its impressive benchmarks (MMLU: 84.0, HumanEval: 92.0, LMSYS Arena ELO: 1225, GSM8K: 93.0) and capabilities (text, vision, function_calling, json_mode, streaming, system_prompts), it's a powerful tool for developers and researchers.

### Top 5 Best Use Cases for Mistral Large 2
Based on its capabilities and performance, here are the top 5 best use cases for Mistral Large 2:

1. **Coding and Code Analysis**: With its high HumanEval score (92.0), Mistral Large 2 is well-suited for coding tasks, such as code completion, code review, and code optimization.
2. **Multilingual Support**: As a multilingual model, Mistral Large 2 can be used for tasks that require language translation, language understanding, and language generation.
3. **RAG (Retrieve, Augment, Generate) Tasks**: Mistral Large 2's ability to retrieve and generate text makes it an excellent choice for RAG tasks, such as question answering, text summarization, and content generation.
4. **Function Calling and API Integration**: With its function_calling capability, Mistral Large 2 can be used to integrate with external APIs and services, enabling developers to build more complex and dynamic applications.
5. **Analysis and Insights**: Mistral Large 2's analysis capabilities make it an excellent choice for tasks that require data analysis, insights generation, and decision-making.

### Code Integration Examples with OpenRouter
To integrate Mistral Large 2 with OpenRouter, you can use the following code examples:

```python
import open

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
