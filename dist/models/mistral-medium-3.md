# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-24
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a robust set of capabilities for developers. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, this model is well-suited for tasks that require in-depth analysis and generation of content. The architecture of Mistral Medium 3 supports a wide range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts.

### Strengths and Use Cases
The main strengths of Mistral Medium 3 lie in its ability to perform complex tasks such as coding, analysis, and content generation. It also excels in vision tasks, summarization, and function calling. With a high MMLU score of 80.0 and a HumanEval score of 77.5, this model demonstrates strong performance in natural language processing and programming tasks. However, it is not recommended for frontier reasoning, bulk cheap tasks, simple classification, or real-time tasks that require sub-100ms response times. The pricing model for Mistral Medium 3 is based on input and output tokens, with costs of $0.4 per 1M input tokens and $2.0 per 1M output tokens.

### Pricing and Competitors
The pricing for Mistral Medium 3 is competitive, with estimated costs of $1.2 for 1,000 calls (avg 500 tokens), $12.0 for 10,000 calls, and $120.0 for 100,000 calls. In comparison to other models, Mistral Medium 3 is priced higher than GPT-4o Mini ($0.15/1M input, $0.6/1M output) but lower than Claude 3.5 Haiku ($0.8/1M input, $4.0/1M output).

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.4 |
| Output | $2.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Mistral Medium 3 Pricing Analysis
#### Overview
Mistral Medium 3, a mid-tier model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2025-04-17, this model is not open source. The pricing structure is based on input and output tokens, with specific rates for cached and batch inputs.

#### Cost Structure
The cost structure for Mistral Medium 3 is as follows:
* **Input**: $0.4 per 1M tokens
* **Output**: $2.0 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs when the same input is used multiple times. Since cached input is free, it is recommended to use cached tokens whenever possible, especially for repeated queries or tasks that require the same input.

#### Batch API Savings
Batch input is also free, which means that sending multiple inputs in a single API call can help reduce costs. This is particularly useful for tasks that require processing large amounts of data in parallel.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: $1.2
* **10,000 calls**: $12.0
* **100,000 calls**: $120.0

These costs are based on the average number of tokens per call and can vary depending on the actual usage.

#### Comparison with Top Competitors
Mistral Medium 3's pricing is competitive with other top models in the market. For example:
* **Claude 3.5 Haiku**: $0.8/1M input, $4.0/1M output
* **GPT-4o Mini

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Medium 3 Benchmark Performance Analysis
#### Model Overview
The Mistral Medium 3 model, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. The model's knowledge cutoff is 2024-11.

#### Pricing
The pricing for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Benchmark Performance
The model's benchmark performance is measured by the following scores:
* **MMLU (Massive Multitask Language Understanding)**: 80.0 - This score indicates the model's ability to understand and generate human-like text across a wide range of tasks and domains. A higher MMLU score suggests better performance in tasks that require a deep understanding of language.
* **HumanEval**: 77.5 - This score evaluates the model's ability to generate code that is correct and functional. A higher HumanEval score indicates better performance in coding tasks.
* **LMSYS Arena ELO**: 1200 - This score measures the model's performance in a competitive environment, where it is pitted against other models in a series of tasks. A higher ELO score suggests better overall performance.

#### Real-World Use Implications
The benchmark scores suggest that Mistral Medium 3 is a capable model for a variety of tasks, including:
* Coding: The model's high HumanEval score indicates that it is well-su

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will delve into the pricing, performance, and capabilities of Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

#### Pricing Comparison
The pricing for each model is as follows:
* **Mistral Medium 3**:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* **Claude 3.5 Haiku**:
	+ Input: $0.8 per 1M tokens
	+ Output: $4.0 per 1M tokens
* **GPT-4o Mini**:
	+ Input: $0.15 per 1M tokens
	+ Output: $0.6 per 1M tokens

Mistral Medium 3 offers a balanced pricing structure, sitting between the more expensive Claude 3.5 Haiku and the cheaper GPT-4o Mini.

#### Performance Trade-offs
The performance of each model can be evaluated using various benchmarks:
* **Mistral Medium 3**: MMLU (80.0), HumanEval (77.5), LMSYS Arena ELO (1200)
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

While the exact performance of Claude 3.5 Haiku and GPT-4o Mini is not available, Mistral Medium 3 demonstrates strong capabilities in coding, analysis, and vision tasks.

#### Capabilities and Use Cases
Mistral Medium 3 supports a wide range of capabilities, including:
* Text
* Vision
* Function calling
* JSON mode
* Streaming
* System prompts

It is best suited for tasks such as:
* Coding
* Analysis
* RAG (Retrieval-Augmented Generation)
* Summarization
* Vision tasks
* Content generation
* Function calling

However, it is not recommended for:
* Frontier reasoning
* Bulk cheap tasks
* Simple classification
* Real-time sub-100ms tasks

#### Cost Examples

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful language model with a wide range of capabilities, including text, vision, function calling, and more. Released on 2025-04-17, it offers a balance between performance and cost, making it suitable for various applications.

### Top 5 Best Use Cases for Mistral Medium 3
Based on its capabilities and limitations, here are the top 5 best use cases for Mistral Medium 3:

1. **Coding and Analysis**: With its high MMLU score of 80.0 and HumanEval score of 77.5, Mistral Medium 3 is well-suited for coding tasks, such as code completion, code review, and code analysis.
2. **Summarization and Content Generation**: Its ability to process large context windows (up to 131,072 tokens) and generate high-quality text makes it ideal for summarization and content generation tasks.
3. **Vision Tasks**: Mistral Medium 3's vision capabilities make it suitable for tasks such as image classification, object detection, and image generation.
4. **RAG (Retrieval-Augmented Generation)**: Its ability to process large context windows and generate text based on retrieved information makes it well-suited for RAG tasks.
5. **Function Calling and API Integration**: With its function calling capability, Mistral Medium 3 can be integrated with external APIs, such as OpenRouter, to perform tasks that require external data or services.

### Code Integration Example with OpenRouter
Here's an example of how to integrate Mistral Medium 3 with OpenRouter using Python:
```python
import requests

# Set up OpenRouter API endpoint
openrouter_url = "https://api.openrouter.com/v1/route"

# Set up Mistral Medium 3 API endpoint
mistral_url = "https://api.mistral.ai/v1/generate"



## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
