# xAI: Grok 4.20 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-05
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to xAI: Grok 4.20
xAI: Grok 4.20 is a standard-tier model provided by X-ai, released on January 1, 2024. This model is not open source. From an architectural standpoint, xAI: Grok 4.20 is designed to handle a wide range of natural language processing tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 2,000,000 tokens and generate outputs of up to 4,096 tokens, making it suitable for complex tasks such as chat, text generation, coding, analysis, and summarization.

### Technical Specifications and Pricing
Technically, xAI: Grok 4.20 has a knowledge cutoff of December 2023, indicating that its training data does not include information beyond this date. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. In terms of pricing, the model charges $2.0 per 1M tokens for input and $6.0 per 1M tokens for output. There are no charges specified for cached input or batch input. For example, 1,000 calls with an average of 500 tokens would cost $4.0, scaling up to $400.0 for 100,000 calls. This pricing structure suggests that the model is designed for applications where the value of the output justifies the cost per token.

### Use Cases and Competitors
xAI: Grok 4.20 is best suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization, thanks to its robust capabilities and large context window. However, its limitations and the absence of direct competitors mean that developers should carefully evaluate their needs against the model's specifications. With

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $2.0 |
| Output | $6.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### xAI: Grok 4.20 Pricing Analysis
#### Overview
The xAI: Grok 4.20 model, provided by X-ai, is a standard, non-open-source model released on January 1, 2024. This analysis will delve into the cost structure, usage scenarios, and scalability of this model.

#### Cost Structure
The pricing for xAI: Grok 4.20 is as follows:
* **Input**: $2.0 per 1M tokens
* **Output**: $6.0 per 1M tokens
* **Cached Input**: $0 per 1M tokens (free)
* **Batch Input**: $0 per 1M tokens (free)

#### Usage Scenarios
* **Cached Tokens**: Since cached input tokens are free, it is recommended to use them whenever possible to minimize costs. This can be particularly useful for applications with repetitive or similar input patterns.
* **Batch API Savings**: Although batch input is free, the cost savings come from reducing the number of API calls. By batching inputs, you can reduce the overall number of calls, resulting in lower output costs.
* **Cost at Scale**: The cost of using xAI: Grok 4.20 at scale is as follows:
	+ **1,000 calls** (avg 500 tokens): $4.0
	+ **10,000 calls**: $40.0
	+ **100,000 calls**: $400.0

#### Cost Calculation
To estimate the cost of using xAI: Grok 4.20, you can use the following formula:
`Cost = (Input Tokens / 1,000,000) * $2.0 + (Output Tokens / 1,000,000) * $6.0`

For example, if you make 1,000 calls with an average of 500 tokens per call, and assuming an average output of 200 tokens per call

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### xAI: Grok 4.20 Benchmark Performance Analysis
#### Overview
The xAI: Grok 4.20 model, released by X-ai on 2024-01-01, is a standard, non-open-source model. This analysis will delve into its benchmark performance, focusing on the MMLU, HumanEval, and Arena ELO scores, to understand its capabilities and limitations in real-world applications.

#### Benchmark Scores
- **MMLU (Massive Multitask Language Understanding) Score: 80.0**
  The MMLU score measures a model's ability to perform a wide range of natural language processing tasks. A score of 80.0 indicates that xAI: Grok 4.20 has a strong foundation in understanding and generating human-like text, making it suitable for tasks such as text generation, chat, and analysis.
- **HumanEval Score: None**
  The absence of a HumanEval score means that the model's performance on human evaluation metrics, which assess the model's ability to generate coherent and contextually appropriate text, is not available. This lack of data makes it challenging to fully assess the model's capabilities in tasks requiring high levels of human-like understanding and response generation.
- **LMSYS Arena ELO Score: 1200**
  The LMSYS Arena ELO score is a measure of a model's performance in a competitive environment, often involving tasks that require strategic thinking and problem-solving. An ELO score of 1200 suggests that xAI: Grok 4.20 has a moderate level of proficiency in such tasks, indicating potential suitability for coding, analysis, and possibly strategy-based applications.

#### Real-World Implications


## Competitor Comparison
### xAI: Grok 4.20 Comparison
Since xAI: Grok 4.20 does not have direct competitors listed, we will provide a general overview of its features, pricing, and performance. This will help users understand when to choose this model and what trade-offs to expect.

#### Pricing
The pricing for xAI: Grok 4.20 is as follows:
* Input: **$2.0 per 1M tokens**
* Output: **$6.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Performance
The performance of xAI: Grok 4.20 is measured by the following benchmarks:
* MMLU: **80.0**
* LMSYS Arena ELO: **1200**

#### Capabilities and Limits
xAI: Grok 4.20 has the following capabilities and limits:
* Context Window: **2,000,000 tokens**
* Max Output: **4,096 tokens**
* Knowledge Cutoff: **2023-12**
* Capabilities: **text**, **function_calling**, **json_mode**, **streaming**, **structured_outputs**

#### Best Use Cases
xAI: Grok 4.20 is best for:
* **chat**
* **text_generation**
* **coding**
* **analysis**
* **rag_pipelines**
* **summarization**

#### Cost Examples
The cost of using xAI: Grok 4.20 can be estimated as follows:
* 1,000 calls (avg 500 tokens): **$4.0**
* 10,000 calls: **$40.0**
* 100,000 calls: **$400.0**

### Choosing xAI: Grok 4.20
Since there are no direct competitors listed, xAI: Grok 4.20 can be considered a unique offering in the market. Its pricing and performance make it a viable option for users who require a model with a large context window and a range of capabilities.

When to choose xAI: Grok 4.20:
* When you need a model with a large context window (**2,000,000 tokens**) and a high max output (**4,096 tokens**).
* When you require a model with a range of capabilities, including **text**, **function_calling

## Best Use Cases
### Introduction to xAI: Grok 4.20
The xAI: Grok 4.20 model, released by X-ai on 2024-01-01, is a standard, non-open source model with a unique set of capabilities. This guide will explore the top 5 best use cases for xAI: Grok 4.20, along with code integration examples using OpenRouter.

### Top 5 Use Cases for xAI: Grok 4.20
Based on the model's capabilities, the top 5 use cases for xAI: Grok 4.20 are:

1. **Chat and Text Generation**: With its ability to handle text and generate human-like responses, xAI: Grok 4.20 is well-suited for chat applications.
2. **Coding and Analysis**: The model's function_calling and structured_outputs capabilities make it a good fit for coding and analysis tasks.
3. **Summarization**: xAI: Grok 4.20's ability to process large amounts of text and generate concise summaries makes it a good choice for summarization tasks.
4. **RAG Pipelines**: The model's support for rag_pipelines makes it a good fit for tasks that require retrieving and generating text based on external knowledge.
5. **Streaming and JSON Mode**: xAI: Grok 4.20's support for streaming and json_mode makes it a good choice for applications that require processing large amounts of JSON data in real-time.

### Code Integration Examples with OpenRouter
To integrate xAI: Grok 4.20 with OpenRouter, you can use the following code examples:

```python
import openrouter

# Initialize the OpenRouter client
client = openrouter.Client(api_key="YOUR_API_KEY")

# Define the input prompt
prompt = "Write a short story about a character who discovers a hidden world."

# Define the model and parameters
model = "x-ai/g

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
