# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-29
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of natural language processing tasks with its ability to process up to 262,144 tokens in its context window and generate outputs of up to 4,096 tokens. Its capabilities include text processing, function calling, JSON mode, streaming, and structured outputs, making it a versatile tool for developers.

### Strengths and Use Cases
The main strengths of Mistral Small 4 lie in its broad range of capabilities, including text generation, coding, analysis, and summarization, among others. It is best utilized for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization. With a pricing model that charges $0.15 per 1M tokens for input and $0.6 per 1M tokens for output, it offers a cost-effective solution for many use cases. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its competence in handling complex language tasks. However, it's essential to note the knowledge cutoff of 2023-12, which might limit its ability to handle very recent information or events.

### Pricing and Cost Considerations
For developers considering integrating Mistral Small 4 into their applications, understanding the pricing model is crucial. The cost examples provided indicate that 1,000 calls with an average of 500 tokens would cost $0.375, scaling up to $3.75 for 10,000 calls and $37.5 for 100,000 calls. With no direct competitors listed, Mistral Small 4 occupies a unique position in the market, offering its set of capabilities at the specified pricing

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
Mistral Small 4, provided by Mistralai, is a standard-tier model released on 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
- **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
- **Batch API**: Batch input is also free, making it an attractive option for large-scale API calls. However, the cost savings from batch input are already factored into the provided cost examples.

#### Cost at Scale
The cost of using Mistral Small 4 at various scales is as follows:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These costs demonstrate a linear relationship with the number of API calls, indicating that the cost per call remains constant regardless of the scale.

#### Cost Calculation
To calculate the cost, we can use the following formula:
`Cost = (Number of Input Tokens / 1,000,000) * $0.15 + (Number of Output Tokens / 1,000,000) * $0.6`

For example, assuming an average of 500 input tokens and 200 output tokens per call:
- **1,000 calls**: `(500,000 / 1,000,000) * $0.15 + (200,

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
Mistral Small 4, provided by Mistralai, is a standard-tier model released on 2024-01-01. It is not open-source and has specific pricing for input and output tokens.

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
Mistral Small 4 has the following benchmark scores:
- **MMLU: 80.0** - This score indicates the model's performance on a specific set of tasks, with higher scores generally representing better performance. An MMLU score of 80.0 suggests that Mistral Small 4 has a good level of competence in understanding and generating human-like text.
- **HumanEval: None** - HumanEval is a benchmark that evaluates a model's ability to generate correct code. The absence of a HumanEval score for Mistral Small 4 means that its coding capabilities, while listed as a capability, are not quantitatively measured by this benchmark.
- **LMSYS Arena ELO: 1200** - The LMSYS Arena ELO score is a measure of a model's performance in a competitive setting, with higher scores indicating better performance

## Competitor Comparison
### Mistral Small 4 Comparison
Since there are no direct competitors listed for the Mistral Small 4 model, we will provide a general overview of its features, pricing, and performance. This will help users understand when to choose this model and what trade-offs to expect.

#### Model Overview
The Mistral Small 4 model is a standard, non-open-source model provided by Mistralai, released on January 1, 2024. Its key features include:

* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12
* **Capabilities**: text, function_calling, json_mode, streaming, structured_outputs
* **Best For**: chat, text_generation, coding, analysis, rag_pipelines, summarization

#### Pricing
The pricing for the Mistral Small 4 model is as follows:

* **Input**: $0.15 per 1M tokens
* **Output**: $0.6 per 1M tokens
* **Cached Input**: $None per 1M tokens
* **Batch Input**: $None per 1M tokens

#### Cost Examples
To help estimate costs, here are some examples:

* **1,000 calls (avg 500 tokens)**: $0.375
* **10,000 calls**: $3.75
* **100,000 calls**: $37.5

#### Performance
The Mistral Small 4 model has the following benchmark scores:

* **MMLU**: 80.0
* **LMSYS Arena ELO**: 1200

Note that HumanEval and GSM8K benchmark scores are not available.

#### Choosing the Mistral Small 4 Model
Given the lack of direct competitors, the Mistral Small 4 model can be considered for tasks that require:

* A large context window (262,144 tokens)
* A moderate maximum output length (4,096 tokens)
* Support for various capabilities such as text, function_calling, json_mode, streaming, and structured_outputs
* A standard, non-open-source model with a knowledge cutoff of 2023-12

Users should evaluate the Mistral Small 4 model based on their specific use cases and requirements, considering the pricing, performance, and capabilities of the model. If the model's features and pricing align with their needs, it may be a suitable choice for tasks such as chat

## Best Use Cases
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on 2024-01-01, this model is classified as a standard, non-open source model.

### Pricing Model
The pricing for Mistral: Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

### Top 5 Best Use Cases for Mistral: Mistral Small 4
Based on its capabilities, here are the top 5 best use cases for Mistral: Mistral Small 4:

1. **Chat and Text Generation**: With its ability to generate human-like text, Mistral: Mistral Small 4 is well-suited for chat applications and text generation tasks.
2. **Coding and Analysis**: The model's function calling and structured outputs capabilities make it a good fit for coding and analysis tasks, such as code completion and data analysis.
3. **Summarization**: Mistral: Mistral Small 4's ability to generate concise and accurate summaries makes it a good choice for summarization tasks.
4. **RAG Pipelines**: The model's support for Retrieval-Augmented Generation (RAG) pipelines makes it a good fit for tasks that require generating text based on external knowledge sources.
5. **Streaming**: With its streaming capability, Mistral: Mistral Small 4 can be used for real-time text generation and analysis tasks.

### Code Integration Example with OpenRouter
Here is an example of how to integrate Mistral: Mistral Small 4 with OpenRouter:
```python
import openrouter

# Initialize the Mistral:

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
