# Gemini 2.5 Pro API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-26
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Gemini 2.5 Pro
Gemini 2.5 Pro, released by Google on 2025-03-25, is a premium, non-open-source model designed for complex tasks. Its architecture is tailored to handle a wide range of capabilities, including text, vision, audio, video, function calling, JSON mode, streaming, system prompts, code execution, and extended thinking. With a context window of 1,048,576 tokens and a maximum output of 65,536 tokens, Gemini 2.5 Pro is suited for tasks that require in-depth analysis and understanding.

### Technical Strengths and Use Cases
The model's technical strengths are reflected in its benchmark scores: MMLU at 91.5, HumanEval at 92.0, LMSYS Arena ELO at 1376, and GSM8K at 97.0. These scores indicate Gemini 2.5 Pro's ability to handle complex reasoning, coding, and multimodal tasks. Its primary use cases include long document analysis, complex reasoning, coding, video understanding, audio analysis, and research. However, it is not recommended for simple tasks, cost-sensitive applications at scale, or real-time applications requiring responses under 100ms. The pricing model is based on input and output tokens, with rates of $1.25 per 1M input tokens and $10.0 per 1M output tokens.

### Pricing and Competitors
The pricing for Gemini 2.5 Pro is as follows: $1.25 per 1M input tokens, $10.0 per 1M output tokens, and $0.125 per 1M cached input tokens. For example, 1,000 calls with an average of 500 tokens would cost $5.625, while 10,000 calls would cost $56.25, and 100,000 calls would cost $562.5. In comparison to its top competitors, such

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $1.25 |
| Output | $10.0 |
| Cached Input | $0.125 |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Gemini 2.5 Pro Pricing Analysis
#### Overview
The Gemini 2.5 Pro model, released by Google on 2025-03-25, is a premium, non-open-source model. It boasts an impressive set of capabilities, including text, vision, audio, and video processing, as well as advanced features like function calling, JSON mode, and system prompts.

#### Cost Structure
The pricing for Gemini 2.5 Pro is as follows:
* Input: $1.25 per 1M tokens
* Output: $10.0 per 1M tokens
* Cached Input: $0.125 per 1M tokens
* Batch Input: No additional cost specified

#### When to Use Cached Tokens
Cached tokens can significantly reduce costs, with a price of $0.125 per 1M tokens, which is 10% of the regular input cost. It is recommended to use cached tokens when:
* The same input is used multiple times
* The input data is static and does not change frequently
* Cost savings are a priority

#### Batch API Savings
Although no specific batch input cost is provided, using batch API calls can still lead to cost savings by reducing the number of individual API calls. This can be particularly beneficial when processing large volumes of data.

#### Cost at Scale
The cost of using Gemini 2.5 Pro at scale is as follows:
* 1,000 calls (avg 500 tokens): $5.625
* 10,000 calls: $56.25
* 100,000 calls: $562.5

These costs demonstrate a linear relationship between the number of API calls and the total cost.

#### Comparison to Competitors
Gemini 2.5 Pro's pricing is competitive with other premium models:
* Claude Opus 4: $15.0/1M input, $75.0/1M output (significantly more expensive)
* OpenAI o

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 91.5 |
| HumanEval | 92.0 |
| LMSYS Arena ELO | 1376 |
| ARC | None |

## Benchmark Analysis
### Analysis of Gemini 2.5 Pro Benchmark Performance
The Gemini 2.5 Pro model, released by Google on 2025-03-25, is a premium, non-open-source model with a unique set of capabilities and pricing structure. To understand its real-world performance, we'll delve into its benchmark scores and what they signify.

#### Benchmark Scores
The model has achieved the following benchmark scores:
* **MMLU (Massive Multitask Language Understanding)**: 91.5
* **HumanEval**: 92.0
* **LMSYS Arena ELO**: 1376
* **GSM8K**: 97.0

These scores indicate the model's performance in various areas:
* **MMLU**: Measures the model's ability to understand and generate human-like text across a wide range of tasks and topics. A score of 91.5 suggests that Gemini 2.5 Pro has a high level of language understanding, making it suitable for complex tasks like long document analysis and coding.
* **HumanEval**: Evaluates the model's ability to write correct and functional code in response to programming prompts. A score of 92.0 indicates that Gemini 2.5 Pro is proficient in code generation and can be used for tasks like coding and software development.
* **LMSYS Arena ELO**: Assesses the model's performance in a competitive environment, where it is pitted against other models in a series of tasks. An ELO score of 1376 suggests that Gemini 2.5 Pro is a strong competitor and can hold its own against other premium models.
* **GSM8K**: Measures the model's ability to reason and solve math problems.

## Competitor Comparison
### Comparison of Gemini 2.5 Pro with Top Competitors
#### Overview
The Gemini 2.5 Pro, released by Google on 2025-03-25, is a premium, non-open-source model that offers a unique set of capabilities and performance metrics. This comparison will delve into the pricing, performance, and use cases of Gemini 2.5 Pro against its top competitors: Claude Opus 4, OpenAI o3, and GPT-4.1.

#### Pricing Comparison
The pricing models of these competitors are as follows:

* **Gemini 2.5 Pro**:
	+ Input: $1.25 per 1M tokens
	+ Output: $10.0 per 1M tokens
	+ Cached Input: $0.125 per 1M tokens
	+ Batch Input: $None per 1M tokens
* **Claude Opus 4**:
	+ Input: $15.0 per 1M tokens
	+ Output: $75.0 per 1M tokens
* **OpenAI o3**:
	+ Input: $2.0 per 1M tokens
	+ Output: $8.0 per 1M tokens
* **GPT-4.1**:
	+ Input: $2.0 per 1M tokens
	+ Output: $8.0 per 1M tokens

#### Performance Comparison
The performance metrics of Gemini 2.5 Pro are:

* MMLU: 91.5
* HumanEval: 92.0
* LMSYS Arena ELO: 1376
* GSM8K: 97.0

While the performance metrics of the competitors are not provided, the pricing difference suggests that Claude Opus 4 is the most expensive option, followed by Gemini 2.5 Pro, and then OpenAI o3 and GPT-4.1.

#### Capabilities and Use Cases
Gemini 2.5 Pro offers a wide range of capabilities, including:

* Text, vision, audio, video, function calling, JSON mode, streaming, system prompts, code execution, and extended thinking
* Best for: long document analysis, complex reasoning, coding, video understanding, audio analysis, multimodal RAG, and research
* Not good for: simple tasks, cost-sensitive at scale, real-time sub 100ms, and embeddings



## Best Use Cases
### Introduction to Gemini 2.5 Pro
The Gemini 2.5 Pro model, released by Google on 2025-03-25, is a premium, non-open-source model that excels in various complex tasks. With its impressive benchmarks, including an MMLU score of 91.5 and a HumanEval score of 92.0, this model is well-suited for tasks that require advanced reasoning and analysis.

### Top 5 Best Use Cases for Gemini 2.5 Pro
Based on its capabilities and performance, the top 5 best use cases for Gemini 2.5 Pro are:

1. **Long Document Analysis**: With a context window of 1,048,576 tokens, Gemini 2.5 Pro is ideal for analyzing lengthy documents, extracting key information, and summarizing complex texts.
2. **Complex Reasoning**: The model's high scores in HumanEval and MMLU benchmarks demonstrate its ability to handle complex reasoning tasks, making it suitable for applications that require logical and analytical thinking.
3. **Coding and Code Execution**: Gemini 2.5 Pro supports code execution and has a high score in HumanEval, making it an excellent choice for coding tasks, such as code completion, code review, and code optimization.
4. **Multimodal Analysis**: The model's capabilities in text, vision, audio, and video analysis make it well-suited for multimodal tasks, such as analyzing videos, understanding audio cues, and recognizing visual patterns.
5. **Research and Extended Thinking**: With its ability to process large amounts of information and generate human-like responses, Gemini 2.5 Pro is an excellent tool for research applications, such as data analysis, hypothesis generation, and scientific writing.

### Code Integration Example with OpenRouter
To integrate Gemini 2.5 Pro with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Gemini 2.5 Pro model
model

## Frequently Asked Questions


---
*Data verified: 2026-04-09 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
