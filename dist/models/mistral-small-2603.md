# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-30
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open-source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of tasks, including but not limited to text generation, coding, analysis, and summarization. Its capabilities extend to function calling, JSON mode, streaming, and structured outputs, making it a versatile tool for developers.

### Technical Specifications and Strengths
Technically, Mistral Small 4 boasts a context window of 262,144 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2023-12. The model's pricing is structured around input and output tokens, with costs of $0.15 per 1M tokens for input and $0.6 per 1M tokens for output. Benchmarks show an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its performance capabilities. The model's strengths lie in its ability to handle chat, text generation, coding, analysis, and other tasks efficiently, thanks to its listed capabilities such as text, function calling, and structured outputs.

### Use Cases and Cost Considerations
Mistral Small 4 is best utilized for applications involving chat, text generation, coding, analysis, and summarization, among others. However, its limitations and areas where it is "not good for" are not specified. In terms of cost, examples provided show that 1,000 calls (averaging 500 tokens) would cost $0.375, scaling up to $3.75 for 10,000 calls and $37.5 for 100,000 calls. With no direct competitors listed, Mistral Small 4 presents a unique offering in the market, especially for developers looking for a model with its specific set of capabilities

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
Mistral: Mistral Small 4, provided by Mistralai, is a standard, non-open-source model released on January 1, 2024. This analysis will delve into its cost structure, highlighting when to utilize cached tokens, batch API savings, and the cost at scale for 1,000, 10,000, and 100,000 API calls.

#### Cost Structure
The pricing for Mistral: Mistral Small 4 is as follows:
- **Input**: $0.15 per 1 million tokens
- **Output**: $0.6 per 1 million tokens
- **Cached Input**: No charge ($None per 1 million tokens)
- **Batch Input**: No charge ($None per 1 million tokens)

This structure indicates that the primary costs are associated with input and output token processing. Cached and batch inputs are not charged, suggesting that optimizing for these can significantly reduce costs.

#### When to Use Cached Tokens
Given that cached input tokens incur no charge, it's beneficial to use cached tokens whenever possible. This is particularly advantageous in scenarios where the same input data is processed multiple times, as it eliminates the need for repeated input token processing charges.

#### Batch API Savings
Although the pricing does not specify a direct discount for batch inputs, the fact that batch inputs are not charged suggests that processing inputs in batches can lead to significant savings. This is because the cost is primarily based on the number of input and output tokens, not the number of API calls. Therefore, batching can help in reducing the overall number of tokens processed, thereby reducing costs.

#### Cost at Scale
The provided cost examples give insight into the cost at scale:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These examples

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
The Mistral Small 4 model, provided by Mistralai, is a standard-tier language model with a release date of 2024-01-01. It is not open-source and has a specific pricing structure based on input and output tokens.

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

#### Benchmarks
The model's performance is measured by the following benchmarks:
* **MMLU: 80.0** - The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to perform a wide range of natural language processing tasks. A higher MMLU score indicates better performance.
* **HumanEval: None** - HumanEval is a benchmark that measures a model's ability to generate code that passes unit tests. The lack of a HumanEval score for Mistral Small 4 makes it difficult to assess its coding capabilities directly.
* **LMSYS Arena ELO: 1200** - The LMSYS Arena ELO score is a measure of a model's performance in a competitive arena, where models are pitted against each other to complete tasks. An ELO score of 1200 is

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
* text
* function_calling
* json_mode
* streaming
* structured_outputs

It is best suited for:
* chat
* text_generation
* coding
* analysis
* rag_pipelines
* summarization

#### Cost Examples
The estimated costs for using Mistral Small 4 are:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

### Choosing Mistral Small 4
Since there are no direct competitors listed, the decision to choose Mistral Small 4 depends on the specific requirements of your project. Consider the following factors:
* **Context Window:** If your application requires a large context window, Mistral Small 4 may be a good choice with its 262,144 token limit.
* **Output Length:** If your application requires longer output sequences, Mistral Small 4's 4,096 token limit may be sufficient.
* **P

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on January 1, 2024, this model is part of the standard tier and is not open source. In this guide, we will explore the top 5 best use cases for Mistral Small 4, along with practical advice and code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Small 4
Based on the capabilities and benchmarks of Mistral Small 4, the following are the top 5 use cases for this model:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and ability to generate up to 4,096 tokens of output, Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: The model's function calling and structured outputs capabilities make it a good fit for coding and analysis tasks, such as code completion and data analysis.
3. **Summarization**: Mistral Small 4's ability to generate concise and accurate summaries of large texts makes it a good choice for summarization tasks.
4. **RAG Pipelines**: The model's support for retrieval-augmented generation (RAG) pipelines makes it a good fit for applications that require the generation of text based on external knowledge sources.
5. **Content Generation**: With its high MMLU benchmark score of 80.0, Mistral Small 4 is well-suited for content generation tasks, such as generating articles, blog posts, and social media content.

### Code Integration Examples with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.Model("mistralai

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
