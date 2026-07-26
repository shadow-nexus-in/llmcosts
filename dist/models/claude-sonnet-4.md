# Claude Sonnet 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-26
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Claude Sonnet 4
Claude Sonnet 4, developed by Anthropic, is a premium, non-open-source model released on 2025-05-22. This model boasts an impressive array of capabilities, including text, vision, tool use, JSON mode, streaming, batch processing, system prompts, extended thinking, and computer use. With a context window of 200,000 tokens and a maximum output of 64,000 tokens, Claude Sonnet 4 is well-suited for tasks that require in-depth analysis and generation of lengthy content.

### Technical Strengths and Use Cases
Claude Sonnet 4 demonstrates exceptional performance across various benchmarks, including MMLU (90.5), HumanEval (93.7), LMSYS Arena ELO (1340), and GSM8K (98.2). Its strengths make it an ideal choice for coding, analysis, agents, long document analysis, RAG, computer use, research, and writing tasks. However, it is not recommended for embeddings, real-time sub-100ms tasks, bulk cheap tasks, or image generation. The model's pricing structure includes input ($3.0 per 1M tokens), output ($15.0 per 1M tokens), cached input ($0.3 per 1M tokens), and batch input ($1.5 per 1M tokens), with example costs including $9.0 for 1,000 calls (avg 500 tokens) and $900.0 for 100,000 calls.

### Pricing and Competitor Comparison
In comparison to its top competitors, Claude Sonnet 4's pricing is as follows: $3.0 per 1M input tokens and $15.0 per 1M output tokens. This is higher than GPT-4o ($2.5/1M input, $10.0/1M output) and DeepSeek R1 ($0.55/1M input

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $3.0 |
| Output | $15.0 |
| Cached Input | $0.3 |
| Batch Input | $1.5 |
| Batch Output | $7.5 |

## Pricing Analysis
### Claude Sonnet 4 Pricing Analysis
#### Overview
The Claude Sonnet 4 model, provided by Anthropic, is a premium, non-open-source model released on 2025-05-22. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale for this model.

#### Cost Structure
The pricing for Claude Sonnet 4 is as follows:
- **Input**: $3.0 per 1M tokens
- **Output**: $15.0 per 1M tokens
- **Cached Input**: $0.3 per 1M tokens (a 90% discount compared to regular input)
- **Batch Input**: $1.5 per 1M tokens (a 50% discount compared to regular input)

#### Optimal Usage Scenarios
- **Cached Tokens**: Use cached input tokens when possible, as they offer a significant discount. This is ideal for scenarios where the input data does not change frequently.
- **Batch API**: Utilize batch input for large-scale operations to take advantage of the 50% discount. This is particularly beneficial for tasks that can be parallelized, such as data analysis or coding tasks.

#### Cost at Scale
The cost examples provided are based on average token usage per call:
- **1,000 calls** (avg 500 tokens): $9.0
- **10,000 calls**: $90.0
- **100,000 calls**: $900.0

To estimate costs at scale more accurately, let's consider the input and output costs separately. Assuming an average of 500 tokens per call (a rough estimate based on the provided cost examples), and considering both input and output costs:

- **1,000 calls**: 
  - Input: 500 tokens * 1,000 calls = 500,000 tokens. At $3.0 per 1M tokens, this equals $1.5.
  - Output: Assuming

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 90.5 |
| HumanEval | 93.7 |
| LMSYS Arena ELO | 1340 |
| ARC | None |

## Benchmark Analysis
### Claude Sonnet 4 Benchmark Analysis
The Claude Sonnet 4 model, released by Anthropic on 2025-05-22, is a premium, non-open-source model with a strong set of benchmark scores. 

#### Benchmark Scores
The model's performance can be evaluated based on the following benchmark scores:
* **MMLU (Massive Multitask Language Understanding)**: 90.5 - This score indicates the model's ability to understand and generate human-like text across a wide range of tasks and topics. A higher MMLU score suggests better language understanding capabilities.
* **HumanEval**: 93.7 - This score measures the model's ability to generate code that is correct and functional. A higher HumanEval score indicates better coding capabilities.
* **LMSYS Arena ELO**: 1340 - This score is a measure of the model's overall performance in a competitive arena, where it is pitted against other models. A higher ELO score suggests better overall performance.

#### Real-World Implications
These benchmark scores have significant implications for real-world use cases:
* **Coding and Analysis**: With a high HumanEval score, Claude Sonnet 4 is well-suited for coding and analysis tasks, such as generating code snippets or analyzing complex data.
* **Long-Document Analysis**: The model's high MMLU score and large context window (200,000 tokens) make it suitable for analyzing long documents and understanding complex topics.
* **Research and Writing**: Claude Sonnet 4's strong language understanding capabilities and ability to generate human-like text make it a good fit for research and writing tasks.

#### Pricing and Cost
The pricing for Claude Sonnet 4 is as follows:
*

## Competitor Comparison
### Claude Sonnet 4 Comparison
#### Overview
Claude Sonnet 4, developed by Anthropic, is a premium language model released on 2025-05-22. This model is not open-source and offers a range of capabilities, including text, vision, and tool use. In this comparison, we will examine Claude Sonnet 4's pricing, performance, and use cases against its top competitors, GPT-4o and DeepSeek R1.

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

Claude Sonnet 4 is the most expensive option, with GPT-4o being moderately priced and DeepSeek R1 being the most cost-effective.

#### Performance Trade-offs
The performance of each model can be evaluated using the following benchmarks:
* **Claude Sonnet 4**:
	+ MMLU: 90.5
	+ HumanEval: 93.7
	+ LMSYS Arena ELO: 1340
	+ GSM8K: 98.2
* **GPT-4o** and **DeepSeek R1** benchmarks are not provided, making a direct comparison challenging.

However, based on the available data, Claude Sonnet 4 demonstrates strong performance across various benchmarks.

#### Context and Limits
The context window and limits for Claude Sonnet 4 are:
* Context Window: 200,000 tokens
* Max Output: 64,000 tokens
* Knowledge Cutoff: 2025-03

These limits are not provided for GPT-4o and DeepSeek R1, making it difficult to compare their capabilities directly.

#### Capabilities and Use Cases
Claude Sonnet 4 offers a range of capabilities, including:
* Text


## Best Use Cases
### Introduction to Claude Sonnet 4
Claude Sonnet 4, developed by Anthropic, is a premium, non-open-source model released on 2025-05-22. It offers a range of capabilities including text, vision, tool use, and more, making it suitable for tasks such as coding, analysis, and long document analysis.

### Top 5 Best Use Cases for Claude Sonnet 4
Given its capabilities and pricing structure, here are the top 5 best use cases for Claude Sonnet 4:

1. **Coding and Software Development**: With its high performance in HumanEval (93.7) and capabilities in computer use, Claude Sonnet 4 is ideal for coding tasks, such as code completion, code review, and bug fixing.
2. **Long Document Analysis**: The model's large context window of 200,000 tokens allows it to process and analyze long documents, making it suitable for tasks such as research paper analysis, contract review, and document summarization.
3. **Research and Writing**: Claude Sonnet 4's capabilities in text and extended thinking make it a great tool for research and writing tasks, such as generating research papers, articles, and blog posts.
4. **Analysis and Agents**: With its high performance in MMLU (90.5) and capabilities in analysis, Claude Sonnet 4 is suitable for tasks such as data analysis, sentiment analysis, and building conversational agents.
5. **Computer Use and Automation**: The model's capabilities in computer use and tool use make it ideal for automating tasks, such as data entry, file management, and system administration.

### Code Integration Examples with OpenRouter
To integrate Claude Sonnet 4 with OpenRouter, you can use the following code examples:

```python
import os
import openrouter

# Initialize OpenRouter
router = openrouter.Router()

# Define the model and provider
model = "anthropic/claude-sonnet-

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
