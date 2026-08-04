# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-04
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly excelling in coding, analysis, and function calling tasks. With its robust architecture, Mistral Large 2 boasts a context window of 131,072 tokens and can generate up to 4,096 tokens as output. This model is part of the premium tier, indicating its high-performance capabilities and reliability.

### Technical Strengths and Use Cases
The technical strengths of Mistral Large 2 are underscored by its impressive benchmark scores: MMLU at 84.0, HumanEval at 92.0, LMSYS Arena ELO at 1225, and GSM8K at 93.0. These scores highlight the model's proficiency in understanding and generating human-like text, making it suitable for tasks that require complex text analysis and generation. Its capabilities extend to text, vision, function calling, JSON mode, streaming, and system prompts, positioning it as a versatile tool for developers. However, it's noted that Mistral Large 2 is not ideal for embeddings, bulk cheap processing, real-time sub-100ms applications, or vision-heavy tasks.

### Pricing and Cost Considerations
The pricing model for Mistral Large 2 is structured around input and output tokens, with costs set at $3.0 per 1M tokens for input and $9.0 per 1M tokens for output. For developers considering the adoption of Mistral Large 2, cost examples provided indicate that 1,000 calls (averaging 500 tokens) would amount to $6.0, scaling up to $60.0 for 10,000 calls and $600.0 for 100,000 calls. In comparison to its top competitor, GPT-4o, which offers input at $2.

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $3.0 |
| Output | $9.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Mistral Large 2
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium model with a release date of 2024-07-24. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Large 2 is as follows:
- **Input**: $3.0 per 1M tokens
- **Output**: $9.0 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

#### Optimizing Costs with Cached Tokens and Batch API
Given that cached input and batch input are free, it's crucial to utilize these features whenever possible to minimize costs. 
- **Cached Tokens**: Since there's no cost associated with cached input, it's beneficial to use cached tokens for repeated input sequences or when the input data doesn't change frequently.
- **Batch API Savings**: Similarly, leveraging batch input can significantly reduce costs, especially for applications with a high volume of similar or identical input requests.

#### Cost at Scale
To understand the cost-effectiveness of Mistral Large 2 at different scales, let's examine the provided cost examples:
- **1,000 calls (avg 500 tokens)**: $6.0
- **10,000 calls**: $60.0
- **100,000 calls**: $600.0

These examples illustrate a linear cost increase with the number of API calls, indicating that the cost per call remains constant regardless of the scale.

#### Competitor Comparison
Comparing Mistral Large 2 with a top competitor, GPT-4o:
- **GPT-4o Input**: $2.5/1M input (cheaper than Mistral Large 2's $3.0/1M input)
- **GPT-

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
The Mistral Large 2 model, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. It is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens.

#### Benchmark Scores
The model's performance is measured by the following benchmark scores:
* **MMLU (Massive Multitask Language Understanding)**: 84.0, indicating the model's ability to understand and generate human-like text across a wide range of tasks and domains.
* **HumanEval**: 92.0, measuring the model's ability to write correct and functional code in response to programming prompts.
* **LMSYS Arena ELO**: 1225, representing the model's competitive performance in a large-scale language model benchmarking arena.
* **GSM8K**: 93.0, evaluating the model's math problem-solving abilities.

#### Real-World Implications
These benchmark scores suggest that the Mistral Large 2 model is:
* Suitable for tasks that require a deep understanding of human language, such as coding, analysis, and multilingual applications.
* Capable of generating high-quality code, making it a good fit for programming tasks.
* Competitive with other large language models, as indicated by its LMSYS Arena ELO score.

#### Limitations and Context
The model has a context window of 131,072 tokens, allowing it to process and understand long sequences of text. However, its maximum output is limited to 4,096 tokens. The knowledge cutoff date is 2024-07, which means the model may not have

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. This comparison will focus on its pricing, performance, and trade-offs against its top competitor, GPT-4o.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, while GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. This indicates that for input tokens, GPT-4o is cheaper by $0.5 per 1M tokens. However, for output tokens, Mistral Large 2 is cheaper by $1.0 per 1M tokens.

#### Performance Comparison
Mistral Large 2 has the following benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

While specific benchmark scores for GPT-4o are not provided, the performance of Mistral Large 2 suggests it is a high-performing model, particularly in coding and analysis tasks.

#### Capabilities and Use Cases
Mistral Large 2 is best suited for tasks such as:
- Coding
- Analysis
- RAG (Retrieval-Augmented Generation)
- Agents
- Multilingual tasks
- Function calling

It is not recommended for:
- Embeddings
- Bulk cheap operations
- Real-time operations under 100ms
- Vision-heavy tasks

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100,000 calls

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium model released on 2024-07-24. With its capabilities in text, vision, function calling, JSON mode, streaming, and system prompts, it is best suited for tasks such as coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual support, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Given its strengths and pricing model, here are the top 5 use cases for Mistral Large 2:

1. **Coding Assistance**: With high scores in HumanEval (92.0) and GSM8K (93.0), Mistral Large 2 is ideal for coding tasks, such as code completion, code review, and code generation. Its ability to understand and generate code in multiple languages makes it a valuable tool for developers.
2. **Complex Analysis**: The model's high context window (131,072 tokens) and ability to handle function calling make it suitable for complex analysis tasks, such as data analysis, research paper summarization, and technical writing.
3. **RAG and Agents**: Mistral Large 2's capabilities in RAG and agents enable it to retrieve and generate text based on external knowledge sources, making it useful for applications such as chatbots, virtual assistants, and content generation.
4. **Multilingual Support**: With its multilingual capabilities, Mistral Large 2 can be used for tasks such as language translation, language understanding, and text generation in multiple languages.
5. **Function Calling and API Integration**: The model's ability to call functions and integrate with APIs makes it suitable for tasks such as data processing, automation, and workflow management.

### Code Integration Example with OpenRouter
To integrate Mistral Large 2 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Mistral

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
