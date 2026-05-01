# Reka Edge API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-01
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Reka Edge
Reka Edge, developed by Rekaai, is a standard-tier model released on 2024-01-01. This non-open-source model is designed to provide efficient and effective solutions for various natural language processing tasks. The architecture of Reka Edge is not explicitly stated, but its capabilities suggest a robust and flexible design, supporting features such as text, function calling, JSON mode, streaming, and structured outputs.

### Strengths and Use-Cases
The main strengths of Reka Edge lie in its ability to handle a wide range of tasks, including chat, text generation, coding, analysis, RAG pipelines, and summarization. With a context window of 16,384 tokens and a maximum output of 16,384 tokens, Reka Edge is well-suited for tasks that require processing and generating large amounts of text. The model's pricing is based on input and output tokens, with a cost of $0.1 per 1M tokens for both input and output. This pricing structure makes it an attractive option for developers who need to process large volumes of text data.

### Technical Specifications and Pricing
Reka Edge has a knowledge cutoff of 2023-12 and has been benchmarked on several datasets, including MMLU (80.0) and LMSYS Arena ELO (1200). The model's capabilities and pricing make it a competitive option for developers, with cost examples including $0.1 for 1,000 calls (avg 500 tokens), $1.0 for 10,000 calls, and $10.0 for 100,000 calls. While there are no direct competitors listed, Reka Edge's unique combination of features and pricing make it a viable option for developers working on a range of NLP tasks. With its robust architecture and flexible capabilities, Reka Edge is well-positioned to support a wide range of applications, from chat and text generation to coding and analysis.

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.1 |
| Output | $0.1 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Reka Edge Pricing Analysis
#### Overview
Reka Edge, a standard-tier model provided by Rekaai, offers a unique pricing structure that can help optimize costs for various use cases. This analysis will delve into the cost structure, the benefits of using cached tokens, batch API savings, and the cost at scale for 1,000, 10,000, and 100,000 API calls.

#### Cost Structure
The pricing for Reka Edge is as follows:
- **Input**: $0.1 per 1M tokens
- **Output**: $0.1 per 1M tokens
- **Cached Input**: $0 per 1M tokens (free)
- **Batch Input**: $0 per 1M tokens (free)

This structure indicates that using cached inputs and batch inputs can significantly reduce costs, as they are provided at no additional charge.

#### Using Cached Tokens
Cached tokens are free, making them an attractive option for reducing costs. If your application involves repeated queries with the same or similar inputs, utilizing cached tokens can eliminate the input cost entirely. This is particularly beneficial for applications where the input data does not change frequently.

#### Batch API Savings
Similar to cached inputs, batch inputs are also free. This means that processing inputs in batches does not incur any additional cost. For applications that can handle batch processing, this can lead to significant cost savings, especially when dealing with a large volume of API calls.

#### Cost at Scale
The cost examples provided give us a clear picture of how the costs scale with the number of API calls:
- **1,000 calls (avg 500 tokens)**: $0.1
- **10,000 calls**: $1.0
- **100,000 calls**: $10.0

These examples suggest a linear scaling of costs with the number of API calls, indicating that the cost per call remains consistent regardless of the volume. This consistency can help in planning and budgeting for API

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Reka Edge Benchmark Performance Analysis
#### Overview
Reka Edge, a standard-tier model provided by Rekaai, boasts a unique set of capabilities and pricing. Released on 2024-01-01, this model is not open source.

#### Pricing Structure
The pricing for Reka Edge is as follows:
* Input: **$0.1 per 1M tokens**
* Output: **$0.1 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Context and Limits
Reka Edge has the following context and limits:
* Context Window: **16,384 tokens**
* Max Output: **16,384 tokens**
* Knowledge Cutoff: **2023-12**

#### Benchmark Performance
The benchmark performance of Reka Edge is as follows:
* MMLU: **80.0**
* HumanEval: **None**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

#### Interpretation of Benchmark Scores
* **MMLU (80.0)**: The MMLU score measures a model's performance on a set of mathematical and logical tasks. A higher score indicates better performance. With a score of 80.0, Reka Edge demonstrates strong mathematical and logical reasoning capabilities.
* **HumanEval (None)**: HumanEval is a benchmark that evaluates a model's ability to generate human-like code. The absence of a score for Reka Edge indicates that its performance on this benchmark is not available.
* **LMSYS Arena ELO (1200)**: The LMSYS Arena ELO score measures a model

## Competitor Comparison
### Reka Edge Comparison
Since there are no direct competitors listed for Reka Edge, we will provide a general analysis of its features, pricing, and performance. This will help users understand when to choose Reka Edge and what to expect from the model.

#### Model Overview
Reka Edge is a standard-tier model provided by Rekaai, released on January 1, 2024. It is not open source.

#### Pricing
The pricing for Reka Edge is as follows:
* Input: $0.1 per 1M tokens
* Output: $0.1 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Context and Limits
Reka Edge has the following context and limits:
* Context Window: 16,384 tokens
* Max Output: 16,384 tokens
* Knowledge Cutoff: 2023-12

#### Benchmarks
Reka Edge has the following benchmark scores:
* MMLU: 80.0
* LMSYS Arena ELO: 1200

#### Capabilities and Use Cases
Reka Edge supports the following capabilities:
* text
* function_calling
* json_mode
* streaming
* structured_outputs

It is best suited for the following use cases:
* chat
* text_generation
* coding
* analysis
* rag_pipelines
* summarization

#### Cost Examples
Here are some cost examples for using Reka Edge:
* 1,000 calls (avg 500 tokens): $0.1
* 10,000 calls: $1.0
* 100,000 calls: $10.0

#### Choosing Reka Edge
Since there are no direct competitors listed, Reka Edge can be considered for its unique combination of features, pricing, and performance. Users should evaluate the model's capabilities, context, and limits to determine if it meets their specific needs.

When to choose Reka Edge:
* When you need a model with a large context window (16,384 tokens) and max output (16,384 tokens)
* When you require a model with a high MMLU score (80.0) and a decent LMSYS Arena ELO score (1200)
* When you need a model that supports multiple capabilities, including text, function_calling, json_mode, streaming, and structured_outputs
* When you

## Best Use Cases
### Introduction to Reka Edge
Reka Edge is a standard-tier model provided by Rekaai, released on 2024-01-01. It is not open source and offers a range of capabilities including text, function calling, JSON mode, streaming, and structured outputs.

### Top 5 Best Use Cases for Reka Edge
Based on its capabilities, Reka Edge is best suited for the following use cases:

1. **Chat and Text Generation**: With its ability to handle text and generate human-like responses, Reka Edge is ideal for chat applications, text generation, and conversational AI.
2. **Coding and Analysis**: Reka Edge's function calling and structured outputs capabilities make it suitable for coding tasks, such as code completion, code review, and analysis.
3. **Summarization and RAG Pipelines**: Reka Edge's ability to handle text and generate summaries makes it a good fit for summarization tasks and RAG (Retrieve, Augment, Generate) pipelines.
4. **Streaming and Real-time Applications**: With its streaming capability, Reka Edge can be used for real-time applications, such as live chat, sentiment analysis, and event-driven processing.
5. **JSON Mode and Structured Outputs**: Reka Edge's JSON mode and structured outputs capabilities make it suitable for applications that require structured data, such as data processing, data integration, and data analytics.

### Code Integration Examples with OpenRouter
To integrate Reka Edge with OpenRouter, you can use the following code examples:

```python
import openrouter

# Initialize Reka Edge model
model = openrouter.Model("rekaai/reka-edge")

# Define a function to call the model
def call_model(input_text):
    # Set the input and output formats
    input_format = "text"
    output_format = "text"

    # Call the model
    output = model(input_text, input_format=input_format, output_format=output_format)

    # Return the

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
