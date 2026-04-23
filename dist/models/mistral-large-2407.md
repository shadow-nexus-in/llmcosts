# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-23
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium large language model released on 2024-07-24. This model is not open source. Its architecture is designed to handle a wide range of tasks, including coding, analysis, and function calling, with a context window of 131,072 tokens and a maximum output of 4,096 tokens. The model's knowledge cutoff is 2024-07, ensuring it has access to a vast amount of information up to that point.

### Technical Strengths and Use Cases
Mistral Large 2 boasts several key strengths, including its high performance in benchmarks such as MMLU (84.0), HumanEval (92.0), LMSYS Arena ELO (1225), and GSM8K (93.0). Its capabilities extend to text, vision, function calling, JSON mode, streaming, and system prompts, making it suitable for tasks like coding, analysis, and multilingual applications. However, it is not recommended for tasks that require embeddings, bulk cheap processing, real-time sub-100ms responses, or vision-heavy applications. The pricing model is based on input and output tokens, with costs of $3.0 per 1M input tokens and $9.0 per 1M output tokens.

### Pricing and Cost Examples
The pricing for Mistral Large 2 is as follows: $3.0 per 1M input tokens and $9.0 per 1M output tokens. There are no specified costs for cached input or batch input. To give developers a better understanding of the costs involved, some examples are provided: 1,000 calls with an average of 500 tokens cost $6.0, 10,000 calls cost $60.0, and 100,000 calls cost $600.0. In comparison to its top competitors, such as GPT-4o which charges

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
Mistral Large 2, provided by Mistral AI, is a premium model released on 2024-07-24. This analysis will delve into the cost structure, optimal usage scenarios, and scalability of this model.

#### Cost Structure
The pricing for Mistral Large 2 is as follows:
- **Input**: $3.0 per 1M tokens
- **Output**: $9.0 per 1M tokens
- **Cached Input**: No additional cost per 1M tokens
- **Batch Input**: No additional cost per 1M tokens

#### Optimal Usage Scenarios
- **Cached Tokens**: Since there is no additional cost for cached input tokens, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
- **Batch API Savings**: Although there is no direct cost savings mentioned for batch input, batching API calls can still lead to indirect savings by reducing the overhead of individual API requests. However, the exact savings from batching are not provided.

#### Cost at Scale
The cost examples provided are:
- **1,000 calls (avg 500 tokens)**: $6.0
- **10,000 calls**: $60.0
- **100,000 calls**: $600.0

To understand the cost structure better, let's calculate the cost per call based on the average tokens per call:
- Assuming an average of 500 tokens per call, 1,000 calls would amount to 500,000 tokens.
- Given the input cost is $3.0 per 1M tokens, for 500,000 tokens, the input cost would be $1.5.
- Since the output cost is $9.0 per 1M tokens and assuming an average output significantly less than the input (considering the max output is 4,096 tokens), the output cost for 1,000 calls would be substantially less than

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
The Mistral Large 2 model, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. Its pricing is as follows:
- Input: $3.0 per 1M tokens
- Output: $9.0 per 1M tokens

#### Benchmark Scores
The model's performance is measured by the following benchmark scores:
- **MMLU (Massive Multitask Language Understanding)**: 84.0
  This score indicates the model's ability to understand and perform a wide range of natural language processing tasks. A higher MMLU score suggests better overall language understanding capabilities.
- **HumanEval**: 92.0
  This score evaluates the model's ability to generate human-like code. A higher HumanEval score implies that the model is more proficient in coding tasks.
- **LMSYS Arena ELO**: 1225
  The LMSYS Arena ELO score is a measure of the model's performance in a competitive environment, where it is pitted against other models. A higher ELO score indicates a stronger model.
- **GSM8K**: 93.0
  This score assesses the model's math problem-solving abilities, with a higher score indicating better performance.

#### Real-World Implications
These benchmark scores have significant implications for real-world use cases:
- **Coding and Analysis**: With a high HumanEval score, Mistral Large 2 is well-suited for coding tasks, such as code generation, code completion, and code analysis.
- **Multilingual Support**: The model's capabilities include multilingual support, making it a good

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium model released on 2024-07-24. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts, making it suitable for coding, analysis, and multilingual tasks.

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

While the benchmarks for GPT-4o are not provided, the choice between Mistral Large 2 and GPT-4o would depend on the specific requirements of the task. If the task requires strong performance in coding and analysis, Mistral Large 2 might be a better choice. However, if cost is a significant factor, GPT-4o might be more suitable.

#### Context and Limits
Mistral Large 2 has a context window of 131,072 tokens and a maximum output of 4,096 tokens. The knowledge cutoff is 2024-07. These limits should be considered when choosing a model for a specific task.

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
- Bulk cheap tasks
- Real-time tasks with latency under 100ms
- Vision-heavy tasks

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. With its robust capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, it is best suited for coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual tasks, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Given its capabilities and limitations, here are the top 5 best use cases for Mistral Large 2, along with practical advice and code integration examples using OpenRouter:

1. **Coding and Development**: Mistral Large 2 excels in coding tasks, thanks to its high HumanEval score of 92.0. It can be used for code completion, code review, and even generating code snippets based on specifications.
   ```python
   import openrouter

   # Initialize Mistral Large 2 model
   model = openrouter.MistralLarge2()

   # Example code completion task
   prompt = "Write a Python function to sort a list of integers."
   response = model.generate(prompt)
   print(response)
   ```

2. **Analysis and Research**: With its high MMLU score of 84.0, Mistral Large 2 is suitable for complex analysis tasks, including data analysis, research paper summarization, and content generation.
   ```python
   import openrouter

   # Initialize Mistral Large 2 model
   model = openrouter.MistralLarge2()

   # Example analysis task
   prompt = "Analyze the impact of climate change on global food production."
   response = model.generate(prompt)
   print(response)
   ```

3. **RAG (Retrieval-Augmented Generation)**: Mistral Large 2 supports RAG, making it ideal for tasks that require generating text based

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
