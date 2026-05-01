# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-01
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly in coding, analysis, and function calling. This model boasts a context window of 131,072 tokens and can generate up to 4,096 tokens as output. With a knowledge cutoff of 2024-07, Mistral Large 2 is equipped with the latest information available up to that point. Its architecture supports various capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Strengths and Use Cases
The technical strengths of Mistral Large 2 are reflected in its benchmark scores: MMLU at 84.0, HumanEval at 92.0, LMSYS Arena ELO at 1225, and GSM8K at 93.0. These scores indicate the model's proficiency in understanding and generating human-like text, solving mathematical problems, and performing well in competitive arenas. Best suited for tasks such as coding, analysis, retrieval-augmented generation (RAG), and multilingual applications, Mistral Large 2 is also adept at handling function calls. However, it is not recommended for applications requiring embeddings, bulk cheap processing, real-time responses under 100ms, or vision-heavy tasks.

### Pricing and Cost Considerations
The pricing for Mistral Large 2 is structured as follows: $3.0 per 1M input tokens and $9.0 per 1M output tokens. For developers, this translates to specific costs based on the number of calls and tokens processed. For example, 1,000 calls averaging 500 tokens each would cost $6.0, while 10,000 calls would amount to $60.0, and 100,000 calls would total $600.

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
* **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
* **Batch API**: With batch input being free, batching API calls can lead to significant cost savings, especially for large-scale applications.

#### Cost at Scale
The cost of using Mistral Large 2 at various scales is as follows:
* **1,000 calls (avg 500 tokens)**: **$6.0**
* **10,000 calls**: **$60.0**
* **100,000 calls**: **$600.0**

To put these costs into perspective, let's calculate the cost per 1M tokens:
* Assuming an average of 500 tokens per call, 1,000 calls would be equivalent to 0.5M tokens.
* The cost for 1,000 calls is $6.0, which translates to **$12.0 per 1M tokens**.
* Similarly, for 10,000 calls (5M tokens), the cost is $60.0, which is **$12.0 per 1M tokens**.
* For 100,000 calls (50M tokens), the cost is $600.0, which is **$12.0 per 1

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
The Mistral Large 2 model, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. It offers a range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, making it suitable for applications such as coding, analysis, and multilingual tasks.

#### Pricing
The pricing for Mistral Large 2 is as follows:
- Input: $3.0 per 1M tokens
- Output: $9.0 per 1M tokens
With no pricing specified for cached input or batch input.

#### Context and Limits
The model has a context window of 131,072 tokens, a maximum output of 4,096 tokens, and a knowledge cutoff of 2024-07.

#### Benchmark Performance
The model's performance is measured across several benchmarks:
- **MMLU (Massive Multitask Language Understanding)**: 84.0. This score indicates the model's ability to understand and perform a wide range of natural language tasks. A higher score suggests better performance in tasks that require a broad understanding of language.
- **HumanEval**: 92.0. This benchmark evaluates the model's ability to generate code that passes a set of unit tests, simulating human evaluation. A higher score here indicates the model is more effective at producing functional code.
- **LMSYS Arena ELO**: 1225. The LMSYS Arena is a platform for evaluating the performance of large language models in a competitive setting. The ELO score is a measure of the model's strength relative to other models, with higher scores indicating better

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. This comparison will focus on its pricing, performance, and capabilities in relation to its top competitor, GPT-4o.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, whereas GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. This indicates that while GPT-4o is cheaper for input, Mistral Large 2 is slightly more economical for output.

#### Performance Comparison
Mistral Large 2 has the following benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

In contrast, the benchmark scores for GPT-4o are not provided in the data. However, based on the available information, Mistral Large 2 demonstrates strong performance across various tasks, suggesting it may be a more capable model.

#### Capabilities and Use Cases
Mistral Large 2 supports the following capabilities:
- Text
- Vision
- Function calling
- JSON mode
- Streaming
- System prompts

It is best suited for tasks such as:
- Coding
- Analysis
- RAG (Retrieve, Augment, Generate)
- Agents
- Multilingual tasks
- Function calling

On the other hand, it is not recommended for:
- Embeddings
- Bulk cheap tasks
- Real-time tasks with sub-100ms latency
- Vision-heavy tasks

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100,000 calls

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium model that offers a wide range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. With its high performance benchmarks (MMLU: 84.0, HumanEval: 92.0, LMSYS Arena ELO: 1225, GSM8K: 93.0), it is best suited for coding, analysis, RAG, agents, multilingual, and function calling tasks.

### Top 5 Best Use Cases for Mistral Large 2
1. **Coding and Software Development**: Mistral Large 2 excels in coding tasks, making it an ideal choice for software development, code review, and code generation. Its high HumanEval score (92.0) demonstrates its ability to understand and generate high-quality code.
2. **Data Analysis and Insights**: With its strong analysis capabilities, Mistral Large 2 can be used to analyze large datasets, provide insights, and generate reports. Its high MMLU score (84.0) indicates its ability to understand and process complex data.
3. **Multilingual Support**: Mistral Large 2 offers multilingual support, making it an excellent choice for applications that require language translation, language understanding, and language generation.
4. **Function Calling and API Integration**: Mistral Large 2's function calling capability allows it to integrate with external APIs and services, enabling the development of more complex and dynamic applications.
5. **RAG (Retrieve, Augment, Generate) Tasks**: Mistral Large 2's RAG capabilities make it suitable for tasks that require retrieving information, augmenting existing data, and generating new content.

### Code Integration Example with OpenRouter
To integrate Mistral Large 2 with OpenRouter, you can use the following code example:
```python
import openrouter

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
