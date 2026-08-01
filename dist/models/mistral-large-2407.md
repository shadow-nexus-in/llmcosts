# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-01
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly in coding, analysis, and multilingual tasks. This model boasts an impressive architecture that supports capabilities such as text and vision processing, function calling, JSON mode, streaming, and system prompts. With a context window of 131,072 tokens and a maximum output of 4,096 tokens, Mistral Large 2 is well-suited for complex tasks that require extensive context understanding.

### Technical Strengths and Use Cases
The technical strengths of Mistral Large 2 are underscored by its benchmark scores: MMLU at 84.0, HumanEval at 92.0, LMSYS Arena ELO at 1225, and GSM8K at 93.0. These scores indicate the model's proficiency in various tasks, making it an ideal choice for developers working on projects that involve coding, analysis, and reasoning. The model's capabilities in function calling, streaming, and system prompts further enhance its utility in real-world applications. However, it's worth noting that Mistral Large 2 is not recommended for tasks that require embeddings, bulk processing at low costs, real-time responses under 100ms, or vision-heavy applications.

### Pricing and Cost Considerations
The pricing for Mistral Large 2 is structured as follows: $3.0 per 1M input tokens and $9.0 per 1M output tokens. For developers, this translates to costs such as $6.0 for 1,000 calls averaging 500 tokens, $60.0 for 10,000 calls, and $600.0 for 100,000 calls. In comparison to its top competitor, GPT-4o, which offers input at $2.5/1M and output at $10.

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
- **Cached Input**: No additional cost ($None per 1M tokens)
- **Batch Input**: No additional cost ($None per 1M tokens)

#### When to Use Cached Tokens
Given that there is no additional cost for cached input tokens, it is beneficial to use cached tokens whenever possible. This can significantly reduce the overall cost, especially for applications where the same input data is processed multiple times.

#### Batch API Savings
Although the pricing data does not specify a direct discount for batch inputs, the fact that batch input costs are listed as $None per 1M tokens suggests that batching may not incur additional costs beyond the standard input cost. However, the actual savings from batching would depend on the efficiency of the batch processing and how it affects the total number of tokens processed.

#### Cost at Scale
To understand the cost implications of using Mistral Large 2 at different scales, let's examine the provided cost examples:
- **1,000 calls (avg 500 tokens)**: $6.0
- **10,000 calls**: $60.0
- **100,000 calls**: $600.0

These examples illustrate a linear scaling of costs with the number of API calls. However, to calculate the cost based on tokens, we need to consider the average token count per call and the input/output ratio.

Assuming an average

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
* **MMLU (Massive Multitask Language Understanding)**: 84.0 - This score indicates the model's ability to understand and generate human-like text across a wide range of tasks and topics. A higher MMLU score suggests better language understanding capabilities.
* **HumanEval**: 92.0 - This score measures the model's ability to write correct and functional code in response to programming tasks. A higher HumanEval score indicates better coding capabilities.
* **LMSYS Arena ELO**: 1225 - This score represents the model's competitive performance in a large language model arena, where models are pitted against each other to complete tasks. A higher ELO score suggests better overall performance.
* **GSM8K**: 93.0 - This score measures the model's ability to solve math problems, specifically those from the Grade School Math (GSM8K) dataset.

#### Real-World Implications
These benchmark scores have significant implications for real-world use cases:
* **Coding and Analysis**: With a high HumanEval score, Mistral Large 2 is well-suited for coding tasks, such as generating code snippets or completing programming assignments.
* **Multilingual Support**: The model's high MMLU score suggests it can handle a wide range of languages and topics

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. This comparison will focus on its pricing, performance, and capabilities in relation to its top competitors, specifically GPT-4o.

#### Pricing Comparison
| Model | Input Price per 1M Tokens | Output Price per 1M Tokens |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens. In contrast, GPT-4o is priced at $2.5 per 1M input tokens but $10.0 per 1M output tokens. This indicates that while GPT-4o is cheaper for input, Mistral Large 2 is more cost-effective for output.

#### Performance Trade-offs
Mistral Large 2 boasts impressive benchmarks:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

These benchmarks suggest that Mistral Large 2 excels in coding, analysis, and multilingual tasks. However, its performance in areas like embeddings, bulk processing, real-time applications under 100ms, and vision-heavy tasks is not its strong suit.

#### Capabilities and Best Use Cases
Mistral Large 2 supports a wide range of capabilities, including:
- Text
- Vision
- Function calling
- JSON mode
- Streaming
- System prompts

It is best utilized for:
- Coding
- Analysis
- RAG (Retrieval-Augmented Generation)
- Agents
- Multilingual tasks
- Function calling

#### Choosing Between Mistral Large 2 and GPT-4o
- **Choose Mistral Large 2** for applications that require strong coding, analysis, and multilingual capabilities, where the output cost-effectiveness and the model's specific capabilities (like function calling and system prompts) are beneficial.
- **Choose GPT-4o** for applications where input cost is a significant factor, and the slightly higher output cost can be

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model that excels in various tasks, including coding, analysis, and function calling. With its impressive benchmarks, such as an MMLU score of 84.0 and a HumanEval score of 92.0, this model is a top choice for many applications.

### Top 5 Best Use Cases for Mistral Large 2
Based on its capabilities and performance, here are the top 5 best use cases for Mistral Large 2:

1. **Coding Assistance**: With its high HumanEval score, Mistral Large 2 is well-suited for coding tasks, such as code completion, code review, and code generation. For example, you can use Mistral Large 2 with OpenRouter to generate code snippets in various programming languages.
    ```python
import openrouter

# Initialize Mistral Large 2 model
model = openrouter.Model("mistralai/mistral-large-2407")

# Generate code snippet
code_snippet = model.generate_code("Write a Python function to calculate the area of a rectangle")
print(code_snippet)
```

2. **Data Analysis**: Mistral Large 2's high MMLU score indicates its ability to understand and analyze complex data. You can use it to analyze large datasets, identify patterns, and generate insights.
    ```python
import pandas as pd
import openrouter

# Load dataset
df = pd.read_csv("data.csv")

# Initialize Mistral Large 2 model
model = openrouter.Model("mistralai/mistral-large-2407")

# Analyze data
analysis = model.analyze_data(df)
print(analysis)
```

3. **RAG (Retrieve, Augment, Generate) Tasks**: Mistral Large 2's capabilities in text and function calling make it an

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
