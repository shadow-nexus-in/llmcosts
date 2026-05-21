# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-21
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of natural language processing tasks with its robust capabilities, including text generation, function calling, JSON mode, streaming, and structured outputs. Its strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens.

### Primary Use Cases and Strengths
Mistral Small 4 is best utilized for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization. Its capabilities make it an ideal choice for developers looking to integrate advanced language processing into their applications. With a context window of 262,144 tokens and a knowledge cutoff of 2023-12, Mistral Small 4 is well-equipped to handle complex and nuanced language tasks. The model's performance is further underscored by its benchmarks, including an MMLU score of 80.0 and an LMSYS Arena ELO score of 1200, demonstrating its proficiency in understanding and generating human-like language.

### Pricing and Cost Considerations
The pricing for Mistral Small 4 is structured around input and output tokens, with costs of $0.15 per 1M input tokens and $0.6 per 1M output tokens. There are no additional costs for cached input or batch input. To illustrate the cost implications, 1,000 calls with an average of 500 tokens would cost $0.375, while 10,000 calls would amount to $3.75, and 100,000 calls would total $37.5. Given its capabilities and pricing, Mistral Small 4 presents a compelling option for developers seeking a powerful language model for their applications, particularly in

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.15 |
| Output | $0.6 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Mistral: Mistral Small 4
#### Overview
Mistral: Mistral Small 4 is a standard, non-open-source model provided by Mistralai, released on January 1, 2024. This analysis will delve into the cost structure, optimal usage scenarios, and scalability of this model.

#### Cost Structure
The pricing for Mistral: Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens (free)
* Batch Input: $None per 1M tokens (free)

This indicates that the primary cost drivers are input and output token counts. Cached and batch inputs are not charged, suggesting that optimizing for these can significantly reduce costs.

#### When to Use Cached Tokens
Given that cached input tokens are free, it is highly beneficial to utilize cached tokens whenever possible. This can be particularly effective in scenarios where the same input data is processed multiple times, such as in chat applications or text generation tasks where user input may be repetitive.

#### Batch API Savings
Similar to cached inputs, batch inputs are also free. This implies that batching API calls can lead to substantial cost savings, especially for applications that require processing large volumes of data in parallel. By grouping multiple inputs into a single batch, the cost per input token can be significantly reduced.

#### Cost at Scale
To understand the cost implications of using Mistral: Mistral Small 4 at scale, let's examine the provided cost examples:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

These examples illustrate a linear cost scaling, where the cost increases directly with the number of API calls. This suggests that the cost structure is straightforward and easy to predict, allowing for

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Benchmark Performance Analysis
#### Model Overview
The Mistral Small 4 model, provided by Mistralai, is a standard-tier model released on 2024-01-01. It is not open source.

#### Pricing
The pricing for Mistral Small 4 is as follows:
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
The benchmark performance of Mistral Small 4 is as follows:
* MMLU: **80.0**
* HumanEval: **None**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

The MMLU score of 80.0 indicates the model's ability to understand and process natural language. A higher MMLU score generally corresponds to better language understanding capabilities.

The LMSYS Arena ELO score of 1200 is a measure of the model's performance in a competitive environment. ELO scores are used to rank models based on their performance, with higher scores indicating better performance.

The lack of HumanEval and GSM8K scores means that the model's performance on these specific benchmarks is not available.

#### Real-World Use
In real-world use, the Mistral Small 4 model is suitable for applications such as:
* Chat


## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral Small 4 model, we will provide a general overview of its features, pricing, and performance. This will serve as a baseline for comparison with other models in the future.

#### Model Overview
The Mistral Small 4 model is a standard, non-open-source model provided by Mistralai, released on January 1, 2024. Its key features include:

* **Pricing**:
	+ Input: $0.15 per 1M tokens
	+ Output: $0.6 per 1M tokens
* **Context and Limits**:
	+ Context Window: 262,144 tokens
	+ Max Output: 4,096 tokens
	+ Knowledge Cutoff: December 2023
* **Benchmarks**:
	+ MMLU: 80.0
	+ LMSYS Arena ELO: 1200
* **Capabilities**:
	+ Text
	+ Function calling
	+ JSON mode
	+ Streaming
	+ Structured outputs
* **Best For**:
	+ Chat
	+ Text generation
	+ Coding
	+ Analysis
	+ RAG pipelines
	+ Summarization

#### Cost Examples
To illustrate the cost of using the Mistral Small 4 model, consider the following examples:

* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

#### Choosing the Right Model
When selecting a model, consider the following factors:

* **Performance requirements**: If you need a model with high performance on specific benchmarks like MMLU or LMSYS Arena ELO, the Mistral Small 4 model may be a good choice.
* **Budget constraints**: If you have a limited budget, you may want to consider models with lower pricing per token.
* **Specific use cases**: If you need a model for chat, text generation, coding, or other specific tasks, the Mistral Small 4 model's capabilities may make it a good fit.

As more competitor models are listed, we can provide a more detailed comparison of the Mistral Small 4 model with its top competitors, including price differences, performance trade-offs, and recommendations for when to choose each model.

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and proprietary license, it offers a unique set of features for various applications.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and max output of 4,096 tokens, Mistral Small 4 is well-suited for chat and text generation applications. Its ability to understand and respond to user input makes it an ideal choice for conversational AI.
2. **Coding and Analysis**: Mistral Small 4's function calling and structured outputs capabilities make it a great tool for coding and analysis tasks. Its ability to generate code and provide detailed analysis makes it a valuable asset for developers and data analysts.
3. **Summarization and RAG Pipelines**: Mistral Small 4's text generation and structured outputs capabilities make it an excellent choice for summarization and RAG (Retrieve, Augment, Generate) pipelines. Its ability to condense large amounts of text into concise summaries makes it a valuable tool for information retrieval and processing.
4. **Streaming and Real-time Applications**: Mistral Small 4's streaming capability makes it well-suited for real-time applications, such as live chat, sentiment analysis, and event detection. Its ability to process and respond to user input in real-time makes it an ideal choice for applications that require immediate feedback.
5. **JSON Mode and Structured Outputs**: Mistral Small 4's JSON mode and structured outputs capabilities make it a great tool for applications that require structured data, such as data integration, data processing, and data visualization. Its ability to generate structured outputs makes it

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
