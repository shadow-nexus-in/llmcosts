# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-16
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly in coding, analysis, and function calling. This model boasts an impressive architecture that supports capabilities such as text, vision, function calling, JSON mode, streaming, and system prompts. With a context window of 131,072 tokens and a maximum output of 4,096 tokens, Mistral Large 2 is well-suited for tasks that require a deep understanding of context and the ability to generate lengthy, coherent responses.

### Technical Strengths and Use Cases
Mistral Large 2 demonstrates its strengths through various benchmarks, including an MMLU score of 84.0, HumanEval score of 92.0, LMSYS Arena ELO of 1225, and a GSM8K score of 93.0. These scores indicate the model's proficiency in handling complex tasks, coding challenges, and mathematical problems. Its capabilities make it an ideal choice for applications such as coding assistance, data analysis, and multilingual support. However, it's essential to note that Mistral Large 2 is not recommended for tasks that require embeddings, bulk processing at low costs, real-time responses under 100ms, or vision-heavy applications.

### Pricing and Cost Considerations
The pricing model for Mistral Large 2 is based on input and output tokens, with costs set at $3.0 per 1M input tokens and $9.0 per 1M output tokens. For example, 1,000 calls with an average of 500 tokens per call would cost $6.0, while 10,000 calls would amount to $60.0, and 100,000 calls would total $600.0. In comparison to its top competitor, GPT-4o, which charges $2.

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
Batch input is also free, which means that making batch API calls can help reduce costs. By batching multiple requests together, users can take advantage of the free batch input pricing.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* **1,000 API calls** (avg 500 tokens): **$6.0**
* **10,000 API calls**: **$60.0**
* **100,000 API calls**: **$600.0**

To estimate the cost of using Mistral Large 2, we can use the following formula:
Cost = (Number of Input Tokens / 1,000,000) \* $3.0 + (Number of Output Tokens / 1,000,000) \* $9.0

For example, if we make 1,000 API calls with an average of 500 input tokens and 200 output tokens, the total cost would be:
Cost = (500,000 /

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 84.0 |
| HumanEval | 92.0 |
| LMSYS Arena ELO | 1225 |
| ARC | 93.0 |

## Benchmark Analysis
### Mistral Large 2 Benchmark Analysis
#### Model Overview
The Mistral Large 2 model, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. It is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens.

#### Benchmark Performance
The model's performance is measured by the following benchmarks:
* **MMLU (Massive Multitask Language Understanding)**: 84.0 - This score indicates the model's ability to understand and process natural language across a wide range of tasks. A higher score suggests better language comprehension.
* **HumanEval**: 92.0 - This benchmark evaluates the model's ability to generate human-like code. A higher score implies better coding capabilities.
* **LMSYS Arena ELO**: 1225 - This score measures the model's performance in a competitive arena, where it is pitted against other models. A higher ELO score indicates better overall performance.
* **GSM8K**: 93.0 - This benchmark assesses the model's ability to solve math problems. A higher score suggests better math reasoning capabilities.

#### Real-World Implications
The benchmark scores suggest that the Mistral Large 2 model is well-suited for:
* **Coding tasks**: With a high HumanEval score, the model is capable of generating high-quality code.
* **Analysis tasks**: The model's high MMLU score indicates its ability to understand and process complex natural language.
* **Multilingual tasks**: The model's capabilities include multilingual support, making it suitable for tasks that require language translation or understanding.

However, the model may not be the best choice

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, a premium model provided by Mistral AI, is a powerful language model with a wide range of capabilities. In this comparison, we will evaluate Mistral Large 2 against its top competitors, focusing on price differences, performance trade-offs, and use cases.

#### Pricing Comparison
The pricing for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens

In comparison, GPT-4o, a top competitor, is priced at:
* Input: $2.5 per 1M tokens
* Output: $10.0 per 1M tokens

Mistral Large 2 is more expensive than GPT-4o in terms of input pricing, but slightly cheaper in terms of output pricing.

#### Performance Comparison
Mistral Large 2 has achieved impressive benchmark scores:
* MMLU: 84.0
* HumanEval: 92.0
* LMSYS Arena ELO: 1225
* GSM8K: 93.0

While the benchmark scores for GPT-4o are not provided, Mistral Large 2's scores indicate a high level of performance in various tasks.

#### Context and Limits
Mistral Large 2 has a context window of 131,072 tokens and a maximum output of 4,096 tokens. The knowledge cutoff is 2024-07.

#### Capabilities and Use Cases
Mistral Large 2 is capable of:
* Text processing
* Vision tasks
* Function calling
* JSON mode
* Streaming
* System prompts

It is best suited for tasks such as:
* Coding
* Analysis
* RAG (Retrieve, Augment, Generate)
* Agents
* Multilingual tasks
* Function calling

However, it is not recommended for:
* Embeddings
* Bulk cheap tasks
* Real-time tasks with latency under 100ms
* Vision-heavy tasks

#### Cost Examples
The estimated costs for using Mistral Large 2 are:
* 1,000 calls (avg 500 tokens): $6.0
* 10,000 calls: $60.0
* 100,000 calls: $600.0

#### Choosing the Right Model
When deciding between Mistral Large 

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. With its impressive capabilities in text, vision, function calling, JSON mode, streaming, and system prompts, it's best suited for tasks such as coding, analysis, RAG, agents, multilingual support, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Given its strengths and pricing model, here are the top 5 use cases for Mistral Large 2, along with specific code integration examples mentioning OpenRouter:

1. **Coding Assistance**: Mistral Large 2 excels in coding tasks, making it an ideal choice for developers looking for AI-powered coding assistance. 
    ```python
    import openrouter
    model = openrouter.load_model("mistralai/mistral-large-2407")
    # Use the model for coding tasks, such as code completion or code review
    coding_prompt = "Write a Python function to sort a list of integers."
    response = model(coding_prompt)
    print(response)
    ```
2. **Analysis and RAG (Retrieval-Augmented Generation)**: With its large context window of 131,072 tokens and the ability to handle system prompts, Mistral Large 2 is well-suited for complex analysis tasks and RAG applications.
    ```python
    import openrouter
    model = openrouter.load_model("mistralai/mistral-large-2407")
    # Use the model for analysis tasks, such as text summarization or question answering
    analysis_prompt = "Summarize the main points of the provided text."
    response = model(analysis_prompt)
    print(response)
    ```
3. **Multilingual Support**: Given its multilingual capabilities, Mistral Large 2 can be used for a variety of tasks that require support for multiple languages

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
