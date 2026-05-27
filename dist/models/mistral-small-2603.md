# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-27
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, released by Mistralai on 2024-01-01, is a standard-tier language model that operates under a closed-source license. This model is part of the Mistralai family, designed to provide efficient and effective language processing capabilities. With its specific architecture tailored for a variety of tasks, Mistral Small 4 is positioned to serve developers in multiple areas, including but not limited to chat, text generation, coding, and analysis.

### Technical Capabilities and Use Cases
Technically, Mistral Small 4 boasts a context window of 262,144 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2023-12. It supports multiple capabilities such as text processing, function calling, JSON mode, streaming, and structured outputs. These features make it an ideal choice for applications requiring complex text handling, coding assistance, and data analysis. The model's strengths are reflected in its benchmark scores, including an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. However, its pricing structure, with input costing $0.15 per 1M tokens and output costing $0.6 per 1M tokens, will be a critical factor for developers in determining its cost-effectiveness for their specific use cases.

### Pricing and Cost Considerations
The pricing model for Mistral Small 4 is straightforward, with costs calculated based on input and output token volumes. For example, 1,000 calls averaging 500 tokens each would cost $0.375, scaling up to $37.5 for 100,000 calls. Given its capabilities and pricing, developers should evaluate how Mistral Small 4 fits into their project budgets, especially considering its suitability for tasks like chat, text generation, and coding, where its strengths can be fully leveraged. With no direct competitors listed

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
Mistral Small 4, provided by Mistralai, is a standard, non-open-source model released on 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and scalability of this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

This structure indicates that input and output tokens are the primary cost factors, while cached and batch inputs are not charged.

#### Optimal Usage Scenarios
- **Cached Tokens**: Since cached input tokens are free, it is highly beneficial to utilize cached tokens whenever possible. This can significantly reduce costs, especially for applications with repetitive or similar input queries.
- **Batch API Savings**: Although batch input is listed as free, the actual cost savings come from the reduced overhead of making fewer API calls. This can lead to indirect cost savings by minimizing the number of calls and thus the associated input and output token costs.

#### Cost at Scale
The provided cost examples give insight into the scalability of Mistral Small 4:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These examples suggest a linear scaling of costs with the number of API calls. To estimate costs for other scenarios, one can use the average cost per call, which is $0.000375 per call (based on the 1,000 calls example).

#### Calculating Costs
Given the average cost per call, you can estimate costs for different numbers of API calls. For instance:
- **

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

The MMLU score of 80.0 indicates the model's performance on a specific set of tasks, with higher scores generally indicating better performance. The LMSYS Arena ELO score of 1200 provides a relative ranking of the model's performance compared to other models, with higher scores indicating better performance.

The lack of HumanEval and GSM8K scores means that the model's performance on these specific benchmarks is unknown.

#### Real-World Implications
For real-world use, the benchmark scores can be interpreted as follows:
* The MMLU score of 80.0 suggests that

## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral Small 4, we will provide a general overview of the model's features, pricing, and performance. This will help users understand the model's strengths and weaknesses and make informed decisions about when to choose it.

#### Model Overview
* **Provider:** Mistralai
* **Release Date:** 2024-01-01
* **Tier:** Standard
* **Open Source:** False

#### Pricing
The pricing for Mistral Small 4 is as follows:
* **Input:** $0.15 per 1M tokens
* **Output:** $0.6 per 1M tokens
* **Cached Input:** $None per 1M tokens
* **Batch Input:** $None per 1M tokens

#### Context and Limits
* **Context Window:** 262,144 tokens
* **Max Output:** 4,096 tokens
* **Knowledge Cutoff:** 2023-12

#### Benchmarks
The model's performance on various benchmarks is:
* **MMLU:** 80.0
* **HumanEval:** None
* **LMSYS Arena ELO:** 1200
* **GSM8K:** None

#### Capabilities and Use Cases
Mistral Small 4 supports the following capabilities:
* **Text**
* **Function calling**
* **JSON mode**
* **Streaming**
* **Structured outputs**

It is best suited for the following use cases:
* **Chat**
* **Text generation**
* **Coding**
* **Analysis**
* **RAG pipelines**
* **Summarization**

#### Cost Examples
Here are some cost examples for using Mistral Small 4:
* **1,000 calls (avg 500 tokens):** $0.375
* **10,000 calls:** $3.75
* **100,000 calls:** $37.5

#### Choosing Mistral Small 4
Since there are no direct competitors listed, we recommend considering the following factors when deciding whether to use Mistral Small 4:
* **Performance requirements:** If you need a model with a high MMLU score (80.0) and a moderate LMSYS Arena ELO score (1200), Mistral Small 4 may be a good choice.
* **Pricing constraints:** If you are looking for a model with a relatively low

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and non-open source status, it offers a unique set of features for various applications.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and ability to generate up to 4,096 tokens, Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: Its function calling and structured outputs capabilities make it an excellent choice for coding and analysis tasks, such as code completion and data analysis.
3. **Summarization**: Mistral Small 4's ability to process large amounts of text and generate concise summaries makes it a great fit for summarization tasks.
4. **RAG Pipelines**: Its support for retrieval-augmented generation (RAG) pipelines enables it to be used in applications that require generating text based on external knowledge sources.
5. **Streaming**: With its streaming capability, Mistral Small 4 can be used in real-time applications, such as live chat or text-based interfaces.

### Code Integration Example with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.Model("mistralai/mistral-small-2603")

# Define a function to generate text using the model
def generate_text(prompt):
    input_ids = openrouter.tokenize(prompt)
    output = model.generate(input_ids, max_length=4096)
    return openrouter.detokenize(output)

# Use the function

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
