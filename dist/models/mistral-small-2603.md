# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-14
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a context window of 262,144 tokens and can generate up to 4,096 output tokens. The model's capabilities include text generation, function calling, JSON mode, streaming, and structured outputs, making it a versatile tool for various applications.

### Strengths and Use Cases
The main strengths of Mistral Small 4 lie in its ability to perform well in tasks such as chat, text generation, coding, analysis, RAG pipelines, and summarization. With a pricing structure of $0.15 per 1M input tokens and $0.6 per 1M output tokens, it offers a cost-effective solution for developers. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its competence in language understanding and generation tasks. However, its limitations, such as a knowledge cutoff of 2023-12, should be considered when choosing this model for specific use cases.

### Cost and Competitiveness
In terms of cost, Mistral Small 4 provides a straightforward pricing model. For example, 1,000 calls with an average of 500 tokens would cost $0.375, while 10,000 calls would amount to $3.75, and 100,000 calls would be $37.5. With no direct competitors listed, Mistral Small 4 occupies a unique position in the market. Its capabilities, combined with its pricing structure, make it an attractive option for developers looking for a reliable language model for their applications, especially those involving text generation, coding, and analysis. However, the absence of open-source availability might be a consideration for

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
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and scalability of this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$0.00 per 1M tokens** (free)
* Batch Input: **$0.00 per 1M tokens** (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following strategies:
* **Cached Tokens**: Since cached input tokens are free, utilize this feature whenever possible to reduce input costs.
* **Batch API**: Leverage batch input to process multiple requests simultaneously, as batch input is also free.

#### Cost at Scale
The cost examples provided are as follows:
* **1,000 calls (avg 500 tokens)**: **$0.375**
* **10,000 calls**: **$3.75**
* **100,000 calls**: **$37.5**

To put these numbers into perspective, let's calculate the cost per call:
* 1,000 calls: **$0.375 / 1,000 calls = $0.000375 per call**
* 10,000 calls: **$3.75 / 10,000 calls = $0.000375 per call**
* 100,000 calls: **$37.5 / 100,000 calls = $0.000375 per call**

As shown, the cost per call remains constant at **$0.000375 per call**, indicating a linear scaling of costs with the number of API calls.

#### Conclusion
Mistral Small 4 offers a

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Benchmark Analysis
The Mistral Small 4 model, provided by Mistralai, is a standard, non-open-source model released on 2024-01-01. This analysis will focus on the benchmark performance of Mistral Small 4, specifically the MMLU, HumanEval, and Arena ELO scores, and their implications for real-world use.

#### Benchmark Scores
* **MMLU (Massive Multitask Language Understanding) Score: 80.0** - The MMLU score measures a model's ability to perform a wide range of natural language understanding tasks. A higher score indicates better performance. With a score of 80.0, Mistral Small 4 demonstrates a strong ability to understand and process human language.
* **HumanEval Score: None** - The HumanEval score evaluates a model's ability to generate code that can be executed and produce the correct output. Unfortunately, no HumanEval score is available for Mistral Small 4, making it difficult to assess its coding capabilities.
* **LMSYS Arena ELO Score: 1200** - The LMSYS Arena ELO score measures a model's performance in a competitive environment, where models are pitted against each other to complete tasks. An ELO score of 1200 indicates that Mistral Small 4 has a moderate level of performance, but may struggle against more advanced models.

#### Real-World Implications
The benchmark scores suggest that Mistral Small 4 is well-suited for tasks that require strong natural language understanding, such as:
* Text generation
* Chat
* Analysis
* Summarization
However, the lack of a HumanEval score and the moderate Arena E

## Competitor Comparison
### Mistral Small 4 Comparison
Since there are no direct competitors listed for the Mistral Small 4 model, we will provide a general overview of its features, pricing, and capabilities to help users make informed decisions.

#### Model Overview
The Mistral Small 4 model is a standard-tier model provided by Mistralai, released on January 1, 2024. It is not open-source.

#### Pricing
The pricing for the Mistral Small 4 model is as follows:
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
The model's performance is measured by the following benchmarks:
* MMLU: 80.0
* LMSYS Arena ELO: 1200

#### Capabilities and Use Cases
The Mistral Small 4 model supports the following capabilities:
* text
* function_calling
* json_mode
* streaming
* structured_outputs

It is best suited for the following use cases:
* chat
* text_generation
* coding
* analysis
* rag_pipelines
* summarization

#### Cost Examples
The estimated costs for using the Mistral Small 4 model are:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

### Choosing the Mistral Small 4 Model
Since there are no direct competitors listed, the decision to choose the Mistral Small 4 model depends on the specific requirements of your project. Consider the following factors:
* **Pricing**: If your project requires a model with a relatively low input cost ($0.15 per 1M tokens) and a moderate output cost ($0.6 per 1M tokens), the Mistral Small 4 model may be a good choice.
* **Context and Limits**: If your project requires a model with a large context window (262,144 tokens) and a moderate maximum output (4,096 tokens), the Mistral Small 4 model

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and release date of 2024-01-01, it offers a robust solution for various use cases.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its high MMLU score of 80.0 and ability to handle large context windows (262,144 tokens), Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: Its function calling and structured outputs capabilities make it an excellent choice for coding and analysis tasks, such as code completion and data analysis.
3. **Summarization**: Mistral Small 4's ability to handle large context windows and generate structured outputs makes it a good fit for summarization tasks, such as summarizing long documents or articles.
4. **RAG Pipelines**: Its support for streaming and structured outputs makes it a suitable choice for RAG (Retrieval-Augmented Generation) pipelines, which involve retrieving information from external sources and generating text based on that information.
5. **OpenRouter Integration**: Mistral Small 4 can be integrated with OpenRouter, a popular open-source routing framework, to generate text-based routing instructions or analyze routing data.

### Code Integration Example with OpenRouter
Here is an example of how to integrate Mistral Small 4 with OpenRouter using Python:
```python
import os
import requests

# Set up OpenRouter API endpoint
openrouter_url = "https://api.openrouter.com/v1/route"

# Set up Mistral Small 4 API endpoint
mistral_url = "https://api.mistralai

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
