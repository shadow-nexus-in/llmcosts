# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-11
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open-source. From an architectural standpoint, Mistral: Mistral Small 4 is designed to handle a wide range of natural language processing tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens, making it suitable for complex tasks such as chat, text generation, coding, analysis, and summarization.

### Technical Specifications and Pricing
Technically, Mistral: Mistral Small 4 boasts a context window of 262,144 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2023-12. The model's pricing is structured as follows: $0.15 per 1M tokens for input, $0.6 per 1M tokens for output, with no charges for cached input or batch input. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. With capabilities such as text, function calling, and structured outputs, Mistral: Mistral Small 4 is best utilized for applications requiring in-depth text analysis and generation. The cost of using this model can be estimated with examples such as 1,000 calls averaging 500 tokens costing $0.375, 10,000 calls costing $3.75, and 100,000 calls costing $37.5.

### Use Cases and Competitors
Mistral: Mistral Small 4 is best suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization, thanks to its robust architecture

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
Mistral Small 4, provided by Mistralai, is a standard tier model released on 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

This indicates that using cached input and batch input can significantly reduce costs, as they are provided at no additional charge.

#### Optimal Usage Scenarios
- **Cached Tokens**: Since cached input is free, it is highly recommended to use cached tokens whenever possible. This can significantly reduce costs, especially for repeated queries or when dealing with a large volume of similar inputs.
- **Batch API**: Utilizing batch API calls can also lead to cost savings, as batch input is free. This is particularly beneficial when processing large datasets or making multiple requests simultaneously.

#### Cost at Scale
The cost examples provided are as follows:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These costs demonstrate a linear scaling of expenses with the number of API calls. To estimate costs for other scales, we can use the provided pricing per token and calculate based on the average tokens per call.

#### Calculating Costs
Given the average cost per call, we can infer the following:
- Average cost per token = ($0.15 + $0.6) / 2 (assuming equal input and output tokens for simplicity) = $0.375 per 1M tokens for a

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Benchmark Performance Analysis
#### Overview
The Mistral Small 4 model, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. It is not open-source and has a specific pricing structure for input and output tokens.

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

The MMLU score of 80.0 indicates the model's performance on a specific set of tasks, with higher scores representing better performance. The LMSYS Arena ELO score of 1200 provides a relative ranking of the model's performance compared to other models, with higher scores indicating better performance.

The lack of HumanEval and GSM8K scores means that the model's performance on these specific benchmarks is not available.

#### Real-World Implications
For real-world use, the benchmark scores can be interpreted as follows:
* The MMLU score of 80.0 suggests

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral: Mistral Small 4, we will provide a general overview of the model's features, pricing, and performance. This will help users understand the value proposition of Mistral: Mistral Small 4 and make informed decisions about its adoption.

#### Model Overview
Mistral: Mistral Small 4 is a standard-tier model released by Mistralai on 2024-01-01. It is not open-source and has the following key features:
* Context Window: 262,144 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2023-12
* Capabilities: text, function_calling, json_mode, streaming, structured_outputs
* Best for: chat, text_generation, coding, analysis, rag_pipelines, summarization

#### Pricing
The pricing for Mistral: Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Cost Examples
To illustrate the cost of using Mistral: Mistral Small 4, here are some examples:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

#### Performance
The performance of Mistral: Mistral Small 4 is measured by the following benchmarks:
* MMLU: 80.0
* LMSYS Arena ELO: 1200

Since there are no direct competitors listed, we cannot provide a direct comparison of Mistral: Mistral Small 4 with other models. However, we can suggest that users consider the following factors when evaluating the suitability of Mistral: Mistral Small 4 for their use case:
* Context window and max output requirements
* Required capabilities (e.g., text, function_calling, json_mode, streaming, structured_outputs)
* Budget constraints
* Performance requirements (e.g., MMLU, LMSYS Arena ELO)

By considering these factors, users can determine whether Mistral: Mistral Small 4 is the best fit for their specific needs. If not,

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and release date of 2024-01-01, it offers a robust set of features for various applications.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and max output of 4,096 tokens, Mistral Small 4 is well-suited for chat and text generation applications. Its ability to understand and respond to user input makes it an excellent choice for conversational AI.
2. **Coding and Analysis**: Mistral Small 4's function calling and structured outputs capabilities make it an ideal model for coding and analysis tasks. It can be used to generate code, analyze data, and provide insights.
3. **Summarization and RAG Pipelines**: The model's ability to process large amounts of text and generate concise summaries makes it a great fit for summarization and RAG (Retrieve, Augment, Generate) pipelines.
4. **Content Creation**: With its text generation capabilities, Mistral Small 4 can be used to create high-quality content, such as articles, blog posts, and social media posts.
5. **Language Translation and Localization**: Although not explicitly mentioned, Mistral Small 4's language understanding and generation capabilities make it a potential candidate for language translation and localization tasks.

### Code Integration Example with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.Model("mistralai/mistral-small-2603")



## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
