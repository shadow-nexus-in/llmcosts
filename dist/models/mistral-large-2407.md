# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-06
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, including coding, analysis, and function calling. This model boasts a context window of 131,072 tokens and can generate up to 4,096 tokens as output. With a knowledge cutoff of 2024-07, Mistral Large 2 is equipped with capabilities such as text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Strengths and Use Cases
The architecture of Mistral Large 2 supports its main strengths, which are reflected in its benchmark scores: MMLU at 84.0, HumanEval at 92.0, LMSYS Arena ELO at 1225, and GSM8K at 93.0. These scores indicate the model's proficiency in coding, analysis, and other tasks. It is best utilized for applications involving coding, analysis, retrieval-augmented generation (RAG), agents, multilingual support, and function calling. However, it is not recommended for use cases requiring embeddings, bulk cheap processing, real-time responses under 100ms, or vision-heavy tasks.

### Pricing and Cost Considerations
The pricing model for Mistral Large 2 is based on input and output tokens, with costs set at $3.0 per 1M input tokens and $9.0 per 1M output tokens. There are no specified costs for cached input or batch input. For example, 1,000 calls averaging 500 tokens each would cost $6.0, while 10,000 calls would amount to $60.0, and 100,000 calls would total $600.0. When comparing with top competitors like GPT-4o, which offers $2.5/1M

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
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. The pricing structure for Mistral Large 2 is based on input and output tokens.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs when the same input is used multiple times. Since cached input is free, it is recommended to use cached tokens whenever possible to minimize costs.

#### Batch API Savings
Batch input is also free, which means that making batch API calls can help reduce costs. By batching multiple inputs together, users can take advantage of the free batch input pricing and save on costs.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* 1,000 calls (avg 500 tokens): $6.0
* 10,000 calls: $60.0
* 100,000 calls: $600.0

To calculate the cost at scale, we can use the following formula:
Cost = (Number of calls \* Average tokens per call) \* (Input cost per token + Output cost per token)

For example, for 1,000 calls with an average of 500 tokens per call:
Cost = (1,000 \* 500) \* ($3.0/1M + $9.0/1M) = $6.0

#### Comparison to Top Competitors
Mist

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 84.0 |
| HumanEval | 92.0 |
| LMSYS Arena ELO | 1225 |
| ARC | 93.0 |

## Benchmark Analysis
### Mistral Large 2 Benchmark Performance Analysis
#### Overview
Mistral Large 2, a premium model provided by Mistral AI, boasts an impressive set of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. This analysis delves into the model's benchmark performance, focusing on MMLU, HumanEval, and Arena ELO scores, to understand its real-world applications.

#### Benchmark Scores
The model's performance is highlighted by the following benchmark scores:
* **MMLU (Massive Multitask Language Understanding)**: 84.0 - This score indicates the model's ability to understand and generate human-like text across a wide range of tasks and topics. A higher MMLU score suggests better language comprehension and generation capabilities.
* **HumanEval**: 92.0 - This score measures the model's ability to generate correct and functional code in response to programming prompts. A high HumanEval score implies that the model is proficient in coding tasks and can produce reliable code.
* **LMSYS Arena ELO**: 1225 - This score represents the model's competitive performance in a large-scale language model benchmarking arena. A higher ELO score indicates that the model can outperform others in various language tasks, demonstrating its overall language proficiency.

#### Real-World Implications
These benchmark scores have significant implications for real-world use cases:
* **Coding and Analysis**: With a high HumanEval score, Mistral Large 2 is well-suited for coding tasks, such as generating functional code, debugging, and code review.
* **Multilingual Support**: The model's impressive MMLU score suggests that it can handle multiple languages, making it a good choice for applications that

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts, making it suitable for coding, analysis, RAG, agents, multilingual tasks, and function calling.

#### Pricing Comparison
The pricing for Mistral Large 2 is as follows:
- Input: $3.0 per 1M tokens
- Output: $9.0 per 1M tokens

In comparison, GPT-4o, a top competitor, is priced at:
- Input: $2.5 per 1M tokens
- Output: $10.0 per 1M tokens

Mistral Large 2 is more expensive in terms of input costs but slightly cheaper for output costs compared to GPT-4o.

#### Performance Trade-offs
Mistral Large 2 has demonstrated strong performance across various benchmarks:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

While specific benchmark scores for GPT-4o are not provided, the choice between Mistral Large 2 and GPT-4o may depend on the specific requirements of the task, including the need for multilingual support, function calling, and the balance between input and output costs.

#### Context and Limits
Mistral Large 2 has a context window of 131,072 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2024-07. These parameters are crucial for determining the suitability of the model for specific tasks, especially those requiring extensive context or detailed outputs.

#### Capabilities and Best Use Cases
Mistral Large 2 is best suited for tasks involving:
- Coding
- Analysis
- RAG (Retrieval-Augmented Generation)
- Agents
- Multilingual tasks
- Function calling

It is not recommended for tasks that require:
- Embeddings
- Bulk cheap processing
- Real-time responses under 100ms
- Vision-heavy tasks

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, a premium model by Mistral AI, offers a wide range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. With its high performance benchmarks (MMLU: 84.0, HumanEval: 92.0, LMSYS Arena ELO: 1225, GSM8K: 93.0), it is best suited for tasks such as coding, analysis, RAG, agents, multilingual, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
#### 1. **Coding and Software Development**
Mistral Large 2 excels in coding tasks, making it an ideal choice for software development. Its ability to understand and generate code in multiple languages can significantly accelerate development processes. For example, integrating Mistral Large 2 with OpenRouter for automated code review and generation can enhance code quality and reduce development time.

```python
import openrouter

# Initialize Mistral Large 2 model
model = openrouter.MistralLarge2()

# Define a coding task
task = "Write a Python function to sort a list of integers."

# Generate code using Mistral Large 2
code = model.generate_code(task)

# Print the generated code
print(code)
```

#### 2. **Data Analysis and Insights**
With its strong analytical capabilities, Mistral Large 2 can be used for data analysis, providing valuable insights from large datasets. Its ability to process and understand natural language queries makes it an excellent tool for data exploration.

```python
import pandas as pd
import openrouter

# Load a dataset
data = pd.read_csv("data.csv")

# Initialize Mistral Large 2 model
model = openrouter.MistralLarge2()

# Define an analysis task
task = "What are the average sales by region?"

# Generate insights using Mistral Large 2

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
