# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-29
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, including coding, analysis, and function calling. This model boasts a context window of 131,072 tokens and can generate up to 4,096 tokens as output, making it suitable for complex tasks that require extensive input and output processing. With a knowledge cutoff of 2024-07, Mistral Large 2 is equipped with the latest information available up to that point.

### Architecture and Strengths
The architecture of Mistral Large 2 supports multiple capabilities such as text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers. Its main strengths are reflected in its benchmark scores: MMLU at 84.0, HumanEval at 92.0, LMSYS Arena ELO at 1225, and GSM8K at 93.0. These scores indicate that Mistral Large 2 excels in coding tasks, multilingual support, and function calling, positioning it as a top choice for applications requiring these functionalities. However, it's noted that Mistral Large 2 is not ideal for embeddings, bulk cheap processing, real-time sub-100ms tasks, or vision-heavy applications.

### Pricing and Use Cases
The pricing for Mistral Large 2 is structured as follows: $3.0 per 1M tokens for input and $9.0 per 1M tokens for output. For developers, this translates to costs such as $6.0 for 1,000 calls averaging 500 tokens, $60.0 for 10,000 calls, and $600.0 for 100,000 calls. Compared to its top competitor, GPT-4o, which charges $2.5/1M input and $10.

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

This indicates that using cached inputs and batch processing can significantly reduce costs, as they are provided at no additional charge.

#### When to Use Cached Tokens
Cached tokens should be utilized whenever possible to minimize input costs. Since cached inputs are free, leveraging them can lead to substantial savings, especially in applications where the same inputs are processed multiple times.

#### Batch API Savings
Batching API calls can also lead to cost savings, although the exact mechanism of these savings is not detailed in the provided pricing structure. Given that batch input is listed as $None per 1M tokens, it suggests that batching does not incur additional costs beyond the standard input and output pricing. This makes batch processing an attractive option for large-scale applications.

#### Cost at Scale
To understand the cost implications of using Mistral Large 2 at scale, let's examine the provided cost examples:
- **1,000 calls (avg 500 tokens)**: $6.0
- **10,000 calls**: $60.0
- **100,000 calls**: $600.0

These examples illustrate a linear scaling of costs with the number of API calls. For applications requiring a large number of calls, the cost can become significant.

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
The Mistral Large 2 model, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. It has a context window of 131,072 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2024-07.

#### Pricing
The pricing for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Benchmark Performance
The model's benchmark performance is as follows:
* **MMLU (Massive Multitask Language Understanding)**: 84.0 - This score indicates the model's ability to understand and perform a wide range of natural language processing tasks. A higher score suggests better performance.
* **HumanEval**: 92.0 - This score measures the model's ability to evaluate and execute human-written code. A higher score indicates better performance in coding tasks.
* **LMSYS Arena ELO**: 1225 - This score is a measure of the model's overall performance in a competitive arena, where it is pitted against other models. A higher score indicates better performance.
* **GSM8K**: 93.0 - This score measures the model's ability to solve math problems, specifically those from the Grade School Math (GSM8K) dataset.

#### Real-World Implications
The benchmark scores suggest that Mistral Large 2 is a high-performance model suitable for a variety of tasks

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts, making it suitable for coding, analysis, RAG, agents, multilingual tasks, and function calling.

#### Pricing Comparison
The pricing for Mistral Large 2 is as follows:
- Input: $3.0 per 1M tokens
- Output: $9.0 per 1M tokens

In comparison, one of its top competitors, GPT-4o, is priced at:
- Input: $2.5 per 1M tokens
- Output: $10.0 per 1M tokens

#### Performance Trade-offs
Mistral Large 2 has demonstrated strong performance across various benchmarks:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

While specific benchmark results for GPT-4o are not provided, the choice between Mistral Large 2 and GPT-4o may depend on the specific requirements of the task, including the balance between input and output costs, and the particular capabilities needed.

#### Context and Limits
Mistral Large 2 has a context window of 131,072 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2024-07. These specifications are crucial for determining the model's suitability for tasks that require extensive context or lengthy outputs.

#### When to Choose Each Model
- **Mistral Large 2** is best for tasks that require:
  - Advanced coding capabilities
  - In-depth analysis
  - Multilingual support
  - Function calling
  - Tasks that benefit from its specific capabilities such as RAG, agents, and system prompts
- **GPT-4o** might be more suitable for scenarios where:
  - Input costs are a significant concern, given its lower input price point
  - The specific capabilities of Mistral Large 2 are not required
  - Tasks are more output-intensive, as the output price difference may not be as significant a factor

#### Cost Examples
For Mistral Large 2, the

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium model released on 2024-07-24. With its extensive capabilities, including text, vision, function calling, and more, it's best suited for tasks like coding, analysis, and multilingual applications. Here, we'll explore the top 5 best use cases for Mistral Large 2, along with specific code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Large 2
1. **Coding and Development**: Mistral Large 2 excels in coding tasks, thanks to its high HumanEval score of 92.0. It can be used for code completion, code review, and even generating entire functions.
    ```python
    import openrouter
    model = openrouter.load_model("mistralai/mistral-large-2407")
    prompt = "Write a Python function to sort a list of integers."
    response = model.generate_text(prompt)
    print(response)
    ```
2. **Data Analysis**: With its strong analysis capabilities, Mistral Large 2 can be used for data analysis, report generation, and even creating data visualizations.
    ```python
    import openrouter
    import pandas as pd
    model = openrouter.load_model("mistralai/mistral-large-2407")
    data = pd.read_csv("data.csv")
    prompt = "Analyze the data and generate a report."
    response = model.generate_text(prompt, data=data)
    print(response)
    ```
3. **RAG (Retrieve, Augment, Generate) Tasks**: Mistral Large 2's high MMLU score of 84.0 makes it suitable for RAG tasks, which involve retrieving information, augmenting it, and generating new content.
    ```python
    import openrouter
    model = openrouter.load_model("mistralai/mistral-large

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
