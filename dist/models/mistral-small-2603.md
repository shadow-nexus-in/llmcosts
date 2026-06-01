# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-01
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a wide range of natural language processing tasks, including text generation, coding, and analysis. Its capabilities extend to function calling, JSON mode, streaming, and structured outputs, making it a versatile tool for developers.

### Strengths and Use Cases
The main strengths of Mistral Small 4 lie in its ability to process large amounts of data, with a context window of up to 262,144 tokens and a maximum output of 4,096 tokens. This makes it well-suited for applications such as chat, text generation, coding, analysis, and summarization. The model's capabilities in handling structured outputs and its support for streaming also position it as a strong candidate for tasks that require real-time processing and complex data handling. With a high MMLU benchmark score of 80.0 and an LMSYS Arena ELO score of 1200, Mistral Small 4 demonstrates strong performance in various linguistic and logical reasoning tasks.

### Pricing and Cost Considerations
The pricing model for Mistral Small 4 is based on input and output tokens, with costs of $0.15 per 1M input tokens and $0.6 per 1M output tokens. There are no additional costs for cached input or batch input. To give developers a better understanding of the costs involved, examples are provided: 1,000 calls averaging 500 tokens would cost $0.375, scaling up to $3.75 for 10,000 calls and $37.5 for 100,000 calls. With no direct competitors listed, Mistral Small 4 offers a unique set of capabilities and performance metrics, making it an attractive option for developers looking for a robust language model

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
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$0.00 per 1M tokens** (free)
* Batch Input: **$0.00 per 1M tokens** (free)

Given this structure, there are no direct costs associated with using cached or batch inputs, which can significantly impact the overall cost of using the model, especially for repeated or bulk queries.

#### When to Use Cached Tokens
Cached tokens should be utilized whenever possible, as they incur **no additional cost**. This is particularly beneficial for applications where the same input data is queried multiple times, such as in chatbots or text analysis tools where user queries may repeat.

#### Batch API Savings
While the pricing does not directly specify a cost for batch inputs, the fact that batch inputs are listed as **$0.00 per 1M tokens** suggests that there is no penalty for batching API calls. This means that making API calls in batches can help reduce the overhead costs associated with individual API requests, potentially leading to significant savings, especially at scale.

#### Cost at Scale
The provided cost examples give insight into the cost structure at different scales:
* **1,000 calls (avg 500 tokens): $0.375**
* **10,000 calls: $3.75**
* **100,000 calls: $37.5**

These examples illustrate a linear cost increase with the number of API calls, indicating that the cost per call remains constant regardless of the volume

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Mistral: Mistral Small 4 Benchmark Performance
#### Overview
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. It is not open-source.

#### Pricing
The pricing model for Mistral: Mistral Small 4 is as follows:
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
The benchmark performance of Mistral: Mistral Small 4 is as follows:
* MMLU: **80.0**
* HumanEval: **None**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

#### Interpretation of Benchmarks
* **MMLU (80.0)**: The MMLU score measures the model's performance on a set of tasks. A higher score indicates better performance. An MMLU score of 80.0 suggests that Mistral: Mistral Small 4 has a good level of performance, but the exact meaning depends on the comparison with other models.
* **HumanEval (None)**: HumanEval is a benchmark that evaluates a model's ability to generate correct code. The absence of a HumanEval score makes it difficult to assess the model

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral: Mistral Small 4, we will provide a general overview of the model's features, pricing, and performance. This will help users understand the value proposition of Mistral: Mistral Small 4 and make informed decisions about its adoption.

#### Model Overview
Mistral: Mistral Small 4 is a standard-tier model provided by Mistralai, released on January 1, 2024. It is not open-source.

#### Pricing
The pricing for Mistral: Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Context and Limits
The model has the following context and limits:
* Context Window: 262,144 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2023-12

#### Benchmarks
Mistral: Mistral Small 4 has the following benchmark scores:
* MMLU: 80.0
* LMSYS Arena ELO: 1200

#### Capabilities and Use Cases
The model supports the following capabilities:
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
The estimated costs for using Mistral: Mistral Small 4 are:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

#### Choosing Mistral: Mistral Small 4
Since there are no direct competitors listed, users should consider the following factors when deciding whether to use Mistral: Mistral Small 4:
* **Performance**: If high performance is required, Mistral: Mistral Small 4's MMLU score of 80.0 and LMSYS Arena ELO score of 1200 may be attractive.
* **Pricing**: If cost is a concern, users should evaluate the estimated costs of using Mistral: Mist

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and release date of 2024-01-01, it offers a robust set of features for various applications.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and ability to generate up to 4,096 tokens, Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: Its function calling and structured outputs capabilities make it an excellent choice for coding and analysis tasks, such as code completion and data analysis.
3. **Summarization**: Mistral Small 4's ability to process large amounts of text and generate concise summaries makes it a great tool for summarization tasks.
4. **RAG Pipelines**: Its support for Retrieval-Augmented Generation (RAG) pipelines enables Mistral Small 4 to be used in applications that require the combination of retrieval and generation capabilities.
5. **Streaming**: With its streaming capability, Mistral Small 4 can be used in real-time applications, such as live chat or text-based interfaces.

### Code Integration Example with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following example code:
```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.MistralSmall4()

# Define a function to generate text
def generate_text(prompt):
    # Use the model to generate text
    output = model.generate_text(prompt, max_length=4096)
    return output

# Test the function
prompt = "Hello

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
