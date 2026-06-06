# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-06
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, including coding, analysis, and multilingual tasks. With its robust architecture, Mistral Large 2 boasts a context window of 131,072 tokens and can generate up to 4,096 output tokens. This model is part of the Mistral AI suite, specifically `mistralai/mistral-large-2407`, indicating its position within the Mistral AI model lineup.

### Technical Strengths and Use Cases
The main strengths of Mistral Large 2 lie in its versatility and performance. It supports multiple capabilities such as text, vision, function calling, JSON mode, streaming, and system prompts, making it a powerful tool for developers. Benchmarks show impressive scores: 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These scores indicate that Mistral Large 2 is best suited for tasks that require complex reasoning, coding, and analysis. However, it is not recommended for tasks that require embeddings, bulk processing at low costs, real-time responses under 100ms, or vision-heavy applications.

### Pricing and Cost Considerations
Pricing for Mistral Large 2 is structured as follows: $3.0 per 1M input tokens and $9.0 per 1M output tokens. There are no specified costs for cached input or batch input. For example, 1,000 calls averaging 500 tokens each would cost $6.0, scaling up to $60.0 for 10,000 calls and $600.0 for 100,000 calls. Compared to its top competitor, GPT-4o, which charges $2.5/1M input and

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
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. The pricing structure is based on input and output tokens, with specific rates for cached and batch inputs.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $None per 1M tokens (free)
* Batch Input: $None per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for reducing costs. Use cached tokens when:
* The input data is repetitive or has a high degree of similarity.
* The model is being used for tasks that require minimal new input, such as generating text based on a fixed prompt.

#### Batch API Savings
Batch inputs are also free, which can lead to significant cost savings when making multiple API calls. To maximize batch API savings:
* Group multiple requests together to minimize the number of API calls.
* Use batch inputs for tasks that require processing large amounts of data, such as data analysis or coding.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* 1,000 API calls (avg 500 tokens): $6.0
* 10,000 API calls: $60.0
* 100,000 API calls: $600.0

These costs demonstrate a linear scaling of costs with the number of API calls.

#### Comparison to Top Competitors
Mistral Large 2's pricing is competitive with top competitors like GPT-4o, which charges $2.5/1M input and $10.

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 84.0 |
| HumanEval | 92.0 |
| LMSYS Arena ELO | 1225 |
| ARC | 93.0 |

## Benchmark Analysis
### Mistral Large 2 Benchmark Analysis
#### Model Overview
The Mistral Large 2 model, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. It is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens.

#### Benchmark Performance
The model's benchmark performance is as follows:
* **MMLU (Massive Multitask Language Understanding) score: 84.0** - This score indicates the model's ability to understand and generate human-like text across a wide range of tasks and topics. A higher MMLU score suggests better language understanding capabilities.
* **HumanEval score: 92.0** - This score evaluates the model's ability to generate correct and functional code in response to programming prompts. A higher HumanEval score indicates superior coding capabilities.
* **LMSYS Arena ELO score: 1225** - This score measures the model's performance in a competitive arena, where it is pitted against other models in a variety of tasks. A higher ELO score suggests better overall performance and adaptability.

#### Real-World Implications
The benchmark scores suggest that the Mistral Large 2 model is well-suited for tasks that require:
* Strong language understanding and generation capabilities (e.g., coding, analysis, and text-based applications)
* Accurate and functional code generation (e.g., programming and software development)
* Adaptability and competitiveness in a variety of tasks and environments

The model's capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, make it a versatile tool for a range of applications. However, it may not

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

Mistral Large 2 is more expensive than GPT-4o in terms of input pricing but slightly cheaper in terms of output pricing.

#### Performance Trade-offs
Mistral Large 2 has the following benchmarks:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

While the specific benchmarks for GPT-4o are not provided, the choice between Mistral Large 2 and GPT-4o may depend on the specific use case and the importance of these benchmark scores.

#### Context and Limits
Mistral Large 2 has a context window of 131,072 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2024-07. These specifications are not provided for GPT-4o, but they are crucial in determining the suitability of each model for specific tasks.

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
- Real-time tasks requiring responses under 100ms
- Vision-heavy tasks

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100,000 calls

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. With its robust capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, it excels in various applications such as coding, analysis, and multilingual tasks.

### Top 5 Best Use Cases for Mistral Large 2
Given its strengths and pricing structure, here are the top 5 best use cases for Mistral Large 2:

1. **Coding and Development**: With its high scores in HumanEval (92.0) and GSM8K (93.0), Mistral Large 2 is well-suited for coding tasks, such as code completion, code review, and bug fixing. Its ability to understand and generate code in multiple languages makes it an excellent choice for development teams.
2. **Complex Analysis**: The model's large context window (131,072 tokens) and high MMLU score (84.0) make it ideal for complex analysis tasks, such as text summarization, sentiment analysis, and data analysis.
3. **RAG (Retrieval-Augmented Generation) Tasks**: Mistral Large 2's capabilities in function calling and JSON mode enable it to perform RAG tasks efficiently, such as retrieving information from external sources and generating text based on that information.
4. **Multilingual Support**: With its support for multiple languages, Mistral Large 2 is an excellent choice for applications that require language translation, language detection, or multilingual text generation.
5. **Agent-Based Systems**: The model's ability to understand and respond to system prompts makes it well-suited for agent-based systems, such as chatbots, virtual assistants, and automated customer support.

### Code Integration Example with OpenRouter
To integrate Mistral Large 2 with OpenRouter, you can use the following code example:
```python


## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
