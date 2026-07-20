# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-20
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly in coding, analysis, and multilingual tasks. The model boasts an impressive architecture that supports capabilities such as text and vision processing, function calling, JSON mode, streaming, and system prompts. With a context window of 131,072 tokens and a maximum output of 4,096 tokens, Mistral Large 2 is well-suited for complex and data-intensive tasks.

### Technical Strengths and Use Cases
The technical strengths of Mistral Large 2 are evident in its benchmark scores, which include an MMLU score of 84.0, HumanEval score of 92.0, LMSYS Arena ELO of 1225, and a GSM8K score of 93.0. These scores indicate the model's high performance in various evaluation metrics. The model's primary use cases include coding, analysis, retrieval-augmented generation (RAG), agents, multilingual tasks, and function calling. However, it is not recommended for tasks that require embeddings, bulk cheap processing, real-time responses under 100ms, or vision-heavy applications.

### Pricing and Cost Considerations
The pricing for Mistral Large 2 is based on input and output tokens, with costs of $3.0 per 1M input tokens and $9.0 per 1M output tokens. There are no costs associated with cached input or batch input. For example, 1,000 calls with an average of 500 tokens would cost $6.0, while 10,000 calls would cost $60.0, and 100,000 calls would cost $600.0. In comparison to its top competitors, such as GPT-4o, which charges $2.5/1M input and $

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
Mistral Large 2, a premium model by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. The pricing structure is based on input and output tokens.

#### Cost Structure
The cost of using Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option when possible. Use cached tokens when:
* The input is repetitive or can be reused.
* The application allows for caching mechanisms.

#### Batch API Savings
Batch input is free, which can lead to significant savings when making multiple API calls. To maximize batch API savings:
* Group multiple requests together in a single API call.
* Ensure the batch size is optimized for the application's requirements.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* 1,000 API calls (avg 500 tokens): $6.0
* 10,000 API calls: $60.0
* 100,000 API calls: $600.0

To estimate the cost at scale, consider the average number of tokens per API call and the number of calls required.

#### Comparison to Top Competitors
Mistral Large 2's pricing is comparable to its top competitors. For example, GPT-4o charges $2.5 per 1M input tokens and $10.0 per 1M output tokens.

#### Conclusion
Mistral Large 2 offers a premium set of capabilities with a competitive pricing structure. By understanding

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
These benchmark scores suggest that Mistral Large 2 is a highly capable model, particularly in:
* **Coding and analysis**: With a high HumanEval score, the model is well-suited for coding tasks, such as generating code snippets or debugging existing code.
* **Multilingual support**: The model's high MMLU score implies strong performance across multiple languages.
* **Function calling and API interactions**: The model's support for function calling and JSON mode makes it a good fit for applications that require interacting with external APIs or services.

#### Cost Considerations
The pricing model for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens


## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. This comparison will focus on its pricing, performance, and use cases against its top competitor, GPT-4o.

#### Pricing Comparison
The pricing structure for Mistral Large 2 and GPT-4o is as follows:
* Mistral Large 2:
	+ Input: $3.0 per 1M tokens
	+ Output: $9.0 per 1M tokens
* GPT-4o:
	+ Input: $2.5 per 1M tokens
	+ Output: $10.0 per 1M tokens

Mistral Large 2 is more expensive than GPT-4o in terms of input costs, but slightly cheaper in terms of output costs.

#### Performance Trade-offs
The performance of both models can be evaluated using various benchmarks:
* Mistral Large 2:
	+ MMLU: 84.0
	+ HumanEval: 92.0
	+ LMSYS Arena ELO: 1225
	+ GSM8K: 93.0
* GPT-4o: Benchmark scores are not provided for direct comparison.

Given the available data, Mistral Large 2 demonstrates strong performance across multiple benchmarks, indicating its suitability for tasks such as coding, analysis, and function calling.

#### Context and Limits
The context window and output limits for Mistral Large 2 are:
* Context Window: 131,072 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2024-07

These specifications are not provided for GPT-4o, making direct comparison challenging. However, the context window and output limits of Mistral Large 2 suggest it is designed for handling complex, long-form inputs and generating substantial outputs.

#### Capabilities and Use Cases
Mistral Large 2 supports the following capabilities:
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
* Multilingual applications
* Function calling

Conversely, it is not recommended for:
* Embeddings
* Bulk

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model that excels in various tasks, including coding, analysis, and function calling. With its impressive benchmarks, such as an MMLU score of 84.0 and a HumanEval score of 92.0, it's a powerful tool for developers and researchers. This guide will explore the top 5 best use cases for Mistral Large 2, along with code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Large 2
#### 1. **Coding Assistance**
Mistral Large 2 is well-suited for coding tasks, thanks to its high HumanEval score. You can use it to generate code snippets, complete partially written code, or even debug existing code.
```python
import openrouter

# Initialize Mistral Large 2 model
model = openrouter.MistralLarge2()

# Generate code snippet
prompt = "Write a Python function to calculate the area of a rectangle."
response = model.generate(prompt)
print(response)
```

#### 2. **Text Analysis**
With its high MMLU score, Mistral Large 2 is capable of performing complex text analysis tasks, such as sentiment analysis, entity recognition, and text summarization.
```python
import openrouter

# Initialize Mistral Large 2 model
model = openrouter.MistralLarge2()

# Perform sentiment analysis
prompt = "Analyze the sentiment of the following text: 'I love using Mistral Large 2 for coding tasks.'"
response = model.generate(prompt)
print(response)
```

#### 3. **RAG (Retrieve, Augment, Generate) Tasks**
Mistral Large 2 supports RAG tasks, which involve retrieving information from a knowledge base, augmenting it with additional information, and generating a response.
```

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
