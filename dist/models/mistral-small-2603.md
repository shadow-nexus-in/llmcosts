# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-24
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open-source. From an architectural standpoint, Mistral: Mistral Small 4 is designed to handle a wide range of natural language processing tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens, making it suitable for complex and lengthy tasks.

### Technical Specifications and Use Cases
The model's technical specifications highlight its robustness, with a context window of 262,144 tokens and a maximum output of 4,096 tokens. The knowledge cutoff is dated 2023-12, indicating that the model's training data is current up to that point. Mistral: Mistral Small 4 excels in various use cases such as chat, text generation, coding, analysis, RAG pipelines, and summarization, thanks to its diverse capabilities. The pricing model is based on input and output tokens, with costs set at $0.15 per 1M tokens for input and $0.6 per 1M tokens for output. This makes it a cost-effective solution for developers who need to process large volumes of text data. Benchmarks show an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, demonstrating its performance capabilities.

### Cost Considerations and Competitors
For developers considering Mistral: Mistral Small 4, the cost can be estimated based on the number of calls and average tokens per call. For example, 1,000 calls with an average of 500 tokens would cost $0.375, while 10,000 calls would amount to $3.75, and

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

#### When to Use Cached Tokens
Given that cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible. This can significantly reduce costs, especially for applications with repetitive or similar input patterns.

#### Batch API Savings
Similar to cached input tokens, batch input tokens are also free. This makes batch processing an attractive option for large-scale applications, as it can help minimize costs associated with input tokens.

#### Cost at Scale
The cost of using Mistral Small 4 at various scales is as follows:
* **1,000 API calls (avg 500 tokens)**: **$0.375**
* **10,000 API calls**: **$3.75**
* **100,000 API calls**: **$37.5**

These costs demonstrate a linear scaling of expenses with the number of API calls, indicating that the pricing model does not offer discounts for larger volumes beyond the free batch and cached input tokens.

#### Conclusion
Mistral Small 4 offers a competitive pricing model, especially when leveraging cached and batch input tokens. To minimize costs, developers should:
* Use cached input tokens for repetitive or similar input patterns
* Utilize batch processing for large-scale applications
* Optimize output token usage, as it is more expensive than input tokens

By

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Benchmark Analysis
The Mistral Small 4 model, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. It is not open-source.

#### Pricing
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
The benchmark performance of Mistral Small 4 is as follows:
* MMLU: **80.0**
* HumanEval: **None**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

The MMLU score of 80.0 indicates the model's performance on a set of mathematical and logical tasks. A higher MMLU score generally indicates better performance on these types of tasks.

The LMSYS Arena ELO score of 1200 is a measure of the model's performance in a competitive setting, where it is pitted against other models. An ELO score of 1200 is a relatively moderate score, indicating that the model is capable of holding its own against other models, but may not be the top performer.

The lack of HumanEval and GSM8K scores means that the model's performance on these specific benchmarks is unknown.

#### Cap

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral: Mistral Small 4 model, we will provide a general overview of its pricing, performance, and capabilities to help users make informed decisions.

#### Pricing
The Mistral: Mistral Small 4 model is priced as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Performance Trade-offs
The model has the following performance characteristics:
* Context Window: 262,144 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2023-12
* Benchmarks:
	+ MMLU: 80.0
	+ LMSYS Arena ELO: 1200

#### Capabilities and Use Cases
The Mistral: Mistral Small 4 model supports the following capabilities:
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
To help estimate costs, here are some examples:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

#### Choosing the Right Model
Since there are no direct competitors listed, users should consider the following factors when deciding whether to use the Mistral: Mistral Small 4 model:
* Required context window size
* Desired output length
* Specific capabilities needed (e.g., function calling, JSON mode)
* Budget constraints
* Performance requirements (e.g., MMLU, LMSYS Arena ELO scores)

In general, the Mistral: Mistral Small 4 model appears to be a capable and versatile option for a range of natural language processing tasks. However, users should carefully evaluate their specific needs and consider factors such as cost, performance, and capabilities before making a decision.

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and release date of 2024-01-01, it's an attractive option for various applications. This guide will explore the top 5 best use cases for Mistral Small 4, along with practical advice and code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, the top 5 use cases for Mistral Small 4 are:

1. **Chat and Text Generation**: With its high MMLU score of 80.0 and ability to handle large context windows (262,144 tokens), Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: Mistral Small 4's function calling and structured outputs capabilities make it an excellent choice for coding and analysis tasks, such as code completion and data analysis.
3. **Summarization**: The model's ability to handle large context windows and generate structured outputs makes it suitable for summarization tasks, such as summarizing long documents or articles.
4. **RAG Pipelines**: Mistral Small 4's support for Retrieval-Augmented Generation (RAG) pipelines enables it to be used in applications that require the retrieval of external knowledge and generation of text based on that knowledge.
5. **Streaming**: With its streaming capability, Mistral Small 4 can be used in real-time applications, such as live chat or streaming text generation.

### Code Integration Examples with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following example code:
```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.Model("mistralai/mistral-small-2603")



## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
