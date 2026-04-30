# Phi-4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-30
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Phi-4
Phi-4, developed by Microsoft, is an open-source language model released on 2024-12-12. This budget-tier model boasts a unique architecture that enables efficient processing of input and output tokens. With a context window of 16,384 tokens and a maximum output of 4,096 tokens, Phi-4 is well-suited for a variety of applications, including coding, math, and reasoning tasks. Its capabilities extend to text processing, function calling, streaming, and system prompts, making it a versatile tool for developers.

### Technical Strengths and Use-Cases
Phi-4's main strengths lie in its cost-effectiveness and performance in specific tasks. Its pricing model charges $0.07 per 1M input tokens and $0.14 per 1M output tokens, with no additional costs for cached or batch input. The model has demonstrated impressive benchmark scores, including 80.0 on MMLU, 82.6 on HumanEval, 1200 on LMSYS Arena ELO, and 91.8 on GSM8K. These results indicate that Phi-4 is particularly well-suited for coding, math, and reasoning tasks, as well as edge deployment scenarios where cost-effective reasoning is crucial. However, it may not be the best choice for tasks that require vision, long context, high volume, frontier reasoning, or the latest knowledge.

### Pricing and Competitors
Phi-4's pricing model offers a competitive edge, with cost examples including $0.105 for 1,000 calls (avg 500 tokens), $1.05 for 10,000 calls, and $10.5 for 100,000 calls. In comparison to its top competitors, such as Llama 3.2 3B Instruct and Llama 3.1 8B Instruct, Phi-4's pricing is on par, with input and output costs of $0.

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
The Phi-4 model, released by Microsoft on 2024-12-12, offers a budget-friendly option for various applications, including coding, math, and reasoning tasks. With its open-source nature and competitive pricing, it's an attractive choice for developers and businesses looking for cost-effective solutions.

#### Cost Structure
The cost structure of Phi-4 is as follows:
* **Input**: $0.07 per 1M tokens
* **Output**: $0.14 per 1M tokens
* **Cached Input**: No additional cost
* **Batch Input**: No additional cost

This structure indicates that the primary cost driver is the number of input and output tokens. However, using cached input or batch input can help reduce costs, as there are no additional fees associated with these features.

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs when:
* The same input is used multiple times
* The input is relatively small compared to the output
* The application requires frequent queries with similar input

By leveraging cached tokens, developers can avoid incurring additional costs for repeated input, making Phi-4 a more cost-effective option for certain use cases.

#### Batch API Savings
Batch input can also help reduce costs by allowing developers to process multiple inputs at once. Since there is no additional cost for batch input, this feature can be particularly useful for applications that require processing large volumes of data.

#### Cost at Scale
To illustrate the cost-effectiveness of Phi-4 at scale, consider the following examples:
* **1,000 calls (avg 500 tokens)**: $0.105
* **10,000 calls**: $1.05
* **100,000 calls**: $10.5

These examples demonstrate that Phi-4 can be a cost-effective option for large-scale applications, with costs increasing linearly with the number of API calls.

#### Comparison to Competitors
Phi-

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 82.6 |
| LMSYS Arena ELO | 1200 |
| ARC | 91.7 |

## Benchmark Analysis
### Phi-4 Benchmark Performance Analysis
The Phi-4 model, released by Microsoft on 2024-12-12, is a budget-friendly, open-source option with a unique set of capabilities and limitations. To understand its performance, we'll delve into its benchmark scores and what they mean for real-world use.

#### Benchmark Scores
The Phi-4 model has achieved the following benchmark scores:
* **MMLU: 80.0** - The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to perform a wide range of natural language processing tasks. A score of 80.0 indicates that Phi-4 has a strong foundation in language understanding, making it suitable for tasks like coding, math, and reasoning tasks.
* **HumanEval: 82.6** - The HumanEval benchmark assesses a model's ability to evaluate and execute Python code. A score of 82.6 suggests that Phi-4 is proficient in understanding and executing code, which is beneficial for coding and programming-related tasks.
* **LMSYS Arena ELO: 1200** - The LMSYS Arena ELO score measures a model's performance in a competitive environment, where it's pitted against other models. An ELO score of 1200 indicates that Phi-4 is a mid-tier model, capable of holding its own in a variety of tasks, but may struggle against more advanced models.
* **GSM8K: 91.8** - The GSM8K benchmark evaluates a model's ability to solve math problems. A score of 91.8 demonstrates that Phi-4 has a strong grasp of mathematical concepts, making it suitable for math-related tasks.

####

## Competitor Comparison
### Phi-4 Comparison Against Top Competitors
#### Overview
The Phi-4 model, released by Microsoft on 2024-12-12, is a budget-friendly, open-source option with a unique set of capabilities and limitations. This comparison will delve into the pricing, performance, and use cases of Phi-4 against its top competitors, Llama 3.2 3B Instruct and Llama 3.1 8B Instruct.

#### Pricing Comparison
The pricing structure for each model is as follows:
* Phi-4 (Microsoft):
	+ Input: $0.07 per 1M tokens
	+ Output: $0.14 per 1M tokens
* Llama 3.2 3B Instruct:
	+ Input: $0.06 per 1M tokens
	+ Output: $0.06 per 1M tokens
* Llama 3.1 8B Instruct:
	+ Input: $0.07 per 1M tokens
	+ Output: $0.07 per 1M tokens

Phi-4 is priced similarly to Llama 3.1 8B Instruct for input tokens, but its output token price is higher. Llama 3.2 3B Instruct offers the most competitive pricing for both input and output tokens.

#### Performance Trade-offs
The performance of each model can be evaluated using various benchmarks:
* Phi-4:
	+ MMLU: 80.0
	+ HumanEval: 82.6
	+ LMSYS Arena ELO: 1200
	+ GSM8K: 91.8
* Llama 3.2 3B Instruct and Llama 3.1 8B Instruct benchmarks are not provided, but their performance is expected to be competitive given their similar pricing and capabilities.

Phi-4 demonstrates strong performance across various benchmarks, indicating its suitability for tasks such as coding, math, and reasoning tasks.

#### Capabilities and Use Cases
Each model has its strengths and weaknesses:
* Phi-4:
	+ Capabilities: text, function_calling, streaming, system_prompts
	+ Best for: coding, math, reasoning_tasks, edge_deployment, cost_effective_reasoning
	+ Not good for: vision, long_context, high_volume, frontier_reasoning, latest_knowledge
* Llama 3

## Best Use Cases
### Practical Advice on Top 5 Best Use Cases for Phi-4
The Phi-4 model, released by Microsoft on 2024-12-12, is a budget-friendly and open-source option with a context window of 16,384 tokens and a max output of 4,096 tokens. Given its capabilities and limitations, here are the top 5 best use cases for Phi-4, along with specific code integration examples mentioning OpenRouter.

#### 1. Coding
Phi-4 excels in coding tasks, making it an ideal choice for applications that require code generation or completion. For example, you can use Phi-4 with OpenRouter to generate code snippets for a specific programming language.
```python
import openrouter

# Initialize Phi-4 model
model = openrouter.Phi4()

# Define a coding prompt
prompt = "Generate a Python function to calculate the area of a circle."

# Get the response from Phi-4
response = model.generate(prompt)

# Print the generated code
print(response)
```

#### 2. Math
Phi-4 is well-suited for math-related tasks, such as equation solving and mathematical reasoning. You can use Phi-4 with OpenRouter to solve mathematical problems, like this example:
```python
import openrouter

# Initialize Phi-4 model
model = openrouter.Phi4()

# Define a math prompt
prompt = "Solve the equation x^2 + 4x + 4 = 0."

# Get the response from Phi-4
response = model.generate(prompt)

# Print the solution
print(response)
```

#### 3. Reasoning Tasks
Phi-4 is capable of performing reasoning tasks, such as logical deductions and problem-solving. For example, you can use Phi-4 with OpenRouter to solve a logical puzzle:
```python
import openrouter

# Initialize Phi-4 model
model = openrouter.Phi4()

# Define a reasoning

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
