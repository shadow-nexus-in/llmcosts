# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-10
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly in coding, analysis, and multilingual tasks. This model boasts a context window of 131,072 tokens and can generate up to 4,096 tokens as output. With a knowledge cutoff of 2024-07, Mistral Large 2 is well-equipped to handle tasks that require a deep understanding of the subject matter up to that point in time.

### Architecture and Strengths
The architecture of Mistral Large 2 supports various capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. Its main strengths lie in its ability to perform well in coding tasks, analysis, and tasks that require the use of Rag (Retrieval-Augmented Generation), making it an ideal choice for developers and researchers working on complex projects. The model's performance is further underscored by its benchmark scores: MMLU at 84.0, HumanEval at 92.0, LMSYS Arena ELO at 1225, and GSM8K at 93.0, indicating its robustness and reliability in handling diverse tasks.

### Pricing and Use Cases
Priced at $3.0 per 1M tokens for input and $9.0 per 1M tokens for output, Mistral Large 2 is positioned as a premium offering. The cost of using this model can be estimated based on the number of calls and tokens used; for example, 1,000 calls with an average of 500 tokens would cost $6.0. While it may not be the most cost-effective option for bulk or real-time applications, its capabilities and performance make it a valuable tool for specific use cases, particularly those that require advanced coding, analysis, and function calling capabilities. Compared to competitors

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
Mistral Large 2 is a premium language model offered by Mistral AI, released on 2024-07-24. This analysis will delve into the cost structure, usage scenarios, and scalability of Mistral Large 2.

#### Cost Structure
The pricing for Mistral Large 2 is as follows:
* Input: **$3.0 per 1M tokens**
* Output: **$9.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### Usage Scenarios
* **Cached Tokens**: Since cached input tokens are free, it is recommended to use them whenever possible to reduce costs.
* **Batch API**: With batch input being free, utilizing the batch API can lead to significant savings, especially for large-scale applications.

#### Cost at Scale
The cost of using Mistral Large 2 at different scales is as follows:
* **1,000 API calls** (avg 500 tokens): **$6.0**
* **10,000 API calls**: **$60.0**
* **100,000 API calls**: **$600.0**

These costs can be broken down into input and output costs. Assuming an average of 500 tokens per call, the total tokens for each scenario would be:
* 1,000 calls: 500,000 tokens
* 10,000 calls: 5,000,000 tokens
* 100,000 calls: 50,000,000 tokens

Using the pricing structure, we can estimate the costs:
* 1,000 calls: (500,000 tokens / 1,000,000) \* $3.0 (input) + (500,000 tokens / 1,000,000) \* $9.0 (output) = **

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
The model's benchmark performance is measured by the following scores:
* **MMLU (Massive Multitask Language Understanding)**: 84.0, indicating the model's ability to understand and process multiple tasks and languages.
* **HumanEval**: 92.0, measuring the model's ability to evaluate and execute human-written code.
* **LMSYS Arena ELO**: 1225, representing the model's competitive performance in a large-scale language model benchmark.
* **GSM8K**: 93.0, evaluating the model's math problem-solving abilities.

#### Real-World Implications
These benchmark scores have significant implications for real-world use:
* The high **HumanEval** score (92.0) suggests that Mistral Large 2 is well-suited for coding and programming tasks, making it a strong choice for applications that require code execution and evaluation.
* The **MMLU** score (84.0) indicates that the model can handle multiple tasks and languages

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, offered by Mistral AI, is a premium, non-open-source model released on 2024-07-24. This comparison will focus on its pricing, performance, and capabilities in relation to its top competitors, specifically GPT-4o.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
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

These scores indicate strong performance across various tasks. However, without the benchmark scores for GPT-4o, a direct comparison of performance is not possible.

#### Capabilities and Use Cases
Mistral Large 2 supports the following capabilities:
- text
- vision
- function_calling
- json_mode
- streaming
- system_prompts

It is best suited for tasks such as:
- coding
- analysis
- rag
- agents
- multilingual
- function_calling

On the other hand, it is not recommended for:
- embeddings
- bulk_cheap
- real_time_sub_100ms
- vision_heavy

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100,000 calls: $600.0

#### Choosing Between Mistral Large 2 and GPT-4o
When deciding between Mist

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium model released on 2024-07-24. With its capabilities in text, vision, function calling, JSON mode, streaming, and system prompts, it is best suited for tasks such as coding, analysis, and function calling. This guide will explore the top 5 best use cases for Mistral Large 2, along with practical advice and code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Large 2
#### 1. **Coding Assistance**
Mistral Large 2 excels in coding tasks, thanks to its high scores in HumanEval (92.0) and GSM8K (93.0). It can be used to generate code snippets, complete partial code, or even provide explanations for coding concepts.
```python
import openrouter

# Initialize Mistral Large 2 model
model = openrouter.MistralLarge2()

# Generate code snippet
code_snippet = model.generate_code("Write a Python function to sort a list of integers.")
print(code_snippet)
```

#### 2. **Text Analysis**
With its high context window (131,072 tokens) and strong performance in MMLU (84.0), Mistral Large 2 is suitable for text analysis tasks such as sentiment analysis, entity recognition, and text summarization.
```python
import openrouter

# Initialize Mistral Large 2 model
model = openrouter.MistralLarge2()

# Analyze text sentiment
sentiment = model.analyze_sentiment("I loved the new restaurant, the food was amazing!")
print(sentiment)
```

#### 3. **RAG (Retrieve, Augment, Generate) Tasks**
Mistral Large 2's capabilities in function calling and JSON mode make it a good fit for RAG tasks, which involve retrieving information, augmenting it, and generating

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
