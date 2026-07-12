# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-12
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of tasks, including text generation, function calling, and structured outputs. Its capabilities extend to chat, text generation, coding, analysis, and summarization, making it a versatile tool for developers.

### Technical Specifications and Strengths
Technically, Mistral Small 4 boasts a context window of 262,144 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2023-12. The model's pricing is structured around input and output costs, with $0.15 per 1M tokens for input and $0.6 per 1M tokens for output. Benchmarks show an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its performance capabilities. The model's strengths lie in its ability to handle complex tasks such as function calling and streaming, alongside its support for JSON mode and structured outputs.

### Use Cases and Cost Considerations
Mistral Small 4 is best utilized for applications such as chat, text generation, coding, analysis, and summarization. However, its suitability for other tasks not listed in its capabilities should be carefully evaluated. Cost-wise, developers can expect to pay $0.375 for 1,000 calls averaging 500 tokens, scaling up to $37.5 for 100,000 calls. With no direct competitors listed, Mistral Small 4 occupies a unique space in the market, offering a blend of functionality and performance that can be leveraged by developers for a wide range of applications. Its pricing model, based on input and output tokens, provides a clear and predictable cost structure for integration into various projects.

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.15 |
| Output | $0.6 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Mistral Small 4
#### Overview
Mistral Small 4, provided by Mistralai, is a standard tier model with a release date of 2024-01-01. It is not open source.

#### Cost Structure
The cost structure for Mistral Small 4 is as follows:
* **Input**: $0.15 per 1M tokens
* **Output**: $0.6 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs. Since cached input tokens are free, it is recommended to use them whenever possible to minimize input costs.

#### Batch API Savings
Batch input is also free, which means that making batch API calls can help reduce costs by minimizing the number of API calls required.

#### Cost at Scale
The cost of using Mistral Small 4 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: $0.375
* **10,000 calls**: $3.75
* **100,000 calls**: $37.5

These costs are based on the average number of tokens per call and the input and output costs per 1M tokens.

#### Cost Calculation
To calculate the cost of using Mistral Small 4, you can use the following formula:
Cost = (Number of Input Tokens / 1,000,000) \* $0.15 + (Number of Output Tokens / 1,000,000) \* $0.6

For example, if you make 1,000 calls with an average of 500 input tokens and 200 output tokens per call, the total cost would be:
Cost = (500,000 / 1,000,000) \* $0.15 + (200,

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Benchmark Analysis
#### Model Overview
The Mistral Small 4 model, provided by Mistralai, is a standard-tier model released on 2024-01-01. It is not open-source.

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
The benchmark performance of Mistral Small 4 is:
* MMLU: **80.0**
* HumanEval: **None**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

The MMLU score of 80.0 indicates the model's performance on a set of tasks, with higher scores representing better performance. The LMSYS Arena ELO score of 1200 is a measure of the model's competitive performance, with higher scores indicating better performance relative to other models.

#### Capabilities and Use Cases
Mistral Small 4 supports the following capabilities:
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
The estimated

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
To illustrate the cost of using the Mistral Small 4 model, consider the following examples:

* **1,000 calls (avg 500 tokens)**: $0.375
* **10,000 calls**: $3.75
* **100,000 calls**: $37.5

#### Performance
The Mistral Small 4 model has the following benchmark scores:

* **MMLU**: 80.0
* **LMSYS Arena ELO**: 1200

Note that HumanEval and GSM8K benchmark scores are not available for this model.

#### Choosing the Mistral Small 4 Model
Given the lack of direct competitors, the Mistral Small 4 model can be considered for a wide range of applications, including:

* Chat and text generation
* Coding and analysis
* RAG pipelines and summarization

However, users should be aware of the model's limitations, including its context window and max output size. Additionally, the model's knowledge cutoff date is 2023-12, which may impact its performance on tasks that require more recent knowledge.

In summary, the Mistral Small 4 model offers a unique set of features and capabilities, and its pricing is competitive. While there are no direct competitors to compare it

## Best Use Cases
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on 2024-01-01, this model is part of the standard tier and is not open-source.

### Pricing Model
The pricing for Mistral: Mistral Small 4 is based on input and output tokens. The costs are as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens
With no costs for cached input or batch input.

### Top 5 Best Use Cases for Mistral: Mistral Small 4
Given its capabilities, here are the top 5 best use cases for Mistral: Mistral Small 4:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and ability to generate up to 4,096 tokens of output, Mistral: Mistral Small 4 is ideal for chat applications and text generation tasks.
2. **Coding and Analysis**: The model's function calling capability and support for structured outputs make it suitable for coding tasks and data analysis.
3. **Summarization**: Mistral: Mistral Small 4 can effectively summarize long pieces of text into concise, meaningful summaries, leveraging its text generation capabilities.
4. **RAG Pipelines**: The model's ability to handle complex, structured data and its support for streaming make it a good fit for RAG (Retrieval-Augmented Generation) pipelines.
5. **OpenRouter Integration**: For tasks that require routing or integrating with other services, Mistral: Mistral Small 4 can be used in conjunction with OpenRouter. Here's an example of how you might integrate Mistral: Mistral Small 4 with OpenRouter for a simple text generation task:
```python
import

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
