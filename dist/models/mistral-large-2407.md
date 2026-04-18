# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-18
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly in coding, analysis, and function calling. With its robust architecture, Mistral Large 2 boasts a context window of 131,072 tokens and can generate up to 4,096 tokens as output. This model is part of the Mistral AI suite, specifically `mistralai/mistral-large-2407`, and is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens.

### Technical Strengths and Use Cases
Mistral Large 2 demonstrates its technical prowess through impressive benchmarks: an MMLU score of 84.0, HumanEval score of 92.0, LMSYS Arena ELO of 1225, and a GSM8K score of 93.0. These metrics highlight the model's capabilities in text and vision tasks, as well as its proficiency in function calling, JSON mode, streaming, and system prompts. It is best utilized for coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual tasks, and function calling. However, it is not recommended for embeddings, bulk cheap processing, real-time applications requiring sub-100ms responses, or vision-heavy tasks.

### Pricing and Competitiveness
The pricing model for Mistral Large 2 is structured around input and output tokens, with no specified costs for cached or batch inputs. For example, 1,000 calls averaging 500 tokens each would cost $6.0, scaling up to $60.0 for 10,000 calls and $600.0 for 100,000 calls. In comparison to its competitors, such as GPT-4o which is priced at $2.5/1M input and $

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
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. The pricing structure is based on input and output tokens, with specific rates for cached and batch inputs.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
* Input: **$3.0 per 1M tokens**
* Output: **$9.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### Using Cached Tokens
Cached input tokens are free, making it an attractive option for applications where input data can be reused. This can significantly reduce costs for use cases with repetitive input patterns.

#### Batch API Savings
Batch input is also free, which means that making API calls in batches does not incur additional input costs. However, output costs still apply. To maximize savings, it's essential to optimize batch sizes to minimize output tokens while taking advantage of free batch inputs.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* **1,000 API calls** (avg 500 tokens): **$6.0**
* **10,000 API calls**: **$60.0**
* **100,000 API calls**: **$600.0**

These costs are based on the provided examples and can serve as a reference for estimating the cost of using Mistral Large 2 for specific use cases.

#### Comparison with Competitors
Mistral Large 2's pricing is competitive, especially considering its capabilities and performance benchmarks (MMLU: 84.0, HumanEval: 92.0, LMSYS Arena ELO: 

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
* **MMLU (Massive Multitask Language Understanding)**: 84.0, indicating the model's ability to understand and generate human-like text across a wide range of tasks and topics.
* **HumanEval**: 92.0, measuring the model's ability to write correct and functional code in response to programming prompts.
* **LMSYS Arena ELO**: 1225, representing the model's competitive performance in a large-scale language model benchmarking arena.
* **GSM8K**: 93.0, evaluating the model's math problem-solving abilities.

#### Real-World Implications
These benchmark scores have significant implications for real-world use cases:
* The high **HumanEval** score suggests that Mistral Large 2 is well-suited for coding tasks, such as code completion, code review, and programming assistance.
* The strong **MMLU** score indicates that the model can handle a wide range of natural language processing tasks, including text analysis, sentiment analysis, and text generation.
* The **LMSYS Arena ELO** score demonstrates the model's competitive performance in a large-scale benchmarking arena, suggesting that it can handle complex and challenging tasks.

#### Capabilities and Limitations
Mistral Large 2 has the following capabilities:
* **Text

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts, making it suitable for applications such as coding, analysis, and multilingual tasks.

#### Pricing Comparison
The pricing for Mistral Large 2 is as follows:
- Input: $3.0 per 1M tokens
- Output: $9.0 per 1M tokens

In comparison, GPT-4o, a top competitor, is priced at:
- Input: $2.5 per 1M tokens
- Output: $10.0 per 1M tokens

Mistral Large 2 is more expensive than GPT-4o in terms of input tokens but slightly cheaper in terms of output tokens.

#### Performance Trade-offs
Mistral Large 2 has the following benchmarks:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

While the specific benchmarks for GPT-4o are not provided, the choice between Mistral Large 2 and GPT-4o may depend on the specific use case and the importance of these benchmarks for the application.

#### Context and Limits
Mistral Large 2 has a context window of 131,072 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2024-07. These limits may influence the choice of model depending on the requirements of the application.

#### Capabilities and Best Use Cases
Mistral Large 2 is best suited for tasks such as:
- Coding
- Analysis
- RAG (Retrieve, Augment, Generate)
- Agents
- Multilingual tasks
- Function calling

It is not recommended for:
- Embeddings
- Bulk cheap tasks
- Real-time tasks requiring responses under 100ms
- Vision-heavy tasks

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100,000 calls: $600

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium model released on 2024-07-24. With its capabilities in text, vision, function calling, JSON mode, streaming, and system prompts, it is best suited for coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual tasks, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Based on its capabilities and benchmarks, here are the top 5 best use cases for Mistral Large 2:

1. **Coding and Software Development**: With a high HumanEval score of 92.0, Mistral Large 2 is well-suited for coding tasks such as code completion, code review, and code generation. For example, you can use Mistral Large 2 with OpenRouter to generate code snippets:
   ```python
import openrouter

# Initialize Mistral Large 2 model
model = openrouter.MistralLarge2()

# Define a coding prompt
prompt = "Write a Python function to calculate the area of a rectangle."

# Generate code using Mistral Large 2
code = model.generate_code(prompt)

print(code)
```

2. **Data Analysis and Insights**: Mistral Large 2's high MMLU score of 84.0 and LMSYS Arena ELO of 1225 make it a strong candidate for data analysis tasks such as data interpretation, trend analysis, and data visualization. You can use Mistral Large 2 with OpenRouter to analyze data and generate insights:
   ```python
import openrouter
import pandas as pd

# Initialize Mistral Large 2 model
model = openrouter.MistralLarge2()

# Load a sample dataset
data = pd.read_csv("sample_data.csv")

# Define an analysis prompt
prompt = "Analyze the trends in the data and provide insights."

# Generate analysis

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
