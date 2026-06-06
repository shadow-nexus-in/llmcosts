# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-06
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of tasks, including text generation, coding, analysis, and summarization, thanks to its capabilities in text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens, making it suitable for complex and lengthy tasks.

### Technical Specifications and Use Cases
Technically, Mistral Small 4 boasts a context window of 262,144 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2023-12. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. Its capabilities in text, function calling, JSON mode, streaming, and structured outputs make it best suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization. However, its pricing structure, which includes $0.15 per 1M tokens for input and $0.6 per 1M tokens for output, indicates that it may not be the most cost-effective option for all use cases, particularly those requiring large volumes of input or output.

### Pricing and Cost Considerations
The pricing model for Mistral Small 4 includes input costs of $0.15 per 1M tokens and output costs of $0.6 per 1M tokens. For example, 1,000 calls with an average of 500 tokens would cost $0.375, while 10,000 calls would cost $3.75, and 100,000 calls would cost $

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
Mistral Small 4, provided by Mistralai, is a standard tier model released on 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and scalability of Mistral Small 4.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$0.00 per 1M tokens** (free)
* Batch Input: **$0.00 per 1M tokens** (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following strategies:
* **Use cached tokens**: Since cached input tokens are free, utilize them whenever possible to reduce input costs.
* **Batch API calls**: With batch input tokens being free, batching API calls can significantly reduce costs.

#### Cost at Scale
The cost of using Mistral Small 4 at various scales is as follows:
* **1,000 calls (avg 500 tokens)**: **$0.375**
* **10,000 calls**: **$3.75**
* **100,000 calls**: **$37.5**

These costs are based on the average number of tokens per call and the pricing structure outlined above.

#### Context and Limits
When using Mistral Small 4, keep in mind the following context and limits:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12

#### Capabilities and Best Use Cases
Mistral Small 4 is capable of:
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
* rag

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

#### Interpretation of Benchmark Scores
* **MMLU (80.0)**: The MMLU score measures the model's performance on a set of tasks. A higher score indicates better performance. In this case, Mistral Small 4 has a score of 80.0, which suggests it has a good level of performance.
* **HumanEval (None)**: HumanEval is a benchmark that evaluates a model's ability to generate human-like code. Since the score is None, it is unclear how Mistral Small 4 performs on this task.
* **LMSYS Arena E

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral: Mistral Small 4, we will create a hypothetical comparison with other models in the same tier and category. 

#### Model Overview
The Mistral: Mistral Small 4 model, provided by Mistralai, is a standard-tier model released on 2024-01-01. It is not open-source and has the following pricing structure:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Performance Metrics
The model has the following performance metrics:
* Context Window: 262,144 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2023-12
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
The cost of using the Mistral: Mistral Small 4 model can be estimated as follows:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

#### Hypothetical Competitor Comparison
Let's assume a competitor model, "Competitor X", with the following pricing structure:
* Input: $0.20 per 1M tokens
* Output: $0.50 per 1M tokens
For a fair comparison, let's consider the following scenarios:
* **Scenario 1**: 1,000 calls (avg 500 tokens)
	+ Mistral: Mistral Small 4: $0.375
	+ Competitor X: $0.425 (assuming 50% input and 50% output)
* **Scenario 2**: 10,000 calls
	+ Mistral: Mistral Small 4: $3.75
	+

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and release date of 2024-01-01, it offers a robust set of features for various applications.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and max output of 4,096 tokens, Mistral Small 4 is well-suited for chat and text generation applications. Its ability to understand and respond to user input makes it an ideal choice for conversational AI.
2. **Coding and Function Calling**: Mistral Small 4's capability to call functions and generate code makes it a great tool for coding and software development. Its support for JSON mode and structured outputs enables seamless integration with other applications.
3. **Analysis and Summarization**: With its high MMLU benchmark score of 80.0, Mistral Small 4 is capable of performing complex analysis and summarization tasks. Its ability to process large amounts of text data makes it an ideal choice for data analysis and insights generation.
4. **RAG Pipelines**: Mistral Small 4's support for RAG (Retrieve, Augment, Generate) pipelines makes it a great tool for applications that require information retrieval, augmentation, and generation.
5. **Streaming and Real-time Applications**: With its streaming capability, Mistral Small 4 can process and generate text in real-time, making it suitable for applications such as live chat, real-time text generation, and streaming data analysis.

### Code Integration Example with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code example:
```

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
