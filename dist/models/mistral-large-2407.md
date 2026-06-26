# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-26
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Technical Overview of Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly in coding, analysis, and function calling. Architecturally, it boasts a context window of 131,072 tokens and can generate up to 4,096 tokens as output. This model is part of the Mistral AI suite, specifically `mistralai/mistral-large-2407`, indicating its positioning within the Mistral AI ecosystem.

### Main Strengths and Use Cases
The main strengths of Mistral Large 2 lie in its versatility and performance. With capabilities including text, vision, function calling, JSON mode, streaming, and system prompts, it is best utilized for tasks such as coding, analysis, retrieval-augmented generation (RAG), agents, multilingual applications, and function calling. Its benchmark scores, including an MMLU of 84.0, HumanEval of 92.0, LMSYS Arena ELO of 1225, and GSM8K of 93.0, underscore its robust performance across various evaluation metrics. However, it is not recommended for applications requiring embeddings, bulk cheap processing, real-time sub-100ms responses, or vision-heavy tasks.

### Pricing and Cost Considerations
Pricing for Mistral Large 2 is structured around input and output tokens, with costs of $3.0 per 1M input tokens and $9.0 per 1M output tokens. There are no specified costs for cached input or batch input. For developers, estimating costs can be straightforward: for example, 1,000 calls averaging 500 tokens each would cost $6.0, scaling to $60.0 for 10,000 calls and $600.0 for 100,000 calls. In comparison to competitors like GPT-4o, which

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
Mistral Large 2, a premium model by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. The pricing structure is based on input and output tokens.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
* Input: **$3.0 per 1M tokens**
* Output: **$9.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs when the same input is used multiple times. Since cached input is free, it is recommended to use cached tokens whenever possible to minimize input costs.

#### Batch API Savings
Batching API calls can help reduce costs by minimizing the number of input tokens required. With batch input being free, batching can lead to significant savings, especially for large-scale applications.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: **$6.0**
* **10,000 calls**: **$60.0**
* **100,000 calls**: **$600.0**

These costs are based on the average number of tokens per call and can vary depending on the actual usage.

#### Comparison with Top Competitors
Mistral Large 2's pricing is competitive with top competitors like GPT-4o, which charges **$2.5/1M input** and **$10.0/1M output**. However, the free cached input and batch input options make Mistral Large 2 a more attractive option for applications with repetitive input or large-scale batch processing

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
* **MMLU (Massive Multitask Language Understanding)**: 84.0, indicating the model's ability to understand and generate human-like text across a wide range of tasks and topics.
* **HumanEval**: 92.0, measuring the model's ability to write correct and functional code in response to programming prompts.
* **LMSYS Arena ELO**: 1225, representing the model's competitive performance in a large-scale language model benchmarking arena.
* **GSM8K**: 93.0, evaluating the model's math problem-solving abilities.

#### Real-World Implications
These benchmark scores suggest that the Mistral Large 2 model is:
* Suitable for coding and analysis tasks, with a high HumanEval score indicating strong programming abilities.
* Effective in multilingual and function-calling tasks, given its high MMLU and GSM8K scores.
* Not ideal for embeddings, bulk cheap processing, or real-time applications requiring sub-100ms response times.
* Competitive with other premium models, such as GPT-4o, but with a higher output price point.

#### Cost Analysis
The pricing model is based on input and output tokens, with examples of costs for different numbers of calls:
* 1,000 calls (avg 500 tokens):

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, a premium model by Mistral AI, offers a robust set of capabilities including text, vision, function calling, and more. Released on 2024-07-24, it stands out with its performance and feature set. This comparison will delve into the pricing, performance, and use cases of Mistral Large 2 against its top competitor, GPT-4o.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, whereas GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. While GPT-4o offers a slightly lower input price, Mistral Large 2's output price is more competitive.

#### Performance Comparison
Mistral Large 2 boasts impressive benchmarks:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

In contrast, specific benchmark scores for GPT-4o are not provided in the data. However, considering the general performance of models in the same tier, Mistral Large 2's scores indicate high capability in coding, analysis, and other areas it's best suited for.

#### Capabilities and Use Cases
Mistral Large 2 is best for:
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
For Mistral Large 2, the estimated costs are:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100,000 calls: $600.0

These costs can help

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model that excels in various tasks, including coding, analysis, and function calling. With its impressive benchmarks, such as an MMLU score of 84.0 and a HumanEval score of 92.0, this model is a top choice for many applications. Here, we will explore the top 5 best use cases for Mistral Large 2, along with code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Large 2
#### 1. **Coding Assistance**
Mistral Large 2 is well-suited for coding tasks, thanks to its high HumanEval score. You can use it to generate code snippets, complete partial code, or even debug existing code.

```python
import openrouter

# Initialize the model
model = openrouter.MistralLarge2()

# Define a coding prompt
prompt = "Write a Python function to calculate the area of a circle."

# Generate code
code = model.generate_code(prompt)

print(code)
```

#### 2. **Analysis and Summarization**
With its high MMLU score, Mistral Large 2 can effectively analyze and summarize long pieces of text. This makes it ideal for applications like text summarization, sentiment analysis, or content generation.

```python
import openrouter

# Initialize the model
model = openrouter.MistralLarge2()

# Define an analysis prompt
prompt = "Summarize the following text: [insert long text here]"

# Generate summary
summary = model.generate_text(prompt)

print(summary)
```

#### 3. **RAG (Retrieval-Augmented Generation)**
Mistral Large 2 supports RAG, which enables it to retrieve relevant information from a knowledge base and generate text based on that information.

```

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
