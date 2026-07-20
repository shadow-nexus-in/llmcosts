# Phi-4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-20
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Phi-4
The Phi-4 model, developed by Microsoft and released on 2024-12-12, is an open-source, budget-friendly language model designed for a variety of tasks, including coding, math, and reasoning tasks. With its architecture optimized for cost-effectiveness and performance, Phi-4 offers a unique blend of capabilities, making it an attractive choice for developers looking for a reliable and affordable language model. Its key strengths include a large context window of 16,384 tokens, the ability to generate up to 4,096 tokens of output, and support for text, function calling, streaming, and system prompts.

### Technical Capabilities and Use Cases
Phi-4 excels in specific use cases such as coding, math, and reasoning tasks, where its capabilities in text processing, function calling, and streaming provide significant advantages. The model's performance is backed by impressive benchmark scores, including 80.0 on MMLU, 82.6 on HumanEval, 1200 on LMSYS Arena ELO, and 91.8 on GSM8K. However, it's essential to note that Phi-4 is not suited for tasks requiring vision, long context, high volume, frontier reasoning, or the latest knowledge, as indicated by its knowledge cutoff of 2024-06. For developers working on projects that fit within Phi-4's strengths, the model offers a cost-effective solution with pricing set at $0.07 per 1M tokens for input and $0.14 per 1M tokens for output.

### Pricing and Cost Examples
The pricing model for Phi-4 is straightforward, with input costing $0.07 per 1M tokens and output costing $0.14 per 1M tokens. There are no additional costs for cached input or batch input. To give developers a better understanding of the costs involved, example scenarios include 1,000 calls averaging 500 tokens, which would cost

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
The Phi-4 model, released by Microsoft on 2024-12-12, offers a budget-friendly option for various applications, including coding, math, and reasoning tasks. As an open-source model, it provides a cost-effective solution for users.

#### Cost Structure
The cost structure of Phi-4 is as follows:
* **Input**: $0.07 per 1M tokens
* **Output**: $0.14 per 1M tokens
* **Cached Input**: No additional cost ($None per 1M tokens)
* **Batch Input**: No additional cost ($None per 1M tokens)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs when the same input is used multiple times. Since there is no additional cost for cached input, it is recommended to use cached tokens whenever possible to minimize expenses.

#### Batch API Savings
Batching API calls can also help reduce costs. Although the pricing table does not provide a specific discount for batch input, the fact that there is no additional cost for batch input suggests that Microsoft encourages users to batch their API calls to improve efficiency and reduce costs.

#### Cost at Scale
The cost of using Phi-4 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: $0.105
* **10,000 calls**: $1.05
* **100,000 calls**: $10.5

These costs demonstrate a linear scaling of expenses with the number of API calls, indicating that the cost per call remains consistent regardless of the volume.

#### Comparison with Top Competitors
Phi-4's pricing is competitive with other models in the market:
* **Llama 3.2 3B Instruct**: $0.06/1M input, $0.06/1M output
* **Llama 3.1 8B Instruct**: $0.07/

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
The Phi-4 model, developed by Microsoft, is a budget-friendly, open-source option with a release date of 2024-12-12. It offers competitive pricing and impressive benchmark performance.

#### Pricing
The pricing structure for Phi-4 is as follows:
* Input: **$0.07 per 1M tokens**
* Output: **$0.14 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Context and Limits
The model has the following context and limits:
* Context Window: **16,384 tokens**
* Max Output: **4,096 tokens**
* Knowledge Cutoff: **2024-06**

#### Benchmarks
The Phi-4 model has achieved the following benchmark scores:
* **MMLU: 80.0** - The MMLU (Measuring Massive Multitask Language Understanding) benchmark evaluates a model's ability to perform a wide range of tasks. A higher score indicates better performance. Phi-4's score of 80.0 suggests strong multitask capabilities.
* **HumanEval: 82.6** - The HumanEval benchmark assesses a model's ability to evaluate and execute Python code. A higher score indicates better performance. Phi-4's score of 82.6 suggests strong coding capabilities.
* **LMSYS Arena ELO: 1200** - The LMSYS Arena ELO benchmark evaluates a model's overall performance in a competitive setting. A higher score indicates better performance. Phi-4's score of 1200 suggests strong overall performance.
* **GSM

## Competitor Comparison
### Phi-4 Model Comparison
#### Introduction
The Phi-4 model, released by Microsoft on 2024-12-12, is a budget-friendly, open-source option for various tasks, including coding, math, and reasoning tasks. This comparison will delve into the pricing, performance, and trade-offs of Phi-4 against its top competitors, Llama 3.2 3B Instruct and Llama 3.1 8B Instruct.

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

Based on the pricing, Llama 3.2 3B Instruct is the most cost-effective option for both input and output. Phi-4 and Llama 3.1 8B Instruct have the same input price, but Phi-4's output price is higher.

#### Performance Comparison
The performance of each model can be evaluated using various benchmarks:
* Phi-4:
	+ MMLU: 80.0
	+ HumanEval: 82.6
	+ LMSYS Arena ELO: 1200
	+ GSM8K: 91.8
* Llama 3.2 3B Instruct and Llama 3.1 8B Instruct benchmark scores are not provided.

Given the available data, Phi-4 demonstrates strong performance across various tasks. However, without benchmark scores for Llama 3.2 3B Instruct and Llama 3.1 8B Instruct, a direct comparison is challenging.

#### Capabilities and Limitations
Phi-4 offers the following capabilities:
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

However, Phi-4 is not recommended for:
* Vision
* Long context

## Best Use Cases
### Introduction to Phi-4
The Phi-4 model, released by Microsoft on 2024-12-12, is a budget-friendly and open-source option for various applications. With its impressive benchmarks, including an MMLU score of 80.0 and a HumanEval score of 82.6, Phi-4 is well-suited for coding, math, reasoning tasks, and edge deployment.

### Top 5 Best Use Cases for Phi-4
Based on its capabilities and limitations, here are the top 5 best use cases for Phi-4:

1. **Coding Assistance**: Phi-4's high scores in HumanEval (82.6) and LMSYS Arena ELO (1200) make it an excellent choice for coding tasks, such as code completion, code review, and code generation.
2. **Math and Reasoning Tasks**: With its strong performance in GSM8K (91.8), Phi-4 is well-suited for math and reasoning tasks, including mathematical problem-solving, logical reasoning, and critical thinking.
3. **Edge Deployment**: Phi-4's cost-effectiveness and compact size make it an ideal choice for edge deployment, where resources are limited, and latency is critical.
4. **Text Analysis and Generation**: Phi-4's capabilities in text processing, including text classification, sentiment analysis, and text generation, make it a suitable choice for applications such as chatbots, language translation, and content generation.
5. **Function Calling and Streaming**: Phi-4's support for function calling and streaming enables it to be used in real-time applications, such as voice assistants, live chat support, and streaming data processing.

### Code Integration Examples with OpenRouter
To integrate Phi-4 with OpenRouter, you can use the following code examples:
```python
import openrouter
from phi4 import Phi4Model

# Initialize the Phi-4 model
model = Phi4Model()

# Define a function to call the

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
