# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-24
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly in coding, analysis, and multilingual tasks. This model boasts an architecture that supports text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers. With a context window of 131,072 tokens and a maximum output of 4,096 tokens, Mistral Large 2 is well-suited for tasks that require understanding and generating long, coherent pieces of text.

### Technical Strengths and Use Cases
The technical strengths of Mistral Large 2 are underscored by its impressive benchmark scores: MMLU at 84.0, HumanEval at 92.0, LMSYS Arena ELO at 1225, and GSM8K at 93.0. These scores indicate the model's capability in handling complex tasks, especially those involving coding and analysis. Its primary use cases include coding assistance, in-depth analysis, and tasks that benefit from its function calling and multilingual capabilities. However, it's not recommended for tasks that require embeddings, bulk processing at low costs, real-time responses under 100ms, or vision-heavy applications.

### Pricing and Cost Considerations
Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, with no specified pricing for cached input or batch input. For developers, this translates to costs such as $6.0 for 1,000 calls averaging 500 tokens, $60.0 for 10,000 calls, and $600.0 for 100,000 calls. Compared to its top competitor, GPT-4o, which offers input at $2.5/1M and output at $10.0/

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
* **Input**: $3.0 per 1M tokens
* **Output**: $9.0 per 1M tokens
* **Cached Input**: $0 per 1M tokens (free)
* **Batch Input**: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option when possible. Use cached tokens for repeated input sequences to minimize costs.

#### Batch API Savings
Batching API calls can lead to significant savings. Since batch input is free, batching large numbers of calls can reduce the average cost per call.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: $6.0
* **10,000 calls**: $60.0
* **100,000 calls**: $600.0

These costs demonstrate a linear scaling of expenses with the number of API calls.

#### Comparison to Top Competitors
Mistral Large 2's pricing can be compared to its top competitor, GPT-4o:
* **GPT-4o**:
	+ Input: $2.5 per 1M tokens
	+ Output: $10.0 per 1M tokens
Mistral Large 2's input pricing is higher than GPT-4o's, but its output pricing is lower.

#### Conclusion
Mistral Large 2 offers a unique set of capabilities and a competitive pricing

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
The Mistral Large 2 model, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. Its pricing structure is as follows:
- Input: $3.0 per 1M tokens
- Output: $9.0 per 1M tokens

#### Benchmark Scores
The model's performance is measured by the following benchmark scores:
- **MMLU (Massive Multitask Language Understanding)**: 84.0
  - MMLU scores evaluate a model's ability to understand and generate human-like text across a wide range of tasks and topics. A higher MMLU score indicates better language understanding capabilities.
- **HumanEval**: 92.0
  - HumanEval scores assess a model's ability to write correct and functional code in response to programming prompts. A higher HumanEval score suggests stronger coding capabilities.
- **LMSYS Arena ELO**: 1225
  - LMSYS Arena ELO scores measure a model's performance in a competitive environment, where models are pitted against each other to solve tasks. A higher ELO score indicates better overall performance and adaptability.
- **GSM8K**: 93.0
  - GSM8K scores evaluate a model's math problem-solving abilities, focusing on grade-school level mathematics. A higher GSM8K score suggests stronger math reasoning capabilities.

#### Real-World Implications
The benchmark scores of Mistral Large 2 imply that it is:
- **Strong in coding tasks**: With a high HumanEval score (92.0), Mistral Large 2 is well-suited for coding and programming

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

Mistral Large 2 is more expensive in terms of input tokens but slightly cheaper in terms of output tokens compared to GPT-4o.

#### Performance Trade-offs
Mistral Large 2 has the following benchmarks:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

While specific benchmark comparisons with GPT-4o are not provided, the performance of Mistral Large 2 indicates strong capabilities in coding and analytical tasks, with high scores in HumanEval and GSM8K.

#### Context and Limits
Mistral Large 2 has:
- Context Window: 131,072 tokens
- Max Output: 4,096 tokens
- Knowledge Cutoff: 2024-07

These specifications suggest that Mistral Large 2 is designed for tasks that require a large context window and moderate output length, with knowledge limited to data available up to July 2024.

#### Capabilities and Use Cases
Mistral Large 2 is best suited for:
- Coding
- Analysis
- RAG (Retrieval-Augmented Generation)
- Agents
- Multilingual tasks
- Function calling

It is not recommended for:
- Embeddings
- Bulk cheap processing
- Real-time sub-100ms applications
- Vision-heavy tasks

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model that excels in various tasks, including coding, analysis, and function calling. With its impressive benchmarks (MMLU: 84.0, HumanEval: 92.0, LMSYS Arena ELO: 1225, GSM8K: 93.0) and capabilities (text, vision, function_calling, json_mode, streaming, system_prompts), it is an ideal choice for applications requiring advanced language understanding and generation.

### Top 5 Best Use Cases for Mistral Large 2
Based on its capabilities and performance, here are the top 5 best use cases for Mistral Large 2:

1. **Coding Assistance**: With its high HumanEval score (92.0), Mistral Large 2 is well-suited for coding tasks, such as code completion, code review, and code generation. For example, you can use Mistral Large 2 with OpenRouter to generate code snippets in various programming languages.
    ```python
import openrouter

# Initialize Mistral Large 2 model
model = openrouter.Model("mistralai/mistral-large-2407")

# Generate code snippet
code_snippet = model.generate_code("Write a Python function to calculate the area of a rectangle.")
print(code_snippet)
```
2. **Text Analysis**: Mistral Large 2's high MMLU score (84.0) makes it an excellent choice for text analysis tasks, such as sentiment analysis, entity recognition, and text classification. You can use Mistral Large 2 with OpenRouter to analyze text data and extract insights.
    ```python
import openrouter

# Initialize Mistral Large 2 model
model = openrouter.Model("mistralai/mistral-large-2407")

# Analyze text data

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
