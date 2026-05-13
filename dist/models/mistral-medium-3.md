# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-13
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier language model with a robust architecture designed to handle a wide range of tasks. This model is not open source, indicating that its internal workings and training data are proprietary. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, Mistral Medium 3 is capable of processing and generating substantial amounts of text. Its knowledge cutoff is 2024-11, meaning it has been trained on data up to that point.

### Technical Capabilities and Pricing
Mistral Medium 3 boasts an impressive array of capabilities, including text and vision processing, function calling, JSON mode, streaming, and system prompts. It is best suited for tasks such as coding, analysis, RAG (Retrieve, Augment, Generate), summarization, vision tasks, content generation, and function calling. However, it is not recommended for frontier reasoning, bulk cheap tasks, simple classification, or real-time applications requiring responses under 100ms. The pricing model for Mistral Medium 3 is as follows: $0.4 per 1M input tokens and $2.0 per 1M output tokens. There are no specific rates provided for cached input or batch input. For example, 1,000 calls averaging 500 tokens each would cost $1.2, scaling up to $120.0 for 100,000 calls.

### Performance and Competitors
Mistral Medium 3 has been benchmarked on several metrics, achieving scores of 80.0 on MMLU, 77.5 on HumanEval, and 1200 on LMSYS Arena ELO. While its performance on GSM8K is not provided, these benchmarks indicate a strong performance across various tasks. In comparison to its competitors, such as Claude 3.5 Haiku and GPT

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
Mistral Medium 3 is a mid-tier model provided by Mistral AI, released on 2025-04-17. This analysis will break down the cost structure, provide guidance on when to use cached tokens, discuss batch API savings, and examine the cost at scale for 1k, 10k, and 100k API calls.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### Using Cached Tokens
Given that cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs. This can be particularly effective for applications with repetitive or similar input sequences.

#### Batch API Savings
Although the batch input is listed as free, the actual cost savings will depend on the specific use case and the number of tokens processed. However, based on the provided pricing, there are no additional discounts for batch processing. The primary cost factor will be the output tokens.

#### Cost at Scale
To illustrate the cost at scale, let's examine the provided cost examples:
* 1,000 calls (avg 500 tokens): **$1.2**
* 10,000 calls: **$12.0**
* 100,000 calls: **$120.0**

These examples suggest a linear cost scaling, which is consistent with the input and output token pricing.

#### Comparison to Top Competitors
Mistral Medium 3's pricing can be compared to its top competitors:
* Claude 3.5 Haiku: **$0.8/1M input**, **$4.0/1M output**
* GPT-4

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
The Mistral Medium 3 model, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. The model's knowledge cutoff is 2024-11.

#### Pricing
The pricing for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Benchmark Performance
The model's benchmark performance is measured by the following scores:
* **MMLU (Massive Multitask Language Understanding)**: 80.0 - This score indicates the model's ability to understand and perform a wide range of natural language processing tasks. A higher score suggests better performance.
* **HumanEval**: 77.5 - This score evaluates the model's ability to generate human-like text based on a given prompt. A higher score indicates more coherent and relevant output.
* **LMSYS Arena ELO**: 1200 - This score measures the model's performance in a competitive environment, where it is pitted against other models. A higher score indicates better performance and a higher ranking.

#### Real-World Implications
The benchmark scores suggest that Mistral Medium 3 is a capable model for a variety of tasks, including:
* Coding: The model's high MMLU score indicates that it can understand and generate code effectively.
* Analysis: The model's high HumanEval score suggests that it can provide

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will examine the pricing, performance, and capabilities of Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

#### Pricing Comparison
The pricing models for each competitor are as follows:
* **Mistral Medium 3**:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* **Claude 3.5 Haiku**:
	+ Input: $0.8 per 1M tokens (100% higher than Mistral Medium 3)
	+ Output: $4.0 per 1M tokens (100% higher than Mistral Medium 3)
* **GPT-4o Mini**:
	+ Input: $0.15 per 1M tokens (62.5% lower than Mistral Medium 3)
	+ Output: $0.6 per 1M tokens (70% lower than Mistral Medium 3)

#### Performance Comparison
The performance benchmarks for each model are:
* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

Note that the performance benchmarks for Claude 3.5 Haiku and GPT-4o Mini are not available, making it difficult to directly compare their performance with Mistral Medium 3.

#### Capabilities and Use Cases
Mistral Medium 3 supports the following capabilities:
* Text
* Vision
* Function calling
* JSON mode
* Streaming
* System prompts

It is best suited for tasks such as:
* Coding
* Analysis
* RAG
* Summarization
* Vision tasks
* Content generation
* Function calling

However, it is not recommended for:
* Frontier reasoning
* Bulk cheap tasks
* Simple classification
* Real-time sub-100ms tasks

#### Cost

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. With its capabilities in text, vision, function calling, JSON mode, streaming, and system prompts, it is best suited for tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling.

### Top 5 Best Use Cases for Mistral Medium 3
Based on its capabilities and benchmarks, here are the top 5 best use cases for Mistral Medium 3:

1. **Coding and Software Development**: With its high scores in HumanEval (77.5) and MMLU (80.0), Mistral Medium 3 is well-suited for coding tasks such as code completion, code review, and bug fixing. It can be integrated with OpenRouter to provide real-time code suggestions and improvements.
   ```python
import openrouter
from mistralai import MistralMedium3

# Initialize the model and OpenRouter
model = MistralMedium3()
router = openrouter.OpenRouter()

# Define a function to generate code
def generate_code(prompt):
    input_ids = model.encode(prompt)
    output_ids = model.generate(input_ids)
    code = model.decode(output_ids)
    return code

# Use OpenRouter to provide real-time code suggestions
def suggest_code(prompt):
    code = generate_code(prompt)
    suggestions = router.suggest(code)
    return suggestions
```

2. **Data Analysis and Summarization**: Mistral Medium 3's capabilities in text analysis and summarization make it an excellent choice for tasks such as data analysis, report generation, and document summarization.
   ```python
import pandas as pd
from mistralai import MistralMedium3

# Load a dataset
df = pd.read

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
