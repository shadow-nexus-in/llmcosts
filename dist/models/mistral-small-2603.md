# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-10
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral: Mistral Small 4 is designed to handle a variety of natural language processing tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens.

### Technical Specifications and Use Cases
The model's technical specifications and pricing are as follows: input costs $0.15 per 1M tokens, and output costs $0.6 per 1M tokens. With a context window of 262,144 tokens and a max output of 4,096 tokens, Mistral: Mistral Small 4 is best suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization. Its performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. Given its capabilities and pricing, developers can estimate costs based on the number of calls and tokens processed, with examples including $0.375 for 1,000 calls averaging 500 tokens, $3.75 for 10,000 calls, and $37.5 for 100,000 calls.

### Pricing and Competitiveness
In terms of pricing, Mistral: Mistral Small 4 offers a straightforward cost structure with no costs for cached input or batch input. The model's pricing is competitive, with no direct competitors listed. Developers can use the provided cost examples to plan and estimate the expenses associated with integrating Mistral: Mistral Small 4 into their applications. With its standard tier and proprietary nature, Mistral: Mistral

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
Mistral: Mistral Small 4, provided by Mistralai, is a standard, non-open-source model released on 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale for this model.

#### Cost Structure
The pricing for Mistral: Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
- **Cached Tokens**: Since cached input tokens are free, it is highly beneficial to utilize cached tokens whenever possible. This can significantly reduce costs, especially for applications with repetitive or similar input sequences.
- **Batch API Savings**: Although the pricing does not explicitly mention a discount for batch inputs, the fact that batch input costs are listed as $None per 1M tokens suggests that batching inputs can be cost-effective. However, the exact savings depend on the implementation and may vary.

#### Cost at Scale
To understand the cost implications of using Mistral: Mistral Small 4 at scale, let's examine the provided cost examples:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These examples indicate a linear cost scaling with the number of API calls, suggesting that the cost per call remains constant regardless of the volume.

#### Cost Calculation
Given the input and output pricing, the total cost for a single API call can be estimated as follows:
- Assume an average of 500 tokens per call (as per the 1,000 calls example).
-

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
The model's benchmark performance is as follows:
* MMLU: **80.0**
* HumanEval: **None**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

The MMLU score of **80.0** indicates the model's ability to understand and process mathematical and logical concepts. A higher MMLU score generally corresponds to better performance in tasks that require mathematical reasoning.

The LMSYS Arena ELO score of **1200** is a measure of the model's overall performance in a competitive setting. ELO scores are used to rank models based on their performance in various tasks, with higher scores indicating better performance.

The lack of HumanEval and GSM8K scores means that the model's performance in these specific areas is unknown.

#### Capabilities and Use Cases
Mistral Small 4 supports the following capabilities:
*

## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral Small 4, we will provide a general comparison framework that can be applied to other models in the market. This framework will consider price differences, performance trade-offs, and use cases.

#### Pricing Comparison
Mistral Small 4 is priced at:
* $0.15 per 1M tokens for input
* $0.6 per 1M tokens for output

To compare, we would need the pricing information of competing models. However, we can establish a general guideline for comparison:
* Models with lower input and output prices may be more cost-effective for large-scale applications.
* Models with higher prices may offer better performance, more advanced capabilities, or larger context windows.

#### Performance Trade-offs
Mistral Small 4 has the following performance metrics:
* MMLU: 80.0
* LMSYS Arena ELO: 1200

When comparing with other models, consider the following trade-offs:
* Models with higher MMLU scores may perform better on tasks that require multi-step reasoning and problem-solving.
* Models with higher LMSYS Arena ELO scores may perform better on tasks that require strategic thinking and decision-making.

#### Context and Limits
Mistral Small 4 has the following context and limits:
* Context Window: 262,144 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2023-12

When comparing with other models, consider the following:
* Models with larger context windows may be more suitable for tasks that require processing long documents or conversations.
* Models with higher max output limits may be more suitable for tasks that require generating long texts or responses.

#### Capabilities and Use Cases
Mistral Small 4 has the following capabilities:
* text, function_calling, json_mode, streaming, structured_outputs

It is best suited for tasks such as:
* chat
* text_generation
* coding
* analysis
* rag_pipelines
* summarization

When choosing a model, consider the specific requirements of your application and select a model that aligns with your needs.

#### Cost Examples
The cost of using Mistral Small 4 can be estimated as follows:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls:

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and proprietary licensing, it offers a unique set of features for various applications.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities, the following are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and ability to generate up to 4,096 tokens, Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: Its function calling and structured outputs capabilities make it an excellent choice for coding and analysis tasks, such as code completion and data analysis.
3. **Summarization and RAG Pipelines**: Mistral Small 4's ability to process large amounts of text and generate concise summaries makes it a great fit for summarization and RAG (Retrieval-Augmented Generation) pipelines.
4. **Streaming and Real-time Applications**: With its streaming capability, Mistral Small 4 can be used for real-time applications, such as live chat, sentiment analysis, and event detection.
5. **JSON Mode and Structured Data Processing**: Its JSON mode and structured outputs capabilities make it suitable for processing and generating structured data, such as JSON objects and XML files.

### Code Integration Examples with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code examples:

```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.Model("mistralai/mistral-small-2603")

# Define a function to generate text
def generate_text(prompt):
    input_ids = openrouter.tokenize(prompt)
    output = model.generate(input_ids, max_length=409

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
