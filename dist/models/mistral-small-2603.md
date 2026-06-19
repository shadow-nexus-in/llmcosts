# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-19
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard, non-open-source language model released on 2024-01-01. This model is part of the Mistral family and is identified as `mistralai/mistral-small-2603`. With its specific architecture, Mistral Small 4 is designed to handle a variety of tasks, including but not limited to chat, text generation, coding, analysis, and summarization. Its capabilities extend to processing text, making function calls, operating in JSON mode, supporting streaming, and producing structured outputs.

### Technical Specifications and Pricing
Technically, Mistral Small 4 boasts a context window of 262,144 tokens and can generate up to 4,096 tokens as output. The knowledge cutoff for this model is 2023-12, indicating that its training data includes information up to December 2023. In terms of pricing, developers are charged $0.15 per 1M tokens for input and $0.6 per 1M tokens for output. There are no specified charges for cached input or batch input. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, although scores for HumanEval and GSM8K are not provided. The pricing structure allows for cost-effective usage, with examples including $0.375 for 1,000 calls averaging 500 tokens, $3.75 for 10,000 calls, and $37.5 for 100,000 calls.

### Use Cases and Competitors
Given its capabilities, Mistral Small 4 is best suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization. However, specific use cases it is not good for are not detailed. Notably, there are no direct competitors listed for Mistral Small 4, suggesting

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
Mistral: Mistral Small 4, provided by Mistralai, is a standard, non-open-source model released on 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and scale-based pricing for this model.

#### Cost Structure
The pricing for Mistral: Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: No additional cost ($None per 1M tokens)
- **Batch Input**: No additional cost ($None per 1M tokens)

This structure indicates that the primary cost factors are the input and output token counts. Cached and batch inputs do not incur additional costs, suggesting that utilizing these features can lead to significant savings.

#### When to Use Cached Tokens
Given that cached input tokens do not incur any additional cost, it is highly beneficial to use cached tokens whenever possible. This is particularly advantageous in scenarios where the same input data is processed multiple times, as it eliminates the need to pay for input tokens repeatedly.

#### Batch API Savings
The absence of additional costs for batch inputs implies that processing inputs in batches does not increase the cost per token. This makes batch processing an attractive option for reducing the overall cost of API calls, as it can help minimize the overhead associated with individual API requests.

#### Cost at Scale
To understand the cost implications of using Mistral: Mistral Small 4 at different scales, let's examine the provided cost examples:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These examples demonstrate a linear increase in cost with the number of API calls, indicating that the cost scales directly with usage. This

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Benchmark Performance Analysis
The Mistral Small 4 model, provided by Mistralai, has a set of benchmark scores that indicate its performance in various tasks. Here's a breakdown of what these scores mean for real-world use:

#### MMLU Score: 80.0
The MMLU (Massive Multitask Language Understanding) score measures a model's ability to perform a wide range of natural language processing tasks. A score of 80.0 indicates that Mistral Small 4 has a strong foundation in language understanding, which is beneficial for tasks like text generation, chat, and analysis.

#### HumanEval Score: None
The HumanEval score is not available for Mistral Small 4. HumanEval is a benchmark that evaluates a model's ability to generate code that is both correct and readable. The lack of a HumanEval score makes it difficult to assess the model's coding capabilities, but its inclusion in the "BEST FOR" list suggests that it may still be suitable for coding tasks.

#### LMSYS Arena ELO Score: 1200
The LMSYS Arena ELO score is a measure of a model's performance in a competitive environment, where it is pitted against other models in a series of tasks. An ELO score of 1200 indicates that Mistral Small 4 is a mid-tier model, capable of holding its own in a variety of tasks, but may struggle against more advanced models.

### Real-World Implications
The benchmark scores suggest that Mistral Small 4 is a solid, all-around model that can handle a variety of tasks, including:

* Text generation and chat
* Coding and analysis
* Summarization and RAG

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral: Mistral Small 4 model, we will provide a general comparison framework that can be applied when evaluating this model against other similar models in the market.

#### Pricing Comparison
The Mistral: Mistral Small 4 model is priced as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens

To compare, consider the pricing of other models:
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral: Mistral Small 4 | $0.15 | $0.6 |
| Competitor Model 1 | *insert price* | *insert price* |
| Competitor Model 2 | *insert price* | *insert price* |

#### Performance Trade-offs
When comparing performance, consider the following benchmarks:
- MMLU: 80.0
- LMSYS Arena ELO: 1200
- Context Window: 262,144 tokens
- Max Output: 4,096 tokens

Other models may offer better performance in certain areas, such as:
* Higher MMLU scores for improved language understanding
* Higher LMSYS Arena ELO scores for better performance in specific tasks
* Larger context windows for handling longer input sequences
* Larger max output for generating longer responses

#### Choosing the Right Model
When deciding between the Mistral: Mistral Small 4 and other models, consider the following factors:
* **Price**: If cost is a primary concern, choose the model with the most competitive pricing for your specific use case.
* **Performance**: If high performance is required, select the model with the best benchmarks for your specific task.
* **Capabilities**: Ensure the chosen model supports the necessary capabilities, such as text, function_calling, json_mode, streaming, and structured_outputs.
* **Use Case**: Consider the best use cases for each model, such as chat, text_generation, coding, analysis, rag_pipelines, and summarization.

### Example Cost Calculations
The following cost examples are provided for the Mistral: Mistral Small 4 model:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.

## Best Use Cases
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on 2024-01-01, this model is part of the standard tier and is not open source.

### Pricing Model
The pricing for Mistral: Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

### Top 5 Best Use Cases
Based on the capabilities and limitations of Mistral: Mistral Small 4, the top 5 best use cases for this model are:

1. **Chat and Text Generation**: With its ability to generate human-like text and its large context window of 262,144 tokens, Mistral: Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: The model's function calling and structured outputs capabilities make it a good fit for coding and analysis tasks, such as code completion and data analysis.
3. **Summarization**: Mistral: Mistral Small 4's ability to generate concise and accurate summaries of large texts makes it a good choice for summarization tasks.
4. **RAG Pipelines**: The model's support for retrieval-augmented generation (RAG) pipelines makes it a good fit for applications that require the generation of text based on external knowledge sources.
5. **Streaming**: With its ability to process streaming data, Mistral: Mistral Small 4 is well-suited for real-time applications, such as live chat and text analysis.

### Code Integration Example with OpenRouter
To integrate Mistral: Mistral Small 4 with OpenRouter,

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
