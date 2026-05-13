# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-13
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly excelling in coding, analysis, and function calling tasks. This model boasts a context window of 131,072 tokens and can generate up to 4,096 tokens as output. With a knowledge cutoff of 2024-07, Mistral Large 2 is well-equipped to handle tasks that require extensive knowledge up to that point.

### Technical Architecture and Strengths
The architecture of Mistral Large 2 supports various capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. Its strengths are reflected in its benchmark scores: MMLU at 84.0, HumanEval at 92.0, LMSYS Arena ELO at 1225, and GSM8K at 93.0. These scores indicate the model's proficiency in understanding and generating human-like text, solving mathematical problems, and performing well in competitive arenas. The pricing model for Mistral Large 2 is based on input and output tokens, with costs set at $3.0 per 1M input tokens and $9.0 per 1M output tokens.

### Use Cases and Cost Considerations
Mistral Large 2 is best utilized for tasks such as coding, analysis, and multilingual support, where its function calling and JSON handling capabilities can be fully leveraged. However, it may not be the most suitable choice for applications requiring embeddings, bulk processing at low costs, real-time responses under 100ms, or vision-heavy tasks. The cost of using Mistral Large 2 can be estimated based on the number of calls and average token count per call. For example, 1,000 calls with an average of 500 tokens per call would cost $6.0, scaling up to $60

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $3.0 |
| Output | $9.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Mistral Large 2 Pricing Analysis
#### Overview
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. The pricing structure for Mistral Large 2 is based on input and output tokens.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for reducing costs. However, the use of cached tokens is not explicitly defined in the provided data. Generally, cached tokens can be used when the input is repeated or when the model is able to retrieve information from its cache instead of processing new input.

#### Batch API Savings
Batch input is also free, which means that making batch API calls can result in significant cost savings. By batching multiple requests together, users can avoid paying for input tokens, which can lead to substantial reductions in costs.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* 1,000 calls (avg 500 tokens): $6.0
* 10,000 calls: $60.0
* 100,000 calls: $600.0

These costs can be broken down into input and output costs. Assuming an average of 500 tokens per call, the total number of tokens for each scale is:
* 1,000 calls: 500,000 tokens
* 10,000 calls: 5,000,000 tokens
* 100,000 calls: 50,000,000 tokens



## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 84.0 |
| HumanEval | 92.0 |
| LMSYS Arena ELO | 1225 |
| ARC | 93.0 |

## Benchmark Analysis
### Mistral Large 2 Benchmark Performance Analysis
The Mistral Large 2 model, released by Mistral AI on 2024-07-24, is a premium, non-open-source model with a context window of 131,072 tokens and a maximum output of 4,096 tokens. 

#### Pricing
The pricing for Mistral Large 2 is as follows:
* Input: **$3.0 per 1M tokens**
* Output: **$9.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Benchmark Scores
The model's performance is measured by the following benchmark scores:
* **MMLU: 84.0** - The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to perform a wide range of natural language processing tasks. A higher MMLU score indicates better performance in tasks such as text classification, sentiment analysis, and question answering.
* **HumanEval: 92.0** - The HumanEval benchmark assesses a model's ability to generate code that is correct and functional. A higher HumanEval score suggests better performance in coding tasks, such as code completion and code generation.
* **LMSYS Arena ELO: 1225** - The LMSYS Arena ELO score measures a model's performance in a competitive environment, where models are pitted against each other to complete tasks. A higher ELO score indicates better performance in tasks that require strategic thinking and problem-solving.

#### Real-World Implications
The benchmark scores suggest that Mistral Large 2 is well-suited for tasks that require:


## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts, making it suitable for coding, analysis, RAG, agents, multilingual tasks, and function calling.

#### Pricing Comparison
The pricing for Mistral Large 2 is as follows:
- Input: $3.0 per 1M tokens
- Output: $9.0 per 1M tokens

In comparison, GPT-4o, a top competitor, is priced at:
- Input: $2.5 per 1M tokens
- Output: $10.0 per 1M tokens

Mistral Large 2 is more expensive than GPT-4o in terms of input tokens, but cheaper in terms of output tokens.

#### Performance Trade-offs
Mistral Large 2 has the following benchmarks:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

While the benchmarks for GPT-4o are not provided, Mistral Large 2's performance can be considered strong, especially in HumanEval and GSM8K, indicating its suitability for coding and analysis tasks.

#### Context and Limits
Mistral Large 2 has a context window of 131,072 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2024-07. These limits are not compared directly with GPT-4o, but they indicate that Mistral Large 2 is designed for tasks that require a large context window and moderate output size.

#### Capabilities and Use Cases
Mistral Large 2 is best suited for:
- Coding
- Analysis
- RAG
- Agents
- Multilingual tasks
- Function calling

It is not recommended for:
- Embeddings
- Bulk cheap tasks
- Real-time tasks with latency under 100ms
- Vision-heavy tasks

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model with a wide range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. It excels in coding, analysis, RAG, agents, multilingual tasks, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Given its capabilities and limitations, here are the top 5 best use cases for Mistral Large 2:

1. **Coding and Software Development**: With its high scores in HumanEval (92.0) and GSM8K (93.0), Mistral Large 2 is well-suited for coding tasks, such as code completion, code review, and bug detection.
2. **Data Analysis and Insights**: The model's ability to process large amounts of text data and its high MMLU score (84.0) make it an excellent choice for data analysis, report generation, and insights extraction.
3. **Multilingual Support**: Mistral Large 2's multilingual capabilities make it an ideal model for applications that require support for multiple languages, such as language translation, sentiment analysis, and text classification.
4. **Conversational Agents**: The model's high LMSYS Arena ELO score (1225) and its ability to process system prompts make it well-suited for conversational agents, chatbots, and virtual assistants.
5. **RAG (Retrieval-Augmented Generation) Tasks**: Mistral Large 2's capabilities in RAG tasks, such as question answering, text summarization, and content generation, make it an excellent choice for applications that require the retrieval and generation of text based on external knowledge sources.

### Code Integration Example with OpenRouter
To integrate Mistral Large 2 with OpenRouter, you can use the following code example:
```python
import

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
