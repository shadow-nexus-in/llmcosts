# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-03
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. This model boasts an impressive set of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. With a context window of 131,072 tokens and a maximum output of 4,096 tokens, Mistral Large 2 is designed to handle complex tasks. Its knowledge cutoff is 2024-07, ensuring it has access to a vast amount of information up to that point.

### Technical Strengths and Use Cases
Mistral Large 2 demonstrates its strengths through various benchmarks: MMLU (84.0), HumanEval (92.0), LMSYS Arena ELO (1225), and GSM8K (93.0). These scores indicate the model's proficiency in coding, analysis, and other areas. It is best utilized for tasks such as coding, analysis, RAG (Retrieve, Augment, Generate), agents, multilingual support, and function calling. However, it is not recommended for embeddings, bulk cheap processing, real-time applications requiring sub-100ms responses, or vision-heavy tasks. The pricing model is based on input and output tokens, with costs of $3.0 per 1M input tokens and $9.0 per 1M output tokens.

### Pricing and Cost Considerations
Developers should consider the pricing structure when integrating Mistral Large 2 into their applications. The cost can be estimated based on the number of calls and average tokens per call. For example, 1,000 calls with an average of 500 tokens would cost $6.0, while 10,000 calls would amount to $60.0, and 100,000 calls would be $600.0. In comparison to its top competitors, such as GPT-4o, which charges $

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
- **Cached Input**: $0 per 1M tokens (free)
- **Batch Input**: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for reducing costs. Use cached tokens when:
* The input data is repetitive or has a high degree of similarity.
* The model is being used for applications where input data can be pre-processed and cached.

#### Batch API Savings
Batch inputs are also free, offering significant savings for bulk API calls. Use batch API calls when:
* Making a large number of API requests with similar input parameters.
* The application can tolerate delayed processing in exchange for cost savings.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: $6.0
* **10,000 calls**: $60.0
* **100,000 calls**: $600.0

These costs demonstrate a linear scaling of expenses with the number of API calls, indicating that the cost per call remains constant regardless of the volume.

#### Comparison to Top Competitors
Mistral Large 2's pricing is competitive with top models like GPT-4o:
* **GPT-4o**: $2.5/1M input,

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
* **MMLU (Massive Multitask Language Understanding)**: 84.0, indicating the model's ability to understand and generate human-like text across a wide range of tasks and domains.
* **HumanEval**: 92.0, measuring the model's ability to write correct and functional code in response to programming prompts.
* **LMSYS Arena ELO**: 1225, representing the model's competitive performance in a large-scale language model benchmarking arena.
* **GSM8K**: 93.0, evaluating the model's math problem-solving abilities.

#### Real-World Implications
These benchmark scores suggest that Mistral Large 2 is a high-performance model suitable for:
* **Coding tasks**: With a high HumanEval score, the model is capable of generating correct and functional code.
* **Analysis and reasoning**: The model's high MMLU score indicates its ability to understand and generate human-like text, making it suitable for analysis and reasoning tasks.
* **Multilingual applications**: The model's capabilities and high benchmark scores make it a good fit for multilingual applications.

#### Cost and Pricing
The model's pricing is as follows:
* **Input**: $3.0 per 1M tokens
* **Output**: $9.0 per 1M

## Competitor Comparison
### Mistral Large 2 Comparison
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. It offers a range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, making it suitable for coding, analysis, RAG, agents, multilingual tasks, and function calling.

#### Pricing Comparison
Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens. In comparison, its top competitor, GPT-4o, is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens.

| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

#### Performance Trade-offs
Mistral Large 2 has a context window of 131,072 tokens and a maximum output of 4,096 tokens. Its performance is measured by the following benchmarks:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

In contrast, GPT-4o's performance benchmarks are not provided in the data. However, its lower input price and slightly higher output price suggest that it may offer a different balance of cost and performance.

#### When to Choose Each Model
Choose Mistral Large 2 for tasks that require:
* High-performance coding, analysis, and RAG capabilities
* Function calling and multilingual support
* A balance of input and output pricing

Choose GPT-4o for tasks that require:
* Lower input costs, potentially suitable for large-scale input processing
* Similar output pricing to Mistral Large 2, with a slightly higher cost per 1M output tokens

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
* 1,000 calls (avg 500 tokens): $6.0
* 10,000 calls: $60.0
* 100,000 calls: $600.

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. With its robust capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, it is best suited for tasks such as coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual support, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Given its capabilities and limitations, here are the top 5 best use cases for Mistral Large 2, along with specific code integration examples mentioning OpenRouter:

1. **Coding and Software Development**: Mistral Large 2 excels in coding tasks, making it an ideal choice for software development, code review, and code generation. 
    ```python
    import openrouter
    model = openrouter.load_model("mistralai/mistral-large-2407")
    prompt = "Write a Python function to sort a list of integers."
    response = model.generate_text(prompt)
    print(response)
    ```
2. **Data Analysis and Insight Generation**: With its strong analytical capabilities, Mistral Large 2 can be used to analyze data, generate insights, and create reports.
    ```python
    import pandas as pd
    import openrouter
    model = openrouter.load_model("mistralai/mistral-large-2407")
    data = pd.read_csv("data.csv")
    prompt = "Analyze the data and generate a report."
    response = model.generate_text(prompt, data=data)
    print(response)
    ```
3. **Multilingual Support and Translation**: Mistral Large 2 supports multiple languages, making it suitable for translation tasks, language understanding, and generation.
    ```python
    import openrouter
    model = openrouter.load_model("mistralai/mistral-large-2407")


## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
