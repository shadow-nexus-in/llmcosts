# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-17
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral: Mistral Small 4 is designed to handle a variety of tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process and generate human-like text, making it suitable for applications such as chat, text generation, coding, analysis, and summarization.

### Technical Specifications and Use Cases
The model has a context window of 262,144 tokens and can produce a maximum output of 4,096 tokens. The knowledge cutoff for this model is 2023-12, indicating that its training data does not include information beyond this date. Mistral: Mistral Small 4 excels in tasks that require understanding and generating text, such as chatbots, text generation, and coding assistance. Its capabilities in function calling and JSON mode also make it a strong candidate for tasks that involve complex data processing and analysis. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, demonstrating its competence in natural language understanding and generation.

### Pricing and Cost Considerations
The pricing for Mistral: Mistral Small 4 is based on input and output tokens. The cost is $0.15 per 1M input tokens and $0.6 per 1M output tokens. There are no specified costs for cached input or batch input. To give developers an idea of the cost, examples are provided: 1,000 calls averaging 500 tokens cost $0.375, 10,000 calls cost $3.75, and 100,000 calls cost $37.5. With its unique set of capabilities and competitive

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
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens (free)
* Batch Input: $None per 1M tokens (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following strategies:
* **Cached Tokens**: Utilize cached input tokens whenever possible, as they are free. This is ideal for scenarios where the input data is repetitive or can be pre-processed and stored.
* **Batch API Savings**: Leverage batch input to reduce costs. Although the pricing is listed as $None per 1M tokens, it is essential to note that this might imply a discounted rate or a free tier for batch processing. However, without explicit pricing, it's challenging to provide a precise cost savings estimate.

#### Cost at Scale
The cost examples provided are:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

To estimate the cost at scale, we can extrapolate from these examples. Assuming a linear cost increase, we can calculate the cost per call:
* 1,000 calls: $0.375 / 1,000 = $0.000375 per call
* 10,000 calls: $3.75 / 10,000 = $0.000375 per call
* 100,000 calls: $37.5 / 100,

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Benchmark Performance Analysis
#### Overview
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. It is not open-source and has specific pricing for input and output tokens.

#### Pricing
The pricing model for Mistral Small 4 is as follows:
- Input: **$0.15 per 1M tokens**
- Output: **$0.6 per 1M tokens**
- Cached Input: **$None per 1M tokens**
- Batch Input: **$None per 1M tokens**

#### Context and Limits
The model has the following context and limits:
- Context Window: **262,144 tokens**
- Max Output: **4,096 tokens**
- Knowledge Cutoff: **2023-12**

#### Benchmarks
The benchmark performance of Mistral Small 4 is:
- MMLU: **80.0**
- HumanEval: **None**
- LMSYS Arena ELO: **1200**
- GSM8K: **None**

#### Capabilities and Use Cases
Mistral Small 4 supports the following capabilities:
- text
- function_calling
- json_mode
- streaming
- structured_outputs

It is best suited for:
- chat
- text_generation
- coding
- analysis
- rag_pipelines
- summarization

#### Benchmark Interpretation
- **MMLU (80.0)**: The MMLU score indicates the model's performance on a specific set of tasks. A higher score generally means better performance. With an MMLU score of 80.0, Mistral Small 4 demonstrates

## Competitor Comparison
### Mistral Small 4 Comparison
Since there are no direct competitors listed for the Mistral Small 4, we will provide a general overview of its features, pricing, and performance. This will help users understand the model's strengths and weaknesses, and make informed decisions about when to choose this model.

#### Pricing
The Mistral Small 4 is priced as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Performance Trade-offs
The Mistral Small 4 has the following performance characteristics:
* Context Window: 262,144 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2023-12
* Benchmarks:
	+ MMLU: 80.0
	+ LMSYS Arena ELO: 1200

#### Capabilities and Use Cases
The Mistral Small 4 supports the following capabilities:
* Text
* Function calling
* JSON mode
* Streaming
* Structured outputs

It is best suited for the following use cases:
* Chat
* Text generation
* Coding
* Analysis
* RAG pipelines
* Summarization

#### Cost Examples
Here are some cost examples for using the Mistral Small 4:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

#### Choosing the Mistral Small 4
When to choose the Mistral Small 4:
* When you need a model with a large context window (262,144 tokens) and a moderate output size (4,096 tokens).
* When you require a model with a high MMLU score (80.0) and a moderate LMSYS Arena ELO score (1200).
* When you need to perform tasks that require text, function calling, JSON mode, streaming, and structured outputs.
* When you are working on chat, text generation, coding, analysis, RAG pipelines, or summarization tasks.

Note that the Mistral Small 4 is not open-source and has a knowledge cutoff of 2023-12, which may be a limitation for some users. Additionally, the model's performance on certain benchmarks (e

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and release date of 2024-01-01, it offers a robust solution for various applications. This guide will explore the top 5 best use cases for Mistral Small 4, along with practical advice and code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, the top 5 use cases for Mistral Small 4 are:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and max output of 4,096 tokens, Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: Its function calling and structured outputs capabilities make it an excellent choice for coding and analysis tasks, such as code completion and code review.
3. **Summarization**: Mistral Small 4's text generation capabilities and high context window make it suitable for summarization tasks, such as summarizing long documents or articles.
4. **RAG Pipelines**: Its support for structured outputs and function calling makes it a good fit for RAG (Retrieval-Augmented Generation) pipelines, which involve retrieving information from a knowledge base and generating text based on that information.
5. **Streaming**: With its streaming capability, Mistral Small 4 can be used for real-time text generation and analysis applications, such as live chat or live content generation.

### Code Integration Examples with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code examples:

```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.Model("mistralai/mistral-small-2603")

# Define a function

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
