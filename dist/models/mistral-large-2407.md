# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-07
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed for a wide range of applications, including coding, analysis, and multilingual support. This model boasts a context window of 131,072 tokens and can generate up to 4,096 tokens as output. With a knowledge cutoff of 2024-07, Mistral Large 2 is equipped with the latest information available up to that point. Its architecture supports various capabilities such as text and vision processing, function calling, JSON mode, streaming, and system prompts.

### Technical Strengths and Use Cases
The technical strengths of Mistral Large 2 are underscored by its impressive benchmark scores: MMLU at 84.0, HumanEval at 92.0, LMSYS Arena ELO at 1225, and GSM8K at 93.0. These scores indicate the model's high performance in coding, problem-solving, and language understanding tasks. Mistral Large 2 is best suited for applications requiring advanced coding capabilities, in-depth analysis, and the ability to handle multiple languages. It also supports function calling and can be used in scenarios where interaction with external systems is necessary. However, it's not recommended for tasks that require embeddings, bulk processing at low costs, real-time responses under 100ms, or vision-heavy applications.

### Pricing and Cost Considerations
The pricing model for Mistral Large 2 is based on input and output tokens, with costs of $3.0 per 1M input tokens and $9.0 per 1M output tokens. There are no specified costs for cached input or batch input. To give developers a better understanding of the costs involved, examples are provided: 1,000 calls averaging 500 tokens each would cost $6.0, scaling up to $60.0 for 10,000 calls and

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $3.0 |
| Output | $9.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Mistral Large 2
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium model released on 2024-07-24. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale for this model.

#### Cost Structure
The pricing for Mistral Large 2 is as follows:
- **Input**: $3.0 per 1M tokens
- **Output**: $9.0 per 1M tokens
- **Cached Input**: $None per 1M tokens (indicating no additional cost for cached inputs)
- **Batch Input**: $None per 1M tokens (suggesting no specific discount for batched inputs, but costs are calculated based on input and output tokens)

#### Optimal Usage Scenarios
- **Cached Tokens**: Since there is no additional cost for cached input tokens, it is highly beneficial to utilize cached tokens whenever possible to minimize input costs.
- **Batch API Savings**: Although there is no direct pricing discount mentioned for batch inputs, processing requests in batches can help reduce the overall number of API calls, thereby indirectly saving on costs associated with input and output tokens.

#### Cost at Scale
Given the average cost examples:
- **1,000 calls (avg 500 tokens)**: $6.0
- **10,000 calls**: $60.0
- **100,000 calls**: $600.0

We can infer the cost per call and the economies of scale:
- For 1,000 calls, the cost per call is $6.0 / 1,000 = $0.006 per call.
- For 10,000 calls, the cost per call is $60.0 / 10,000 = $0.006 per call.
- For 100,000 calls, the cost per call is $600.0 / 100,000 = $0.006 per call

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
These benchmark scores suggest that the Mistral Large 2 model is:
* Suitable for coding and analysis tasks, with a high HumanEval score indicating strong programming abilities.
* Effective in multilingual and function-calling applications, given its high MMLU and GSM8K scores.
* Less suitable for embeddings, bulk cheap processing, real-time sub-100ms applications, and vision-heavy tasks.

#### Cost Analysis
The model's pricing is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Example costs:
	+ 1,000 calls (avg 500 tokens): $6.0

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, a premium model offered by Mistral AI, is a powerful language model with a wide range of capabilities, including text, vision, function calling, and more. Released on 2024-07-24, it is a strong contender in the market, with a context window of 131,072 tokens and a maximum output of 4,096 tokens. In this comparison, we will pit Mistral Large 2 against its top competitor, GPT-4o, and explore the price differences, performance trade-offs, and use cases for each model.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, while GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. This means that for input-heavy workloads, GPT-4o is 16.7% cheaper, while for output-heavy workloads, Mistral Large 2 is 10% cheaper.

#### Performance Comparison
Mistral Large 2 has a strong set of benchmark scores:
* MMLU: 84.0
* HumanEval: 92.0
* LMSYS Arena ELO: 1225
* GSM8K: 93.0

While the benchmark scores for GPT-4o are not provided, we can assume that it is a strong competitor given its pricing. However, based on the available data, Mistral Large 2 appears to have a strong performance profile, making it suitable for tasks such as coding, analysis, and function calling.

#### Capabilities and Use Cases
Mistral Large 2 has a wide range of capabilities, including:
* Text
* Vision
* Function calling
* JSON mode
* Streaming
* System prompts

It is best suited for tasks such as:
* Coding
* Analysis
* RAG (Retrieval-Augmented Generation)
* Agents
*

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model with a wide range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. This model excels in coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual tasks, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Given its capabilities and limitations, here are the top 5 best use cases for Mistral Large 2, along with specific code integration examples mentioning OpenRouter:

1. **Coding and Development**: Mistral Large 2's high performance in coding tasks (as indicated by its HumanEval score of 92.0) makes it an excellent choice for coding assistance, code review, and automated code generation.
   ```python
   import openrouter
   model = openrouter.load_model("mistralai/mistral-large-2407")
   def generate_code(prompt):
       response = model.generate(prompt, max_tokens=4096)
       return response
   print(generate_code("Write a Python function to sort a list of integers"))
   ```
2. **Complex Analysis and Reasoning**: With a context window of 131,072 tokens and high scores in MMLU (84.0) and GSM8K (93.0), Mistral Large 2 is well-suited for complex analysis and reasoning tasks, such as answering multi-step questions or providing detailed explanations.
   ```python
   import openrouter
   model = openrouter.load_model("mistralai/mistral-large-2407")
   def analyze_text(prompt):
       response = model.generate(prompt, max_tokens=4096)
       return response
   print(analyze_text("Explain the implications of climate change on global food production"))
   ```
3. **Multilingual Support**:

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
