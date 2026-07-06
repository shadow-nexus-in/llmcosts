# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-06
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard tier language model released on 2024-01-01. This model is not open source. The architecture of Mistral Small 4 is designed to handle a variety of tasks, including text generation, coding, and analysis, with capabilities such as text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens.

### Technical Specifications and Use Cases
Mistral Small 4 is best utilized for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization. The model's pricing structure includes input costs of $0.15 per 1M tokens and output costs of $0.6 per 1M tokens. With a knowledge cutoff of 2023-12, this model is well-suited for tasks that require a strong understanding of data up to that point. The benchmarks for Mistral Small 4 show an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its performance capabilities. However, it is not recommended for tasks that fall outside its listed capabilities or require knowledge beyond its cutoff date.

### Pricing and Cost Considerations
The cost of using Mistral Small 4 can be estimated based on the number of calls and tokens processed. For example, 1,000 calls with an average of 500 tokens would cost $0.375, while 10,000 calls would amount to $3.75, and 100,000 calls would total $37.5. Given its capabilities and pricing structure, developers should carefully evaluate their use cases and budget requirements before integrating Mistral Small 4 into their applications. As there are no direct competitors listed,

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
Mistral Small 4, provided by Mistralai, is a standard tier model released on 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

This indicates that input and output tokens are the primary cost drivers, while cached and batch inputs are provided at no additional cost.

#### Optimal Usage Scenarios
- **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs. This can be particularly effective in scenarios where the same input tokens are reused across multiple API calls.
- **Batch API Savings**: Although batch input is listed as free, the actual cost savings come from reducing the number of API calls. By batching inputs, users can decrease the overall number of calls, thus saving on input and output token costs.

#### Cost at Scale
The provided cost examples illustrate the cost structure at different scales:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These examples demonstrate a linear cost increase with the number of API calls, indicating that the cost per call remains constant.

#### Cost Calculation
To estimate costs for a specific use case, calculate the total number of input and output tokens required. Given the pricing, the cost can be calculated as follows:
- **Input Cost**: (Total Input Tokens / 1,000,000) * $

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
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. It is not open source.

#### Pricing Model
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

#### Capabilities and Use Cases
Mistral Small 4 supports the following capabilities:
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

#### Cost Examples
The estimated costs for using Mistral Small 4 are:
* 1,000 calls (avg 500 tokens): **$0.375**
* 10,000 calls: **$3.75**
* 100,000 calls: **$37.5**

#### Interpretation of Benchmark Scores
*

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral: Mistral Small 4, we will provide a general overview of its features, pricing, and performance. This will help users understand when to choose this model and what trade-offs to expect.

#### Model Overview
* **Model:** Mistral: Mistral Small 4 (mistralai/mistral-small-2603)
* **Provider:** Mistralai
* **Release Date:** 2024-01-01
* **Tier:** Standard
* **Open Source:** False

#### Pricing
The pricing for Mistral: Mistral Small 4 is as follows:
* **Input:** $0.15 per 1M tokens
* **Output:** $0.6 per 1M tokens
* **Cached Input:** $None per 1M tokens
* **Batch Input:** $None per 1M tokens

#### Context and Limits
The model has the following context and limits:
* **Context Window:** 262,144 tokens
* **Max Output:** 4,096 tokens
* **Knowledge Cutoff:** 2023-12

#### Benchmarks
The model's performance on various benchmarks is:
* **MMLU:** 80.0
* **HumanEval:** None
* **LMSYS Arena ELO:** 1200
* **GSM8K:** None

#### Capabilities and Best Use Cases
Mistral: Mistral Small 4 supports the following capabilities:
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

#### Cost Examples
The estimated costs for using Mistral: Mistral Small 4 are:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

#### Choosing Mistral: Mistral Small 4
Since there are no direct competitors listed, users should consider the following factors when deciding whether to use Mistral: Mistral Small 4:
* **Performance requirements:** If your application requires a high context window (262,144 tokens) and moderate output size (4,096 tokens), Mistral:

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and proprietary licensing, it offers a unique set of features for various applications.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and ability to generate up to 4,096 tokens, Mistral Small 4 is well-suited for chat applications and text generation tasks.
2. **Coding and Analysis**: Mistral Small 4's function calling and structured outputs capabilities make it an excellent choice for coding and analysis tasks, such as code completion and data analysis.
3. **Summarization and RAG Pipelines**: Its ability to process large amounts of text and generate concise summaries makes it a good fit for summarization tasks and RAG (Retrieve, Augment, Generate) pipelines.
4. **Streaming and Real-time Applications**: With its streaming capability, Mistral Small 4 can be used for real-time applications, such as live chat, sentiment analysis, and event detection.
5. **JSON Mode and Structured Data Processing**: Its JSON mode and structured outputs capabilities make it suitable for processing and generating structured data, such as JSON objects and arrays.

### Code Integration Examples with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code examples:

```python
import os
import openrouter

# Initialize OpenRouter client
client = openrouter.Client(api_key="YOUR_API_KEY")

# Define a function to call Mistral Small 4
def call_mistral(input_text):
    response = client.call_model(
        model="mistralai/mistral-small-

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
