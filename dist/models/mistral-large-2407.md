# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-21
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly in coding, analysis, and function calling. With its robust architecture, Mistral Large 2 boasts a context window of 131,072 tokens and can generate up to 4,096 tokens as output. This model is well-suited for tasks that require in-depth understanding and generation of text, making it a valuable tool for developers.

### Technical Strengths and Use Cases
The technical strengths of Mistral Large 2 are evident in its benchmark scores: MMLU at 84.0, HumanEval at 92.0, LMSYS Arena ELO at 1225, and GSM8K at 93.0. These scores indicate the model's high proficiency in various tasks, including coding and problem-solving. Its capabilities extend to text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile model for applications such as coding assistance, data analysis, and multilingual support. However, it's not recommended for tasks that require embeddings, bulk processing at low costs, real-time responses under 100ms, or vision-heavy tasks.

### Pricing and Cost Considerations
The pricing for Mistral Large 2 is structured as follows: $3.0 per 1M input tokens and $9.0 per 1M output tokens. For developers, this translates to $6.0 for 1,000 calls with an average of 500 tokens, $60.0 for 10,000 calls, and $600.0 for 100,000 calls. In comparison to its top competitor, GPT-4o, which charges $2.5/1M input and $10.0/1M output, Mistral Large 2 offers competitive pricing for its

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
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. The pricing structure is based on input and output tokens.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs when the same input is used multiple times. Since cached input is free, it is recommended to use cached tokens whenever possible to minimize costs.

#### Batch API Savings
Batch input is also free, which means that making batch API calls can help reduce costs. By batching multiple inputs together, users can take advantage of the free batch input pricing and reduce their overall costs.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* 1,000 calls (avg 500 tokens): $6.0
* 10,000 calls: $60.0
* 100,000 calls: $600.0

To calculate the cost at scale, we can use the following formula:
Cost = (Number of calls \* Average tokens per call) \* (Input cost per 1M tokens + Output cost per 1M tokens) / 1,000,000

For example, for 1,000 calls with an average of 500 tokens per call:
Cost = (1,000 \* 500) \* ($3.0 + $9.0) / 1,000,000 = $6.0

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 84.0 |
| HumanEval | 92.0 |
| LMSYS Arena ELO | 1225 |
| ARC | 93.0 |

## Benchmark Analysis
### Mistral Large 2 Benchmark Performance Analysis
#### Model Overview
The Mistral Large 2 model, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. It is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens.

#### Benchmark Scores
The model's performance is measured by the following benchmark scores:
* **MMLU (Massive Multitask Language Understanding)**: 84.0, indicating the model's ability to understand and process natural language across a wide range of tasks.
* **HumanEval**: 92.0, measuring the model's ability to generate human-like code and solve programming tasks.
* **LMSYS Arena ELO**: 1225, representing the model's competitive performance in a large-scale language model benchmarking arena.
* **GSM8K**: 93.0, evaluating the model's math problem-solving abilities.

#### Real-World Implications
These benchmark scores suggest that the Mistral Large 2 model is:
* Suitable for coding and analysis tasks, with a high HumanEval score indicating strong programming abilities.
* Capable of handling multilingual tasks, with a high MMLU score demonstrating its language understanding capabilities.
* Competitive in large-scale language model benchmarks, as shown by its LMSYS Arena ELO score.

#### Pricing and Cost Examples
The model's pricing is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cost examples:
	+ 1,000 calls (avg 500 tokens): $6.0
	+ 10,

## Competitor Comparison
### Mistral Large 2 Comparison
#### Overview
Mistral Large 2, a premium model by Mistral AI, offers a robust set of capabilities, including text, vision, function calling, and more. Released on July 24, 2024, this model is not open source. In this comparison, we will evaluate Mistral Large 2 against its top competitor, GPT-4o, focusing on price differences, performance trade-offs, and use cases.

#### Pricing Comparison
The pricing for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens

In contrast, GPT-4o is priced at:
* Input: $2.5 per 1M tokens
* Output: $10.0 per 1M tokens

Mistral Large 2 is more expensive for input tokens but cheaper for output tokens compared to GPT-4o.

#### Performance Trade-offs
Mistral Large 2 has the following benchmarks:
* MMLU: 84.0
* HumanEval: 92.0
* LMSYS Arena ELO: 1225
* GSM8K: 93.0

While the benchmarks for GPT-4o are not provided, we can infer that Mistral Large 2 has a strong performance profile, especially in coding and analysis tasks.

#### Context and Limits
Mistral Large 2 has a context window of 131,072 tokens and a maximum output of 4,096 tokens. The knowledge cutoff is July 2024.

#### Capabilities and Use Cases
Mistral Large 2 is best suited for:
* Coding
* Analysis
* RAG (Retrieve, Augment, Generate)
* Agents
* Multilingual tasks
* Function calling

However, it is not recommended for:
* Embeddings
* Bulk cheap tasks
* Real-time tasks with sub-100ms latency
* Vision-heavy tasks

#### Cost Examples
The estimated costs for Mistral Large 2 are:
* 1,000 calls (avg 500 tokens): $6.0
* 10,000 calls: $60.0
* 100,000 calls: $600.0

#### Choosing Between Mistral Large 2 and GPT-4o
Consider the following factors when deciding between Mistral Large 2 and G

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. With its impressive benchmarks, including an MMLU score of 84.0 and a HumanEval score of 92.0, it is well-suited for a variety of tasks, particularly those involving coding, analysis, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Given its capabilities and limitations, here are the top 5 best use cases for Mistral Large 2:

1. **Coding Assistance**: With its high HumanEval score, Mistral Large 2 is ideal for coding tasks, such as code completion, code review, and code generation. Its ability to understand and generate code in multiple languages makes it a valuable tool for developers.
2. **Analysis and Rag**: Mistral Large 2's high MMLU score and context window of 131,072 tokens make it well-suited for complex analysis tasks, such as text analysis, sentiment analysis, and information retrieval.
3. **Agents and Multilingual Support**: With its support for multiple languages and ability to generate human-like text, Mistral Large 2 is ideal for building conversational agents, chatbots, and language translation systems.
4. **Function Calling and JSON Mode**: Mistral Large 2's ability to call functions and parse JSON data makes it a great choice for tasks that involve data processing, API integration, and data analysis.
5. **Streaming and System Prompts**: With its support for streaming and system prompts, Mistral Large 2 can be used for real-time data processing, live updates, and interactive systems.

### Code Integration Example with OpenRouter
To integrate Mistral Large 2 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Mistral Large 2 model
model = open

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
