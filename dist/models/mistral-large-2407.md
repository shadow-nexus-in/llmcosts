# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-07
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly in coding, analysis, and multilingual tasks. This model boasts a context window of 131,072 tokens and can generate up to 4,096 tokens as output. With its capabilities extending to text, vision, function calling, JSON mode, streaming, and system prompts, Mistral Large 2 is positioned as a versatile tool for developers seeking advanced AI functionalities.

### Technical Strengths and Use Cases
The architecture of Mistral Large 2 is underpinned by its robust benchmark scores, including an MMLU score of 84.0, HumanEval score of 92.0, LMSYS Arena ELO of 1225, and a GSM8K score of 93.0. These metrics indicate the model's proficiency in handling complex tasks, coding challenges, and analytical queries. Its primary use cases include coding assistance, in-depth analysis, and applications requiring the integration of multiple functionalities such as text and vision processing. However, it's noted that Mistral Large 2 is not ideal for tasks requiring embeddings, bulk processing at low costs, real-time responses under 100ms, or vision-heavy applications.

### Pricing and Cost Considerations
The pricing for Mistral Large 2 is structured as follows: $3.0 per 1M input tokens and $9.0 per 1M output tokens. There are no specified costs for cached input or batch input. For developers, this translates to $6.0 for 1,000 calls averaging 500 tokens, $60.0 for 10,000 calls, and $600.0 for 100,000 calls. In comparison to its top competitor, GPT-4o, which charges $2.5/1M input and $

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
Mistral Large 2 is a premium model provided by Mistral AI, released on 2024-07-24. This analysis will break down the cost structure, provide guidance on when to use cached tokens, discuss batch API savings, and examine the cost at scale for 1,000, 10,000, and 100,000 API calls.

#### Cost Structure
The pricing for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### Using Cached Tokens
Cached input tokens are free, making them an attractive option for repetitive or similar inputs. If your application involves a high volume of identical or similar input queries, utilizing cached tokens can significantly reduce costs.

#### Batch API Savings
Batch input is also free, which means that submitting multiple inputs in a single API call does not incur additional costs. This can lead to significant savings, especially for applications that require processing large volumes of data in parallel.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* 1,000 calls (avg 500 tokens): $6.0
* 10,000 calls: $60.0
* 100,000 calls: $600.0

To put these costs into perspective, let's calculate the cost per token:
* Assuming an average of 500 tokens per call, 1,000 calls would involve 500,000 tokens.
* At $6.0 for 1,000 calls, the cost per token would be $6.0 / 500,000 tokens = $0.000012 per token.
* Similarly, for 10,000 calls and 100,000

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
* **MMLU (Massive Multitask Language Understanding)**: 84.0, indicating the model's ability to understand and process natural language across a wide range of tasks.
* **HumanEval**: 92.0, measuring the model's ability to evaluate and execute human-written code, with a high score indicating strong coding capabilities.
* **LMSYS Arena ELO**: 1225, representing the model's competitive performance in a large-scale language model benchmark, with higher scores indicating better performance.
* **GSM8K**: 93.0, evaluating the model's math problem-solving abilities, with higher scores indicating stronger mathematical reasoning.

#### Real-World Implications
These benchmark scores suggest that the Mistral Large 2 model is well-suited for:
* **Coding tasks**: With a high HumanEval score, the model excels in coding-related tasks, making it a strong choice for applications that require code generation, analysis, or execution.
* **Analysis and reasoning**: The model's strong MMLU and GSM8K scores indicate its ability to understand and process complex natural language and mathematical concepts, making it suitable for tasks that require in-depth analysis and reasoning.
* **Multilingual applications**: As the model is capable of handling multiple languages, it can be used in applications

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, a premium model by Mistral AI, offers a unique set of capabilities and performance metrics. This comparison will delve into the details of Mistral Large 2 and its top competitor, GPT-4o, highlighting price differences, performance trade-offs, and scenarios where each model is best suited.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, whereas GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. This indicates that GPT-4o is cheaper for input tokens but more expensive for output tokens.

#### Performance Comparison
Mistral Large 2 boasts impressive benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

While the benchmark scores for GPT-4o are not provided, the performance of Mistral Large 2 suggests it is a high-performing model.

#### Capabilities and Limitations
Mistral Large 2 supports a range of capabilities, including:
- Text
- Vision
- Function calling
- JSON mode
- Streaming
- System prompts

It is best suited for tasks such as:
- Coding
- Analysis
- RAG
- Agents
- Multilingual
- Function calling

However, it is not recommended for:
- Embeddings
- Bulk cheap tasks
- Real-time sub 100ms tasks
- Vision-heavy tasks

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100,000 calls: $600.0

#### Choosing the Right Model
Based on the comparison, Mistral Large 2 is a

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model that excels in various tasks, including coding, analysis, and function calling. With its impressive benchmarks, such as an MMLU score of 84.0 and a HumanEval score of 92.0, this model is well-suited for complex applications.

### Top 5 Best Use Cases for Mistral Large 2
Based on its capabilities and limitations, here are the top 5 best use cases for Mistral Large 2:

1. **Coding and Software Development**: With its high HumanEval score, Mistral Large 2 is ideal for coding tasks, such as code completion, code review, and code generation. For example, you can use Mistral Large 2 with OpenRouter to generate code snippets in various programming languages.
   ```python
import openrouter

# Initialize Mistral Large 2 model
model = openrouter.MistralLarge2()

# Generate code snippet
code_snippet = model.generate_code("Write a Python function to sort a list of integers.")
print(code_snippet)
```

2. **Data Analysis and Insights**: Mistral Large 2's analysis capabilities make it suitable for data analysis tasks, such as data visualization, trend identification, and predictive modeling. You can use Mistral Large 2 to analyze large datasets and provide actionable insights.
   ```python
import pandas as pd
import openrouter

# Load dataset
df = pd.read_csv("data.csv")

# Initialize Mistral Large 2 model
model = openrouter.MistralLarge2()

# Analyze dataset
insights = model.analyze_data(df)
print(insights)
```

3. **RAG (Retrieve, Augment, Generate) Tasks**: Mistral Large 2's capabilities in text and function calling make it well-suited for R

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
