# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-13
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance between performance and cost. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, this model is well-suited for a variety of tasks, including coding, analysis, and content generation. The model's capabilities include text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Architecture and Strengths
The architecture of Mistral Medium 3 is not publicly disclosed, but its performance can be gauged through its benchmark scores. With an MMLU score of 80.0, HumanEval score of 77.5, and LMSYS Arena ELO of 1200, this model demonstrates strong capabilities in coding and analysis tasks. Its pricing structure, with input costs at $0.4 per 1M tokens and output costs at $2.0 per 1M tokens, makes it a competitive option for developers who require high-quality outputs. The model's limitations, including a knowledge cutoff of 2024-11, should be considered when selecting use cases.

### Use Cases and Cost Considerations
Mistral Medium 3 is best suited for tasks that require complex analysis, coding, and content generation. Its capabilities in vision tasks, function calling, and summarization make it a strong contender for applications that require multi-modal inputs and outputs. However, it may not be the best choice for frontier reasoning, bulk cheap tasks, simple classification, or real-time tasks that require sub-100ms response times. With cost examples ranging from $1.2 for 1,000 calls to $120.0 for 100,000 calls, developers can plan their budget accordingly. Compared to its top competitors, such as Claude 3.5 Haiku and G

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
Mistral Medium 3 is a mid-tier model provided by Mistral AI, released on 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following scenarios:
* **Cached Tokens**: Use cached input tokens whenever possible, as they are free. This can significantly reduce costs for repeated or similar input queries.
* **Batch API Calls**: Take advantage of free batch input tokens by batching API calls together. This can lead to substantial cost savings for large-scale applications.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* **1,000 API Calls**: $1.2 (avg 500 tokens per call)
* **10,000 API Calls**: $12.0
* **100,000 API Calls**: $120.0

These costs can be broken down into input and output costs:
* **1,000 API Calls**: Assuming an average of 500 tokens per call, the total tokens processed would be 500,000. At $0.4 per 1M input tokens and $2.0 per 1M output tokens, the total cost would be $1.2 (calculated as: (500,000 / 1,000,000) \* $0.4 + (500,000 / 1,000,000) \* $2.0).
* **10,000 API Calls**: The total tokens

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
The Mistral Medium 3 model, provided by Mistral AI, is a mid-tier model released on 2025-04-17. It is not open source.

#### Pricing
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Context and Limits
The model has the following context and limits:
* Context Window: **131,072 tokens**
* Max Output: **16,384 tokens**
* Knowledge Cutoff: **2024-11**

#### Benchmarks
The model's benchmark performance is as follows:
* MMLU: **80.0** - This score indicates the model's ability to understand and generate human-like text. A higher score generally corresponds to better performance in natural language understanding and generation tasks.
* HumanEval: **77.5** - This score evaluates the model's ability to write correct and functional code. A higher score indicates better performance in coding tasks.
* LMSYS Arena ELO: **1200** - This score measures the model's overall performance in a competitive arena, with higher scores indicating better performance.

#### Real-World Implications
The benchmark scores suggest that Mistral Medium 3 is suitable for real-world applications that require:
* Natural language understanding and generation (e.g., text analysis, summarization, content generation)
* Coding and programming tasks (e.g., coding, function calling)
* Vision tasks (e.g

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. Here's a detailed comparison with its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

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
The performance of each model can be evaluated based on their benchmark scores:
* Mistral Medium 3:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* Claude 3.5 Haiku: Not provided
* GPT-4o Mini: Not provided

Since the benchmark scores for Claude 3.5 Haiku and GPT-4o Mini are not available, it's challenging to directly compare their performance. However, Mistral Medium 3 has a higher MMLU score than many other models, indicating its strong performance in natural language understanding tasks.

#### When to Choose Each Model
Based on the pricing and capabilities of each model, here are some guidelines on when to choose each:
* **Mistral Medium 3**: Suitable for coding, analysis, RAG, summarization, vision tasks, content generation, and function calling. Avoid using it for frontier reasoning, bulk cheap tasks, simple classification, or real-time sub-100ms tasks.
* **Claude 3.5 Haiku**: May be a good choice when high-performance and advanced capabilities are required, but the budget is not a concern. However,

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. With its capabilities in text, vision, function calling, JSON mode, streaming, and system prompts, it is best suited for tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling.

### Top 5 Best Use Cases for Mistral Medium 3
Based on its capabilities and limitations, here are the top 5 best use cases for Mistral Medium 3:

1. **Coding and Software Development**: Mistral Medium 3's ability to understand and generate code makes it an excellent choice for coding tasks. Its function calling capability allows it to interact with external systems, making it suitable for tasks that require integration with other tools.
2. **Data Analysis and Summarization**: With its ability to process large amounts of text data, Mistral Medium 3 is well-suited for data analysis and summarization tasks. Its context window of 131,072 tokens allows it to understand complex documents and generate concise summaries.
3. **Content Generation**: Mistral Medium 3's capabilities in text generation make it an excellent choice for content generation tasks such as writing articles, blog posts, or social media content.
4. **Vision Tasks**: Mistral Medium 3's ability to process visual data makes it suitable for vision tasks such as image classification, object detection, and image generation.
5. **RAG (Retrieve, Augment, Generate) Tasks**: Mistral Medium 3's ability to retrieve information from external sources, augment it with additional data, and generate new content makes it an excellent choice for RAG tasks.

### Code Integration Examples with OpenRouter
To integrate Mistral Medium 3 with OpenRouter, you can use the following code example

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
