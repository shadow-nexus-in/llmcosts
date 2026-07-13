# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-13
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source language model designed to cater to a wide range of applications, including coding, analysis, and multilingual support. This model boasts a context window of 131,072 tokens and can generate up to 4,096 tokens as output. With a knowledge cutoff of 2024-07, Mistral Large 2 is positioned as a powerful tool for developers seeking advanced language processing capabilities.

### Architecture and Strengths
The architecture of Mistral Large 2 supports various capabilities such as text and vision processing, function calling, JSON mode, streaming, and system prompts. Its strengths are reflected in its benchmark scores: MMLU at 84.0, HumanEval at 92.0, LMSYS Arena ELO at 1225, and GSM8K at 93.0. These scores indicate the model's proficiency in understanding and generating human-like text, making it suitable for tasks that require complex language understanding and generation. The model's pricing is set at $3.0 per 1M input tokens and $9.0 per 1M output tokens, with no specified costs for cached input or batch input.

### Use Cases and Cost Considerations
Mistral Large 2 is best utilized for coding, analysis, and applications that require the model to understand and generate text based on system prompts or function calls. However, it is not recommended for tasks that require embeddings, bulk cheap processing, real-time responses under 100ms, or vision-heavy applications. For developers planning to use this model, the cost can be estimated based on the number of calls and tokens. For example, 1,000 calls with an average of 500 tokens would cost $6.0, while 10,000 calls would amount to $60.0, and 100,000 calls would

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
Batch input is also free, which means that batching API calls can help reduce the overall cost. By grouping multiple input sequences into a single API call, you can minimize the number of input tokens billed.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* 1,000 calls (avg 500 tokens): $6.0
* 10,000 calls: $60.0
* 100,000 calls: $600.0

To put this into perspective, let's calculate the cost per 1M tokens:
* Assuming an average of 500 tokens per call, 1,000 calls would correspond to approximately 0.5M tokens (1,000 calls \* 500 tokens/call = 500,000 tokens).
* Using the input and output pricing, the total cost would be: (0.5M tokens \* $3.0/1M tokens) + (0.5M tokens \* $9.0/1M tokens) = $1.5 + $4.5 = $6.0

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
The Mistral Large 2 model, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. It has a context window of 131,072 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2024-07.

#### Pricing
The pricing for Mistral Large 2 is as follows:
* Input: **$3.0 per 1M tokens**
* Output: **$9.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Benchmark Performance
The model's benchmark performance is as follows:
* **MMLU: 84.0** - The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to perform a wide range of natural language processing tasks. A higher MMLU score indicates better performance. With a score of 84.0, Mistral Large 2 demonstrates strong language understanding capabilities.
* **HumanEval: 92.0** - The HumanEval benchmark assesses a model's ability to generate code that is correct and functional. A higher HumanEval score indicates better coding abilities. With a score of 92.0, Mistral Large 2 shows excellent coding capabilities.
* **LMSYS Arena ELO: 1225** - The LMSYS Arena ELO benchmark evaluates a model's overall performance in a competitive setting. A higher ELO score indicates better performance. With a score of 1225, Mistral Large 2 demonstrates strong overall performance

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. This comparison will focus on its pricing, performance, and use cases against its top competitor, GPT-4o.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, whereas GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. This indicates that while GPT-4o is cheaper for input, Mistral Large 2 is cheaper for output.

#### Performance Comparison
Mistral Large 2 has the following benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

In contrast, the benchmark scores for GPT-4o are not provided. However, based on the available data, Mistral Large 2 demonstrates strong performance across various tasks.

#### Context and Limits
Mistral Large 2 has a context window of 131,072 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2024-07. These limits are not provided for GPT-4o, making a direct comparison challenging.

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

However, it is not recommended for:
- embeddings
- bulk_cheap
- real_time_sub_100ms
- vision_heavy

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model with a wide range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. This model excels in tasks such as coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual support, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Given its capabilities and pricing structure, here are the top 5 best use cases for Mistral Large 2:

1. **Advanced Coding Assistance**: With its high scores in HumanEval (92.0) and LMSYS Arena ELO (1225), Mistral Large 2 is well-suited for providing advanced coding assistance. It can help with code completion, code review, and even generating entire functions based on specifications.

    ```python
    import openrouter

    # Initialize Mistral Large 2 model
    model = openrouter.Model("mistralai/mistral-large-2407")

    # Define a coding prompt
    prompt = "Write a Python function to sort a list of integers."

    # Generate code using the model
    response = model.generate(prompt)
    print(response)
    ```

2. **Multilingual Support**: Given its multilingual capabilities, Mistral Large 2 can be used to develop applications that require support for multiple languages. This includes translation services, multilingual chatbots, and more.

    ```python
    import openrouter

    # Initialize Mistral Large 2 model
    model = openrouter.Model("mistralai/mistral-large-2407")

    # Define a translation prompt
    prompt = "Translate 'Hello, how are you?' from English to Spanish."

    # Generate translation using the model
    response = model.generate(prompt)
    print(response)


## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
