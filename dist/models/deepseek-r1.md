# DeepSeek R1 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-20
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to DeepSeek R1
DeepSeek R1 is a standard-tier, open-source language model released by DeepSeek on 2025-01-20. This model is designed to excel in complex reasoning, math, coding, science, and research, making it an ideal choice for PhD-level problems. The DeepSeek R1 architecture is capable of handling a context window of 64,000 tokens and can generate up to 8,192 tokens as output. Its knowledge cutoff is 2024-11, ensuring that it has been trained on a vast amount of data up to that point.

### Technical Capabilities and Pricing
DeepSeek R1 boasts an impressive set of capabilities, including text processing, function calling, streaming, system prompts, and extended thinking. The model has demonstrated strong performance in various benchmarks, with scores of 90.8 on MMLU, 92.6 on HumanEval, 1358 on LMSYS Arena ELO, and 97.3 on GSM8K. In terms of pricing, DeepSeek R1 costs $0.55 per 1M input tokens and $2.19 per 1M output tokens. For example, 1,000 calls with an average of 500 tokens would cost $1.37, while 10,000 calls would cost $13.7, and 100,000 calls would cost $137.0. Compared to its top competitors, such as OpenAI o1 and OpenAI o3-mini, DeepSeek R1 offers a competitive pricing model.

### Use Cases and Limitations
DeepSeek R1 is best suited for complex tasks that require in-depth reasoning, mathematical calculations, and scientific analysis. However, it may not be the most suitable choice for simple tasks, high-volume applications, or low-latency requirements. Additionally, it is not designed for vision-related tasks or budget-conscious projects. Developers should carefully evaluate their use cases and consider the model's strengths and limitations

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
DeepSeek R1 is a standard-tier model released by DeepSeek on 2025-01-20. It is an open-source model with a context window of 64,000 tokens and a maximum output of 8,192 tokens.

#### Cost Structure
The cost structure of DeepSeek R1 is as follows:
* Input: $0.55 per 1M tokens
* Output: $2.19 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for reducing costs. Use cached tokens when:
* The input data is repetitive or has a high degree of similarity.
* The model is being used for tasks that require minimal input variation.

#### Batch API Savings
Batch input is also free, making it an ideal choice for large-scale API calls. Use batch API when:
* Making multiple API calls with similar input data.
* Processing large datasets that can be batched together.

#### Cost at Scale
The cost of using DeepSeek R1 at scale is as follows:
* 1,000 calls (avg 500 tokens): $1.37
* 10,000 calls: $13.7
* 100,000 calls: $137.0

To put this into perspective, the cost per 1M tokens is:
* Input: $0.55
* Output: $2.19
* Total (assuming 1:1 input:output ratio): $2.74 per 1M tokens

Compared to top competitors:
* OpenAI o1: $75.0 per 1M tokens (input: $15.0, output: $60.0)
* OpenAI o3-mini: $5.5 per 1M tokens (input

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 90.8 |
| HumanEval | 92.6 |
| LMSYS Arena ELO | 1358 |
| ARC | None |

## Benchmark Analysis
### DeepSeek R1 Benchmark Performance Analysis
#### Model Overview
The DeepSeek R1 model, released by DeepSeek on 2025-01-20, is an open-source model classified under the standard tier. It boasts a range of capabilities, including text, function calling, streaming, system prompts, and extended thinking, making it suitable for complex reasoning, math, coding, science, research, and PhD-level problems.

#### Pricing Structure
The pricing for DeepSeek R1 is as follows:
* Input: **$0.55 per 1M tokens**
* Output: **$2.19 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Benchmark Scores
DeepSeek R1 has achieved notable scores in various benchmarks:
* **MMLU: 90.8** - The MMLU (Measuring Massive Multitask Language Understanding) score indicates the model's ability to understand and generate human-like text across a wide range of tasks and topics. A higher score suggests better language understanding capabilities.
* **HumanEval: 92.6** - The HumanEval score measures the model's ability to generate correct and functional code in response to programming prompts. A higher score indicates stronger coding capabilities.
* **LMSYS Arena ELO: 1358** - The LMSYS Arena ELO score is a measure of the model's performance in a competitive environment, where it is pitted against other models in a series of tasks. A higher ELO score suggests better overall performance and adaptability.
* **GSM8K: 97.3** - The GSM8K score is a

## Competitor Comparison
### DeepSeek R1 Comparison with Top Competitors
#### Overview
The DeepSeek R1 model, released on 2025-01-20, is a standard, open-source model offered by DeepSeek. This comparison will delve into the pricing, performance, and use cases of DeepSeek R1 against its top competitors, OpenAI o1 and OpenAI o3-mini.

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

DeepSeek R1 offers significantly lower input and output prices compared to OpenAI o1, with a 96.3% reduction in input cost and a 96.3% reduction in output cost. In comparison to OpenAI o3-mini, DeepSeek R1 has a 50% lower input price and a 50.5% lower output price.

#### Performance Trade-offs
The performance of each model can be evaluated using the provided benchmarks:
* DeepSeek R1:
	+ MMLU: 90.8
	+ HumanEval: 92.6
	+ LMSYS Arena ELO: 1358
	+ GSM8K: 97.3
* OpenAI o1 and OpenAI o3-mini benchmarks are not provided, but their pricing suggests they may offer higher performance.

While the exact performance differences are unclear, the lower pricing of DeepSeek R1 may indicate a trade-off in terms of performance or capabilities.

#### Capabilities and Use Cases
DeepSeek R1 offers the following capabilities:
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

However, it is not recommended for:
* simple_tasks
* high_volume
* low_latency
* vision
* budget_conscious applications (despite its lower pricing)

#### Cost Examples
To illustrate the cost differences

## Best Use Cases
### Introduction to DeepSeek R1
DeepSeek R1 is a powerful language model released by DeepSeek on 2025-01-20. As an open-source model with a standard tier, it offers competitive pricing and impressive capabilities. In this guide, we will explore the top 5 best use cases for DeepSeek R1, along with code integration examples using OpenRouter.

### Top 5 Use Cases for DeepSeek R1
Based on its capabilities and benchmarks, DeepSeek R1 is best suited for the following use cases:

1. **Complex Reasoning and Problem-Solving**: With a high MMLU score of 90.8 and HumanEval score of 92.6, DeepSeek R1 excels in complex reasoning and problem-solving tasks.
2. **Math and Science Applications**: DeepSeek R1's high GSM8K score of 97.3 demonstrates its proficiency in math and science-related tasks, making it an excellent choice for research and PhD-level problems.
3. **Coding and Software Development**: With its ability to perform function calling and streaming, DeepSeek R1 can assist in coding tasks, such as code completion and code review.
4. **Research and Academic Writing**: DeepSeek R1's extended thinking capability and large context window of 64,000 tokens make it an ideal model for research and academic writing tasks.
5. **Scientific Research and Analysis**: DeepSeek R1's ability to process large amounts of text data and its high LMSYS Arena ELO score of 1358 make it a suitable choice for scientific research and analysis tasks.

### Code Integration Examples with OpenRouter
To integrate DeepSeek R1 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the DeepSeek R1 model
model = openrouter.Model("deepseek/deepseek-r1")

# Define a function to generate text using the model
def generate_text(prompt):
    response = model.generate

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
