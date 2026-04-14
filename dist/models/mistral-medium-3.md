# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-14
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance between performance and cost. As a non-open source model, it is designed to provide reliable and efficient processing for various tasks. The architecture of Mistral Medium 3 is not explicitly stated, but its capabilities suggest a robust and versatile design. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, this model is well-suited for tasks that require significant input and output processing.

### Strengths and Use-Cases
The main strengths of Mistral Medium 3 lie in its ability to handle complex tasks such as coding, analysis, and vision tasks. Its capabilities include text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile model for a wide range of applications. The model's performance is reflected in its benchmark scores, with an MMLU score of 80.0, HumanEval score of 77.5, and LMSYS Arena ELO score of 1200. Mistral Medium 3 is best suited for tasks that require in-depth analysis, summarization, and content generation. However, it may not be the best choice for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time processing under 100ms.

### Pricing and Cost Examples
The pricing for Mistral Medium 3 is as follows: $0.4 per 1M input tokens and $2.0 per 1M output tokens. In comparison to its top competitors, Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers a competitive pricing model. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 10,000 calls would cost $12.0, and 

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.4 |
| Output | $2.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Mistral Medium 3 Pricing Analysis
#### Overview
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### Optimal Usage Scenarios
* **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
* **Batch API**: With batch input being free, batching API calls can lead to significant savings, especially for large-scale applications.

#### Cost at Scale
The cost examples provided are as follows:
* **1,000 calls (avg 500 tokens)**: **$1.2**
* **10,000 calls**: **$12.0**
* **100,000 calls**: **$120.0**

To estimate the cost at scale, we can calculate the cost per call:
* Assuming an average of 500 tokens per call, the total tokens per 1,000 calls would be 500,000 tokens.
* Using the input and output pricing, the estimated cost per 1,000 calls would be:
	+ Input: 500,000 tokens / 1,000,000 tokens * $0.4 = $0.2
	+ Output: assuming an average output of 100 tokens per call (conservative estimate), the total output tokens per 1,000 calls would be 100,000 tokens. The estimated output cost would be: 100,000 tokens / 1,000,000

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Medium 3 Benchmark Performance Analysis
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

The **MMLU (Massive Multitask Language Understanding)** score of 80.0 indicates the model's ability to perform well across a wide range of natural language processing tasks. A higher MMLU score suggests better overall language understanding.

The **HumanEval** score of 77.5 measures the model's ability to generate code that is correct and functional.

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a unique set of capabilities and pricing. This comparison will delve into the details of Mistral Medium 3 versus its top competitors, Claude 3.5 Haiku and GPT-4o Mini, highlighting price differences, performance trade-offs, and use cases for each model.

#### Pricing Comparison
The pricing for each model is as follows:
* Mistral Medium 3:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* Claude 3.5 Haiku:
	+ Input: $0.8 per 1M tokens
	+ Output: $4.0 per 1M tokens
* GPT-4o Mini:
	+ Input: $0.15 per 1M tokens
	+ Output: $0.6 per 1M tokens

Mistral Medium 3 offers a balanced pricing approach, sitting between the more expensive Claude 3.5 Haiku and the cheaper GPT-4o Mini.

#### Performance Trade-offs
The performance of each model can be evaluated using various benchmarks:
* Mistral Medium 3:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* Claude 3.5 Haiku and GPT-4o Mini's benchmark scores are not provided for direct comparison.

However, based on the capabilities and pricing, we can infer the following:
* Mistral Medium 3 is suitable for tasks that require a balance between performance and cost, such as coding, analysis, and content generation.
* Claude 3.5 Haiku may be more suitable for tasks that require high-performance and are less sensitive to cost, such as complex vision tasks or high-stakes decision-making.
* GPT-4o Mini may be more suitable for tasks that require low-cost and high-volume processing, such as bulk data processing or simple classification tasks.

#### Context and Limits
The context window and output limits for Mistral Medium 3 are:
* Context Window: 131,072 tokens
* Max Output: 16,384 tokens
* Knowledge Cutoff: 2024-11

These limits are

## Best Use Cases
### Practical Advice for Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. Given its capabilities and limitations, here are the top 5 best use cases for Mistral Medium 3, along with specific code integration examples mentioning OpenRouter:

#### 1. **Coding and Analysis**
Mistral Medium 3 excels in coding and analysis tasks, making it an ideal choice for applications such as code review and debugging. When integrated with OpenRouter, you can leverage Mistral Medium 3's capabilities to analyze code snippets and provide insightful feedback.
```python
import openrouter
from mistralai import MistralMedium3

# Initialize Mistral Medium 3 model
model = MistralMedium3()

# Define a code snippet for analysis
code_snippet = """
def add(a, b):
    return a + b
"""

# Use OpenRouter to send the code snippet to Mistral Medium 3
response = openrouter.send_code(code_snippet, model)

# Print the analysis results
print(response)
```

#### 2. **Summarization and Content Generation**
With its strong text generation capabilities, Mistral Medium 3 is well-suited for tasks such as summarization and content generation. You can use OpenRouter to integrate Mistral Medium 3 into your application and generate high-quality summaries or content.
```python
import openrouter
from mistralai import MistralMedium3

# Initialize Mistral Medium 3 model
model = MistralMedium3()

# Define a text prompt for summarization
prompt = """
This is a sample text prompt for summarization.
"""

# Use OpenRouter to send the prompt to Mistral Medium 3
response = openrouter.send_prompt(prompt, model)

# Print the generated summary
print(response)


## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
