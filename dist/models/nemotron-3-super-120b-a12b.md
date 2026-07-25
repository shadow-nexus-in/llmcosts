# NVIDIA: Nemotron 3 Super API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-25
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super, released on 2024-01-01, is a powerful language model developed by Nvidia. This model, identified as `nvidia/nemotron-3-super-120b-a12b`, operates under a standard tier and is not open-source. With its robust architecture, the Nemotron 3 Super is designed to handle a wide range of tasks, including but not limited to text generation, coding, analysis, and summarization. Its capabilities extend to function calling, JSON mode, streaming, and structured outputs, making it a versatile tool for developers.

### Technical Specifications and Pricing
Technically, the Nemotron 3 Super boasts a context window of 262,144 tokens and can generate up to 4,096 tokens as output. The model's knowledge cutoff is 2023-12, ensuring it is informed by data up to that point. In terms of pricing, developers can expect to pay $0.1 per 1M tokens for input and $0.5 per 1M tokens for output. There are no specified costs for cached input or batch input. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its capabilities in various linguistic and logical tasks. With cost examples ranging from $0.3 for 1,000 calls (avg 500 tokens) to $30.0 for 100,000 calls, the Nemotron 3 Super offers a scalable solution for projects of varying sizes.

### Use Cases and Competitiveness
The NVIDIA Nemotron 3 Super is best utilized for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization, thanks to its broad capabilities. However, its limitations and areas where it is "not good for" are not specified, suggesting a need for further evaluation based on specific

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
The NVIDIA Nemotron 3 Super is a powerful language model offered by Nvidia, released on January 1, 2024. This analysis will delve into the cost structure, usage scenarios, and provide a detailed breakdown of the costs at various scales.

#### Cost Structure
The pricing for the NVIDIA Nemotron 3 Super is as follows:
* **Input**: $0.1 per 1M tokens
* **Output**: $0.5 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

#### Usage Scenarios
* **Cached Tokens**: Since cached input is free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
* **Batch API Savings**: Although batch input is free, the actual cost savings will depend on the output tokens required. Batch processing can help reduce the overall number of API calls, leading to cost savings on output tokens.

#### Cost at Scale
The costs for the NVIDIA Nemotron 3 Super at various scales are as follows:
* **1,000 calls (avg 500 tokens)**: $0.3
* **10,000 calls**: $3.0
* **100,000 calls**: $30.0

To estimate the costs, we can use the following formula:
`Cost = (Input Tokens / 1,000,000) * $0.1 + (Output Tokens / 1,000,000) * $0.5`

Assuming an average output of 500 tokens per call, we can calculate the costs as follows:
* **1,000 calls**: `(500,000 / 1,000,000) * $0.1 + (500,000 / 1,000,000) * $0.5 = $0.3`
* **10,000 calls

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
The NVIDIA Nemotron 3 Super is a standard-tier model released by Nvidia on January 1, 2024. It is not open-source and has a specific pricing structure for input and output tokens.

#### Pricing Structure
The pricing for the Nemotron 3 Super is as follows:
* Input: **$0.1 per 1M tokens**
* Output: **$0.5 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Context and Limits
The model has the following context and limits:
* Context Window: **262,144 tokens**
* Max Output: **4,096 tokens**
* Knowledge Cutoff: **2023-12**

#### Benchmarks
The Nemotron 3 Super has the following benchmark scores:
* MMLU: **80.0**
* HumanEval: **None**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

The MMLU score of 80.0 indicates the model's performance on a specific set of tasks, with higher scores generally indicating better performance. The LMSYS Arena ELO score of 1200 provides a relative ranking of the model's performance compared to other models, with higher scores indicating better performance.

#### Capabilities and Use Cases
The Nemotron 3 Super supports the following capabilities:
* text
* function_calling
* json_mode
* streaming
* structured_outputs

It is best suited for tasks such as:
* chat
* text_generation
* coding
* analysis
* rag_pipelines
*

## Competitor Comparison
### Comparison of NVIDIA Nemotron 3 Super with Top Competitors
Since there are no direct competitors listed for the NVIDIA Nemotron 3 Super, we will provide a general overview of the model's features, pricing, and performance. This will help users understand when to choose this model and what trade-offs to expect.

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

#### Performance
The model's performance is measured by the following benchmarks:
* **MMLU**: 80.0
* **LMSYS Arena ELO**: 1200

#### Cost Examples
The estimated costs for using the NVIDIA Nemotron 3 Super are:
* **1,000 calls (avg 500 tokens)**: $0.3
* **10,000 calls**: $3.0
* **100,000 calls**: $30.0

#### Choosing the NVIDIA Nemotron 3 Super
Since there are no direct competitors listed, the decision to choose the NVIDIA Nemotron 3 Super depends on the specific use case and requirements. Consider the following factors:
* **Performance**: If high performance is required, the NVIDIA Nemotron 3 Super's MMLU score of 80.0 and LMSYS Arena ELO score of 1200 may be attractive.
* **Pricing**: The model's pricing is competitive, with input costs of $0.1 per 1M tokens and output costs of $0.5 per 1M tokens.
* **Capabilities**: The model supports a range of capabilities, including text, function_calling, json_mode, streaming, and structured_outputs, making

## Best Use Cases
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super is a powerful language model released by Nvidia on 2024-01-01. With its standard tier and closed-source architecture, it offers a range of capabilities including text generation, function calling, and structured outputs. In this guide, we will explore the top 5 best use cases for the NVIDIA Nemotron 3 Super, along with practical advice and code integration examples using OpenRouter.

### Top 5 Use Cases for NVIDIA Nemotron 3 Super
#### 1. **Chat and Text Generation**
The NVIDIA Nemotron 3 Super excels in chat and text generation tasks, making it an ideal choice for conversational AI applications. With its context window of 262,144 tokens, it can handle complex conversations with ease.

#### 2. **Coding and Analysis**
The model's ability to perform function calling and generate structured outputs makes it suitable for coding and analysis tasks. It can be used to generate code snippets, analyze code quality, and even provide suggestions for improvement.

#### 3. **Summarization and RAG Pipelines**
The NVIDIA Nemotron 3 Super can be used for summarization tasks, condensing large amounts of text into concise summaries. It also supports RAG (Retrieve, Augment, Generate) pipelines, enabling it to retrieve relevant information, augment it with additional context, and generate summaries.

#### 4. **JSON Mode and Streaming**
The model's JSON mode and streaming capabilities make it suitable for real-time data processing and analysis. It can be used to process JSON data streams, generate reports, and provide insights in real-time.

#### 5. **Structured Outputs**
The NVIDIA Nemotron 3 Super's ability to generate structured outputs makes it ideal for applications that require well-organized data. It can be used to generate reports, invoices, and other documents with precise formatting and structure.

### Code Integration Examples with OpenRouter
To integrate the NVIDIA Nem

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
