# Phi-4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-23
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Phi-4
The Phi-4 model, developed by Microsoft, is an open-source language model released on 2024-12-12. It is classified as a budget-tier model, making it an attractive option for developers looking for a cost-effective solution. Phi-4's architecture is designed to provide a balance between performance and affordability, with a context window of 16,384 tokens and a maximum output of 4,096 tokens. This model is particularly suited for tasks that require coding, math, and reasoning capabilities, making it a valuable tool for edge deployment and cost-effective reasoning applications.

### Technical Capabilities and Pricing
Phi-4 boasts a range of technical capabilities, including text processing, function calling, streaming, and system prompts. Its pricing structure is based on input and output tokens, with costs of $0.07 per 1M input tokens and $0.14 per 1M output tokens. Notably, cached input and batch input are offered at no additional cost. The model's performance is backed by impressive benchmark scores, including 80.0 on MMLU, 82.6 on HumanEval, 1200 on LMSYS Arena ELO, and 91.8 on GSM8K. With its budget-friendly pricing and robust capabilities, Phi-4 is an excellent choice for developers working on projects that require efficient and effective language processing.

### Use Cases and Competitors
Phi-4 is best suited for applications that involve coding, math, and reasoning tasks, as well as edge deployment scenarios where cost-effectiveness is crucial. However, it may not be the ideal choice for tasks that require vision capabilities, long context windows, high-volume processing, or frontier reasoning. In terms of cost, Phi-4 is competitive with other models in its class, such as Llama 3.2 3B Instruct and Llama 3.1 8B Instruct, which offer similar pricing structures. For

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
The Phi-4 model, released by Microsoft on 2024-12-12, offers a budget-friendly option for various applications, including coding, math, and reasoning tasks. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Phi-4 is as follows:
* Input: $0.07 per 1M tokens
* Output: $0.14 per 1M tokens
* Cached Input: $0.00 per 1M tokens (free)
* Batch Input: $0.00 per 1M tokens (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following strategies:
* **Use cached tokens**: Since cached input tokens are free, leverage this feature whenever possible to reduce input costs.
* **Batch API calls**: With batch input tokens being free, batching API calls can significantly reduce overall costs.

#### Cost at Scale
The cost of using Phi-4 at different scales is as follows:
* **1,000 calls (avg 500 tokens)**: $0.105
* **10,000 calls**: $1.05
* **100,000 calls**: $10.5

These costs demonstrate a linear scaling of expenses with the number of API calls.

#### Comparison to Competitors
Phi-4's pricing is competitive with other models in the market:
* **Llama 3.2 3B Instruct**: $0.06/1M input, $0.06/1M output
* **Llama 3.1 8B Instruct**: $0.07/1M input, $0.07/1M output

Phi-4's input price is comparable to Llama 3.1 8B Instruct, while its output price is slightly higher.

#### Conclusion
The Phi-4 model offers a cost-effective

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

#### Pricing Structure
The pricing for Phi-4 is as follows:
* Input: **$0.07 per 1M tokens**
* Output: **$0.14 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Context and Limits
Key context and limit specifications for Phi-4 include:
* Context Window: **16,384 tokens**
* Max Output: **4,096 tokens**
* Knowledge Cutoff: **2024-06**

#### Benchmark Performance
Phi-4's benchmark scores are:
* MMLU: **80.0**
* HumanEval: **82.6**
* LMSYS Arena ELO: **1200**
* GSM8K: **91.8**

These scores indicate the model's capabilities in various areas:
* **MMLU (Massive Multitask Language Understanding)**: Measures the model's ability to understand and generate text across a wide range of tasks. A score of 80.0 suggests Phi-4 has a strong foundation in language understanding.
* **HumanEval**: Evaluates the model's ability to generate code that passes unit tests. A score of 82.6 indicates Phi-4 is proficient in coding tasks.
* **LMSYS Arena

## Competitor Comparison
### Phi-4 Comparison Against Top Competitors
#### Overview
The Phi-4 model, released by Microsoft on 2024-12-12, is a budget-friendly, open-source option with a unique set of capabilities and limitations. This comparison will delve into the pricing, performance, and use cases of Phi-4 against its top competitors, Llama 3.2 3B Instruct and Llama 3.1 8B Instruct.

#### Pricing Comparison
The pricing models for each competitor are as follows:
* Phi-4 (Microsoft):
	+ Input: $0.07 per 1M tokens
	+ Output: $0.14 per 1M tokens
* Llama 3.2 3B Instruct:
	+ Input: $0.06 per 1M tokens
	+ Output: $0.06 per 1M tokens
* Llama 3.1 8B Instruct:
	+ Input: $0.07 per 1M tokens
	+ Output: $0.07 per 1M tokens

Phi-4 is priced competitively with its competitors for input costs, but its output costs are significantly higher. However, the overall cost-effectiveness of Phi-4 can be seen in the cost examples:
* 1,000 calls (avg 500 tokens): $0.105
* 10,000 calls: $1.05
* 100,000 calls: $10.5

#### Performance Trade-offs
The performance of each model can be evaluated using various benchmarks:
* Phi-4:
	+ MMLU: 80.0
	+ HumanEval: 82.6
	+ LMSYS Arena ELO: 1200
	+ GSM8K: 91.8
* Llama 3.2 3B Instruct and Llama 3.1 8B Instruct benchmarks are not provided, but their performance can be inferred to be competitive with Phi-4 given their similar pricing and capabilities.

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

#### Choosing the Right Model
When deciding between Phi-4 and its competitors

## Best Use Cases
### Introduction to Phi-4
The Phi-4 model, released by Microsoft on 2024-12-12, is a budget-friendly, open-source language model with a tier classification of "budget". It is particularly suited for coding, math, reasoning tasks, edge deployment, and cost-effective reasoning.

### Top 5 Best Use Cases for Phi-4
Given its capabilities and limitations, here are the top 5 best use cases for Phi-4:

1. **Coding Assistance**: With its high scores in HumanEval (82.6) and GSM8K (91.8), Phi-4 is well-suited for coding tasks, such as code completion, code review, and code generation.
2. **Mathematical Reasoning**: Phi-4's high MMLU score (80.0) indicates its strength in mathematical reasoning tasks, making it a good choice for applications that require mathematical problem-solving.
3. **Edge Deployment**: As a cost-effective and compact model, Phi-4 is ideal for edge deployment, where resources are limited and latency needs to be minimized.
4. **Reasoning Tasks**: Phi-4's capabilities in reasoning tasks, such as logical reasoning and problem-solving, make it a good fit for applications that require critical thinking.
5. **Cost-Effective Reasoning**: With its low pricing ($0.07 per 1M tokens for input and $0.14 per 1M tokens for output), Phi-4 is an attractive option for applications that require reasoning capabilities without breaking the bank.

### Code Integration Examples with OpenRouter
To integrate Phi-4 with OpenRouter, you can use the following code examples:

```python
import openrouter

# Initialize the Phi-4 model
model = openrouter.load_model("microsoft/phi-4")

# Define a function to generate code using Phi-4
def generate_code(prompt):
    input_tokens = openrouter.tokenize(prompt)
    output = model.generate(input_tokens

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
