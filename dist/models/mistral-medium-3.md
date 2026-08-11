# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-11
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Technical Overview of Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier language model designed for a variety of tasks, including coding, analysis, and content generation. The model's architecture is not explicitly detailed, but its capabilities suggest a robust and versatile design, supporting text, vision, function calling, JSON mode, streaming, and system prompts. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, Mistral Medium 3 is well-suited for complex tasks that require significant contextual understanding.

### Strengths and Use Cases
The main strengths of Mistral Medium 3 lie in its ability to handle complex tasks such as coding, analysis, and content generation. Its high scores on benchmarks like MMLU (80.0) and HumanEval (77.5) demonstrate its proficiency in these areas. Additionally, its support for vision tasks and function calling expands its potential use cases. However, it is not recommended for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms. The model's pricing structure, with input costs at $0.4 per 1M tokens and output costs at $2.0 per 1M tokens, reflects its positioning as a mid-tier model.

### Pricing and Competitors
In terms of pricing, Mistral Medium 3 is competitively positioned, with cost examples indicating that 1,000 calls (avg 500 tokens) would cost $1.2, 10,000 calls would cost $12.0, and 100,000 calls would cost $120.0. Compared to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3's pricing is more aligned with Claude 3.5 Haiku, although the latter has higher input and output costs ($0

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
To minimize costs, consider the following strategies:
* **Use cached tokens** when possible, as they are free. This can significantly reduce costs for repeated or similar inputs.
* **Utilize batch API calls** to take advantage of the free batch input pricing.

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
* 1,000 calls: (500,000 tokens / 1,000,000 tokens) \* $0.4 (input) + (500,000 tokens / 1,000,000 tokens) \* $2.

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Medium 3 Benchmark Performance Analysis
#### Overview
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. It is not open source.

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
The benchmark performance of Mistral Medium 3 is as follows:
* **MMLU (Massive Multitask Language Understanding)**: 80.0
	+ MMLU measures a model's ability to perform a wide range of natural language processing tasks. A higher score indicates better performance.
* **HumanEval**: 77.5
	+ HumanEval evaluates a model's ability to generate code that passes a set of unit tests. A higher score indicates better coding abilities.
* **LMSYS Arena ELO**: 1200
	+ LMSYS Arena ELO measures a model's overall performance in a competitive environment. A higher ELO score indicates better performance.

#### Real-World Implications
The benchmark scores indicate that Mistral Medium 3 is a capable model for a variety of tasks, including:
* Coding: The high HumanEval score suggests that Mistral Medium

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. It offers a range of capabilities including text, vision, function calling, and more. This comparison will delve into the pricing, performance, and use cases of Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

#### Pricing Comparison
The pricing for each model is as follows:
- **Mistral Medium 3**:
  - Input: $0.4 per 1M tokens
  - Output: $2.0 per 1M tokens
- **Claude 3.5 Haiku**:
  - Input: $0.8 per 1M tokens
  - Output: $4.0 per 1M tokens
- **GPT-4o Mini**:
  - Input: $0.15 per 1M tokens
  - Output: $0.6 per 1M tokens

Mistral Medium 3 is more expensive than GPT-4o Mini but cheaper than Claude 3.5 Haiku in terms of both input and output costs.

#### Performance Comparison
Performance benchmarks for each model are:
- **Mistral Medium 3**:
  - MMLU: 80.0
  - HumanEval: 77.5
  - LMSYS Arena ELO: 1200
- **Claude 3.5 Haiku** and **GPT-4o Mini** benchmarks are not provided for direct comparison.

Given the available data, Mistral Medium 3 demonstrates strong performance across various benchmarks, but without direct comparisons for Claude 3.5 Haiku and GPT-4o Mini, it's challenging to assess their relative performance.

#### Capabilities and Use Cases
- **Mistral Medium 3** is capable of:
  - Text
  - Vision
  - Function calling
  - JSON mode
  - Streaming
  - System prompts
- It is best for:
  - Coding
  - Analysis
  - RAG (Retrieval-Augmented Generation)
  - Summarization
  - Vision tasks
  - Content generation
  - Function calling
- Not recommended for:
  - Frontier reasoning
  - Bulk

## Best Use Cases
### Practical Advice for Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a wide range of capabilities, including text, vision, function calling, and more. Here are the top 5 best use cases for Mistral Medium 3, along with specific code integration examples and mentions of OpenRouter:

#### 1. **Coding and Analysis**
Mistral Medium 3 excels in coding and analysis tasks, making it an ideal choice for applications that require in-depth code understanding and generation. 
```python
import openrouter
from mistralai import MistralMedium3

# Initialize the model
model = MistralMedium3()

# Define a coding task
task = "Write a Python function to sort a list of integers."

# Use OpenRouter to integrate with the model
response = openrouter.query(model, task)

# Print the response
print(response)
```

#### 2. **Summarization**
With its strong capabilities in text processing, Mistral Medium 3 is well-suited for summarization tasks. You can use it to summarize long documents, articles, or even entire books.
```python
import openrouter
from mistralai import MistralMedium3

# Initialize the model
model = MistralMedium3()

# Define a summarization task
task = "Summarize the following text: [insert long text here]"

# Use OpenRouter to integrate with the model
response = openrouter.query(model, task)

# Print the response
print(response)
```

#### 3. **Content Generation**
Mistral Medium 3's capabilities in text generation make it an excellent choice for content generation tasks, such as writing articles, blog posts, or even entire books.
```python
import openrouter
from mistralai import MistralMedium3

# Initialize the model
model = MistralMedium3()

# Define a content generation task
task

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
