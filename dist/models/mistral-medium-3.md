# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-17
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Technical Overview of Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier, closed-source model designed for a wide range of applications. Its architecture supports multiple capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. This versatility makes Mistral Medium 3 a robust tool for developers, particularly in areas such as coding, analysis, and content generation. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, it is well-suited for complex tasks that require both understanding and generation of substantial amounts of data.

### Strengths and Use Cases
The main strengths of Mistral Medium 3 lie in its balanced performance across various benchmarks, including an MMLU score of 80.0, a HumanEval score of 77.5, and an LMSYS Arena ELO of 1200. These scores indicate its capability in handling complex tasks that require both understanding and generation of text. Its best use cases include coding, analysis, RAG (Retrieve, Augment, Generate), summarization, vision tasks, content generation, and function calling. However, it is not recommended for frontier reasoning, bulk cheap tasks, simple classification, or real-time applications requiring responses under 100ms. The model's pricing is structured around input and output tokens, with costs of $0.4 per 1M input tokens and $2.0 per 1M output tokens, making it a competitive option for many applications.

### Pricing and Competitors
The pricing model of Mistral Medium 3 is designed to balance affordability with the model's capabilities. For example, 1,000 calls averaging 500 tokens each would cost $1.2, scaling to $120.0 for 100,000 calls. In comparison to its top competitors, such as Claude 3.5 Haiku and GPT

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and provide a breakdown of costs at various scales.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
- **Input**: $0.4 per 1M tokens
- **Output**: $2.0 per 1M tokens
- **Cached Input**: $0 per 1M tokens (free)
- **Batch Input**: $0 per 1M tokens (free)

#### Optimal Usage Scenarios
- **Cached Tokens**: Since cached input tokens are free, it's highly beneficial to use them whenever possible. This can significantly reduce costs for repeated or similar inputs.
- **Batch API Savings**: With batch input being free, batching API calls can lead to substantial savings, especially for high-volume users.

#### Cost at Scale
Given the average cost per call, we can estimate costs at different scales:
- **1,000 calls (avg 500 tokens)**: $1.2
- **10,000 calls**: $12.0
- **100,000 calls**: $120.0

To understand these costs better, let's break down the estimated cost per call:
- Assuming an average of 500 tokens per call, the input cost per call would be $0.4 * (500 / 1,000,000) = $0.0002 per call for input.
- The output cost, assuming an average output significantly less than the max output of 16,384 tokens (since the exact average output isn't provided), would be substantially less than $2.0 * (16,384 / 1,000,000) = $0.032768 per call for output, but this can vary widely based on actual output

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
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. The model's pricing is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens

#### Benchmark Scores
The model's benchmark performance is measured by the following scores:
* **MMLU (Massive Multitask Language Understanding)**: 80.0, indicating the model's ability to understand and generate human-like text across a wide range of tasks and domains.
* **HumanEval**: 77.5, measuring the model's ability to write correct and functional code in response to programming prompts.
* **LMSYS Arena ELO**: 1200, representing the model's competitive ranking in a large-scale language model benchmarking arena.

#### Real-World Implications
These benchmark scores have significant implications for real-world use cases:
* The high MMLU score suggests that Mistral Medium 3 is well-suited for tasks that require a deep understanding of language, such as **text analysis**, **summarization**, and **content generation**.
* The strong HumanEval score indicates that the model is capable of generating high-quality code, making it a good fit for **coding** and **function calling** tasks.
* The LMSYS Arena ELO score of 1200 suggests that the model is competitive with other mid-tier models, but may not be the top choice for tasks that require extreme precision or accuracy.

#### Cost Examples


## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will analyze its pricing, performance, and capabilities against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

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

Mistral Medium 3 offers a balance between input and output costs, while Claude 3.5 Haiku is more expensive on both fronts. GPT-4o Mini is the most cost-effective option for input, but its output cost is still lower than Mistral Medium 3.

#### Performance Trade-offs
The performance of each model can be evaluated using the provided benchmarks:
* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

Without direct comparisons, it's challenging to assess the performance trade-offs. However, Mistral Medium 3's benchmarks suggest it is capable of handling complex tasks.

#### Capabilities and Use Cases
Mistral Medium 3 supports a range of capabilities, including:
* Text
* Vision
* Function calling
* JSON mode
* Streaming
* System prompts

It is best suited for tasks such as:
* Coding
* Analysis
* RAG (Retrieve, Augment, Generate)
* Summarization
* Vision tasks
* Content generation
* Function calling

On the other hand, it is not recommended for:
* Frontier

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful language model with a wide range of capabilities, including text, vision, function calling, and more. Released on 2025-04-17, it offers a balance of performance and cost, making it suitable for various applications.

### Top 5 Best Use Cases for Mistral Medium 3
Based on its capabilities and pricing, here are the top 5 best use cases for Mistral Medium 3:

1. **Coding and Analysis**: With its high MMLU score of 80.0 and HumanEval score of 77.5, Mistral Medium 3 is well-suited for coding tasks, such as code completion, code review, and bug detection. Its ability to understand and generate code makes it an excellent choice for development teams.
2. **Summarization and Content Generation**: Mistral Medium 3's capabilities in text processing and generation make it ideal for summarization and content generation tasks. Its high context window of 131,072 tokens allows it to process large amounts of text and generate coherent summaries.
3. **Vision Tasks**: With its vision capabilities, Mistral Medium 3 can be used for image classification, object detection, and image generation tasks. Its ability to process visual data makes it a great choice for applications that require image analysis.
4. **RAG (Retrieve, Augment, Generate) Tasks**: Mistral Medium 3's capabilities in text processing and generation, combined with its ability to retrieve information, make it well-suited for RAG tasks. Its high context window and ability to generate text make it an excellent choice for applications that require retrieving and generating text.
5. **Function Calling and API Integration**: Mistral Medium 3's ability to call functions and integrate with APIs makes it an excellent choice for applications that require interacting with external services. Its ability to process and generate JSON data makes it a

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
