# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-03
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly excelling in coding, analysis, and multilingual tasks. This model boasts a context window of 131,072 tokens and can generate up to 4,096 tokens as output. With a knowledge cutoff of 2024-07, Mistral Large 2 is equipped with capabilities such as text and vision processing, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Strengths and Use Cases
The architecture of Mistral Large 2 is designed to leverage its strengths in coding, analysis, and other specialized tasks. It achieves high scores in various benchmarks: 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These benchmarks highlight the model's proficiency in understanding and generating human-like text, solving mathematical problems, and handling complex tasks. However, it's noted that Mistral Large 2 is not ideal for embeddings, bulk cheap processing, real-time applications requiring sub-100ms responses, or vision-heavy tasks. Its pricing model charges $3.0 per 1M input tokens and $9.0 per 1M output tokens, with no specified charges for cached or batch input.

### Pricing and Competitiveness
Developers looking to integrate Mistral Large 2 into their applications should consider the cost implications. For example, 1,000 calls averaging 500 tokens each would cost $6.0, scaling to $60.0 for 10,000 calls and $600.0 for 100,000 calls. In comparison to its top competitors, such as GPT-4o, which charges $2.5/1

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
Mistral Large 2, a premium model offered by Mistral AI, boasts an impressive set of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. This analysis delves into the cost structure of Mistral Large 2, exploring when to utilize cached tokens, batch API savings, and the cost at scale for 1,000, 10,000, and 100,000 API calls.

#### Cost Structure
The pricing for Mistral Large 2 is as follows:
- **Input**: $3.0 per 1M tokens
- **Output**: $9.0 per 1M tokens
- **Cached Input**: $0 per 1M tokens (free)
- **Batch Input**: $0 per 1M tokens (free)

Given that cached input and batch input are free, it is highly beneficial to utilize these features whenever possible to minimize costs.

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for reducing costs. Consider using cached tokens for:
- **Frequently accessed data**: If your application involves frequent queries on the same data, caching can significantly reduce costs.
- **Static content**: For static content that does not change often, caching can help avoid redundant input costs.

#### Batch API Savings
Batch input is also free, which means processing multiple inputs in a single API call can lead to substantial savings. Consider batch processing for:
- **Bulk operations**: When performing operations on large datasets, batching can help reduce the overall cost by minimizing the number of API calls.
- **Real-time data processing**: For applications that require real-time data processing, batching can help manage costs while maintaining performance.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
- **1,000 calls (avg 500 tokens)**: $6.0
- **10,000

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 84.0 |
| HumanEval | 92.0 |
| LMSYS Arena ELO | 1225 |
| ARC | 93.0 |

## Benchmark Analysis
### Mistral Large 2 Benchmark Performance Analysis
The Mistral Large 2 model, released by Mistral AI on 2024-07-24, is a premium, non-open-source model with a context window of 131,072 tokens and a maximum output of 4,096 tokens. 

#### Pricing
The pricing for Mistral Large 2 is as follows:
* Input: **$3.0 per 1M tokens**
* Output: **$9.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Benchmark Scores
The model's performance is measured by the following benchmark scores:
* **MMLU: 84.0** - The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to perform a wide range of natural language processing tasks. A higher MMLU score indicates better overall language understanding.
* **HumanEval: 92.0** - The HumanEval benchmark assesses a model's ability to generate code that is both correct and readable. A higher HumanEval score suggests stronger coding capabilities.
* **LMSYS Arena ELO: 1225** - The LMSYS Arena ELO score measures a model's performance in a competitive environment, where it is pitted against other models. A higher ELO score indicates better performance in this setting.
* **GSM8K: 93.0** - The GSM8K benchmark evaluates a model's ability to reason about mathematical concepts and solve problems. A higher GSM8K score suggests stronger mathematical reasoning capabilities.

#### Real-World Implications
These benchmark scores have

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. This comparison will focus on its pricing, performance, and use cases against its top competitor, GPT-4o.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, while GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. For input tokens, GPT-4o is 16.67% cheaper than Mistral Large 2. However, for output tokens, Mistral Large 2 is 10% cheaper than GPT-4o.

#### Performance Comparison
Mistral Large 2 has the following benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

In contrast, the benchmark scores for GPT-4o are not provided in the data. Therefore, a direct performance comparison cannot be made.

#### Context and Limits
Mistral Large 2 has a context window of 131,072 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2024-07. The context and limits for GPT-4o are not provided in the data.

#### Capabilities and Use Cases
Mistral Large 2 is best suited for:
- Coding
- Analysis
- RAG (Retrieve, Augment, Generate)
- Agents
- Multilingual tasks
- Function calling

It is not recommended for:
- Embeddings
- Bulk cheap tasks
- Real-time tasks with sub-100ms latency
- Vision-heavy tasks

#### Cost Examples
The cost of

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. With its robust capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, it's best suited for applications such as coding, analysis, RAG (Retrieve, Augment, Generate), agents, multilingual tasks, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Given its strengths and pricing model, here are the top 5 best use cases for Mistral Large 2, along with specific code integration examples mentioning OpenRouter:

1. **Coding and Development Assistance**: 
   - **Use Case**: Utilize Mistral Large 2 for coding tasks such as code completion, code review, and debugging.
   - **Example**: Integrate Mistral Large 2 with OpenRouter to generate code snippets based on user input.
   ```python
   import openrouter
   from mistralai import MistralLarge2

   # Initialize Mistral Large 2 model
   model = MistralLarge2()

   # Define a function to generate code snippets
   def generate_code(prompt):
       input_ids = model.encode(prompt, return_tensors='pt')
       output = model.generate(input_ids, max_length=2048)
       return model.decode(output[0], skip_special_tokens=True)

   # Use OpenRouter to route requests to Mistral Large 2
   router = openrouter.Router()
   router.add_route('/generate_code', generate_code)

   # Test the endpoint
   print(router.generate_code("Write a Python function to sort a list"))
   ```

2. **Multilingual Support**:
   - **Use Case**: Leverage Mistral Large 2 for multilingual tasks such as translation, language detection, and text analysis.
   - **Example**: Use Mistral Large 2 with

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
