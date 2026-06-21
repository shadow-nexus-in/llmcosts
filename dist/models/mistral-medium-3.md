# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-21
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance between performance and cost. As a non-open source model, it provides a unique set of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, Mistral Medium 3 is well-suited for a variety of tasks, including coding, analysis, and content generation.

### Architecture and Strengths
The architecture of Mistral Medium 3 is designed to support a wide range of applications, with a focus on mid-level complexity tasks. Its strengths lie in its ability to handle complex inputs and generate high-quality outputs, as evidenced by its benchmarks: MMLU (80.0), HumanEval (77.5), and LMSYS Arena ELO (1200). While it may not be the best choice for frontier reasoning, bulk cheap tasks, or simple classification, Mistral Medium 3 excels in tasks that require a balance of complexity and nuance. Its pricing model, with input costs of $0.4 per 1M tokens and output costs of $2.0 per 1M tokens, reflects its mid-tier positioning.

### Use Cases and Cost Considerations
Mistral Medium 3 is best suited for tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling. Its capabilities make it an attractive choice for developers who need a reliable and versatile model for a variety of applications. In terms of cost, Mistral Medium 3 is competitive with other mid-tier models, such as Claude 3.5 Haiku and GPT-4o Mini. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. It is not open source. The pricing structure is based on input and output tokens.

#### Cost Structure
The cost structure for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs. Since cached input tokens are free, it is recommended to use them whenever possible. This can be particularly useful for applications with repetitive input patterns.

#### Batch API Savings
Batch input tokens are also free, which means that batching API calls can help reduce costs. By sending multiple requests in a single batch, the cost of input tokens can be minimized.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: **$1.2**
* **10,000 calls**: **$12.0**
* **100,000 calls**: **$120.0**

These costs are based on the average number of tokens per call and the pricing structure.

#### Comparison with Competitors
Mistral Medium 3 can be compared to its top competitors:
* Claude 3.5 Haiku: **$0.8/1M input**, **$4.0/1M output**
* GPT-4o Mini: **$0.15/1M input**, **$0.6/1M output**

While Mistral Medium 3 has a higher input cost than GPT-4o Mini

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Mistral Medium 3 Benchmark Performance
#### Overview
Mistral Medium 3, a mid-tier model provided by Mistral AI, offers a balance of performance and cost. Released on 2025-04-17, this model is not open source.

#### Pricing
The pricing structure for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Context and Limits
The model has the following context and limits:
* Context Window: 131,072 tokens
* Max Output: 16,384 tokens
* Knowledge Cutoff: 2024-11

#### Benchmarks
The benchmark performance of Mistral Medium 3 is:
* MMLU: 80.0
* HumanEval: 77.5
* LMSYS Arena ELO: 1200
* GSM8K: None

These benchmarks indicate the model's performance in various areas:
* **MMLU (Massive Multitask Language Understanding)**: A score of 80.0 suggests that Mistral Medium 3 has strong language understanding capabilities, making it suitable for tasks that require comprehension of complex texts.
* **HumanEval**: A score of 77.5 indicates that the model is capable of generating human-like text, which is beneficial for tasks such as content generation, summarization, and coding.
* **LMSYS Arena ELO**: An ELO score of 1200 suggests that the model has a moderate level of competence in competitive tasks, such

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will examine the pricing, performance, and capabilities of Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

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

#### Performance Trade-offs
The performance of each model is measured by the following benchmarks:
* Mistral Medium 3:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* Claude 3.5 Haiku: Not provided
* GPT-4o Mini: Not provided

While the exact performance of Claude 3.5 Haiku and GPT-4o Mini is not available, Mistral Medium 3's benchmarks indicate strong capabilities in coding, analysis, and vision tasks.

#### Capabilities and Use Cases
Mistral Medium 3 is best suited for:
* Coding
* Analysis
* RAG (Retrieval-Augmented Generation)
* Summarization
* Vision tasks
* Content generation
* Function calling

It is not recommended for:
* Frontier reasoning
* Bulk cheap tasks
* Simple classification
* Real-time sub-100ms tasks

#### Cost Examples
The cost of using Mistral Medium 3 for different numbers of calls is as follows:
* 1,000 calls (avg 500 tokens):

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful language model with a wide range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. Released on 2025-04-17, this model is best suited for tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling.

### Top 5 Best Use Cases for Mistral Medium 3
Based on its capabilities and limitations, here are the top 5 best use cases for Mistral Medium 3:

1. **Coding and Code Analysis**: With its high MMLU score of 80.0 and HumanEval score of 77.5, Mistral Medium 3 is well-suited for coding tasks, such as code completion, code review, and code analysis.
2. **Text Summarization and Analysis**: The model's high context window of 131,072 tokens and max output of 16,384 tokens make it ideal for text summarization and analysis tasks, such as summarizing long documents or analyzing large datasets.
3. **Vision Tasks**: Mistral Medium 3's capability for vision tasks, such as image classification and object detection, makes it a great choice for applications that require visual understanding.
4. **Content Generation**: With its ability to generate high-quality text, Mistral Medium 3 is well-suited for content generation tasks, such as writing articles, creating chatbot responses, or generating product descriptions.
5. **Function Calling and API Integration**: The model's ability to call functions and integrate with APIs makes it a great choice for tasks that require interacting with external systems, such as data processing or workflow automation.

### Code Integration Example with OpenRouter
To integrate Mistral Medium 3 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Mistral Medium 3

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
