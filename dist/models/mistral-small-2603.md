# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-13
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral: Mistral Small 4 is designed to handle a wide range of natural language processing tasks with its ability to process up to 262,144 tokens in its context window and generate outputs of up to 4,096 tokens. Its capabilities include text processing, function calling, JSON mode, streaming, and structured outputs.

### Strengths and Use Cases
The main strengths of Mistral: Mistral Small 4 lie in its versatility and performance across various tasks. With a context window of 262,144 tokens and a maximum output of 4,096 tokens, it is well-suited for applications requiring in-depth text analysis and generation. Its primary use cases include chat, text generation, coding, analysis, RAG pipelines, and summarization. The model's performance is further underscored by its benchmarks, such as an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. However, it's essential to note the knowledge cutoff of 2023-12, indicating that the model's training data does not include information beyond this date.

### Pricing and Cost Considerations
The pricing for Mistral: Mistral Small 4 is structured around input and output tokens. Developers are charged $0.15 per 1M input tokens and $0.6 per 1M output tokens. There are no charges for cached input or batch input. To illustrate the cost implications, 1,000 calls with an average of 500 tokens would cost $0.375, while 10,000 calls would amount to $3.75, and 100,000 calls would total $37.5. Understanding these pricing dynamics is crucial for developers

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
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$0.00 per 1M tokens** (free)
* Batch Input: **$0.00 per 1M tokens** (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following scenarios:
* **Cached Tokens**: Utilize cached input tokens whenever possible, as they are **free**. This is ideal for applications with repetitive or similar input patterns.
* **Batch API Calls**: Leverage batch input to reduce costs, as batch input is also **free**. This is suitable for applications that can process multiple inputs simultaneously.

#### Cost at Scale
The cost of using Mistral Small 4 at various scales is as follows:
* **1,000 API calls** (avg 500 tokens): **$0.375**
* **10,000 API calls**: **$3.75**
* **100,000 API calls**: **$37.5**

These costs demonstrate a linear scaling of expenses with the number of API calls. To put this into perspective, the cost per 1,000 API calls remains constant at **$0.375**, indicating no economies of scale based on the provided pricing structure.

#### Conclusion
Mistral Small 4 offers a competitive pricing model, especially when leveraging cached input tokens and batch API calls. However, the costs scale linearly with the number of API calls, and there are no direct competitors listed for comparison. As with any cloud-based

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
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. It is not open source.

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
The benchmark performance of Mistral Small 4 is:
* MMLU: **80.0**
* HumanEval: **None**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

The MMLU score of 80.0 indicates the model's ability to understand and process natural language. A higher MMLU score generally corresponds to better language understanding capabilities.

The LMSYS Arena ELO score of 1200 is a measure of the model's performance in a competitive environment, where it is pitted against other models. A higher ELO score indicates better performance.

The lack of HumanEval and GSM8K scores limits the understanding of the model's capabilities in specific areas, such as coding and mathematical problem-solving.

#### Capabilities and Use Cases
Mistral Small 4 supports the following capabilities:
* text
* function_calling
*

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral: Mistral Small 4, we will provide a general comparison framework that can be applied to other models in the market. This will help in understanding the trade-offs and making informed decisions.

#### Pricing Comparison
Mistral: Mistral Small 4 pricing is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

To compare, we would need the pricing of competitor models. However, we can discuss the general pricing strategies:
* Models with lower input prices might be more suitable for applications with large input sizes.
* Models with lower output prices might be more suitable for applications with large output sizes.
* Models with cached input or batch input pricing might offer discounts for specific use cases.

#### Performance Trade-offs
Mistral: Mistral Small 4 has the following performance metrics:
* MMLU: 80.0
* LMSYS Arena ELO: 1200
* Context Window: 262,144 tokens
* Max Output: 4,096 tokens

When comparing with competitor models, consider the following:
* Models with higher MMLU scores might perform better on certain tasks but might be more expensive.
* Models with higher LMSYS Arena ELO scores might perform better in competitive scenarios.
* Models with larger context windows might be more suitable for tasks that require longer input sequences.
* Models with larger max output sizes might be more suitable for tasks that require longer output sequences.

#### Capabilities and Use Cases
Mistral: Mistral Small 4 has the following capabilities:
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

When choosing a model, consider the specific capabilities and use cases required for your application.

#### Cost Examples
Mistral: Mistral Small 4 cost examples are as follows:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

When comparing with

## Best Use Cases
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4 is a standard, non-open-source model provided by Mistralai, released on 2024-01-01. This model excels in various tasks, including chat, text generation, coding, analysis, and summarization.

### Top 5 Best Use Cases for Mistral: Mistral Small 4
Based on its capabilities, here are the top 5 best use cases for Mistral: Mistral Small 4:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and ability to generate up to 4,096 tokens, Mistral: Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Function Calling**: The model's support for function calling and structured outputs makes it an excellent choice for coding tasks, such as code completion and code generation.
3. **Analysis and Summarization**: Mistral: Mistral Small 4's capabilities in analysis and summarization make it a great fit for tasks like text summarization, sentiment analysis, and data analysis.
4. **RAG Pipelines**: The model's support for Retrieval-Augmented Generation (RAG) pipelines enables it to perform well in tasks that require combining retrieval and generation capabilities.
5. **Streaming and JSON Mode**: Mistral: Mistral Small 4's support for streaming and JSON mode makes it suitable for real-time applications and tasks that require processing JSON data.

### Code Integration Examples with OpenRouter
To integrate Mistral: Mistral Small 4 with OpenRouter, you can use the following code examples:
```python
import openrouter

# Initialize the OpenRouter client
client = openrouter.Client("mistralai/mistral-small-2603")

# Define a function to generate text using Mistral: Mistral Small 4
def generate_text(prompt):
    response = client.generate

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
