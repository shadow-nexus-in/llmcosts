# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-27
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a context window of up to 262,144 tokens and can generate output of up to 4,096 tokens. Its knowledge cutoff is 2023-12, indicating that its training data includes information up to December 2023.

### Strengths and Use Cases
The main strengths of Mistral Small 4 include its capabilities in text generation, function calling, JSON mode, streaming, and structured outputs. These capabilities make it well-suited for a variety of applications, including chat, text generation, coding, analysis, RAG pipelines, and summarization. With a pricing model that charges $0.15 per 1M tokens for input and $0.6 per 1M tokens for output, developers can estimate costs based on their specific use cases. For example, 1,000 calls with an average of 500 tokens would cost $0.375, while 10,000 calls would cost $3.75, and 100,000 calls would cost $37.5.

### Technical Benchmarks and Competitors
Mistral Small 4 has been benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO score of 1200. While there are no direct competitors listed for this model, its unique combination of capabilities and pricing make it an attractive option for developers working on applications that require advanced language processing. With its high context window and output limits, Mistral Small 4 is particularly well-suited for applications that require generating long-form text or handling complex input sequences. However, its limitations and lack of open-source availability may make it less appealing to developers who require more transparency or customization in their language models.

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
Mistral Small 4, provided by Mistralai, is a standard, non-open-source model released on January 1, 2024. This analysis will delve into the cost structure, usage scenarios, and scalability of this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: No charge ($None per 1M tokens)
- **Batch Input**: No charge ($None per 1M tokens)

#### Usage Scenarios
- **Cached Tokens**: Since there is no charge for cached input tokens, it is highly beneficial to use cached tokens whenever possible. This can significantly reduce costs, especially in applications where the same or similar inputs are processed multiple times.
- **Batch API Savings**: Although there is no direct charge for batch input, optimizing API calls by batching can reduce the overall number of calls, thereby saving on input and output costs. This approach is particularly useful for applications that can process data in batches.

#### Cost at Scale
The cost examples provided give insight into the scalability of Mistral Small 4:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These examples indicate a linear scaling of costs with the number of API calls, which is consistent with the pricing structure based on input and output tokens.

#### Calculating Costs
To estimate costs for specific use cases, consider the average number of tokens per call and the total number of calls. Given the pricing, for every 1 million input tokens, the cost is $0.15, and for every 1 million output tokens, the cost is $0.6. 

For instance, if

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Mistral Small 4 Benchmark Performance
#### Model Overview
The Mistral Small 4 model, provided by Mistralai, is a standard-tier model released on 2024-01-01. It is not open-source.

#### Pricing
The pricing for Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Context and Limits
The model has the following context and limits:
* Context Window: 262,144 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2023-12

#### Benchmarks
The benchmark performance of Mistral Small 4 is:
* MMLU: 80.0
* HumanEval: None
* LMSYS Arena ELO: 1200
* GSM8K: None

The MMLU score of 80.0 indicates the model's performance on a set of mathematical and logical tasks. A higher MMLU score generally indicates better performance on these tasks.

The LMSYS Arena ELO score of 1200 is a measure of the model's overall performance in a competitive setting. ELO scores are used to rank models based on their performance, with higher scores indicating better performance.

The lack of HumanEval and GSM8K scores means that the model's performance on these specific benchmarks is unknown.

#### Capabilities and Use Cases
Mistral Small 4 has the following capabilities:
* text
* function_calling
* json_mode
* streaming


## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral Small 4 model, we will provide a general comparison framework that can be applied to other models in the market. This framework will cover price differences, performance trade-offs, and scenarios where one might choose the Mistral Small 4 over other models.

#### Pricing Comparison
The Mistral Small 4 is priced as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens

To compare, let's consider a hypothetical competitor model, "Competitor X", with the following pricing:
- Input: $0.20 per 1M tokens
- Output: $0.50 per 1M tokens

| Model | Input Price per 1M Tokens | Output Price per 1M Tokens |
| --- | --- | --- |
| Mistral Small 4 | $0.15 | $0.60 |
| Competitor X | $0.20 | $0.50 |

#### Performance Trade-offs
The performance of the Mistral Small 4 is benchmarked as follows:
- MMLU: 80.0
- LMSYS Arena ELO: 1200

When comparing with Competitor X, assume it has the following benchmarks:
- MMLU: 85.0
- LMSYS Arena ELO: 1100

| Model | MMLU | LMSYS Arena ELO |
| --- | --- | --- |
| Mistral Small 4 | 80.0 | 1200 |
| Competitor X | 85.0 | 1100 |

#### Choosing the Right Model
The choice between the Mistral Small 4 and a competitor like Competitor X depends on several factors:

1. **Budget**: If cost is a significant concern, the Mistral Small 4 might be more attractive due to its lower input price. However, the output price is higher, so the overall cost depends on the specific use case and the ratio of input to output tokens.
2. **Performance Requirements**: If a higher MMLU score is crucial, Competitor X might be preferable. However, if the application requires a higher LMSYS Arena ELO score, the Mistral Small 4 could be the better choice.
3. **Capabilities and Limits**: Consider the context window, max output, and knowledge

## Best Use Cases
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a powerful language model released on 2024-01-01. With its standard tier and closed-source model, it offers a unique set of capabilities that make it suitable for various applications. This guide will explore the top 5 best use cases for Mistral: Mistral Small 4, along with code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral: Mistral Small 4
Based on its capabilities, the following are the top 5 use cases for Mistral: Mistral Small 4:

1. **Chat and Text Generation**: With its ability to handle text and generate human-like responses, Mistral: Mistral Small 4 is ideal for chatbots and text generation applications.
2. **Coding and Function Calling**: The model's capability to perform function calling and handle JSON mode makes it suitable for coding and software development tasks.
3. **Analysis and Summarization**: Mistral: Mistral Small 4 can be used for analysis and summarization tasks, such as extracting key points from large documents or summarizing long pieces of text.
4. **RAG Pipelines**: The model's ability to handle structured outputs and streaming makes it a good fit for RAG (Retrieve, Augment, Generate) pipelines.
5. **Content Creation**: With its text generation capabilities, Mistral: Mistral Small 4 can be used for content creation tasks, such as generating articles, blog posts, or social media content.

### Code Integration Examples with OpenRouter
To integrate Mistral: Mistral Small 4 with OpenRouter, you can use the following code examples:

```python
import openrouter

# Initialize the Mistral: Mistral Small 4 model
model = openrouter.Model("mistralai/mistral-small-2603")

# Define a function to generate text


## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
