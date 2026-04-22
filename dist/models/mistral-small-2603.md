# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-22
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open-source and is part of the Mistralai offerings. With a context window of 262,144 tokens and a maximum output of 4,096 tokens, Mistral Small 4 is designed to handle a wide range of natural language processing tasks. Its knowledge cutoff is 2023-12, ensuring it has a broad and up-to-date understanding of the world up to that point.

### Architecture and Strengths
The architecture of Mistral Small 4 supports various capabilities, including text processing, function calling, JSON mode, streaming, and structured outputs. These features make it highly versatile for applications such as chat, text generation, coding, analysis, and summarization. The model's strengths are further highlighted by its benchmarks, with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, demonstrating its competence in understanding and generating human-like text. However, its pricing is structured around input and output tokens, with costs of $0.15 per 1M input tokens and $0.6 per 1M output tokens, indicating a focus on efficient and cost-effective processing.

### Use Cases and Cost Considerations
Mistral Small 4 is best suited for applications that require advanced text processing, such as chatbots, text generation tools, coding assistants, and analysis platforms. Its ability to handle large context windows and generate coherent text makes it a valuable asset for these use cases. When considering the cost, developers can expect to pay $0.375 for 1,000 calls with an average of 500 tokens, scaling up to $3.75 for 10,000 calls and $37.5 for 100,000 calls. With no direct competitors listed, Mistral Small 4 presents a unique

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.15 |
| Output | $0.6 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Mistral: Mistral Small 4
#### Overview
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral: Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option when possible. Utilize cached tokens for:
- Frequently accessed data
- Static or infrequently changing inputs
- Applications where input data can be pre-processed and cached

#### Batch API Savings
Batching API calls can significantly reduce costs. Although the pricing does not explicitly mention batch input costs, it implies that batch inputs are free. To maximize savings:
- Batch similar requests together
- Optimize batch sizes to minimize the number of API calls
- Leverage batch processing for high-volume applications

#### Cost at Scale
The cost examples provided are:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These costs demonstrate a linear scaling of expenses with the number of API calls. To estimate costs for other scales, assume a linear relationship based on the provided examples.

#### Cost Calculation
To calculate the cost for a specific number of API calls, use the following formula:
- **Cost per call**: $0.000375 per call (derived from $0.375 for 1,000 calls)


## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Benchmark Performance Analysis
#### Overview
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. It is not open source. The model's pricing is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens

#### Benchmark Scores
The model's benchmark performance is as follows:
* **MMLU (Massive Multitask Language Understanding)**: 80.0
	+ MMLU is a benchmark that evaluates a model's ability to perform a wide range of natural language processing tasks. A higher MMLU score indicates better performance. With a score of 80.0, Mistral Small 4 demonstrates a strong understanding of various language tasks.
* **HumanEval**: None
	+ HumanEval is a benchmark that assesses a model's ability to write code. The lack of a HumanEval score for Mistral Small 4 makes it difficult to evaluate its coding capabilities.
* **LMSYS Arena ELO**: 1200
	+ LMSYS Arena ELO is a benchmark that measures a model's performance in a competitive environment. An ELO score of 1200 indicates that Mistral Small 4 has a moderate level of performance, with higher scores indicating better performance.
* **GSM8K**: None
	+ GSM8K is a benchmark that evaluates a model's math problem-solving abilities. The absence of a GSM8K score for Mistral Small 4 limits its evaluation in this area.

#### Real-World Implications
The benchmark scores suggest that Mistral Small 

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral: Mistral Small 4 model, we will provide a general comparison framework that can be applied to other models in the market. This will help in understanding the trade-offs and making informed decisions.

#### Pricing Comparison
The Mistral: Mistral Small 4 model is priced as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens

To compare, we would need the pricing information of the top competitors. However, we can establish a general guideline for comparison:
- **Lower Input Price**: Models with lower input prices per 1M tokens may be more suitable for applications with large input sizes.
- **Lower Output Price**: Models with lower output prices per 1M tokens may be more suitable for applications that require generating large amounts of text.

#### Performance Trade-offs
The Mistral: Mistral Small 4 model has the following performance metrics:
- MMLU: 80.0
- LMSYS Arena ELO: 1200

When comparing with top competitors, consider the following:
- **Higher MMLU Score**: Models with higher MMLU scores may perform better in tasks that require understanding and generating human-like text.
- **Higher LMSYS Arena ELO**: Models with higher LMSYS Arena ELO scores may perform better in competitive benchmarking tasks.

#### Context and Limits
The Mistral: Mistral Small 4 model has the following context and limits:
- Context Window: 262,144 tokens
- Max Output: 4,096 tokens
- Knowledge Cutoff: 2023-12

When comparing with top competitors, consider the following:
- **Larger Context Window**: Models with larger context windows may be more suitable for tasks that require understanding long-range dependencies in text.
- **Larger Max Output**: Models with larger max output sizes may be more suitable for tasks that require generating long pieces of text.

#### Capabilities and Best Use Cases
The Mistral: Mistral Small 4 model has the following capabilities:
- text, function_calling, json_mode, streaming, structured_outputs

It is best suited for:
- chat
- text_generation
- coding
- analysis
- rag_pipelines
- summarization

When comparing with top competitors, consider the following:
- **Over

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, coding, analysis, and more. With its standard tier and release date of 2024-01-01, it offers a robust set of features for various applications.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and max output of 4,096 tokens, Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Function Calling**: Mistral Small 4's ability to perform function calling and its high MMLU benchmark score of 80.0 make it a great choice for coding and software development tasks.
3. **Analysis and Summarization**: The model's capabilities in analysis and summarization, combined with its high context window, make it an excellent choice for tasks that require understanding and condensing large amounts of text.
4. **RAG Pipelines**: Mistral Small 4's support for RAG (Retrieval-Augmented Generation) pipelines makes it a great choice for applications that require generating text based on external knowledge sources.
5. **Streaming and Structured Outputs**: With its support for streaming and structured outputs, Mistral Small 4 is well-suited for applications that require real-time text generation and processing.

### Code Integration Examples with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.Model("mistralai/mistral-small-2603")

# Define a function to generate text using the model
def generate_text(prompt

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
