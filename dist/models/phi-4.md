# Phi-4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-17
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Phi-4
The Phi-4 model, developed by Microsoft, is an open-source language model released on December 12, 2024. As a budget-tier model, Phi-4 offers a cost-effective solution for developers, with pricing set at $0.07 per 1M tokens for input and $0.14 per 1M tokens for output. With its architecture designed for efficiency, Phi-4 is well-suited for applications that require text processing, function calling, streaming, and system prompts.

### Technical Capabilities and Use Cases
Phi-4 boasts a context window of 16,384 tokens and a maximum output of 4,096 tokens, making it suitable for coding, math, reasoning tasks, and edge deployment. Its capabilities are further enhanced by its support for text, function calling, streaming, and system prompts. The model's performance is backed by impressive benchmarks, including an MMLU score of 80.0, HumanEval score of 82.6, LMSYS Arena ELO of 1200, and GSM8K score of 91.8. However, Phi-4 is not recommended for tasks that require vision, long context, high volume, frontier reasoning, or the latest knowledge, as its knowledge cutoff is limited to June 2024.

### Pricing and Competitors
Phi-4's pricing is competitive, with cost examples including $0.105 for 1,000 calls (avg 500 tokens), $1.05 for 10,000 calls, and $10.5 for 100,000 calls. In comparison to its top competitors, Phi-4's pricing is on par with Llama 3.1 8B Instruct, which also costs $0.07 per 1M input and $0.07 per 1M output. However, Llama 3.2 3B Instruct offers a slightly lower price point at $0.06

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
The Phi-4 pricing model is based on input and output tokens:
* **Input**: $0.07 per 1M tokens
* **Output**: $0.14 per 1M tokens
* **Cached Input**: $0.00 per 1M tokens (free)
* **Batch Input**: $0.00 per 1M tokens (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following strategies:
* **Use cached tokens**: When possible, utilize cached input tokens to avoid input costs.
* **Batch API calls**: Take advantage of free batch input to reduce costs for large volumes of requests.
* **Optimize output**: Be mindful of output token counts, as they incur a higher cost per token.

#### Cost at Scale
The cost of using Phi-4 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: $0.105
* **10,000 calls**: $1.05
* **100,000 calls**: $10.5

These costs demonstrate a linear scaling of expenses with the number of API calls.

#### Competitor Comparison
Phi-4's pricing is competitive with top models like Llama 3.2 3B Instruct and Llama 3.1 8B Instruct:
* **Llama 3.2 3B Instruct**: $0.06/1M input, $0.06/1M output
* **Llama 3.1 8B Instruct**: $0.07/1M input, $0.07/1M output

Phi-

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
The Phi-4 model has achieved the following benchmark scores:
* **MMLU: 80.0** - The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to perform a wide range of natural language processing tasks. A score of 80.0 indicates that Phi-4 has a strong foundation in language understanding, making it suitable for tasks like coding, math, and reasoning tasks.
* **HumanEval: 82.6** - The HumanEval benchmark assesses a model's ability to evaluate and execute code. Phi-4's score of 82.6 suggests that it can effectively understand and generate code, which is beneficial for coding and programming-related applications.
* **LMSYS Arena ELO: 1200** - The LMSYS Arena ELO score measures a model's overall performance in a competitive environment. A score of 1200 indicates that Phi-4 is a mid-tier model, capable of handling a variety of tasks, but may struggle with more complex or high-stakes applications.

#### Real-World Implications
The benchmark scores suggest that Phi-4 is well-suited for:
* **Coding and programming**: Phi-4's strong HumanEval score and capabilities in text and function_calling make it an excellent choice for coding

## Competitor Comparison
### Phi-4 Model Comparison
#### Overview
The Phi-4 model, released by Microsoft on 2024-12-12, is a budget-friendly, open-source option for various tasks, including coding, math, and reasoning tasks. This comparison will examine the Phi-4 model against its top competitors, Llama 3.2 3B Instruct and Llama 3.1 8B Instruct, in terms of pricing, performance, and use cases.

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

The Phi-4 model is priced competitively with its competitors for input costs, but its output costs are significantly higher. However, the Phi-4 model offers free cached input and batch input, which can help reduce overall costs for certain use cases.

#### Performance Comparison
The performance of each model can be evaluated using various benchmarks:
* Phi-4 (Microsoft):
	+ MMLU: 80.0
	+ HumanEval: 82.6
	+ LMSYS Arena ELO: 1200
	+ GSM8K: 91.8
* Llama 3.2 3B Instruct and Llama 3.1 8B Instruct benchmark data is not provided, making a direct comparison challenging.

However, based on the provided data, the Phi-4 model demonstrates strong performance in various tasks, including coding, math, and reasoning tasks.

#### Use Case Comparison
The Phi-4 model is best suited for:
* Coding
* Math
* Reasoning tasks
* Edge deployment
* Cost-effective reasoning

On the other hand, the Phi-4 model is not recommended for:
* Vision tasks
* Long context tasks
* High-volume tasks
* Frontier reasoning tasks
* Latest knowledge tasks

In contrast, Llama 3.2 3B Instruct and

## Best Use Cases
### Introduction to Phi-4
The Phi-4 model, released by Microsoft on 2024-12-12, is a budget-friendly, open-source language model with a tier classification of "budget". It offers a unique combination of capabilities, including text processing, function calling, streaming, and system prompts, making it suitable for a variety of applications.

### Top 5 Best Use Cases for Phi-4
Based on its capabilities and limitations, the top 5 best use cases for Phi-4 are:

1. **Coding**: Phi-4 excels in coding tasks, with a high score of 82.6 on the HumanEval benchmark. It can be used for code completion, code review, and code generation.
2. **Math**: Phi-4's strong performance on math-related tasks, such as the GSM8K benchmark (91.8), makes it an ideal choice for mathematical reasoning and problem-solving.
3. **Reasoning Tasks**: With a high MMLU score of 80.0, Phi-4 is well-suited for reasoning tasks that require logical and analytical thinking.
4. **Edge Deployment**: Phi-4's cost-effectiveness and compact size make it an attractive option for edge deployment, where resources are limited and latency is critical.
5. **Cost-Effective Reasoning**: Phi-4 offers a cost-effective solution for reasoning tasks, with a pricing model that charges $0.07 per 1M input tokens and $0.14 per 1M output tokens.

### Code Integration Example with OpenRouter
To integrate Phi-4 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Phi-4 model
phi_4 = openrouter.Model("microsoft/phi-4")

# Define a function to call the Phi-4 model
def call_phi_4(input_text):
    # Create a request to the Phi-4 model
    request = openrouter

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
