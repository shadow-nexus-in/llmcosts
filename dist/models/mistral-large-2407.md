# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-12
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly excelling in coding, analysis, and multilingual tasks. This model boasts a context window of 131,072 tokens and can generate up to 4,096 tokens as output. With a knowledge cutoff of 2024-07, Mistral Large 2 is well-equipped to handle tasks that require extensive knowledge up to that point. Its architecture supports various capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts.

### Technical Strengths and Use Cases
Mistral Large 2 demonstrates its technical prowess through its performance in several benchmarks: achieving 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These scores underscore its suitability for tasks that involve complex reasoning, coding, and analysis. The model's capabilities in function calling, along with its support for multilingual tasks, make it an attractive choice for developers working on projects that require these specific functionalities. However, it's worth noting that Mistral Large 2 is not recommended for tasks that require embeddings, bulk processing at low costs, real-time responses under 100ms, or vision-heavy applications.

### Pricing and Cost Considerations
The pricing model for Mistral Large 2 is structured as follows: $3.0 per 1M tokens for input, $9.0 per 1M tokens for output, with no specified costs for cached input or batch input. To put these costs into perspective, for 1,000 calls averaging 500 tokens, the cost would be $6.0, scaling up to $60.0 for 10,000 calls and $600.0 for 100,000

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
Mistral Large 2 is a premium model offered by Mistral AI, released on 2024-07-24. This model is not open source and has a tier classification of premium.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
* Input: **$3.0 per 1M tokens**
* Output: **$9.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs when the same input is used multiple times. Since cached input is free, it is recommended to use cached tokens whenever possible to minimize costs.

#### Batch API Savings
Batch input is also free, which means that batching API calls can help reduce costs. By batching API calls, users can take advantage of the free batch input pricing to minimize costs.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* 1,000 calls (avg 500 tokens): **$6.0**
* 10,000 calls: **$60.0**
* 100,000 calls: **$600.0**

To calculate the cost at scale, we can use the following formula:
Cost = (Number of tokens * Input cost per token) + (Number of output tokens * Output cost per token)

For example, for 1,000 calls with an average of 500 tokens per call, the cost would be:
Cost = (500,000 tokens * $3.0/1M tokens) + (500,000 tokens * $9.0/1M tokens) = $6.0

#### Comparison to Top Competitors
Mistral Large 2 is priced competitively with top competitors such as

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
* **MMLU (Massive Multitask Language Understanding)**: 84.0, indicating the model's ability to understand and process a wide range of language tasks.
* **HumanEval**: 92.0, measuring the model's ability to generate human-like code and evaluate its coding capabilities.
* **LMSYS Arena ELO**: 1225, representing the model's competitive performance in a large-scale language model benchmarking arena.
* **GSM8K**: 93.0, assessing the model's math problem-solving skills.

#### Real-World Implications
These benchmark scores have significant implications for real-world use cases:
* The high **HumanEval** score suggests that Mistral Large 2 is well-suited for coding tasks, such as code generation, code completion, and code review.
* The strong **MMLU** score indicates that the model can handle a wide range of language tasks, including text analysis, sentiment analysis, and language translation.
* The competitive **LMSYS Arena ELO** score demonstrates the model's ability to perform well in large-scale language modeling tasks, such as text generation, summarization, and question answering.

#### Capabilities and Limitations
Mistral Large 2 has the following capabilities:
* **Text**: processing and generation

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. It offers a unique set of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. In this comparison, we will evaluate Mistral Large 2 against its top competitor, GPT-4o, focusing on pricing, performance, and use cases.

#### Pricing Comparison
The pricing for Mistral Large 2 and GPT-4o is as follows:
* Mistral Large 2:
	+ Input: $3.0 per 1M tokens
	+ Output: $9.0 per 1M tokens
* GPT-4o:
	+ Input: $2.5 per 1M tokens
	+ Output: $10.0 per 1M tokens

Mistral Large 2 is more expensive than GPT-4o in terms of input pricing, with a difference of $0.5 per 1M tokens. However, the output pricing for Mistral Large 2 is lower than GPT-4o, with a difference of $1.0 per 1M tokens.

#### Performance Comparison
The performance of Mistral Large 2 and GPT-4o can be evaluated based on various benchmarks:
* Mistral Large 2:
	+ MMLU: 84.0
	+ HumanEval: 92.0
	+ LMSYS Arena ELO: 1225
	+ GSM8K: 93.0
* GPT-4o: Not provided

Since the benchmark scores for GPT-4o are not available, a direct comparison is not possible. However, the scores for Mistral Large 2 indicate its strong performance in various tasks, including coding, analysis, and multilingual capabilities.

#### Capabilities and Use Cases
Mistral Large 2 offers a range of capabilities, including:
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
* Multilingual
* Function calling

On the other hand, it is not recommended for tasks that require:
* Embeddings
*

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts, making it suitable for tasks such as coding, analysis, and multilingual applications.

### Top 5 Best Use Cases for Mistral Large 2
Given its capabilities and pricing structure, here are the top 5 best use cases for Mistral Large 2:

1. **Coding and Development**: With its high scores in HumanEval (92.0) and GSM8K (93.0), Mistral Large 2 is well-suited for coding tasks, such as generating code snippets, debugging, and code review.
2. **Analysis and RAG (Retrieval-Augmented Generation)**: Its high context window (131,072 tokens) and ability to handle system prompts make it ideal for complex analysis tasks and RAG applications.
3. **Multilingual Support**: Mistral Large 2's support for multilingual applications makes it a great choice for projects that require text processing and generation in multiple languages.
4. **Function Calling and API Integration**: With its function calling capability, Mistral Large 2 can be integrated with external APIs and services, such as OpenRouter, to enhance its functionality and provide more comprehensive solutions.
5. **Agent-Based Systems**: Its ability to handle system prompts and streaming data makes it suitable for building agent-based systems that can interact with users and respond to changing conditions.

### Code Integration Example with OpenRouter
Here's an example of how to integrate Mistral Large 2 with OpenRouter using Python:
```python
import requests

# Set up OpenRouter API endpoint and credentials
openrouter_url = "https://api.openrouter.com/v1/"
api_key = "YOUR_API_KEY"

# Set up Mistral Large 2

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
