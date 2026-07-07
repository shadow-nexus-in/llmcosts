# Phi-4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-07
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Phi-4
The Phi-4 model, developed by Microsoft, is a budget-friendly, open-source language model released on 2024-12-12. With its architecture designed for cost-effective reasoning, Phi-4 is particularly suited for coding, math, and reasoning tasks, making it an attractive option for edge deployment scenarios. Its capabilities include text processing, function calling, streaming, and system prompts, showcasing its versatility in handling various tasks.

### Technical Specifications and Pricing
Phi-4 operates with a context window of 16,384 tokens and can generate up to 4,096 tokens as output. The model's knowledge cutoff is 2024-06, indicating that its training data is current up to that point. In terms of pricing, Phi-4 charges $0.07 per 1M tokens for input and $0.14 per 1M tokens for output. Notably, there are no charges for cached input or batch input. This pricing structure makes Phi-4 competitive, especially when compared to its top competitors like Llama 3.2 3B Instruct and Llama 3.1 8B Instruct, which charge $0.06/1M and $0.07/1M for input and output, respectively.

### Performance and Use Cases
Phi-4 demonstrates strong performance across various benchmarks, including MMLU (80.0), HumanEval (82.6), LMSYS Arena ELO (1200), and GSM8K (91.8). These scores highlight its capabilities in handling a range of tasks, from mathematical problems to coding challenges. Given its strengths and cost-effectiveness, Phi-4 is best utilized for coding, math, and reasoning tasks, especially in scenarios where budget is a concern. However, it may not be the best fit for tasks requiring vision capabilities, long context understanding, high-volume processing, frontier reasoning, or the need for the latest knowledge updates. Cost

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
* **Batch API calls**: With batch input tokens being free, batching API calls can help reduce overall costs.

#### Cost at Scale
The cost of using Phi-4 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: $0.105
* **10,000 calls**: $1.05
* **100,000 calls**: $10.5

These costs demonstrate a linear scaling of expenses with the number of API calls.

#### Comparison to Competitors
Phi-4's pricing is competitive with other models in the market:
* **Llama 3.2 3B Instruct**: $0.06/1M input, $0.06/1M output
* **Llama 3.1 8B Instruct**: $0.07/1M input, $0.07/1M output

While Phi-4's input price is comparable to Llama 3.1 8B Instruct, its output price is higher. However, the free cached input and batch input tokens can help offset these

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
The Phi-4 model, released by Microsoft on 2024-12-12, is a budget-friendly, open-source option with a tier classification of "budget". It offers competitive pricing for input and output tokens.

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
Phi-4's performance is measured across several benchmarks:
* **MMLU: 80.0** - The MMLU (Measuring Massive Multitask Language Understanding) score indicates the model's ability to understand and generate text across a wide range of tasks. A higher score signifies better performance.
* **HumanEval: 82.6** - HumanEval assesses a model's ability to generate code that meets specific requirements. The score reflects the model's coding capabilities, with higher scores indicating better performance.
* **LMSYS Arena ELO: 1200** - The LMSYS Arena ELO score measures a model's competitive performance in a variety of tasks, with higher scores indicating better overall performance.
* **GSM8K: 91.8** - The GSM8K score evaluates a model's math problem-solving abilities, with higher scores indicating better performance.



## Competitor Comparison
### Phi-4 Model Comparison
#### Introduction
The Phi-4 model, released by Microsoft on 2024-12-12, is a budget-friendly, open-source option for various natural language processing tasks. This comparison will delve into the pricing, performance, and trade-offs of Phi-4 against its top competitors, Llama 3.2 3B Instruct and Llama 3.1 8B Instruct.

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

#### Performance Trade-offs
The performance of each model can be evaluated using various benchmarks:

* Phi-4:
	+ MMLU: 80.0
	+ HumanEval: 82.6
	+ LMSYS Arena ELO: 1200
	+ GSM8K: 91.8
* Llama 3.2 3B Instruct and Llama 3.1 8B Instruct benchmarks are not provided, but their pricing suggests they may offer similar or better performance.

#### Context and Limits
The context window and output limits for Phi-4 are:

* Context Window: 16,384 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2024-06

#### Capabilities and Use Cases
Phi-4 is best suited for:
* Coding
* Math
* Reasoning tasks
* Edge deployment
* Cost-effective reasoning

However, it is not recommended for:
* Vision
* Long context
* High volume
* Frontier reasoning
* Latest knowledge

#### Cost Examples
The estimated costs for using Phi-4 are:
* 1,000 calls (avg 500 tokens): $0.105
* 10,000 calls: $1.05
* 100,000 calls: $10.5

#### Choosing the Right Model
Based on the pricing

## Best Use Cases
### Introduction to Phi-4
The Phi-4 model, released by Microsoft on 2024-12-12, is a budget-friendly and open-source language model. With its impressive benchmarks, including an MMLU score of 80.0 and a HumanEval score of 82.6, Phi-4 is well-suited for various applications, particularly those that require coding, math, and reasoning tasks.

### Top 5 Best Use Cases for Phi-4
Given its capabilities and limitations, here are the top 5 best use cases for Phi-4:

1. **Coding Assistance**: Phi-4's strong performance in coding tasks makes it an excellent choice for providing code completion suggestions, debugging assistance, and code review.
2. **Mathematical Reasoning**: With its high GSM8K score of 91.8, Phi-4 is well-suited for mathematical reasoning tasks, such as solving mathematical problems, generating mathematical proofs, and providing step-by-step solutions.
3. **Edge Deployment**: Phi-4's cost-effectiveness and ability to handle streaming inputs make it an ideal choice for edge deployment scenarios, such as real-time data processing, IoT applications, and autonomous systems.
4. **Reasoning Tasks**: Phi-4's strong performance in reasoning tasks, including its LMSYS Arena ELO score of 1200, makes it suitable for applications that require logical reasoning, such as decision-making systems, expert systems, and chatbots.
5. **Cost-Effective Reasoning**: Phi-4's budget-friendly pricing, with an input cost of $0.07 per 1M tokens and an output cost of $0.14 per 1M tokens, makes it an attractive choice for applications that require reasoning capabilities without breaking the bank.

### Code Integration Example with OpenRouter
To integrate Phi-4 with OpenRouter, you can use the following code example:
```python
import os
import openrouter

# Set up OpenRouter

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
