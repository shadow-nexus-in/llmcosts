# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-18
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. The architecture of Mistral Small 4 is designed to handle a wide range of natural language processing tasks with its context window of 262,144 tokens and a maximum output of 4,096 tokens. Its knowledge cutoff is 2023-12, indicating that its training data includes information up to December 2023.

### Strengths and Use Cases
The main strengths of Mistral: Mistral Small 4 include its capabilities in text generation, function calling, JSON mode, streaming, and structured outputs. It is best suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization. With a pricing model of $0.15 per 1M tokens for input and $0.6 per 1M tokens for output, it offers a cost-effective solution for developers. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO score of 1200, demonstrating its competence in various linguistic tasks. However, its limitations and areas where it is not recommended are not specified, suggesting a broad applicability.

### Technical Specifications and Cost
Technically, Mistral: Mistral Small 4 is specified with a context window that allows for complex and lengthy input sequences, making it suitable for tasks that require understanding and generating long pieces of text. The pricing examples provided indicate that the cost scales linearly with the number of calls, with 1,000 calls (averaging 500 tokens) costing $0.375, 10,000 calls costing $3.75, and 100,000 calls costing $37.5. This linear pricing model simplifies budgeting for developers. Without direct competitors listed,

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
Mistral Small 4, provided by Mistralai, is a standard, non-open-source model released on 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

This indicates that using cached input and batch input can significantly reduce costs, as they are provided at no additional charge.

#### When to Use Cached Tokens
Cached tokens should be utilized whenever possible, as they are free. This is particularly beneficial for applications where the same input is processed multiple times, such as in chatbots or text analysis pipelines. By leveraging cached tokens, users can avoid incurring the $0.15 per 1M tokens input cost.

#### Batch API Savings
Batching API calls can also lead to cost savings, as batch input is free. This is advantageous for use cases where multiple inputs can be processed together, such as in data analysis or coding applications. By batching inputs, users can minimize the number of paid input tokens.

#### Cost at Scale
The cost of using Mistral Small 4 at scale is as follows:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These costs demonstrate a linear relationship between the number of API calls and the total cost. This suggests that the cost per call remains constant, regardless of the scale.

#### Conclusion
Mistral Small 4 offers a cost-effective solution for text

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Benchmark Analysis
#### Overview
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. It is not open-source and has a specific pricing structure for input and output tokens.

#### Pricing Structure
The pricing for Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: $None per 1M tokens
- **Batch Input**: $None per 1M tokens

#### Context and Limits
The model has the following context and limits:
- **Context Window**: 262,144 tokens
- **Max Output**: 4,096 tokens
- **Knowledge Cutoff**: 2023-12

#### Benchmark Performance
The benchmark performance of Mistral Small 4 is measured by the following scores:
- **MMLU**: 80.0
  - The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to perform a wide range of natural language processing tasks. A higher MMLU score indicates better performance. With a score of 80.0, Mistral Small 4 demonstrates strong language understanding capabilities.
- **HumanEval**: None
  - HumanEval is a benchmark that assesses a model's ability to generate code that passes human-written unit tests. The absence of a HumanEval score for Mistral Small 4 means its coding capabilities are not evaluated in this context.
- **LMSYS Arena ELO**: 1200
  - The LMSYS Arena ELO score is

## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral Small 4, we will provide a general analysis of its features, pricing, and performance. This will help users understand when to choose Mistral Small 4 and what trade-offs to expect.

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

#### Choosing Mistral Small 4
Since there are no direct competitors listed, users should consider the following factors when deciding whether to use Mistral Small 4:
* **Performance requirements:** If your application requires a high context window (262,144 tokens) and moderate output size (4,096 tokens), Mistral Small 4 may be a good choice.
* **Budget constraints:** If your budget is limited, you may want to consider the cost examples provided above and estimate the total cost of using Mistral Small

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and release date of 2024-01-01, it offers a robust set of features for various applications. This guide will explore the top 5 best use cases for Mistral Small 4, along with code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, the top 5 use cases for Mistral Small 4 are:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and ability to generate up to 4,096 output tokens, Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: Mistral Small 4's function calling and structured outputs capabilities make it an excellent choice for coding and analysis tasks, such as code completion and data analysis.
3. **Summarization**: The model's ability to process large amounts of text and generate concise summaries makes it a good fit for summarization tasks.
4. **RAG Pipelines**: Mistral Small 4's support for RAG (Retrieve, Augment, Generate) pipelines enables it to be used in applications that require retrieving and augmenting knowledge from external sources.
5. **Streaming**: With its streaming capability, Mistral Small 4 can be used in real-time applications, such as live chat or text generation.

### Code Integration Examples with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code examples:

```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.Model("mistralai/mistral-small-2603")

# Define a function to generate text using the model
def generate

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
