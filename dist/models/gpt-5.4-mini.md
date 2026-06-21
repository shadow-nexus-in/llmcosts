# OpenAI: GPT-5.4 Mini API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-21
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to OpenAI: GPT-5.4 Mini
The OpenAI: GPT-5.4 Mini model, released on 2024-01-01, is a standard tier language model provided by OpenAI. This model is not open source. From an architectural standpoint, while specific details about its architecture are not provided, it is part of the GPT series, which typically involves transformer-based architectures designed for natural language processing tasks. The GPT-5.4 Mini is positioned as a versatile tool for developers, capable of handling a wide range of tasks including text generation, coding, analysis, and more.

### Strengths and Use Cases
The main strengths of the OpenAI: GPT-5.4 Mini include its broad capabilities such as text, function calling, JSON mode, streaming, and structured outputs. It is best suited for applications like chat, text generation, coding, analysis, RAG pipelines, and summarization. With a context window of 400,000 tokens and a maximum output of 128,000 tokens, this model can handle complex and lengthy inputs and outputs. Its performance is underscored by benchmarks such as an MMLU score of 94.0 and an LMSYS Arena ELO of 1350. However, its limitations, such as a knowledge cutoff of 2023-12, should be considered when choosing this model for specific tasks.

### Pricing and Cost Considerations
The pricing for the OpenAI: GPT-5.4 Mini is structured around input and output tokens. Developers are charged $0.75 per 1M input tokens and $4.5 per 1M output tokens. There are no specified costs for cached input or batch input. To give developers a clearer picture, cost examples are provided: 1,000 calls averaging 500 tokens would cost $2.625, scaling up to $26.25 for 10,000 calls, and $262.5 for

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.75 |
| Output | $4.5 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### OpenAI: GPT-5.4 Mini Pricing Analysis
#### Overview
The OpenAI: GPT-5.4 Mini model is a standard, non-open source model released on January 1, 2024. This analysis will break down the cost structure, provide guidance on when to use cached tokens, discuss batch API savings, and examine the cost at scale for 1,000, 10,000, and 100,000 API calls.

#### Cost Structure
The pricing for OpenAI: GPT-5.4 Mini is as follows:
* Input: **$0.75 per 1M tokens**
* Output: **$4.5 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### Using Cached Tokens
Cached input tokens are free, which means that if you can utilize cached tokens, you can significantly reduce your costs. This is particularly useful for applications where the input is repetitive or where the same input is used multiple times.

#### Batch API Savings
Batch input is also free, which means that batching your API calls can help reduce your costs. However, the actual cost savings will depend on the output tokens, as the output price is **$4.5 per 1M tokens**.

#### Cost at Scale
The cost examples provided are as follows:
* 1,000 calls (avg 500 tokens): **$2.625**
* 10,000 calls: **$26.25**
* 100,000 calls: **$262.5**

To put these costs into perspective, let's calculate the cost per call:
* 1,000 calls: **$2.625 / 1,000 = $0.002625 per call**
* 10,000 calls: **$26.25 / 10,000 = $0.002625

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 94.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1350 |
| ARC | None |

## Benchmark Analysis
### Analysis of OpenAI: GPT-5.4 Mini Benchmark Performance
#### Introduction
The OpenAI: GPT-5.4 Mini model, released on 2024-01-01, is a standard-tier model provided by OpenAI. This analysis will delve into the model's benchmark performance, focusing on the MMLU, HumanEval, and Arena ELO scores, and their implications for real-world use.

#### Benchmark Scores
The model's benchmark scores are as follows:
* **MMLU (Massive Multitask Language Understanding)**: 94.0
* **HumanEval**: None
* **LMSYS Arena ELO**: 1350
* **GSM8K**: None

The MMLU score of 94.0 indicates the model's ability to understand and generate human-like text across a wide range of tasks and topics. A higher MMLU score suggests better performance in tasks that require a deep understanding of language.

The absence of HumanEval and GSM8K scores limits the analysis of the model's performance in specific areas, such as coding and mathematical problem-solving.

The LMSYS Arena ELO score of 1350 provides a measure of the model's overall language understanding and generation capabilities in a competitive setting. A higher ELO score indicates better performance compared to other models.

#### Real-World Implications
The benchmark scores suggest that the OpenAI: GPT-5.4 Mini model is well-suited for tasks that require a strong understanding of language, such as:
* Text generation
* Chat
* Analysis
* Summarization
* Coding

However, the lack of HumanEval and GSM8K scores means that the model's performance in

## Competitor Comparison
### Comparison of OpenAI: GPT-5.4 Mini with Top Competitors
Since there are no direct competitors listed for the OpenAI: GPT-5.4 Mini model, we will provide a general overview of the model's features, pricing, and performance. This will help users understand the model's capabilities and make informed decisions about its use.

#### Model Overview
The OpenAI: GPT-5.4 Mini model is a standard, non-open-source model released by OpenAI on January 1, 2024. It has a context window of 400,000 tokens, a maximum output of 128,000 tokens, and a knowledge cutoff of December 2023.

#### Pricing
The pricing for the OpenAI: GPT-5.4 Mini model is as follows:
* Input: $0.75 per 1M tokens
* Output: $4.5 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Performance Trade-offs
The model has the following benchmark scores:
* MMLU: 94.0
* LMSYS Arena ELO: 1350

The model is capable of performing the following tasks:
* Text generation
* Function calling
* JSON mode
* Streaming
* Structured outputs

It is best suited for the following use cases:
* Chat
* Text generation
* Coding
* Analysis
* RAG pipelines
* Summarization

#### Cost Examples
The estimated costs for using the OpenAI: GPT-5.4 Mini model are:
* 1,000 calls (avg 500 tokens): $2.625
* 10,000 calls: $26.25
* 100,000 calls: $262.5

#### Choosing the Right Model
Since there are no direct competitors listed, the decision to use the OpenAI: GPT-5.4 Mini model will depend on the specific requirements of the project. Users should consider the model's capabilities, pricing, and performance trade-offs when deciding whether to use this model.

In general, the OpenAI: GPT-5.4 Mini model is a good choice for projects that require:
* High-quality text generation
* Function calling capabilities
* Support for JSON mode and structured outputs
* Streaming capabilities

However, users should also consider the model's limitations, such as its

## Best Use Cases
### Introduction to OpenAI: GPT-5.4 Mini
The OpenAI: GPT-5.4 Mini model, released on 2024-01-01, is a standard, non-open-source model provided by Openai. It offers a range of capabilities, including text generation, function calling, JSON mode, streaming, and structured outputs, making it suitable for various applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization.

### Top 5 Best Use Cases for OpenAI: GPT-5.4 Mini
Based on its capabilities and benchmarks, here are the top 5 best use cases for OpenAI: GPT-5.4 Mini:

1. **Chat and Text Generation**: With its high MMLU score of 94.0 and LMSYS Arena ELO of 1350, OpenAI: GPT-5.4 Mini is well-suited for generating human-like text and engaging in conversations.
2. **Coding and Analysis**: The model's ability to perform function calling and structured outputs makes it a good fit for coding tasks, such as generating code snippets or analyzing codebases.
3. **Summarization and RAG Pipelines**: OpenAI: GPT-5.4 Mini's capabilities in text generation and analysis make it a good choice for summarization tasks and RAG (Retrieve, Augment, Generate) pipelines.
4. **Content Generation**: The model's text generation capabilities can be leveraged to generate high-quality content, such as articles, blog posts, or social media posts.
5. **Conversational AI**: With its high benchmarks and capabilities in text generation and conversation, OpenAI: GPT-5.4 Mini can be used to build conversational AI models, such as chatbots or virtual assistants.

### Code Integration Examples with OpenRouter
To integrate OpenAI: GPT-5.4 Mini with OpenRouter, you can use the following

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
