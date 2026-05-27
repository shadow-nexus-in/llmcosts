# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-27
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance between performance and cost. As a non-open source model, it is designed to provide a robust set of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, Mistral Medium 3 is well-suited for a variety of tasks, including coding, analysis, and content generation.

### Architecture and Strengths
The architecture of Mistral Medium 3 is not publicly disclosed, but its performance can be gauged through its benchmark scores. With an MMLU score of 80.0, HumanEval score of 77.5, and LMSYS Arena ELO of 1200, Mistral Medium 3 demonstrates strong capabilities in natural language processing and generation. Its primary strengths lie in its ability to handle complex tasks, such as coding and analysis, with a high degree of accuracy. Additionally, its support for vision tasks and function calling makes it a versatile model for a wide range of applications.

### Pricing and Use Cases
Mistral Medium 3 is priced at $0.4 per 1M input tokens and $2.0 per 1M output tokens. This makes it a competitive option for developers who require a high-performance model for tasks such as coding, summarization, and content generation. However, it may not be the best choice for bulk cheap tasks, simple classification, or real-time applications that require sub-100ms response times. As shown in the cost examples, 1,000 calls with an average of 500 tokens would cost $1.2, while 100,000 calls would cost $120.0. Compared to its top competitors, such as Claude 3.5 Haiku and

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.4 |
| Output | $2.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Mistral Medium 3
#### Overview
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### Optimal Usage Scenarios
* **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
* **Batch API Calls**: With batch input being free, batching API calls can lead to significant cost savings, especially for large-scale applications.

#### Cost at Scale
The cost examples provided are as follows:
* **1,000 calls (avg 500 tokens)**: **$1.2**
* **10,000 calls**: **$12.0**
* **100,000 calls**: **$120.0**

To estimate the cost at scale, we can calculate the cost per call:
* **1,000 calls**: $1.2 / 1,000 calls = **$0.0012 per call**
* **10,000 calls**: $12.0 / 10,000 calls = **$0.0012 per call**
* **100,000 calls**: $120.0 / 100,000 calls = **$0.0012 per call**

The cost per call remains constant at **$0.0012**, indicating a linear pricing model.

#### Comparison with Top Competitors
Mistral Medium 3's pricing can be compared to its top competitors:


## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Medium 3 Benchmark Performance Analysis
#### Overview
Mistral Medium 3 is a mid-tier model released by Mistral AI on 2025-04-17. This analysis will delve into its benchmark performance, focusing on MMLU, HumanEval, and Arena ELO scores, and explore their implications for real-world use.

#### Benchmark Scores
The model's benchmark scores are as follows:
* **MMLU (Massive Multitask Language Understanding)**: 80.0
* **HumanEval**: 77.5
* **LMSYS Arena ELO**: 1200

These scores indicate the model's capabilities in various areas:
* **MMLU**: Measures the model's ability to understand and generate human-like text across a wide range of tasks. A score of 80.0 suggests that Mistral Medium 3 has a strong foundation in language understanding.
* **HumanEval**: Evaluates the model's ability to write correct and functional code. A score of 77.5 indicates that the model is proficient in coding tasks, but may struggle with more complex or nuanced problems.
* **LMSYS Arena ELO**: Assesses the model's performance in a competitive environment, where it is pitted against other models. An ELO score of 1200 suggests that Mistral Medium 3 is a mid-tier model, capable of holding its own against other models in its class.

#### Real-World Implications
The benchmark scores have significant implications for real-world use:
* **Coding and analysis tasks**: Mistral Medium 3's strong MMLU and HumanEval scores make it well-suited for coding and analysis tasks, such as code generation, code review,

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance of performance and pricing. In this comparison, we will evaluate Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini, in terms of pricing, performance, and use cases.

#### Pricing Comparison
The pricing for each model is as follows:
* Mistral Medium 3:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* Claude 3.5 Haiku:
	+ Input: $0.8 per 1M tokens (100% more than Mistral Medium 3)
	+ Output: $4.0 per 1M tokens (100% more than Mistral Medium 3)
* GPT-4o Mini:
	+ Input: $0.15 per 1M tokens (62.5% less than Mistral Medium 3)
	+ Output: $0.6 per 1M tokens (70% less than Mistral Medium 3)

#### Performance Comparison
The performance of each model can be evaluated based on the provided benchmarks:
* Mistral Medium 3:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* Claude 3.5 Haiku: Not provided
* GPT-4o Mini: Not provided

However, based on the pricing, we can infer that Claude 3.5 Haiku may offer higher performance, but at a significant cost increase. GPT-4o Mini, on the other hand, may offer lower performance, but at a substantially lower cost.

#### Use Case Comparison
Mistral Medium 3 is best suited for:
* Coding
* Analysis
* RAG
* Summarization
* Vision tasks
* Content generation
* Function calling

It is not recommended for:
* Frontier reasoning
* Bulk cheap tasks
* Simple classification
* Real-time sub 100ms tasks

Claude 3.5 Haiku and GPT-4o Mini may have different use case recommendations, but based on their pricing, Claude 3.5 Haiku may be more suitable

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful language model released on 2025-04-17. It is classified as a mid-tier model and is not open source. With its capabilities in text, vision, function calling, JSON mode, streaming, and system prompts, it is best suited for tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling.

### Top 5 Best Use Cases for Mistral Medium 3
Based on its capabilities and limitations, here are the top 5 best use cases for Mistral Medium 3:

1. **Coding and Development**: Mistral Medium 3 excels in coding tasks, making it an ideal choice for developers who need assistance with code completion, code review, and code generation. Its ability to understand and generate code in various programming languages makes it a valuable tool for development teams.
2. **Data Analysis and Summarization**: With its strong text analysis capabilities, Mistral Medium 3 can be used to analyze large datasets, identify patterns, and generate summaries of complex data. This makes it an excellent choice for data analysts and scientists who need to extract insights from large datasets.
3. **Content Generation**: Mistral Medium 3's capabilities in content generation make it an ideal choice for content creators, writers, and marketers who need to generate high-quality content quickly. Its ability to understand context and generate coherent text makes it a valuable tool for content generation tasks.
4. **Vision Tasks**: Mistral Medium 3's vision capabilities make it suitable for tasks such as image classification, object detection, and image generation. Its ability to understand and generate visual content makes it an excellent choice for applications that require visual analysis and generation.
5. **Function Calling and API Integration**: Mistral Medium 3's ability to call functions and integrate with APIs makes it an ideal choice for applications that require integration with external

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
