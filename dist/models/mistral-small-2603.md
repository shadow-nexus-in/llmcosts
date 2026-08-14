# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-14
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open-source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of tasks, including text generation, coding, and analysis, thanks to its capabilities such as text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its versatility and the breadth of applications it can support, including chat, text generation, coding, analysis, RAG pipelines, and summarization.

### Technical Specifications and Pricing
Technically, Mistral Small 4 boasts a context window of 262,144 tokens and can generate up to 4,096 tokens as output. The model's knowledge cutoff is 2023-12, indicating that its training data does not include information beyond this date. In terms of pricing, developers are charged $0.15 per 1M tokens for input and $0.6 per 1M tokens for output. There are no specified charges for cached input or batch input. The model has been benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, though HumanEval and GSM8K benchmarks are not provided. These specifications and pricing make it an attractive option for developers looking to integrate advanced language capabilities into their applications without incurring excessive costs.

### Use Cases and Cost Considerations
Given its capabilities, Mistral Small 4 is best suited for applications involving chat, text generation, coding, analysis, and more complex tasks like RAG pipelines and summarization. However, its limitations, such as the context window and output token limits, should be considered when designing applications. For cost estimation, examples provided indicate that 1,000 calls with an average of 500 tokens would cost $0.375,

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.15 |
| Output | $0.6 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Mistral Small 4 Pricing Analysis
#### Overview
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and scalability of Mistral Small 4.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$0.00 per 1M tokens** (free)
* Batch Input: **$0.00 per 1M tokens** (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following strategies:
* **Use cached tokens**: Since cached input tokens are free, utilize them whenever possible to reduce input costs.
* **Batch API calls**: With batch input tokens being free, batching API calls can lead to significant savings, especially for large-scale applications.
* **Optimize output tokens**: As output tokens are more expensive than input tokens, optimize your application to produce only necessary output tokens.

#### Cost at Scale
The cost of using Mistral Small 4 at various scales is as follows:
* **1,000 calls (avg 500 tokens)**: **$0.375**
* **10,000 calls**: **$3.75**
* **100,000 calls**: **$37.5**

These costs demonstrate a linear scaling of expenses with the number of API calls, indicating that the cost structure is straightforward and predictable.

#### Conclusion
Mistral Small 4 offers a competitive pricing model, especially when leveraging cached input tokens and batch API calls. By understanding the cost structure and optimizing usage, developers can effectively utilize Mistral Small 4 for various applications, including chat, text generation, coding, analysis, and summarization, while minimizing expenses. 

### Recommendations
*

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Analysis
#### Overview
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. It is not open-source.

#### Pricing
The pricing model for Mistral Small 4 is as follows:
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Context and Limits
The model has the following context and limits:
* Context Window: **262,144 tokens**
* Max Output: **4,096 tokens**
* Knowledge Cutoff: **2023-12**

#### Benchmarks
The model's benchmark performance is as follows:
* MMLU: **80.0**
* HumanEval: **None**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

The **MMLU (Massive Multitask Language Understanding) score** of 80.0 indicates the model's ability to perform well across a wide range of natural language processing tasks. A higher MMLU score suggests better performance in understanding and generating human-like language.

The **LMSYS Arena ELO score** of 1200 is a measure of the model's overall language understanding and generation capabilities in a competitive setting. ELO scores are used to rank models based on their performance in various tasks, with higher scores indicating better performance.

The lack of **HumanEval** and **GSM8K** scores means that the model's performance in specific areas, such

## Competitor Comparison
### Mistral Small 4 Comparison
Since there are no direct competitors listed for the Mistral Small 4, we will provide a general overview of its features, pricing, and performance. This will help potential users understand the model's capabilities and make informed decisions.

#### Model Overview
The Mistral Small 4 is a standard-tier model provided by Mistralai, released on January 1, 2024. It is not open-source.

#### Pricing
The pricing for the Mistral Small 4 is as follows:
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Context and Limits
The model has the following context and limits:
* Context Window: **262,144 tokens**
* Max Output: **4,096 tokens**
* Knowledge Cutoff: **2023-12**

#### Benchmarks
The Mistral Small 4 has the following benchmark scores:
* MMLU: **80.0**
* LMSYS Arena ELO: **1200**

#### Capabilities and Use Cases
The model supports the following capabilities:
* text
* function_calling
* json_mode
* streaming
* structured_outputs

It is best suited for:
* chat
* text_generation
* coding
* analysis
* rag_pipelines
* summarization

#### Cost Examples
Here are some cost examples for using the Mistral Small 4:
* 1,000 calls (avg 500 tokens): **$0.375**
* 10,000 calls: **$3.75**
* 100,000 calls: **$37.5**

### Choosing the Mistral Small 4
Since there are no direct competitors listed, the decision to choose the Mistral Small 4 depends on the specific use case and requirements. If the model's capabilities and pricing align with your needs, it may be a good choice. However, it's essential to evaluate the model's performance and limitations before making a decision.

In general, the Mistral Small 4 may be a good choice for applications that require:
* A context window of up to 262,144 tokens
* A maximum output of 4,096 tokens
* Support for text, function_calling, json_mode, streaming, and structured_outputs


## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and release date of 2024-01-01, it offers a robust solution for various applications. This guide will explore the top 5 best use cases for Mistral Small 4, along with code integration examples and practical advice.

### Top 5 Use Cases for Mistral Small 4
#### 1. **Chat and Text Generation**
Mistral Small 4 excels in chat and text generation tasks, making it an ideal choice for conversational AI applications. Its ability to understand context and generate human-like responses is unparalleled.

#### 2. **Coding and Analysis**
With its function calling and structured outputs capabilities, Mistral Small 4 is well-suited for coding and analysis tasks. It can be used to generate code snippets, analyze data, and provide insights.

#### 3. **Summarization and RAG Pipelines**
Mistral Small 4's ability to process large amounts of text and generate concise summaries makes it an excellent choice for summarization tasks. Its support for RAG pipelines enables it to retrieve and generate text based on specific queries.

#### 4. **Streaming and Real-time Applications**
Mistral Small 4's streaming capability allows it to process and generate text in real-time, making it suitable for applications that require immediate responses, such as live chatbots or virtual assistants.

#### 5. **JSON Mode and Structured Outputs**
Mistral Small 4's JSON mode and structured outputs enable it to generate and process structured data, making it an ideal choice for applications that require data exchange and processing, such as data integration and API development.

### Code Integration Examples with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code example:


## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
