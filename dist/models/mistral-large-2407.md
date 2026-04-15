# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-15
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. This model boasts an impressive architecture with a context window of 131,072 tokens and a maximum output of 4,096 tokens. Its knowledge cutoff is 2024-07, ensuring it has a broad and up-to-date understanding of the world. With capabilities including text, vision, function calling, JSON mode, streaming, and system prompts, Mistral Large 2 is a versatile tool for developers.

### Strengths and Use Cases
Mistral Large 2 demonstrates its strengths through various benchmarks: it achieves 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These scores indicate the model's proficiency in coding, analysis, and other complex tasks. It is best utilized for coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual tasks, and function calling. However, it is not recommended for embeddings, bulk cheap processing, real-time applications requiring sub-100ms responses, or vision-heavy tasks. The pricing model, with input costing $3.0 per 1M tokens and output costing $9.0 per 1M tokens, reflects its premium tier and targeted use cases.

### Pricing and Competitiveness
The cost of using Mistral Large 2 can be estimated based on the number of calls and tokens processed. For example, 1,000 calls averaging 500 tokens each would cost $6.0, scaling up to $60.0 for 10,000 calls and $600.0 for 100,000 calls. In comparison to its top competitors, such as GPT-4o which charges $2.5/1M input and $10.0/1M

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
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. The pricing structure is based on input and output tokens, with specific considerations for cached and batch inputs.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
- **Input**: $3.0 per 1M tokens
- **Output**: $9.0 per 1M tokens
- **Cached Input**: No additional cost ($None per 1M tokens)
- **Batch Input**: No additional cost ($None per 1M tokens)

#### Using Cached Tokens
Cached tokens can be used without incurring any additional cost. This is beneficial for applications where the same input tokens are used repeatedly, as it can significantly reduce the overall cost.

#### Batch API Savings
While there is no explicit cost savings mentioned for batch inputs, the fact that batch inputs do not incur additional costs implies that using batch API calls can help optimize resource utilization and potentially reduce the overall cost by minimizing the overhead of individual API calls.

#### Cost at Scale
The cost of using Mistral Large 2 at scale can be estimated based on the provided cost examples:
- **1,000 calls (avg 500 tokens)**: $6.0
- **10,000 calls**: $60.0
- **100,000 calls**: $600.0

To calculate the cost per call, we can divide the total cost by the number of calls:
- **1,000 calls**: $6.0 / 1,000 = $0.006 per call
- **10,000 calls**: $60.0 / 10,000 = $0.006 per call
- **100,000 calls**: $600.0 / 100

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
The Mistral Large 2 model, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. It offers a range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts.

#### Pricing
The pricing for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Context and Limits
The model has the following context and limits:
* Context Window: 131,072 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2024-07

#### Benchmarks
The model's benchmark performance is as follows:
* MMLU: 84.0
* HumanEval: 92.0
* LMSYS Arena ELO: 1225
* GSM8K: 93.0

These benchmarks indicate the model's performance in various areas:
* **MMLU (Massive Multitask Language Understanding)**: A score of 84.0 indicates the model's ability to understand and generate human-like text across a wide range of tasks and domains.
* **HumanEval**: A score of 92.0 suggests the model's proficiency in evaluating and generating code that is similar to human-written code.
* **LMSYS Arena ELO**: A score of 1225 indicates the model's competitive performance in a large-scale language model benchmark, with higher scores

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium model released on 2024-07-24. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. This comparison will focus on its pricing, performance, and trade-offs against its top competitor, GPT-4o.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, whereas GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. This indicates that Mistral Large 2 is more expensive for input tokens but cheaper for output tokens compared to GPT-4o.

#### Performance Comparison
| Model | MMLU | HumanEval | LMSYS Arena ELO | GSM8K |
| --- | --- | --- | --- | --- |
| Mistral Large 2 | 84.0 | 92.0 | 1225 | 93.0 |
| GPT-4o | *Not Provided* | *Not Provided* | *Not Provided* | *Not Provided* |

Since the performance benchmarks for GPT-4o are not provided, a direct comparison cannot be made. However, Mistral Large 2 demonstrates strong performance across various benchmarks, including MMLU, HumanEval, LMSYS Arena ELO, and GSM8K.

#### Capabilities and Use Cases
Mistral Large 2 is best suited for tasks such as coding, analysis, RAG, agents, multilingual, and function calling. It is not recommended for embeddings, bulk cheap, real-time sub 100ms, or vision-heavy tasks.

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open source model released on 2024-07-24. With its robust capabilities, including text, vision, function calling, and more, it's suited for various applications. Here, we'll explore the top 5 best use cases for Mistral Large 2, along with practical advice and code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Large 2
#### 1. **Coding and Analysis**
Mistral Large 2 excels in coding tasks, thanks to its high scores in HumanEval (92.0) and GSM8K (93.0). It can be used for code review, generation, and analysis. 
```python
import openrouter

# Initialize Mistral Large 2 model
model = openrouter.MistralLarge2()

# Example coding task
code_prompt = "Write a Python function to calculate the area of a circle."
response = model.generate(code_prompt)
print(response)
```

#### 2. **RAG (Retrieval-Augmented Generation) Tasks**
With its large context window (131,072 tokens) and ability to handle function calling, Mistral Large 2 is well-suited for RAG tasks. This involves retrieving relevant information from a database and generating text based on that information.
```python
import openrouter

# Initialize Mistral Large 2 model
model = openrouter.MistralLarge2()

# Example RAG task
rag_prompt = "What are the benefits of using Mistral Large 2 for coding tasks? Retrieve information from the model's documentation."
response = model.generate(rag_prompt)
print(response)
```

#### 3. **Multilingual Support**
Mistral Large 2 supports multiple languages, making it an excellent choice for applications that require language translation or multilingual text generation.
```python
import

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
