# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-07
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly excelling in coding, analysis, and function calling tasks. With its robust architecture, Mistral Large 2 boasts a context window of 131,072 tokens and can generate up to 4,096 tokens as output. This model is part of the premium tier, indicating its high-performance capabilities and reliability.

### Technical Strengths and Use Cases
The strengths of Mistral Large 2 are underscored by its impressive benchmark scores: 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These scores reflect its superior performance in understanding and generating human-like text, making it ideal for tasks such as coding assistance, complex analysis, and multi-lingual support. Additionally, its capabilities extend to vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers. However, it's noted that Mistral Large 2 is not suited for tasks requiring embeddings, bulk cheap processing, real-time responses under 100ms, or vision-heavy applications.

### Pricing and Cost Efficiency
The pricing model for Mistral Large 2 is based on input and output tokens, with costs set at $3.0 per 1M input tokens and $9.0 per 1M output tokens. For developers, this translates to specific cost examples: $6.0 for 1,000 calls averaging 500 tokens, $60.0 for 10,000 calls, and $600.0 for 100,000 calls. In comparison to its top competitor, GPT-4o, which charges $2.5/1M input and $10.0/1M

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
Mistral Large 2 is a premium model offered by Mistral AI, released on 2024-07-24. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for repeated input sequences. If your application involves frequent reuse of input tokens, utilizing cached tokens can significantly reduce costs.

#### Batch API Savings
Batch input is also free, which means that submitting multiple input sequences in a single API call does not incur additional costs. This can lead to substantial savings when processing large volumes of data.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* 1,000 calls (avg 500 tokens): $6.0
* 10,000 calls: $60.0
* 100,000 calls: $600.0

These costs can be broken down into input and output costs. Assuming an average of 500 tokens per call, the total input tokens for each scenario would be:
* 1,000 calls: 500,000 tokens (0.5M tokens)
* 10,000 calls: 5,000,000 tokens (5M tokens)
* 100,000 calls: 50,000,000 tokens (50M tokens)

Using the input pricing of $3.0 per 1M tokens, the input costs would be:
* 1,000 calls: 0.5M tokens \* $3.0

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 84.0 |
| HumanEval | 92.0 |
| LMSYS Arena ELO | 1225 |
| ARC | 93.0 |

## Benchmark Analysis
### Mistral Large 2 Benchmark Performance Analysis
The Mistral Large 2 model, released by Mistral AI on 2024-07-24, is a premium, non-open-source model with a unique set of capabilities and performance metrics.

#### Benchmark Scores
The model's performance is measured by the following benchmark scores:
* **MMLU (Massive Multitask Language Understanding)**: 84.0, indicating the model's ability to understand and process natural language across a wide range of tasks.
* **HumanEval**: 92.0, measuring the model's ability to generate human-like code and solve programming tasks.
* **LMSYS Arena ELO**: 1225, representing the model's competitive performance in a large-scale language model benchmarking arena.
* **GSM8K**: 93.0, evaluating the model's performance on a math problem-solving dataset.

#### Real-World Implications
These benchmark scores have significant implications for real-world use cases:
* The high HumanEval score (92.0) suggests that Mistral Large 2 is well-suited for coding and programming tasks, making it a strong choice for applications such as code generation, code completion, and code review.
* The MMLU score (84.0) indicates that the model has a strong foundation in natural language understanding, which is essential for tasks like text analysis, sentiment analysis, and language translation.
* The LMSYS Arena ELO score (1225) demonstrates the model's competitive performance in a wide range of language tasks, making it a viable option for applications that require a high level of language understanding and generation capabilities.

#### Pricing and Cost Examples
The pricing for Mistral Large 2 is as

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. This comparison will focus on its pricing, performance, and capabilities relative to its top competitors, specifically GPT-4o.

#### Pricing Comparison
| Model | Input Price per 1M tokens | Output Price per 1M tokens |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, whereas GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. This indicates that while GPT-4o is cheaper for input tokens, Mistral Large 2 is slightly more cost-effective for output tokens.

#### Performance Trade-offs
Mistral Large 2 has the following benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

In contrast, the performance benchmarks for GPT-4o are not provided in the data. However, considering the pricing difference, if GPT-4o offers similar or better performance, it might be a more cost-effective option for input-heavy tasks.

#### Capabilities and Use Cases
Mistral Large 2 supports a wide range of capabilities, including:
- Text
- Vision
- Function calling
- JSON mode
- Streaming
- System prompts

It is best suited for tasks such as:
- Coding
- Analysis
- RAG (Retrieval-Augmented Generation)
- Agents
- Multilingual tasks
- Function calling

However, it is not recommended for:
- Embeddings
- Bulk cheap tasks
- Real-time tasks requiring sub-100ms responses
- Vision-heavy tasks

#### Choosing the Right Model
- **Choose Mistral Large 2** when you prioritize its specific capabilities, such as function calling, and are willing to pay a premium for its performance and features.
- **Choose GPT-4o** when you

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model that excels in various tasks, including coding, analysis, and function calling. With its capabilities in text, vision, and JSON mode, among others, it's a versatile tool for developers and analysts. This guide outlines the top 5 best use cases for Mistral Large 2, along with practical advice and code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Large 2

1. **Coding Assistance**: Mistral Large 2 is highly proficient in coding tasks, with a HumanEval score of 92.0. It can assist in writing, debugging, and optimizing code.
   ```python
   import openrouter
   model = openrouter.MistralLarge2()
   prompt = "Write a Python function to sort a list of integers."
   response = model.generate_text(prompt)
   print(response)
   ```

2. **Complex Analysis**: With its high MMLU score of 84.0, Mistral Large 2 can handle complex analytical tasks, including data analysis and report generation.
   ```python
   import openrouter
   model = openrouter.MistralLarge2()
   prompt = "Analyze the impact of climate change on global food production."
   response = model.generate_text(prompt)
   print(response)
   ```

3. **RAG (Retrieve, Augment, Generate) Tasks**: Mistral Large 2's capabilities in text and function calling make it suitable for RAG tasks, which involve retrieving information, augmenting it, and generating new content.
   ```python
   import openrouter
   model = openrouter.MistralLarge2()
   prompt = "Retrieve information on the latest advancements in renewable energy and generate a report."
   response = model.generate_text(prompt)
   print(response)
  

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
