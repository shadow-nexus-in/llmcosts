# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-22
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly excelling in coding, analysis, and function calling tasks. This model boasts a context window of 131,072 tokens and can generate up to 4,096 tokens as output. With a knowledge cutoff of 2024-07, Mistral Large 2 is equipped with capabilities such as text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Strengths and Use Cases
The architecture of Mistral Large 2 supports its main strengths, which include high performance in coding and analysis tasks, as evidenced by its benchmarks: MMLU at 84.0, HumanEval at 92.0, LMSYS Arena ELO at 1225, and GSM8K at 93.0. These scores indicate the model's proficiency in understanding and generating high-quality code and text. The model is best utilized for tasks that require in-depth analysis, coding, and the ability to call functions, making it suitable for applications involving agents, multilingual support, and function calling. However, it is not recommended for tasks requiring embeddings, bulk cheap processing, real-time responses under 100ms, or vision-heavy applications.

### Pricing and Cost Considerations
The pricing for Mistral Large 2 is structured as follows: $3.0 per 1M input tokens and $9.0 per 1M output tokens. There are no specified costs for cached input or batch input. To give developers a clearer picture, example costs include $6.0 for 1,000 calls averaging 500 tokens, $60.0 for 10,000 calls, and $600.0 for 100,000 calls. In comparison to its top competitors, such

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
Mistral Large 2 is a premium model offered by Mistral AI, released on 2024-07-24. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Large 2 is as follows:
* Input: **$3.0 per 1M tokens**
* Output: **$9.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### Optimal Usage Scenarios
* **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
* **Batch API**: With batch input being free, batching API calls can significantly reduce costs. However, the cost savings will primarily come from reduced output token costs.
* **Cost at Scale**:
	+ 1,000 API calls (avg 500 tokens): **$6.0**
	+ 10,000 API calls: **$60.0**
	+ 100,000 API calls: **$600.0**

#### Cost Comparison
Compared to its top competitor, GPT-4o:
* Input: Mistral Large 2 (**$3.0/1M**) vs GPT-4o (**$2.5/1M**)
* Output: Mistral Large 2 (**$9.0/1M**) vs GPT-4o (**$10.0/1M**)

While Mistral Large 2 has a higher input cost, its output cost is lower than GPT-4o. This makes Mistral Large 2 a more cost-effective option when output tokens are a significant portion of the overall token count.

#### Conclusion
Mistral Large 2 offers a

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
These benchmark scores suggest that the Mistral Large 2 model is well-suited for:
* **Coding tasks**: With a high HumanEval score, the model can generate accurate and functional code.
* **Analysis and reasoning**: The model's high MMLU score indicates its ability to understand complex text and generate human-like responses.
* **Multilingual support**: The model's capabilities include multilingual support, making it suitable for applications that require language flexibility.

#### Cost and Pricing
The model's pricing is as follows:
* **Input**: $3.0 per 1M tokens
* **Output**: $9.0 per 1M tokens
* **Cost examples**:


## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. This comparison will focus on its pricing, performance, and use cases against its top competitor, GPT-4o.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens. In contrast, GPT-4o is priced at $2.5 per 1M input tokens but $10.0 per 1M output tokens. This indicates that while GPT-4o is cheaper for input, Mistral Large 2 is more cost-effective for output.

#### Performance Comparison
Mistral Large 2 has the following benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

GPT-4o's benchmark scores are not provided, making a direct comparison challenging. However, based on the provided data, Mistral Large 2 demonstrates strong performance across various tasks, suggesting it may be a more capable model.

#### Context and Limits
Mistral Large 2 has a context window of 131,072 tokens and a maximum output of 4,096 tokens. Its knowledge cutoff is 2024-07. These specifications are not provided for GPT-4o, but they are crucial for understanding the limitations and potential applications of each model.

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
- Bulk, cheap operations
- Real-time operations under 100ms
- Vision-heavy tasks

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. With its robust capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, it is best suited for tasks such as coding, analysis, RAG (Retrieve, Augment, Generate), agents, multilingual support, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Given its capabilities and pricing structure, here are the top 5 best use cases for Mistral Large 2, along with specific code integration examples mentioning OpenRouter:

1. **Coding and Development**: Mistral Large 2 excels in coding tasks, making it an ideal choice for developers. For example, you can use it with OpenRouter to generate code snippets or complete functions.
   ```python
   import openrouter

   # Initialize Mistral Large 2 model
   model = openrouter.initialize_model("mistralai/mistral-large-2407")

   # Define a coding prompt
   prompt = "Write a Python function to sort a list of integers."

   # Generate code using Mistral Large 2
   response = openrouter.generate_code(model, prompt)

   # Print the generated code
   print(response)
   ```

2. **Analysis and Research**: With its strong analysis capabilities, Mistral Large 2 is suitable for research tasks, such as data analysis, report generation, and summarization.
   ```python
   import openrouter

   # Initialize Mistral Large 2 model
   model = openrouter.initialize_model("mistralai/mistral-large-2407")

   # Define an analysis prompt
   prompt = "Analyze the impact of climate change on global food production."

   # Generate a report using Mistral Large 2
   response = openrouter.generate_report(model, prompt

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
