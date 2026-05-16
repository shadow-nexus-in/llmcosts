# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-16
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance between performance and cost. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, this model is well-suited for a variety of tasks, including coding, analysis, and content generation. The model's capabilities include text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Architecture and Strengths
The architecture of Mistral Medium 3 is not publicly disclosed, but its performance can be gauged from its benchmarks. It scores 80.0 on MMLU, 77.5 on HumanEval, and 1200 on LMSYS Arena ELO, indicating strong performance in coding and analysis tasks. The model's primary strengths lie in its ability to handle complex tasks, such as function calling and vision tasks, with ease. However, it is not suitable for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms.

### Pricing and Use Cases
Mistral Medium 3 is priced at $0.4 per 1M input tokens and $2.0 per 1M output tokens, making it a competitive option for developers who need a balance between performance and cost. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 100,000 calls would cost $120.0. Compared to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers a unique combination of capabilities and pricing. Developers can use this model for tasks such as coding, analysis, summarization, and content generation, but should consider alternative options for tasks that require ultra-low latency or extremely high

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
Mistral Medium 3 is a mid-tier model provided by Mistral AI, released on 2025-04-17. This model is not open source and has a specific cost structure for input and output tokens.

#### Cost Structure
The cost structure for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs when the same input tokens are used multiple times. Since cached input tokens are free, it is recommended to use them whenever possible to minimize costs.

#### Batch API Savings
Batching API calls can also help reduce costs. Although the pricing data does not provide a specific discount for batch API calls, the fact that batch input is free suggests that batching can help reduce the overall cost per call.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* 1,000 calls (avg 500 tokens): $1.2
* 10,000 calls: $12.0
* 100,000 calls: $120.0

To estimate the cost per call, we can calculate the cost per token and then multiply it by the average number of tokens per call. However, based on the provided cost examples, we can see that the cost scales linearly with the number of calls.

#### Comparison with Competitors
Mistral Medium 3's pricing can be compared to its top competitors:
* Claude 3.5 Haiku: $0.8/1M input, $4.0/1M output
* GPT-4o Mini: $0.15/1M input, $

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Medium 3 Performance Analysis
#### Model Overview
The Mistral Medium 3 model, released by Mistral AI on 2025-04-17, is a mid-tier model with the following key characteristics:
* **Tier**: Mid
* **Open Source**: False
* **Context Window**: 131,072 tokens
* **Max Output**: 16,384 tokens
* **Knowledge Cutoff**: 2024-11

#### Pricing
The pricing for Mistral Medium 3 is as follows:
* **Input**: $0.4 per 1M tokens
* **Output**: $2.0 per 1M tokens
* **Cached Input**: $None per 1M tokens
* **Batch Input**: $None per 1M tokens

#### Benchmark Performance
The model's performance is measured by the following benchmarks:
* **MMLU**: 80.0 - The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to perform a wide range of natural language processing tasks. A higher MMLU score indicates better performance.
* **HumanEval**: 77.5 - The HumanEval benchmark assesses a model's ability to generate code that is correct and functional. A higher HumanEval score indicates better coding abilities.
* **LMSYS Arena ELO**: 1200 - The LMSYS Arena ELO benchmark measures a model's performance in a competitive environment, where models are pitted against each other to complete tasks. A higher ELO score indicates better performance.

#### Real-World Implications
The benchmark scores have the following implications for real-world use:
* **MMLU**: With a score of 80

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a unique set of capabilities and pricing. This comparison will analyze its strengths and weaknesses against top competitors, Claude 3.5 Haiku and GPT-4o Mini.

#### Pricing Comparison
The pricing for each model is as follows:
* Mistral Medium 3:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* Claude 3.5 Haiku:
	+ Input: $0.8 per 1M tokens
	+ Output: $4.0 per 1M tokens
* GPT-4o Mini:
	+ Input: $0.15 per 1M tokens
	+ Output: $0.6 per 1M tokens

Mistral Medium 3 is more expensive than GPT-4o Mini but cheaper than Claude 3.5 Haiku in terms of input and output costs.

#### Performance Trade-offs
The performance of each model can be evaluated using benchmarks:
* Mistral Medium 3:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* Claude 3.5 Haiku and GPT-4o Mini benchmarks are not provided for direct comparison.

However, considering the capabilities and best use cases, Mistral Medium 3 excels in:
* Coding
* Analysis
* RAG
* Summarization
* Vision tasks
* Content generation
* Function calling

It is not suitable for:
* Frontier reasoning
* Bulk cheap tasks
* Simple classification
* Real-time sub 100ms tasks

#### Cost Examples
The cost of using Mistral Medium 3 for different numbers of calls is:
* 1,000 calls (avg 500 tokens): $1.2
* 10,000 calls: $12.0
* 100,000 calls: $120.0

#### Choosing the Right Model
Based on the pricing and performance trade-offs, consider the following scenarios:
* **Choose Mistral Medium 3** when you need a balance between performance and cost for tasks like coding, analysis, and vision tasks.
* **Choose Claude 3

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. This model is best suited for tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling.

### Top 5 Best Use Cases for Mistral Medium 3
Based on its capabilities and limitations, here are the top 5 best use cases for Mistral Medium 3:

1. **Coding and Software Development**: Mistral Medium 3 excels in coding tasks, making it an ideal choice for software development, code review, and code generation. Its ability to understand and generate code in various programming languages can significantly improve development efficiency.
2. **Data Analysis and Summarization**: With its strong analytical capabilities, Mistral Medium 3 can be used for data analysis, summarization, and insights generation. It can process large datasets, identify patterns, and provide concise summaries.
3. **Content Generation**: Mistral Medium 3's content generation capabilities make it suitable for tasks such as writing articles, blog posts, and social media content. Its ability to understand context and generate coherent text can save time and effort.
4. **Vision Tasks**: Mistral Medium 3's vision capabilities enable it to perform tasks such as image classification, object detection, and image generation. Its ability to process visual data can be useful in applications such as robotics, healthcare, and surveillance.
5. **Function Calling and API Integration**: Mistral Medium 3's function calling capability allows it to integrate with external APIs and services, making it suitable for tasks such as data processing, automation, and workflow management.

### Code Integration Example with OpenRouter
To integrate Mistral Medium 3 with OpenRouter, you can use the following code example:
```python


## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
