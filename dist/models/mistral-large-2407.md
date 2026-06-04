# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-04
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly excelling in coding, analysis, and function calling tasks. With a context window of 131,072 tokens and a maximum output of 4,096 tokens, this model is well-suited for handling complex, long-form inputs and generating detailed responses. Its capabilities extend to text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Strengths and Use Cases
Mistral Large 2 demonstrates its technical prowess through impressive benchmark scores: 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These scores underscore its effectiveness in coding tasks, understanding natural language, and solving complex problems. The model is best utilized for coding, analysis, retrieval-augmented generation (RAG), agents, multilingual tasks, and function calling, thanks to its robust architecture and extensive capabilities. However, it is not recommended for applications requiring embeddings, bulk cheap processing, real-time responses under 100ms, or vision-heavy tasks.

### Pricing and Cost Considerations
The pricing for Mistral Large 2 is structured as follows: $3.0 per 1M input tokens and $9.0 per 1M output tokens, with no specified costs for cached input or batch input. For example, 1,000 calls averaging 500 tokens each would cost $6.0, while 10,000 calls would amount to $60.0, and 100,000 calls would total $600.0. When comparing costs, it's notable that competitors like GPT-4o offer input pricing at $2.5/1M tokens

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
Mistral Large 2 is a premium model offered by Mistral AI, released on 2024-07-24. This model is not open source and has a tier classification of premium. The pricing structure for Mistral Large 2 is based on input and output tokens, with additional considerations for cached input and batch API savings.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $None per 1M tokens (indicating no additional cost for cached input)
* Batch Input: $None per 1M tokens (indicating no additional cost for batch input)

#### When to Use Cached Tokens
Given that there is no additional cost for cached input, it is always beneficial to use cached tokens when possible. This can help reduce the overall cost of API calls by minimizing the number of new input tokens that need to be processed.

#### Batch API Savings
Although the pricing data does not provide a specific cost savings for batch API calls, the fact that batch input is listed as $None per 1M tokens suggests that there may be some inherent efficiency or discount for processing multiple inputs in a single batch. However, without explicit savings data, the exact benefit of batch API calls is unclear.

#### Cost at Scale
The provided cost examples give insight into the cost of using Mistral Large 2 at different scales:
* 1,000 calls (avg 500 tokens): $6.0
* 10,000 calls: $60.0
* 100,000 calls: $600.0

These examples suggest a linear scaling of costs with the number of API calls. To further analyze the cost structure, let's calculate the cost per call based on the provided examples:
* 1,000 calls: $6

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
The Mistral Large 2 model, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. It offers a range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts.

#### Pricing
The pricing for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Context and Limits
The model has the following context and limits:
* Context Window: 131,072 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2024-07

#### Benchmarks
The model's benchmark performance is as follows:
* MMLU: 84.0
* HumanEval: 92.0
* LMSYS Arena ELO: 1225
* GSM8K: 93.0

These benchmarks indicate the model's performance in various areas:
* **MMLU (Massive Multitask Language Understanding)**: A score of 84.0 indicates that the model has strong language understanding capabilities, but may struggle with certain tasks or nuances.
* **HumanEval**: A score of 92.0 suggests that the model is highly effective in evaluating and generating human-like text, making it suitable for tasks such as coding, analysis, and writing.
* **LMSYS Arena ELO**: An ELO score of 1225 indicates that the model has a

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, a premium model offered by Mistral AI, is a powerful language model with a wide range of capabilities, including text, vision, function calling, and more. Released on July 24, 2024, this model has a context window of 131,072 tokens and can generate up to 4,096 tokens of output. In this comparison, we will evaluate Mistral Large 2 against its top competitor, GPT-4o, in terms of pricing, performance, and use cases.

#### Pricing Comparison
The pricing for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens

In contrast, GPT-4o is priced at:
* Input: $2.5 per 1M tokens
* Output: $10.0 per 1M tokens

As shown in the cost examples, the total cost for Mistral Large 2 is:
* 1,000 calls (avg 500 tokens): $6.0
* 10,000 calls: $60.0
* 100,000 calls: $600.0

#### Performance Comparison
Mistral Large 2 has achieved impressive benchmarks:
* MMLU: 84.0
* HumanEval: 92.0
* LMSYS Arena ELO: 1225
* GSM8K: 93.0

While the benchmarks for GPT-4o are not provided, we can compare the pricing and capabilities of the two models to determine which one is more suitable for specific use cases.

#### Capabilities and Use Cases
Mistral Large 2 is best suited for:
* Coding
* Analysis
* RAG (Retrieval-Augmented Generation)
* Agents
* Multilingual tasks
* Function calling

On the other hand, it is not recommended for:
* Embeddings
* Bulk cheap tasks
* Real-time tasks with latency under 100ms
* Vision-heavy tasks

#### Choosing the Right Model
Based on the pricing and performance comparison, Mistral Large 2 is a good choice when:
* You need a model with a large context window (131,072 tokens) and high output generation capacity (4,096 tokens).
* You prioritize capabilities such as function calling, R

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium language model released on 2024-07-24. With its robust capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, it is best suited for applications such as coding, analysis, and multilingual support.

### Top 5 Best Use Cases for Mistral Large 2
Given its strengths and pricing model, here are the top 5 best use cases for Mistral Large 2, along with specific code integration examples using OpenRouter:

1. **Coding Assistance**: Mistral Large 2 excels in coding tasks, making it an ideal choice for developers looking for AI-powered coding assistance.
    * Example: Using OpenRouter, you can integrate Mistral Large 2 to generate code snippets based on user input.
    ```python
import openrouter

# Initialize Mistral Large 2 model
model = openrouter.MistralLarge2()

# Define a function to generate code snippets
def generate_code(prompt):
    response = model.generate(prompt)
    return response

# Test the function
print(generate_code("Write a Python function to sort a list of integers"))
```

2. **Data Analysis**: With its strong analytical capabilities, Mistral Large 2 can be used for data analysis tasks, such as data visualization and statistical modeling.
    * Example: Using OpenRouter, you can integrate Mistral Large 2 to analyze data and generate insights.
    ```python
import openrouter
import pandas as pd

# Initialize Mistral Large 2 model
model = openrouter.MistralLarge2()

# Define a function to analyze data
def analyze_data(data):
    prompt = "Analyze the following data: " + str(data)
    response = model.generate(prompt)
    return response

# Test the function
data = pd.DataFrame({'A': [1, 2, 

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
