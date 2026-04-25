# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-25
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of natural language processing tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens, making it suitable for complex tasks such as chat, text generation, coding, analysis, and summarization.

### Technical Specifications and Pricing
Technically, Mistral Small 4 has a context window of 262,144 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2023-12. The model's pricing is based on input and output tokens, with costs of $0.15 per 1M input tokens and $0.6 per 1M output tokens. There are no specified costs for cached input or batch input. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. Given its capabilities and pricing, developers can estimate costs based on the number of calls and tokens processed, such as $0.375 for 1,000 calls averaging 500 tokens, $3.75 for 10,000 calls, and $37.5 for 100,000 calls.

### Use Cases and Competitors
Mistral Small 4 is best suited for applications involving chat, text generation, coding, analysis, RAG pipelines, and summarization, thanks to its robust capabilities and large context window. However, its limitations and areas where it is not recommended are not specified. As of the provided data, there are no direct competitors listed for Mistral Small

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
Mistral: Mistral Small 4, provided by Mistralai, is a standard tier model with a release date of 2024-01-01. This model is not open source. The pricing structure for this model is based on input and output tokens.

#### Cost Structure
The cost structure for Mistral: Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs when the same input is used multiple times. Since cached input is free, it is recommended to use cached tokens whenever possible to minimize costs.

#### Batch API Savings
Batch input is also free, which means that making batch API calls can help reduce costs. By batching API calls, users can take advantage of the free batch input pricing to lower their overall costs.

#### Cost at Scale
The cost of using Mistral: Mistral Small 4 at scale is as follows:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These costs are based on the average number of tokens per call and can be used to estimate the total cost of using the model for large-scale applications.

#### Context and Limits
The context window for Mistral: Mistral Small 4 is 262,144 tokens, and the maximum output is 4,096 tokens. The knowledge cutoff for this model is 2023-12, which means that it may not have information on events or developments after this date.

#### Capabilities and Best

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Performance Analysis
The Mistral Small 4 model, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. It is not open source.

#### Pricing Structure
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

#### Benchmark Performance
The benchmark performance of Mistral Small 4 is as follows:
* MMLU: **80.0**
* HumanEval: **None**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

The MMLU score of 80.0 indicates the model's performance on a set of math and logic problems. A higher score generally indicates better performance. However, without a direct comparison to other models, it's difficult to assess the significance of this score.

The LMSYS Arena ELO score of 1200 is a measure of the model's performance in a competitive setting, with higher scores indicating better performance. An ELO score of 1200 is generally considered to be a moderate level of performance.

The lack of HumanEval and GSM8K scores makes it difficult to assess the model's performance on specific tasks such as coding and math problem-solving.



## Competitor Comparison
### Mistral Small 4 Comparison
Since there are no direct competitors listed for the Mistral Small 4, we will provide a general overview of its features, pricing, and performance. This will help users understand its value proposition and make informed decisions.

#### Model Overview
The Mistral Small 4 is a standard-tier model released by Mistralai on 2024-01-01. It is not open-source and has the following key features:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12
* **Capabilities**: text, function_calling, json_mode, streaming, structured_outputs
* **Best For**: chat, text_generation, coding, analysis, rag_pipelines, summarization

#### Pricing
The pricing for the Mistral Small 4 is as follows:
* **Input**: $0.15 per 1M tokens
* **Output**: $0.6 per 1M tokens
* **Cached Input**: $None per 1M tokens
* **Batch Input**: $None per 1M tokens

#### Cost Examples
To illustrate the cost of using the Mistral Small 4, consider the following examples:
* **1,000 calls (avg 500 tokens)**: $0.375
* **10,000 calls**: $3.75
* **100,000 calls**: $37.5

#### Performance Trade-offs
The Mistral Small 4 has the following benchmark scores:
* **MMLU**: 80.0
* **LMSYS Arena ELO**: 1200
These scores indicate the model's performance in various tasks, but without direct competitors, it's challenging to provide a direct comparison.

#### Choosing the Mistral Small 4
Given its capabilities and pricing, the Mistral Small 4 is suitable for applications that require:
* Text generation and analysis
* Coding and summarization
* Chat and conversational AI
* RAG pipelines

When to choose the Mistral Small 4:
* When you need a standard-tier model with a large context window and moderate output size.
* When your application requires a balance between performance and cost.
* When you want to leverage the model's capabilities in text, function_calling, json_mode, streaming, and structured_outputs.

Keep in mind that the lack of direct competitors makes it essential to evaluate the Mistral

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and release date of 2024-01-01, it offers a robust solution for various applications. This guide will explore the top 5 best use cases for Mistral Small 4, along with practical advice and code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, the top 5 use cases for Mistral Small 4 are:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and max output of 4,096 tokens, Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: Its function calling and structured outputs capabilities make it an excellent choice for coding and analysis tasks, such as code completion and code review.
3. **Summarization**: Mistral Small 4's ability to process large amounts of text and generate concise summaries makes it a great fit for summarization tasks.
4. **RAG Pipelines**: Its support for retrieval-augmented generation (RAG) pipelines enables it to be used in applications that require generating text based on external knowledge sources.
5. **Content Creation**: With its text generation capabilities, Mistral Small 4 can be used for content creation tasks, such as generating articles, blog posts, and social media content.

### Code Integration Examples with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code examples:

```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.MistralSmall4()

# Text generation example
input_text = "Write a short story about a character who discovers a hidden world."
output =

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
