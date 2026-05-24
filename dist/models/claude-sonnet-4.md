# Claude Sonnet 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-24
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Claude Sonnet 4
Claude Sonnet 4, developed by Anthropic, is a premium large language model (LLM) released on 2025-05-22. This model is not open source, indicating that its internal architecture and training data are proprietary. The architecture of Claude Sonnet 4 is designed to handle a wide range of tasks, including text and vision processing, with capabilities such as `text`, `vision`, `tool_use`, and `json_mode`. Its strengths lie in its high performance on various benchmarks, including MMLU (90.5), HumanEval (93.7), LMSYS Arena ELO (1340), and GSM8K (98.2), showcasing its potential for coding, analysis, and research applications.

### Technical Specifications and Use Cases
Claude Sonnet 4 has a context window of 200,000 tokens and can generate up to 64,000 tokens as output. Its knowledge cutoff is 2025-03, meaning it may not have information on events or developments after this date. The model is best suited for tasks like coding, analysis, agents, long document analysis, and research, thanks to its extended capabilities including `extended_thinking`, `computer_use`, and `system_prompts`. However, it is not recommended for tasks requiring embeddings, real-time responses under 100ms, bulk cheap tasks, or image generation. Pricing for Claude Sonnet 4 is structured around input and output tokens, with costs of $3.0 per 1M input tokens and $15.0 per 1M output tokens, and discounted rates for cached input ($0.3 per 1M tokens) and batch input ($1.5 per 1M tokens).

### Pricing and Competitor Comparison
The pricing strategy for Claude Sonnet 4 reflects its premium positioning, with example costs including $9.0 for 1,000 calls averaging 500 tokens, $90

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
The Claude Sonnet 4 model, provided by Anthropic, is a premium, non-open-source model released on 2025-05-22. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Claude Sonnet 4 is as follows:
* Input: **$3.0 per 1M tokens**
* Output: **$15.0 per 1M tokens**
* Cached Input: **$0.3 per 1M tokens**
* Batch Input: **$1.5 per 1M tokens**

#### Optimal Usage Scenarios
* **Cached Tokens**: Use cached input tokens when possible, as they offer a significant discount (**$0.3 per 1M tokens**, which is 10% of the regular input price). This is ideal for applications with repetitive or similar input patterns.
* **Batch API Savings**: Utilize batch input for bulk requests to reduce costs (**$1.5 per 1M tokens**, which is 50% of the regular input price). This is suitable for applications that can process multiple requests in parallel.

#### Cost at Scale
The cost of using Claude Sonnet 4 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: **$9.0**
* **10,000 calls**: **$90.0**
* **100,000 calls**: **$900.0**

To put this into perspective, assuming an average of 500 tokens per call, the cost per call would be:
* **1,000 calls**: **$9.0 / 1,000 calls = $0.009 per call**
* **10,000 calls**: **$90.0 / 10,000 calls = $0.009 per call**
* **100,000 calls**: **$900.0

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
The Claude Sonnet 4 model, provided by Anthropic, is a premium, non-open-source model released on 2025-05-22. It boasts a range of capabilities, including text, vision, tool use, and more, making it suitable for tasks like coding, analysis, and research.

#### Pricing
The pricing for Claude Sonnet 4 is as follows:
* Input: $3.0 per 1M tokens
* Output: $15.0 per 1M tokens
* Cached Input: $0.3 per 1M tokens
* Batch Input: $1.5 per 1M tokens

#### Benchmark Performance
The model's performance is measured through several benchmarks:
* **MMLU (Massive Multitask Language Understanding)**: A score of 90.5, indicating the model's ability to understand and process a wide range of language tasks.
* **HumanEval**: A score of 93.7, demonstrating the model's capacity to generate human-like code and solve programming tasks.
* **LMSYS Arena ELO**: A score of 1340, which is a measure of the model's performance in a competitive arena, evaluating its ability to respond to a variety of prompts and tasks.
* **GSM8K**: A score of 98.2, showing the model's proficiency in solving math problems.

#### Real-World Implications
These benchmark scores have significant implications for real-world use:
* The high MMLU score suggests that Claude Sonnet 4 can handle complex, multi-task language understanding tasks, making it suitable for applications like chatbots, virtual assistants, and content

## Competitor Comparison
### Claude Sonnet 4 Comparison
#### Overview
Claude Sonnet 4, developed by Anthropic, is a premium language model released on 2025-05-22. This model offers a range of capabilities, including text, vision, and tool use, making it suitable for various applications such as coding, analysis, and research.

#### Pricing Comparison
The pricing for Claude Sonnet 4 is as follows:
* Input: $3.0 per 1M tokens
* Output: $15.0 per 1M tokens
* Cached Input: $0.3 per 1M tokens
* Batch Input: $1.5 per 1M tokens

In comparison, the top competitors have the following pricing:
* GPT-4o:
	+ Input: $2.5 per 1M tokens (20% cheaper than Claude Sonnet 4)
	+ Output: $10.0 per 1M tokens (33% cheaper than Claude Sonnet 4)
* DeepSeek R1:
	+ Input: $0.55 per 1M tokens (81.7% cheaper than Claude Sonnet 4)
	+ Output: $2.19 per 1M tokens (85.4% cheaper than Claude Sonnet 4)

#### Performance Trade-offs
Claude Sonnet 4 has the following benchmarks:
* MMLU: 90.5
* HumanEval: 93.7
* LMSYS Arena ELO: 1340
* GSM8K: 98.2

While the benchmark scores for GPT-4o and DeepSeek R1 are not provided, Claude Sonnet 4's premium pricing suggests that it may offer superior performance. However, the significant price difference between Claude Sonnet 4 and its competitors may make them more attractive for budget-conscious applications.

#### Context and Limits
Claude Sonnet 4 has the following context and limits:
* Context Window: 200,000 tokens
* Max Output: 64,000 tokens
* Knowledge Cutoff: 2025-03

These limits may affect the model's performance in certain applications, such as long-document analysis or computer use.

#### Capabilities and Use Cases
Claude Sonnet 4 is capable of:
* Text
* Vision
* Tool use
* JSON mode
* Streaming
* Batch processing
* System prompts
* Extended thinking
* Computer use

## Best Use Cases
### Introduction to Claude Sonnet 4
The Claude Sonnet 4 model, developed by Anthropic, is a premium, non-open-source language model released on 2025-05-22. With its impressive benchmarks, including an MMLU score of 90.5 and a HumanEval score of 93.7, this model is well-suited for a variety of tasks, particularly those involving coding, analysis, and long document analysis.

### Top 5 Use Cases for Claude Sonnet 4
Based on its capabilities and performance, the top 5 use cases for Claude Sonnet 4 are:

1. **Coding and Software Development**: Claude Sonnet 4 excels in coding tasks, with a high HumanEval score of 93.7. It can be used for code review, code generation, and debugging.
2. **Long Document Analysis**: With a context window of 200,000 tokens, Claude Sonnet 4 is ideal for analyzing long documents, such as research papers, books, and articles.
3. **Research and Writing**: The model's ability to understand and generate human-like text makes it suitable for research and writing tasks, such as summarizing articles, generating content, and proofreading.
4. **Analysis and Agents**: Claude Sonnet 4's capabilities in analysis and agent-based tasks make it a good fit for applications such as data analysis, decision-making, and automation.
5. **Computer Use and System Prompts**: The model's ability to understand and respond to system prompts, as well as its capabilities in computer use, make it suitable for tasks such as system administration, technical support, and automation.

### Code Integration Examples with OpenRouter
To integrate Claude Sonnet 4 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the OpenRouter client
client = openrouter.Client(api_key="YOUR_API_KEY")

# Define the input and output formats
input_format =

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
