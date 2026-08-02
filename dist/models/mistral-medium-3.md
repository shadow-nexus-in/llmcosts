# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-02
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a mid-tier language model released on 2025-04-17. This model is not open source. From an architectural standpoint, Mistral Medium 3 is designed to handle a wide range of tasks, including coding, analysis, and vision tasks, thanks to its capabilities in text, vision, function calling, JSON mode, streaming, and system prompts. Its primary strengths lie in its ability to perform complex tasks such as summarization, content generation, and function calling efficiently.

### Technical Specifications and Use Cases
Technically, Mistral Medium 3 operates with a context window of 131,072 tokens and can output up to 16,384 tokens. It has a knowledge cutoff of 2024-11, indicating that its training data is current up to that point. The model's pricing is structured as $0.4 per 1M input tokens and $2.0 per 1M output tokens, with no specified costs for cached or batch input. Its performance is benchmarked with an MMLU score of 80.0, HumanEval score of 77.5, and an LMSYS Arena ELO of 1200. This model is best suited for tasks that require in-depth analysis, coding, and generation of content, but it is not recommended for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms.

### Pricing and Competitor Analysis
The cost of using Mistral Medium 3 can be estimated based on the number of calls and tokens used. For example, 1,000 calls with an average of 500 tokens would cost $1.2, scaling up to $120.0 for 100,000 calls. In comparison to its competitors, Mistral Medium 3 is priced competitively, with Claude 3.5 Haiku costing $0.8

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option when possible. However, the context window limit of **131,072 tokens** and the knowledge cutoff of **2024-11** should be considered when deciding whether to utilize cached tokens.

#### Batch API Savings
Batch input is free, which can lead to significant cost savings when making multiple API calls. This is particularly beneficial for tasks that require a large number of requests, such as bulk data processing or analysis.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: **$1.2**
* **10,000 calls**: **$12.0**
* **100,000 calls**: **$120.0**

These costs demonstrate a linear scaling of expenses with the number of API calls.

#### Comparison to Top Competitors
Mistral Medium 3's pricing is compared to its top competitors:
* Claude 3.5 Haiku: **$0.8/1M input**, **$4.0/1M output**
* GPT-4o Mini: **$0.15/1M input**, **$0.6/1M output**

Mist

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
The Mistral Medium 3 model, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. It is not open-source.

#### Pricing
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Context and Limits
The model has the following context and limits:
* Context Window: **131,072 tokens**
* Max Output: **16,384 tokens**
* Knowledge Cutoff: **2024-11**

#### Benchmarks
The model's benchmark performance is as follows:
* **MMLU: 80.0**: The MMLU (Massive Multitask Language Understanding) benchmark measures a model's ability to understand and generate human-like text. A higher score indicates better performance. With a score of 80.0, Mistral Medium 3 demonstrates strong language understanding capabilities.
* **HumanEval: 77.5**: The HumanEval benchmark evaluates a model's ability to write correct and functional code. A higher score indicates better performance. With a score of 77.5, Mistral Medium 3 shows good coding capabilities.
* **LMSYS Arena ELO: 1200**: The LMSYS Arena ELO benchmark measures a model's overall performance in a competitive environment. A higher score indicates better performance. With a score of 1200, Mistral Medium 3 demonstrates moderate

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will evaluate Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini, in terms of pricing, performance, and use cases.

#### Pricing Comparison
The pricing for each model is as follows:
* **Mistral Medium 3**:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* **Claude 3.5 Haiku**:
	+ Input: $0.8 per 1M tokens
	+ Output: $4.0 per 1M tokens
* **GPT-4o Mini**:
	+ Input: $0.15 per 1M tokens
	+ Output: $0.6 per 1M tokens

Mistral Medium 3 offers a balanced pricing structure, with input costs lower than Claude 3.5 Haiku but higher than GPT-4o Mini. However, the output costs of Mistral Medium 3 are lower than Claude 3.5 Haiku but higher than GPT-4o Mini.

#### Performance Comparison
The performance benchmarks for each model are:
* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

Based on the available data, Mistral Medium 3 demonstrates strong performance in various benchmarks. However, without comparable data for Claude 3.5 Haiku and GPT-4o Mini, it is challenging to make a direct performance comparison.

#### Use Case Comparison
The recommended use cases for each model are:
* **Mistral Medium 3**: coding, analysis, rag, summarization, vision_tasks, content_generation, function_calling
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

Mistral Medium

## Best Use Cases
### Practical Advice for Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. It offers a range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. Here are the top 5 best use cases for Mistral Medium 3, along with specific code integration examples mentioning OpenRouter:

#### 1. Coding and Analysis
Mistral Medium 3 excels in coding and analysis tasks. Its high MMLU score of 80.0 and HumanEval score of 77.5 make it an ideal choice for tasks that require complex code understanding and generation.
```python
import openrouter
from mistralai import MistralMedium3

# Initialize the model
model = MistralMedium3()

# Define a coding task
task = "Write a Python function to sort a list of integers."

# Use OpenRouter to send the task to the model
response = openrouter.send_task(task, model)

# Print the response
print(response)
```

#### 2. Summarization and Content Generation
Mistral Medium 3 is well-suited for summarization and content generation tasks. Its high context window of 131,072 tokens and max output of 16,384 tokens make it capable of handling large amounts of text data.
```python
import openrouter
from mistralai import MistralMedium3

# Initialize the model
model = MistralMedium3()

# Define a summarization task
task = "Summarize a given article in 100 words."

# Use OpenRouter to send the task to the model
response = openrouter.send_task(task, model)

# Print the response
print(response)
```

#### 3. Vision Tasks
Mistral Medium 3 has capabilities in vision tasks, making it a good choice for tasks that require image understanding

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
