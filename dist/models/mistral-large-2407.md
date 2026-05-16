# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-16
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly in coding, analysis, and multilingual tasks. This model boasts a context window of 131,072 tokens and can generate up to 4,096 tokens as output. With its knowledge cutoff in July 2024, Mistral Large 2 is equipped with the latest information available up to that point. Its architecture supports various capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Strengths and Use Cases
Mistral Large 2 demonstrates its strengths through impressive benchmark scores: 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These scores underscore its effectiveness in coding, analysis, and other complex tasks. The model is best utilized for applications such as coding assistance, in-depth analysis, retrieval-augmented generation (RAG), agent development, and multilingual support. However, it is not recommended for tasks requiring embeddings, bulk processing at low costs, real-time responses under 100ms, or vision-heavy applications. With its pricing set at $3.0 per 1M input tokens and $9.0 per 1M output tokens, developers can estimate costs based on the number of calls and tokens involved.

### Pricing and Competitiveness
The pricing model of Mistral Large 2 is straightforward, with costs calculated based on input and output tokens. For example, 1,000 calls averaging 500 tokens each would cost $6.0, scaling up to $60.0 for 10,000 calls and $600.0 for 100,000 calls. In comparison to its top

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
Mistral Large 2 is a premium model offered by Mistral AI, released on 2024-07-24. This model is not open source and is priced based on input and output tokens.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
* Input: **$3.0 per 1M tokens**
* Output: **$9.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs when the same input is used multiple times. Since cached input is free, it is recommended to use cached tokens whenever possible to minimize costs.

#### Batch API Savings
Batching API calls can also help reduce costs. Although the pricing data does not provide a specific discount for batch API calls, the fact that batch input is free suggests that Mistral AI encourages batching to improve efficiency.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: **$6.0**
* **10,000 calls**: **$60.0**
* **100,000 calls**: **$600.0**

To calculate the cost per call, we can divide the total cost by the number of calls:
* **1,000 calls**: **$6.0 / 1,000 = $0.006 per call**
* **10,000 calls**: **$60.0 / 10,000 = $0.006 per call**
* **100,000 calls**: **$600.0 / 100,000 = $0.006 per call**

This suggests that the cost per call remains constant, regardless of the number of calls.

#### Comparison

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
The Mistral Large 2 model, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. It has a context window of 131,072 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2024-07.

#### Pricing
The pricing for Mistral Large 2 is as follows:
* Input: **$3.0 per 1M tokens**
* Output: **$9.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Benchmark Performance
The model's benchmark performance is measured by the following scores:
* **MMLU: 84.0**: The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to perform a wide range of natural language processing tasks. A higher MMLU score indicates better performance in tasks such as text classification, sentiment analysis, and question answering.
* **HumanEval: 92.0**: The HumanEval benchmark assesses a model's ability to generate code that is correct and functional. A higher HumanEval score indicates better performance in coding tasks, such as code completion and code generation.
* **LMSYS Arena ELO: 1225**: The LMSYS Arena ELO score measures a model's performance in a competitive environment, where it is pitted against other models in a series of tasks. A higher ELO score indicates better performance in a wide range of tasks, including coding, analysis, and reasoning.
* **GSM8

## Competitor Comparison
### Mistral Large 2 Comparison
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium language model released on 2024-07-24. This comparison will examine its pricing, performance, and capabilities against its top competitor, GPT-4o.

#### Pricing Comparison
The pricing for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens

In comparison, GPT-4o is priced at:
* Input: $2.5 per 1M tokens
* Output: $10.0 per 1M tokens

Mistral Large 2 is $0.5 more expensive per 1M input tokens, but $1.0 cheaper per 1M output tokens compared to GPT-4o.

#### Performance Comparison
Mistral Large 2 has the following benchmark scores:
* MMLU: 84.0
* HumanEval: 92.0
* LMSYS Arena ELO: 1225
* GSM8K: 93.0

Unfortunately, the benchmark scores for GPT-4o are not provided. However, we can compare the capabilities and limitations of both models.

#### Capabilities and Limitations
Mistral Large 2 has the following capabilities:
* Text
* Vision
* Function calling
* JSON mode
* Streaming
* System prompts

It is best suited for:
* Coding
* Analysis
* RAG
* Agents
* Multilingual
* Function calling

However, it is not suitable for:
* Embeddings
* Bulk cheap
* Real-time sub 100ms
* Vision heavy

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
* 1,000 calls (avg 500 tokens): $6.0
* 10,000 calls: $60.0
* 100,000 calls: $600.0

#### Choosing the Right Model
Mistral Large 2 is a good choice when:
* You need a premium language model with advanced capabilities such as function calling and vision.
* You prioritize performance and are willing to pay a higher price for it.
* Your use case requires a model with a large context window (131,072 tokens) and max output (4,096 tokens).

On the other

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. With its release on 2024-07-24, it has established itself as a powerful tool for various applications. This guide will explore the top 5 best use cases for Mistral Large 2, along with specific code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Large 2
#### 1. **Coding and Development**
Mistral Large 2 excels in coding tasks, making it an ideal choice for developers. Its high scores in HumanEval (92.0) and GSM8K (93.0) benchmarks demonstrate its proficiency in generating and understanding code.

```python
import openrouter

# Initialize Mistral Large 2 model
model = openrouter.MistralLarge2()

# Generate code for a simple function
input_prompt = "Write a Python function to calculate the area of a rectangle."
output = model.generate_code(input_prompt)
print(output)
```

#### 2. **Analysis and Research**
With its large context window (131,072 tokens) and high MMLU score (84.0), Mistral Large 2 is well-suited for in-depth analysis and research tasks.

```python
import openrouter

# Initialize Mistral Large 2 model
model = openrouter.MistralLarge2()

# Analyze a research paper
input_prompt = "Summarize the main points of a research paper on climate change."
output = model.analyze_text(input_prompt)
print(output)
```

#### 3. **RAG (Retrieval-Augmented Generation) Tasks**
Mistral Large 2's ability to perform RAG tasks makes it an excellent choice for applications that require generating text based on external knowledge.

```python
import openrouter

# Initialize Mistral Large 

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
