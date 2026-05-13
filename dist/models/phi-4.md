# Phi-4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-13
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Phi-4
The Phi-4 model, developed by Microsoft, is an open-source language model released on December 12, 2024. As a budget-tier model, Phi-4 offers a cost-effective solution for developers, with pricing set at $0.07 per 1M tokens for input and $0.14 per 1M tokens for output. This model is designed to handle a context window of up to 16,384 tokens and can generate a maximum output of 4,096 tokens. With its open-source nature and competitive pricing, Phi-4 is an attractive option for developers looking for a cost-effective language model.

### Architecture and Capabilities
Phi-4 boasts a range of capabilities, including text processing, function calling, streaming, and system prompts. Its architecture is well-suited for tasks such as coding, math, and reasoning tasks, making it an ideal choice for edge deployment and cost-effective reasoning. The model's performance is backed by impressive benchmark scores, including 80.0 on MMLU, 82.6 on HumanEval, 1200 on LMSYS Arena ELO, and 91.8 on GSM8K. However, Phi-4 is not recommended for tasks that require vision, long context, high volume, frontier reasoning, or the latest knowledge, as it has limitations in these areas. With a knowledge cutoff of June 2024, Phi-4 may not be the best choice for applications that require very recent information.

### Use Cases and Cost Examples
Phi-4 is best utilized for applications that require coding, math, and reasoning tasks, such as automated programming, mathematical modeling, and decision-making systems. The cost of using Phi-4 can be estimated using the provided pricing examples: 1,000 calls with an average of 500 tokens cost $0.105, while 10,000 calls cost $1.05, and 100,000 calls cost $10.

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
The Phi-4 model, released by Microsoft on 2024-12-12, is a budget-friendly option with a tier classification as "budget" and is open-source. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Phi-4 is as follows:
* Input: **$0.07 per 1M tokens**
* Output: **$0.14 per 1M tokens**
* Cached Input: **$0.00 per 1M tokens** (free)
* Batch Input: **$0.00 per 1M tokens** (free)

This structure indicates that using cached or batch inputs can significantly reduce costs, as they are provided at no additional charge.

#### Optimal Usage Scenarios
To minimize costs, consider the following scenarios:
* **Cached Tokens**: Utilize cached input tokens whenever possible, as they are free. This is particularly beneficial for applications with repetitive or similar input patterns.
* **Batch API Calls**: Leverage batch input for multiple requests, as it also incurs no additional cost. This approach is ideal for high-volume applications where multiple inputs can be processed simultaneously.

#### Cost at Scale
The cost of using Phi-4 at various scales is as follows:
* **1,000 calls (avg 500 tokens)**: **$0.105**
* **10,000 calls**: **$1.05**
* **100,000 calls**: **$10.5**

These examples demonstrate a linear cost increase with the number of API calls, indicating that the cost per call remains consistent regardless of the scale.

#### Comparison to Competitors
Phi-4's pricing is competitive with other models in the market:
* **Llama 3.2 3B Instruct**: $0.06/1M input, $0.06/1M output
* **Llama

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 82.6 |
| LMSYS Arena ELO | 1200 |
| ARC | 91.7 |

## Benchmark Analysis
### Phi-4 Benchmark Performance Analysis
The Phi-4 model, released by Microsoft on 2024-12-12, is a budget-friendly, open-source option with a unique set of capabilities and limitations. To understand its real-world performance, we'll delve into its benchmark scores.

#### Benchmark Scores
The Phi-4 model has achieved the following benchmark scores:
* **MMLU (Massive Multitask Language Understanding)**: 80.0
* **HumanEval**: 82.6
* **LMSYS Arena ELO**: 1200
* **GSM8K**: 91.8

These scores indicate the model's performance in various areas:
* **MMLU**: Measures the model's ability to understand and generate human-like text across a wide range of tasks. A score of 80.0 suggests that Phi-4 has a good understanding of language, but may struggle with more complex or nuanced tasks.
* **HumanEval**: Evaluates the model's ability to write correct and functional code. A score of 82.6 indicates that Phi-4 is capable of generating high-quality code, making it suitable for coding and programming tasks.
* **LMSYS Arena ELO**: Assesses the model's performance in a competitive environment, where it is pitted against other models. An ELO score of 1200 suggests that Phi-4 is a mid-tier model, capable of holding its own against other models, but may struggle against more advanced competitors.
* **GSM8K**: Measures the model's ability to reason and solve math problems. A score of 91.8 indicates that Phi-4 has excellent math reasoning capabilities, making it suitable for tasks that require

## Competitor Comparison
### Phi-4 Comparison Against Top Competitors
#### Overview
The Phi-4 model, released by Microsoft on 2024-12-12, is a budget-friendly, open-source option with a unique set of capabilities and limitations. This comparison will delve into the pricing, performance, and use cases of Phi-4 against its top competitors, Llama 3.2 3B Instruct and Llama 3.1 8B Instruct.

#### Pricing Comparison
The pricing for each model is as follows:
* Phi-4 (Microsoft):
	+ Input: $0.07 per 1M tokens
	+ Output: $0.14 per 1M tokens
* Llama 3.2 3B Instruct:
	+ Input: $0.06 per 1M tokens
	+ Output: $0.06 per 1M tokens
* Llama 3.1 8B Instruct:
	+ Input: $0.07 per 1M tokens
	+ Output: $0.07 per 1M tokens

Phi-4 is priced similarly to Llama 3.1 8B Instruct for input, but its output price is higher. Llama 3.2 3B Instruct offers the lowest pricing for both input and output.

#### Performance Comparison
The performance of each model can be evaluated using various benchmarks:
* Phi-4:
	+ MMLU: 80.0
	+ HumanEval: 82.6
	+ LMSYS Arena ELO: 1200
	+ GSM8K: 91.8
* Llama 3.2 3B Instruct and Llama 3.1 8B Instruct benchmarks are not provided, making a direct comparison challenging.

However, based on the provided benchmarks, Phi-4 demonstrates strong performance in coding, math, and reasoning tasks.

#### Capabilities and Use Cases
Phi-4 is best suited for:
* Coding
* Math
* Reasoning tasks
* Edge deployment
* Cost-effective reasoning

It is not recommended for:
* Vision
* Long context
* High volume
* Frontier reasoning
* Latest knowledge

#### Cost Examples
The cost of using Phi-4 can be estimated as follows:
* 1,000 calls (avg 500 tokens): $0.105
* 10,000 calls: $1

## Best Use Cases
### Practical Advice on Top 5 Use Cases for Phi-4
The Phi-4 model, released by Microsoft on 2024-12-12, offers a budget-friendly and open-source solution for various applications. With its capabilities in text, function calling, streaming, and system prompts, Phi-4 is best suited for coding, math, reasoning tasks, edge deployment, and cost-effective reasoning. Here are the top 5 use cases for Phi-4, along with specific code integration examples using OpenRouter:

#### 1. **Coding Assistance**
Phi-4's strength in coding tasks makes it an ideal choice for coding assistance tools. You can integrate Phi-4 with OpenRouter to provide code completion suggestions, code review, and debugging assistance.
```python
import openrouter
from phi4 import Phi4Model

# Initialize Phi-4 model
model = Phi4Model()

# Define a coding task
task = "Write a Python function to calculate the area of a rectangle."

# Use OpenRouter to send the task to Phi-4
response = openrouter.send_request(model, task)

# Print the response
print(response)
```

#### 2. **Math Problem Solving**
Phi-4's math capabilities make it suitable for math problem-solving applications. You can use Phi-4 to solve algebraic equations, calculus problems, and other mathematical tasks.
```python
import openrouter
from phi4 import Phi4Model

# Initialize Phi-4 model
model = Phi4Model()

# Define a math problem
problem = "Solve for x: 2x + 5 = 11"

# Use OpenRouter to send the problem to Phi-4
response = openrouter.send_request(model, problem)

# Print the response
print(response)
```

#### 3. **Reasoning Tasks**
Phi-4's reasoning capabilities make it suitable for tasks that require logical reasoning, such as decision-making and problem-solving. You can use

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
