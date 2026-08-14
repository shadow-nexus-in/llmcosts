# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-14
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly in coding, analysis, and function calling. This model boasts an impressive architecture with a context window of 131,072 tokens and a maximum output of 4,096 tokens. Its capabilities extend to text and vision processing, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Strengths and Use Cases
Mistral Large 2 demonstrates its strengths through various benchmarks, scoring 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These scores highlight its proficiency in coding and analytical tasks. The model is best utilized for applications involving coding, analysis, retrieval-augmented generation (RAG), agents, multilingual support, and function calling. However, it is not recommended for tasks requiring embeddings, bulk processing at low costs, real-time responses under 100ms, or vision-heavy applications. The pricing model is based on input and output tokens, with costs of $3.0 per 1M input tokens and $9.0 per 1M output tokens.

### Pricing and Competitiveness
The pricing of Mistral Large 2 is structured around its usage, with examples showing that 1,000 calls averaging 500 tokens cost $6.0, scaling to $60.0 for 10,000 calls and $600.0 for 100,000 calls. In comparison to its top competitors, such as GPT-4o, which charges $2.5 per 1M input tokens and $10.0 per 1M output tokens, Mistral Large 2 offers a competitive pricing model, especially considering its robust

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
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. The pricing structure is based on input and output tokens, with specific considerations for cached and batched inputs.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
- **Input**: $3.0 per 1M tokens
- **Output**: $9.0 per 1M tokens
- **Cached Input**: No additional cost ($None per 1M tokens)
- **Batch Input**: No additional cost ($None per 1M tokens)

#### When to Use Cached Tokens
Given that there is no additional cost for cached input tokens, it is advantageous to use cached tokens whenever possible. This can significantly reduce costs, especially in applications where the same inputs are processed multiple times.

#### Batch API Savings
Although the pricing data does not specify a direct discount for batched inputs, the fact that batch input costs are listed as $None per 1M tokens suggests that batch processing may not incur additional costs beyond the standard input cost. However, the exact savings from batch processing would depend on the implementation and how the model provider calculates costs for batched requests.

#### Cost at Scale
To understand the cost implications of using Mistral Large 2 at scale, let's examine the provided cost examples:
- **1,000 calls (avg 500 tokens)**: $6.0
- **10,000 calls**: $60.0
- **100,000 calls**: $600.0

These examples suggest a linear scaling of costs with the number of API calls. To estimate costs for different scenarios, we can use these examples as a basis. However, the actual cost will depend on the average number of tokens per call, as

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
The Mistral Large 2 model, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. Its pricing is structured as follows:
- Input: $3.0 per 1M tokens
- Output: $9.0 per 1M tokens

#### Benchmark Scores
The model's performance is measured by several benchmark scores:
- **MMLU (Massive Multitask Language Understanding)**: 84.0
  - This score indicates the model's ability to understand and perform a wide range of natural language processing tasks. A higher score suggests better performance in tasks such as text classification, question answering, and language translation.
- **HumanEval**: 92.0
  - This score evaluates the model's ability to generate human-like code based on a given prompt. A higher score indicates better coding capabilities, making the model more suitable for tasks like coding assistance and automated programming.
- **LMSYS Arena ELO**: 1225
  - The LMSYS Arena ELO score is a measure of the model's performance in a competitive environment, where it is pitted against other models in various tasks. A higher ELO score suggests superior performance and adaptability in real-world scenarios.
- **GSM8K**: 93.0
  - This score assesses the model's ability to solve math problems, specifically those from the Grade School Math (GSM8K) dataset. A higher score indicates better mathematical reasoning capabilities.

#### Real-World Implications
These benchmark scores have significant implications for real-world use cases:
- **Coding and Analysis**: With a high

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. This comparison will focus on its pricing, performance, and use cases against its top competitor, GPT-4o.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, while GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. For input-intensive tasks, GPT-4o is cheaper by $0.5 per 1M tokens. However, for output-intensive tasks, Mistral Large 2 is cheaper by $1.0 per 1M tokens.

#### Performance Comparison
Mistral Large 2 has the following benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

GPT-4o's benchmark scores are not provided in the data. However, based on the provided scores, Mistral Large 2 demonstrates strong performance across various tasks.

#### Context and Limits
Mistral Large 2 has a context window of 131,072 tokens and a maximum output of 4,096 tokens. Its knowledge cutoff is 2024-07.

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
- Real-time tasks with sub-100ms latency
- Vision-heavy tasks

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. With its robust capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, it's best suited for tasks such as coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual support, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Given its capabilities and limitations, here are the top 5 best use cases for Mistral Large 2, along with practical advice and code integration examples using OpenRouter:

1. **Coding and Development**: Mistral Large 2 excels in coding tasks, thanks to its high HumanEval benchmark score of 92.0. It can be used for code completion, code review, and even generating code snippets based on specifications.
   ```python
   import openrouter
   # Initialize Mistral Large 2 model
   model = openrouter.MistralLarge2()
   # Generate code snippet
   code_snippet = model.generate_code("Write a Python function to sort a list")
   print(code_snippet)
   ```

2. **Complex Analysis**: With a context window of 131,072 tokens and a high MMLU score of 84.0, Mistral Large 2 is ideal for complex text analysis tasks, such as summarizing long documents or analyzing detailed reports.
   ```python
   import openrouter
   # Initialize Mistral Large 2 model
   model = openrouter.MistralLarge2()
   # Summarize a long document
   summary = model.summarize_document("Path to your document")
   print(summary)
   ```

3. **Multilingual Support**: Given its multilingual capabilities, Mistral Large 2 can be used for tasks such as language translation, multilingual

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
