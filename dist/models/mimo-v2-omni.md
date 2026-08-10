# Xiaomi: MiMo-V2-Omni API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-10
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Xiaomi: MiMo-V2-Omni
The Xiaomi: MiMo-V2-Omni model, released by Xiaomi on 2024-01-01, is a standard, non-open-source language model designed for a variety of tasks. Its architecture is tailored to handle complex inputs and generate coherent outputs, making it suitable for applications such as chat, text generation, coding, analysis, and summarization. With a context window of 262,144 tokens and a maximum output of 65,536 tokens, this model is capable of processing and generating substantial amounts of text.

### Technical Strengths and Use Cases
Xiaomi: MiMo-V2-Omni boasts several key strengths, including its ability to handle text, function calling, JSON mode, streaming, and structured outputs. These capabilities make it an ideal choice for developers working on projects that require advanced language understanding and generation. The model's performance is reflected in its benchmarks, with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. While it excels in certain areas, its limitations are notable, particularly its knowledge cutoff of 2023-12, which may impact its performance on tasks requiring more recent information.

### Pricing and Cost Considerations
The pricing for Xiaomi: MiMo-V2-Omni is structured around input and output tokens, with costs of $0.4 per 1M input tokens and $2.0 per 1M output tokens. There are no additional costs for cached input or batch input. To illustrate the cost implications, 1,000 calls with an average of 500 tokens would cost $1.2, while 10,000 calls would amount to $12.0, and 100,000 calls would total $120.0. With no direct competitors listed, Xiaomi: MiMo-V2-Omni presents a unique offering in the market, and its pricing reflects its capabilities and the value

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
The Xiaomi: MiMo-V2-Omni model is a standard, non-open source model provided by Xiaomi, released on January 1, 2024. This analysis will delve into the cost structure, optimal usage scenarios, and cost projections at scale for this model.

#### Cost Structure
The pricing for Xiaomi: MiMo-V2-Omni is as follows:
- **Input**: $0.4 per 1M tokens
- **Output**: $2.0 per 1M tokens
- **Cached Input**: No charge ($None per 1M tokens)
- **Batch Input**: No charge ($None per 1M tokens)

This structure indicates that the primary cost driver is the output, which is significantly more expensive than the input. Cached and batch inputs are free, suggesting that optimizing for these can significantly reduce costs.

#### Optimal Usage Scenarios
- **Cached Tokens**: Since cached input tokens are free, it's highly beneficial to use cached tokens whenever possible. This can be particularly useful in applications where the same or similar inputs are processed multiple times.
- **Batch API Savings**: Although there's no direct cost savings mentioned for batch inputs, the lack of a charge for batch inputs implies that processing inputs in batches can help reduce the overall cost by minimizing the number of API calls needed, thus indirectly reducing the output cost.

#### Cost at Scale
Given the cost examples provided:
- **1,000 calls (avg 500 tokens)**: $1.2
- **10,000 calls**: $12.0
- **100,000 calls**: $120.0

These examples suggest a linear scaling of costs with the number of API calls. To estimate costs at different scales, we can use these examples as a baseline.

#### Cost Projections
Based on the provided cost examples, the cost per call appears to be constant, regardless of the number of

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
The Xiaomi: MiMo-V2-Omni model, released by Xiaomi on 2024-01-01, is a standard, non-open-source model. Its pricing structure includes input costs of $0.4 per 1M tokens and output costs of $2.0 per 1M tokens.

#### Benchmark Scores
The model's performance is measured by the following benchmark scores:
* **MMLU (Massive Multitask Language Understanding) Score: 80.0** - This score indicates the model's ability to understand and perform a wide range of natural language tasks. A higher MMLU score suggests better performance in tasks such as text classification, sentiment analysis, and question answering.
* **HumanEval Score: None** - HumanEval is a benchmark that evaluates a model's ability to generate correct and executable code. The absence of a HumanEval score for this model means its coding capabilities are not directly comparable to other models using this metric.
* **LMSYS Arena ELO Score: 1200** - The LMSYS Arena ELO score is a measure of a model's overall performance in a competitive setting, where models are pitted against each other to complete tasks. An ELO score of 1200 suggests that the Xiaomi: MiMo-V2-Omni model has a moderate level of performance compared to other models in the arena.

#### Real-World Use Implications
Given its benchmark scores, the Xiaomi: MiMo-V2-Omni model is suitable for a variety of real-world applications, including:
* **Text Generation**: With a context window of 262,144 tokens and a

## Competitor Comparison
### Comparison of Xiaomi: MiMo-V2-Omni with Top Competitors
Since there are no direct competitors listed for the Xiaomi: MiMo-V2-Omni, we will provide a general overview of its features, pricing, and performance. This will help users understand when to choose this model and what trade-offs to expect.

#### Pricing
The Xiaomi: MiMo-V2-Omni has the following pricing structure:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Performance
The model's performance is measured by the following benchmarks:
* MMLU: 80.0
* LMSYS Arena ELO: 1200

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

The model has the following limits:
* Context Window: 262,144 tokens
* Max Output: 65,536 tokens
* Knowledge Cutoff: 2023-12

#### Cost Examples
The estimated costs for using the Xiaomi: MiMo-V2-Omni are:
* 1,000 calls (avg 500 tokens): $1.2
* 10,000 calls: $12.0
* 100,000 calls: $120.0

#### Choosing the Xiaomi: MiMo-V2-Omni
Since there are no direct competitors, the decision to choose the Xiaomi: MiMo-V2-Omni depends on the specific use case and requirements. Consider the following factors:
* **Task suitability**: If your task aligns with the model's capabilities, such as chat, text generation, or coding, the Xiaomi: MiMo-V2-Omni may be a good choice.
* **Performance requirements**: If you need a model with a high MMLU score (80.0) and a decent LMSYS Arena ELO score (1200), the Xiaomi: MiMo-V2-Omni may be suitable.
* **Budget constraints**: If you are looking for a model with a relatively low

## Best Use Cases
### Introduction to Xiaomi: MiMo-V2-Omni
The Xiaomi: MiMo-V2-Omni model, released by Xiaomi on 2024-01-01, is a standard, non-open-source model with a unique set of capabilities. This guide will explore the top 5 best use cases for this model, along with practical advice and code integration examples using OpenRouter.

### Top 5 Use Cases for Xiaomi: MiMo-V2-Omni
Based on the model's capabilities, the following are the top 5 use cases:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and support for text generation, this model is well-suited for chat applications and text generation tasks.
2. **Coding and Analysis**: The model's support for function calling, JSON mode, and structured outputs makes it a good fit for coding and analysis tasks, such as code completion and data analysis.
3. **Summarization and RAG Pipelines**: The model's ability to process large amounts of text and generate summaries makes it a good fit for summarization tasks and RAG (Retrieve, Augment, Generate) pipelines.
4. **Streaming and Real-time Applications**: The model's support for streaming and real-time processing makes it a good fit for applications that require fast and efficient processing of large amounts of data.
5. **Structured Data Processing**: The model's support for structured outputs and JSON mode makes it a good fit for processing and generating structured data, such as JSON or XML.

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

#

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
