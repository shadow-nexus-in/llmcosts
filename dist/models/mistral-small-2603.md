# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-06
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of tasks, including but not limited to text generation, function calling, and structured output handling. Its capabilities are diverse, supporting text, function calling, JSON mode, streaming, and structured outputs, making it a versatile tool for developers.

### Strengths and Use Cases
The primary strengths of Mistral Small 4 lie in its ability to handle complex tasks with a context window of up to 262,144 tokens and a maximum output of 4,096 tokens. This makes it particularly suited for applications such as chat, text generation, coding, analysis, and summarization. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its competence in various linguistic and logical tasks. However, its limitations, such as a knowledge cutoff of 2023-12, should be considered when choosing it for specific projects.

### Pricing and Cost Considerations
The pricing model for Mistral Small 4 is based on input and output tokens. Developers are charged $0.15 per 1M input tokens and $0.6 per 1M output tokens. There are no charges for cached input or batch input. To give developers a better understanding of the costs involved, examples are provided: 1,000 calls with an average of 500 tokens cost $0.375, 10,000 calls cost $3.75, and 100,000 calls cost $37.5. With no direct competitors listed, Mistral Small 4 offers a unique set of capabilities and pricing that can be attractive for projects requiring its specific strengths, especially in areas like chat, coding, and

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.15 |
| Output | $0.6 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Mistral Small 4
#### Overview
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
- **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
- **Batch API**: Given that batch input is free, batching API calls can significantly reduce the overall cost by minimizing the number of input tokens required.

#### Cost at Scale
The cost examples provided for Mistral Small 4 are as follows:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These costs indicate a linear scaling of expenses with the number of API calls, suggesting that the cost per call remains constant regardless of the volume.

#### Technical Considerations
- **Context Window**: 262,144 tokens
- **Max Output**: 4,096 tokens
- **Knowledge Cutoff**: 2023-12

These technical specifications are crucial for understanding the capabilities and limitations of the Mistral Small 4 model.

#### Capabilities and Best Use Cases
Mistral Small 4 supports the following capabilities:
- text
- function_calling
- json_mode
- streaming
- structured_outputs

It is best suited for applications such as:
-

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Analysis
#### Overview
Mistral Small 4, provided by Mistralai, is a standard-tier model released on 2024-01-01. It is not open-source and has specific pricing and performance benchmarks.

#### Pricing
The pricing for Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: $None per 1M tokens
- **Batch Input**: $None per 1M tokens

#### Context and Limits
- **Context Window**: 262,144 tokens
- **Max Output**: 4,096 tokens
- **Knowledge Cutoff**: 2023-12

#### Benchmarks
The model's performance is measured by the following benchmarks:
- **MMLU (Massive Multitask Language Understanding)**: 80.0
  - MMLU measures a model's ability to understand and perform a wide range of natural language tasks. A higher score indicates better performance across these tasks.
- **HumanEval**: None
  - HumanEval assesses a model's ability to generate code that passes unit tests. The lack of a score here indicates that Mistral Small 4's performance on this benchmark is not provided.
- **LMSYS Arena ELO**: 1200
  - The LMSYS Arena ELO score is a measure of a model's competitive performance in generating text, with higher scores indicating better performance. An ELO score of 1200 suggests that Mistral Small 4 has a moderate level of proficiency in text generation tasks.
- **GSM8K**:

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral: Mistral Small 4, we will provide a general analysis of its features, pricing, and performance. This will help in understanding when to choose this model over others in the market.

#### Model Overview
* **Model:** Mistral: Mistral Small 4 (mistralai/mistral-small-2603)
* **Provider:** Mistralai
* **Release Date:** 2024-01-01
* **Tier:** Standard
* **Open Source:** False

#### Pricing
The pricing for Mistral: Mistral Small 4 is as follows:
* **Input:** $0.15 per 1M tokens
* **Output:** $0.6 per 1M tokens
* **Cached Input:** $None per 1M tokens
* **Batch Input:** $None per 1M tokens

#### Performance and Capabilities
Mistral: Mistral Small 4 has the following capabilities and limitations:
* **Context Window:** 262,144 tokens
* **Max Output:** 4,096 tokens
* **Knowledge Cutoff:** 2023-12
* **Capabilities:** text, function_calling, json_mode, streaming, structured_outputs
* **Best For:** chat, text_generation, coding, analysis, rag_pipelines, summarization

#### Benchmarks
The model's performance on various benchmarks is:
* **MMLU:** 80.0
* **HumanEval:** None
* **LMSYS Arena ELO:** 1200
* **GSM8K:** None

#### Cost Examples
The estimated costs for using Mistral: Mistral Small 4 are:
* **1,000 calls (avg 500 tokens):** $0.375
* **10,000 calls:** $3.75
* **100,000 calls:** $37.5

#### Choosing Mistral: Mistral Small 4
Given the lack of direct competitors, Mistral: Mistral Small 4 can be considered for applications that require:
* High context window (262,144 tokens)
* Moderate output size (4,096 tokens)
* Support for text, function calling, JSON mode, streaming, and structured outputs
* Applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization

However

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and release date of 2024-01-01, it offers a versatile tool for various applications. This guide will outline the top 5 best use cases for Mistral Small 4, along with practical advice and code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Small 4
#### 1. **Chat and Text Generation**
Mistral Small 4 excels in chat and text generation tasks, making it an ideal choice for conversational AI applications. Its context window of 262,144 tokens allows for engaging and contextually relevant conversations.

#### 2. **Coding and Analysis**
With its function calling and structured outputs capabilities, Mistral Small 4 is well-suited for coding and analysis tasks. It can be used to generate code snippets, analyze data, and provide insights.

#### 3. **Summarization**
Mistral Small 4's text generation capabilities make it an excellent choice for summarization tasks. It can condense large amounts of text into concise and meaningful summaries.

#### 4. **RAG Pipelines**
Mistral Small 4's support for RAG (Retrieval-Augmented Generation) pipelines enables it to retrieve relevant information from external knowledge sources and generate text based on that information.

#### 5. **Streaming and Real-time Applications**
Mistral Small 4's streaming capability allows it to process and generate text in real-time, making it suitable for applications such as live chat, sentiment analysis, and real-time text generation.

### Code Integration Examples with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Mistral Small 4 model

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
