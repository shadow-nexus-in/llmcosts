# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-01
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, including coding, analysis, and multilingual tasks. With a context window of 131,072 tokens and a maximum output of 4,096 tokens, this model is well-suited for handling complex and lengthy inputs. Its architecture supports various capabilities such as text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Strengths and Use Cases
The main strengths of Mistral Large 2 lie in its high performance on benchmarks such as MMLU (84.0), HumanEval (92.0), LMSYS Arena ELO (1225), and GSM8K (93.0), indicating its excellence in coding, analysis, and other tasks. It is best utilized for coding, analysis, retrieval-augmented generation (RAG), agents, multilingual tasks, and function calling. However, it is not recommended for embeddings, bulk cheap processing, real-time applications requiring sub-100ms responses, or vision-heavy tasks. With a pricing structure of $3.0 per 1M input tokens and $9.0 per 1M output tokens, developers can estimate costs based on their specific use cases, such as $6.0 for 1,000 calls averaging 500 tokens.

### Pricing and Competitors
Mistral Large 2's pricing is competitive, especially considering its premium features and performance. For example, 10,000 calls would cost $60.0, and 100,000 calls would amount to $600.0. In comparison to its top competitor, GPT-4o, which charges $2.5 per 1M input tokens and $10.0 per 1M output tokens, Mistral Large 

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
Mistral Large 2 is a premium model offered by Mistral AI, released on 2024-07-24. This model is not open source and is part of the premium tier. The pricing structure is based on input and output tokens, with specific rates for cached input and batch input.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $None per 1M tokens (no additional cost for cached input)
* Batch Input: $None per 1M tokens (no additional cost for batch input)

#### When to Use Cached Tokens
Cached tokens can be used to reduce the cost of input tokens. Since there is no additional cost for cached input, it is recommended to use cached tokens whenever possible to minimize the cost of input tokens.

#### Batch API Savings
The pricing structure does not provide a specific discount for batch API calls. However, the cost of input and output tokens remains the same, regardless of the batch size. This means that making batch API calls can still provide savings in terms of reduced overhead and improved efficiency, even if there is no direct discount on the cost of tokens.

#### Cost at Scale
The cost of using Mistral Large 2 at scale can be estimated based on the provided cost examples:
* 1,000 calls (avg 500 tokens): $6.0
* 10,000 calls: $60.0
* 100,000 calls: $600.0

These estimates suggest that the cost of using Mistral Large 2 increases linearly with the number of API calls. To estimate the cost at scale, we can use the following calculations:
* 1,000 calls: $6.0 / 1,000 calls = $0.006 per call

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
* Input: **$3.0 per 1M tokens**
* Output: **$9.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Benchmark Performance
The model's benchmark performance is measured by the following scores:
* **MMLU: 84.0** - The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to perform a wide range of natural language processing tasks. A higher MMLU score indicates better performance.
* **HumanEval: 92.0** - The HumanEval benchmark assesses a model's ability to generate code that is correct and functional. A higher HumanEval score indicates better coding capabilities.
* **LMSYS Arena ELO: 1225** - The LMSYS Arena ELO score measures a model's performance in a competitive environment, where it is pitted against other models. A higher ELO score indicates better performance.

#### Real-World Implications
The benchmark scores have the following implications for real-world use:
* The high **HumanEval score (92.0)** indicates that Mistral Large 2 is well-suited for coding

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Introduction
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. This comparison will focus on its pricing, performance, and trade-offs against its top competitor, GPT-4o.

#### Pricing Comparison
The pricing for Mistral Large 2 and GPT-4o is as follows:
* Mistral Large 2:
	+ Input: $3.0 per 1M tokens
	+ Output: $9.0 per 1M tokens
* GPT-4o:
	+ Input: $2.5 per 1M tokens
	+ Output: $10.0 per 1M tokens

Mistral Large 2 is more expensive than GPT-4o for input tokens, but slightly cheaper for output tokens.

#### Performance Comparison
The performance benchmarks for Mistral Large 2 are:
* MMLU: 84.0
* HumanEval: 92.0
* LMSYS Arena ELO: 1225
* GSM8K: 93.0

GPT-4o's performance benchmarks are not provided, making a direct comparison challenging. However, based on the available data, Mistral Large 2 demonstrates strong performance across various tasks.

#### Context and Limits
Mistral Large 2 has the following context and limits:
* Context Window: 131,072 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2024-07

These specifications indicate that Mistral Large 2 is suitable for tasks requiring a large context window and moderate output length.

#### Capabilities and Use Cases
Mistral Large 2 supports the following capabilities:
* text
* vision
* function_calling
* json_mode
* streaming
* system_prompts

It is best suited for tasks such as:
* coding
* analysis
* rag
* agents
* multilingual
* function_calling

However, it is not recommended for:
* embeddings
* bulk_cheap
* real_time_sub_100ms
* vision_heavy

#### Cost Examples
The estimated costs for using Mistral Large 2 are:
* 1,000 calls (avg 500 tokens): $6.0
* 10,000 calls: $60.0
*

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. With its robust capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, it is best suited for tasks such as coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual support, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Given its capabilities and limitations, here are the top 5 best use cases for Mistral Large 2, along with specific code integration examples mentioning OpenRouter:

1. **Coding and Development**: Mistral Large 2 excels in coding tasks, making it an ideal choice for developers looking to automate code generation, code review, or even generate documentation.
   ```python
   import openrouter
   model = openrouter.load_model("mistralai/mistral-large-2407")
   prompt = "Generate a Python function to calculate the area of a circle."
   response = model.generate_text(prompt)
   print(response)
   ```

2. **Analysis and Research**: With its strong analysis capabilities, Mistral Large 2 can be used for research purposes, such as data analysis, report generation, or even summarizing long documents.
   ```python
   import openrouter
   model = openrouter.load_model("mistralai/mistral-large-2407")
   prompt = "Summarize the main points of a given research paper."
   response = model.generate_text(prompt)
   print(response)
   ```

3. **RAG (Retrieval-Augmented Generation)**: Mistral Large 2 supports RAG, which is useful for generating text based on external knowledge sources.
   ```python
   import openrouter
   model = openrouter.load_model("mistralai/mistral-large-2407")


## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
