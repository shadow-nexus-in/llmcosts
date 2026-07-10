# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-10
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral: Mistral Small 4 is designed to handle a variety of tasks with its robust capabilities, including text generation, function calling, JSON mode, streaming, and structured outputs. Its architecture supports a context window of up to 262,144 tokens and can generate a maximum output of 4,096 tokens.

### Strengths and Use Cases
The main strengths of Mistral: Mistral Small 4 lie in its versatility and performance. With a high context window and the ability to handle multiple input formats, it is well-suited for applications such as chat, text generation, coding, analysis, and summarization. Its capabilities in function calling and structured outputs also make it a strong candidate for tasks involving complex data processing and RAG (Retrieval-Augmented Generation) pipelines. The model's performance is reflected in its benchmarks, with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its potential for handling a wide range of natural language processing tasks.

### Pricing and Cost Considerations
Pricing for Mistral: Mistral Small 4 is based on input and output tokens, with costs of $0.15 per 1M input tokens and $0.6 per 1M output tokens. There are no additional costs for cached input or batch input. Example costs include $0.375 for 1,000 calls averaging 500 tokens, $3.75 for 10,000 calls, and $37.5 for 100,000 calls. With its competitive pricing and robust feature set, Mistral: Mistral Small 4 is an attractive option for developers looking for a reliable and versatile language model for their applications

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
Mistral: Mistral Small 4, provided by Mistralai, is a standard tier model released on 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and scalability of this model.

#### Cost Structure
The pricing for Mistral: Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

This indicates that the primary cost factors are the input and output token counts. Cached and batch inputs are not charged, suggesting potential cost savings through efficient usage.

#### When to Use Cached Tokens
Given that cached input tokens are free, it is highly beneficial to utilize cached tokens whenever possible. This can be particularly useful in applications where the same input data is processed multiple times, such as in chatbots or text analysis pipelines. By leveraging cached inputs, users can significantly reduce their costs.

#### Batch API Savings
Similar to cached inputs, batch inputs are also free. This means that processing inputs in batches can lead to substantial cost savings, especially for large-scale applications. However, the actual cost savings will depend on the specific use case and how the batch processing is implemented.

#### Cost at Scale
To understand the cost implications of using Mistral: Mistral Small 4 at scale, let's examine the provided cost examples:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These examples illustrate a linear cost scaling with the number of API calls. This linear relationship indicates that the cost per call remains constant, regardless of the scale.

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
The Mistral Small 4 model, provided by Mistralai, is a standard, non-open-source model released on 2024-01-01. 

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

The MMLU score of **80.0** indicates the model's performance on a set of tasks, with higher scores generally indicating better performance. The LMSYS Arena ELO score of **1200** is a measure of the model's competitive performance, with higher scores indicating better performance relative to other models.

The lack of HumanEval and GSM8K scores limits the understanding of the model's performance in specific areas, such as coding and mathematical problem-solving.

#### Real-World Implications
For real-world use, the Mistral Small 4 model's performance can be summarized as follows:
* The model's **MMLU score of 80.0

## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral Small 4, we will provide a general comparison framework that can be applied to other models in the market. This framework will help in evaluating the strengths and weaknesses of Mistral Small 4 against potential competitors.

#### Pricing Comparison
Mistral Small 4 is priced at:
- **$0.15 per 1M tokens** for input
- **$0.6 per 1M tokens** for output

To compare, we would need the pricing of competitor models. However, we can establish a general guideline for comparison:
- **Lower input and output costs** per 1M tokens generally indicate a more cost-effective option.
- **Batch input and cached input pricing** can significantly affect the overall cost for high-volume users; Mistral Small 4 does not charge for these, which could be a significant advantage.

#### Performance Trade-offs
Mistral Small 4 has the following performance metrics:
- **MMLU: 80.0**
- **LMSYS Arena ELO: 1200**

When comparing with competitors, consider:
- **Higher MMLU and LMSYS Arena ELO scores** typically indicate better performance in respective benchmarks.
- **The absence of HumanEval and GSM8K scores** for Mistral Small 4 means potential competitors with these scores may offer more comprehensive performance data.

#### Context and Limits
Mistral Small 4 has:
- **Context Window: 262,144 tokens**
- **Max Output: 4,096 tokens**
- **Knowledge Cutoff: 2023-12**

Competitors with:
- **Larger context windows** can handle longer inputs, potentially beneficial for certain applications.
- **Later knowledge cutoffs** may have more up-to-date information.

#### Capabilities and Best Use Cases
Mistral Small 4 supports:
- **Text, function calling, JSON mode, streaming, structured outputs**
- **Best for:** chat, text generation, coding, analysis, RAG pipelines, summarization

Consider competitors that:
- **Offer additional capabilities** or have a more specialized set of features that align better with specific use cases.
- **Are recommended for overlapping or different use cases**, which could indicate a more versatile or specialized model.

#### Choosing the Right Model
Given the data, Mistral Small 4 seems to be a strong contender for applications

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on 2024-01-01, this standard-tier model is not open-source and offers a context window of 262,144 tokens and a maximum output of 4,096 tokens.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its high context window and ability to generate human-like text, Mistral Small 4 is well-suited for chat applications and text generation tasks.
2. **Coding and Analysis**: The model's ability to perform function calling and generate structured outputs makes it a good fit for coding and analysis tasks, such as code completion and data analysis.
3. **Summarization**: Mistral Small 4's capabilities in text generation and analysis make it a good choice for summarization tasks, such as summarizing long documents or articles.
4. **RAG Pipelines**: The model's ability to generate structured outputs and perform function calling makes it a good fit for RAG (Retrieval-Augmented Generation) pipelines, which involve retrieving information from a knowledge base and generating text based on that information.
5. **Streaming**: With its ability to process streaming data, Mistral Small 4 can be used for real-time text generation and analysis tasks, such as live chat or real-time data analysis.

### Code Integration Examples with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code examples:

```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.Model("mistralai/mistral-small-2603")

# Define a function to generate text using the

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
