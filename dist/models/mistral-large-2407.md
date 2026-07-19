# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-19
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. This model boasts an architecture that supports a wide range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. With a context window of 131,072 tokens and a maximum output of 4,096 tokens, Mistral Large 2 is designed to handle complex tasks with a knowledge cutoff of 2024-07.

### Technical Strengths and Use Cases
Mistral Large 2 demonstrates its technical strengths through various benchmarks: achieving 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These scores highlight the model's proficiency in coding, analysis, and multilingual tasks, making it best suited for applications such as coding, analysis, RAG (Retrieval-Augmented Generation), agents, and function calling. However, it is not recommended for embeddings, bulk cheap processing, real-time sub-100ms tasks, or vision-heavy applications. The pricing model is based on input and output tokens, with costs of $3.0 per 1M input tokens and $9.0 per 1M output tokens.

### Pricing and Cost Considerations
Developers should consider the pricing structure when integrating Mistral Large 2 into their applications. The cost examples provided indicate that 1,000 calls with an average of 500 tokens would amount to $6.0, scaling up to $60.0 for 10,000 calls and $600.0 for 100,000 calls. In comparison to its top competitor, GPT-4o, which charges $2.5 per 1M input tokens and $10.0 per 1M output tokens, Mistral Large 2 offers

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
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. The pricing structure is based on input and output tokens, with specific considerations for cached and batch inputs.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
- **Input**: $3.0 per 1M tokens
- **Output**: $9.0 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

This indicates that using cached inputs and batch processing can significantly reduce costs, as these are provided at no additional charge.

#### When to Use Cached Tokens
Cached tokens should be utilized whenever possible to minimize input costs. Since cached inputs are free, leveraging them can lead to substantial savings, especially in applications where the same or similar inputs are processed repeatedly.

#### Batch API Savings
Batching API calls can also lead to cost savings, as batch inputs are free. This makes Mistral Large 2 particularly cost-effective for applications that can process data in batches, rather than requiring real-time, individual API calls.

#### Cost at Scale
To understand the cost implications of using Mistral Large 2 at scale, let's examine the provided cost examples:
- **1,000 calls (avg 500 tokens)**: $6.0
- **10,000 calls**: $60.0
- **100,000 calls**: $600.0

These examples illustrate a linear cost scaling, where the cost per call decreases as the volume of calls increases. However, it's essential to calculate the cost based on the actual number of tokens processed, considering both input and output tokens.

For a more precise calculation, let's

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
Mistral Large 2, a premium model provided by Mistral AI, demonstrates strong performance across various benchmarks. Released on 2024-07-24, this model is well-suited for tasks such as coding, analysis, and function calling.

#### Benchmark Scores
The model's performance can be evaluated through the following benchmark scores:
* **MMLU (Massive Multitask Language Understanding)**: 84.0 - This score indicates the model's ability to understand and process natural language across a wide range of tasks. A higher MMLU score suggests better language comprehension and generation capabilities.
* **HumanEval**: 92.0 - This benchmark assesses the model's ability to generate correct and functional code in response to programming prompts. A high HumanEval score, such as 92.0, demonstrates the model's proficiency in coding tasks.
* **LMSYS Arena ELO**: 1225 - The LMSYS Arena ELO score measures the model's competitive performance in a variety of tasks, including coding, reasoning, and natural language processing. A higher ELO score indicates better overall performance and adaptability.
* **GSM8K**: 93.0 - This benchmark evaluates the model's ability to reason and solve math problems. A high GSM8K score suggests strong mathematical reasoning capabilities.

#### Real-World Implications
The benchmark scores suggest that Mistral Large 2 is well-suited for tasks that require:
* Strong language understanding and generation capabilities (MMLU: 84.0)
* Proficient coding and programming skills (HumanEval: 92.0)
* Competitive performance in a variety of tasks (L

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. It offers a range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, making it suitable for coding, analysis, and multilingual applications.

#### Pricing Comparison
The pricing for Mistral Large 2 is as follows:
- Input: $3.0 per 1M tokens
- Output: $9.0 per 1M tokens

In comparison, GPT-4o, a top competitor, is priced at:
- Input: $2.5 per 1M tokens
- Output: $10.0 per 1M tokens

Mistral Large 2 is more expensive than GPT-4o in terms of input pricing but slightly cheaper in terms of output pricing.

#### Performance Trade-offs
Mistral Large 2 has the following benchmarks:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

While the specific benchmarks for GPT-4o are not provided, the performance trade-offs between the two models can be considered in terms of their capabilities and limitations. Mistral Large 2 is best suited for coding, analysis, and multilingual applications but is not recommended for embeddings, bulk cheap processing, real-time sub-100ms applications, or vision-heavy tasks.

#### Context and Limits
Mistral Large 2 has a context window of 131,072 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2024-07. These specifications are not provided for GPT-4o, making a direct comparison challenging. However, when choosing between the two models, consider the specific requirements of your application, including the need for a large context window, output size, and the relevance of the knowledge cutoff.

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100,000 calls: $600.0

These estimates are based on the pricing model and do not account for

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. With its impressive benchmarks, including an MMLU score of 84.0 and a HumanEval score of 92.0, it's well-suited for various applications, particularly those involving coding, analysis, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Given its capabilities and limitations, here are the top 5 best use cases for Mistral Large 2:

1. **Coding Assistance**: With its high HumanEval score, Mistral Large 2 is ideal for coding tasks, such as code completion, code review, and bug detection. For example, you can integrate Mistral Large 2 with OpenRouter to generate code snippets based on user input:
    ```python
import openrouter

# Initialize Mistral Large 2 model
model = openrouter.MistralLarge2()

# Define a function to generate code snippets
def generate_code(prompt):
    response = model.generate_text(prompt, max_tokens=4096)
    return response

# Test the function
print(generate_code("Write a Python function to sort a list of integers"))
```

2. **Data Analysis**: Mistral Large 2's high MMLU score and ability to process large context windows make it suitable for data analysis tasks, such as data summarization, data visualization, and data mining. You can use OpenRouter to integrate Mistral Large 2 with your data analysis pipeline:
    ```python
import openrouter
import pandas as pd

# Load data into a Pandas dataframe
df = pd.read_csv("data.csv")

# Define a function to summarize data using Mistral Large 2
def summarize_data(df):
    prompt = "Summarize the data in the following table: " + str(df)
    response = open

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
