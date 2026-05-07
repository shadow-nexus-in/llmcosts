# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-07
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral: Mistral Small 4 is designed to handle a variety of tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens, making it suitable for complex text generation and analysis tasks.

### Technical Specifications and Use Cases
The model's technical specifications highlight its potential for various applications. With a context window of 262,144 tokens and a maximum output of 4,096 tokens, Mistral: Mistral Small 4 is well-suited for tasks such as chat, text generation, coding, analysis, and summarization. Its capabilities in function calling, JSON mode, and streaming further enhance its utility in real-time and dynamic applications. The model's knowledge cutoff is 2023-12, indicating that its training data includes information up to December 2023. Benchmarks show an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, demonstrating its competence in language understanding and generation tasks.

### Pricing and Cost Considerations
The pricing model for Mistral: Mistral Small 4 is based on input and output tokens, with costs of $0.15 per 1M input tokens and $0.6 per 1M output tokens. There are no specified costs for cached input or batch input. Example costs include $0.375 for 1,000 calls averaging 500 tokens, $3.75 for 10,000 calls, and $37.5 for 100,000 calls. Given its capabilities and pricing, Mistral:

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
Mistral Small 4, provided by Mistralai, is a standard tier model released on 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and scaling costs for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$0.00 per 1M tokens** (free)
* Batch Input: **$0.00 per 1M tokens** (free)

#### Optimal Usage Scenarios
* **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
* **Batch API Savings**: Although batch input is free, there is no direct cost savings mentioned for batch API calls. However, batch processing can still improve efficiency and reduce the overall number of API calls.

#### Cost at Scale
The costs for Mistral Small 4 at different scales are as follows:
* **1,000 calls (avg 500 tokens)**: **$0.375**
* **10,000 calls**: **$3.75**
* **100,000 calls**: **$37.5**

These costs demonstrate a linear scaling of expenses with the number of API calls, indicating that the cost per call remains constant.

#### Conclusion
Mistral Small 4 offers a competitive pricing structure, especially with the availability of free cached input tokens. By leveraging cached tokens and optimizing API calls, users can minimize their expenses. As the number of API calls increases, the total cost scales linearly, making it essential to carefully plan and manage API usage to control costs.

#### Recommendations
* Utilize cached input tokens whenever possible to reduce costs.
* Optimize API calls to minimize the total number of requests.


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

The MMLU score of **80.0** indicates the model's ability to understand and generate human-like text. A higher MMLU score generally corresponds to better performance in natural language understanding and generation tasks.

The LMSYS Arena ELO score of **1200** is a measure of the model's performance in a competitive setting, where it is pitted against other models. A higher ELO score indicates better performance.

The lack of HumanEval and GSM8K scores means that the model's performance in these specific areas is not available.

#### Capabilities and Use Cases
Mistral Small 4 supports the following capabilities:
* text
* function_calling


## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral Small 4 model, we will provide a general overview of the model's features, pricing, and performance. This will help users understand the value proposition of the Mistral Small 4 and make informed decisions about its adoption.

#### Model Overview
The Mistral Small 4 model is a standard-tier model provided by Mistralai, released on 2024-01-01. It is not open-source.

#### Pricing
The pricing for the Mistral Small 4 model is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Performance and Capabilities
The Mistral Small 4 model has the following performance metrics and capabilities:
* Context Window: 262,144 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2023-12
* Benchmarks:
	+ MMLU: 80.0
	+ LMSYS Arena ELO: 1200
* Capabilities: text, function_calling, json_mode, streaming, structured_outputs
* Best for: chat, text_generation, coding, analysis, rag_pipelines, summarization

#### Cost Examples
The estimated costs for using the Mistral Small 4 model are:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

#### Choosing the Mistral Small 4 Model
Since there are no direct competitors listed, the decision to choose the Mistral Small 4 model depends on the specific use case and requirements. Consider the following factors:
* **Performance**: If your application requires a high context window (262,144 tokens) and moderate output size (4,096 tokens), the Mistral Small 4 model may be a good choice.
* **Pricing**: If your budget is constrained, the Mistral Small 4 model's pricing may be competitive, with an input cost of $0.15 per 1M tokens and an output cost of $0.6 per 1M tokens.
* **Capabilities**: If your application requires advanced features like function

## Best Use Cases
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on 2024-01-01, this model is part of the standard tier and is not open source.

### Pricing Model
The pricing for Mistral: Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

### Top 5 Best Use Cases for Mistral: Mistral Small 4
Based on its capabilities, here are the top 5 best use cases for Mistral: Mistral Small 4:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and ability to generate up to 4,096 tokens of output, Mistral: Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: The model's function calling and structured outputs capabilities make it a good fit for coding and analysis tasks, such as code completion and data analysis.
3. **Summarization**: Mistral: Mistral Small 4's ability to generate concise and accurate summaries of long pieces of text makes it a good choice for summarization tasks.
4. **RAG Pipelines**: The model's support for Retrieval-Augmented Generation (RAG) pipelines makes it a good fit for applications that require the generation of text based on external knowledge sources.
5. **Streaming**: With its support for streaming, Mistral: Mistral Small 4 can be used for real-time text generation and analysis applications.

### Code Integration Example with OpenRouter
Here is an example of how to integrate Mist

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
