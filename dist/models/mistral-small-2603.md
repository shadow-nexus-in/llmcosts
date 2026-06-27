# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-27
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of natural language processing (NLP) tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens, making it suitable for complex tasks such as chat, text generation, coding, analysis, and summarization.

### Technical Specifications and Pricing
Technically, Mistral Small 4 boasts a context window of 262,144 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2023-12. The model's pricing is structured around input and output tokens, with costs of $0.15 per 1M input tokens and $0.6 per 1M output tokens. There are no specified costs for cached input or batch input. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. These specifications and pricing make Mistral Small 4 a competitive choice for developers looking to integrate advanced NLP capabilities into their applications without incurring excessive costs, as exemplified by the cost examples provided: $0.375 for 1,000 calls (avg 500 tokens), $3.75 for 10,000 calls, and $37.5 for 100,000 calls.

### Use Cases and Competitiveness
Given its capabilities and pricing structure, Mistral Small 4 is best suited for applications involving chat, text generation, coding, analysis, RAG pipelines, and summarization. It is not recommended for

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
Mistral Small 4, provided by Mistralai, is a standard-tier model released on 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
- **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
- **Batch API Savings**: Although batch input is free, the cost savings come from reducing the number of API calls. This can lead to significant cost reductions, especially for large-scale applications.

#### Cost at Scale
The cost examples provided are as follows:
- **1,000 calls** (avg 500 tokens): $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These costs can be broken down into input and output costs. Assuming an average of 500 tokens per call, the total tokens for each scenario would be:
- **1,000 calls**: 500,000 tokens
- **10,000 calls**: 5,000,000 tokens
- **100,000 calls**: 50,000,000 tokens

Using the provided pricing, we can estimate the costs:
- **Input Cost** (500,000 tokens / 1,000,000 tokens) \* $0.15 = $0.075 (for 1,000 calls)
- **Output Cost** (assuming 4,096 tokens output per

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Analysis
#### Overview
The Mistral Small 4 model, provided by Mistralai, is a standard, non-open-source model released on January 1, 2024. This analysis will delve into its benchmark performance, focusing on MMLU, HumanEval, and Arena ELO scores, to understand its real-world applications.

#### Pricing
The pricing structure for Mistral Small 4 is as follows:
- Input: **$0.15 per 1M tokens**
- Output: **$0.6 per 1M tokens**
- Cached Input: **$None per 1M tokens**
- Batch Input: **$None per 1M tokens**

#### Context and Limits
Key context and limit specifications include:
- Context Window: **262,144 tokens**
- Max Output: **4,096 tokens**
- Knowledge Cutoff: **2023-12**

#### Benchmarks
The model's performance is benchmarked as follows:
- **MMLU: 80.0** - The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to perform a wide range of natural language understanding tasks. A score of 80.0 indicates that Mistral Small 4 has a strong foundation in understanding and processing human language, making it suitable for tasks that require comprehension and generation of text.
- **HumanEval: None** - HumanEval is a benchmark that tests a model's ability to generate code based on human-written specifications. The absence of a HumanEval score for Mistral Small 4 suggests that its coding capabilities, while present, have not been formally evaluated against this specific benchmark.
- **LMSYS Arena ELO:

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral: Mistral Small 4, we will provide a general comparison framework based on the provided data. This will help in understanding how Mistral: Mistral Small 4 stands out and when it might be the preferred choice.

#### Pricing Comparison
Mistral: Mistral Small 4 pricing is as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens

Without direct competitors, we can't directly compare prices. However, these prices suggest that Mistral: Mistral Small 4 is positioned as a standard tier model, which may offer a balance between cost and performance.

#### Performance Trade-offs
Given the benchmarks:
- MMLU: 80.0
- LMSYS Arena ELO: 1200

Mistral: Mistral Small 4 demonstrates a specific level of performance. The absence of direct competitors makes it challenging to compare these metrics directly. However, the model's capabilities, such as text, function_calling, json_mode, streaming, and structured_outputs, suggest it is versatile and can be applied to various tasks like chat, text_generation, coding, analysis, rag_pipelines, and summarization.

#### When to Choose Mistral: Mistral Small 4
Based on the provided data, Mistral: Mistral Small 4 is best for:
- Chat
- Text generation
- Coding
- Analysis
- RAG pipelines
- Summarization

It is not specified what tasks Mistral: Mistral Small 4 is "NOT GOOD FOR," which could be an important consideration in choosing the right model for a specific application.

#### Cost Examples
The cost examples given are:
- 1,000 calls (avg 500 tokens): $0.375
- 10,000 calls: $3.75
- 100,000 calls: $37.5

These examples illustrate how the cost scales with the number of calls, which can help in budget planning for projects utilizing Mistral: Mistral Small 4.

### Conclusion
Mistral: Mistral Small 4, with its unique set of capabilities and pricing, occupies a distinct position in the market. While direct competitors are not listed, its performance metrics and capabilities suggest it can be a strong choice for a variety of applications, especially

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on 2024-01-01, this model is part of the standard tier and is not open-source.

### Pricing Model
The pricing for Mistral Small 4 is based on input and output tokens. The costs are as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens

### Top 5 Best Use Cases for Mistral Small 4
Given its capabilities, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its ability to handle text and generate human-like responses, Mistral Small 4 is ideal for chatbots and text generation tasks.
2. **Coding and Function Calling**: The model's capability to perform function calling makes it suitable for coding tasks, such as generating code snippets or completing partial code.
3. **Analysis and Summarization**: Mistral Small 4 can be used for analysis and summarization tasks, providing concise and accurate summaries of large texts.
4. **RAG Pipelines**: The model's support for structured outputs and json mode makes it a good fit for RAG (Retrieval-Augmented Generation) pipelines.
5. **Streaming**: With its ability to handle streaming data, Mistral Small 4 can be used for real-time text processing and generation tasks.

### Code Integration Example with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.Model("mistralai/mistral-small-2603")

# Define a function to generate text using the model
def generate_text(prompt):
   

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
