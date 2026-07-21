# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-21
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly in coding, analysis, and multilingual tasks. This model boasts a context window of 131,072 tokens and can generate up to 4,096 tokens as output. With a knowledge cutoff of 2024-07, Mistral Large 2 is well-equipped to handle tasks that require up-to-date information up to its knowledge cutoff date.

### Architecture and Strengths
The architecture of Mistral Large 2 supports various capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. Its strengths are reflected in its benchmark scores: MMLU at 84.0, HumanEval at 92.0, LMSYS Arena ELO at 1225, and GSM8K at 93.0. These scores indicate that Mistral Large 2 excels in coding and analytical tasks, making it a prime choice for developers working on projects that involve complex problem-solving and code generation. Its ability to handle multilingual inputs and function calling further expands its utility in diverse applications.

### Pricing and Use Cases
Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, with no charges for cached or batch inputs. This pricing model makes it suitable for applications where the input and output token counts are manageable. For example, 1,000 calls averaging 500 tokens each would cost $6.0, scaling to $60.0 for 10,000 calls and $600.0 for 100,000 calls. While it may not be the most cost-effective option for bulk or real-time applications, its capabilities and performance make it a strong contender for tasks that require precision and advanced functionalities, positioning it

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
Mistral Large 2, provided by Mistral AI, is a premium model released on 2024-07-24. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts, making it best suited for applications such as coding, analysis, and multilingual tasks.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
- **Input**: $3.0 per 1M tokens
- **Output**: $9.0 per 1M tokens
- **Cached Input**: No additional cost ($None per 1M tokens)
- **Batch Input**: No additional cost ($None per 1M tokens)

#### When to Use Cached Tokens
Cached tokens can be utilized without incurring any additional cost. This feature is beneficial when the same input tokens are used multiple times, as it eliminates the need to pay for input tokens more than once. However, the specific scenarios where cached tokens can be applied are not detailed in the provided data.

#### Batch API Savings
The pricing data does not specify any cost savings for using batch API calls explicitly. Instead, it indicates that there is no additional cost for batch input ($None per 1M tokens), suggesting that the cost per token remains consistent regardless of the batch size.

#### Cost at Scale
The cost of using Mistral Large 2 at scale can be estimated based on the provided examples:
- **1,000 calls (avg 500 tokens)**: $6.0
- **10,000 calls**: $60.0
- **100,000 calls**: $600.0

These examples suggest a linear cost scaling with the number of API calls. To estimate the cost per token, we can use the average token count per call. For instance, for 1,000 calls with an average of 500 tokens per call, the total tokens would

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
The Mistral Large 2 model, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. It has a context window of 131,072 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff date of 2024-07.

#### Pricing
The pricing for Mistral Large 2 is as follows:
* Input: **$3.0 per 1M tokens**
* Output: **$9.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Benchmark Performance
The model's benchmark performance is measured by the following scores:
* **MMLU: 84.0** - The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to perform a wide range of natural language processing tasks. A higher MMLU score indicates better performance.
* **HumanEval: 92.0** - The HumanEval benchmark assesses a model's ability to generate code that is correct and functional. A higher HumanEval score indicates better coding capabilities.
* **LMSYS Arena ELO: 1225** - The LMSYS Arena ELO score measures a model's performance in a competitive environment, where it is pitted against other models. A higher ELO score indicates better performance.
* **GSM8K: 93.0** - The GSM8K benchmark evaluates a model's ability to solve math problems. A higher GSM8K score indicates better math problem-solving capabilities.

#### Real-

## Competitor Comparison
### Mistral Large 2 Comparison
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. This comparison will evaluate Mistral Large 2 against its top competitors, focusing on price differences, performance trade-offs, and use case recommendations.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens. In comparison, GPT-4o is priced at $2.5 per 1M input tokens but $10.0 per 1M output tokens. This indicates that while GPT-4o is cheaper for input, Mistral Large 2 is more cost-effective for output.

#### Performance Comparison
Mistral Large 2 boasts impressive benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

These scores suggest that Mistral Large 2 excels in various tasks, including coding, analysis, and multilingual capabilities. However, without direct benchmark comparisons to GPT-4o, it's challenging to determine which model performs better in specific areas.

#### Capabilities and Limitations
Mistral Large 2 supports a range of capabilities, including:
- Text
- Vision
- Function calling
- JSON mode
- Streaming
- System prompts

It is best suited for tasks like:
- Coding
- Analysis
- RAG (Retrieval-Augmented Generation)
- Agents
- Multilingual
- Function calling

However, it is not recommended for:
- Embeddings
- Bulk cheap processing
- Real-time sub-100ms applications
- Vision-heavy tasks

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100,000 calls: $

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model with a wide range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. It is particularly suited for coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual tasks, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Given its capabilities and pricing, here are the top 5 best use cases for Mistral Large 2:

1. **Advanced Coding Assistance**: With its high HumanEval score of 92.0, Mistral Large 2 is ideal for providing coding assistance, including code completion, code review, and code optimization. Its ability to understand and generate code in multiple programming languages makes it a valuable tool for developers.

2. **Complex Text Analysis**: Mistral Large 2's high MMLU score of 84.0 indicates its proficiency in understanding and analyzing complex texts. This makes it suitable for tasks such as text summarization, sentiment analysis, and information extraction.

3. **Multilingual Support**: Given its multilingual capabilities, Mistral Large 2 can be used for tasks that require understanding and generating text in multiple languages, such as language translation, cross-lingual information retrieval, and multilingual text analysis.

4. **RAG and Agents**: With its support for RAG and agents, Mistral Large 2 can be used to build conversational AI models that can retrieve information from external knowledge sources and engage in more informed and context-specific conversations.

5. **Function Calling and JSON Mode**: Mistral Large 2's ability to call external functions and process JSON data makes it suitable for tasks that require interacting with external APIs, processing structured data, and generating JSON output.

### Code Integration Example with OpenRouter
To integrate Mistral Large 2 with

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
