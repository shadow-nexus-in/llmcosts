# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-12
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a wide range of natural language processing tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens.

### Technical Specifications and Use Cases
The model's technical specifications highlight its suitability for various applications. With a context window of 262,144 tokens and a maximum output of 4,096 tokens, Mistral Small 4 is well-suited for tasks that require processing and understanding large pieces of text. Its capabilities in text generation, function calling, and structured outputs make it an ideal choice for chat, text generation, coding, analysis, RAG pipelines, and summarization tasks. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its competence in handling complex language tasks.

### Pricing and Cost Considerations
The pricing model for Mistral Small 4 is based on input and output tokens, with costs of $0.15 per 1M input tokens and $0.6 per 1M output tokens. For developers, estimating costs is straightforward, with examples provided such as 1,000 calls averaging 500 tokens costing $0.375, 10,000 calls costing $3.75, and 100,000 calls costing $37.5. Given its capabilities and pricing structure, Mistral Small 4 is positioned as a competitive option for developers seeking a robust language model for a variety of applications, although it does not have direct competitors listed. Its limitations, such as a

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
Mistral Small 4, provided by Mistralai, is a standard, non-open-source model released on 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* **Input**: $0.15 per 1M tokens
* **Output**: $0.6 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
* **Cached Tokens**: Since cached input tokens are free, it is advisable to use cached tokens whenever possible to minimize costs. This is particularly beneficial for applications with repetitive or similar input sequences.
* **Batch API Savings**: Batch input is also free, making it an attractive option for bulk processing. By batching API calls, users can significantly reduce their costs.

#### Cost at Scale
The cost of using Mistral Small 4 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: $0.375
* **10,000 calls**: $3.75
* **100,000 calls**: $37.5

These costs demonstrate a linear scaling of expenses with the number of API calls, indicating that the cost per call remains constant regardless of the volume.

#### Context and Limits
It is essential to consider the context window and output limits when using Mistral Small 4:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12

These constraints may impact the model's performance and suitability for specific applications.

#### Capabilities and Recommendations
Mistral Small 4 is capable of:
* Text processing
*

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
Mistral Small 4, provided by Mistralai, is a standard-tier model released on 2024-01-01. It is not open source and offers a range of capabilities including text, function calling, JSON mode, streaming, and structured outputs.

#### Pricing
The pricing model for Mistral Small 4 is as follows:
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
The benchmark performance of Mistral Small 4 is as follows:
* MMLU: 80.0
* HumanEval: None
* LMSYS Arena ELO: 1200
* GSM8K: None

The MMLU score of 80.0 indicates the model's performance on a range of natural language processing tasks. A higher MMLU score generally indicates better performance. 
The LMSYS Arena ELO score of 1200 is a measure of the model's performance in a competitive environment, with higher scores indicating better performance. 
The lack of HumanEval and GSM8K scores limits the understanding of the model's performance on specific tasks such as coding and math problem-solving.

#### Capabilities and Use Cases
Mistral Small 4 is best suited for tasks such as:
* Chat


## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral: Mistral Small 4, we will provide a general comparison framework that can be applied to other models in the same tier and category.

#### Pricing Comparison
The pricing for Mistral: Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

To compare, we would need the pricing information of the top competitors. However, we can provide a general outline of how to evaluate the pricing:
* Calculate the total cost per call based on the average number of tokens per call.
* Compare the cost per call across different models.
* Consider the cost savings of using cached input or batch input, if available.

#### Performance Trade-offs
Mistral: Mistral Small 4 has the following performance characteristics:
* Context Window: 262,144 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2023-12
* Benchmarks:
	+ MMLU: 80.0
	+ LMSYS Arena ELO: 1200

When evaluating top competitors, consider the following performance trade-offs:
* Context window: A larger context window may be beneficial for tasks that require longer input sequences.
* Max output: A larger max output may be beneficial for tasks that require longer output sequences.
* Knowledge cutoff: A more recent knowledge cutoff may be beneficial for tasks that require up-to-date information.
* Benchmarks: Compare the performance of Mistral: Mistral Small 4 with top competitors on relevant benchmarks.

#### Capabilities and Use Cases
Mistral: Mistral Small 4 has the following capabilities:
* Text
* Function calling
* JSON mode
* Streaming
* Structured outputs

It is best suited for the following use cases:
* Chat
* Text generation
* Coding
* Analysis
* RAG pipelines
* Summarization

When choosing a model, consider the specific capabilities and use cases required for your application.

#### Cost Examples
The cost examples for Mistral: Mistral Small 4 are:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls:

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on 2024-01-01, this model is part of the standard tier and is not open source.

### Pricing Model
The pricing for Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its ability to generate human-like text, Mistral Small 4 is well-suited for chat applications and text generation tasks.
2. **Coding and Analysis**: Mistral Small 4's function calling and structured outputs capabilities make it an excellent choice for coding and analysis tasks, such as code completion and data analysis.
3. **Summarization**: The model's ability to process large amounts of text and generate concise summaries makes it a good fit for summarization tasks.
4. **RAG Pipelines**: Mistral Small 4's support for Retrieval-Augmented Generation (RAG) pipelines makes it a good choice for tasks that require generating text based on external knowledge sources.
5. **Streaming**: With its streaming capability, Mistral Small 4 can be used for real-time text processing and generation tasks, such as live chat or text-based customer support.

### Code Integration Example with OpenRouter
Here is an example of how to integrate Mistral Small 4 with OpenRouter:
```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.Model

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
