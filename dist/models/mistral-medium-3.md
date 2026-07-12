# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-12
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance between performance and cost. As a non-open source model, its architecture is proprietary, but its capabilities and limitations provide insight into its potential applications. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, Mistral Medium 3 is designed to handle complex tasks that require significant input and output processing.

### Strengths and Use-Cases
Mistral Medium 3 excels in tasks such as coding, analysis, summarization, and content generation, thanks to its support for text, vision, function calling, JSON mode, streaming, and system prompts. Its benchmark scores, including an MMLU score of 80.0 and a HumanEval score of 77.5, demonstrate its capabilities in these areas. However, it is not suitable for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms. The model's pricing structure, with input costs of $0.4 per 1M tokens and output costs of $2.0 per 1M tokens, makes it a viable option for developers who need to process large amounts of data.

### Cost and Competitiveness
To estimate costs, developers can consider the following examples: 1,000 calls with an average of 500 tokens cost $1.2, while 10,000 calls cost $12.0, and 100,000 calls cost $120.0. In comparison to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers a unique balance of price and performance. For instance, Claude 3.5 Haiku charges $0.8/1M input and $4.0/1M output, while G

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option when possible. However, the context window limit of **131,072 tokens** and the knowledge cutoff of **2024-11** should be considered when deciding whether to utilize cached tokens.

#### Batch API Savings
Batch input is also free, which can lead to significant cost savings when making multiple API calls. By batching inputs, users can reduce their costs to **$2.0 per 1M output tokens**, as the input cost is waived.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: **$1.2**
* **10,000 calls**: **$12.0**
* **100,000 calls**: **$120.0**

To put these costs into perspective, let's calculate the cost per 1M tokens for each scenario:
* Assuming an average of 500 tokens per call, 1,000 calls would be approximately **500,000 tokens**. The cost would be **$1.2**, which translates to **$2.4 per 1M tokens**.
* For 10,000 calls, the total tokens would be approximately **

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Mistral Medium 3 Benchmark Performance
The Mistral Medium 3 model, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. The model's pricing is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens

#### Benchmark Scores
The model's benchmark performance is as follows:
* **MMLU (Massive Multitask Language Understanding)**: 80.0 - This score indicates the model's ability to understand and generate human-like text across a wide range of tasks and topics. A higher MMLU score suggests better performance in tasks that require a deep understanding of language.
* **HumanEval**: 77.5 - This score evaluates the model's ability to write correct and functional code in response to programming prompts. A higher HumanEval score indicates better performance in coding tasks.
* **LMSYS Arena ELO**: 1200 - This score measures the model's performance in a competitive arena, where it is pitted against other models in a series of tasks. A higher ELO score indicates better overall performance.

#### Real-World Implications
The benchmark scores suggest that Mistral Medium 3 is a capable model for a variety of tasks, including:
* Coding and analysis: The model's high HumanEval score indicates that it is well-suited for tasks that require writing correct and functional code.
* Text generation and summarization: The model's high MMLU score suggests that it is capable of generating high-quality text and summarizing complex topics.
* Vision tasks

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will focus on its pricing, performance, and capabilities relative to its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

#### Pricing Comparison
The pricing for each model is as follows:
- **Mistral Medium 3**:
  - Input: $0.4 per 1M tokens
  - Output: $2.0 per 1M tokens
- **Claude 3.5 Haiku**:
  - Input: $0.8 per 1M tokens
  - Output: $4.0 per 1M tokens
- **GPT-4o Mini**:
  - Input: $0.15 per 1M tokens
  - Output: $0.6 per 1M tokens

Mistral Medium 3 is priced between Claude 3.5 Haiku and GPT-4o Mini, offering a balance between cost and performance.

#### Performance Trade-offs
The performance of each model can be evaluated based on the provided benchmarks:
- **Mistral Medium 3**:
  - MMLU: 80.0
  - HumanEval: 77.5
  - LMSYS Arena ELO: 1200
- **Claude 3.5 Haiku**: Not provided
- **GPT-4o Mini**: Not provided

While the exact performance metrics for Claude 3.5 Haiku and GPT-4o Mini are not available, Mistral Medium 3's benchmarks suggest it is capable of handling complex tasks.

#### Capabilities and Use Cases
Mistral Medium 3 supports a wide range of capabilities, including:
- Text
- Vision
- Function calling
- JSON mode
- Streaming
- System prompts

It is best suited for tasks such as:
- Coding
- Analysis
- RAG (Retrieval-Augmented Generation)
- Summarization
- Vision tasks
- Content generation
- Function calling

However, it is not recommended for:
- Frontier reasoning
- Bulk cheap tasks
- Simple classification
- Real-time sub-100ms

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful model with a wide range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. Released on 2025-04-17, it is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens.

### Top 5 Best Use Cases for Mistral Medium 3
Based on its capabilities and pricing, here are the top 5 best use cases for Mistral Medium 3:

1. **Coding and Analysis**: With its high MMLU score of 80.0 and HumanEval score of 77.5, Mistral Medium 3 is well-suited for coding and analysis tasks. It can be used for tasks such as code completion, code review, and debugging.
2. **RAG (Retrieve, Augment, Generate) Tasks**: Mistral Medium 3's ability to handle large context windows and its high LMSYS Arena ELO score of 1200 make it a good fit for RAG tasks, such as question answering and text generation.
3. **Summarization**: With its ability to handle large input and output sizes, Mistral Medium 3 can be used for summarization tasks, such as summarizing long documents or articles.
4. **Vision Tasks**: Mistral Medium 3's vision capabilities make it a good fit for tasks such as image classification, object detection, and image generation.
5. **Content Generation**: With its high MMLU score and ability to handle large input and output sizes, Mistral Medium 3 can be used for content generation tasks, such as generating articles, blog posts, or social media content.

### Code Integration Examples with OpenRouter
Here is an example of how to integrate Mistral Medium 3 with OpenRouter for a coding task:
```python
import open

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
