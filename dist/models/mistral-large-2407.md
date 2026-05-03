# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-03
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly excelling in coding, analysis, and function calling tasks. With a context window of 131,072 tokens and a maximum output of 4,096 tokens, this model is well-suited for complex, high-level tasks that require extensive context understanding. Its capabilities include text and vision processing, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Strengths and Use Cases
Mistral Large 2 boasts impressive benchmarks, including an MMLU score of 84.0, HumanEval score of 92.0, LMSYS Arena ELO of 1225, and a GSM8K score of 93.0. These metrics underscore its strength in coding and analytical tasks. The model is best utilized for applications such as coding assistance, in-depth analysis, and tasks that require the integration of external functions. However, it is not recommended for tasks that require embeddings, bulk processing at low costs, real-time responses under 100ms, or vision-heavy applications. With pricing set at $3.0 per 1M input tokens and $9.0 per 1M output tokens, developers can expect to pay $6.0 for 1,000 calls averaging 500 tokens, scaling up to $600.0 for 100,000 calls.

### Pricing and Competitiveness
In comparison to its top competitors, such as GPT-4o which offers input at $2.5/1M and output at $10.0/1M, Mistral Large 2 positions itself competitively in the premium model market. The pricing strategy, combined with its technical capabilities and benchmark performance, makes Mistral Large 2 an attractive option for developers

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

This indicates that using cached inputs can significantly reduce costs, as there is no charge for them. Similarly, batch inputs are also free, which can lead to substantial savings when making multiple API calls.

#### When to Use Cached Tokens
Cached tokens should be utilized whenever possible to minimize costs. Since there is no charge for cached inputs, leveraging this feature can lead to significant cost savings, especially for applications with repetitive or similar input patterns.

#### Batch API Savings
The fact that batch inputs are free suggests that making API calls in batches can lead to substantial cost savings. By batching API requests, users can avoid the input costs associated with individual calls, which can lead to significant reductions in overall expenses.

#### Cost at Scale
To understand the cost implications of using Mistral Large 2 at scale, let's examine the provided cost examples:
- **1,000 calls (avg 500 tokens)**: $6.0
- **10,000 calls**: $60.0
- **100,000 calls**: $600.0

These examples illustrate a linear cost scaling, where the cost increases directly with the number of API calls. This suggests that the cost per call remains constant, regardless of the scale.

####

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
The Mistral Large 2 model, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. It has a context window of 131,072 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2024-07.

#### Pricing
The pricing for Mistral Large 2 is as follows:
* Input: **$3.0 per 1M tokens**
* Output: **$9.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Benchmark Performance
The model's benchmark performance is measured by the following scores:
* **MMLU: 84.0** - The MMLU (Massive Multitask Language Understanding) score evaluates a model's ability to perform a wide range of natural language processing tasks. A higher score indicates better performance.
* **HumanEval: 92.0** - The HumanEval score assesses a model's ability to generate code that is correct and functional. A higher score indicates better coding capabilities.
* **LMSYS Arena ELO: 1225** - The LMSYS Arena ELO score measures a model's performance in a competitive environment, where it is pitted against other models. A higher score indicates better overall performance.
* **GSM8K: 93.0** - The GSM8K score evaluates a model's ability to solve math problems. A higher score indicates better math reasoning capabilities.

#### Real-World Implications
The benchmark scores indicate that Mist

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. This comparison will focus on its pricing, performance, and capabilities relative to its top competitors, specifically GPT-4o.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, whereas GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. This indicates that while GPT-4o is cheaper for input, Mistral Large 2 is more cost-effective for output.

#### Performance Trade-offs
Mistral Large 2 has the following benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

These scores indicate strong performance across various tasks. However, without direct comparison benchmarks for GPT-4o in the provided data, it's challenging to make a direct performance comparison. Generally, higher benchmark scores suggest better model performance.

#### Capabilities and Use Cases
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

However, it is not recommended for:
- Embeddings
- Bulk cheap operations
- Real-time operations under 100ms
- Vision-heavy tasks

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100,000 calls: $

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model that excels in various tasks, including coding, analysis, and function calling. With its extensive capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, it is an ideal choice for complex applications.

### Top 5 Best Use Cases for Mistral Large 2
Given its strengths and pricing model, here are the top 5 best use cases for Mistral Large 2, along with specific code integration examples mentioning OpenRouter:

1. **Coding and Software Development**: Mistral Large 2's high performance in coding tasks, as evidenced by its HumanEval score of 92.0, makes it suitable for applications like code completion, code review, and automated coding.
   ```python
   # Example of using Mistral Large 2 with OpenRouter for code completion
   import openrouter
   model = openrouter.load_model("mistralai/mistral-large-2407")
   prompt = "Complete the following code: def greet(name: str) -> None:"
   response = model.generate_text(prompt, max_tokens=100)
   print(response)
   ```

2. **Complex Data Analysis**: With its ability to handle large context windows (up to 131,072 tokens) and its high MMLU score of 84.0, Mistral Large 2 is well-suited for complex data analysis tasks, such as analyzing large datasets or generating detailed reports.
   ```python
   # Example of using Mistral Large 2 with OpenRouter for data analysis
   import openrouter
   import pandas as pd
   model = openrouter.load_model("mistralai/mistral-large-2407")
   data = pd.read_csv("data.csv")
   prompt = "Analyze the following data and provide insights:

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
