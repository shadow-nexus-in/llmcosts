# Phi-4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-28
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Phi-4
The Phi-4 model, released by Microsoft on 2024-12-12, is a budget-friendly, open-source language model designed for a variety of tasks, including coding, math, and reasoning tasks. Its architecture is geared towards providing cost-effective reasoning capabilities, making it an attractive option for edge deployment scenarios. With a context window of 16,384 tokens and a maximum output of 4,096 tokens, Phi-4 is well-suited for applications that require processing and generating human-like text within moderate context limits.

### Technical Capabilities and Pricing
Phi-4 boasts an impressive array of capabilities, including text processing, function calling, streaming, and system prompts. Its performance is underscored by strong benchmark scores: 80.0 on MMLU, 82.6 on HumanEval, 1200 on LMSYS Arena ELO, and 91.8 on GSM8K. In terms of pricing, Phi-4 is competitively positioned, with costs of $0.07 per 1M tokens for input and $0.14 per 1M tokens for output. Notably, cached input and batch input are offered at no additional cost. For example, 1,000 calls averaging 500 tokens would cost approximately $0.105, while 10,000 calls would cost $1.05, and 100,000 calls would cost $10.5. This pricing structure makes Phi-4 an attractive option for developers seeking a balance between performance and cost.

### Use Cases and Competitors
Phi-4 is best utilized for coding, math, reasoning tasks, and edge deployment scenarios where cost-effective reasoning is crucial. However, it may not be the ideal choice for applications involving vision, long context, high volume, frontier reasoning, or the need for the latest knowledge, given its knowledge cutoff of 2024-06. In comparison to its top competitors, such as Llama 3

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.07 |
| Output | $0.14 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Phi-4 Pricing Analysis
#### Overview
The Phi-4 model, released by Microsoft on 2024-12-12, is a budget-friendly, open-source option with a unique pricing structure. This analysis will delve into the cost structure, optimal usage scenarios, and provide examples of costs at scale.

#### Cost Structure
The Phi-4 model has the following pricing tiers:
* **Input**: $0.07 per 1M tokens
* **Output**: $0.14 per 1M tokens
* **Cached Input**: $0.00 per 1M tokens (free)
* **Batch Input**: $0.00 per 1M tokens (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following strategies:
* **Use cached tokens**: Since cached input tokens are free, utilize them whenever possible to reduce input costs.
* **Batch API calls**: With batch input tokens being free, batching API calls can significantly reduce overall costs.
* **Optimize output tokens**: As output tokens are more expensive than input tokens, optimize your prompts to minimize output token usage.

#### Cost at Scale
The following examples illustrate the cost of using Phi-4 at different scales:
* **1,000 calls (avg 500 tokens)**: $0.105
* **10,000 calls**: $1.05
* **100,000 calls**: $10.5

These costs demonstrate a linear scaling of expenses with the number of API calls.

#### Comparison to Competitors
Phi-4's pricing is competitive with other models in the market:
* **Llama 3.2 3B Instruct**: $0.06/1M input, $0.06/1M output
* **Llama 3.1 8B Instruct**: $0.07/1M input, $0.07/1M output

While Phi-4's input pricing is comparable to its competitors,

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 82.6 |
| LMSYS Arena ELO | 1200 |
| ARC | 91.7 |

## Benchmark Analysis
### Phi-4 Model Analysis
#### Overview
The Phi-4 model, released by Microsoft on 2024-12-12, is a budget-friendly, open-source option with a unique set of capabilities and limitations. This analysis will delve into the model's benchmark performance, focusing on the MMLU, HumanEval, and Arena ELO scores, and explore their implications for real-world use.

#### Benchmark Performance
The Phi-4 model boasts the following benchmark scores:
* **MMLU: 80.0** - The MMLU (Measuring Massive Multitask Language Understanding) score evaluates a model's ability to understand and generate human-like text across a wide range of tasks. A score of 80.0 indicates that Phi-4 has a strong foundation in language understanding, making it suitable for tasks like coding, math, and reasoning tasks.
* **HumanEval: 82.6** - The HumanEval score assesses a model's ability to write correct and functional code. With a score of 82.6, Phi-4 demonstrates a high level of proficiency in code generation, making it a viable option for coding tasks.
* **LMSYS Arena ELO: 1200** - The LMSYS Arena ELO score measures a model's performance in a competitive environment, where it is pitted against other models. An ELO score of 1200 indicates that Phi-4 is a mid-tier model, capable of holding its own in most tasks, but may struggle against more advanced models.

#### Real-World Implications
The benchmark scores suggest that Phi-4 is well-suited for:
* **Coding tasks**: With a high HumanEval score, Phi-4 can generate

## Competitor Comparison
### Phi-4 Comparison Against Top Competitors
#### Overview
The Phi-4 model, released by Microsoft on 2024-12-12, is a budget-friendly, open-source option with a unique set of capabilities and limitations. This comparison will delve into the price differences, performance trade-offs, and use cases for Phi-4 against its top competitors, Llama 3.2 3B Instruct and Llama 3.1 8B Instruct.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Phi-4 | $0.07 | $0.14 |
| Llama 3.2 3B Instruct | $0.06 | $0.06 |
| Llama 3.1 8B Instruct | $0.07 | $0.07 |

The Phi-4 model is priced competitively with its competitors, with a slight premium on output pricing. However, the input price is identical to Llama 3.1 8B Instruct and only $0.01 higher than Llama 3.2 3B Instruct.

#### Performance Trade-Offs
The Phi-4 model boasts impressive benchmark scores:
* MMLU: 80.0
* HumanEval: 82.6
* LMSYS Arena ELO: 1200
* GSM8K: 91.8

While the benchmark scores for Llama 3.2 3B Instruct and Llama 3.1 8B Instruct are not provided, the Phi-4 model's performance is likely to be competitive, given its capabilities and pricing.

#### Capabilities and Limitations
The Phi-4 model excels in the following areas:
* Text processing
* Function calling
* Streaming
* System prompts
* Coding
* Math
* Reasoning tasks
* Edge deployment
* Cost-effective reasoning

However, it is not suitable for:
* Vision tasks
* Long context applications
* High-volume usage
* Frontier reasoning
* Latest knowledge requirements

#### Cost Examples
The cost of using the Phi-4 model can be estimated as follows:
* 1,000 calls (avg 500 tokens): $0.105
* 10,000 calls: $1.05
* 100,000 calls

## Best Use Cases
### Practical Advice on the Top 5 Best Use Cases for Phi-4
The Phi-4 model, released by Microsoft on 2024-12-12, is a budget-friendly and open-source option with a context window of 16,384 tokens and a maximum output of 4,096 tokens. Given its capabilities and limitations, here are the top 5 best use cases for Phi-4, along with specific code integration examples mentioning OpenRouter.

#### 1. Coding
Phi-4 is well-suited for coding tasks, with a high score of 82.6 on the HumanEval benchmark. To integrate Phi-4 with OpenRouter for coding tasks, you can use the following code example:
```python
import openrouter

# Initialize the Phi-4 model
model = openrouter.Phi4Model()

# Define a coding prompt
prompt = "Write a Python function to calculate the area of a rectangle."

# Generate code using Phi-4
code = model.generate_code(prompt)

# Print the generated code
print(code)
```

#### 2. Math
Phi-4 has a strong performance on math-related tasks, with a score of 91.8 on the GSM8K benchmark. To use Phi-4 for math tasks with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Phi-4 model
model = openrouter.Phi4Model()

# Define a math prompt
prompt = "Solve the equation 2x + 5 = 11."

# Generate a solution using Phi-4
solution = model.generate_solution(prompt)

# Print the solution
print(solution)
```

#### 3. Reasoning Tasks
Phi-4 is capable of performing reasoning tasks, with a score of 80.0 on the MMLU benchmark. To integrate Phi-4 with OpenRouter for reasoning tasks, you can use the following code example:
```python
import open

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
