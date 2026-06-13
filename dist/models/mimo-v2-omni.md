# Xiaomi: MiMo-V2-Omni API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-13
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Xiaomi: MiMo-V2-Omni
The Xiaomi: MiMo-V2-Omni model, released by Xiaomi on 2024-01-01, is a standard, non-open-source language model designed for a variety of tasks. Its architecture, although not explicitly detailed, is implied to be robust given its capabilities in handling text, function calling, JSON mode, streaming, and structured outputs. This model is particularly suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization, thanks to its broad range of capabilities.

### Technical Specifications and Pricing
Technically, the MiMo-V2-Omni model boasts a context window of 262,144 tokens and can generate outputs of up to 65,536 tokens. The knowledge cutoff for this model is 2023-12, indicating that its training data includes information up to December 2023. The pricing for using this model is structured as follows: $0.4 per 1M tokens for input, $2.0 per 1M tokens for output, with no specified costs for cached input or batch input. This pricing model suggests that the cost of using MiMo-V2-Omni will primarily be driven by the output generated, with input costs being significantly lower. For example, 1,000 calls with an average of 500 tokens would cost $1.2, scaling up to $120.0 for 100,000 calls.

### Performance and Use Cases
The performance of MiMo-V2-Omni is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating a level of competence in language understanding and generation tasks. However, the absence of HumanEval and GSM8K benchmarks leaves some aspects of its performance unassessed. Given its capabilities and pricing, MiMo-V2-Omni is best utilized for applications requiring robust text handling

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.4 |
| Output | $2.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Xiaomi: MiMo-V2-Omni
#### Overview
The Xiaomi: MiMo-V2-Omni model is a standard, non-open source model released by Xiaomi on January 1, 2024. This analysis will break down the cost structure, provide guidance on when to use cached tokens, discuss batch API savings, and examine the cost at scale for 1,000, 10,000, and 100,000 API calls.

#### Cost Structure
The cost structure for Xiaomi: MiMo-V2-Omni is as follows:
* Input: $0.4 per 1 million tokens
* Output: $2.0 per 1 million tokens
* Cached Input: No charge ($None per 1 million tokens)
* Batch Input: No charge ($None per 1 million tokens)

#### Using Cached Tokens
Cached tokens can be used without incurring any additional costs. This makes them an attractive option when the same input is used multiple times. However, the context window limit of 262,144 tokens should be considered when deciding whether to use cached tokens.

#### Batch API Savings
There are no costs associated with batch input, making it a cost-effective option for large-scale API calls. However, the cost savings will primarily come from the reduced output costs, as the input costs are already relatively low.

#### Cost at Scale
The cost at scale for Xiaomi: MiMo-V2-Omni is as follows:
* 1,000 calls (avg 500 tokens): $1.2
* 10,000 calls: $12.0
* 100,000 calls: $120.0

To calculate the cost per call, we can divide the total cost by the number of calls:
* 1,000 calls: $1.2 / 1,000 = $0.0012 per call
* 10,000 calls: $12.0 / 10,000 =

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Xiaomi: MiMo-V2-Omni Benchmark Performance
#### Overview
The Xiaomi: MiMo-V2-Omni model, released on 2024-01-01, is a standard-tier model provided by Xiaomi. It is not open source.

#### Pricing
The pricing for this model is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Context and Limits
The model has the following context and limits:
* Context Window: 262,144 tokens
* Max Output: 65,536 tokens
* Knowledge Cutoff: 2023-12

#### Benchmarks
The model's benchmark performance is as follows:
* MMLU: 80.0
* HumanEval: None
* LMSYS Arena ELO: 1200
* GSM8K: None

The **MMLU (Massive Multitask Language Understanding) score** of 80.0 indicates the model's ability to perform well across a wide range of natural language processing tasks. A higher MMLU score generally corresponds to better performance in tasks such as text classification, sentiment analysis, and question answering.

The **LMSYS Arena ELO score** of 1200 is a measure of the model's overall language understanding and generation capabilities. ELO scores are used to rank models based on their performance in various tasks, with higher scores indicating better performance. An ELO score of 1200 suggests that the Xiaomi: MiMo-V2-Omni model has a moderate level

## Competitor Comparison
### Comparison of Xiaomi: MiMo-V2-Omni with Top Competitors
Since there are no direct competitors listed for the Xiaomi: MiMo-V2-Omni model, we will provide a general overview of the model's features, pricing, and performance. This will help users understand when to choose this model and what trade-offs to expect.

#### Model Overview
The Xiaomi: MiMo-V2-Omni is a standard-tier model released by Xiaomi on January 1, 2024. It is not open-source and has the following key features:
* **Context Window**: 262,144 tokens
* **Max Output**: 65,536 tokens
* **Knowledge Cutoff**: December 2023
* **Capabilities**: text, function_calling, json_mode, streaming, structured_outputs
* **Best For**: chat, text_generation, coding, analysis, rag_pipelines, summarization

#### Pricing
The pricing for the Xiaomi: MiMo-V2-Omni model is as follows:
* **Input**: $0.4 per 1M tokens
* **Output**: $2.0 per 1M tokens
* **Cached Input**: $None per 1M tokens
* **Batch Input**: $None per 1M tokens

#### Cost Examples
To give users an idea of the costs involved, here are some examples:
* **1,000 calls (avg 500 tokens)**: $1.2
* **10,000 calls**: $12.0
* **100,000 calls**: $120.0

#### Performance Trade-Offs
The Xiaomi: MiMo-V2-Omni model has the following benchmark scores:
* **MMLU**: 80.0
* **LMSYS Arena ELO**: 1200

Since there are no direct competitors listed, we cannot provide a direct comparison of performance trade-offs. However, users can consider the following factors when choosing a model:
* **Context Window**: If you need to process longer sequences of text, a model with a larger context window may be more suitable.
* **Max Output**: If you need to generate longer outputs, a model with a higher max output limit may be more suitable.
* **Knowledge Cutoff**: If you need access to more recent knowledge, a model with a more recent knowledge cutoff may be more suitable.

#### When to Choose Xiaomi: MiMo-V2-Omni
Based on the

## Best Use Cases
### Introduction to Xiaomi: MiMo-V2-Omni
The Xiaomi: MiMo-V2-Omni model, released by Xiaomi on 2024-01-01, is a standard, non-open-source model with a unique set of capabilities and pricing structure. This guide provides practical advice on the top 5 best use cases for this model, along with specific code integration examples using OpenRouter.

### Top 5 Use Cases for Xiaomi: MiMo-V2-Omni
Based on the capabilities and benchmarks of the Xiaomi: MiMo-V2-Omni model, the top 5 use cases are:

1. **Chat and Text Generation**: With its high MMLU score of 80.0 and support for text and structured outputs, this model is well-suited for chat and text generation applications.
2. **Coding and Analysis**: The model's function_calling and json_mode capabilities make it a good fit for coding and analysis tasks, such as code completion and data analysis.
3. **Summarization**: The Xiaomi: MiMo-V2-Omni model's support for summarization and its high context window of 262,144 tokens make it a good choice for summarizing long documents and texts.
4. **RAG Pipelines**: The model's support for rag_pipelines and its ability to handle structured outputs make it a good fit for applications that require retrieval-augmented generation.
5. **Streaming**: With its support for streaming, the Xiaomi: MiMo-V2-Omni model can be used for real-time text generation and analysis applications.

### Code Integration Examples with OpenRouter
To integrate the Xiaomi: MiMo-V2-Omni model with OpenRouter, you can use the following code examples:

```python
import openrouter

# Initialize the Xiaomi: MiMo-V2-Omni model
model = openrouter.Model("xiaomi/mimo-v2-omni")

# Use the model for text generation


## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
