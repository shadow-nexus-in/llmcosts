# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-14
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open-source. From an architectural standpoint, Mistral: Mistral Small 4 is designed to handle a variety of tasks, including text generation, coding, analysis, and summarization, thanks to its capabilities in text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens.

### Technical Specifications and Use Cases
The model's technical specifications highlight its suitability for certain use cases. With a context window of 262,144 tokens and a maximum output of 4,096 tokens, Mistral: Mistral Small 4 is well-suited for applications requiring in-depth text analysis and generation, such as chat, text generation, coding, and summarization. Its performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its capabilities in understanding and generating human-like text. The model's knowledge cutoff is 2023-12, meaning it may not have information on events or developments after this date.

### Pricing and Cost Considerations
The pricing for Mistral: Mistral Small 4 is structured around input and output tokens. The cost is $0.15 per 1M input tokens and $0.6 per 1M output tokens. For developers, estimating costs can be straightforward: for example, 1,000 calls averaging 500 tokens each would cost $0.375, while 100,000 calls would amount to $37.5. This pricing model makes it accessible for a range of applications, from small-scale text analysis to larger-scale content generation tasks. Given its capabilities and

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
Mistral Small 4, provided by Mistralai, is a standard, non-open-source model released on 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: No additional cost ($None per 1M tokens)
- **Batch Input**: No additional cost ($None per 1M tokens)

This structure indicates that the primary cost drivers are the input and output token volumes. Cached and batch inputs do not incur additional costs, suggesting potential savings through efficient input handling.

#### When to Use Cached Tokens
Given that cached input tokens do not incur additional costs, it is advisable to utilize cached tokens whenever possible. This approach can significantly reduce expenses, especially in applications where the same or similar inputs are processed repeatedly. However, the effectiveness of this strategy depends on the specific use case and the model's ability to leverage cached inputs efficiently.

#### Batch API Savings
The absence of additional costs for batch inputs implies that batching API calls can lead to cost savings by reducing the overhead associated with individual requests. This is particularly beneficial for applications that can accumulate and process inputs in batches, thereby minimizing the number of API calls required.

#### Cost at Scale
To understand the cost-effectiveness of Mistral Small 4 at scale, let's examine the provided cost examples:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These examples suggest a linear cost scaling, where the cost increases directly with the number of API calls. This linear relationship indicates that the

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
The Mistral Small 4 model, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. It is not open source.

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

The MMLU score of 80.0 indicates the model's performance on a set of mathematical and logical tasks. A higher MMLU score generally indicates better performance on these tasks.

The LMSYS Arena ELO score of 1200 is a measure of the model's overall performance in a competitive setting. A higher ELO score generally indicates better performance.

The lack of HumanEval and GSM8K scores makes it difficult to assess the model's performance on specific tasks such as coding and mathematical problem-solving.

#### Capabilities and Use Cases
Mistral Small 4 has the following capabilities:
* text
* function_calling
* json

## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral Small 4, we will provide a general comparison framework that can be applied when evaluating this model against other similar models in the market.

#### Pricing Comparison
The pricing for Mistral Small 4 is as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens

To compare, consider the pricing of other models:
| Model | Input Price per 1M Tokens | Output Price per 1M Tokens |
| --- | --- | --- |
| Mistral Small 4 | $0.15 | $0.6 |
| Competitor Model | *Insert Competitor Pricing* | *Insert Competitor Pricing* |

#### Performance Trade-offs
Mistral Small 4 has the following performance metrics:
- MMLU: 80.0
- LMSYS Arena ELO: 1200
- Context Window: 262,144 tokens
- Max Output: 4,096 tokens

When comparing with competitors, consider the trade-offs between these performance metrics and pricing. For example:
- A competitor model with higher MMLU scores may come at a higher price per token.
- A model with a larger context window may be more suitable for certain tasks but could be more expensive.

#### Choosing the Right Model
Consider the following when deciding between Mistral Small 4 and its competitors:
- **Task Requirements**: If your tasks require a large context window (up to 262,144 tokens) and can benefit from the capabilities of text, function calling, JSON mode, streaming, and structured outputs, Mistral Small 4 might be a good choice.
- **Budget Constraints**: Calculate the cost based on your expected usage. For example, 1,000 calls with an average of 500 tokens would cost $0.375 with Mistral Small 4. Compare this with the costs of competitor models.
- **Performance Needs**: Evaluate the MMLU, HumanEval, LMSYS Arena ELO, and GSM8K benchmarks of competitor models to determine which best fits your performance requirements.

### Example Use Cases for Mistral Small 4
Given its capabilities and best use cases, Mistral Small 4 is suitable for:
- Chat applications
- Text generation tasks
- Coding and analysis
- Summarization tasks
- RAG pipelines



## Best Use Cases
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on 2024-01-01, this model is part of the standard tier and is not open-source.

### Pricing Model
The pricing for Mistral: Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

### Top 5 Best Use Cases
Based on its capabilities, here are the top 5 best use cases for Mistral: Mistral Small 4:

1. **Chat and Text Generation**: With its ability to handle text and generate human-like responses, Mistral: Mistral Small 4 is ideal for chatbots and text generation applications.
2. **Coding and Analysis**: The model's function calling and structured outputs capabilities make it suitable for coding and analysis tasks, such as code completion and data analysis.
3. **Summarization**: Mistral: Mistral Small 4 can be used for summarization tasks, such as summarizing long documents or articles.
4. **RAG Pipelines**: The model's ability to handle structured outputs makes it a good fit for RAG (Retrieval-Augmented Generation) pipelines.
5. **Streaming**: With its streaming capability, Mistral: Mistral Small 4 can be used for real-time text generation and analysis applications.

### Code Integration Example with OpenRouter
Here is an example of how to integrate Mistral: Mistral Small 4 with OpenRouter:
```python
import openrouter

# Initialize the Mistral: Mistral Small 4 model
model = openrouter.Model("mistralai

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
