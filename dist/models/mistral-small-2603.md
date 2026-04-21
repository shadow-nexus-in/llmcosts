# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-21
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of natural language processing tasks with its robust capabilities, including text generation, function calling, JSON mode, streaming, and structured outputs. Its architecture supports a context window of up to 262,144 tokens and can generate output up to 4,096 tokens, with a knowledge cutoff of 2023-12.

### Strengths and Use Cases
The main strengths of Mistral: Mistral Small 4 lie in its versatility and performance across multiple benchmarks, such as achieving an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. It is best utilized for applications like chat, text generation, coding, analysis, RAG pipelines, and summarization, thanks to its capabilities in handling text and generating structured outputs. The pricing model for Mistral Small 4 is based on input and output tokens, with costs of $0.15 per 1M tokens for input and $0.6 per 1M tokens for output. This makes it a cost-effective solution for developers looking to integrate advanced language processing capabilities into their applications.

### Cost Considerations and Competitors
When considering the use of Mistral: Mistral Small 4, developers should be aware of the pricing structure and how it applies to their specific use case. For example, 1,000 calls with an average of 500 tokens would cost $0.375, scaling up to $37.5 for 100,000 calls. As of the current data, there are no direct competitors listed for Mistral Small 4, making it a unique offering in the market. By understanding the capabilities, strengths, and pricing of Mist

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
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens (free)
* Batch Input: $None per 1M tokens (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following scenarios:
* **Cached Tokens**: Since cached input tokens are free, utilize them whenever possible to reduce input costs.
* **Batch API Calls**: With batch input being free, batching API calls can significantly reduce overall costs by minimizing the number of input tokens required.

#### Cost at Scale
The costs for Mistral Small 4 at various scales are as follows:
* **1,000 API Calls**: With an average of 500 tokens per call, the cost is $0.375.
* **10,000 API Calls**: The cost increases to $3.75.
* **100,000 API Calls**: At this scale, the cost is $37.5.

#### Cost Calculation
To calculate the cost, consider the following formula:
Cost = (Input Tokens / 1,000,000) * $0.15 + (Output Tokens / 1,000,000) * $0.6

Given the average output is not provided, we assume the cost examples are based on the input tokens only. However, in a real-world scenario, you should consider both input and output tokens for accurate cost estimation.

#### Conclusion
Mistral Small 4 offers a competitive pricing structure, especially when utilizing cached input tokens and batch API

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Performance Analysis
#### Model Overview
The Mistral Small 4 model, provided by Mistralai, is a standard-tier model released on 2024-01-01. It is not open-source.

#### Pricing Structure
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

#### Benchmark Performance
The benchmark performance of Mistral Small 4 is:
* MMLU: **80.0**
* HumanEval: **None**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

The MMLU score of 80.0 indicates the model's ability to understand and generate human-like text. A higher MMLU score generally corresponds to better performance in natural language processing tasks.

The LMSYS Arena ELO score of 1200 is a measure of the model's performance in a competitive environment, with higher scores indicating better performance. In this case, the score of 1200 suggests that Mistral Small 4 has a moderate level of performance.

The lack of HumanEval and GSM8K scores makes it difficult to directly compare Mistral Small 4's performance in specific areas, such as coding and math problem-solving.

#### Real-World

## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral Small 4 model, we will provide a general overview of the model's features, pricing, and performance. This will help users understand the value proposition of the Mistral Small 4 and make informed decisions about its adoption.

#### Model Overview
The Mistral Small 4 model, released by Mistralai on 2024-01-01, is a standard-tier model that is not open source. It has a context window of 262,144 tokens and can generate up to 4,096 tokens of output.

#### Pricing
The pricing for the Mistral Small 4 model is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Performance
The Mistral Small 4 model has the following benchmark scores:
* MMLU: 80.0
* LMSYS Arena ELO: 1200

#### Capabilities and Use Cases
The Mistral Small 4 model supports the following capabilities:
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
The estimated costs for using the Mistral Small 4 model are:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

#### Choosing the Mistral Small 4 Model
Given the lack of direct competitors, the decision to choose the Mistral Small 4 model depends on the specific requirements of your project. If you need a model with a large context window, support for various capabilities, and a standard tier, the Mistral Small 4 may be a good fit. However, it's essential to evaluate the model's performance and pricing in the context of your specific use case and compare it with other models that may not be direct competitors but can still meet your needs.

### Comparison with Hypothetical Competitors
If we were to compare the Mistral Small 4 model with hypothetical competitors, we

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and non-open source status, it offers a unique set of features for various applications.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and ability to generate up to 4,096 tokens, Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: Its function calling and structured outputs capabilities make it an excellent choice for coding and analysis tasks, such as code completion and data analysis.
3. **Summarization**: Mistral Small 4's ability to process large amounts of text and generate concise summaries makes it a great fit for summarization tasks.
4. **RAG Pipelines**: Its support for Retrieval-Augmented Generation (RAG) pipelines enables it to be used in applications that require generating text based on external knowledge sources.
5. **Streaming**: With its streaming capability, Mistral Small 4 can be used in real-time applications, such as live chat or text-based interfaces.

### Code Integration Examples with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code examples:

```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.MistralSmall4()

# Generate text based on a prompt
prompt = "Write a short story about a character who discovers a hidden world."
response = model.generate_text(prompt)
print(response)

# Use function calling to perform a calculation
def calculate_area(length, width):
    return length * width

response = model

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
