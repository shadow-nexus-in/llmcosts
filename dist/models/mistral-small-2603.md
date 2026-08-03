# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-03
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral: Mistral Small 4 is designed to handle a variety of tasks, including text generation, function calling, and structured outputs, thanks to its capabilities in text, function_calling, json_mode, streaming, and structured_outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens.

### Technical Specifications and Use Cases
The model's technical specifications highlight its potential for various applications. With a context window of 262,144 tokens and a maximum output of 4,096 tokens, Mistral: Mistral Small 4 is well-suited for tasks that require understanding and generating lengthy texts. Its capabilities in areas such as chat, text_generation, coding, analysis, rag_pipelines, and summarization make it a versatile tool for developers. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its competence in language understanding and generation tasks. However, its limitations, such as a knowledge cutoff of 2023-12, should be considered when applying it to tasks requiring very recent information.

### Pricing and Cost Considerations
The pricing model for Mistral: Mistral Small 4 is based on input and output tokens, with costs of $0.15 per 1M input tokens and $0.6 per 1M output tokens. For developers, understanding these costs is crucial for budgeting. For example, 1,000 calls with an average of 500 tokens would cost $0.375, while 100,000 calls would amount to $37.5. Given

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
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$0.00 per 1M tokens** (free)
* Batch Input: **$0.00 per 1M tokens** (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following strategies:
* **Cached Tokens**: Since cached input tokens are free, utilize them whenever possible to reduce input costs.
* **Batch API Calls**: With batch input being free, batch your API calls to minimize the number of requests and reduce overall costs.

#### Cost at Scale
The cost of using Mistral Small 4 at various scales is as follows:
* **1,000 calls (avg 500 tokens)**: **$0.375**
* **10,000 calls**: **$3.75**
* **100,000 calls**: **$37.5**

These costs demonstrate a linear relationship with the number of API calls, indicating that the cost per call remains constant regardless of the scale.

#### Context and Limits
When using Mistral Small 4, be aware of the following context and limits:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12

#### Capabilities and Use Cases
Mistral Small 4 is capable of:
* Text
* Function calling
* JSON mode
* Streaming
* Structured outputs

It is best suited for applications such

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Mistral Small 4 Benchmark Performance
#### Model Overview
The Mistral Small 4 model, provided by Mistralai, is a standard-tier model released on 2024-01-01. It is not open-source.

#### Pricing Structure
The pricing for Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Context and Limits
The model has the following context and limits:
* Context Window: 262,144 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2023-12

#### Benchmark Performance
The benchmark performance of Mistral Small 4 is as follows:
* MMLU: 80.0
* HumanEval: None
* LMSYS Arena ELO: 1200
* GSM8K: None

The MMLU score of 80.0 indicates the model's performance on a set of mathematical and logical tasks. A higher MMLU score generally indicates better performance on these tasks.

The LMSYS Arena ELO score of 1200 is a measure of the model's overall performance in a competitive setting. ELO scores are used to rank models based on their performance, with higher scores indicating better performance.

The lack of HumanEval and GSM8K scores means that the model's performance on these specific benchmarks is not available.

#### Real-World Implications
The benchmark performance of Mistral Small 4 has the following implications for real-world use:
* The model's

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral: Mistral Small 4 model, we will provide a general analysis of its features, pricing, and performance. This will help potential users understand the value proposition of this model and make informed decisions.

#### Model Overview
The Mistral: Mistral Small 4 model is a standard, non-open-source model released by Mistralai on 2024-01-01. It has a context window of 262,144 tokens and can generate up to 4,096 output tokens.

#### Pricing
The pricing for the Mistral: Mistral Small 4 model is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens (not available)
* Batch Input: $None per 1M tokens (not available)

#### Performance
The model's performance is measured by the following benchmarks:
* MMLU: 80.0
* LMSYS Arena ELO: 1200

#### Capabilities and Use Cases
The Mistral: Mistral Small 4 model supports the following capabilities:
* text
* function_calling
* json_mode
* streaming
* structured_outputs

It is best suited for the following use cases:
* chat
* text_generation
* coding
* analysis
* rag_pipelines
* summarization

#### Cost Examples
To help estimate costs, here are some examples:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

#### Choosing the Right Model
Since there are no direct competitors listed, the decision to use the Mistral: Mistral Small 4 model will depend on the specific requirements of your project. Consider the following factors:
* **Context window**: If your application requires a large context window, this model may be a good choice.
* **Output length**: If you need to generate longer output sequences, this model's 4,096 token limit may be sufficient.
* **Pricing**: Compare the pricing of this model with other available options to ensure it fits within your budget.
* **Capabilities**: If your use case requires one or more of the supported capabilities (e.g

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and release date of 2024-01-01, it's an attractive option for various applications. This guide will explore the top 5 best use cases for Mistral Small 4, along with practical advice and code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Small 4
#### 1. **Chat and Conversational AI**
Mistral Small 4 is well-suited for chat and conversational AI applications, thanks to its text generation capabilities and large context window of 262,144 tokens. You can use it to build conversational interfaces, such as chatbots or virtual assistants.

#### 2. **Text Generation and Summarization**
With its ability to generate human-like text and summarize long documents, Mistral Small 4 is ideal for text generation and summarization tasks. You can use it to automate content creation, summarize news articles, or generate product descriptions.

#### 3. **Coding and Function Calling**
Mistral Small 4's function calling capability makes it a great tool for coding and software development. You can use it to generate code snippets, automate coding tasks, or even build entire applications.

#### 4. **Analysis and RAG Pipelines**
Mistral Small 4's ability to analyze and process large amounts of data makes it suitable for analysis and RAG (Retrieve, Augment, Generate) pipeline tasks. You can use it to analyze customer feedback, generate insights, or build predictive models.

#### 5. **Structured Outputs and JSON Mode**
Mistral Small 4's structured output and JSON mode capabilities make it a great tool for generating structured data, such as JSON objects or XML files. You can use it to automate data processing,

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
