# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-08
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. This model boasts an impressive set of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. Its architecture is designed to support a wide range of applications, with a context window of 131,072 tokens and a maximum output of 4,096 tokens. The knowledge cutoff for this model is 2024-07, ensuring it has a broad and up-to-date knowledge base.

### Strengths and Use Cases
Mistral Large 2 demonstrates its strengths through various benchmarks, scoring 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These scores indicate the model's proficiency in coding, analysis, and other complex tasks. It is best utilized for applications such as coding, analysis, RAG (Retrieve, Augment, Generate), agents, multilingual tasks, and function calling. However, it is not recommended for tasks that require embeddings, bulk cheap processing, real-time responses under 100ms, or vision-heavy applications. The pricing model for Mistral Large 2 includes $3.0 per 1M input tokens and $9.0 per 1M output tokens, with no charges for cached or batch input.

### Pricing and Competitiveness
The cost of using Mistral Large 2 can be estimated based on the number of calls and tokens. For example, 1,000 calls with an average of 500 tokens would cost $6.0, while 10,000 calls would amount to $60.0, and 100,000 calls would total $600.0. In comparison to its top competitor, GPT-4o, which charges $2.5 per 

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
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. The pricing structure is based on input and output tokens.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option when possible. Use cached tokens when:
* The input is repeated or can be reused.
* The application allows for caching and reuse of input tokens.

#### Batch API Savings
Batch input is also free, providing significant savings when making multiple API calls. To maximize batch API savings:
* Batch multiple requests together to reduce the number of API calls.
* Use batch input for large-scale applications or when making multiple requests.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* 1,000 API calls (avg 500 tokens): $6.0
* 10,000 API calls: $60.0
* 100,000 API calls: $600.0

These costs demonstrate a linear scaling of costs with the number of API calls.

#### Comparison to Top Competitors
Mistral Large 2 is priced competitively with top competitors like GPT-4o:
* GPT-4o: $2.5/1M input, $10.0/1M output
* Mistral Large 2: $3.0/1M input, $9.0/1M output

While

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
* **MMLU (Massive Multitask Language Understanding)**: 84.0, indicating the model's ability to understand and process a wide range of language tasks.
* **HumanEval**: 92.0, measuring the model's ability to generate human-like code and evaluate its coding capabilities.
* **LMSYS Arena ELO**: 1225, representing the model's competitive performance in a large-scale language model benchmark.
* **GSM8K**: 93.0, evaluating the model's math problem-solving skills.

#### Real-World Implications
These benchmark scores have significant implications for real-world use:
* The high **HumanEval** score suggests that Mistral Large 2 is well-suited for coding tasks, such as code generation and review.
* The strong **MMLU** score indicates that the model can handle a wide range of language tasks, making it a good choice for applications that require general language understanding.
* The **LMSYS Arena ELO** score demonstrates the model's competitive performance, implying that it can be used in applications where high-quality language generation is crucial.
* The **GSM8K** score shows that the model has good math problem-solving skills, making it suitable for tasks that require mathematical reasoning.

#### Capabilities and Limitations

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. This comparison will focus on its pricing, performance, and capabilities relative to its top competitors, specifically GPT-4o.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, whereas GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. This indicates that while GPT-4o is cheaper for input, Mistral Large 2 is slightly more cost-effective for output.

#### Performance Trade-offs
Mistral Large 2 boasts the following benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

These scores suggest strong performance across various tasks, including coding, analysis, and multilingual capabilities. However, without direct comparison benchmarks for GPT-4o in this context, it's challenging to assess performance trade-offs directly.

#### Capabilities and Best Use Cases
Mistral Large 2 supports a wide range of capabilities, including:
- Text
- Vision
- Function calling
- JSON mode
- Streaming
- System prompts

It is best suited for tasks such as:
- Coding
- Analysis
- RAG (Retrieve, Augment, Generate)
- Agents
- Multilingual tasks
- Function calling

On the other hand, it is not recommended for:
- Embeddings
- Bulk cheap operations
- Real-time applications requiring responses under 100ms
- Vision-heavy tasks

#### Cost Examples
For perspective, here are some cost examples for using Mistral Large 2:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
-

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium model released on 2024-07-24. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts, making it suitable for various applications such as coding, analysis, and multilingual support.

### Top 5 Best Use Cases for Mistral Large 2
Given its capabilities and pricing, here are the top 5 best use cases for Mistral Large 2:

1. **Coding and Development**: With its high scores in HumanEval (92.0) and LMSYS Arena ELO (1225), Mistral Large 2 is well-suited for coding tasks. It can be integrated with OpenRouter for automated code generation and review.
    ```python
    import openrouter
    from mistralai import MistralLarge2

    # Initialize Mistral Large 2 model
    model = MistralLarge2()

    # Define a coding task
    task = "Write a Python function to sort a list of integers."

    # Use OpenRouter to generate code
    generated_code = openrouter.generate_code(task, model)

    # Print the generated code
    print(generated_code)
    ```
2. **Analysis and Research**: Mistral Large 2's high MMLU score (84.0) and context window of 131,072 tokens make it ideal for in-depth analysis and research tasks. It can process large amounts of text data and provide insightful outputs.
    ```python
    import pandas as pd
    from mistralai import MistralLarge2

    # Load a dataset
    df = pd.read_csv("data.csv")

    # Initialize Mistral Large 2 model
    model = MistralLarge2()

    # Define an analysis task
    task = "Analyze the trends in the data and provide recommendations."

    #

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
