# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-09
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of natural language processing tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens, making it suitable for complex tasks such as chat, text generation, coding, analysis, and summarization.

### Technical Specifications and Pricing
Technically, Mistral Small 4 has a context window of 262,144 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2023-12. The model's pricing is based on input and output tokens, with costs of $0.15 per 1M tokens for input and $0.6 per 1M tokens for output. There are no specified costs for cached input or batch input. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. With capabilities such as function calling and structured outputs, Mistral Small 4 is positioned for tasks that require both understanding and generation of complex text, including coding and analysis.

### Use Cases and Cost Considerations
Mistral Small 4 is best suited for applications like chat, text generation, coding, analysis, and summarization, given its robust capabilities and large context window. However, its cost-effectiveness should be considered based on the specific use case. For example, 1,000 calls with an average of 500 tokens would cost $0.375, while 100,000 calls would amount to $37.5. With no direct competitors listed, Mist

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
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* **Input**: $0.15 per 1M tokens
* **Output**: $0.6 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
Given the cost structure, it's essential to understand when to utilize cached tokens and batch API calls to minimize costs.

* **Cached Tokens**: Since cached input tokens are free, it's beneficial to use them whenever possible. This can significantly reduce costs, especially for applications with repetitive or similar input patterns.
* **Batch API Savings**: Although batch input is free, the primary cost driver is the output tokens. To maximize savings, consider batching API calls to reduce the number of output tokens generated.

#### Cost at Scale
To illustrate the cost-effectiveness of Mistral Small 4 at scale, let's examine the provided cost examples:
* **1,000 calls (avg 500 tokens)**: $0.375
* **10,000 calls**: $3.75
* **100,000 calls**: $37.5

These examples demonstrate a linear cost increase with the number of API calls. To estimate costs for larger scales, we can extrapolate from these examples.

#### Cost Estimation
Assuming an average of 500 tokens per call, we can estimate the cost per call as follows:
* **Input cost**: 500 tokens / 1,000,000 tokens per $0.15 = $0.000075 per call


## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Mistral: Mistral Small 4 Benchmark Performance
#### Overview
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. It is not open source.

#### Pricing
The pricing model for Mistral: Mistral Small 4 is as follows:
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
The benchmark performance of Mistral: Mistral Small 4 is as follows:
* MMLU: 80.0
* HumanEval: None
* LMSYS Arena ELO: 1200
* GSM8K: None

#### Interpretation of Benchmarks
* **MMLU (Massive Multitask Language Understanding)**: A score of 80.0 indicates the model's ability to understand and perform a wide range of natural language tasks. A higher score generally indicates better performance.
* **HumanEval**: Not available for this model.
* **LMSYS Arena ELO**: A score of 1200 indicates the model's competitive performance in the LMSYS Arena, a benchmark for evaluating language models. A higher score generally indicates better performance.

#### Real-World Use
The benchmark scores suggest that Mistral: Mistral

## Competitor Comparison
### Mistral Small 4 Comparison
Since there are no direct competitors listed for the Mistral Small 4 model, we will provide a general overview of its features, pricing, and performance. This will help users understand the model's strengths and weaknesses, as well as its potential use cases.

#### Model Overview
The Mistral Small 4 model is a standard-tier model released by Mistralai on 2024-01-01. It is not open-source and has the following key features:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12
* **Capabilities**: text, function_calling, json_mode, streaming, structured_outputs
* **Best For**: chat, text_generation, coding, analysis, rag_pipelines, summarization

#### Pricing
The pricing for the Mistral Small 4 model is as follows:
* **Input**: $0.15 per 1M tokens
* **Output**: $0.6 per 1M tokens
* **Cached Input**: $None per 1M tokens
* **Batch Input**: $None per 1M tokens

#### Cost Examples
To help estimate costs, here are some examples:
* **1,000 calls (avg 500 tokens)**: $0.375
* **10,000 calls**: $3.75
* **100,000 calls**: $37.5

#### Performance
The Mistral Small 4 model has the following benchmark scores:
* **MMLU**: 80.0
* **LMSYS Arena ELO**: 1200

Since there are no direct competitors listed, we cannot provide a direct comparison of pricing and performance. However, users can use the provided information to evaluate the Mistral Small 4 model's strengths and weaknesses and determine if it is suitable for their specific use case.

### Choosing the Right Model
When choosing a model, consider the following factors:
* **Context Window**: If you need to process longer sequences of text, look for models with larger context windows.
* **Max Output**: If you need to generate longer outputs, look for models with higher max output limits.
* **Knowledge Cutoff**: If you need access to more recent knowledge, look for models with more recent knowledge cutoffs.
* **Capabilities**: Consider the specific capabilities you need, such as text generation, coding, or analysis.


## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and proprietary licensing, it offers a unique set of features that can be leveraged for various applications.

### Top 5 Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, here are the top 5 use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its high MMLU score of 80.0, Mistral Small 4 is well-suited for chat and text generation applications. Its ability to process up to 262,144 tokens in its context window makes it an ideal choice for generating coherent and contextually relevant text.
2. **Coding and Analysis**: Mistral Small 4's function calling and structured outputs capabilities make it a great tool for coding and analysis tasks. Its ability to process JSON data and generate structured outputs makes it an ideal choice for data analysis and processing applications.
3. **Summarization and RAG Pipelines**: Mistral Small 4's text generation capabilities and high MMLU score make it well-suited for summarization tasks. Its ability to process large amounts of text and generate concise summaries makes it an ideal choice for RAG pipelines and other summarization applications.
4. **OpenRouter Integration**: Mistral Small 4 can be integrated with OpenRouter to enable advanced routing and navigation capabilities. For example, the following code snippet demonstrates how to use Mistral Small 4 with OpenRouter to generate directions:
```python
import openrouter
from mistralai import MistralSmall4

# Initialize Mistral Small 4 model
model = MistralSmall4()

# Define a function to generate directions using OpenRouter
def generate_directions(start, end):
    # Use OpenRouter to generate directions
    directions = open

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
