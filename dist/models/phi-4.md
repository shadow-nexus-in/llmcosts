# Phi-4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-27
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Phi-4
The Phi-4 model, developed by Microsoft and released on 2024-12-12, is an open-source, budget-friendly language model. With its architecture designed for efficiency and cost-effectiveness, Phi-4 is particularly suited for coding, math, reasoning tasks, and edge deployment scenarios where budget constraints are a consideration. The model's capabilities include text processing, function calling, streaming, and system prompts, making it a versatile tool for a variety of applications.

### Technical Specifications and Pricing
Phi-4 operates with a context window of 16,384 tokens and can generate up to 4,096 tokens as output. The model's knowledge cutoff is 2024-06, indicating that its training data includes information up to that point. In terms of pricing, Phi-4 charges $0.07 per 1M tokens for input and $0.14 per 1M tokens for output. Notably, there are no additional charges for cached input or batch input. This pricing structure makes Phi-4 an attractive option for developers looking for a cost-effective solution. For example, 1,000 calls averaging 500 tokens would cost approximately $0.105, while 10,000 calls would cost $1.05, and 100,000 calls would cost $10.5.

### Performance and Competitors
Phi-4 demonstrates strong performance across various benchmarks, including MMLU (80.0), HumanEval (82.6), LMSYS Arena ELO (1200), and GSM8K (91.8). While it is not suited for tasks requiring vision, long context, high volume, frontier reasoning, or the latest knowledge, Phi-4's strengths in coding, math, and reasoning tasks make it a valuable asset for specific use cases. In comparison to its top competitors, such as Llama 3.2 3B Instruct and Llama 3.1 8B In

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
The Phi-4 model, released by Microsoft on 2024-12-12, is a budget-friendly, open-source option with a unique pricing structure. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale.

#### Cost Structure
The Phi-4 model has the following pricing tiers:
* Input: $0.07 per 1M tokens
* Output: $0.14 per 1M tokens
* Cached Input: $0.00 per 1M tokens (free)
* Batch Input: $0.00 per 1M tokens (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following scenarios:
* **Cached Tokens**: Use cached input tokens whenever possible, as they are free. This can significantly reduce costs for repeated or similar input queries.
* **Batch API**: Utilize batch input for multiple queries at once, as it is also free. This can help reduce the overall cost per query.

#### Cost at Scale
The cost of using Phi-4 at scale is as follows:
* **1,000 calls** (avg 500 tokens): $0.105
* **10,000 calls**: $1.05
* **100,000 calls**: $10.5

These costs demonstrate a linear scaling of expenses with the number of API calls.

#### Comparison to Competitors
Phi-4's pricing is competitive with other models in the market:
* **Llama 3.2 3B Instruct**: $0.06/1M input, $0.06/1M output
* **Llama 3.1 8B Instruct**: $0.07/1M input, $0.07/1M output

Phi-4's input pricing is on par with Llama 3.1 8B Instruct, while its output pricing is slightly higher.

####

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
The Phi-4 model, released by Microsoft on 2024-12-12, is a budget-friendly, open-source option with a tier classification as "budget". This analysis will delve into its benchmark performance, focusing on the MMLU, HumanEval, and Arena ELO scores, to understand its real-world applications.

#### Benchmark Performance
The Phi-4 model boasts the following benchmark scores:
- **MMLU: 80.0** - The MMLU (Measuring Massive Multitask Language Understanding) benchmark evaluates a model's ability to understand and generate human-like text across a wide range of tasks. A score of 80.0 indicates that Phi-4 has a strong foundation in language understanding, suitable for tasks that require generating coherent and contextually relevant text.
- **HumanEval: 82.6** - HumanEval is a benchmark that assesses a model's ability to write correct and functional code based on human-provided specifications. With a score of 82.6, Phi-4 demonstrates a high level of proficiency in coding tasks, making it a viable option for applications that involve code generation or programming-related queries.
- **LMSYS Arena ELO: 1200** - The LMSYS Arena ELO score is a measure of a model's overall performance in a competitive environment, where models are pitted against each other to solve various tasks. An ELO score of 1200 suggests that Phi-4 has a moderate to high level of competence, indicating it can perform well in a wide range of tasks but may struggle against more advanced or specialized models.

#### Real-World Implications
Given its benchmark performance, the Phi

## Competitor Comparison
### Phi-4 Model Comparison
#### Overview
The Phi-4 model, released by Microsoft on 2024-12-12, is a budget-friendly, open-source option for various applications, including coding, math, and reasoning tasks. This comparison will delve into the pricing, performance, and trade-offs of Phi-4 against its top competitors, Llama 3.2 3B Instruct and Llama 3.1 8B Instruct.

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
* Llama 3.2 3B Instruct and Llama 3.1 8B Instruct benchmarks are not provided, but their pricing suggests a potential trade-off between cost and performance.

#### Context and Limits
The context window and max output for Phi-4 are:
* Context Window: 16,384 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2024-06

#### Capabilities and Best Use Cases
Phi-4 is capable of:
* Text
* Function calling
* Streaming
* System prompts
It is best suited for:
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
* 10,000 calls:

## Best Use Cases
### Introduction to Phi-4
The Phi-4 model, released by Microsoft on 2024-12-12, is a budget-friendly and open-source language model. With its impressive benchmarks, including an MMLU score of 80.0 and a HumanEval score of 82.6, Phi-4 is well-suited for various applications, particularly those involving coding, math, and reasoning tasks.

### Top 5 Best Use Cases for Phi-4
Given its capabilities and limitations, here are the top 5 best use cases for Phi-4:

1. **Coding Assistance**: Phi-4 excels in coding tasks, making it an excellent choice for developers seeking to automate code completion, code review, or code generation. Its ability to understand and generate code in various programming languages can significantly improve development efficiency.
2. **Mathematical Reasoning**: With its strong performance in mathematical reasoning tasks, Phi-4 can be used to solve mathematical problems, generate mathematical proofs, or even assist in mathematical education.
3. **Edge Deployment**: Phi-4's cost-effectiveness and ability to operate within a limited context window make it an attractive choice for edge deployment scenarios, such as IoT devices or embedded systems, where computational resources are constrained.
4. **Reasoning Tasks**: Phi-4's strengths in reasoning tasks, such as logical deduction and problem-solving, make it suitable for applications like chatbots, virtual assistants, or decision support systems.
5. **Cost-Effective Reasoning**: For applications where budget is a concern, Phi-4 offers a cost-effective solution for reasoning tasks, providing a balance between performance and affordability.

### Code Integration Example with OpenRouter
To integrate Phi-4 with OpenRouter, you can use the following example code:
```python
import os
import openrouter

# Initialize OpenRouter
router = openrouter.Router()

# Define the Phi-4 model
model_name = "microsoft/phi-4"
model_version =

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
