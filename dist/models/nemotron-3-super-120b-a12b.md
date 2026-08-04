# NVIDIA: Nemotron 3 Super API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-04
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super, released on 2024-01-01, is a powerful language model developed by Nvidia. This model, identified as `nvidia/nemotron-3-super-120b-a12b`, operates on a standard tier and is not open-source. With its robust architecture, it is designed to handle a wide range of tasks, including but not limited to text generation, coding, analysis, and summarization. The model boasts a context window of 262,144 tokens and can generate up to 4,096 tokens as output.

### Technical Specifications and Pricing
From a technical standpoint, the Nemotron 3 Super supports various capabilities such as text, function calling, JSON mode, streaming, and structured outputs, making it versatile for different applications. The pricing model for this service is based on input and output tokens, with costs set at $0.1 per 1M tokens for input and $0.5 per 1M tokens for output. Notably, cached input and batch input are priced at $None per 1M tokens, indicating no additional cost for these services. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, demonstrating its capabilities.

### Use Cases and Cost Considerations
The NVIDIA Nemotron 3 Super is best utilized for tasks such as chat, text generation, coding, analysis, RAG pipelines, and summarization. However, its limitations and areas where it is "not good for" are not specified. To plan usage, developers can consider the cost examples provided: for instance, 1,000 calls averaging 500 tokens would cost $0.3, scaling up to $3.0 for 10,000 calls and $30.0 for 100,000 calls. With no direct competitors listed, the Nemotron 3 Super stands

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.1 |
| Output | $0.5 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### NVIDIA Nemotron 3 Super Pricing Analysis
#### Overview
The NVIDIA Nemotron 3 Super is a standard, non-open-source model released by Nvidia on January 1, 2024. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for the NVIDIA Nemotron 3 Super is as follows:
* **Input**: $0.1 per 1M tokens
* **Output**: $0.5 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following scenarios:
* **Cached Tokens**: Since cached input tokens are free, utilize this feature whenever possible to reduce input costs.
* **Batch API Calls**: Batch input is also free, so batching API calls can help reduce overall costs by minimizing the number of requests.

#### Cost at Scale
The cost of using the NVIDIA Nemotron 3 Super at scale is as follows:
* **1,000 calls (avg 500 tokens)**: $0.3
* **10,000 calls**: $3.0
* **100,000 calls**: $30.0

These costs demonstrate a linear relationship between the number of API calls and the total cost.

#### Context and Limits
When using the NVIDIA Nemotron 3 Super, keep in mind the following context and limits:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12

#### Capabilities and Best Use Cases
The NVIDIA Nemotron 3 Super is capable of:
* Text
* Function calling
* JSON mode
* Streaming
* Structured outputs

It is best suited for:
* Chat
* Text generation
* Coding
* Analysis


## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### NVIDIA Nemotron 3 Super Analysis
#### Overview
The NVIDIA Nemotron 3 Super is a standard, non-open-source model released by Nvidia on January 1, 2024. This model is priced at $0.1 per 1M input tokens and $0.5 per 1M output tokens.

#### Benchmark Performance
The model's performance is measured by the following benchmarks:
* **MMLU (Massive Multitask Language Understanding) Score: 80.0** - This score indicates the model's ability to understand and perform a wide range of natural language tasks. A higher score suggests better performance.
* **HumanEval: None** - HumanEval is a benchmark that evaluates a model's ability to generate correct code. The absence of a score for this benchmark suggests that the model's coding capabilities have not been evaluated or reported.
* **LMSYS Arena ELO Score: 1200** - The LMSYS Arena ELO score is a measure of a model's performance in a competitive environment, where models are pitted against each other to solve tasks. A higher score indicates better performance relative to other models.

#### Real-World Implications
The benchmark scores have the following implications for real-world use:
* The MMLU score of 80.0 suggests that the NVIDIA Nemotron 3 Super is capable of handling a wide range of natural language tasks with reasonable proficiency.
* The absence of a HumanEval score makes it difficult to assess the model's coding capabilities.
* The LMSYS Arena ELO score of 1200 indicates that the model is a mid-tier performer in competitive environments.

#### Pricing and Cost Examples
The pricing for the NVIDIA Nemotron 3 Super is

## Competitor Comparison
### NVIDIA Nemotron 3 Super Comparison
#### Introduction
The NVIDIA Nemotron 3 Super is a standard-tier model released by Nvidia on 2024-01-01. With no direct competitors listed, this comparison will focus on the model's features, pricing, and performance trade-offs to help users decide when to choose this model.

#### Pricing
The NVIDIA Nemotron 3 Super pricing is as follows:
* Input: **$0.1 per 1M tokens**
* Output: **$0.5 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Context and Limits
The model has the following context and limits:
* Context Window: **262,144 tokens**
* Max Output: **4,096 tokens**
* Knowledge Cutoff: **2023-12**

#### Benchmarks
The model's performance is measured by the following benchmarks:
* MMLU: **80.0**
* LMSYS Arena ELO: **1200**

#### Capabilities and Best Use Cases
The NVIDIA Nemotron 3 Super supports the following capabilities:
* text
* function_calling
* json_mode
* streaming
* structured_outputs

It is best suited for:
* chat
* text_generation
* coding
* analysis
* rag_pipelines
* summarization

#### Cost Examples
The estimated costs for using the NVIDIA Nemotron 3 Super are:
* 1,000 calls (avg 500 tokens): **$0.3**
* 10,000 calls: **$3.0**
* 100,000 calls: **$30.0**

#### Choosing the NVIDIA Nemotron 3 Super
Given the lack of direct competitors, the decision to choose the NVIDIA Nemotron 3 Super depends on the specific use case and requirements. Consider the following factors:
* **Context window**: If your application requires a large context window, the NVIDIA Nemotron 3 Super's 262,144 token limit may be sufficient.
* **Output size**: If your application requires generating large outputs, the model's 4,096 token limit may be a constraint.
* **Knowledge cutoff**: If your application requires knowledge up to 2023-12, the NVIDIA Nemotron 3 Super may be a good choice.
* **Pricing**: The model's pricing is competitive, with an input cost of $0.

## Best Use Cases
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super is a powerful language model released by Nvidia on 2024-01-01. With its capabilities in text, function calling, JSON mode, streaming, and structured outputs, it is best suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization.

### Top 5 Best Use Cases for NVIDIA Nemotron 3 Super
Based on its capabilities and pricing, here are the top 5 best use cases for the NVIDIA Nemotron 3 Super:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and ability to generate up to 4,096 output tokens, the Nemotron 3 Super is ideal for chat and text generation applications. Its high MMLU benchmark score of 80.0 ensures that it can understand and respond to complex queries.
2. **Coding and Analysis**: The Nemotron 3 Super's function calling and structured outputs capabilities make it suitable for coding and analysis tasks. It can be used to generate code snippets, analyze code, and provide recommendations for improvement.
3. **RAG Pipelines**: The Nemotron 3 Super's ability to handle JSON mode and streaming makes it a good fit for RAG (Retrieve, Augment, Generate) pipelines. It can be used to retrieve information, augment it with additional data, and generate new content.
4. **Summarization**: With its high context window and ability to generate concise output, the Nemotron 3 Super is well-suited for summarization tasks. It can be used to summarize long documents, articles, and other types of text.
5. **OpenRouter Integration**: The Nemotron 3 Super can be integrated with OpenRouter to enable more efficient and cost-effective routing of requests. For example, you can use the following code to integrate the Nemotron 3 Super with OpenRouter:
```python
import open

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
