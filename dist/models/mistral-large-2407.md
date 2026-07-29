# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-29
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly excelling in coding, analysis, and function calling tasks. This model boasts a context window of 131,072 tokens and can generate up to 4,096 tokens as output. With a knowledge cutoff of 2024-07, Mistral Large 2 is equipped with the latest information available up to that point.

### Technical Architecture and Strengths
The architecture of Mistral Large 2 supports multiple capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. Its strengths are reflected in its benchmark scores: 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These scores indicate the model's high performance in various tasks, making it suitable for applications that require advanced language understanding and generation. However, it's worth noting that Mistral Large 2 is not recommended for tasks that require embeddings, bulk cheap processing, real-time responses under 100ms, or vision-heavy applications.

### Pricing and Use Cases
Pricing for Mistral Large 2 is structured as follows: $3.0 per 1M input tokens and $9.0 per 1M output tokens. There are no specified costs for cached input or batch input. To give developers a better understanding of the costs, examples are provided: 1,000 calls averaging 500 tokens cost $6.0, scaling up to $60.0 for 10,000 calls and $600.0 for 100,000 calls. Compared to its top competitor, GPT-4o, which charges $2.5/1M input and $10.0/1M output, Mist

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
Mistral Large 2, provided by Mistral AI, is a premium model released on 2024-07-24. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following strategies:
* **Cached Tokens**: Utilize cached input tokens whenever possible, as they are free. This is ideal for applications with repetitive or similar input sequences.
* **Batch API Calls**: Leverage batch input to reduce the number of API calls, as batch input is also free. This approach is suitable for applications that can process multiple inputs simultaneously.

#### Cost at Scale
The cost of using Mistral Large 2 at various scales is as follows:
* **1,000 API Calls**: $6.0 (avg 500 tokens per call)
* **10,000 API Calls**: $60.0
* **100,000 API Calls**: $600.0

To put these costs into perspective, let's calculate the cost per token:
* Assuming an average of 500 tokens per call, the cost per token is:
	+ $6.0 / (1,000 calls \* 500 tokens/call) = $0.012 per token (1,000 calls)
	+ $60.0 / (10,000 calls \* 500 tokens/call) = $0.012 per token (10,000 calls)
	+ $600.0 / (100,000 calls \* 500 tokens/call) = $

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
* **MMLU (Massive Multitask Language Understanding)**: 84.0, indicating the model's ability to understand and process a wide range of natural language tasks.
* **HumanEval**: 92.0, measuring the model's ability to evaluate and execute human-written code, with higher scores indicating better performance.
* **LMSYS Arena ELO**: 1225, representing the model's competitive ranking in the LMSYS Arena, a benchmark for language models. A higher ELO score indicates better performance compared to other models.
* **GSM8K**: 93.0, evaluating the model's performance on a specific math problem-solving benchmark.

#### Real-World Implications
These benchmark scores have significant implications for real-world use:
* The high **HumanEval** score (92.0) suggests that Mistral Large 2 is well-suited for coding and programming tasks, making it a strong choice for applications involving code generation, code review, or automated programming.
* The **MMLU** score (84.0) indicates that the model has a strong foundation in natural language understanding, making it suitable for tasks like text analysis, sentiment analysis, or language translation.
* The **LMSYS Arena ELO** score (1225) provides a relative

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts, making it suitable for coding, analysis, and multilingual tasks.

#### Pricing Comparison
The pricing for Mistral Large 2 is as follows:
- Input: $3.0 per 1M tokens
- Output: $9.0 per 1M tokens

In comparison, GPT-4o, a top competitor, is priced at:
- Input: $2.5 per 1M tokens
- Output: $10.0 per 1M tokens

Mistral Large 2 is more expensive in terms of input cost but slightly cheaper in terms of output cost compared to GPT-4o.

#### Performance Trade-offs
Mistral Large 2 has the following benchmarks:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

While specific benchmark comparisons with GPT-4o are not provided, Mistral Large 2's performance metrics indicate strong capabilities in coding, analysis, and other areas it is best suited for.

#### Context and Limits
Mistral Large 2 has:
- Context Window: 131,072 tokens
- Max Output: 4,096 tokens
- Knowledge Cutoff: 2024-07

These specifications are not directly compared to GPT-4o in the provided data, but they are crucial for understanding the model's limitations and potential applications.

#### Capabilities and Best Use Cases
Mistral Large 2 is capable of:
- Text
- Vision
- Function calling
- JSON mode
- Streaming
- System prompts

It is best for:
- Coding
- Analysis
- RAG (Retrieval-Augmented Generation)
- Agents
- Multilingual tasks
- Function calling

However, it is not recommended for:
- Embeddings
- Bulk cheap tasks
- Real-time sub 100ms tasks
- Vision-heavy tasks

#### Cost Examples
For Mistral Large 2, the estimated costs are:
- 1,000 calls (avg 500 tokens

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model that excels in various tasks, including coding, analysis, and function calling. With its capabilities in text, vision, and function calling, it's an ideal choice for applications requiring advanced language understanding and generation.

### Top 5 Best Use Cases for Mistral Large 2
Given its strengths and pricing, here are the top 5 best use cases for Mistral Large 2:

1. **Advanced Coding Assistance**: With a high HumanEval score of 92.0, Mistral Large 2 is well-suited for coding tasks, such as code completion, debugging, and optimization. Its ability to understand and generate code in multiple languages makes it an excellent tool for developers.
2. **In-Depth Analysis and Research**: The model's high MMLU score of 84.0 and context window of 131,072 tokens enable it to perform in-depth analysis and research tasks, such as text summarization, sentiment analysis, and data extraction.
3. **RAG (Retrieve, Augment, Generate) Tasks**: Mistral Large 2's capabilities in text and function calling make it an ideal choice for RAG tasks, which involve retrieving information, augmenting it, and generating new content.
4. **Multilingual Support**: With its support for multiple languages, Mistral Large 2 is well-suited for applications requiring language translation, localization, and cultural adaptation.
5. **Agent-Based Systems**: The model's ability to understand and generate text, combined with its function calling capabilities, makes it an excellent choice for building agent-based systems, such as chatbots, virtual assistants, and autonomous agents.

### Code Integration Example with OpenRouter
To integrate Mistral Large 2 with OpenRouter, you can use the following code example:
```python
import openrouter

#

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
