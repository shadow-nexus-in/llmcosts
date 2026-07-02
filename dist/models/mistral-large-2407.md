# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-02
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium large language model (LLM) designed to cater to a wide range of applications, particularly in coding, analysis, and multilingual tasks. This model is not open-source, indicating that its internal workings and training data are proprietary. With a context window of 131,072 tokens and a maximum output of 4,096 tokens, Mistral Large 2 is well-suited for tasks that require understanding and generating long pieces of text.

### Technical Strengths and Use Cases
The architecture of Mistral Large 2 supports various capabilities, including text and vision processing, function calling, JSON mode, streaming, and system prompts. Its strengths are reflected in its benchmark scores: 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These scores indicate that Mistral Large 2 is particularly adept at coding tasks, analysis, and tasks that require reasoning and problem-solving abilities. It is best utilized for applications such as coding assistance, data analysis, and tasks that involve multiple languages. However, it is not recommended for tasks that require embeddings, bulk processing at a low cost, real-time responses under 100ms, or vision-heavy tasks.

### Pricing and Cost Considerations
The pricing model for Mistral Large 2 is based on input and output tokens, with costs of $3.0 per 1M input tokens and $9.0 per 1M output tokens. There are no specified costs for cached input or batch input. For developers, estimating costs can be done using the provided examples: 1,000 calls averaging 500 tokens cost $6.0, scaling up to $60.0 for 10,000 calls and $600.0 for 100,000 calls

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
Cached tokens are free, making them an attractive option when possible. Use cached tokens for:
- **Frequent queries with the same input**: If your application involves asking the same questions or providing the same context repeatedly, cached tokens can significantly reduce costs.
- **Pre-computed inputs**: If you can pre-compute inputs and store them, using cached tokens for these inputs can save on input costs.

#### Batch API Savings
Batch inputs are also free, offering a way to reduce costs for bulk operations. Consider using batch inputs for:
- **Bulk processing**: When you need to process a large number of inputs at once, batching can help minimize costs.
- **Periodic tasks**: For tasks that run periodically and involve a large number of inputs, batch inputs can be particularly cost-effective.

#### Cost at Scale
To understand the cost implications of using Mistral Large 2 at scale, consider the following examples based on the provided data:
- **1,000 calls (avg 500 tokens)**: $6.0
- **10,000 calls**: $60.0
- **100,000 calls**: $600.0

These examples illustrate a linear scaling of

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 84.0 |
| HumanEval | 92.0 |
| LMSYS Arena ELO | 1225 |
| ARC | 93.0 |

## Benchmark Analysis
### Analysis of Mistral Large 2 Benchmark Performance
#### Model Overview
The Mistral Large 2 model, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. It has a context window of 131,072 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2024-07.

#### Pricing
The pricing for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Benchmark Performance
The model's benchmark performance is measured by the following scores:
* **MMLU (Massive Multitask Language Understanding)**: 84.0 - This score indicates the model's ability to understand and perform a wide range of natural language tasks. A higher score suggests better performance in tasks such as text classification, sentiment analysis, and question answering.
* **HumanEval**: 92.0 - This score measures the model's ability to evaluate and execute human-written code. A higher score indicates better performance in coding tasks, such as code completion and code optimization.
* **LMSYS Arena ELO**: 1225 - This score represents the model's performance in a competitive arena, where it is pitted against other models in a variety of tasks. A higher ELO score indicates better overall performance and adaptability.
* **GSM8K**: 93.0 - This score measures the model's performance in math problem-solving, specifically in the Grade School Math (GSM8K)

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, offered by Mistral AI, is a premium model released on 2024-07-24. It is not open source and is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens. This comparison will focus on its top competitor, GPT-4o, highlighting price differences, performance trade-offs, and scenarios where each model is preferred.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is more expensive than GPT-4o in terms of input price but cheaper in terms of output price. This suggests that for applications where the output is significantly larger than the input, Mistral Large 2 might be more cost-effective.

#### Performance Comparison
Mistral Large 2 has the following benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

While specific benchmark scores for GPT-4o are not provided, the choice between Mistral Large 2 and GPT-4o may depend on the specific use case and the importance of these benchmarks for the intended application.

#### Capabilities and Use Cases
Mistral Large 2 supports a wide range of capabilities including text, vision, function_calling, json_mode, streaming, and system_prompts. It is best suited for:
- Coding
- Analysis
- RAG (Retrieval-Augmented Generation)
- Agents
- Multilingual tasks
- Function calling

It is not recommended for:
- Embeddings
- Bulk cheap operations
- Real-time applications requiring responses under 100ms
- Vision-heavy tasks

#### Cost Examples
For Mistral Large 2, the cost can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100,000 calls: $600.0

These costs are based on the

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model that excels in various tasks, including coding, analysis, and function calling. With its impressive benchmarks, such as an MMLU score of 84.0 and a HumanEval score of 92.0, this model is a powerful tool for developers and analysts.

### Top 5 Best Use Cases for Mistral Large 2
Based on its capabilities and limitations, here are the top 5 best use cases for Mistral Large 2:

1. **Coding and Code Review**: With its high HumanEval score, Mistral Large 2 is well-suited for coding tasks, such as code completion, code review, and code optimization. For example, you can use Mistral Large 2 with OpenRouter to generate code snippets in various programming languages.
   ```python
import openrouter

# Initialize Mistral Large 2 model
model = openrouter.Model("mistralai/mistral-large-2407")

# Generate code snippet
code_snippet = model.generate_code("Write a Python function to calculate the area of a circle")
print(code_snippet)
```

2. **Data Analysis and Visualization**: Mistral Large 2's analysis capabilities make it an excellent choice for data analysis and visualization tasks. You can use it to generate insights, create reports, and visualize data.
   ```python
import openrouter
import pandas as pd

# Load data
data = pd.read_csv("data.csv")

# Analyze data using Mistral Large 2
analysis = openrouter.Model("mistralai/mistral-large-2407").analyze_data(data)
print(analysis)
```

3. **RAG (Retrieve, Augment, Generate) Tasks**: Mistral Large 2's capabilities in text and function calling make it well-suited for R

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
