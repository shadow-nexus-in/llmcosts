# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-30
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly excelling in coding, analysis, and function calling tasks. With a context window of 131,072 tokens and a maximum output of 4,096 tokens, this model is well-suited for complex, multi-step tasks that require a deep understanding of the input context. Its capabilities include text and vision processing, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Architecture and Strengths
The architecture of Mistral Large 2 is not explicitly detailed, but its performance benchmarks indicate a high level of competence across various tasks. It achieves scores of 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K, demonstrating its strength in understanding and generating human-like text. The model's pricing is set at $3.0 per 1M input tokens and $9.0 per 1M output tokens, with no specified costs for cached input or batch input. This pricing model suggests that Mistral Large 2 is geared towards applications where high-quality output is valued over input volume.

### Use Cases and Cost Considerations
Mistral Large 2 is best utilized for tasks such as coding, analysis, and function calling, where its ability to understand complex contexts and generate accurate outputs is invaluable. However, it may not be the most cost-effective option for tasks that require embeddings, bulk processing, or real-time responses under 100ms. For example, 1,000 calls with an average of 500 tokens would cost $6.0, while 100,000 calls would amount to $600.0. In comparison to its top competitor, GPT-

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
Mistral Large 2 is a premium model offered by Mistral AI, released on 2024-07-24. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for repeated input sequences. If your application involves frequent reuse of input tokens, utilizing cached tokens can significantly reduce costs.

#### Batch API Savings
Batch input is also free, which means that submitting multiple inputs in a single API call does not incur additional costs. This can lead to substantial savings when processing large volumes of data. However, it's essential to consider the context window and max output limits when batching inputs.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* 1,000 API calls (avg 500 tokens): $6.0
* 10,000 API calls: $60.0
* 100,000 API calls: $600.0

To put this into perspective, the cost per API call decreases as the volume of calls increases. However, the cost per token remains constant.

#### Comparison to Top Competitors
Mistral Large 2's pricing is comparable to its top competitors, such as GPT-4o, which charges $2.5 per 1M input tokens and $10.0 per 1M output tokens. While GPT-4o is cheaper for input tokens, Mistral Large 2's free cached and batch input tokens can

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 84.0 |
| HumanEval | 92.0 |
| LMSYS Arena ELO | 1225 |
| ARC | 93.0 |

## Benchmark Analysis
### Analysis of Mistral Large 2 Benchmark Performance
#### Model Overview
The Mistral Large 2 model, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. It has a context window of 131,072 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2024-07.

#### Pricing
The pricing for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Benchmark Performance
The model's benchmark performance is:
* MMLU: 84.0
* HumanEval: 92.0
* LMSYS Arena ELO: 1225
* GSM8K: 93.0

These benchmarks indicate the model's performance in various areas:
* **MMLU (Massive Multitask Language Understanding)**: A score of 84.0 indicates the model's ability to understand and generate human-like text across a wide range of tasks and domains.
* **HumanEval**: A score of 92.0 suggests that the model is highly effective in evaluating and generating code that is similar to human-written code.
* **LMSYS Arena ELO**: A score of 1225 indicates the model's competitive performance in a variety of tasks and games, with higher scores indicating better performance.
* **GSM8K**: A score of 93.0 indicates the model's ability to solve math problems and reason abstractly.

#### Real-World

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. This comparison will focus on its pricing, performance, and capabilities relative to its top competitors, specifically GPT-4o.

#### Pricing Comparison
| Model | Input Price per 1M Tokens | Output Price per 1M Tokens |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens. In contrast, GPT-4o is priced at $2.5 per 1M input tokens but $10.0 per 1M output tokens. This indicates that while GPT-4o is cheaper for input, Mistral Large 2 is more cost-effective for output.

#### Performance Comparison
Mistral Large 2 boasts impressive benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

These scores suggest high performance in various tasks, including coding, analysis, and multilingual support. However, without direct comparison benchmarks for GPT-4o in this context, it's challenging to assess which model performs better in specific areas.

#### Capabilities and Limitations
Mistral Large 2 supports a wide range of capabilities:
- Text
- Vision
- Function calling
- JSON mode
- Streaming
- System prompts

It is best suited for tasks such as coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual tasks, and function calling. However, it is not recommended for embeddings, bulk cheap processing, real-time sub-100ms applications, or vision-heavy tasks.

#### Context and Limits
- **Context Window**: 131,072 tokens
- **Max Output**: 4,096 tokens
- **Knowledge Cutoff**: 2024-07

These specifications indicate that Mistral Large 2 can handle large contexts and generate substantial outputs, making it suitable for complex tasks. However, its knowledge cutoff in July

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, a premium model by Mistral AI, offers a wide range of capabilities including text, vision, function calling, and more. With its impressive benchmarks and large context window, it's suitable for various applications. Here are the top 5 best use cases for Mistral Large 2, along with code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Large 2
#### 1. **Coding and Development**
Mistral Large 2 excels in coding tasks, thanks to its high HumanEval score of 92.0. You can use it for code completion, code review, and even generating code snippets.
```python
import openrouter

# Initialize the Mistral Large 2 model
model = openrouter.MistralLarge2()

# Generate code snippet
prompt = "Write a Python function to sort a list of integers."
response = model.generate_text(prompt)
print(response)
```

#### 2. **Analysis and Research**
With its high MMLU score of 84.0, Mistral Large 2 is well-suited for analysis and research tasks. You can use it for text analysis, data analysis, and even generating research papers.
```python
import openrouter

# Initialize the Mistral Large 2 model
model = openrouter.MistralLarge2()

# Analyze a piece of text
prompt = "Analyze the sentiment of the following text: 'I love using Mistral Large 2.'"
response = model.generate_text(prompt)
print(response)
```

#### 3. **RAG (Retrieve, Augment, Generate) Tasks**
Mistral Large 2's large context window of 131,072 tokens makes it ideal for RAG tasks. You can use it for question answering, text summarization, and more.
```python
import openrouter

# Initialize the Mistral Large 2 model

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
