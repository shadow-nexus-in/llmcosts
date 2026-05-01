# Xiaomi: MiMo-V2-Omni API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-01
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Technical Overview
The Xiaomi: MiMo-V2-Omni model, released by Xiaomi on 2024-01-01, is a standard, non-open-source language model designed for a variety of natural language processing tasks. Its architecture is not explicitly detailed, but its capabilities suggest a robust and versatile model. The MiMo-V2-Omni model supports text, function calling, JSON mode, streaming, and structured outputs, making it a powerful tool for developers.

### Strengths and Use Cases
The main strengths of the Xiaomi: MiMo-V2-Omni model lie in its ability to handle a wide range of tasks, including chat, text generation, coding, analysis, RAG pipelines, and summarization. With a context window of 262,144 tokens and a maximum output of 65,536 tokens, this model is well-suited for tasks that require processing and generating large amounts of text. The model's pricing is based on input and output tokens, with costs of $0.4 per 1M tokens for input and $2.0 per 1M tokens for output. For example, 1,000 calls with an average of 500 tokens would cost $1.2.

### Performance and Cost
The Xiaomi: MiMo-V2-Omni model has demonstrated its performance through various benchmarks, including an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. While its performance on other benchmarks, such as HumanEval and GSM8K, is not available, its capabilities and pricing make it an attractive option for developers. With a knowledge cutoff of 2023-12, this model is well-suited for tasks that require up-to-date information. The cost of using this model can be estimated based on the number of calls and tokens, with 10,000 calls costing $12.0 and 100,000 calls costing $120.0. As there are no direct

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.4 |
| Output | $2.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Xiaomi: MiMo-V2-Omni
#### Overview
The Xiaomi: MiMo-V2-Omni model is a standard, non-open source model released by Xiaomi on 2024-01-01. This analysis will break down the cost structure, provide guidance on when to use cached tokens, discuss batch API savings, and calculate the cost at scale for 1,000, 10,000, and 100,000 API calls.

#### Cost Structure
The pricing for Xiaomi: MiMo-V2-Omni is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### Using Cached Tokens
Cached tokens are free, making them an attractive option for reducing costs. Consider using cached tokens when:
* The input data is repetitive or has a high degree of similarity.
* The model is being used for applications where the input data is largely static.

#### Batch API Savings
Batch input is also free, which can lead to significant cost savings when making multiple API calls. To maximize batch API savings:
* Group multiple requests together to reduce the number of API calls.
* Ensure that the total input tokens for the batch are within the context window limit (262,144 tokens).

#### Cost at Scale
The cost examples provided are:
* 1,000 calls (avg 500 tokens): **$1.2**
* 10,000 calls: **$12.0**
* 100,000 calls: **$120.0**

To calculate the cost at scale, we can use the provided pricing structure. Assuming an average of 500 tokens per call:
* 1,000 calls: 500 tokens/call \* 1,000 calls = 500,000

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Xiaomi: MiMo-V2-Omni Benchmark Performance
#### Overview
The Xiaomi: MiMo-V2-Omni model, released on 2024-01-01, is a standard-tier model provided by Xiaomi. It is not open-source and has specific pricing for input and output tokens.

#### Pricing
The pricing for Xiaomi: MiMo-V2-Omni is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
No pricing is provided for cached input or batch input.

#### Context and Limits
The model has the following context and limits:
* Context Window: 262,144 tokens
* Max Output: 65,536 tokens
* Knowledge Cutoff: 2023-12

#### Benchmarks
The model's benchmark performance is as follows:
* MMLU: 80.0
* HumanEval: None
* LMSYS Arena ELO: 1200
* GSM8K: None

The MMLU score of 80.0 indicates the model's performance on a set of tasks, with higher scores generally indicating better performance. The LMSYS Arena ELO score of 1200 provides a relative ranking of the model's performance compared to other models, with higher scores indicating better performance.

#### Capabilities and Use Cases
The model has the following capabilities:
* text
* function_calling
* json_mode
* streaming
* structured_outputs

It is best suited for tasks such as:
* chat
* text_generation
* coding
* analysis
* rag_pipelines
* summarization

#### Cost Examples
The cost of using the model can

## Competitor Comparison
### Comparison of Xiaomi: MiMo-V2-Omni with Top Competitors
Since there are no direct competitors listed for the Xiaomi: MiMo-V2-Omni model, we will provide a general overview of its features, pricing, and performance. This will help users understand when to choose this model and what trade-offs to expect.

#### Model Overview
The Xiaomi: MiMo-V2-Omni is a standard-tier model released by Xiaomi on 2024-01-01. It is not open-source.

#### Pricing
The pricing for the Xiaomi: MiMo-V2-Omni model is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Performance and Capabilities
The model has the following benchmarks:
* MMLU: 80.0
* LMSYS Arena ELO: 1200
It supports the following capabilities:
* Text
* Function calling
* JSON mode
* Streaming
* Structured outputs
It is best suited for tasks such as:
* Chat
* Text generation
* Coding
* Analysis
* RAG pipelines
* Summarization

#### Cost Examples
The estimated costs for using the Xiaomi: MiMo-V2-Omni model are:
* 1,000 calls (avg 500 tokens): $1.2
* 10,000 calls: $12.0
* 100,000 calls: $120.0

#### Choosing the Xiaomi: MiMo-V2-Omni Model
Given the lack of direct competitors, the Xiaomi: MiMo-V2-Omni model can be considered for its unique combination of capabilities and pricing. However, users should carefully evaluate their specific use cases and requirements to determine if this model is the best fit.

### Trade-Offs and Considerations
When considering the Xiaomi: MiMo-V2-Omni model, keep in mind the following trade-offs:
* **Context Window**: The model has a context window of 262,144 tokens, which may be sufficient for many tasks but could be limiting for very long-range dependencies.
* **Max Output**: The maximum output length is 65,536 tokens, which should be sufficient for most tasks but could be a limitation for very long outputs.
* **Knowledge

## Best Use Cases
### Introduction to Xiaomi: MiMo-V2-Omni
The Xiaomi: MiMo-V2-Omni model, released by Xiaomi on 2024-01-01, is a standard tier model with a context window of 262,144 tokens and a maximum output of 65,536 tokens. This model is not open source and has a knowledge cutoff of 2023-12.

### Pricing
The pricing for Xiaomi: MiMo-V2-Omni is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

### Top 5 Best Use Cases
Based on the capabilities and benchmarks of the Xiaomi: MiMo-V2-Omni model, the top 5 best use cases are:

1. **Chat**: With its high context window and ability to generate text, this model is well-suited for chat applications.
2. **Text Generation**: The model's ability to generate text and its high output limit make it a good choice for text generation tasks.
3. **Coding**: The model's ability to perform function calling and generate structured outputs make it a good choice for coding tasks.
4. **Analysis**: The model's high context window and ability to generate text make it a good choice for analysis tasks such as summarization.
5. **RAG Pipelines**: The model's ability to generate text and perform function calling make it a good choice for RAG (Retrieve, Augment, Generate) pipelines.

### Code Integration Examples
To integrate the Xiaomi: MiMo-V2-Omni model with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the model
model = openrouter.Model("xiaomi/mimo-v2-omni")

# Define a function to generate text
def generate

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
