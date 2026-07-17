# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-17
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly those requiring advanced text and function calling capabilities. With its robust architecture, Mistral Large 2 is positioned as a high-tier model, offering a balance between performance and cost. The model's pricing structure includes $3.0 per 1M tokens for input and $9.0 per 1M tokens for output, with no specified costs for cached input or batch input.

### Technical Capabilities and Use Cases
Mistral Large 2 boasts an impressive set of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. Its strengths are reflected in its benchmark scores: 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These capabilities make it best suited for tasks such as coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual applications, and function calling. However, it is not recommended for embeddings, bulk cheap processing, real-time applications requiring sub-100ms responses, or vision-heavy tasks. The model's context window of 131,072 tokens and max output of 4,096 tokens provide a solid foundation for handling complex and lengthy inputs and outputs.

### Pricing and Competitiveness
The pricing model of Mistral Large 2 is designed to accommodate various usage scenarios. For example, 1,000 calls with an average of 500 tokens per call would cost $6.0, scaling up to $60.0 for 10,000 calls and $600.0 for 100,000 calls. In comparison to its top competitor, GPT-4o, which charges $2.5 per 1

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
Mistral Large 2 is a premium, non-open-source model provided by Mistral AI, released on 2024-07-24. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### Optimal Usage Scenarios
* **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
* **Batch API**: With batch input being free, batching API calls can significantly reduce costs. However, the actual cost savings will depend on the output tokens generated.

#### Cost at Scale
The cost examples provided are as follows:
* 1,000 calls (avg 500 tokens): $6.0
* 10,000 calls: $60.0
* 100,000 calls: $600.0

To estimate the cost at scale, we can calculate the cost per call:
* 1,000 calls: $6.0 / 1,000 = $0.006 per call
* 10,000 calls: $60.0 / 10,000 = $0.006 per call
* 100,000 calls: $600.0 / 100,000 = $0.006 per call

The cost per call remains constant at $0.006, indicating a linear cost structure.

#### Comparison to Top Competitors
Mistral Large 2's pricing is compared to GPT-4o:
* GPT-4o: $2.5/1M input, $10.

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 84.0 |
| HumanEval | 92.0 |
| LMSYS Arena ELO | 1225 |
| ARC | 93.0 |

## Benchmark Analysis
### Mistral Large 2 Benchmark Performance Analysis
The Mistral Large 2 model, released by Mistral AI on 2024-07-24, is a premium, non-open-source model with a unique set of capabilities and limitations. This analysis will delve into the benchmark performance of Mistral Large 2, focusing on the MMLU, HumanEval, and Arena ELO scores, and their implications for real-world use.

#### Benchmark Scores
The model's benchmark scores are as follows:
* **MMLU (Massive Multitask Language Understanding)**: 84.0
* **HumanEval**: 92.0
* **LMSYS Arena ELO**: 1225
* **GSM8K**: 93.0

These scores indicate the model's performance in various areas:
* **MMLU**: Measures the model's ability to understand and generate human-like language across a wide range of tasks. A score of 84.0 suggests that Mistral Large 2 has a strong foundation in language understanding, but may struggle with more complex or nuanced tasks.
* **HumanEval**: Evaluates the model's ability to write correct and functional code in response to prompts. A score of 92.0 indicates that Mistral Large 2 is highly proficient in coding tasks, making it a strong candidate for applications such as coding assistance or automated programming.
* **LMSYS Arena ELO**: Measures the model's performance in a competitive environment, where it is pitted against other models in a series of tasks. An ELO score of 1225 suggests that Mistral Large 2 is a strong competitor, capable of holding its own against other high-performing models.

#### Real-

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. This comparison will focus on its pricing, performance, and capabilities relative to its top competitors, specifically GPT-4o.

#### Pricing Comparison
| Model | Input Price per 1M Tokens | Output Price per 1M Tokens |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens. In contrast, GPT-4o is priced at $2.5 per 1M input tokens but $10.0 per 1M output tokens. For applications where input token count is significantly higher than output, GPT-4o might offer a cost advantage. However, for scenarios where output tokens are substantial, Mistral Large 2 could be more cost-effective.

#### Performance Trade-offs
Mistral Large 2 boasts impressive benchmarks:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

While specific benchmarks for GPT-4o are not provided, the choice between Mistral Large 2 and GPT-4o may depend on the specific use case and the importance of these benchmarked capabilities.

#### Capabilities and Best Use Cases
Mistral Large 2 supports a wide range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. It is best suited for:
- Coding
- Analysis
- RAG (Retrieval-Augmented Generation)
- Agents
- Multilingual tasks
- Function calling

However, it is not recommended for:
- Embeddings
- Bulk cheap operations
- Real-time operations under 100ms
- Vision-heavy tasks

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100,000 calls

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. With its robust capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, it is best suited for tasks such as coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual support, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Given its capabilities and pricing structure, here are the top 5 best use cases for Mistral Large 2:

1. **Coding and Development**: With its high scores in HumanEval (92.0) and GSM8K (93.0), Mistral Large 2 is particularly adept at coding tasks. It can be used for code completion, code review, and even generating code snippets based on specifications.
2. **Complex Analysis**: The model's ability to handle a context window of 131,072 tokens makes it suitable for complex analysis tasks, such as analyzing lengthy documents or providing in-depth summaries of large datasets.
3. **Multilingual Support**: Given its multilingual capabilities, Mistral Large 2 can be used for tasks that require understanding and generating text in multiple languages, making it a valuable tool for global applications.
4. **RAG (Retrieval-Augmented Generation)**: With its function calling capability, Mistral Large 2 can be integrated with external knowledge bases to retrieve information and generate text based on that information, making it useful for tasks that require up-to-date knowledge.
5. **Agent Development**: Its support for agents and system prompts allows Mistral Large 2 to be used in the development of conversational AI agents that can interact with users in a more human-like way.

### Code Integration Example with OpenRouter
To integrate Mistral Large 2 with OpenRouter for a coding task, you might use the

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
