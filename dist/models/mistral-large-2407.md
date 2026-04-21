# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-21
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly in coding, analysis, and multilingual tasks. This model boasts an impressive architecture that supports capabilities such as text and vision processing, function calling, JSON mode, streaming, and system prompts. With a context window of 131,072 tokens and a maximum output of 4,096 tokens, Mistral Large 2 is well-suited for complex tasks that require extensive context understanding.

### Technical Strengths and Use Cases
Mistral Large 2 demonstrates its technical prowess through its benchmark scores: 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These scores underscore its strengths in coding, analysis, and reasoning tasks. The model is best utilized for applications involving coding, analysis, retrieval-augmented generation (RAG), agents, multilingual tasks, and function calling. However, it may not be the ideal choice for tasks that require embeddings, bulk processing at low costs, real-time responses under 100ms, or vision-heavy workloads. Developers can leverage Mistral Large 2's capabilities to build sophisticated applications, but they should be aware of its limitations and pricing structure.

### Pricing and Cost Considerations
The pricing for Mistral Large 2 is structured as follows: $3.0 per 1M input tokens and $9.0 per 1M output tokens. There are no specified costs for cached input or batch input. To put this into perspective, 1,000 calls averaging 500 tokens each would cost $6.0, while 10,000 calls would amount to $60.0, and 100,000 calls would total $600.0. When comparing

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $3.0 |
| Output | $9.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Mistral Large 2
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium model released on 2024-07-24. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale for this model.

#### Cost Structure
The pricing for Mistral Large 2 is as follows:
- **Input**: $3.0 per 1M tokens
- **Output**: $9.0 per 1M tokens
- **Cached Input**: No additional cost ($None per 1M tokens)
- **Batch Input**: No additional cost ($None per 1M tokens)

#### Optimal Usage Scenarios
- **Cached Tokens**: Since there is no additional cost for cached input tokens, it is highly beneficial to utilize cached tokens whenever possible to minimize costs.
- **Batch API Savings**: Although there is no direct cost savings mentioned for batch input, batching API calls can still lead to indirect savings by reducing the overhead of individual API requests, thus optimizing resource utilization and potentially lowering overall costs.

#### Cost at Scale
The cost examples provided are based on average token usage per call:
- **1,000 calls (avg 500 tokens)**: $6.0
- **10,000 calls**: $60.0
- **100,000 calls**: $600.0

To understand the cost structure better, let's calculate the cost per call based on the provided examples:
- For 1,000 calls, the cost per call is $6.0 / 1,000 = $0.006 per call.
- For 10,000 calls, the cost per call is $60.0 / 10,000 = $0.006 per call.
- For 100,000 calls, the cost per call is $600.0 / 100,000 = $0.006 per call.

This indicates a consistent cost per call regardless

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
* **GSM8K**: 93.0, evaluating the model's math problem-solving skills.

#### Real-World Implications
These benchmark scores suggest that Mistral Large 2 is:
* Suitable for **coding** and **analysis** tasks, given its high HumanEval score.
* Effective in **multilingual** applications, due to its strong performance in MMLU.
* Capable of handling **function_calling** and **system_prompts**, making it a good fit for complex, interactive tasks.
* Less suitable for **embeddings**, **bulk_cheap**, **real_time_sub_100ms**, and **vision_heavy** applications, as indicated by its limitations.

#### Cost Analysis
The model's pricing is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium model released on 2024-07-24. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. This comparison will focus on its pricing, performance, and suitability against its top competitor, GPT-4o.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, whereas GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. This indicates that GPT-4o is cheaper for input tokens but more expensive for output tokens.

#### Performance Comparison
Mistral Large 2 has the following benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

In contrast, the benchmark scores for GPT-4o are not provided in the given data. However, based on the provided capabilities and best use cases, we can infer that Mistral Large 2 is suited for coding, analysis, RAG, agents, multilingual, and function calling tasks.

#### Performance Trade-offs
Mistral Large 2 has a context window of 131,072 tokens and a maximum output of 4,096 tokens. It is not suitable for embeddings, bulk cheap, real-time sub 100ms, or vision-heavy tasks.

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100,000 calls: $600.0

#### Choosing the Right Model
Based on the pricing and performance comparison, Mistral Large 2 is a better choice when:
* You prioritize a

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium model released on 2024-07-24. With its robust capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, it is best suited for tasks such as coding, analysis, and multilingual applications.

### Top 5 Best Use Cases for Mistral Large 2
1. **Coding and Development**: Given its high scores in HumanEval (92.0) and GSM8K (93.0), Mistral Large 2 is ideal for coding tasks, such as code completion, code review, and debugging.
2. **Complex Analysis**: With a context window of 131,072 tokens, Mistral Large 2 can handle complex, in-depth analyses, making it suitable for tasks that require understanding and processing large amounts of data.
3. **Multilingual Support**: Its capability to handle multilingual inputs makes it a great choice for applications that need to support users speaking different languages.
4. **RAG (Retrieval-Augmented Generation) Tasks**: Mistral Large 2's ability to perform function calling and its high performance in benchmarks like MMLU (84.0) and LMSYS Arena ELO (1225) make it well-suited for RAG tasks.
5. **Agent-Based Systems**: Its support for system prompts and function calling capabilities make it a good fit for developing intelligent agents that can interact with users and other systems.

### Code Integration Example with OpenRouter
To integrate Mistral Large 2 with OpenRouter for a coding task, you might use the following Python example:
```python
import openrouter

# Initialize the Mistral Large 2 model
model = openrouter.Model("mistralai/mistral-large-2407")

# Define a function to generate code based on a prompt
def generate_code(prompt):
    # Prepare the input for the model

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
