# Xiaomi: MiMo-V2-Omni API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-16
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Xiaomi: MiMo-V2-Omni
The Xiaomi: MiMo-V2-Omni model, released by Xiaomi on 2024-01-01, is a standard tier language model that is not open source. This model is part of the Xiaomi lineup and is identified by the name `xiaomi/mimo-v2-omni`. With its robust architecture, MiMo-V2-Omni is designed to handle a wide range of tasks, including but not limited to text generation, chat, coding, analysis, and summarization. The model's capabilities are further enhanced by its support for text, function calling, JSON mode, streaming, and structured outputs.

### Technical Specifications and Pricing
From a technical standpoint, the MiMo-V2-Omni model boasts a context window of 262,144 tokens and a maximum output of 65,536 tokens, with a knowledge cutoff of 2023-12. The pricing for this model is as follows: input costs $0.4 per 1M tokens, while output costs $2.0 per 1M tokens. There is no charge for cached input or batch input. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. With its capabilities and pricing in mind, developers can estimate costs based on the number of calls they anticipate, such as $1.2 for 1,000 calls averaging 500 tokens, $12.0 for 10,000 calls, and $120.0 for 100,000 calls.

### Use Cases and Competitors
The Xiaomi: MiMo-V2-Omni model is best suited for applications involving chat, text generation, coding, analysis, RAG pipelines, and summarization. However, its limitations and areas where it is not recommended are not explicitly stated. As of the current data, there are no direct competitors listed for the Mi

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.4 |
| Output | $2.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Xiaomi: MiMo-V2-Omni
#### Overview
The Xiaomi: MiMo-V2-Omni model is a standard, non-open-source model provided by Xiaomi, released on January 1, 2024. This analysis will delve into the cost structure, optimal usage scenarios, and cost projections at various scales.

#### Cost Structure
The pricing for Xiaomi: MiMo-V2-Omni is as follows:
- **Input**: $0.4 per 1M tokens
- **Output**: $2.0 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
- **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
- **Batch API Savings**: Although there is no specific pricing discount mentioned for batch inputs, the fact that batch input is free suggests that batching API calls can significantly reduce costs by minimizing the number of input tokens required.

#### Cost at Scale
Based on the provided cost examples:
- **1,000 calls (avg 500 tokens)**: $1.2
- **10,000 calls**: $12.0
- **100,000 calls**: $120.0

These costs demonstrate a linear scaling of expenses with the number of API calls, indicating that the cost per call remains constant regardless of the volume.

#### Cost Projection
To understand the cost structure better, let's calculate the cost per token based on the input and output pricing:
- **Input Cost per Token**: $0.4 / 1,000,000 tokens = $0.0000004 per token
- **Output Cost per Token**: $2.0 / 1,000,000 tokens = $0.000002 per token

Given the average token usage per call is not explicitly stated

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Xiaomi: MiMo-V2-Omni Benchmark Performance
#### Overview
The Xiaomi: MiMo-V2-Omni model, released by Xiaomi on 2024-01-01, is a standard-tier model that is not open source. It has a context window of 262,144 tokens and a maximum output of 65,536 tokens, with a knowledge cutoff of 2023-12.

#### Pricing
The pricing for this model is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Benchmark Performance
The benchmark performance of the Xiaomi: MiMo-V2-Omni model is as follows:
* **MMLU (Massive Multitask Language Understanding)**: 80.0 - This score indicates the model's ability to perform well across a wide range of natural language processing tasks. A higher score indicates better performance.
* **HumanEval**: None - This benchmark evaluates the model's ability to write correct and functional code. The lack of a score indicates that the model has not been evaluated on this benchmark.
* **LMSYS Arena ELO**: 1200 - This score is a measure of the model's performance in a competitive setting, where it is pitted against other models. A higher score indicates better performance.

#### Real-World Implications
The benchmark scores have the following implications for real-world use:
* The MMLU score of 80.0 indicates that the model is capable of performing well across a range of NLP tasks, making it suitable

## Competitor Comparison
### Comparison of Xiaomi: MiMo-V2-Omni with Top Competitors
Since there are no direct competitors listed for the Xiaomi: MiMo-V2-Omni, we will provide a general overview of its features, pricing, and performance. This will help users understand when to choose this model and what trade-offs to expect.

#### Pricing
The Xiaomi: MiMo-V2-Omni pricing is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Performance
The model's performance is measured by the following benchmarks:
* MMLU: **80.0**
* LMSYS Arena ELO: **1200**
Note that HumanEval and GSM8K benchmarks are not available for this model.

#### Capabilities and Limits
The Xiaomi: MiMo-V2-Omni supports the following capabilities:
* text
* function_calling
* json_mode
* streaming
* structured_outputs
It is best suited for tasks such as:
* chat
* text_generation
* coding
* analysis
* rag_pipelines
* summarization

#### Context and Limits
The model has the following context and limits:
* Context Window: **262,144 tokens**
* Max Output: **65,536 tokens**
* Knowledge Cutoff: **2023-12**

#### Cost Examples
The estimated costs for using the Xiaomi: MiMo-V2-Omni are:
* 1,000 calls (avg 500 tokens): **$1.2**
* 10,000 calls: **$12.0**
* 100,000 calls: **$120.0**

#### Choosing the Xiaomi: MiMo-V2-Omni
Given the lack of direct competitors, the Xiaomi: MiMo-V2-Omni can be considered for tasks that require its specific capabilities, such as text generation, coding, and analysis. However, users should be aware of the model's limitations, including its context window and knowledge cutoff.

When to choose the Xiaomi: MiMo-V2-Omni:
* For tasks that require a standard tier model with a large context window (262,144 tokens)
* For applications that need a model with a high MMLU score (80.0)
* For use

## Best Use Cases
### Introduction to Xiaomi: MiMo-V2-Omni
The Xiaomi: MiMo-V2-Omni model, released by Xiaomi on 2024-01-01, is a standard, non-open-source model with a unique set of capabilities. This guide will explore the top 5 best use cases for this model, along with practical advice and code integration examples using OpenRouter.

### Top 5 Use Cases for Xiaomi: MiMo-V2-Omni
Based on the model's capabilities and benchmarks, the top 5 use cases are:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and ability to generate text, this model is well-suited for chat applications and text generation tasks.
2. **Coding and Function Calling**: The model's ability to perform function calling and generate structured outputs makes it a good fit for coding tasks, such as code completion and code generation.
3. **Analysis and Summarization**: The model's high MMLU benchmark score of 80.0 indicates its ability to perform complex analysis and summarization tasks.
4. **RAG Pipelines**: The model's support for streaming and structured outputs makes it a good fit for RAG (Retrieve, Augment, Generate) pipelines.
5. **Text-based Applications**: The model's capabilities in text generation, function calling, and analysis make it a good fit for text-based applications, such as text-based games or interactive stories.

### Code Integration Examples with OpenRouter
To integrate the Xiaomi: MiMo-V2-Omni model with OpenRouter, you can use the following code examples:
```python
import openrouter

# Initialize the model
model = openrouter.Model("xiaomi/mimo-v2-omni")

# Text generation example
input_text = "Hello, how are you?"
output = model.generate_text(input_text)
print(output)

# Function calling example
input_function = "add(2, 3

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
