# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-05
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model that boasts an impressive array of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. With a context window of 131,072 tokens and a maximum output of 4,096 tokens, this model is well-suited for complex tasks that require a deep understanding of context and the ability to generate lengthy, coherent responses. The knowledge cutoff for Mistral Large 2 is 2024-07, ensuring that its training data is current up to that point.

### Technical Strengths and Use Cases
The architecture of Mistral Large 2 is designed to excel in areas such as coding, analysis, retrieval-augmented generation (RAG), agents, multilingual tasks, and function calling. Its strengths are reflected in its benchmark scores, which include an MMLU score of 84.0, a HumanEval score of 92.0, an LMSYS Arena ELO of 1225, and a GSM8K score of 93.0. These scores indicate that Mistral Large 2 is a highly capable model that can perform a wide range of tasks with a high degree of accuracy. However, it is not well-suited for tasks that require embeddings, bulk processing at a low cost, real-time responses under 100ms, or vision-heavy workloads.

### Pricing and Cost Considerations
The pricing for Mistral Large 2 is $3.0 per 1M input tokens and $9.0 per 1M output tokens. There are no additional costs for cached input or batch input. To give developers a better understanding of the costs involved, consider the following examples: 1,000 calls with an average of 500 tokens per call would cost $6.0, while 10,000 calls would cost

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
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. The pricing structure is based on input and output tokens.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
* Input: **$3.0 per 1M tokens**
* Output: **$9.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs when the same input is used multiple times. Since cached input is free, it is recommended to use cached tokens whenever possible to minimize costs.

#### Batch API Savings
Batching API calls can also help reduce costs. Although the pricing data does not provide a specific discount for batch API calls, the fact that batch input is free suggests that batching can help reduce the overall cost per call.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* 1,000 calls (avg 500 tokens): **$6.0**
* 10,000 calls: **$60.0**
* 100,000 calls: **$600.0**

To put these costs into perspective, let's calculate the cost per call:
* 1,000 calls: **$6.0 / 1,000 = $0.006 per call**
* 10,000 calls: **$60.0 / 10,000 = $0.006 per call**
* 100,000 calls: **$600.0 / 100,000 = $0.006 per call**

As we can see,

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
Mistral Large 2, a premium model provided by Mistral AI, boasts an impressive set of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. This analysis will delve into the benchmark performance of Mistral Large 2, focusing on the MMLU, HumanEval, and Arena ELO scores, and explore their implications for real-world use.

#### Benchmark Scores
The model's performance is measured across several benchmarks:
* **MMLU (Massive Multitask Language Understanding)**: 84.0
* **HumanEval**: 92.0
* **LMSYS Arena ELO**: 1225
* **GSM8K**: 93.0

These scores indicate the model's proficiency in various areas:
* **MMLU**: Measures the model's ability to understand and generate human-like text across a wide range of tasks. A score of 84.0 suggests strong language understanding capabilities.
* **HumanEval**: Evaluates the model's ability to write correct and functional code. A score of 92.0 indicates excellent coding skills.
* **LMSYS Arena ELO**: Assesses the model's performance in a competitive environment, with a higher score indicating better performance. An ELO score of 1225 suggests that Mistral Large 2 is a strong competitor.

#### Real-World Implications
The benchmark scores have significant implications for real-world use:
* **Coding and Analysis**: With high HumanEval and MMLU scores, Mistral Large 2 is well-suited for coding, analysis, and other tasks that require strong language understanding and generation capabilities.
*

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2 is a premium, non-open-source model provided by Mistral AI, released on 2024-07-24. It offers a range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. This comparison will focus on its pricing, performance, and trade-offs against its top competitor, GPT-4o.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, whereas GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. This indicates that GPT-4o is cheaper for input tokens but more expensive for output tokens.

#### Performance Comparison
| Model | MMLU | HumanEval | LMSYS Arena ELO | GSM8K |
| --- | --- | --- | --- | --- |
| Mistral Large 2 | 84.0 | 92.0 | 1225 | 93.0 |
| GPT-4o | Not provided | Not provided | Not provided | Not provided |

Since the performance benchmarks for GPT-4o are not provided, a direct comparison is not possible. However, Mistral Large 2 has demonstrated strong performance across various benchmarks, including MMLU, HumanEval, LMSYS Arena ELO, and GSM8K.

#### Context and Limits Comparison
| Model | Context Window | Max Output |
| --- | --- | --- |
| Mistral Large 2 | 131,072 tokens | 4,096 tokens |
| GPT-4o | Not provided | Not provided |

Mistral Large 2 has a context window of 131,072 tokens and a maximum output of 4,096 tokens. Without the corresponding information for GPT-4o, it is difficult to compare these aspects directly.

#### Capabilities and Use Cases
Mistral Large 2 is best suited for:


## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium model released on 2024-07-24. With its capabilities in text, vision, function calling, JSON mode, streaming, and system prompts, it is best suited for tasks such as coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual support, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Given its strengths, here are the top 5 use cases for Mistral Large 2, along with specific code integration examples mentioning OpenRouter:

1. **Coding and Software Development**: Mistral Large 2 excels in coding tasks, making it an ideal choice for software development, code review, and code generation.
   ```python
   import openrouter
   model = openrouter.load_model("mistralai/mistral-large-2407")
   prompt = "Write a Python function to sort a list of integers."
   response = model.generate_text(prompt)
   print(response)
   ```
2. **Data Analysis and Insights**: With its strong analytical capabilities, Mistral Large 2 can be used for data analysis, providing insights and summaries of complex data sets.
   ```python
   import pandas as pd
   import openrouter
   model = openrouter.load_model("mistralai/mistral-large-2407")
   data = pd.read_csv("data.csv")
   prompt = "Analyze the data and provide key insights."
   response = model.generate_text(prompt, data=data)
   print(response)
   ```
3. **Multilingual Support**: Mistral Large 2 supports multiple languages, making it an excellent choice for applications requiring language translation, localization, or multilingual customer support.
   ```python
   import openrouter
   model = openrouter.load_model("mistralai/mistral-large-2407")
   prompt = "Translate

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
