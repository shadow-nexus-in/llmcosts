# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-04
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, including coding, analysis, and multilingual support. This model boasts an impressive architecture, with a context window of 131,072 tokens and a maximum output of 4,096 tokens. Its capabilities extend to text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Strengths and Use Cases
The technical strengths of Mistral Large 2 are underscored by its benchmark scores: MMLU at 84.0, HumanEval at 92.0, LMSYS Arena ELO at 1225, and GSM8K at 93.0. These scores indicate the model's proficiency in various tasks, from coding and analysis to multilingual support. Its primary use cases include coding, analysis, RAG (Retrieval-Augmented Generation), agents, and function calling, where its ability to handle complex inputs and generate coherent outputs is particularly valuable. However, it is not recommended for tasks requiring embeddings, bulk processing at low costs, real-time responses under 100ms, or vision-heavy applications.

### Pricing and Cost Considerations
The pricing for Mistral Large 2 is structured as follows: $3.0 per 1M input tokens and $9.0 per 1M output tokens, with no specific pricing for cached input or batch input. For developers, this translates to costs such as $6.0 for 1,000 calls averaging 500 tokens, $60.0 for 10,000 calls, and $600.0 for 100,000 calls. In comparison to its top competitor, GPT-4o, which offers $2.5/1M input and $10.0/1M output,

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
Mistral Large 2 is a premium model offered by Mistral AI, released on 2024-07-24. This analysis will delve into the cost structure, usage scenarios, and cost savings opportunities for this model.

#### Cost Structure
The pricing for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option when the same input tokens are used multiple times. This can be particularly useful in scenarios where the same prompt or context is used to generate multiple outputs.

#### Batch API Savings
Batch input is also free, which means that making batch API calls can result in significant cost savings. By batching multiple input tokens together, users can avoid paying for individual input tokens.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* 1,000 calls (avg 500 tokens): $6.0
* 10,000 calls: $60.0
* 100,000 calls: $600.0

These costs are based on the average number of tokens per call and do not take into account the use of cached or batch input tokens.

#### Comparison to Top Competitors
Mistral Large 2 is priced competitively with top competitors like GPT-4o, which costs $2.5/1M input and $10.0/1M output. While GPT-4o is cheaper for input tokens, Mistral Large 2 offers free cached and batch input tokens, which can result in significant cost savings for certain use cases.

#### Conclusion
Mistral Large 2 offers a unique

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
* **MMLU (Massive Multitask Language Understanding)**: 84.0, indicating the model's ability to understand and generate human-like language across a wide range of tasks.
* **HumanEval**: 92.0, measuring the model's ability to write correct and functional code in response to programming prompts.
* **LMSYS Arena ELO**: 1225, representing the model's competitive performance in a large-scale language model benchmarking arena.
* **GSM8K**: 93.0, evaluating the model's math problem-solving abilities.

#### Real-World Implications
These benchmark scores have significant implications for real-world use:
* The high **HumanEval** score suggests that Mistral Large 2 is well-suited for coding and programming tasks, making it a valuable tool for developers and programmers.
* The strong **MMLU** score indicates that the model can handle a wide range of language understanding tasks, such as text analysis and generation.
* The **LMSYS Arena ELO** score demonstrates the model's competitive performance in a large-scale benchmarking arena, implying that it can handle complex and challenging tasks.

#### Capabilities and Limitations
Mistral Large 2 has the following capabilities:
* **Text**: processing and generating human-like text


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

#### Performance Trade-offs
Mistral Large 2 has the following benchmarks:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

While the benchmarks for GPT-4o are not provided, the choice between Mistral Large 2 and GPT-4o may depend on the specific requirements of the task, including the balance between input and output costs, and the performance needed.

#### Context and Limits
Mistral Large 2 has:
- Context Window: 131,072 tokens
- Max Output: 4,096 tokens
- Knowledge Cutoff: 2024-07

These specifications should be considered when choosing a model, especially for tasks that require a large context window or significant output.

#### Capabilities and Best Use Cases
Mistral Large 2 is best for:
- Coding
- Analysis
- RAG
- Agents
- Multilingual tasks
- Function calling

It is not recommended for:
- Embeddings
- Bulk cheap tasks
- Real-time tasks requiring sub-100ms response times
- Vision-heavy tasks

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100,000 calls: $600.0

#### Choosing the Right Model
When deciding between Mistral Large 2 and its competitors

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. With its impressive capabilities in text, vision, function calling, JSON mode, streaming, and system prompts, it is best suited for tasks such as coding, analysis, question-answering, and multilingual support.

### Top 5 Best Use Cases for Mistral Large 2
Given its capabilities and limitations, here are the top 5 best use cases for Mistral Large 2:

1. **Coding and Development**: With its high HumanEval score of 92.0, Mistral Large 2 is ideal for coding tasks, such as code completion, code review, and code generation. Its ability to understand and generate code in multiple programming languages makes it a valuable tool for developers.
2. **Complex Analysis and Reasoning**: Mistral Large 2's high MMLU score of 84.0 and LMSYS Arena ELO score of 1225 demonstrate its ability to perform complex analysis and reasoning tasks. It can be used for tasks such as data analysis, research paper summarization, and decision-making.
3. **Multilingual Support**: With its support for multiple languages, Mistral Large 2 can be used for tasks such as language translation, language understanding, and multilingual text generation.
4. **Function Calling and API Integration**: Mistral Large 2's ability to call functions and integrate with APIs makes it ideal for tasks such as automating workflows, integrating with external services, and building custom applications.
5. **RAG (Retrieval-Augmented Generation) Tasks**: Mistral Large 2's high GSM8K score of 93.0 demonstrates its ability to perform RAG tasks, such as question-answering, text summarization, and dialogue generation.

### Code Integration Examples with OpenRouter
To integrate Mistral Large

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
