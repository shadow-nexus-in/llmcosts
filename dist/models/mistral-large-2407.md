# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-19
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source language model designed to cater to a wide range of applications, particularly in coding, analysis, and function calling. With a context window of 131,072 tokens and a maximum output of 4,096 tokens, this model is well-suited for tasks that require extensive contextual understanding and generation capabilities. Its architecture supports various capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Strengths and Use Cases
The technical strengths of Mistral Large 2 are reflected in its benchmark scores: MMLU at 84.0, HumanEval at 92.0, LMSYS Arena ELO at 1225, and GSM8K at 93.0. These scores indicate the model's high performance in various tasks, especially those involving coding and problem-solving. Its primary use cases include coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual applications, and function calling. However, it is not recommended for tasks that require embeddings, bulk cheap processing, real-time responses under 100ms, or vision-heavy applications.

### Pricing and Cost Considerations
The pricing model for Mistral Large 2 is based on input and output tokens, with costs of $3.0 per 1M input tokens and $9.0 per 1M output tokens. There are no specified costs for cached input or batch input. For example, 1,000 calls with an average of 500 tokens would cost $6.0, while 10,000 calls would cost $60.0, and 100,000 calls would cost $600.0. In comparison to its top competitor, GPT-4o, which charges $2.5/1M input

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $3.0 |
| Output | $9.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Mistral Large 2 Pricing Analysis
#### Overview
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. The pricing structure is based on input and output tokens, with specific considerations for cached and batched inputs.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
- **Input**: $3.0 per 1M tokens
- **Output**: $9.0 per 1M tokens
- **Cached Input**: $0 per 1M tokens (free)
- **Batch Input**: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs when the same input is processed multiple times. Since cached input is free, it is recommended to use cached tokens whenever possible, especially in applications where the same input is repeated.

#### Batch API Savings
Batching API calls can also help reduce costs. Although the pricing data does not provide a specific discount for batched inputs, the fact that batch input is listed as $0 per 1M tokens suggests that batching may be free or discounted. However, the exact savings from batching are not clear from the provided data.

#### Cost at Scale
The cost of using Mistral Large 2 at scale can be estimated based on the provided cost examples:
- **1,000 calls (avg 500 tokens)**: $6.0
- **10,000 calls**: $60.0
- **100,000 calls**: $600.0

These examples suggest a linear scaling of costs with the number of API calls. To estimate the cost of using Mistral Large 2 for a specific use case, you can calculate the total number of tokens required and multiply it by the input and output costs.

#### Comparison to Top Compet

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 84.0 |
| HumanEval | 92.0 |
| LMSYS Arena ELO | 1225 |
| ARC | 93.0 |

## Benchmark Analysis
### Mistral Large 2 Benchmark Performance Analysis
#### Model Overview
The Mistral Large 2 model, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. It is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens.

#### Benchmark Scores
The model's performance is measured by the following benchmark scores:
* **MMLU (Massive Multitask Language Understanding)**: 84.0, indicating the model's ability to understand and process natural language across a wide range of tasks.
* **HumanEval**: 92.0, measuring the model's ability to evaluate and execute human-written code, with higher scores indicating better performance.
* **LMSYS Arena ELO**: 1225, representing the model's competitive ranking in the LMSYS Arena, a platform for evaluating language models. A higher ELO score indicates better performance.
* **GSM8K**: 93.0, measuring the model's performance on the GSM8K dataset, which focuses on math problem-solving.

#### Real-World Implications
These benchmark scores have significant implications for real-world use cases:
* The high **HumanEval** score (92.0) suggests that Mistral Large 2 is well-suited for coding and programming tasks, making it a strong choice for applications that require code evaluation and execution.
* The **MMLU** score (84.0) indicates that the model has a good understanding of natural language, which is beneficial for tasks like text analysis, rag, and multilingual applications.
* The **LMSYS Arena ELO** score (1225) demonstrates the model

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. This comparison will focus on its pricing, performance, and capabilities relative to its top competitors, specifically GPT-4o.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, whereas GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. This indicates that GPT-4o is cheaper for input tokens but more expensive for output tokens compared to Mistral Large 2.

#### Performance Trade-offs
Mistral Large 2 has the following benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

In contrast, the benchmark scores for GPT-4o are not provided in the given data. However, considering the general performance of models in the same tier, Mistral Large 2 seems to offer competitive performance, especially in coding and analysis tasks.

#### Capabilities and Use Cases
Mistral Large 2 supports the following capabilities:
- text
- vision
- function_calling
- json_mode
- streaming
- system_prompts

It is best suited for tasks such as:
- coding
- analysis
- rag
- agents
- multilingual
- function_calling

On the other hand, it is not recommended for:
- embeddings
- bulk_cheap
- real_time_sub_100ms
- vision_heavy

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100,000 calls: $600.0

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model that offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. With its high performance benchmarks (MMLU: 84.0, HumanEval: 92.0, LMSYS Arena ELO: 1225, GSM8K: 93.0), it is best suited for tasks such as coding, analysis, RAG, agents, multilingual, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
1. **Coding and Software Development**: Given its high HumanEval score (92.0), Mistral Large 2 is ideal for coding tasks, such as code completion, code review, and bug fixing. For example, you can integrate it with OpenRouter to generate code snippets based on user input:
    ```python
import openrouter

# Initialize Mistral Large 2 model
model = openrouter.Model("mistralai/mistral-large-2407")

# Define a function to generate code snippets
def generate_code(prompt):
    response = model.generate(prompt)
    return response

# Test the function
print(generate_code("Write a Python function to sort a list of integers"))
```
2. **Data Analysis and Insights**: With its high MMLU score (84.0), Mistral Large 2 can be used for data analysis tasks, such as data summarization, data visualization, and data mining. You can use it to analyze large datasets and provide insights to users:
    ```python
import pandas as pd
import openrouter

# Load a sample dataset
df = pd.read_csv("data.csv")

# Initialize Mistral Large 2 model
model = openrouter.Model("mistralai/mistral-large-2407")

#

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
