# Claude Sonnet 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-24
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Claude Sonnet 4
Claude Sonnet 4, developed by Anthropic, is a premium, non-open-source model released on 2025-05-22. This model boasts an impressive array of capabilities, including text, vision, tool use, JSON mode, streaming, batch processing, system prompts, extended thinking, and computer use. With a context window of 200,000 tokens and a maximum output of 64,000 tokens, Claude Sonnet 4 is well-suited for tasks that require in-depth analysis and generation of lengthy content.

### Technical Strengths and Use Cases
The architecture of Claude Sonnet 4 is designed to excel in coding, analysis, agents, long document analysis, RAG, computer use, research, and writing tasks. Its strengths are reflected in its benchmark scores: MMLU (90.5), HumanEval (93.7), LMSYS Arena ELO (1340), and GSM8K (98.2). However, it is not recommended for tasks such as embeddings, real-time sub-100ms tasks, bulk cheap tasks, or image generation. The pricing model for Claude Sonnet 4 includes input costs of $3.0 per 1M tokens, output costs of $15.0 per 1M tokens, cached input costs of $0.3 per 1M tokens, and batch input costs of $1.5 per 1M tokens.

### Cost Considerations and Competitors
To understand the cost implications of using Claude Sonnet 4, consider the following examples: 1,000 calls with an average of 500 tokens cost $9.0, while 10,000 calls cost $90.0, and 100,000 calls cost $900.0. In comparison to its top competitors, such as GPT-4o ($2.5/1M input, $10.0/1M output) and DeepSeek R

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
* **Cached Tokens**: Use cached input tokens when possible, as they offer a significant reduction in cost (**$0.3 per 1M tokens**, which is 10% of the regular input cost and 20% of the batch input cost).
* **Batch API**: Utilize batch API calls for input tokens to save on costs (**$1.5 per 1M tokens**, which is 50% of the regular input cost).

#### Cost at Scale
The cost of using Claude Sonnet 4 at scale is as follows:
* **1,000 calls** (avg 500 tokens): **$9.0**
* **10,000 calls**: **$90.0**
* **100,000 calls**: **$900.0**

To put this into perspective, assuming an average of 500 tokens per call, the cost per call can be broken down as follows:
* **1 call**: **$0.009** (input) + **$0.075** (output, assuming 500 tokens is approximately 1/20th of 1M tokens, thus $15.0/20) = **$0.084** per call, which is roughly in line with the provided cost example of **$9

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
The Claude Sonnet 4 model, provided by Anthropic, is a premium, non-open-source model released on 2025-05-22. It offers a range of capabilities, including text, vision, tool use, and more, making it suitable for tasks like coding, analysis, and research.

#### Pricing
The pricing for Claude Sonnet 4 is as follows:
* Input: $3.0 per 1M tokens
* Output: $15.0 per 1M tokens
* Cached Input: $0.3 per 1M tokens
* Batch Input: $1.5 per 1M tokens

#### Context and Limits
The model has a context window of 200,000 tokens, a maximum output of 64,000 tokens, and a knowledge cutoff of 2025-03.

#### Benchmarks
The benchmark performance of Claude Sonnet 4 is:
* MMLU: 90.5
* HumanEval: 93.7
* LMSYS Arena ELO: 1340
* GSM8K: 98.2

These benchmarks indicate the model's performance in various areas:
* **MMLU (Massive Multitask Language Understanding)**: A score of 90.5 indicates that Claude Sonnet 4 has a high level of language understanding, making it suitable for tasks that require comprehension and reasoning.
* **HumanEval**: A score of 93.7 suggests that the model is highly effective in evaluating and generating human-like text, which is beneficial for applications that require natural language generation.
* **LMSYS Arena ELO**: An ELO score

## Competitor Comparison
### Claude Sonnet 4 Comparison
#### Overview
The Claude Sonnet 4 model, provided by Anthropic, is a premium, non-open-source model released on 2025-05-22. It offers a range of capabilities, including text, vision, and tool use, making it suitable for tasks such as coding, analysis, and research.

#### Pricing Comparison
The pricing for Claude Sonnet 4 is as follows:
* Input: $3.0 per 1M tokens
* Output: $15.0 per 1M tokens
* Cached Input: $0.3 per 1M tokens
* Batch Input: $1.5 per 1M tokens

In comparison, its top competitors have the following pricing:
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

While the exact benchmarks for GPT-4o and DeepSeek R1 are not provided, Claude Sonnet 4's high scores suggest it is a high-performance model. However, its premium pricing may make it less accessible to some users.

#### When to Choose Each Model
* **Claude Sonnet 4**: Choose this model for tasks that require high performance, such as coding, analysis, and research. Its capabilities, including text, vision, and tool use, make it well-suited for complex tasks.
* **GPT-4o**: Choose this model for tasks that require a balance between performance and cost. Its pricing is lower than Claude Sonnet 4, but its performance may not be as high.
* **DeepSeek R1**: Choose this model for tasks that require low-cost processing, such as bulk or cheap tasks. Its extremely low pricing makes

## Best Use Cases
### Introduction to Claude Sonnet 4
Claude Sonnet 4, provided by Anthropic, is a premium, non-open-source model released on 2025-05-22. With its impressive benchmarks, including an MMLU score of 90.5 and a HumanEval score of 93.7, this model is well-suited for a variety of tasks. The following sections will outline the top 5 best use cases for Claude Sonnet 4, along with specific code integration examples using OpenRouter.

### Top 5 Use Cases for Claude Sonnet 4
#### 1. Coding
Claude Sonnet 4 excels in coding tasks, with a high HumanEval score of 93.7. It can be used for code completion, code review, and even generating code snippets.
```python
import openrouter

# Initialize the model
model = openrouter.ClaudeSonnet4()

# Use the model for code completion
def complete_code(prompt):
    response = model.generate(prompt, max_tokens=64_000)
    return response

# Example usage
prompt = "Write a Python function to sort a list of integers."
print(complete_code(prompt))
```

#### 2. Analysis
With its high MMLU score of 90.5, Claude Sonnet 4 is well-suited for analysis tasks, such as text analysis and data analysis.
```python
import openrouter

# Initialize the model
model = openrouter.ClaudeSonnet4()

# Use the model for text analysis
def analyze_text(text):
    response = model.generate(f"Analyze the following text: {text}", max_tokens=64_000)
    return response

# Example usage
text = "The quick brown fox jumps over the lazy dog."
print(analyze_text(text))
```

#### 3. Agents
Claude Sonnet 4 can be used to build conversational agents, with its ability to

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
