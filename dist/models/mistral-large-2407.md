# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-10
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed for a wide range of applications, including coding, analysis, and multilingual tasks. With a context window of 131,072 tokens and a maximum output of 4,096 tokens, this model is capable of handling complex and lengthy inputs. Its knowledge cutoff is 2024-07, ensuring it has access to a vast amount of information up to that point. The model's architecture supports various capabilities such as text, vision, function calling, JSON mode, streaming, and system prompts.

### Technical Strengths and Use Cases
Mistral Large 2 demonstrates its strengths through several benchmarks: achieving 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These scores indicate the model's high performance in understanding and generating human-like text, as well as its coding capabilities. It is best utilized for tasks that require in-depth analysis, coding, and the ability to understand and respond to complex queries. However, it is not recommended for applications that require embeddings, bulk cheap processing, real-time responses under 100ms, or vision-heavy tasks. The pricing model is based on input and output tokens, with costs of $3.0 per 1M input tokens and $9.0 per 1M output tokens.

### Pricing and Competitiveness
The pricing of Mistral Large 2 is competitive, especially considering its premium features and performance. For example, 1,000 calls with an average of 500 tokens would cost $6.0, scaling up to $60.0 for 10,000 calls and $600.0 for 100,000 calls. In comparison to its top competitors, such as GPT-4o which charges

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
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. The pricing structure is based on input and output tokens, with specific considerations for cached and batch inputs.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
- **Input**: $3.0 per 1M tokens
- **Output**: $9.0 per 1M tokens
- **Cached Input**: No additional cost ($None per 1M tokens)
- **Batch Input**: No additional cost ($None per 1M tokens)

#### When to Use Cached Tokens
Cached tokens can be utilized without incurring additional costs. This is particularly beneficial for applications where the same input tokens are repeatedly used, as it eliminates the need for redundant calculations and reduces the overall cost.

#### Batch API Savings
Although the pricing does not specify a direct discount for batch inputs, the absence of additional costs for batch inputs implies that processing inputs in batches does not incur extra charges beyond the standard input cost. This can lead to significant savings when dealing with large volumes of data, as the cost per token remains constant regardless of the batch size.

#### Cost at Scale
To understand the cost implications at scale, let's examine the provided cost examples:
- **1,000 calls (avg 500 tokens)**: $6.0
- **10,000 calls**: $60.0
- **100,000 calls**: $600.0

These examples illustrate a linear cost scaling, where the cost increases directly with the number of API calls. For applications requiring a large number of calls, it's essential to factor in these costs to ensure scalability and budget alignment.

#### Comparison with Top Competitors
Mistral Large 2's pricing can be compared

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
* **GSM8K**: 93.0, evaluating the model's math problem-solving capabilities.

#### Real-World Implications
These benchmark scores have significant implications for real-world use cases:
* The high **HumanEval** score suggests that Mistral Large 2 is well-suited for coding tasks, such as code generation, code completion, and code review.
* The strong **MMLU** score indicates that the model can handle a wide range of natural language processing tasks, including text analysis, sentiment analysis, and text generation.
* The **LMSYS Arena ELO** score demonstrates the model's competitive performance in a large-scale benchmarking arena, making it a viable option for applications that require high-performance language understanding.

#### Capabilities and Limitations
Mistral Large 2 has the following capabilities

## Competitor Comparison
### Mistral Large 2 Comparison
#### Overview
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. This comparison will examine its pricing, performance, and capabilities against its top competitors, specifically GPT-4o.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, whereas GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. This indicates that GPT-4o is cheaper for input tokens but more expensive for output tokens.

#### Performance Comparison
Mistral Large 2 has the following benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

In contrast, the benchmark scores for GPT-4o are not provided. However, based on the available data, Mistral Large 2 demonstrates strong performance across various benchmarks.

#### Capabilities and Limits
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

However, it is not recommended for:
- embeddings
- bulk_cheap
- real_time_sub_100ms
- vision_heavy

Mistral Large 2 has a context window of 131,072 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2024-07.

#### Cost Examples
The estimated costs for using Mistral Large 2 are:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100,000 calls: $600.0

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. With its robust capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, it is best suited for tasks such as coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual support, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Given its capabilities and limitations, here are the top 5 best use cases for Mistral Large 2, along with practical advice and code integration examples using OpenRouter:

1. **Coding and Software Development**: Mistral Large 2 excels in coding tasks, thanks to its high HumanEval score of 92.0. It can be used for code completion, code review, and even generating entire functions based on specifications.
   ```python
   import openrouter
   model = openrouter.MistralLarge2()
   prompt = "Write a Python function to sort a list of integers."
   response = model.generate(prompt)
   print(response)
   ```

2. **Complex Analysis and Reasoning**: With a high MMLU score of 84.0, Mistral Large 2 is capable of complex analysis and reasoning tasks. It can be used to analyze large datasets, understand complex systems, and provide insights based on the data.
   ```python
   import openrouter
   model = openrouter.MistralLarge2()
   prompt = "Analyze the impact of climate change on global food production."
   response = model.generate(prompt)
   print(response)
   ```

3. **Multilingual Support**: Mistral Large 2 supports multiple languages, making it an excellent choice for applications that require multilingual support. It can be used for translation, language understanding, and generation tasks.
   ```python
   import open

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
