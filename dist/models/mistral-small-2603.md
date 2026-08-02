# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-02
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open-source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of natural language processing tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens, making it suitable for complex tasks such as chat, text generation, coding, analysis, and summarization.

### Technical Specifications and Pricing
Technically, Mistral Small 4 has a context window of 262,144 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2023-12. The model's pricing is based on input and output tokens, with costs of $0.15 per 1M tokens for input and $0.6 per 1M tokens for output. There are no specified costs for cached input or batch input. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. Given its capabilities and pricing, developers can estimate costs based on the number of calls and tokens processed, with examples including $0.375 for 1,000 calls averaging 500 tokens, $3.75 for 10,000 calls, and $37.5 for 100,000 calls.

### Use Cases and Competitors
Mistral Small 4 is best suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization, thanks to its robust capabilities and large context window. However, its limitations and areas where it is not recommended are not specified. As of the provided data, there are no direct competitors listed

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
Mistral: Mistral Small 4, provided by Mistralai, is a standard, non-open-source model released on 2024-01-01. This analysis will delve into its cost structure, highlighting when to utilize cached tokens, batch API savings, and the cost at scale for various API call volumes.

#### Cost Structure
The pricing for Mistral: Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: $None per 1M tokens (indicating no additional cost for cached input)
- **Batch Input**: $None per 1M tokens (suggesting no specific discount for batched inputs)

Given this structure, the primary cost drivers are the input and output token volumes.

#### Using Cached Tokens
Since cached input tokens incur no additional cost ($None per 1M tokens), it's highly beneficial to leverage cached tokens whenever possible. This can significantly reduce costs, especially in applications where the same or similar inputs are processed multiple times.

#### Batch API Savings
The pricing data does not specify a direct discount for batched inputs ($None per 1M tokens for batch input). However, processing inputs in batches can still offer indirect savings by reducing the overhead of individual API calls. The actual cost savings from batching would depend on the specific implementation and how the model is utilized.

#### Cost at Scale
To understand the cost implications at scale, let's examine the provided cost examples:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These examples illustrate a linear cost scaling with the number of API calls, which is consistent with the per-token pricing model. For applications requiring a

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
Mistral Small 4, provided by Mistralai, is a standard-tier model released on 2024-01-01. It is not open-source and offers a range of capabilities including text, function calling, JSON mode, streaming, and structured outputs.

#### Pricing
The pricing model for Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: $None per 1M tokens
- **Batch Input**: $None per 1M tokens

#### Context and Limits
- **Context Window**: 262,144 tokens
- **Max Output**: 4,096 tokens
- **Knowledge Cutoff**: 2023-12

#### Benchmarks
- **MMLU (Massive Multitask Language Understanding)**: 80.0
  - MMLU measures a model's ability to perform a wide range of natural language understanding tasks. A score of 80.0 indicates that Mistral Small 4 has a good level of language understanding, suitable for tasks like text generation, chat, and analysis.
- **HumanEval**: None
  - HumanEval is a benchmark that evaluates a model's ability to generate code. The absence of a score for Mistral Small 4 makes it difficult to assess its coding capabilities directly.
- **LMSYS Arena ELO**: 1200
  - LMSYS Arena ELO is a measure of a model's performance in a competitive setting, with higher scores indicating better performance. An ELO score of 1200 suggests that Mist

## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral Small 4, we will provide a general overview of the model's features, pricing, and performance. This will help users understand the value proposition of Mistral Small 4 and make informed decisions.

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

#### Performance and Capabilities
Mistral Small 4 has the following capabilities:
* **Context Window:** 262,144 tokens
* **Max Output:** 4,096 tokens
* **Knowledge Cutoff:** 2023-12
* **Capabilities:** text, function_calling, json_mode, streaming, structured_outputs
* **Best For:** chat, text_generation, coding, analysis, rag_pipelines, summarization

#### Benchmarks
The model has the following benchmark scores:
* **MMLU:** 80.0
* **LMSYS Arena ELO:** 1200

#### Cost Examples
The estimated costs for using Mistral Small 4 are:
* **1,000 calls (avg 500 tokens):** $0.375
* **10,000 calls:** $3.75
* **100,000 calls:** $37.5

#### Choosing Mistral Small 4
Given the lack of direct competitors, Mistral Small 4 can be considered for a wide range of applications, including:
* Chat and text generation
* Coding and analysis
* RAG pipelines and summarization

When choosing Mistral Small 4, consider the following factors:
* **Context Window:** If your application requires a large context window, Mistral Small 4 may be a good choice.
* **Output Requirements:** If your application requires a maximum output of 4,096 tokens, Mistral Small 4 can meet this requirement.
* **Knowledge Cutoff:** If

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and release date of 2024-01-01, it offers a robust set of features for various applications.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and max output of 4,096 tokens, Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: Its function calling and structured outputs capabilities make it an excellent choice for coding and analysis tasks, such as code completion and data analysis.
3. **Summarization**: Mistral Small 4's ability to process large amounts of text and generate concise summaries makes it a great tool for summarization tasks.
4. **RAG Pipelines**: Its support for retrieval-augmented generation (RAG) pipelines enables it to generate text based on external knowledge sources, making it suitable for applications that require incorporating external information.
5. **Streaming**: With its streaming capability, Mistral Small 4 can process and generate text in real-time, making it a good fit for applications that require live text generation, such as live chat or real-time content creation.

### Code Integration Example with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following example code:
```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.Model("mistralai/mistral-small-2603")

# Define a function to generate text using the model
def generate_text(prompt):
    input_ids = openrouter.tokenize(prompt, model)
   

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
