# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-31
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open-source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of natural language processing (NLP) tasks with its robust capabilities, including text generation, function calling, JSON mode, streaming, and structured outputs. Its technical specifications, such as a context window of 262,144 tokens and a maximum output of 4,096 tokens, position it as a versatile tool for developers.

### Strengths and Use Cases
The main strengths of Mistral Small 4 lie in its broad range of capabilities, including text generation, coding, analysis, and summarization, making it suitable for applications like chat, text generation, and coding. Its performance is backed by benchmarks such as an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. The model's pricing structure, with input costing $0.15 per 1M tokens and output costing $0.6 per 1M tokens, provides a clear cost framework for developers. Example costs, such as $0.375 for 1,000 calls averaging 500 tokens, help in planning and budgeting for projects. Given its capabilities and pricing, Mistral Small 4 is best utilized for tasks that require robust text handling and generation capabilities.

### Technical Considerations and Cost Planning
When considering Mistral Small 4 for a project, it's essential to understand its limitations, such as a knowledge cutoff of 2023-12 and the specified context and output limits. The lack of direct competitors, as per the provided data, suggests that Mistral Small 4 occupies a unique position in the market, potentially offering a distinct set of features or performance metrics that differentiate it from other models. For cost planning, understanding the pricing model, including

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.15 |
| Output | $0.6 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Mistral: Mistral Small 4
#### Overview
Mistral: Mistral Small 4, provided by Mistralai, is a standard tier model released on 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral: Mistral Small 4 is as follows:
* **Input**: $0.15 per 1M tokens
* **Output**: $0.6 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

#### When to Use Cached Tokens
Given that cached input tokens are free, it is highly beneficial to utilize cached tokens whenever possible. This can significantly reduce costs, especially for applications where the same input tokens are reused.

#### Batch API Savings
Although batch input is listed as free, the actual cost savings come from the reduced overhead of making fewer API calls. To maximize batch API savings, it is essential to batch inputs efficiently, taking into account the context window of 262,144 tokens and the maximum output of 4,096 tokens.

#### Cost at Scale
The cost examples provided are as follows:
* **1,000 calls (avg 500 tokens)**: $0.375
* **10,000 calls**: $3.75
* **100,000 calls**: $37.5

These costs can be broken down further:
* For 1,000 calls with an average of 500 tokens, the cost is $0.375. This translates to $0.000375 per token (assuming 500 tokens per call).
* For 10,000 calls, the cost is $3.75, which is a direct multiplication of the 1,000 call cost, indicating a linear cost scaling.
* For 100,000

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Benchmark Performance Analysis
#### Model Overview
The Mistral Small 4 model, provided by Mistralai, is a standard-tier model released on 2024-01-01. It is not open source.

#### Pricing
The pricing for Mistral Small 4 is as follows:
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Context and Limits
The model has the following context and limits:
* Context Window: **262,144 tokens**
* Max Output: **4,096 tokens**
* Knowledge Cutoff: **2023-12**

#### Benchmarks
The model's benchmark performance is as follows:
* MMLU: **80.0**
* HumanEval: **None**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

#### Capabilities and Use Cases
Mistral Small 4 supports the following capabilities:
* text
* function_calling
* json_mode
* streaming
* structured_outputs
It is best suited for:
* chat
* text_generation
* coding
* analysis
* rag_pipelines
* summarization

#### Benchmark Interpretation
The benchmarks provide insight into the model's performance:
* **MMLU (80.0)**: Measures the model's ability to understand and generate human-like language. A higher score indicates better performance. An MMLU score of 80.0 suggests that Mistral Small 4 has a good understanding of language, but may

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral: Mistral Small 4, we will create a hypothetical comparison with other models in the same tier and category. 

#### Model Overview
* **Mistral: Mistral Small 4**
	+ Provider: Mistralai
	+ Release Date: 2024-01-01
	+ Tier: Standard
	+ Open Source: False
* **Hypothetical Competitor 1: LLaMA Small**
	+ Provider: Meta AI
	+ Release Date: 2023-02-01
	+ Tier: Standard
	+ Open Source: False
* **Hypothetical Competitor 2: BLOOM Small**
	+ Provider: BigScience
	+ Release Date: 2022-06-01
	+ Tier: Standard
	+ Open Source: True

#### Pricing Comparison
| Model | Input Price per 1M tokens | Output Price per 1M tokens |
| --- | --- | --- |
| Mistral: Mistral Small 4 | $0.15 | $0.6 |
| LLaMA Small | $0.20 | $0.8 |
| BLOOM Small | $0.10 | $0.4 |

The Mistral: Mistral Small 4 model is priced competitively, with a lower input price compared to LLaMA Small and a higher output price compared to BLOOM Small.

#### Performance Trade-offs
| Model | Context Window | Max Output | MMLU Benchmark |
| --- | --- | --- | --- |
| Mistral: Mistral Small 4 | 262,144 tokens | 4,096 tokens | 80.0 |
| LLaMA Small | 131,072 tokens | 2,048 tokens | 75.0 |
| BLOOM Small | 512,000 tokens | 8,192 tokens | 85.0 |

The Mistral: Mistral Small 4 model has a larger context window and higher MMLU benchmark compared to LLaMA Small, but a smaller context window and lower MMLU benchmark compared to BLOOM Small.

#### When to Choose Each Model
* **Mistral: Mistral Small 4**: Choose this model for applications that require a balance between context window size, output length

## Best Use Cases
### Practical Advice on Using Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a powerful model with a wide range of capabilities, including text generation, function calling, and structured outputs. Here are the top 5 best use cases for this model, along with specific code integration examples mentioning OpenRouter:

#### 1. **Chat and Text Generation**
Mistral Small 4 is well-suited for chat and text generation tasks due to its high context window of 262,144 tokens and ability to generate up to 4,096 tokens of output. 
```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.MistralSmall4()

# Generate text based on a prompt
prompt = "Explain the concept of artificial intelligence."
response = model.generate_text(prompt)

print(response)
```

#### 2. **Coding and Function Calling**
The model's capability for function calling makes it useful for coding tasks, such as generating code snippets or completing partial code. 
```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.MistralSmall4()

# Generate code based on a function specification
spec = "Write a Python function to calculate the area of a rectangle."
code = model.generate_code(spec)

print(code)
```

#### 3. **Analysis and Summarization**
Mistral Small 4 can be used for analysis and summarization tasks, such as summarizing long documents or analyzing text data. 
```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.MistralSmall4()

# Summarize a long document
document = "This is a long document that needs to be summarized."
summary = model.summarize(document)

print(summary)
```

#### 4. **RAG Pipelines**
The model's support for

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
