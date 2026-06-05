# OpenAI: GPT-5.4 Mini API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-05
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to OpenAI: GPT-5.4 Mini
The OpenAI: GPT-5.4 Mini model, released on 2024-01-01, is a standard-tier language model provided by OpenAI. This model is not open source. From an architectural standpoint, while specific details about its architecture are not provided, it is part of the GPT series, which is known for its transformer-based design. This architecture is particularly adept at handling sequential data like text, making it highly effective for a wide range of natural language processing tasks.

### Strengths and Use Cases
The OpenAI: GPT-5.4 Mini model boasts several key strengths, including its ability to handle text, function calling, JSON mode, streaming, and structured outputs. Its capabilities make it best suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization. With a context window of 400,000 tokens and a maximum output of 128,000 tokens, this model is designed to process and generate substantial amounts of text. The model's performance is further underscored by its benchmark scores, including an MMLU score of 94.0 and an LMSYS Arena ELO score of 1350. However, it's worth noting the model's knowledge cutoff is 2023-12, which may limit its applicability to very recent events or developments.

### Pricing and Cost Considerations
The pricing for the OpenAI: GPT-5.4 Mini model is structured around input and output tokens. Developers are charged $0.75 per 1 million input tokens and $4.5 per 1 million output tokens. There are no specified charges for cached input or batch input. To give developers a better understanding of the costs involved, examples are provided: 1,000 calls with an average of 500 tokens would cost $2.625, scaling up to $26.25 for 10,000

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.75 |
| Output | $4.5 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### OpenAI: GPT-5.4 Mini Pricing Analysis
#### Overview
The OpenAI: GPT-5.4 Mini model is a standard, non-open source language model released on January 1, 2024. This analysis will delve into the cost structure, usage scenarios, and scalability of this model.

#### Cost Structure
The pricing for OpenAI: GPT-5.4 Mini is as follows:
* **Input**: $0.75 per 1 million tokens
* **Output**: $4.5 per 1 million tokens
* **Cached Input**: No additional cost per 1 million tokens
* **Batch Input**: No additional cost per 1 million tokens

#### Usage Scenarios
* **Cached Tokens**: Since there is no additional cost for cached input tokens, it is recommended to use cached tokens whenever possible to minimize costs.
* **Batch API Savings**: Although there is no explicit discount for batch API calls, making batch requests can still reduce the overall cost by minimizing the number of API calls.

#### Cost at Scale
The cost of using OpenAI: GPT-5.4 Mini at scale is as follows:
* **1,000 API calls** (avg 500 tokens): $2.625
* **10,000 API calls**: $26.25
* **100,000 API calls**: $262.5

These costs demonstrate a linear scaling of expenses with the number of API calls.

#### Context and Limits
It's essential to consider the context window and output limits when using this model:
* **Context Window**: 400,000 tokens
* **Max Output**: 128,000 tokens
* **Knowledge Cutoff**: December 2023

#### Capabilities and Best Use Cases
OpenAI: GPT-5.4 Mini supports the following capabilities:
* Text
* Function calling
* JSON mode
* Streaming
* Structured outputs

This model is best suited for:
*

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 94.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1350 |
| ARC | None |

## Benchmark Analysis
### Analysis of OpenAI: GPT-5.4 Mini Benchmark Performance
#### Overview
The OpenAI: GPT-5.4 Mini model is a standard, non-open-source model released by OpenAI on January 1, 2024. This analysis will delve into the model's benchmark performance, focusing on the MMLU, HumanEval, and Arena ELO scores, and their implications for real-world use.

#### Benchmark Scores
The model's benchmark scores are as follows:
* **MMLU (Massive Multitask Language Understanding)**: 94.0
* **HumanEval**: Not available
* **LMSYS Arena ELO**: 1350
* **GSM8K**: Not available

#### Interpretation of Benchmark Scores
* **MMLU**: A score of 94.0 indicates that the model has achieved a high level of performance in understanding and generating human-like text across a wide range of tasks. This suggests that the model is well-suited for applications such as text generation, chat, and analysis.
* **HumanEval**: The lack of a HumanEval score makes it difficult to assess the model's performance in evaluating and executing human-written code. However, the model's capabilities include function_calling, which suggests that it may still be suitable for coding-related tasks.
* **LMSYS Arena ELO**: An ELO score of 1350 indicates that the model has achieved a moderate level of performance in the LMSYS Arena benchmark, which evaluates a model's ability to play games and engage in interactive tasks. This suggests that the model may be suitable for applications such as chat and text-based games.

#### Real-World Implications
The benchmark scores suggest

## Competitor Comparison
### Comparison of OpenAI: GPT-5.4 Mini with Top Competitors
Since there are no direct competitors listed for OpenAI: GPT-5.4 Mini, we will provide a general overview of the model's features, pricing, and performance. This will help users understand when to choose this model and what trade-offs to expect.

#### Model Overview
The OpenAI: GPT-5.4 Mini model is a standard, non-open-source model released on January 1, 2024. It has the following key features:
* **Context Window**: 400,000 tokens
* **Max Output**: 128,000 tokens
* **Knowledge Cutoff**: 2023-12
* **Capabilities**: text, function_calling, json_mode, streaming, structured_outputs
* **Best For**: chat, text_generation, coding, analysis, rag_pipelines, summarization

#### Pricing
The pricing for OpenAI: GPT-5.4 Mini is as follows:
* **Input**: $0.75 per 1M tokens
* **Output**: $4.5 per 1M tokens
* **Cached Input**: $None per 1M tokens
* **Batch Input**: $None per 1M tokens

#### Cost Examples
Here are some cost examples to help estimate the expenses:
* **1,000 calls (avg 500 tokens)**: $2.625
* **10,000 calls**: $26.25
* **100,000 calls**: $262.5

#### Performance
The model's performance is measured by the following benchmarks:
* **MMLU**: 94.0
* **LMSYS Arena ELO**: 1350

#### Choosing OpenAI: GPT-5.4 Mini
Since there are no direct competitors listed, OpenAI: GPT-5.4 Mini can be considered for a wide range of applications, including:
* Chat and text generation
* Coding and analysis
* Summarization and rag_pipelines

However, users should be aware of the model's limitations, such as the context window and max output size. Additionally, the model's knowledge cutoff is 2023-12, which may not be suitable for applications that require more recent information.

In summary, OpenAI: GPT-5.4 Mini is a powerful model with a range of capabilities and a competitive pricing structure. While there are no direct competitors

## Best Use Cases
### Introduction to OpenAI: GPT-5.4 Mini
The OpenAI: GPT-5.4 Mini model is a standard, non-open-source model released by OpenAI on 2024-01-01. This model is part of the GPT series and is known for its capabilities in text generation, coding, analysis, and more.

### Top 5 Best Use Cases for OpenAI: GPT-5.4 Mini
Based on the capabilities and benchmarks of the OpenAI: GPT-5.4 Mini model, the top 5 best use cases are:

1. **Chat and Text Generation**: With its high MMLU score of 94.0, this model is well-suited for generating human-like text and engaging in conversation.
2. **Coding and Analysis**: The model's ability to perform function calling and structured outputs makes it a great tool for coding and analysis tasks.
3. **Summarization**: The OpenAI: GPT-5.4 Mini model can be used to summarize long pieces of text into concise and meaningful summaries.
4. **RAG Pipelines**: The model's support for Retrieval-Augmented Generation (RAG) pipelines makes it a great tool for tasks that require generating text based on external knowledge.
5. **Streaming and JSON Mode**: The model's ability to handle streaming input and output, as well as JSON mode, makes it a great tool for real-time applications and data processing.

### Code Integration Examples with OpenRouter
To integrate the OpenAI: GPT-5.4 Mini model with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the OpenRouter client
client = openrouter.Client(api_key="YOUR_API_KEY")

# Define the input prompt
prompt = "Write a short story about a character who discovers a hidden world."

# Define the model and parameters
model = "openai/gpt-5.4-mini"


## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
