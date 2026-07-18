# Phi-4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-18
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Phi-4
The Phi-4 model, developed by Microsoft and released on 2024-12-12, is a budget-friendly, open-source language model designed for a variety of tasks, including coding, math, and reasoning tasks. Its architecture is optimized for edge deployment and cost-effective reasoning, making it an attractive option for developers who require a balance between performance and affordability. With a context window of 16,384 tokens and a maximum output of 4,096 tokens, Phi-4 is well-suited for applications that involve moderate-length input and output sequences.

### Technical Capabilities and Pricing
Phi-4 boasts a range of technical capabilities, including text processing, function calling, streaming, and system prompts. Its pricing model is based on input and output tokens, with costs of $0.07 per 1M input tokens and $0.14 per 1M output tokens. Notably, cached input and batch input are offered at no additional cost. The model's performance is backed by impressive benchmark scores, including 80.0 on MMLU, 82.6 on HumanEval, 1200 on LMSYS Arena ELO, and 91.8 on GSM8K. With cost examples ranging from $0.105 for 1,000 calls (avg 500 tokens) to $10.5 for 100,000 calls, Phi-4 offers a cost-effective solution for developers who require a reliable language model for their applications.

### Use Cases and Competitors
Phi-4 is best suited for coding, math, and reasoning tasks, as well as edge deployment scenarios where cost-effectiveness is a primary concern. However, it may not be the best choice for applications that involve vision, long context, high volume, frontier reasoning, or the need for the latest knowledge. In terms of competition, Phi-4 is positioned alongside other models such as Llama 3.2 3B Instruct and L

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
The Phi-4 model, released by Microsoft on 2024-12-12, is a budget-friendly, open-source option with a unique pricing structure. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The Phi-4 model has the following pricing components:
* **Input**: $0.07 per 1M tokens
* **Output**: $0.14 per 1M tokens
* **Cached Input**: $0.00 per 1M tokens (free)
* **Batch Input**: $0.00 per 1M tokens (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following strategies:
* **Use cached tokens**: Since cached input tokens are free, utilize them whenever possible to reduce input costs.
* **Batch API calls**: With batch input tokens being free, batching API calls can significantly reduce overall costs.

#### Cost at Scale
The cost of using Phi-4 at different scales is as follows:
* **1,000 calls (avg 500 tokens)**: $0.105
* **10,000 calls**: $1.05
* **100,000 calls**: $10.5

These costs demonstrate a linear scaling of expenses with the number of API calls.

#### Competitor Comparison
In comparison to top competitors:
* **Llama 3.2 3B Instruct**: $0.06/1M input, $0.06/1M output
* **Llama 3.1 8B Instruct**: $0.07/1M input, $0.07/1M output

Phi-4's input pricing is competitive, but its output pricing is higher. However, the free cached input and batch input tokens can help offset these costs in certain use cases.

#### Conclusion
The Phi-4 model offers a cost-effective solution for

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
The Phi-4 model, released by Microsoft on 2024-12-12, is a budget-friendly, open-source option with a tier classification of "budget". This analysis will delve into the benchmark performance of Phi-4, exploring what the MMLU, HumanEval, and Arena ELO scores signify for real-world applications.

#### Pricing
The pricing structure for Phi-4 is as follows:
* Input: **$0.07 per 1M tokens**
* Output: **$0.14 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Context and Limits
Key context and limit specifications include:
* Context Window: **16,384 tokens**
* Max Output: **4,096 tokens**
* Knowledge Cutoff: **2024-06**

#### Benchmarks
Phi-4's benchmark performance is summarized below:
* MMLU: **80.0**
* HumanEval: **82.6**
* LMSYS Arena ELO: **1200**
* GSM8K: **91.8**

These benchmarks provide insight into the model's capabilities:
* **MMLU (Massive Multitask Language Understanding)**: A score of 80.0 indicates Phi-4's ability to understand and process a wide range of language tasks, with higher scores representing better performance.
* **HumanEval**: With a score of 82.6, Phi-4 demonstrates its capacity for human-like evaluation of code and text, suggesting strong reasoning and coding abilities.
* **LMSYS Arena ELO**: An ELO score of

## Competitor Comparison
### Phi-4 Comparison Against Top Competitors
#### Overview
The Phi-4 model, released by Microsoft on 2024-12-12, is a budget-friendly, open-source option for various tasks, including coding, math, and reasoning tasks. This comparison will delve into the pricing, performance, and use cases of Phi-4 against its top competitors, Llama 3.2 3B Instruct and Llama 3.1 8B Instruct.

#### Pricing Comparison
The pricing for each model is as follows:
* Phi-4:
	+ Input: $0.07 per 1M tokens
	+ Output: $0.14 per 1M tokens
* Llama 3.2 3B Instruct:
	+ Input: $0.06 per 1M tokens
	+ Output: $0.06 per 1M tokens
* Llama 3.1 8B Instruct:
	+ Input: $0.07 per 1M tokens
	+ Output: $0.07 per 1M tokens

Phi-4 is priced competitively with Llama 3.1 8B Instruct for input tokens but is more expensive for output tokens. Llama 3.2 3B Instruct offers the most cost-effective option for both input and output tokens.

#### Performance Trade-offs
The performance of each model can be evaluated based on the provided benchmarks:
* Phi-4:
	+ MMLU: 80.0
	+ HumanEval: 82.6
	+ LMSYS Arena ELO: 1200
	+ GSM8K: 91.8
* Llama 3.2 3B Instruct and Llama 3.1 8B Instruct benchmarks are not provided, making direct comparisons challenging.

However, based on the capabilities and best use cases, Phi-4 excels in coding, math, and reasoning tasks, making it a strong contender in these areas.

#### When to Choose Each Model
* **Phi-4**:
	+ Choose for coding, math, and reasoning tasks where cost-effectiveness is crucial.
	+ Suitable for edge deployment due to its budget-friendly pricing.
	+ Not recommended for vision, long context, high volume, frontier reasoning, or tasks requiring the latest knowledge.
* **Llama 3.2 3B Instruct**:


## Best Use Cases
### Practical Advice on Top 5 Best Use Cases for Phi-4
The Phi-4 model, released by Microsoft on 2024-12-12, is a budget-friendly and open-source option with a tier classification of "budget". Given its capabilities and limitations, here are the top 5 best use cases for Phi-4, along with specific code integration examples mentioning OpenRouter:

#### 1. **Coding**
Phi-4 excels in coding tasks, making it an ideal choice for automated code generation, code review, and code completion. To integrate Phi-4 with OpenRouter for coding tasks, you can use the following example:
```python
import openrouter

# Initialize Phi-4 model
model = openrouter.Phi4()

# Define a coding prompt
prompt = "Write a Python function to calculate the area of a circle"

# Generate code using Phi-4
code = model.generate_code(prompt)

# Print the generated code
print(code)
```
#### 2. **Math**
Phi-4's math capabilities make it suitable for tasks such as mathematical reasoning, equation solving, and numerical computations. To use Phi-4 with OpenRouter for math tasks, you can use the following example:
```python
import openrouter

# Initialize Phi-4 model
model = openrouter.Phi4()

# Define a math prompt
prompt = "Solve the equation x^2 + 4x + 4 = 0"

# Generate solution using Phi-4
solution = model.solve_math(prompt)

# Print the solution
print(solution)
```
#### 3. **Reasoning Tasks**
Phi-4's reasoning capabilities make it suitable for tasks such as logical reasoning, problem-solving, and decision-making. To integrate Phi-4 with OpenRouter for reasoning tasks, you can use the following example:
```python
import openrouter

# Initialize Phi-4 model
model = openrouter.Phi4()

# Define a reasoning

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
