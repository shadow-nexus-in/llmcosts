# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-04
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral: Mistral Small 4 is designed to handle a variety of tasks, including text generation, function calling, and structured outputs. Its capabilities are further enhanced by features such as JSON mode and streaming, making it a versatile tool for developers.

### Strengths and Use Cases
The main strengths of Mistral: Mistral Small 4 lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens. With a knowledge cutoff of 2023-12, this model is well-suited for tasks that require up-to-date information prior to this date. Its primary use cases include chat, text generation, coding, analysis, and summarization, among others. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its capabilities in various linguistic and logical tasks. With pricing set at $0.15 per 1M input tokens and $0.6 per 1M output tokens, developers can estimate costs based on their specific use cases, such as $0.375 for 1,000 calls averaging 500 tokens.

### Technical Specifications and Cost Considerations
Technically, Mistral: Mistral Small 4 supports several key capabilities: text processing, function calling, JSON mode, streaming, and structured outputs. These features make it an attractive choice for applications requiring complex text manipulation and generation. The model's limitations, such as the context window and max output, should be considered when designing applications to ensure they align with the model's specifications. For cost planning, developers can refer to the provided examples, which illustrate the

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.15 |
| Output | $0.6 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Mistral Small 4 Pricing Analysis
#### Overview
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$None per 1M tokens** (free)
* Batch Input: **$None per 1M tokens** (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following strategies:
* **Cached Tokens**: Utilize cached input tokens whenever possible, as they are **free**. This is ideal for applications with repetitive or similar input sequences.
* **Batch API**: Leverage batch input for multiple requests, as it is also **free**. This approach is suitable for high-volume applications or those with concurrent requests.

#### Cost at Scale
The cost of using Mistral Small 4 at various scales is as follows:
* **1,000 calls (avg 500 tokens)**: **$0.375**
* **10,000 calls**: **$3.75**
* **100,000 calls**: **$37.5**

These costs demonstrate a linear relationship with the number of API calls, indicating that the pricing model is straightforward and easy to predict.

#### Conclusion
Mistral Small 4 offers a competitive pricing structure, especially when utilizing cached input tokens and batch API requests. By understanding the cost structure and optimizing usage, developers can effectively integrate this model into their applications while managing costs. The provided cost examples enable accurate budgeting and planning for large-scale deployments.

### Recommendations
* Use cached input tokens for repetitive or similar input sequences to reduce costs.
* Leverage

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Analysis
#### Model Overview
The Mistral Small 4 model, provided by Mistralai, is a standard-tier model released on 2024-01-01. It is not open-source.

#### Pricing
The pricing for Mistral Small 4 is as follows:
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Context and Limits
The model has the following context and limits:
* Context Window: **262,144 tokens**
* Max Output: **4,096 tokens**
* Knowledge Cutoff: **2023-12**

#### Benchmarks
The model's benchmark performance is:
* MMLU: **80.0**
* HumanEval: **None**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

The MMLU score of 80.0 indicates the model's ability to understand and generate human-like text. A higher MMLU score generally corresponds to better performance in natural language processing tasks.

The LMSYS Arena ELO score of 1200 is a measure of the model's performance in a competitive environment, where it is pitted against other models. A higher ELO score indicates better performance.

The lack of HumanEval and GSM8K scores means that the model's performance in these specific areas is unknown.

#### Capabilities and Use Cases
Mistral Small 4 supports the following capabilities:
* text
* function_calling
* json_mode
* streaming
* structured

## Competitor Comparison
### Mistral Small 4 Comparison
Since there are no direct competitors listed for the Mistral Small 4 model, we will provide a general overview of its features, pricing, and performance. This will help users understand the value proposition of the Mistral Small 4 and make informed decisions about its adoption.

#### Model Overview
The Mistral Small 4 model is a standard-tier model released by Mistralai on 2024-01-01. It is not open-source and has the following key features:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12
* **Capabilities**: text, function_calling, json_mode, streaming, structured_outputs
* **Best For**: chat, text_generation, coding, analysis, rag_pipelines, summarization

#### Pricing
The pricing for the Mistral Small 4 model is as follows:
* **Input**: $0.15 per 1M tokens
* **Output**: $0.6 per 1M tokens
* **Cached Input**: $None per 1M tokens
* **Batch Input**: $None per 1M tokens

#### Cost Examples
To illustrate the cost of using the Mistral Small 4 model, consider the following examples:
* **1,000 calls (avg 500 tokens)**: $0.375
* **10,000 calls**: $3.75
* **100,000 calls**: $37.5

#### Performance
The Mistral Small 4 model has the following benchmark scores:
* **MMLU**: 80.0
* **LMSYS Arena ELO**: 1200

#### Choosing the Mistral Small 4 Model
Given the lack of direct competitors, the decision to choose the Mistral Small 4 model depends on the specific use case and requirements. Consider the following factors:
* **Context Window**: If your application requires a large context window, the Mistral Small 4 model may be a good choice.
* **Max Output**: If your application requires generating long outputs, the Mistral Small 4 model may be a good choice.
* **Knowledge Cutoff**: If your application requires knowledge up to 2023-12, the Mistral Small 4 model may be a good choice.
* **Capabilities**: If your application requires text, function_calling, json_mode, streaming, or

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and release date of 2024-01-01, it offers a robust solution for various applications.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and max output of 4,096 tokens, Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: Its function calling and structured outputs capabilities make it an ideal choice for coding and analysis tasks, such as code completion and debugging.
3. **Summarization and RAG Pipelines**: Mistral Small 4's text generation and analysis capabilities also make it suitable for summarization and RAG (Retrieve, Augment, Generate) pipelines.
4. **Streaming and Real-time Applications**: With its streaming capability, Mistral Small 4 can be used for real-time applications, such as live chat or text-based customer support.
5. **JSON Mode and Structured Data Processing**: Its JSON mode and structured outputs capabilities make it a good choice for processing and generating structured data, such as JSON files.

### Code Integration Examples with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code examples:
```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.Model("mistralai/mistral-small-2603")

# Define a function to generate text using the model
def generate_text(prompt):
    input_ids = openrouter.tokenize(prompt)
    output = model.generate(input_ids, max_length=4096)
   

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
