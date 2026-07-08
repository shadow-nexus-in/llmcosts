# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-08
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Technical Overview of Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, including coding, analysis, and multilingual tasks. Architecturally, Mistral Large 2 boasts a context window of 131,072 tokens and can generate outputs of up to 4,096 tokens. This capability, combined with its knowledge cutoff of 2024-07, positions it as a robust tool for tasks requiring extensive contextual understanding and generation capabilities.

### Strengths and Use Cases
The main strengths of Mistral Large 2 lie in its versatility and performance. With capabilities such as text, vision, function calling, JSON mode, streaming, and system prompts, it is best suited for coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual tasks, and function calling. Its benchmark scores, including an MMLU of 84.0, HumanEval of 92.0, LMSYS Arena ELO of 1225, and GSM8K of 93.0, underscore its high performance across various tasks. However, it is not recommended for embeddings, bulk cheap processing, real-time applications requiring sub-100ms responses, or vision-heavy tasks.

### Pricing and Cost Considerations
Pricing for Mistral Large 2 is structured around input and output tokens, with costs of $3.0 per 1M input tokens and $9.0 per 1M output tokens. There are no specified costs for cached input or batch input. For developers, understanding these pricing dynamics is crucial for budgeting. For example, 1,000 calls averaging 500 tokens each would cost $6.0, scaling to $60.0 for 10,000 calls and $600.0 for 100,000 calls. In comparison to its top competitors, such as G

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
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral Large 2 is as follows:
- **Input**: $3.0 per 1M tokens
- **Output**: $9.0 per 1M tokens
- **Cached Input**: No additional cost per 1M tokens
- **Batch Input**: No additional cost per 1M tokens

#### Optimal Usage Scenarios
- **Cached Tokens**: Since there is no additional cost for cached input tokens, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
- **Batch API**: Although there is no direct cost savings mentioned for batch input, batching API calls can still lead to overall cost efficiency by reducing the number of API calls needed, thus indirectly saving on input token costs.

#### Cost at Scale
Given the average cost per call and total costs for different numbers of calls, we can analyze the cost structure further:
- **1,000 calls (avg 500 tokens)**: $6.0
- **10,000 calls**: $60.0
- **100,000 calls**: $600.0

These examples suggest a linear scaling of costs with the number of API calls, indicating that the cost per call remains constant regardless of the volume.

#### Comparison with Competitors
Mistral Large 2's pricing can be compared with its top competitors, such as GPT-4o, which charges $2.5/1M input and $10.0/1M output. While GPT-4o is cheaper on input costs, Mistral Large 2 offers a more competitive output pricing, which could be beneficial for applications with shorter output requirements

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
These benchmark scores have significant implications for real-world use cases:
* The high **HumanEval** score suggests that Mistral Large 2 is well-suited for coding tasks, such as code generation, code completion, and code review.
* The strong **MMLU** score indicates that the model can handle a wide range of natural language processing tasks, including text analysis, sentiment analysis, and text generation.
* The competitive **LMSYS Arena ELO** score demonstrates that Mistral Large 2 can perform well in large-scale language modeling tasks, such as conversational AI, chatbots, and language translation.

#### Capabilities and Limitations
Mistral Large 2 has

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. This comparison will focus on its pricing, performance, and capabilities in relation to its top competitor, GPT-4o.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, while GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. This indicates that GPT-4o offers a cheaper input option but a more expensive output option.

#### Performance Trade-offs
Mistral Large 2 has the following benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

In contrast, the benchmark scores for GPT-4o are not provided in the data. However, based on the pricing and capabilities, we can infer that Mistral Large 2 is designed for premium applications with high performance requirements.

#### Capabilities and Use Cases
Mistral Large 2 supports the following capabilities:
- text
- vision
- function_calling
- json_mode
- streaming
- system_prompts

It is best suited for:
- coding
- analysis
- rag
- agents
- multilingual
- function_calling

On the other hand, it is not recommended for:
- embeddings
- bulk_cheap
- real_time_sub_100ms
- vision_heavy

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100,000 calls: $600.0

#### Choosing Between Mistral Large 2 and GPT-4

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. With its robust capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, it is best suited for tasks such as coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual support, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Given its strengths and pricing structure, here are the top 5 best use cases for Mistral Large 2, along with practical advice and code integration examples mentioning OpenRouter:

1. **Coding and Development**: Mistral Large 2 excels in coding tasks, making it an ideal choice for developers looking to automate code generation, code review, or even assist in debugging processes.
   - **Example**: Using Mistral Large 2 with OpenRouter for automated code completion.
   ```python
   import openrouter

   # Initialize OpenRouter with Mistral Large 2
   model = openrouter.MistralLarge2()

   # Function to generate code based on a prompt
   def generate_code(prompt):
       response = model.generate(prompt)
       return response

   # Example usage
   prompt = "Write a Python function to sort a list in ascending order."
   print(generate_code(prompt))
   ```

2. **Complex Analysis and Report Generation**: For tasks that require in-depth analysis and the generation of comprehensive reports, Mistral Large 2's ability to process large context windows and its high performance on benchmarks like MMLU and GSM8K make it a strong candidate.
   - **Example**: Integrating Mistral Large 2 into an analysis pipeline to generate detailed reports based on large datasets.
   ```python
   # Assuming data is a large dataset
   data = ...

   # Function to analyze data and generate a

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
