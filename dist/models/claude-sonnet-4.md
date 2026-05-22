# Claude Sonnet 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-22
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Claude Sonnet 4
Claude Sonnet 4, developed by Anthropic, is a premium, non-open-source language model released on 2025-05-22. This model boasts an impressive architecture, with a context window of 200,000 tokens and a maximum output of 64,000 tokens. Its knowledge cutoff is 2025-03, ensuring it has a robust understanding of information up to that point. Claude Sonnet 4 is designed to excel in various tasks, including coding, analysis, and long document analysis, thanks to its capabilities in text, vision, tool use, and more.

### Technical Strengths and Use Cases
Claude Sonnet 4 demonstrates exceptional performance across several benchmarks, including MMLU (90.5), HumanEval (93.7), LMSYS Arena ELO (1340), and GSM8K (98.2). These scores underscore its strengths in understanding and generating human-like text. The model's primary use cases include coding, analysis, agents, and research, where its extended thinking and computer use capabilities shine. However, it is not recommended for tasks like embeddings, real-time sub-100ms responses, bulk cheap tasks, or image generation. Developers can leverage Claude Sonnet 4's strengths in areas like system prompts, batch processing, and JSON mode to build sophisticated applications.

### Pricing and Cost Considerations
The pricing for Claude Sonnet 4 is as follows: $3.0 per 1M input tokens, $15.0 per 1M output tokens, $0.3 per 1M cached input tokens, and $1.5 per 1M batch input tokens. To put this into perspective, 1,000 calls with an average of 500 tokens would cost $9.0, while 10,000 calls would amount to $90.0, and 100,000 calls would total $900.0. In comparison to its

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $3.0 |
| Output | $15.0 |
| Cached Input | $0.3 |
| Batch Input | $1.5 |
| Batch Output | $7.5 |

## Pricing Analysis
### Pricing Analysis for Claude Sonnet 4
#### Overview
The Claude Sonnet 4 model, provided by Anthropic, offers a premium tier with a specific pricing structure. This analysis will break down the cost structure, discuss the use of cached tokens, batch API savings, and calculate the cost at scale for 1,000, 10,000, and 100,000 API calls.

#### Cost Structure
The pricing for Claude Sonnet 4 is as follows:
* Input: $3.0 per 1M tokens
* Output: $15.0 per 1M tokens
* Cached Input: $0.3 per 1M tokens
* Batch Input: $1.5 per 1M tokens

#### Cached Tokens
Cached tokens can significantly reduce costs. With a price of $0.3 per 1M tokens, cached input is 10 times cheaper than regular input ($3.0 per 1M tokens) and 50 times cheaper than output ($15.0 per 1M tokens). It is recommended to use cached tokens whenever possible to minimize expenses.

#### Batch API Savings
Batch input is priced at $1.5 per 1M tokens, which is half the cost of regular input ($3.0 per 1M tokens). This represents a 50% discount for batch processing. Utilizing batch API calls can lead to substantial cost savings, especially for large-scale applications.

#### Cost at Scale
To estimate the cost at scale, we will calculate the cost for 1,000, 10,000, and 100,000 API calls, assuming an average of 500 tokens per call.

* 1,000 calls (avg 500 tokens): $9.0 (as provided in the cost examples)
* 10,000 calls: $90.0 (as provided in the cost examples)
* 100,000 calls: $900.0 (as provided in the cost examples

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 90.5 |
| HumanEval | 93.7 |
| LMSYS Arena ELO | 1340 |
| ARC | None |

## Benchmark Analysis
### Claude Sonnet 4 Benchmark Performance Analysis
#### Model Overview
The Claude Sonnet 4 model, provided by Anthropic, is a premium, non-open-source model released on 2025-05-22. It offers a range of capabilities, including text, vision, and tool use, making it suitable for tasks such as coding, analysis, and research.

#### Pricing
The pricing for Claude Sonnet 4 is as follows:
* Input: $3.0 per 1M tokens
* Output: $15.0 per 1M tokens
* Cached Input: $0.3 per 1M tokens
* Batch Input: $1.5 per 1M tokens

#### Benchmark Performance
The model's benchmark performance is as follows:
* **MMLU (Massive Multitask Language Understanding)**: 90.5 - This score indicates the model's ability to understand and generate human-like text across a wide range of tasks and domains. A higher MMLU score suggests better performance in tasks that require a deep understanding of language.
* **HumanEval**: 93.7 - This score evaluates the model's ability to write correct and functional code in response to a given prompt. A higher HumanEval score indicates better performance in coding tasks.
* **LMSYS Arena ELO**: 1340 - This score measures the model's performance in a competitive arena, where it is pitted against other models in a series of tasks. A higher LMSYS Arena ELO score suggests better overall performance and adaptability.
* **GSM8K**: 98.2 - This score is not explicitly defined in the provided data, but it is likely related to the model's performance

## Competitor Comparison
### Comparison of Claude Sonnet 4 with Top Competitors
#### Overview
Claude Sonnet 4, a premium model by Anthropic, is a powerful tool with a wide range of capabilities, including text, vision, and tool use. In this comparison, we will examine its pricing, performance, and trade-offs against its top competitors, GPT-4o and DeepSeek R1.

#### Pricing Comparison
The pricing for each model is as follows:
* **Claude Sonnet 4**:
	+ Input: $3.0 per 1M tokens
	+ Output: $15.0 per 1M tokens
	+ Cached Input: $0.3 per 1M tokens
	+ Batch Input: $1.5 per 1M tokens
* **GPT-4o**:
	+ Input: $2.5 per 1M tokens
	+ Output: $10.0 per 1M tokens
* **DeepSeek R1**:
	+ Input: $0.55 per 1M tokens
	+ Output: $2.19 per 1M tokens

#### Performance Comparison
The performance of each model can be evaluated based on the following benchmarks:
* **Claude Sonnet 4**:
	+ MMLU: 90.5
	+ HumanEval: 93.7
	+ LMSYS Arena ELO: 1340
	+ GSM8K: 98.2
* Note: The benchmark scores for GPT-4o and DeepSeek R1 are not provided.

#### Trade-offs and Choosing the Right Model
When choosing a model, consider the following trade-offs:
* **Claude Sonnet 4**:
	+ High-performance capabilities, including text, vision, and tool use.
	+ Large context window (200,000 tokens) and max output (64,000 tokens).
	+ Suitable for coding, analysis, agents, long document analysis, and research.
	+ More expensive than competitors, especially for output tokens.
* **GPT-4o**:
	+ Lower input and output costs compared to Claude Sonnet 4.
	+ May not offer the same level of performance or capabilities as Claude Sonnet 4.
* **DeepSeek R1**:
	+ Significantly lower input and output costs compared to Claude Sonnet 4 and GPT-4o.
	+ May

## Best Use Cases
### Introduction to Claude Sonnet 4
Claude Sonnet 4, provided by Anthropic, is a premium model with a wide range of capabilities, including text, vision, tool use, and more. Released on 2025-05-22, this model is well-suited for tasks such as coding, analysis, and long document analysis.

### Top 5 Best Use Cases for Claude Sonnet 4
Based on its capabilities and pricing, here are the top 5 best use cases for Claude Sonnet 4:

1. **Coding and Software Development**: With its high scores in HumanEval (93.7) and LMSYS Arena ELO (1340), Claude Sonnet 4 is an excellent choice for coding tasks, such as code completion, code review, and bug fixing.
2. **Long Document Analysis**: Claude Sonnet 4's large context window (200,000 tokens) and high score in GSM8K (98.2) make it well-suited for analyzing long documents, such as research papers, articles, and books.
3. **Research and Writing**: With its ability to understand and generate human-like text, Claude Sonnet 4 is an excellent tool for research and writing tasks, such as summarizing articles, generating reports, and writing content.
4. **Computer Use and Automation**: Claude Sonnet 4's capabilities in computer use and automation make it an excellent choice for tasks such as automating workflows, generating scripts, and interacting with other systems.
5. **Analysis and Agents**: Claude Sonnet 4's high scores in MMLU (90.5) and LMSYS Arena ELO (1340) make it well-suited for analysis tasks, such as data analysis, and building agents that can interact with humans and other systems.

### Code Integration Examples with OpenRouter
To integrate Claude Sonnet 4 with OpenRouter, you can use the following code example:
```python
import open

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
