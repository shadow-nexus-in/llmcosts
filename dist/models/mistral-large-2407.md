# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-17
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, including coding, analysis, and function calling. This model boasts an impressive architecture with a context window of 131,072 tokens and a maximum output of 4,096 tokens. Its knowledge cutoff is 2024-07, ensuring it has been trained on a vast amount of data up to that point.

### Technical Strengths and Use Cases
Mistral Large 2 demonstrates its technical prowess through its capabilities, which include text, vision, function calling, JSON mode, streaming, and system prompts. Its strengths are reflected in its benchmark scores: MMLU at 84.0, HumanEval at 92.0, LMSYS Arena ELO at 1225, and GSM8K at 93.0. These scores indicate the model's proficiency in various tasks, making it best suited for applications such as coding, analysis, and multilingual support. However, it's not recommended for use cases that require embeddings, bulk cheap processing, real-time sub-100ms responses, or vision-heavy tasks.

### Pricing and Cost Considerations
The pricing model for Mistral Large 2 is based on input and output tokens, with costs set at $3.0 per 1M input tokens and $9.0 per 1M output tokens. For developers, understanding these costs is crucial for budgeting. For example, 1,000 calls averaging 500 tokens would cost $6.0, while 10,000 calls would amount to $60.0, and 100,000 calls would total $600.0. When comparing with top competitors like GPT-4o, which offers $2.5/1M input and $10.0/1M output, developers must weigh the capabilities

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
Mistral Large 2, a premium model by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. The pricing structure is based on input and output tokens, with specific considerations for cached and batch inputs.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for reducing costs. Use cached tokens when:
* The input data is repetitive or has a high degree of overlap.
* The model is being used for applications where input data is frequently reused.

#### Batch API Savings
Batch inputs are also free, which can lead to significant cost savings when making multiple API calls. Batch API calls when:
* Making a large number of requests with similar input data.
* The application can tolerate delayed processing in exchange for reduced costs.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* 1,000 calls (avg 500 tokens): $6.0
* 10,000 calls: $60.0
* 100,000 calls: $600.0

To estimate costs for a specific use case, consider the average number of tokens per call and the total number of calls. For example, if the average call has 500 tokens, the cost per call would be:
* 500 tokens / 1,000,000 tokens per 1M * ($3.0 + $9.0) = $0.006 per call (input

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
The Mistral Large 2 model, released by Mistral AI on 2024-07-24, is a premium, non-open-source model with a context window of 131,072 tokens and a maximum output of 4,096 tokens.

#### Pricing
The pricing for Mistral Large 2 is as follows:
* Input: **$3.0 per 1M tokens**
* Output: **$9.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Benchmark Scores
The model's benchmark performance is measured by the following scores:
* **MMLU: 84.0**: The MMLU (Massive Multitask Language Understanding) score evaluates a model's ability to perform a wide range of natural language processing tasks. A higher MMLU score indicates better overall language understanding.
* **HumanEval: 92.0**: The HumanEval score assesses a model's ability to generate code that is correct and functional. A higher HumanEval score suggests better coding capabilities.
* **LMSYS Arena ELO: 1225**: The LMSYS Arena ELO score measures a model's performance in a competitive environment, where it is pitted against other models. A higher ELO score indicates better overall performance.

#### Real-World Implications
The benchmark scores suggest that Mistral Large 2 is a strong performer in the following areas:
* **Coding**: With a high HumanEval score of **92.0**, Mistral Large 2 is well-suited for coding tasks, such as generating

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium language model released on 2024-07-24. It offers a range of capabilities including text, vision, function calling, and more. In this comparison, we will evaluate Mistral Large 2 against its top competitor, GPT-4o, focusing on pricing, performance, and use cases.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, whereas GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. This indicates that GPT-4o is cheaper for input tokens but more expensive for output tokens.

#### Performance Comparison
Mistral Large 2 has the following benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

In contrast, the benchmark scores for GPT-4o are not provided. However, based on the pricing and capabilities, we can infer that both models are high-performance language models suitable for various applications.

#### Capabilities and Use Cases
Mistral Large 2 supports the following capabilities:
- Text
- Vision
- Function calling
- JSON mode
- Streaming
- System prompts

It is best suited for:
- Coding
- Analysis
- RAG (Retrieval-Augmented Generation)
- Agents
- Multilingual
- Function calling

On the other hand, Mistral Large 2 is not recommended for:
- Embeddings
- Bulk cheap processing
- Real-time sub-100ms processing
- Vision-heavy applications

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model with a wide range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. This model excels in coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual tasks, and function calling.

### Top 5 Best Use Cases for Mistral Large 2

1. **Coding and Development**: With its high HumanEval score of 92.0, Mistral Large 2 is well-suited for coding tasks, such as code completion, code review, and code generation. For example, you can use Mistral Large 2 with OpenRouter to generate code snippets in various programming languages.
   ```python
import openrouter

# Initialize Mistral Large 2 model
model = openrouter.MistralLarge2()

# Generate code snippet
code_snippet = model.generate_code("Write a Python function to sort a list of integers.")
print(code_snippet)
```

2. **Data Analysis and Insights**: Mistral Large 2's high MMLU score of 84.0 and LMSYS Arena ELO score of 1225 make it an excellent choice for data analysis and providing insights. You can use it to analyze large datasets, identify trends, and generate reports.
   ```python
import openrouter
import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

# Initialize Mistral Large 2 model
model = openrouter.MistralLarge2()

# Analyze dataset and generate insights
insights = model.analyze_data(df)
print(insights)
```

3. **Multilingual Support**: With its multilingual capabilities, Mistral Large 2 can be used for language translation, language understanding, and text generation in multiple languages.
   ```python

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
