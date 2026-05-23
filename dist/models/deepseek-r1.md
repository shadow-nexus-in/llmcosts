# DeepSeek R1 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-23
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to DeepSeek R1
DeepSeek R1 is a standard-tier, open-source language model released by DeepSeek on 2025-01-20. This model is designed to excel in complex reasoning, math, coding, science, and research, making it an ideal choice for tackling PhD-level problems. The DeepSeek R1 architecture is capable of handling a context window of up to 64,000 tokens and can generate output of up to 8,192 tokens. Its knowledge cutoff is 2024-11, ensuring that it has been trained on a vast amount of data up to that point.

### Technical Capabilities and Pricing
DeepSeek R1 boasts an impressive set of capabilities, including text processing, function calling, streaming, system prompts, and extended thinking. This model has demonstrated strong performance in various benchmarks, scoring 90.8 on MMLU, 92.6 on HumanEval, 1358 on LMSYS Arena ELO, and 97.3 on GSM8K. In terms of pricing, DeepSeek R1 costs $0.55 per 1M tokens for input and $2.19 per 1M tokens for output. There are no additional costs for cached input or batch input. For example, 1,000 calls with an average of 500 tokens would cost $1.37, while 10,000 calls would cost $13.7, and 100,000 calls would cost $137.0.

### Comparison and Use Cases
DeepSeek R1 is not suitable for simple tasks, high-volume applications, low-latency requirements, vision-related tasks, or budget-conscious projects. However, it outshines its competitors in certain aspects, such as pricing. For instance, OpenAI o1 costs $15.0/1M input and $60.0/1M output, while OpenAI o3-mini costs $1.1/1M input and $4.4/

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.55 |
| Output | $2.19 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### DeepSeek R1 Pricing Analysis
#### Overview
DeepSeek R1 is a standard, open-source model released by DeepSeek on 2025-01-20. This analysis will break down the cost structure, provide guidance on when to use cached tokens, and highlight batch API savings and costs at scale.

#### Cost Structure
The cost structure for DeepSeek R1 is as follows:
* **Input**: $0.55 per 1M tokens
* **Output**: $2.19 per 1M tokens
* **Cached Input**: $0 per 1M tokens (free)
* **Batch Input**: $0 per 1M tokens (free)

#### Using Cached Tokens
Cached tokens are free, making them an attractive option for reducing costs. Consider using cached tokens when:
* You have a high volume of repeated input queries.
* Your application can tolerate slightly outdated knowledge (up to the knowledge cutoff date of 2024-11).

#### Batch API Savings
Batch input is also free, which can lead to significant cost savings when making multiple API calls. To maximize batch API savings:
* Group multiple input queries into a single batch API call.
* Ensure that the total input tokens in the batch do not exceed the context window of 64,000 tokens.

#### Cost at Scale
The cost of using DeepSeek R1 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: $1.37
* **10,000 calls**: $13.7
* **100,000 calls**: $137.0

These costs are significantly lower than those of top competitors, such as OpenAI o1 and OpenAI o3-mini.

#### Comparison to Top Competitors
| Model | Input Cost (1M tokens) | Output Cost (1M tokens) |
| --- | --- | --- |
| DeepSeek R1 | $0.55 | $2.19 |
| OpenAI o1 |

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 90.8 |
| HumanEval | 92.6 |
| LMSYS Arena ELO | 1358 |
| ARC | None |

## Benchmark Analysis
### DeepSeek R1 Benchmark Analysis
The DeepSeek R1 model, released on 2025-01-20, is a standard, open-source model with a unique set of capabilities and limitations. To understand its performance, we'll delve into its benchmark scores and what they mean for real-world use.

#### Benchmark Scores
The DeepSeek R1 model has achieved the following benchmark scores:
* **MMLU: 90.8** - The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to understand and generate human-like text across a wide range of tasks and domains. A score of 90.8 indicates that DeepSeek R1 has a high level of language understanding, making it suitable for complex reasoning and text-based tasks.
* **HumanEval: 92.6** - The HumanEval benchmark assesses a model's ability to write correct and functional code in response to a given prompt. A score of 92.6 suggests that DeepSeek R1 is highly proficient in coding tasks, making it a strong candidate for applications involving programming and software development.
* **LMSYS Arena ELO: 1358** - The LMSYS Arena ELO score is a measure of a model's overall performance in a competitive environment, where models are pitted against each other to solve a variety of tasks. An ELO score of 1358 indicates that DeepSeek R1 is a strong competitor, capable of holding its own against other models in the arena.

#### Real-World Implications
These benchmark scores have significant implications for real-world use:
* **Complex Reasoning**: With its high MMLU score, DeepSeek R1 is well-suited for tasks that

## Competitor Comparison
### DeepSeek R1 Comparison
#### Introduction
DeepSeek R1 is a standard, open-source model released by DeepSeek on 2025-01-20. This comparison will analyze the pricing, performance, and capabilities of DeepSeek R1 against its top competitors, OpenAI o1 and OpenAI o3-mini.

#### Pricing Comparison
The pricing for each model is as follows:
* DeepSeek R1:
	+ Input: $0.55 per 1M tokens
	+ Output: $2.19 per 1M tokens
* OpenAI o1:
	+ Input: $15.0 per 1M tokens
	+ Output: $60.0 per 1M tokens
* OpenAI o3-mini:
	+ Input: $1.1 per 1M tokens
	+ Output: $4.4 per 1M tokens

DeepSeek R1 offers significant cost savings compared to OpenAI o1, with input and output prices 96.3% and 96.3% lower, respectively. Compared to OpenAI o3-mini, DeepSeek R1 is 50% cheaper for input and 50.5% cheaper for output.

#### Performance Comparison
The performance benchmarks for DeepSeek R1 are:
* MMLU: 90.8
* HumanEval: 92.6
* LMSYS Arena ELO: 1358
* GSM8K: 97.3

While the performance benchmarks for OpenAI o1 and OpenAI o3-mini are not provided, DeepSeek R1's benchmarks indicate strong capabilities in complex reasoning, math, coding, science, and research.

#### Capabilities and Use Cases
DeepSeek R1 supports the following capabilities:
* text
* function_calling
* streaming
* system_prompts
* extended_thinking

It is best suited for:
* complex_reasoning
* math
* coding
* science
* research
* phd_level_problems

On the other hand, it is not recommended for:
* simple_tasks
* high_volume
* low_latency
* vision
* budget_conscious use cases

#### Cost Examples
The estimated costs for using DeepSeek R1 are:
* 1,000 calls (avg 500 tokens): $1.37
* 10,000 calls: $13.7
* 100,000 calls: $137.0

#### Choosing

## Best Use Cases
### Introduction to DeepSeek R1
The DeepSeek R1 model, released by DeepSeek on 2025-01-20, is a standard, open-source model with a context window of 64,000 tokens and a maximum output of 8,192 tokens. With its capabilities in text, function calling, streaming, system prompts, and extended thinking, it is best suited for complex reasoning, math, coding, science, research, and PhD-level problems.

### Top 5 Best Use Cases for DeepSeek R1
Based on its capabilities and benchmarks, here are the top 5 best use cases for DeepSeek R1:

1. **Complex Math Problem Solving**: With a high score of 97.3 on the GSM8K benchmark, DeepSeek R1 is well-suited for solving complex math problems. It can be integrated with OpenRouter to solve math problems using the following code example:
    ```python
import openrouter

# Initialize the DeepSeek R1 model
model = openrouter.Model("deepseek/deepseek-r1")

# Define a math problem
problem = "What is the derivative of x^2 + 3x - 4?"

# Get the solution
solution = model.solve(problem)

print(solution)
```
2. **Coding and Programming**: DeepSeek R1's high score of 92.6 on the HumanEval benchmark makes it a great tool for coding and programming tasks. It can be used to generate code snippets, debug code, and even write entire programs. Here's an example of how to integrate DeepSeek R1 with OpenRouter for coding tasks:
    ```python
import openrouter

# Initialize the DeepSeek R1 model
model = openrouter.Model("deepseek/deepseek-r1")

# Define a coding task
task = "Write a Python function to sort a list of integers."

# Get the code
code = model.generate_code(task)

print(code)
```
3.

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
