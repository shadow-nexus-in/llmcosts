# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-13
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral: Mistral Small 4 is designed to handle a variety of tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens, making it suitable for complex tasks.

### Technical Specifications and Use Cases
The model's technical specifications highlight its prowess in handling extensive inputs and generating substantial outputs. With a context window of 262,144 tokens and a maximum output of 4,096 tokens, Mistral: Mistral Small 4 is best utilized for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization. Its benchmark scores, including an MMLU of 80.0 and an LMSYS Arena ELO of 1200, demonstrate its competence in these areas. However, its limitations, such as a knowledge cutoff of 2023-12, should be considered when applying it to tasks requiring more recent information.

### Pricing and Cost Efficiency
The pricing model for Mistral: Mistral Small 4 is based on input and output tokens, with costs of $0.15 per 1M input tokens and $0.6 per 1M output tokens. This pricing structure makes it an economical choice for developers, with estimated costs of $0.375 for 1,000 calls (averaging 500 tokens), $3.75 for 10,000 calls, and $37.5 for 100,000 calls. Given its capabilities and cost efficiency, Mistral: Mistral Small 4 is a viable option for developers seeking a robust model

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
Mistral: Mistral Small 4, provided by Mistralai, is a standard tier model with a release date of 2024-01-01. It is not open source. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale.

#### Cost Structure
The pricing for Mistral: Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: No charge ($None per 1M tokens)
- **Batch Input**: No charge ($None per 1M tokens)

#### Optimal Usage Scenarios
- **Cached Tokens**: Since there is no charge for cached input tokens, it is highly beneficial to use cached tokens whenever possible. This can significantly reduce costs, especially in applications where the same or similar inputs are processed multiple times.
- **Batch API**: Although there is no direct cost saving mentioned for batch input, utilizing batch API calls can still lead to efficiency gains and potentially reduce the overall cost by minimizing the number of API requests.

#### Cost at Scale
The cost examples provided give insight into the expenses at different scales:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These examples illustrate a linear cost increase with the number of API calls, indicating that the cost per call remains constant regardless of the scale.

#### Calculating Costs Based on Tokens
To understand the cost structure better, let's calculate the cost per token based on the input and output pricing:
- **Input Cost per Token**: $0.15 / 1,000,000 tokens = $0.00000015 per token
- **Output Cost per Token**: $

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
The Mistral Small 4 model, provided by Mistralai, is a standard-tier language model with a release date of 2024-01-01. It is not open source.

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

The MMLU score of 80.0 indicates the model's ability to understand and generate human-like text. A higher MMLU score generally corresponds to better performance in natural language understanding and generation tasks.

The LMSYS Arena ELO score of 1200 is a measure of the model's performance in a competitive environment, where it is pitted against other models. A higher ELO score indicates better performance.

The lack of HumanEval and GSM8K scores makes it difficult to assess the model's performance in specific areas, such as coding and mathematical reasoning.

#### Capabilities and Use Cases
Mistral Small 4 supports the following capabilities:
* text


## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral: Mistral Small 4, we will create a hypothetical comparison with other models in the same tier and with similar capabilities. 

#### Hypothetical Competitors
For the purpose of this comparison, let's consider two hypothetical models: 
- **Model A**: A standard, open-source model with similar capabilities to Mistral: Mistral Small 4.
- **Model B**: A premium model with advanced capabilities and higher pricing.

#### Pricing Comparison
The pricing for Mistral: Mistral Small 4 is as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens

In comparison, the hypothetical competitors may have the following pricing:
- **Model A**:
  - Input: $0.10 per 1M tokens (33% cheaper than Mistral: Mistral Small 4)
  - Output: $0.50 per 1M tokens (17% cheaper than Mistral: Mistral Small 4)
- **Model B**:
  - Input: $0.30 per 1M tokens (100% more expensive than Mistral: Mistral Small 4)
  - Output: $1.20 per 1M tokens (100% more expensive than Mistral: Mistral Small 4)

#### Performance Trade-offs
The performance of Mistral: Mistral Small 4 is measured by the following benchmarks:
- MMLU: 80.0
- LMSYS Arena ELO: 1200

In comparison, the hypothetical competitors may have the following performance:
- **Model A**:
  - MMLU: 70.0 (12.5% lower than Mistral: Mistral Small 4)
  - LMSYS Arena ELO: 1000 (16.7% lower than Mistral: Mistral Small 4)
- **Model B**:
  - MMLU: 90.0 (12.5% higher than Mistral: Mistral Small 4)
  - LMSYS Arena ELO: 1500 (25% higher than Mistral: Mistral Small 4)

#### When to Choose Each Model
Based on the pricing and performance comparison, here are some guidelines on when to choose each model:
- **Mistral: Mist

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on 2024-01-01, this model is part of the standard tier and is not open-source.

### Pricing Model
The pricing for Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its ability to generate human-like text, Mistral Small 4 is ideal for chat applications, content generation, and text summarization.
2. **Coding and Function Calling**: Mistral Small 4 can be used for coding tasks, such as generating code snippets, and function calling, making it a great tool for developers.
3. **Analysis and Summarization**: The model's ability to analyze and summarize large amounts of text makes it perfect for applications such as news summarization, research paper analysis, and data analysis.
4. **RAG Pipelines**: Mistral Small 4 can be used in RAG (Retrieval-Augmented Generation) pipelines to generate text based on retrieved information, making it a great tool for applications such as question answering and text generation.
5. **Streaming and Structured Outputs**: With its ability to generate structured outputs and stream text, Mistral Small 4 is ideal for applications such as live text generation, sentiment analysis, and data streaming.

### Code Integration Example with OpenRouter
Here is an example of how to integrate Mistral Small 4 with Open

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
