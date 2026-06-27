# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-27
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly in coding, analysis, and multilingual tasks. This model boasts a context window of 131,072 tokens and can generate up to 4,096 tokens as output. With a knowledge cutoff of 2024-07, Mistral Large 2 is equipped with the latest information available up to that point. Its architecture supports various capabilities including text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Strengths and Use Cases
Mistral Large 2 demonstrates its strengths through impressive benchmark scores: 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These scores indicate the model's high performance in coding, problem-solving, and understanding complex tasks. It is best utilized for coding, analysis, retrieval-augmented generation (RAG), agents, multilingual tasks, and function calling. However, it is not recommended for applications requiring embeddings, bulk cheap processing, real-time responses under 100ms, or vision-heavy tasks. The pricing model charges $3.0 per 1M input tokens and $9.0 per 1M output tokens, with no specified charges for cached input or batch input.

### Pricing and Cost Considerations
For developers planning to integrate Mistral Large 2 into their projects, understanding the pricing model is crucial. The cost can be estimated based on the number of calls and average tokens per call. For example, 1,000 calls with an average of 500 tokens per call would cost $6.0, scaling up to $60.0 for 10,000 calls and $600.

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
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. The pricing structure for Mistral Large 2 is based on input and output tokens.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for reducing costs. However, the context window limit of 131,072 tokens and the knowledge cutoff of 2024-07 should be considered when deciding whether to use cached tokens. If the input data is within the context window and does not require knowledge beyond the cutoff date, cached tokens can be a cost-effective option.

#### Batch API Savings
Batch input is also free, which can lead to significant savings when making multiple API calls. By batching API requests, users can avoid paying for input tokens, resulting in cost savings.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* 1,000 calls (avg 500 tokens): $6.0
* 10,000 calls: $60.0
* 100,000 calls: $600.0

These costs are based on the average number of tokens per call and do not take into account the potential savings from using cached tokens or batch API calls.

#### Comparison to Top Competitors
Mistral Large 2 is priced competitively with top competitors like GPT-4o, which charges $2.5/1M input

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
* **MMLU (Massive Multitask Language Understanding)**: A score of 84.0 indicates the model's ability to understand and process natural language across a wide range of tasks.
* **HumanEval**: A score of 92.0 suggests the model's ability to generate human-like text and respond to prompts in a way that is coherent and contextually relevant.
* **LMSYS Arena ELO**: A score of 1225 indicates the model's performance in a competitive environment, where it is

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, a premium model by Mistral AI, is a powerful language model with a wide range of capabilities, including text, vision, function calling, and more. Released on 2024-07-24, it offers a unique set of features and performance metrics. In this comparison, we will analyze Mistral Large 2 against its top competitors, focusing on price differences, performance trade-offs, and use cases.

#### Pricing Comparison
The pricing for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens

In comparison, GPT-4o, a top competitor, offers:
* Input: $2.5 per 1M tokens
* Output: $10.0 per 1M tokens

While GPT-4o is cheaper for input tokens, Mistral Large 2 is more cost-effective for output tokens. This difference in pricing strategy may influence the choice of model depending on the specific use case.

#### Performance Trade-offs
Mistral Large 2 boasts impressive benchmark scores:
* MMLU: 84.0
* HumanEval: 92.0
* LMSYS Arena ELO: 1225
* GSM8K: 93.0

These scores indicate strong performance in various areas, including coding, analysis, and multilingual capabilities. However, the model's limitations, such as a context window of 131,072 tokens and a max output of 4,096 tokens, may impact its suitability for certain applications.

#### When to Choose Each Model
Mistral Large 2 is best suited for:
* Coding and analysis tasks
* Multilingual applications
* Function calling and system prompts
* Applications that require a balance between input and output costs

On the other hand, GPT-4o may be a better choice for:
* Applications with high input token requirements, where the lower input cost can lead to significant savings
* Use cases that prioritize output quality over cost, given its higher output cost

#### Cost Examples
To illustrate the cost differences, consider the following examples:
* 1,000 calls (avg 500 tokens): Mistral Large 2 costs $6.0, while GPT-4o would cost approximately $5.0 (assuming a similar output

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model that excels in various tasks, including coding, analysis, and function calling. With its impressive benchmarks (MMLU: 84.0, HumanEval: 92.0, LMSYS Arena ELO: 1225, GSM8K: 93.0) and capabilities (text, vision, function_calling, json_mode, streaming, system_prompts), it is an ideal choice for applications requiring advanced language understanding and generation.

### Top 5 Best Use Cases for Mistral Large 2
1. **Coding and Software Development**: Mistral Large 2's high HumanEval score (92.0) makes it suitable for coding tasks, such as code completion, code review, and bug fixing. Its ability to understand and generate code in multiple programming languages is a significant advantage.
2. **Data Analysis and Insights**: With its strong analytical capabilities, Mistral Large 2 can be used for data analysis, report generation, and providing insights from large datasets. Its ability to process and understand natural language queries makes it an excellent choice for data-driven applications.
3. **Conversational Agents and Chatbots**: Mistral Large 2's high LMSYS Arena ELO score (1225) indicates its potential in building conversational agents and chatbots that can engage in meaningful discussions and provide helpful responses.
4. **Multilingual Support and Translation**: As a multilingual model, Mistral Large 2 can be used for translation tasks, language understanding, and generation. Its ability to process and generate text in multiple languages makes it an excellent choice for global applications.
5. **Function Calling and API Integration**: Mistral Large 2's function_calling capability allows it to integrate with external APIs and services, making it suitable for tasks that require interacting with external systems

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
