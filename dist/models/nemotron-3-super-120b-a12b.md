# NVIDIA: Nemotron 3 Super API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-11
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super is a powerful language model developed by Nvidia, released on January 1, 2024. This model, identified as `nvidia/nemotron-3-super-120b-a12b`, operates under a standard tier and is not open-source. With its robust architecture, the Nemotron 3 Super is designed to handle a wide range of tasks, including text generation, coding, analysis, and more. Its capabilities include text processing, function calling, JSON mode, streaming, and structured outputs, making it a versatile tool for developers.

### Technical Specifications and Pricing
Technically, the Nemotron 3 Super boasts a context window of 262,144 tokens and can generate up to 4,096 tokens as output. Its knowledge cutoff is December 2023, ensuring it has a broad and up-to-date understanding of the world. In terms of pricing, the model charges $0.1 per 1M tokens for input and $0.5 per 1M tokens for output. There are no charges for cached input or batch input. The model has been benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, demonstrating its capabilities. For example, using the model for 1,000 calls with an average of 500 tokens would cost $0.3, scaling to $3.0 for 10,000 calls and $30.0 for 100,000 calls.

### Use Cases and Competitors
The Nemotron 3 Super is best suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization. Its strengths lie in its ability to handle complex tasks with its large context window and output capabilities. While there are no direct competitors listed for the Nemotron 3 Super, its unique combination of capabilities and pricing makes it an attractive option for developers

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.1 |
| Output | $0.5 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### NVIDIA Nemotron 3 Super Pricing Analysis
#### Overview
The NVIDIA Nemotron 3 Super is a standard, non-open-source model released by Nvidia on January 1, 2024. This analysis will delve into the cost structure, usage scenarios, and scalability of this model.

#### Cost Structure
The pricing for the NVIDIA Nemotron 3 Super is as follows:
* Input: **$0.1 per 1M tokens**
* Output: **$0.5 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### Usage Scenarios
* **Cached Tokens**: Since cached input is free, it is highly recommended to use cached tokens whenever possible to minimize costs.
* **Batch API Savings**: Batch input is also free, making it an attractive option for large-scale API calls. However, the cost savings will depend on the output tokens, which are charged at **$0.5 per 1M tokens**.

#### Cost at Scale
The cost of using the NVIDIA Nemotron 3 Super at scale is as follows:
* **1,000 calls (avg 500 tokens)**: **$0.3**
* **10,000 calls**: **$3.0**
* **100,000 calls**: **$30.0**

These costs demonstrate a linear scaling of expenses with the number of API calls.

#### Context and Limits
The model has the following context and limits:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: December 2023

#### Capabilities and Best Use Cases
The NVIDIA Nemotron 3 Super supports the following capabilities:
* text
* function_calling
* json_mode
* streaming
* structured_outputs

It is best suited for:
* chat
* text_generation
* coding

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### NVIDIA Nemotron 3 Super Benchmark Analysis
#### Overview
The NVIDIA Nemotron 3 Super is a standard, non-open-source model released by Nvidia on 2024-01-01. This analysis will delve into its benchmark performance, focusing on the MMLU, HumanEval, and Arena ELO scores, and explain their implications for real-world use.

#### Benchmark Scores
* **MMLU (Massive Multitask Language Understanding) Score: 80.0**
The MMLU score measures a model's ability to perform a wide range of natural language processing tasks. A higher score indicates better performance. With a score of 80.0, the NVIDIA Nemotron 3 Super demonstrates strong language understanding capabilities.
* **HumanEval Score: None**
The HumanEval score evaluates a model's ability to generate code that passes human-written unit tests. Unfortunately, the HumanEval score is not available for this model, making it difficult to assess its coding capabilities.
* **LMSYS Arena ELO Score: 1200**
The LMSYS Arena ELO score measures a model's performance in a competitive environment, where it is pitted against other models. An ELO score of 1200 indicates that the NVIDIA Nemotron 3 Super is a strong competitor, but its ranking may vary depending on the specific tasks and opponents.

#### Real-World Implications
The benchmark scores suggest that the NVIDIA Nemotron 3 Super is well-suited for tasks that require strong language understanding, such as:
* Text generation
* Chat
* Analysis
* Summarization
However, the lack of a HumanEval score makes it difficult to recommend this model for coding tasks.

#### Pricing and Cost Examples
The

## Competitor Comparison
### NVIDIA Nemotron 3 Super Comparison
#### Introduction
The NVIDIA Nemotron 3 Super is a standard, non-open-source model released by Nvidia on January 1, 2024. With its unique capabilities and pricing structure, it's essential to understand its strengths and weaknesses compared to other models in the market.

#### Pricing Comparison
The Nemotron 3 Super has the following pricing structure:
* Input: $0.1 per 1M tokens
* Output: $0.5 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

Since there are no direct competitors listed, we will focus on the model's capabilities and provide guidance on when to choose it.

#### Performance Trade-offs
The Nemotron 3 Super has the following benchmarks:
* MMLU: 80.0
* LMSYS Arena ELO: 1200

It also has the following capabilities:
* Context Window: 262,144 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2023-12
* Capabilities: text, function_calling, json_mode, streaming, structured_outputs

#### When to Choose Nemotron 3 Super
The Nemotron 3 Super is best for:
* Chat
* Text generation
* Coding
* Analysis
* RAG pipelines
* Summarization

It is not explicitly stated what the model is not good for, but its capabilities and benchmarks suggest it may not be suitable for tasks that require:
* Extremely large context windows
* High-performance computing
* Open-source customization

#### Cost Examples
The cost of using the Nemotron 3 Super can be estimated as follows:
* 1,000 calls (avg 500 tokens): $0.3
* 10,000 calls: $3.0
* 100,000 calls: $30.0

These estimates are based on the input and output pricing structure, assuming an average token length.

#### Conclusion
The NVIDIA Nemotron 3 Super is a powerful model with a unique set of capabilities and a competitive pricing structure. While there are no direct competitors listed, its strengths and weaknesses make it an attractive choice for specific use cases, such as chat, text generation, and coding. By understanding its performance trade-offs and capabilities, developers can make informed decisions about when to choose the Nemotron 3 Super for their

## Best Use Cases
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super is a powerful language model released by Nvidia on 2024-01-01. With its impressive capabilities, including text generation, function calling, and structured outputs, it is an ideal choice for various applications. In this section, we will explore the top 5 best use cases for the NVIDIA Nemotron 3 Super, along with specific code integration examples using OpenRouter.

### Top 5 Use Cases for NVIDIA Nemotron 3 Super
#### 1. **Chat and Text Generation**
The NVIDIA Nemotron 3 Super excels in chat and text generation tasks, making it suitable for applications like conversational AI, content creation, and language translation. With its context window of 262,144 tokens, it can handle complex conversations and generate coherent text.

#### 2. **Coding and Analysis**
The model's capabilities in function calling and structured outputs make it an excellent choice for coding and analysis tasks. It can be used for code completion, code review, and debugging, as well as data analysis and visualization.

#### 3. **Summarization and Rag Pipelines**
The NVIDIA Nemotron 3 Super is well-suited for summarization tasks, such as summarizing long documents or articles. Its ability to handle rag pipelines also makes it a good choice for tasks that require processing and generating text based on external knowledge.

#### 4. **Analysis and Insights**
With its impressive MMLU benchmark score of 80.0, the NVIDIA Nemotron 3 Super can be used for analysis and insights tasks, such as sentiment analysis, entity recognition, and topic modeling.

#### 5. **Streaming and Real-time Applications**
The model's support for streaming and real-time applications makes it an excellent choice for use cases like live chat, real-time language translation, and streaming text generation.

### Code Integration Examples with OpenRouter
To integrate the NVIDIA Nemotron 3 Super with OpenRouter,

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
