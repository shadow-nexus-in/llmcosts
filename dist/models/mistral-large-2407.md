# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-15
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, including coding, analysis, and function calling. This model boasts an impressive architecture, with a context window of 131,072 tokens and a maximum output of 4,096 tokens. Its knowledge cutoff is 2024-07, ensuring it is equipped with the latest information up to that point. Mistral Large 2 is part of the mistralai/mistral-large-2407 family, indicating its robust capabilities and extensive training.

### Technical Strengths and Use Cases
The technical strengths of Mistral Large 2 are evident in its benchmark scores: MMLU at 84.0, HumanEval at 92.0, LMSYS Arena ELO at 1225, and GSM8K at 93.0. These scores demonstrate the model's proficiency in various tasks, from coding and analysis to more complex problem-solving. Its capabilities include text and vision processing, function calling, JSON mode, streaming, and system prompts, making it versatile for applications such as coding assistance, data analysis, and multilingual support. However, it's not recommended for tasks requiring embeddings, bulk cheap processing, real-time responses under 100ms, or vision-heavy applications.

### Pricing and Cost Considerations
The pricing for Mistral Large 2 is structured as follows: $3.0 per 1M tokens for input and $9.0 per 1M tokens for output. There are no specified costs for cached input or batch input. To give developers a clearer picture, example costs include $6.0 for 1,000 calls averaging 500 tokens, $60.0 for 10,000 calls, and $600.0 for 100,000 calls. When comparing with top competitors like GPT-4

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
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale for this model.

#### Cost Structure
The pricing for Mistral Large 2 is as follows:
- **Input**: $3.0 per 1M tokens
- **Output**: $9.0 per 1M tokens
- **Cached Input**: $None per 1M tokens (indicating no additional cost for cached input tokens)
- **Batch Input**: $None per 1M tokens (suggesting no specific discount for batched input tokens)

#### Optimal Usage Scenarios
- **Cached Tokens**: Since there's no additional cost for cached input tokens, it's beneficial to use cached tokens whenever possible to minimize input costs.
- **Batch API Savings**: Although there's no specific pricing discount mentioned for batched inputs, batching can still help reduce the overall cost by minimizing the number of API calls needed. However, the exact savings would depend on the implementation and the model's ability to handle batched inputs efficiently.

#### Cost at Scale
Given the average cost examples:
- **1,000 calls (avg 500 tokens)**: $6.0
- **10,000 calls**: $60.0
- **100,000 calls**: $600.0

These costs imply a linear scaling of costs with the number of API calls. To understand the cost per token, let's calculate based on the average cost for 1,000 calls:
- Assuming an average of 500 tokens per call, 1,000 calls would process 500,000 tokens.
- The cost for 1,000 calls is $6.0, which translates to $12.0 per 1M tokens (since 500,000

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
* **HumanEval**: 92.0, measuring the model's ability to evaluate and execute human-written code, with higher scores indicating better performance.
* **LMSYS Arena ELO**: 1225, representing the model's competitive ranking in the LMSYS Arena, a platform for evaluating large language models. A higher ELO score indicates better performance compared to other models.
* **GSM8K**: 93.0, evaluating the model's performance on math problems, with higher scores indicating better math reasoning capabilities.

#### Real-World Implications
These benchmark scores have significant implications for real-world use cases:
* The high **HumanEval** score (92.0) suggests that Mistral Large 2 is well-suited for coding and programming tasks, making it a strong choice for applications that require code generation, code completion, or code review.
* The **MMLU** score (84.0) indicates that the model has a good understanding of natural language, making it suitable for tasks such as text analysis, sentiment analysis, and language translation.
* The **LMSYS Arena E

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium model released on 2024-07-24. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. This comparison will focus on its pricing, performance, and suitability against its top competitor, GPT-4o.

#### Pricing Comparison
| Model | Input Price per 1M tokens | Output Price per 1M tokens |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, whereas GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. This indicates that while GPT-4o is cheaper for input, Mistral Large 2 is more cost-effective for output.

#### Performance Trade-offs
Mistral Large 2 has the following benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

In contrast, the performance metrics for GPT-4o are not provided. However, considering the general trend that higher-priced models often perform better, it's essential to weigh the cost against the required performance.

#### Context and Limits
Mistral Large 2 has:
- Context Window: 131,072 tokens
- Max Output: 4,096 tokens
- Knowledge Cutoff: 2024-07

These specifications are not provided for GPT-4o, making a direct comparison challenging. However, the context window and max output are crucial for determining the suitability of a model for specific tasks.

#### Capabilities and Best Use Cases
Mistral Large 2 supports:
- Text
- Vision
- Function calling
- JSON mode
- Streaming
- System prompts

It is best suited for:
- Coding
- Analysis
- RAG (Retrieval-Augmented Generation)
- Agents
- Multilingual tasks
- Function calling

On the other hand

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open source model released on 2024-07-24. With its robust capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, it is best suited for tasks such as coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual support, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Given its capabilities and pricing structure, here are the top 5 best use cases for Mistral Large 2:

1. **Coding and Development**: With its high scores in HumanEval (92.0) and GSM8K (93.0), Mistral Large 2 is ideal for coding tasks, such as code completion, code review, and code generation. Its ability to understand and generate code in multiple languages makes it a valuable tool for developers.

2. **Complex Analysis and RAG**: The model's large context window (131,072 tokens) and high MMLU score (84.0) make it suitable for complex analysis tasks, including retrieval-augmented generation. This capability is particularly useful for tasks that require understanding and generating long pieces of text.

3. **Multilingual Support**: Mistral Large 2's support for multiple languages makes it an excellent choice for applications that require language translation, multilingual text generation, or language understanding.

4. **Agent-Based Systems**: With its ability to handle system prompts and function calling, Mistral Large 2 can be used to build sophisticated agent-based systems that can interact with users, understand their needs, and provide personalized responses.

5. **Streaming and Real-Time Applications**: Although not suitable for real-time applications under 100ms, Mistral Large 2's streaming capability makes it a good fit for applications that require real-time text or vision processing, such as live chatbots or

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
