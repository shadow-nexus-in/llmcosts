# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-09
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. This model boasts an impressive architecture, with a context window of 131,072 tokens and a maximum output of 4,096 tokens. Its capabilities include text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for various applications. The model's knowledge cutoff is 2024-07, ensuring it has a broad and up-to-date understanding of the world.

### Strengths and Use Cases
Mistral Large 2 excels in several areas, as evidenced by its benchmark scores: MMLU (84.0), HumanEval (92.0), LMSYS Arena ELO (1225), and GSM8K (93.0). Its primary use cases include coding, analysis, RAG, agents, multilingual applications, and function calling. The model is well-suited for tasks that require a deep understanding of language and the ability to generate coherent, context-specific responses. However, it is not recommended for tasks that require embeddings, bulk processing at a low cost, real-time responses under 100ms, or vision-heavy applications.

### Pricing and Cost Considerations
The pricing for Mistral Large 2 is as follows: $3.0 per 1M input tokens and $9.0 per 1M output tokens. There are no additional costs for cached input or batch input. To give developers a better understanding of the costs involved, some examples are provided: 1,000 calls (avg 500 tokens) cost $6.0, 10,000 calls cost $60.0, and 100,000 calls cost $600.0. Compared to its top competitor, GPT-4o, which charges $2.5/1M input and $10.0/1

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
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. The pricing structure for Mistral Large 2 is as follows:

* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### Cost Structure
The cost structure for Mistral Large 2 is based on the number of input and output tokens. The input cost is $3.0 per 1M tokens, while the output cost is $9.0 per 1M tokens. Notably, cached input and batch input are free, which can significantly reduce costs for certain use cases.

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for reducing costs. If your application involves repeated input sequences or similar prompts, utilizing cached tokens can help minimize expenses. However, the effectiveness of cached tokens depends on the specific use case and the frequency of repeated inputs.

#### Batch API Savings
Batch input is also free, which means that processing multiple inputs in a single API call can lead to significant cost savings. By batching inputs, you can avoid paying for individual input tokens, resulting in lower overall costs. This is particularly beneficial for applications that require processing large volumes of data.

#### Cost at Scale
To illustrate the cost implications of using Mistral Large 2, let's examine the costs for different numbers of API calls:

* 1,000 calls (avg 500 tokens): $6.0
* 10,000 calls: $60.0
* 100,000 calls: $600.0

These costs demonstrate the economies

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 84.0 |
| HumanEval | 92.0 |
| LMSYS Arena ELO | 1225 |
| ARC | 93.0 |

## Benchmark Analysis
### Mistral Large 2 Benchmark Performance Analysis
#### Overview
Mistral Large 2, a premium model provided by Mistral AI, boasts an impressive set of benchmark scores. This analysis will delve into the MMLU, HumanEval, and Arena ELO scores, explaining their significance for real-world applications.

#### Benchmark Scores
The model's benchmark scores are as follows:
* **MMLU (Massive Multitask Language Understanding)**: 84.0
* **HumanEval**: 92.0
* **LMSYS Arena ELO**: 1225
* **GSM8K**: 93.0

These scores indicate the model's performance in various areas:
* **MMLU**: Measures the model's ability to understand and generate human-like text across a wide range of tasks. A score of 84.0 suggests that Mistral Large 2 has a strong foundation in language understanding.
* **HumanEval**: Evaluates the model's ability to write correct and functional code. With a score of 92.0, Mistral Large 2 demonstrates exceptional coding capabilities.
* **LMSYS Arena ELO**: Assesses the model's performance in a competitive environment, where it is pitted against other models. An ELO score of 1225 indicates that Mistral Large 2 is a strong competitor in the arena.

#### Real-World Implications
The benchmark scores have significant implications for real-world use cases:
* **Coding and Analysis**: With high HumanEval and MMLU scores, Mistral Large 2 is well-suited for coding, analysis, and other tasks that require strong language understanding and generation capabilities.
* **Multilingual Support**: The model's capabilities

## Competitor Comparison
### Mistral Large 2 Comparison
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. This comparison will examine its pricing, performance, and trade-offs against its top competitors, specifically GPT-4o.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, whereas GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. This indicates that GPT-4o is cheaper for input tokens but more expensive for output tokens.

#### Performance Comparison
Mistral Large 2 has the following benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

In contrast, the benchmark scores for GPT-4o are not provided. However, based on the available data, Mistral Large 2 demonstrates strong performance across various tasks.

#### Context and Limits Comparison
| Model | Context Window | Max Output |
| --- | --- | --- |
| Mistral Large 2 | 131,072 tokens | 4,096 tokens |
| GPT-4o | Not provided | Not provided |

Mistral Large 2 has a context window of 131,072 tokens and a maximum output of 4,096 tokens. Without the corresponding data for GPT-4o, it is challenging to compare the two models directly in this regard.

#### Capabilities and Best Use Cases
Mistral Large 2 supports the following capabilities:
- text
- vision
- function_calling
- json_mode
- streaming
- system_prompts

It is best suited for tasks such as:
- coding
- analysis
- rag
- agents
- multilingual
- function_calling

On the other hand, it is not recommended for:
- embeddings


## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. With its robust capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, it stands out as a powerful tool for various applications. This guide will explore the top 5 best use cases for Mistral Large 2, along with practical advice and code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Large 2
1. **Coding and Development**: Mistral Large 2 excels in coding tasks, thanks to its high scores in HumanEval (92.0) and GSM8K (93.0). It can be used for code completion, debugging, and optimization.
2. **Analysis and Research**: With its large context window (131,072 tokens) and high MMLU score (84.0), Mistral Large 2 is suitable for in-depth analysis and research tasks, such as text analysis, sentiment analysis, and data extraction.
3. **RAG (Retrieval-Augmented Generation)**: Mistral Large 2's capabilities in function calling and JSON mode make it an excellent choice for RAG tasks, which involve retrieving information from external sources and generating text based on that information.
4. **Multilingual Support**: As a model that supports multiple languages, Mistral Large 2 can be used for tasks such as language translation, language understanding, and cross-lingual information retrieval.
5. **Agent Development**: With its ability to handle system prompts and function calling, Mistral Large 2 can be used to develop intelligent agents that can interact with users and perform tasks on their behalf.

### Code Integration Example with OpenRouter
To integrate Mistral Large 2 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Mistral Large 

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
