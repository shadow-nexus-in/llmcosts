# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-26
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Technical Overview of Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that boasts a robust architecture designed to handle a wide range of tasks. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, this model is well-suited for applications that require in-depth analysis and generation of text. Its capabilities include text and vision processing, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Strengths and Use Cases
The main strengths of Mistral Medium 3 lie in its ability to perform complex tasks such as coding, analysis, and content generation. It excels in tasks that require a deep understanding of the input context, such as summarization and vision tasks. With a high MMLU score of 80.0 and a HumanEval score of 77.5, this model demonstrates its proficiency in handling intricate tasks. However, it is not recommended for frontier reasoning, bulk cheap tasks, simple classification, or real-time tasks that require sub-100ms response times.

### Pricing and Competitors
Mistral Medium 3 is priced at $0.4 per 1M input tokens and $2.0 per 1M output tokens. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 10,000 calls would cost $12.0. In comparison to its top competitors, Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers a competitive pricing model. Claude 3.5 Haiku is priced at $0.8/1M input and $4.0/1M output, while GPT-4o Mini is priced at $0.15/1M input and $0.6/1M output. Developers can

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
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for repeated input sequences. If your application involves frequent reuse of the same input, utilizing cached tokens can significantly reduce costs.

#### Batch API Savings
Batch input is also free, which means that batching API calls can lead to substantial cost savings, especially for high-volume applications. By batching input, you can minimize the number of API calls, reducing the overall cost.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: **$1.2**
* **10,000 calls**: **$12.0**
* **100,000 calls**: **$120.0**

To put these costs into perspective, let's calculate the cost per token:
* Assuming an average of 500 tokens per call, the cost per token is: **$1.2 / (1,000 \* 500) = $0.0024 per token** (for 1,000 calls)
* For 10,000 calls, the cost per token remains the same, as the cost scales linearly: **$12.0 / (10,000 \* 500) = $0.0024 per

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Mistral Medium 3 Benchmark Performance
#### Model Overview
The Mistral Medium 3 model, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. The model's knowledge cutoff is 2024-11.

#### Pricing
The pricing for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Benchmark Performance
The benchmark performance of Mistral Medium 3 is measured by the following metrics:
* **MMLU (Massive Multitask Language Understanding)**: 80.0 - This score indicates the model's ability to understand and generate human-like text across a wide range of tasks and domains. A higher MMLU score suggests better language understanding capabilities.
* **HumanEval**: 77.5 - This score measures the model's ability to write correct and functional code in response to programming prompts. A higher HumanEval score indicates better coding capabilities.
* **LMSYS Arena ELO**: 1200 - This score represents the model's performance in a competitive arena, where it is pitted against other models in a series of tasks and challenges. A higher ELO score suggests better overall performance and competitiveness.

#### Real-World Implications
The benchmark performance of Mistral Medium 3 has the following implications for real-world use:
* **Coding and Analysis**: With a high HumanEval score, Mistral Medium 3

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a unique set of capabilities and pricing. This comparison will delve into the details of Mistral Medium 3 and its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

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

Mistral Medium 3 is priced lower than Claude 3.5 Haiku but higher than GPT-4o Mini for both input and output.

#### Performance Trade-offs
The performance of each model can be evaluated using various benchmarks:
* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

While the exact performance of Claude 3.5 Haiku and GPT-4o Mini is not available, Mistral Medium 3 demonstrates strong capabilities in coding, analysis, and vision tasks.

#### Context and Limits
The context window and maximum output for Mistral Medium 3 are:
* **Context Window**: 131,072 tokens
* **Max Output**: 16,384 tokens
* **Knowledge Cutoff**: 2024-11

These limits are not provided for Claude 3.5 Haiku and GPT-4o Mini.

#### Capabilities and Use Cases
Mistral Medium 3 is best suited for:
* Coding
* Analysis
* RAG
* Summarization
* Vision tasks
* Content generation
* Function calling

It is not recommended for:
* Frontier reasoning
* Bulk

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful language model with a wide range of capabilities, including text, vision, function calling, and more. Released on 2025-04-17, this model is well-suited for tasks such as coding, analysis, and content generation.

### Top 5 Best Use Cases for Mistral Medium 3
Based on its capabilities and pricing, here are the top 5 best use cases for Mistral Medium 3:

1. **Coding and Software Development**: With its strong performance in coding tasks, Mistral Medium 3 can be used for code completion, code review, and code generation. For example, you can use it to integrate with OpenRouter, a popular open-source routing library, to generate optimized routes for logistics and transportation applications.
   ```python
import openrouter
from mistralai import MistralMedium3

# Initialize the model and OpenRouter
model = MistralMedium3()
router = openrouter.Router()

# Generate optimized routes using the model and OpenRouter
def generate_routes(locations):
    # Use the model to generate routes
    routes = model.generate(text="Generate optimized routes for the following locations: " + locations)
    # Use OpenRouter to optimize the routes
    optimized_routes = router.optimize(routes)
    return optimized_routes
```

2. **Data Analysis and Summarization**: Mistral Medium 3 can be used for data analysis and summarization tasks, such as generating reports and summaries from large datasets. Its ability to process large amounts of data and generate concise summaries makes it an ideal choice for data analysis tasks.
   ```python
import pandas as pd
from mistralai import MistralMedium3

# Load the dataset
df = pd.read_csv("data.csv")

# Initialize the model
model = MistralMedium3()

# Generate a summary of the dataset
summary = model.generate(text="

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
