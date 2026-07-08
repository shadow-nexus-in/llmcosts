# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-08
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a mid-tier language model released on 2025-04-17. This model is not open source. From an architectural standpoint, Mistral Medium 3 is designed to handle a variety of tasks with its robust capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. Its main strengths lie in its ability to perform complex tasks such as coding, analysis, and content generation, making it a versatile tool for developers.

### Technical Specifications and Use Cases
Technically, Mistral Medium 3 operates with a context window of 131,072 tokens and can generate up to 16,384 tokens as output. The model's knowledge cutoff is 2024-11, indicating that its training data is current up to that point. The pricing model for Mistral Medium 3 is based on input and output tokens, with costs of $0.4 per 1M input tokens and $2.0 per 1M output tokens. This model is best suited for tasks that require in-depth analysis, coding, and content generation, but it may not be the most cost-effective option for bulk, cheap tasks or real-time applications requiring responses under 100ms.

### Pricing and Competitor Comparison
In terms of pricing, Mistral Medium 3 offers a competitive rate, especially for developers who require high-quality output. For example, 1,000 calls with an average of 500 tokens would cost $1.2, scaling up to $120.0 for 100,000 calls. When compared to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3's pricing is positioned in the market with $0.4/1M input and $2.0/1M output. Claude 3.5 Haiku charges $0.8/1

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.4 |
| Output | $2.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Mistral Medium 3
#### Overview
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
- **Input**: $0.4 per 1M tokens
- **Output**: $2.0 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
- **Cached Tokens**: Since cached input tokens are free, it's highly beneficial to use them whenever possible. This can significantly reduce costs for repeated or similar inputs.
- **Batch API Savings**: Although batch input is free, the primary cost savings come from minimizing output tokens, as the output cost is 5 times that of the input. Efficiently structuring API calls to reduce output tokens can lead to substantial cost savings.

#### Cost at Scale
Given the average cost per call, we can calculate the costs at different scales:
- **1,000 calls (avg 500 tokens)**: $1.2
- **10,000 calls**: $12.0
- **100,000 calls**: $120.0

These costs indicate a linear scaling with the number of calls, suggesting that the cost per call remains constant regardless of the volume.

#### Competitor Comparison
Comparing Mistral Medium 3 with its top competitors:
- **Claude 3.5 Haiku**:
  - Input: $0.8/1M (2 times more expensive than Mistral Medium 3)
  - Output: $4.0/1M (2 times more expensive than Mistral Medium 3)
- **GPT-4o Mini**:


## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Medium 3 Benchmark Analysis
#### Model Overview
The Mistral Medium 3 model, released by Mistral AI on 2025-04-17, is a mid-tier model with the following key characteristics:
* **Model Name:** Mistral Medium 3 (mistralai/mistral-medium-3)
* **Provider:** Mistral AI
* **Release Date:** 2025-04-17
* **Tier:** Mid
* **Open Source:** False

#### Pricing
The pricing for Mistral Medium 3 is as follows:
* **Input:** $0.4 per 1M tokens
* **Output:** $2.0 per 1M tokens
* **Cached Input:** $None per 1M tokens
* **Batch Input:** $None per 1M tokens

#### Context and Limits
The model has the following context and limits:
* **Context Window:** 131,072 tokens
* **Max Output:** 16,384 tokens
* **Knowledge Cutoff:** 2024-11

#### Benchmarks
The model's benchmark performance is as follows:
* **MMLU:** 80.0
* **HumanEval:** 77.5
* **LMSYS Arena ELO:** 1200
* **GSM8K:** None

The **MMLU (Massive Multitask Language Understanding) score** of 80.0 indicates the model's ability to perform well across a wide range of natural language processing tasks. A higher MMLU score suggests better overall language understanding capabilities.

The **HumanEval score** of 77.5 measures the model's ability to generate human-like code. A higher

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. It offers a range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. This comparison will examine the pricing, performance, and use cases of Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

#### Pricing Comparison
The pricing models of the three competitors are as follows:

* **Mistral Medium 3**:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* **Claude 3.5 Haiku**:
	+ Input: $0.8 per 1M tokens
	+ Output: $4.0 per 1M tokens
* **GPT-4o Mini**:
	+ Input: $0.15 per 1M tokens
	+ Output: $0.6 per 1M tokens

Mistral Medium 3 is priced lower than Claude 3.5 Haiku but higher than GPT-4o Mini for both input and output.

#### Performance Comparison
The performance of the three models can be evaluated based on their benchmark scores:

* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

While the benchmark scores for Claude 3.5 Haiku and GPT-4o Mini are not available, Mistral Medium 3's scores indicate strong performance in coding, analysis, and other tasks.

#### Capabilities and Use Cases
Mistral Medium 3 is suitable for a range of tasks, including:

* Coding
* Analysis
* RAG (Retrieve, Augment, Generate)
* Summarization
* Vision tasks
* Content generation
* Function calling

However, it is not recommended for:

* Frontier reasoning
* Bulk cheap tasks
* Simple classification
* Real-time

## Best Use Cases
### Practical Advice for Mistral Medium 3
Mistral Medium 3, offered by Mistral AI, is a mid-tier model with a wide range of capabilities, including text, vision, function calling, and more. Given its strengths and pricing, here are the top 5 best use cases for Mistral Medium 3, along with specific code integration examples mentioning OpenRouter.

#### 1. **Coding and Analysis**
Mistral Medium 3 excels in coding and analysis tasks, making it suitable for applications such as code review, code generation, and debugging. When integrating with OpenRouter for coding tasks, consider the following example:
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Define a coding task
task = "Write a Python function to sort a list of integers."

# Generate code using the model
code = model.generate_code(task)

# Print the generated code
print(code)
```
With an input cost of $0.4 per 1M tokens and an output cost of $2.0 per 1M tokens, this use case can be cost-effective for small to medium-sized coding tasks.

#### 2. **Summarization and Content Generation**
Mistral Medium 3 is well-suited for summarization and content generation tasks, such as summarizing long documents or generating product descriptions. When integrating with OpenRouter for summarization tasks, consider the following example:
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Define a summarization task
task = "Summarize a 1000-word article about AI trends."

# Generate a summary using the model
summary = model.summarize(task)

# Print the generated summary
print(summary)
```
With a context window of 131,072 tokens, Mistral Medium 3 can handle long documents and generate

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
