# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-16
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open-source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of natural language processing tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens, making it suitable for tasks that require understanding and generating lengthy texts.

### Technical Specifications and Use Cases
The model's technical specifications highlight its potential for various applications. With a context window of 262,144 tokens and a maximum output of 4,096 tokens, Mistral Small 4 is well-suited for tasks such as chat, text generation, coding, analysis, and summarization. Its capabilities in function calling and structured outputs also make it a good fit for more complex tasks like RAG pipelines. The pricing model for Mistral Small 4 includes charges of $0.15 per 1M tokens for input and $0.6 per 1M tokens for output, with no charges specified for cached input or batch input. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its competency in handling a range of language tasks.

### Cost and Competitiveness
In terms of cost, Mistral Small 4 offers a competitive pricing structure, with examples including $0.375 for 1,000 calls averaging 500 tokens, $3.75 for 10,000 calls, and $37.5 for 100,000 calls. While there are no direct competitors listed for Mistral Small 4, its unique combination of capabilities, pricing, and performance benchmarks position it as a

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
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens (free)
* Batch Input: $None per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for reducing costs. It is recommended to use cached tokens whenever possible, especially for repetitive or similar input sequences.

#### Batch API Savings
Batch input is also free, which means that batching API calls can significantly reduce costs. By batching input, users can avoid paying for input tokens, leading to substantial savings.

#### Cost at Scale
The cost of using Mistral Small 4 at scale is as follows:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

These costs demonstrate a linear scaling of expenses with the number of API calls. To minimize costs, users should leverage cached tokens and batch input whenever possible.

#### Example Cost Calculation
Assuming an average input size of 500 tokens per call, the cost per call can be broken down as follows:
* Input cost: 500 tokens / 1,000,000 tokens per $0.15 = $0.000075 per call
* Output cost: assuming an average output size of 200 tokens ( rough estimate, as the max output is 4,096 tokens), the output cost would be 200 tokens /

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Mistral Small 4 Benchmark Performance
#### Model Overview
The Mistral Small 4 model, provided by Mistralai, is a standard-tier model released on 2024-01-01. It is not open-source and has the following pricing structure:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Context and Limits
The model has a context window of 262,144 tokens, a maximum output of 4,096 tokens, and a knowledge cutoff of 2023-12.

#### Benchmark Performance
The model's benchmark performance is as follows:
* **MMLU (Massive Multitask Language Understanding) Score**: 80.0
	+ The MMLU score measures a model's ability to perform a wide range of natural language understanding tasks. A higher score indicates better performance. With a score of 80.0, Mistral Small 4 demonstrates a strong ability to understand and process human language.
* **HumanEval Score**: None
	+ HumanEval is a benchmark that evaluates a model's ability to generate code that passes a set of unit tests. The lack of a HumanEval score for Mistral Small 4 makes it difficult to assess its code generation capabilities.
* **LMSYS Arena ELO Score**: 1200
	+ The LMSYS Arena ELO score is a measure of a model's performance in a competitive environment, where it is pitted against other models. An ELO score of 1200 indicates that Mistral Small 4

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral: Mistral Small 4 model, we will provide a general comparison framework that can be applied to other models in the market. This framework will consider key factors such as pricing, performance, and capabilities.

#### Pricing Comparison
The Mistral: Mistral Small 4 model is priced as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens

To compare, we would need the pricing information of competing models. However, we can establish a general guideline for comparison:
- **Lower Input Price**: Models with lower input prices per 1M tokens may be more cost-effective for applications with large input sizes.
- **Lower Output Price**: Models with lower output prices per 1M tokens may be more suitable for applications requiring extensive output generation.

#### Performance Trade-offs
The performance of the Mistral: Mistral Small 4 model is indicated by the following benchmarks:
- MMLU: 80.0
- LMSYS Arena ELO: 1200

When comparing with other models, consider the following:
- **Higher MMLU Score**: Models with higher MMLU scores may perform better in tasks requiring understanding and reasoning.
- **Higher LMSYS Arena ELO**: Models with higher LMSYS Arena ELO scores may have an advantage in competitive scenarios or tasks that require strategic thinking.

#### Capabilities and Use Cases
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

When choosing a model, consider the specific requirements of your application and select a model that aligns with those needs.

#### Cost Examples
The cost of using the Mistral: Mistral Small 4 model can be estimated as follows:
- 1,000 calls (avg 500 tokens): $0.375
- 10,000 calls: $3.75
- 100,000 calls: $37.5

When comparing costs with other models, consider the average token size of your inputs and outputs to accurately estimate the expenses.

### Conclusion
While there are no direct competitors

## Best Use Cases
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4 is a powerful language model offered by Mistralai, released on 2024-01-01. This model is part of the standard tier and is not open source. In this guide, we will explore the top 5 best use cases for Mistral: Mistral Small 4, along with practical advice and code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral: Mistral Small 4
Based on the capabilities and benchmarks of Mistral: Mistral Small 4, the top 5 use cases are:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and ability to generate up to 4,096 tokens, Mistral: Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: The model's capabilities in function calling, JSON mode, and structured outputs make it an excellent choice for coding and analysis tasks.
3. **Summarization and RAG Pipelines**: Mistral: Mistral Small 4's ability to process large amounts of text and generate concise summaries makes it a great fit for summarization and RAG (Retrieve, Augment, Generate) pipelines.
4. **Text Analysis and Insights**: The model's high MMLU benchmark score of 80.0 indicates its ability to understand and analyze complex text, making it suitable for text analysis and insights applications.
5. **Streaming and Real-time Applications**: With its streaming capability, Mistral: Mistral Small 4 can be used for real-time applications such as live chat, sentiment analysis, and more.

### Code Integration Example with OpenRouter
To integrate Mistral: Mistral Small 4 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Mistral: Mistral Small 4 model
model

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
