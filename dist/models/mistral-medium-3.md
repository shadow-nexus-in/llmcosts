# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-30
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Technical Overview of Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that operates on a closed-source architecture. Its primary strengths lie in its ability to handle a wide range of tasks, including coding, analysis, and vision tasks, thanks to its capabilities in text, vision, function calling, JSON mode, streaming, and system prompts. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, Mistral Medium 3 is well-suited for complex tasks that require a deep understanding of the input context.

### Architecture and Pricing
The architecture of Mistral Medium 3 is designed to balance performance and cost. The pricing model is based on input and output tokens, with a cost of $0.4 per 1M input tokens and $2.0 per 1M output tokens. This makes it a competitive option for developers who need to process large amounts of data. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 100,000 calls would cost $120.0. In comparison to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers a unique balance of performance and cost, with a MMLU benchmark score of 80.0 and a HumanEval score of 77.5.

### Use Cases and Limitations
Mistral Medium 3 is best suited for tasks that require complex analysis, coding, and vision tasks. Its capabilities in function calling, JSON mode, and streaming make it an ideal choice for developers who need to integrate AI into their applications. However, it may not be the best option for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms. With a knowledge cutoff of 2024-

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale for this model.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
- **Input**: $0.4 per 1M tokens
- **Output**: $2.0 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

This indicates that using cached input tokens and batch API calls can significantly reduce costs, as they are provided at no additional charge.

#### Optimal Usage Scenarios
- **Cached Tokens**: Utilize cached input tokens whenever possible, as they are free. This is beneficial for applications where the input data does not change frequently or can be pre-processed and stored.
- **Batch API Calls**: Leverage batch input for processing multiple inputs simultaneously. Since batch input is free, this can lead to substantial savings for high-volume applications.

#### Cost at Scale
The cost examples provided are:
- **1,000 calls (avg 500 tokens)**: $1.2
- **10,000 calls**: $12.0
- **100,000 calls**: $120.0

To understand the cost structure better, let's calculate the cost per call:
- For 1,000 calls, the cost per call is $1.2 / 1,000 = $0.0012 per call.
- For 10,000 calls, the cost per call is $12.0 / 10,000 = $0.0012 per call.
- For 100,000 calls, the cost per call is $120.0 / 100,000 = $

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Medium 3 Benchmark Analysis
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. The model's pricing is as follows:
- Input: **$0.4 per 1M tokens**
- Output: **$2.0 per 1M tokens**

#### Benchmark Performance
The model's benchmark performance is measured by the following scores:
- **MMLU (80.0)**: The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to perform a wide range of natural language processing tasks. A higher MMLU score indicates better performance. With a score of 80.0, Mistral Medium 3 demonstrates strong language understanding capabilities.
- **HumanEval (77.5)**: The HumanEval benchmark assesses a model's ability to evaluate and execute Python code. A higher HumanEval score indicates better coding abilities. With a score of 77.5, Mistral Medium 3 shows strong coding capabilities.
- **LMSYS Arena ELO (1200)**: The LMSYS Arena ELO score measures a model's performance in a competitive environment, where models are pitted against each other to complete tasks. A higher ELO score indicates better performance. With a score of 1200, Mistral Medium 3 demonstrates competitive performance.

#### Real-World Implications
The benchmark scores suggest that Mistral Medium 3 is well-suited for tasks that require strong language understanding, coding abilities, and competitive performance. Specifically, the model is **best

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

Mistral Medium 3 is more expensive than GPT-4o Mini but cheaper than Claude 3.5 Haiku in terms of input and output costs.

#### Performance Trade-offs
The performance of each model can be evaluated using the following benchmarks:
* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

While the exact performance of Claude 3.5 Haiku and GPT-4o Mini is not available, Mistral Medium 3 demonstrates strong capabilities with an MMLU score of 80.0 and a HumanEval score of 77.5.

#### Capabilities and Use Cases
Mistral Medium 3 supports the following capabilities:
* text
* vision
* function_calling
* json_mode
* streaming
* system_prompts

It is best suited for tasks such as:
* coding
* analysis
* rag
* summarization
* vision_tasks
* content_generation
* function_calling

However, it is not recommended for:
* frontier_reasoning
* bulk_cheap_tasks


## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful language model released on 2025-04-17. With its mid-tier pricing and extensive capabilities, it's an attractive option for various applications. This guide will explore the top 5 best use cases for Mistral Medium 3, along with code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Medium 3
#### 1. **Coding and Analysis**
Mistral Medium 3 excels in coding and analysis tasks, making it ideal for applications such as code review, code generation, and debugging. Its high MMLU score of 80.0 and HumanEval score of 77.5 demonstrate its proficiency in these areas.

#### 2. **Summarization and Content Generation**
With its capabilities in text and vision, Mistral Medium 3 is well-suited for summarization and content generation tasks. Its context window of 131,072 tokens allows for processing large amounts of text, making it perfect for generating high-quality summaries and content.

#### 3. **RAG (Retrieve, Augment, Generate) Tasks**
Mistral Medium 3's ability to perform RAG tasks makes it an excellent choice for applications that require retrieving information, augmenting it, and generating new content. Its high LMSYS Arena ELO score of 1200 demonstrates its strength in these tasks.

#### 4. **Vision Tasks**
Mistral Medium 3's vision capabilities make it suitable for tasks such as image classification, object detection, and image generation. Its ability to process visual data makes it an excellent choice for applications that require computer vision.

#### 5. **Function Calling and JSON Mode**
Mistral Medium 3's function calling and JSON mode capabilities make it an excellent choice for applications that require interacting with external APIs or processing JSON data. Its ability to call functions and process JSON data

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
