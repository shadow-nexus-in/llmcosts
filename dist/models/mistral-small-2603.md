# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-20
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral: Mistral Small 4 is designed to handle a wide range of tasks, including text generation, function calling, and structured outputs. Its capabilities extend to chat, text generation, coding, analysis, and summarization, making it a versatile tool for developers.

### Technical Specifications and Strengths
The model boasts a context window of 262,144 tokens and can generate up to 4,096 tokens as output. With a knowledge cutoff of 2023-12, it is well-equipped to handle tasks that require a broad and up-to-date understanding of the world up to that point. The pricing for Mistral: Mistral Small 4 is as follows: $0.15 per 1M tokens for input, $0.6 per 1M tokens for output, with no charges for cached or batch input. Its strengths are reflected in its benchmark scores, including an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. These specifications and strengths make it particularly suited for applications such as chatbots, text analysis, and coding assistance.

### Use Cases and Cost Considerations
Given its capabilities, Mistral: Mistral Small 4 is best utilized for tasks like chat, text generation, coding, analysis, and summarization. It is not recommended for tasks outside these domains, as indicated by the lack of direct competitors and specific "not good for" use cases. For developers considering this model, the cost can be estimated based on the number of calls and tokens used. For example, 1,000 calls averaging 500 tokens would cost $0.375, scaling up to $37.5 for 100,000 calls

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
Mistral Small 4, provided by Mistralai, is a standard tier model with a release date of 2024-01-01. It is not open source. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* **Input**: $0.15 per 1M tokens
* **Output**: $0.6 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
* **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
* **Batch API Savings**: Although batch input is free, the actual cost savings come from reduced output tokens. To maximize batch API savings, prioritize output token reduction.

#### Cost at Scale
The cost examples provided are as follows:
* **1,000 calls (avg 500 tokens)**: $0.375
* **10,000 calls**: $3.75
* **100,000 calls**: $37.5

These costs can be broken down into input and output token costs. Assuming an average of 500 tokens per call, the total tokens for each scenario would be:
* **1,000 calls**: 500,000 tokens (input) + 4,096 tokens (output) * 1,000 calls (assuming max output) = 500,000 + 4,096,000 = 4,596,000 tokens
* **10,000 calls**: 5,000,000 tokens (input) + 40,960,000 tokens (output) = 45,960,000 tokens
* **100,000 calls**: 50,000

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
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. It is not open source.

#### Pricing
The pricing model for Mistral Small 4 is as follows:
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
The benchmark performance of Mistral Small 4 is:
* MMLU: **80.0**
* HumanEval: **None**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

The MMLU score of 80.0 indicates the model's ability to understand and process mathematical and logical concepts. A higher MMLU score generally corresponds to better performance in tasks that require mathematical reasoning.

The LMSYS Arena ELO score of 1200 is a measure of the model's overall performance in a competitive setting, with higher scores indicating better performance. However, without a HumanEval score, it is difficult to assess the model's performance in coding and programming tasks.

#### Capabilities and Use Cases
Mistral Small 4 supports the following capabilities:
* text
* function_calling
* json_mode
* streaming
* structured_outputs



## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral: Mistral Small 4 model, we will provide a general comparison framework that can be applied to other models in the market. This framework will consider key factors such as pricing, performance, and capabilities.

#### Pricing Comparison
The Mistral: Mistral Small 4 model is priced as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens

To compare, we would need the pricing information of its top competitors. However, based on the provided data, we can calculate the cost of using the Mistral: Mistral Small 4 model for different scenarios:
- 1,000 calls (avg 500 tokens): $0.375
- 10,000 calls: $3.75
- 100,000 calls: $37.5

#### Performance Trade-offs
The performance of the Mistral: Mistral Small 4 model can be evaluated based on its benchmarks:
- MMLU: 80.0
- LMSYS Arena ELO: 1200

When comparing with other models, consider the following:
- **MMLU Score**: A higher score indicates better performance. If a competitor has a significantly higher MMLU score, it may be a better choice for applications requiring high accuracy.
- **LMSYS Arena ELO**: This score indicates the model's performance in a competitive environment. A higher score suggests better performance in tasks that require strategic thinking and adaptation.

#### Capabilities and Best Use Cases
The Mistral: Mistral Small 4 model supports the following capabilities:
- text
- function_calling
- json_mode
- streaming
- structured_outputs

It is best suited for applications such as:
- chat
- text_generation
- coding
- analysis
- rag_pipelines
- summarization

When choosing between the Mistral: Mistral Small 4 model and its competitors, consider the specific requirements of your project. If your project requires capabilities that are not supported by the Mistral: Mistral Small 4 model, you may need to consider alternative options.

#### Example Use Cases
Based on the provided capabilities and best use cases, here are some example scenarios where the Mistral: Mistral Small 4 model can be used:
- **Chatbots**: The model's support

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on January 1, 2024, this model is part of the standard tier and is not open source.

### Pricing Model
The pricing for Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities and pricing, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its ability to generate human-like text and its support for streaming, Mistral Small 4 is well-suited for chat applications and text generation tasks.
2. **Coding and Analysis**: Mistral Small 4's function calling and structured outputs capabilities make it a good fit for coding and analysis tasks, such as code completion and data analysis.
3. **Summarization**: The model's ability to generate concise and accurate summaries makes it a good choice for summarization tasks.
4. **RAG Pipelines**: Mistral Small 4's support for Retrieval-Augmented Generation (RAG) pipelines makes it a good fit for tasks that require generating text based on external knowledge sources.
5. **OpenRouter Integration**: Mistral Small 4 can be integrated with OpenRouter to enable more efficient and effective routing of text-based inputs and outputs. For example:
```python
import openrouter

# Initialize OpenRouter
router = openrouter.Router()

# Define a function to generate text using Mistral Small 4
def generate_text(input_text):
    # Use Mistral Small 4

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
