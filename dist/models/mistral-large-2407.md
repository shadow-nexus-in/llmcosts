# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-02
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly excelling in coding, analysis, and function calling tasks. This model boasts a context window of 131,072 tokens and can generate up to 4,096 tokens as output. With a knowledge cutoff of 2024-07, Mistral Large 2 is well-equipped to handle tasks that require up-to-date information up to its knowledge cutoff date.

### Architecture and Strengths
The architecture of Mistral Large 2 supports multiple capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. Its strengths are reflected in its benchmark scores: 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These scores indicate the model's high performance in various tasks, making it suitable for applications that require advanced language understanding and generation capabilities. The model's pricing is set at $3.0 per 1M input tokens and $9.0 per 1M output tokens, with no charges for cached or batch input.

### Use Cases and Cost Considerations
Mistral Large 2 is best utilized for coding, analysis, RAG (Retrieve, Augment, Generate), agents, multilingual tasks, and function calling. However, it is not recommended for embeddings, bulk cheap tasks, real-time applications requiring sub-100ms responses, or vision-heavy tasks. The cost of using Mistral Large 2 can be estimated based on the number of calls and average tokens per call. For example, 1,000 calls with an average of 500 tokens per call would cost $6.0, while 10,000 calls would amount to $60.0, and

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
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. The pricing structure is based on input and output tokens, with specific considerations for cached input and batch API calls.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
- **Input**: $3.0 per 1M tokens
- **Output**: $9.0 per 1M tokens
- **Cached Input**: $0 per 1M tokens (free)
- **Batch Input**: $0 per 1M tokens (free)

This structure indicates that using cached input or batch API calls can significantly reduce costs, as there are no additional fees associated with these features.

#### When to Use Cached Tokens
Cached tokens should be utilized whenever possible, as they are free. This is particularly beneficial for applications where the same input is used multiple times, such as in chatbots or virtual assistants. By leveraging cached tokens, developers can minimize their input costs.

#### Batch API Savings
Batching API calls can also lead to cost savings, as the input cost per token is reduced when making bulk requests. Although the exact savings are not specified, the fact that batch input is free suggests that Mistral AI encourages users to make batch requests to optimize their workflow and reduce costs.

#### Cost at Scale
To understand the cost implications of using Mistral Large 2 at scale, let's examine the provided cost examples:
- **1,000 calls (avg 500 tokens)**: $6.0
- **10,000 calls**: $60.0
- **100,000 calls**: $600.0

These examples illustrate a linear cost increase with the number of API calls. Assuming an average of 500 tokens per call, we can

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
Mistral Large 2, a premium model by Mistral AI, demonstrates strong performance across various benchmarks. This analysis will delve into the MMLU, HumanEval, and Arena ELO scores, providing insights into their implications for real-world applications.

#### Benchmark Scores
The model achieves the following benchmark scores:
* **MMLU (Massive Multitask Language Understanding)**: 84.0
* **HumanEval**: 92.0
* **LMSYS Arena ELO**: 1225
* **GSM8K**: 93.0

These scores indicate the model's capabilities in understanding and generating human-like text, as well as its performance in mathematical and logical reasoning tasks.

#### MMLU Score (84.0)
The MMLU score measures the model's ability to understand and generate text across a wide range of tasks and domains. A score of 84.0 suggests that Mistral Large 2 has a strong foundation in language understanding, making it suitable for applications that require text analysis, generation, and processing.

#### HumanEval Score (92.0)
The HumanEval score evaluates the model's ability to write correct and functional code in response to programming prompts. With a score of 92.0, Mistral Large 2 demonstrates exceptional coding capabilities, making it an excellent choice for coding, analysis, and function_calling tasks.

#### LMSYS Arena ELO Score (1225)
The LMSYS Arena ELO score measures the model's performance in a competitive environment, where it is pitted against other models in a series of tasks. An ELO score of 1225 indicates that Mistral

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. This comparison will focus on its pricing, performance, and capabilities against its top competitor, GPT-4o.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, while GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. GPT-4o offers a lower input price but a higher output price compared to Mistral Large 2.

#### Performance Comparison
Mistral Large 2 has the following benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

In contrast, the benchmark scores for GPT-4o are not provided. However, based on the available data, Mistral Large 2 demonstrates strong performance across various benchmarks.

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

On the other hand, it is not recommended for tasks that require:
- embeddings
- bulk_cheap
- real_time_sub_100ms
- vision_heavy

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100,000 calls: $600.0

#### Choosing Between Mistral Large 2 and GPT-4o
Consider the following factors

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open source model released on 2024-07-24. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts, making it suitable for applications such as coding, analysis, and multilingual support.

### Top 5 Best Use Cases for Mistral Large 2
Given its capabilities and limitations, here are the top 5 best use cases for Mistral Large 2:

1. **Coding and Development**: With its high scores in HumanEval (92.0) and GSM8K (93.0), Mistral Large 2 is well-suited for coding tasks, such as code completion, code review, and bug fixing. Its ability to understand and generate code in multiple languages makes it a valuable tool for developers.

2. **Complex Analysis**: The model's high context window of 131,072 tokens allows it to process and analyze large amounts of text, making it suitable for complex analysis tasks such as research paper summarization, technical document analysis, and data analysis.

3. **RAG (Retrieval-Augmented Generation) Tasks**: Mistral Large 2's ability to perform function calling and its support for JSON mode make it a good fit for RAG tasks, which involve retrieving information from external sources and generating text based on that information.

4. **Multilingual Support**: With its multilingual capabilities, Mistral Large 2 can be used for tasks such as language translation, language understanding, and text generation in multiple languages.

5. **Agent-Based Systems**: The model's ability to understand and respond to system prompts makes it suitable for use in agent-based systems, such as chatbots, virtual assistants, and other conversational AI systems.

### Code Integration Example with OpenRouter
To integrate Mistral Large 2 with OpenRouter, you can use the following code

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
