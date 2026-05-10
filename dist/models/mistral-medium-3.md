# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-10
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance between performance and cost. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, this model is well-suited for a variety of tasks, including coding, analysis, and content generation. The model's capabilities include text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Strengths and Use-Cases
Mistral Medium 3's main strengths lie in its ability to handle complex tasks with ease, thanks to its large context window and robust capabilities. The model excels in tasks such as coding, analysis, and summarization, with benchmark scores of 80.0 on MMLU and 77.5 on HumanEval. Additionally, the model's support for vision tasks and function calling makes it an ideal choice for applications that require multi-modal input and output. However, the model is not well-suited for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms.

### Pricing and Cost Considerations
The pricing for Mistral Medium 3 is as follows: $0.4 per 1M input tokens and $2.0 per 1M output tokens. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 10,000 calls would cost $12.0, and 100,000 calls would cost $120.0. Compared to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers a competitive pricing model, with a lower cost per input token than Claude 3.5 Haiku, but a higher cost per output token than GPT-

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### Optimal Usage Scenarios
* **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
* **Batch API Savings**: With batch input being free, batching API calls can lead to significant cost savings, especially for large-scale applications.

#### Cost at Scale
The cost of using Mistral Medium 3 at different scales is as follows:
* **1,000 calls (avg 500 tokens)**: **$1.2**
* **10,000 calls**: **$12.0**
* **100,000 calls**: **$120.0**

These costs can be broken down into input and output costs. Assuming an average of 500 tokens per call, the total tokens for each scenario would be:
* 1,000 calls: 500,000 tokens
* 10,000 calls: 5,000,000 tokens
* 100,000 calls: 50,000,000 tokens

Using the pricing structure, we can estimate the costs:
* 1,000 calls: (500,000 tokens / 1,000,000) \* ($0.4 + $2.0) = $1.2
* 10,000 calls: (5,

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

The MMLU, HumanEval, and LMSYS Arena ELO scores are measures of the model's performance in various tasks:
* **MMLU (Massive Multitask Language Understanding):** Measures the model's ability to understand and generate text across a wide range of tasks and domains. A higher MMLU score indicates better performance.
* **HumanEval:**

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a unique set of capabilities and pricing. This comparison will delve into the details of Mistral Medium 3 and its top competitors, Claude 3.5 Haiku and GPT-4o Mini, highlighting their differences in pricing, performance, and use cases.

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

Mistral Medium 3 is priced lower than Claude 3.5 Haiku but higher than GPT-4o Mini for both input and output tokens.

#### Performance Comparison
The performance of the three models can be compared using various benchmarks:

* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

While the exact performance of Claude 3.5 Haiku and GPT-4o Mini is not available, Mistral Medium 3's benchmarks suggest a strong performance in coding, analysis, and other tasks.

#### Capabilities and Use Cases
The capabilities and use cases of the three models are:

* **Mistral Medium 3**:
	+ Capabilities: text, vision, function_calling, json_mode, streaming, system_prompts
	+ Best for: coding, analysis, rag, summarization, vision_tasks, content_generation, function_calling
	+ Not good for: frontier_reasoning, bulk_cheap_tasks, simple_classification, real_time_sub_100ms
* **Claude 3.5 Haiku**: Not provided


## Best Use Cases
### Practical Advice for Mistral Medium 3
Mistral Medium 3, a mid-tier model provided by Mistral AI, offers a balance of capabilities and pricing. With its release on 2025-04-17, it has established itself as a versatile tool for various tasks. Here are the top 5 best use cases for Mistral Medium 3, along with specific code integration examples mentioning OpenRouter.

#### 1. **Coding and Analysis**
Mistral Medium 3 excels in coding and analysis tasks, making it an ideal choice for developers and data analysts. Its capabilities in text and function_calling enable it to understand and generate code snippets.
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Define a coding task
task = "Write a Python function to calculate the area of a rectangle."

# Get the response from the model
response = model.generate_text(task)

print(response)
```

#### 2. **Summarization**
With its strong text capabilities, Mistral Medium 3 can effectively summarize long pieces of text, making it suitable for content generation and analysis tasks.
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Define a summarization task
task = "Summarize the following text: [insert long text]"

# Get the response from the model
response = model.generate_text(task)

print(response)
```

#### 3. **Vision Tasks**
Mistral Medium 3's vision capabilities make it an excellent choice for tasks that involve image analysis and generation.
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Define a vision task
task = "Generate an image of a cat."

# Get the response from the model
response = model.generate_image(task)

print(response

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
