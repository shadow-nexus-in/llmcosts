# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-28
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly in coding, analysis, and multilingual tasks. This model boasts a context window of 131,072 tokens and can generate outputs of up to 4,096 tokens. With its knowledge cutoff in July 2024, Mistral Large 2 is equipped with the latest information available up to that point. Its architecture supports various capabilities including text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Strengths and Use Cases
Mistral Large 2 demonstrates its technical prowess through impressive benchmark scores: 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These scores underscore its effectiveness in coding, analysis, and other complex tasks. The model is best utilized for applications such as coding assistance, in-depth analysis, retrieval-augmented generation (RAG), agent development, and multilingual support. However, it's not recommended for tasks requiring embeddings, bulk processing at low costs, real-time responses under 100ms, or vision-intensive applications. The pricing model is based on input and output tokens, with costs of $3.0 per 1M input tokens and $9.0 per 1M output tokens.

### Pricing and Cost Considerations
Developers should be aware of the pricing structure to optimize their usage of Mistral Large 2. The cost examples provided indicate that for 1,000 calls averaging 500 tokens, the cost would be $6.0, scaling up to $60.0 for 10,000 calls and $600.0 for 100,000 calls. In comparison to its top competitor

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
Mistral Large 2, a premium model offered by Mistral AI, boasts an impressive set of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is particularly suited for coding, analysis, and multilingual tasks. The following analysis breaks down the cost structure, optimal usage scenarios, and provides a detailed examination of the costs at scale.

#### Cost Structure
The pricing for Mistral Large 2 is as follows:
- **Input**: $3.0 per 1M tokens
- **Output**: $9.0 per 1M tokens
- **Cached Input**: $0 per 1M tokens (free)
- **Batch Input**: $0 per 1M tokens (free)

This structure indicates that users can significantly reduce costs by leveraging cached input and batch processing for their API calls.

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for reducing costs. Users should utilize cached tokens whenever possible, especially for repetitive or similar input queries. This can lead to substantial savings, especially in applications where the same or similar inputs are processed multiple times.

#### Batch API Savings
Similar to cached input, batch input is also free. Batch processing can significantly reduce the overall cost of API calls by minimizing the number of requests made to the server. Users should batch their inputs whenever feasible to take advantage of this cost-saving measure.

#### Cost at Scale
To understand the cost implications of using Mistral Large 2 at scale, let's examine the provided cost examples:
- **1,000 calls (avg 500 tokens)**: $6.0
- **10,000 calls**: $60.0
- **100,000 calls**: $600.0

These examples illustrate a linear scaling of costs with the number of API calls. For applications requiring a large volume of requests, it's essential to consider

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
The Mistral Large 2 model, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. It boasts a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts, making it suitable for applications such as coding, analysis, and multilingual tasks.

#### Pricing Structure
The pricing for Mistral Large 2 is as follows:
- Input: $3.0 per 1M tokens
- Output: $9.0 per 1M tokens
With no specified pricing for cached input or batch input.

#### Context and Limits
The model has a context window of 131,072 tokens, a maximum output of 4,096 tokens, and a knowledge cutoff of 2024-07.

#### Benchmark Performance
The model's performance is benchmarked across several metrics:
- **MMLU (Massive Multitask Language Understanding)**: A score of 84.0, indicating the model's ability to understand and perform a wide range of language tasks.
- **HumanEval**: A score of 92.0, suggesting the model's proficiency in generating code that passes human evaluation, which is crucial for coding and programming tasks.
- **LMSYS Arena ELO**: A score of 1225, which reflects the model's competitive performance in a large-scale language model benchmarking arena, indicating its overall language understanding and generation capabilities.
- **GSM8K**: A score of 93.0, demonstrating the model's performance on a math problem-solving benchmark, which is relevant for tasks requiring logical reasoning and mathematical insights.

#### Real-World

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. This comparison will focus on its pricing, performance, and trade-offs against its top competitor, GPT-4o.

#### Pricing Comparison
| Model | Input Price per 1M Tokens | Output Price per 1M Tokens |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, whereas GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. This indicates that while GPT-4o is cheaper for input, Mistral Large 2 is more cost-effective for output.

#### Performance Comparison
Mistral Large 2 has the following benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

In contrast, the benchmark scores for GPT-4o are not provided in the data. However, based on the capabilities and pricing, we can infer that both models are high-performance and suitable for demanding tasks.

#### Capabilities and Use Cases
Mistral Large 2 is best suited for:
- Coding
- Analysis
- RAG (Retrieval-Augmented Generation)
- Agents
- Multilingual tasks
- Function calling

It is not recommended for:
- Embeddings
- Bulk cheap tasks
- Real-time tasks with sub-100ms latency
- Vision-heavy tasks

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100,000 calls: $600.0

#### Choosing Between Mistral Large 2 and GPT-4o
Based

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model that offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. With its strong performance in benchmarks such as MMLU (84.0), HumanEval (92.0), LMSYS Arena ELO (1225), and GSM8K (93.0), it is best suited for tasks like coding, analysis, RAG, agents, multilingual support, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
1. **Coding and Development**: Given its high score in HumanEval (92.0), Mistral Large 2 is particularly adept at coding tasks. It can assist in writing code, debugging, and optimizing existing codebases.
2. **Complex Analysis and Reasoning**: With its strong performance in MMLU (84.0) and GSM8K (93.0), Mistral Large 2 is well-suited for complex analytical tasks that require deep understanding and reasoning.
3. **Multilingual Support**: Its capability for multilingual support makes it an excellent choice for applications that need to serve a diverse, globally distributed user base.
4. **Function Calling and Integration**: Mistral Large 2's ability to perform function calling and its support for JSON mode make it a good fit for integrating with other services and systems, such as OpenRouter, for more complex workflows.
5. **Agent-Based Systems**: Its suitability for agents, combined with its analytical capabilities, positions Mistral Large 2 as a strong candidate for building intelligent agent-based systems that can interact with users or other systems effectively.

### Code Integration Example with OpenRouter
To integrate Mistral Large 2 with OpenRouter for a coding task, you might use a Python client that interacts with the Mistral AI API.

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
