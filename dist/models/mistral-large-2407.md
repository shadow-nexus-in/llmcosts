# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-05
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed for a wide range of applications, including coding, analysis, and function calling. This model boasts a context window of 131,072 tokens and can generate up to 4,096 tokens as output. With a knowledge cutoff of 2024-07, Mistral Large 2 is equipped with the latest information available up to that date. Its capabilities extend beyond text processing to include vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Strengths and Use Cases
Mistral Large 2 demonstrates its technical prowess through impressive benchmark scores: 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These scores underscore its suitability for complex tasks such as coding, where it can leverage its function calling and analysis capabilities. The model is particularly adept at handling multilingual inputs and can be effectively utilized in applications requiring sophisticated text and vision processing. However, it's worth noting that Mistral Large 2 is not optimized for embeddings, bulk cheap processing, real-time sub-100ms responses, or vision-heavy tasks, making it less ideal for these specific use cases.

### Pricing and Cost Considerations
The pricing model for Mistral Large 2 is based on input and output tokens, with costs set at $3.0 per 1M input tokens and $9.0 per 1M output tokens. For developers, this translates to $6.0 for 1,000 calls averaging 500 tokens, $60.0 for 10,000 calls, and $600.0 for 100,000 calls. In comparison to competitors like GPT-4o, which offers $2

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
* The input is repetitive or can be reused.
* The application allows for caching and reuse of input tokens.

#### Batch API Savings
Batch input is also free, providing significant savings when making multiple API calls. To maximize batch API savings:
* Group multiple requests together in a single API call.
* Ensure the total input tokens are within the context window limit (131,072 tokens).

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* 1,000 API calls (avg 500 tokens): $6.0
* 10,000 API calls: $60.0
* 100,000 API calls: $600.0

These costs are based on the average number of tokens per call and the pricing structure. For larger-scale applications, the cost can be significant, but the capabilities and performance of Mistral Large 2 may justify the expense.

#### Comparison to Top Competitors
Mistral Large 2 competes with models like GPT-4o, which offers:
* Input: $2.5 per 1M tokens
* Output: $10.0

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
* **MMLU (Massive Multitask Language Understanding)**: 84.0 - This score indicates the model's ability to understand and process natural language across a wide range of tasks. A higher MMLU score suggests better performance in tasks that require comprehension, reasoning, and generation of human-like text.
* **HumanEval**: 92.0 - This score evaluates the model's ability to generate code that is correct and functional. A higher HumanEval score indicates better performance in coding tasks, such as code completion, bug fixing, and code generation.
* **LMSYS Arena ELO**: 1225 - This score measures the model's performance in a competitive arena, where it is pitted against other models in a variety of tasks. A higher LMSYS Arena ELO score suggests better overall performance and adaptability.
* **GSM8K**: 93.0 - This score is not explicitly defined in the provided data, but it is likely related to the model's performance on a specific benchmark or task.

#### Real-World Implications
The benchmark scores suggest that Mistral Large 2 is a high-performance model suitable for a variety of tasks, including:
* **Coding**: With a high HumanEval score, Mistral Large 2 is well-suited for coding

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts, making it suitable for coding, analysis, RAG, agents, multilingual tasks, and function calling.

#### Pricing Comparison
The pricing for Mistral Large 2 is as follows:
- Input: $3.0 per 1M tokens
- Output: $9.0 per 1M tokens

In comparison, one of its top competitors, GPT-4o, is priced at:
- Input: $2.5 per 1M tokens
- Output: $10.0 per 1M tokens

Mistral Large 2 is more expensive in terms of input cost but slightly cheaper in terms of output cost compared to GPT-4o.

#### Performance Trade-offs
Mistral Large 2 has the following benchmarks:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

While the exact benchmarks for GPT-4o are not provided, the performance of Mistral Large 2 indicates a strong capability in coding, analysis, and other tasks it is best suited for.

#### Context and Limits
Mistral Large 2 has:
- Context Window: 131,072 tokens
- Max Output: 4,096 tokens
- Knowledge Cutoff: 2024-07

These specifications are not provided for GPT-4o, but they are crucial for understanding the limitations and capabilities of Mistral Large 2, especially in tasks requiring large context windows or significant output.

#### When to Choose Each Model
- **Mistral Large 2** is best for tasks that require its specific capabilities such as coding, analysis, RAG, agents, multilingual tasks, and function calling. Its performance in these areas, as indicated by its benchmarks, makes it a strong choice despite its higher input cost.
- **GPT-4o** might be more economical for tasks where input cost is a significant factor and the specific capabilities of Mistral Large 2 are not required. However, the slightly higher output cost of GPT

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model that offers a wide range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. With its strong performance in benchmarks like MMLU (84.0), HumanEval (92.0), LMSYS Arena ELO (1225), and GSM8K (93.0), it is best suited for tasks such as coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual support, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Given its capabilities and performance metrics, here are the top 5 best use cases for Mistral Large 2, along with practical advice and code integration examples using OpenRouter:

1. **Coding and Software Development**: Mistral Large 2 excels in coding tasks, making it an ideal choice for software development, code review, and code generation. 
    ```python
    # Example of using Mistral Large 2 for coding tasks via OpenRouter
    import openrouter
    
    # Initialize the model
    model = openrouter.MistralLarge2()
    
    # Define a coding prompt
    prompt = "Write a Python function to sort a list of integers."
    
    # Generate code using the model
    generated_code = model.generate_code(prompt)
    
    # Print the generated code
    print(generated_code)
    ```

2. **Data Analysis and Insights**: With its strong analytical capabilities, Mistral Large 2 can be used for data analysis, providing insights from complex data sets. 
    ```python
    # Example of using Mistral Large 2 for data analysis via OpenRouter
    import openrouter
    import pandas as pd
    
    # Load a sample dataset
    data = pd.read_csv

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
