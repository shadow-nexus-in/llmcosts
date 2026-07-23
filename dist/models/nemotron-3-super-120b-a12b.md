# NVIDIA: Nemotron 3 Super API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-23
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super is a powerful language model developed by Nvidia, released on January 1, 2024. This model, identified as `nvidia/nemotron-3-super-120b-a12b`, operates on a standard tier and is not open-source. With its robust architecture, the Nemotron 3 Super is designed to handle a wide range of tasks, including text generation, coding, analysis, and more. Its capabilities extend to function calling, JSON mode, streaming, and structured outputs, making it a versatile tool for developers.

### Technical Specifications and Strengths
Technically, the Nemotron 3 Super boasts a context window of 262,144 tokens and can generate up to 4,096 tokens as output. Its knowledge cutoff is December 2023, ensuring it has a broad and up-to-date understanding of the world. The model's pricing structure includes charges of $0.1 per 1M tokens for input and $0.5 per 1M tokens for output. Benchmarks show an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating strong performance in various evaluations. The Nemotron 3 Super's main strengths lie in its ability to handle complex tasks such as chat, text generation, coding, and summarization, thanks to its advanced capabilities like text, function calling, and structured outputs.

### Use Cases and Cost Considerations
The NVIDIA Nemotron 3 Super is best utilized for applications requiring sophisticated text processing, such as chatbots, content generation, coding assistance, and data analysis. However, its pricing should be considered in the context of the application. For example, 1,000 calls with an average of 500 tokens would cost $0.3, while 100,000 calls would amount to $30.0. Understanding the cost structure and the model's capabilities is crucial for optimizing

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
* **Input**: $0.1 per 1M tokens
* **Output**: $0.5 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

This structure indicates that input and output tokens are the primary cost drivers. However, utilizing cached input and batch input can help reduce costs.

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for reducing costs. If your application involves repeated input sequences or has a high degree of input similarity, leveraging cached tokens can significantly lower your expenses.

#### Batch API Savings
Similar to cached input, batch input is also free. When possible, batching API calls together can help minimize costs. This approach is particularly beneficial for applications that require processing large volumes of data in parallel.

#### Cost at Scale
To understand the cost implications of using the NVIDIA Nemotron 3 Super at scale, let's examine the provided cost examples:
* **1,000 calls (avg 500 tokens)**: $0.3
* **10,000 calls**: $3.0
* **100,000 calls**: $30.0

These examples illustrate a linear cost increase with the number of API calls. This linearity suggests that the cost per call remains relatively consistent, regardless of the scale.

### Cost Estimation
Based on the provided pricing, we can estimate the cost for a given number of tokens. Assuming an average input size of 500 tokens per call (as in the 1,000 calls example

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### NVIDIA Nemotron 3 Super Analysis
#### Overview
The NVIDIA Nemotron 3 Super is a standard, non-open-source model released by Nvidia on January 1, 2024. This model is designed for various tasks, including chat, text generation, coding, analysis, and summarization.

#### Pricing
The pricing for the Nemotron 3 Super is as follows:
* Input: **$0.1 per 1M tokens**
* Output: **$0.5 per 1M tokens**
* Cached Input: **$None per 1M tokens** (not available)
* Batch Input: **$None per 1M tokens** (not available)

#### Context and Limits
The model has the following context and limits:
* Context Window: **262,144 tokens**
* Max Output: **4,096 tokens**
* Knowledge Cutoff: **2023-12** (model knowledge is limited to data up to December 2023)

#### Benchmarks
The Nemotron 3 Super has the following benchmark scores:
* **MMLU: 80.0** - The MMLU (Massive Multitask Language Understanding) benchmark measures a model's ability to perform a wide range of natural language processing tasks. A higher score indicates better performance. In this case, the Nemotron 3 Super has a score of 80.0, which suggests good performance in various NLP tasks.
* **HumanEval: None** - HumanEval is a benchmark that measures a model's ability to generate code that is correct and functional. The lack of a score for HumanEval suggests that the Nemotron 3 Super's coding capabilities have not been evaluated using this benchmark.
* **L

## Competitor Comparison
### Comparison of NVIDIA Nemotron 3 Super with Top Competitors
Since there are no direct competitors listed for the NVIDIA Nemotron 3 Super, we will provide a general overview of its features, pricing, and performance. This will help users understand its value proposition and make informed decisions.

#### Model Overview
The NVIDIA Nemotron 3 Super is a standard-tier model released by Nvidia on 2024-01-01. It is not open-source and has the following key features:

* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12
* **Capabilities**: text, function_calling, json_mode, streaming, structured_outputs
* **Best For**: chat, text_generation, coding, analysis, rag_pipelines, summarization

#### Pricing
The pricing for the NVIDIA Nemotron 3 Super is as follows:

* **Input**: $0.1 per 1M tokens
* **Output**: $0.5 per 1M tokens
* **Cached Input**: $None per 1M tokens
* **Batch Input**: $None per 1M tokens

#### Cost Examples
Here are some cost examples to help estimate the expenses:

* **1,000 calls (avg 500 tokens)**: $0.3
* **10,000 calls**: $3.0
* **100,000 calls**: $30.0

#### Performance Trade-offs
The NVIDIA Nemotron 3 Super has the following benchmark scores:

* **MMLU**: 80.0
* **LMSYS Arena ELO**: 1200

While there are no direct competitors, these benchmark scores indicate that the NVIDIA Nemotron 3 Super is a capable model. However, the lack of HumanEval and GSM8K scores makes it difficult to compare its performance with other models in certain areas.

#### When to Choose the NVIDIA Nemotron 3 Super
Based on its features and pricing, the NVIDIA Nemotron 3 Super is suitable for applications that require:

* Large context windows (262,144 tokens)
* Medium to long output sequences (up to 4,096 tokens)
* Support for text, function_calling, json_mode, streaming, and structured_outputs
* Reasonable pricing ($0.1 per 1M input tokens and $0.5 per 1M output tokens)

In the absence of direct competitors,

## Best Use Cases
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super is a powerful language model released by Nvidia on 2024-01-01. With its capabilities in text, function calling, JSON mode, streaming, and structured outputs, it is best suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization.

### Top 5 Best Use Cases for NVIDIA Nemotron 3 Super
Given its capabilities and pricing model, here are the top 5 best use cases for the NVIDIA Nemotron 3 Super:

1. **Chat and Conversational Systems**: The model's ability to understand and generate human-like text makes it an ideal choice for building conversational systems. With a context window of 262,144 tokens, it can engage in lengthy and meaningful conversations.
2. **Text Generation and Summarization**: The Nemotron 3 Super can generate high-quality text and summaries, making it suitable for applications such as content generation, news summarization, and document analysis.
3. **Coding and Function Calling**: The model's capability to call functions and generate code makes it a valuable tool for developers. It can be used to automate coding tasks, generate boilerplate code, and even assist in debugging.
4. **Analysis and RAG Pipelines**: The Nemotron 3 Super can be used to analyze large datasets and generate insights. Its ability to work with structured outputs and JSON mode makes it an ideal choice for building RAG (Retrieval-Augmented Generation) pipelines.
5. **Streaming and Real-time Applications**: The model's support for streaming and real-time processing makes it suitable for applications such as live chat, real-time text analysis, and streaming data processing.

### Code Integration Examples with OpenRouter
To integrate the NVIDIA Nemotron 3 Super with OpenRouter, you can use the following code examples:

```python
import openrouter
from nvidia import Nemotron3Super

# Initialize the Nem

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
