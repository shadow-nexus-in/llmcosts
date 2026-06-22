# DeepSeek R1 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-22
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to DeepSeek R1
The DeepSeek R1 model, released by DeepSeek on 2025-01-20, is a standard, open-source language model designed to handle complex tasks. Its architecture is geared towards providing robust capabilities in text processing, function calling, streaming, system prompts, and extended thinking. With a context window of 64,000 tokens and a maximum output of 8,192 tokens, DeepSeek R1 is well-suited for tasks that require in-depth analysis and reasoning.

### Technical Strengths and Use-Cases
DeepSeek R1 excels in tasks that demand complex reasoning, math, coding, science, and research, making it an ideal choice for PhD-level problems. Its benchmark scores, including 90.8 on MMLU, 92.6 on HumanEval, 1358 on LMSYS Arena ELO, and 97.3 on GSM8K, demonstrate its capabilities in handling intricate tasks. However, it may not be the best fit for simple tasks, high-volume applications, low-latency requirements, vision-related tasks, or budget-conscious projects. The model's pricing is competitive, with input costs at $0.55 per 1M tokens and output costs at $2.19 per 1M tokens.

### Cost Considerations and Competitors
To give developers a better understanding of the costs involved, examples are provided: 1,000 calls with an average of 500 tokens cost $1.37, while 10,000 calls cost $13.7, and 100,000 calls cost $137.0. In comparison to its top competitors, DeepSeek R1 offers a competitive pricing model. For instance, OpenAI's o1 model charges $15.0/1M input and $60.0/1M output, while the o3-mini model charges $1.1/1M input and $4.4/1M output. This makes Deep

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
DeepSeek R1 is a standard, open-source model released on 2025-01-20. It is priced based on input and output tokens, with specific costs for cached and batch inputs.

#### Cost Structure
The cost structure for DeepSeek R1 is as follows:
* Input: **$0.55 per 1M tokens**
* Output: **$2.19 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs when the same input is used multiple times. Since cached input is free, it is recommended to use cached tokens whenever possible to minimize costs.

#### Batch API Savings
Batch input is also free, which means that making batch API calls can help reduce costs. By batching multiple inputs together, users can take advantage of the free batch input pricing and save on costs.

#### Cost at Scale
The cost of using DeepSeek R1 at scale is as follows:
* **1,000 API calls (avg 500 tokens)**: **$1.37**
* **10,000 API calls**: **$13.7**
* **100,000 API calls**: **$137.0**

These costs are significantly lower than those of top competitors, such as OpenAI o1 and OpenAI o3-mini, which charge **$15.0/1M input** and **$1.1/1M input**, respectively.

#### Comparison to Top Competitors
Here is a comparison of the pricing of DeepSeek R1 with its top competitors:
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| DeepSeek R1 | $0.55 | $2.19 |


## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 90.8 |
| HumanEval | 92.6 |
| LMSYS Arena ELO | 1358 |
| ARC | None |

## Benchmark Analysis
### DeepSeek R1 Benchmark Performance Analysis
#### Introduction
The DeepSeek R1 model, released by DeepSeek on 2025-01-20, is an open-source standard tier model. This analysis will delve into its benchmark performance, focusing on the MMLU, HumanEval, and Arena ELO scores, and explain their implications for real-world use.

#### Benchmark Scores
The DeepSeek R1 model has achieved the following benchmark scores:
* **MMLU: 90.8** - The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to understand and generate text across a wide range of tasks. A score of 90.8 indicates that DeepSeek R1 has excellent language understanding capabilities.
* **HumanEval: 92.6** - The HumanEval benchmark assesses a model's ability to generate code that is correct and functional. A score of 92.6 suggests that DeepSeek R1 is highly proficient in coding tasks.
* **LMSYS Arena ELO: 1358** - The LMSYS Arena ELO benchmark measures a model's overall performance in a competitive environment. An ELO score of 1358 indicates that DeepSeek R1 is a strong competitor in the language model landscape.

#### Real-World Implications
These benchmark scores have significant implications for real-world use:
* **Complex Reasoning and Coding**: With high scores in MMLU and HumanEval, DeepSeek R1 is well-suited for complex reasoning, math, coding, science, and research tasks, making it an excellent choice for PhD-level problems.
* **Text and Function Calling**: The model's capabilities in text, function calling, streaming, system prompts

## Competitor Comparison
### DeepSeek R1 Comparison with Top Competitors
#### Overview
The DeepSeek R1 model, released on 2025-01-20, is a standard, open-source model offered by DeepSeek. This comparison will examine the pricing, performance, and capabilities of DeepSeek R1 against its top competitors, OpenAI o1 and OpenAI o3-mini.

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

DeepSeek R1 offers significant cost savings compared to OpenAI o1, with input and output prices approximately 27x and 27x lower, respectively. Compared to OpenAI o3-mini, DeepSeek R1 is roughly 2x cheaper for input and 0.5x cheaper for output.

#### Performance Trade-offs
The performance of each model can be evaluated using various benchmarks:
* DeepSeek R1:
	+ MMLU: 90.8
	+ HumanEval: 92.6
	+ LMSYS Arena ELO: 1358
	+ GSM8K: 97.3
* OpenAI o1 and o3-mini benchmark scores are not provided, making direct comparisons challenging. However, the high benchmark scores of DeepSeek R1 suggest strong performance in complex reasoning, math, coding, science, and research tasks.

#### Capabilities and Use Cases
DeepSeek R1 offers a range of capabilities, including:
* Text
* Function calling
* Streaming
* System prompts
* Extended thinking

It is best suited for tasks that require:
* Complex reasoning
* Math
* Coding
* Science
* Research
* PhD-level problems

However, it may not be the best choice for:
* Simple tasks
* High-volume requests
* Low-latency applications
* Vision tasks
* Budget-conscious projects

#### Cost Examples
To illustrate the cost differences, consider the following examples:
* 1,000 calls (avg 500 tokens): DeepSeek

## Best Use Cases
### Introduction to DeepSeek R1
DeepSeek R1 is a standard, open-source model released by DeepSeek on 2025-01-20. With its impressive benchmarks, including an MMLU score of 90.8 and a HumanEval score of 92.6, it is well-suited for complex reasoning, math, coding, science, research, and PhD-level problems.

### Top 5 Best Use Cases for DeepSeek R1
Based on its capabilities and limitations, the top 5 best use cases for DeepSeek R1 are:

1. **Complex Math Problem Solving**: DeepSeek R1 excels in math-related tasks, making it an ideal choice for solving complex mathematical problems. Its high GSM8K score of 97.3 demonstrates its ability to accurately solve math problems.
2. **Code Generation and Review**: With its function_calling and streaming capabilities, DeepSeek R1 can be used for code generation, review, and optimization. Its high HumanEval score of 92.6 indicates its proficiency in coding tasks.
3. **Scientific Research Assistance**: DeepSeek R1's ability to handle complex reasoning and its knowledge cutoff of 2024-11 make it a valuable tool for scientific research assistance, including literature review and hypothesis generation.
4. **PhD-Level Research Support**: DeepSeek R1's capabilities in extended thinking and complex reasoning make it an excellent choice for supporting PhD-level research, including thesis writing and research paper review.
5. **Education and Learning Platforms**: DeepSeek R1 can be integrated into education and learning platforms to provide personalized learning experiences, including adaptive assessments and learning path recommendations.

### Code Integration Example with OpenRouter
To integrate DeepSeek R1 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the OpenRouter client
client = openrouter.Client()

# Define the input prompt
prompt = "Solve the equation: 2x + 

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
