# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-06
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of natural language processing tasks with its robust capabilities, including text generation, function calling, JSON mode, streaming, and structured outputs. Its architecture supports a context window of up to 262,144 tokens and can generate outputs of up to 4,096 tokens.

### Strengths and Use Cases
The main strengths of Mistral: Mistral Small 4 lie in its versatility and performance across multiple benchmarks. With an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, it demonstrates a strong foundation in understanding and generating human-like text. Its capabilities make it best suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization. Developers can leverage these strengths to build applications that require advanced language understanding and generation capabilities. The model's pricing structure, with input costing $0.15 per 1M tokens and output costing $0.6 per 1M tokens, provides a clear cost framework for integration and scaling.

### Technical Specifications and Cost Considerations
Technically, Mistral: Mistral Small 4 has specific limits, including a context window of 262,144 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2023-12. For developers planning to integrate this model, understanding the pricing is crucial. For example, 1,000 calls with an average of 500 tokens would cost $0.375, scaling up to $3.75 for 10,000 calls and $37.5 for 100,000 calls. Given its capabilities and pricing, Mistral: Mistral Small 

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
Mistral Small 4, provided by Mistralai, is a standard-tier model released on 2024-01-01. This analysis breaks down the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$0.00 per 1M tokens** (free)
* Batch Input: **$0.00 per 1M tokens** (free)

#### Optimizing Costs with Cached Tokens and Batch API
To minimize costs, utilize **cached input tokens** whenever possible, as they are free. Additionally, leverage **batch input** for bulk operations, which also incurs no extra cost.

#### Cost at Scale
The cost of using Mistral Small 4 at various scales is as follows:
* **1,000 API calls** (avg 500 tokens): **$0.375**
* **10,000 API calls**: **$3.75**
* **100,000 API calls**: **$37.5**

These costs are calculated based on the average token usage per call. For precise calculations, consider the input and output token counts for your specific use case.

#### Context and Limits
Keep in mind the following context and limits when using Mistral Small 4:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12

#### Capabilities and Best Use Cases
Mistral Small 4 supports the following capabilities:
* text
* function_calling
* json_mode
* streaming
* structured_outputs

It is best suited for applications such as:
* chat
* text_generation
* coding
* analysis

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
The Mistral Small 4 model, provided by Mistralai, is a standard-tier model released on 2024-01-01. It is not open-source.

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
The model's benchmark performance is as follows:
* MMLU: **80.0**
* HumanEval: **None**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

The MMLU score of **80.0** indicates the model's ability to understand and generate human-like text. A higher MMLU score generally corresponds to better language understanding and generation capabilities.

The LMSYS Arena ELO score of **1200** is a measure of the model's performance in a competitive setting, where it is pitted against other models. A higher ELO score indicates better performance.

The lack of HumanEval and GSM8K scores means that the model's performance on these specific benchmarks is unknown.

#### Capabilities and Use Cases
Mistral Small 4 supports the following capabilities:
* text
* function_calling
* json_mode


## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral Small 4, we will provide a general overview of its features, pricing, and performance. This will help users understand when to choose Mistral Small 4 and what trade-offs to expect.

#### Model Overview
* **Model:** Mistral Small 4 (mistralai/mistral-small-2603)
* **Provider:** Mistralai
* **Release Date:** 2024-01-01
* **Tier:** Standard
* **Open Source:** False

#### Pricing
The pricing for Mistral Small 4 is as follows:
* **Input:** $0.15 per 1M tokens
* **Output:** $0.6 per 1M tokens
* **Cached Input:** $None per 1M tokens
* **Batch Input:** $None per 1M tokens

#### Context and Limits
* **Context Window:** 262,144 tokens
* **Max Output:** 4,096 tokens
* **Knowledge Cutoff:** 2023-12

#### Benchmarks
* **MMLU:** 80.0
* **HumanEval:** None
* **LMSYS Arena ELO:** 1200
* **GSM8K:** None

#### Capabilities and Best Use Cases
Mistral Small 4 supports the following capabilities:
* **Text**
* **Function calling**
* **JSON mode**
* **Streaming**
* **Structured outputs**

It is best suited for:
* **Chat**
* **Text generation**
* **Coding**
* **Analysis**
* **RAG pipelines**
* **Summarization**

#### Cost Examples
Here are some cost examples for using Mistral Small 4:
* **1,000 calls (avg 500 tokens):** $0.375
* **10,000 calls:** $3.75
* **100,000 calls:** $37.5

#### Choosing Mistral Small 4
Since there are no direct competitors listed, users should consider the following factors when choosing Mistral Small 4:
* **Performance requirements:** If you need a model with a high context window (262,144 tokens) and a moderate max output (4,096 tokens), Mistral Small 4 may be a good choice.
* **Pricing constraints:** If you are looking for a model with a relatively low input

## Best Use Cases
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on 2024-01-01, this model is part of the standard tier and is not open source.

### Pricing Model
The pricing for Mistral: Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

### Top 5 Best Use Cases
Based on the capabilities and benchmarks of Mistral: Mistral Small 4, the top 5 best use cases for this model are:

1. **Chat**: With its high MMLU score of 80.0 and ability to handle large context windows (262,144 tokens), Mistral: Mistral Small 4 is well-suited for chat applications.
2. **Text Generation**: The model's text generation capabilities make it a good fit for tasks such as writing articles, creating content, and generating text summaries.
3. **Coding**: Mistral: Mistral Small 4's function calling and structured outputs capabilities make it a good choice for coding tasks, such as generating code snippets or completing partial code.
4. **Analysis**: The model's ability to handle large context windows and generate structured outputs make it suitable for analysis tasks, such as data analysis or research paper summarization.
5. **Summarization**: With its high MMLU score and ability to generate structured outputs, Mistral: Mistral Small 4 is well-suited for summarization tasks, such as summarizing long documents or articles.

### Code Integration Example with OpenRouter
To integrate Mistral: Mistral Small 4 with OpenRouter

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
