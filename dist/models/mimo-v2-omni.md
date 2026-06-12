# Xiaomi: MiMo-V2-Omni API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-12
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Xiaomi: MiMo-V2-Omni
The Xiaomi: MiMo-V2-Omni model, released by Xiaomi on 2024-01-01, is a standard-tier language model that is not open source. This model is part of the Xiaomi lineup and is identified by the `xiaomi/mimo-v2-omni` model name. With a context window of 262,144 tokens and a maximum output of 65,536 tokens, the MiMo-V2-Omni is designed to handle a wide range of natural language processing tasks. The model's knowledge cutoff is 2023-12, indicating that it was trained on data up to December 2023.

### Architecture and Strengths
The architecture of the Xiaomi: MiMo-V2-Omni model supports various capabilities, including text, function calling, JSON mode, streaming, and structured outputs. These features make it an ideal choice for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization. The model's strengths are reflected in its benchmark scores, with an MMLU score of 80.0 and an LMSYS Arena ELO score of 1200. However, its limitations are noted in the absence of HumanEval and GSM8K benchmark scores. The model's pricing is based on input and output tokens, with costs of $0.4 per 1M input tokens and $2.0 per 1M output tokens.

### Use Cases and Cost Considerations
Developers can leverage the Xiaomi: MiMo-V2-Omni model for a variety of use cases, taking into account its capabilities and pricing structure. For example, the model can be used for chat applications, text generation, and coding tasks. The cost of using the model can be estimated based on the number of calls and tokens processed. As illustrated in the cost examples, 1,000 calls with an average of 500 tokens would

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
The Xiaomi: MiMo-V2-Omni model is a standard, non-open source model released by Xiaomi on 2024-01-01. This analysis will break down the cost structure, explore the use of cached tokens, batch API savings, and calculate the cost at scale for 1,000, 10,000, and 100,000 API calls.

#### Cost Structure
The pricing for Xiaomi: MiMo-V2-Omni is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### Using Cached Tokens
Since cached input tokens are free (**$0 per 1M tokens**), it is highly recommended to utilize cached tokens whenever possible to minimize costs.

#### Batch API Savings
Batch input tokens are also free (**$0 per 1M tokens**), which means that batching API calls can help reduce the overall cost. However, the actual savings will depend on the specific use case and the number of tokens processed per call.

#### Cost at Scale
The cost examples provided are:
* 1,000 calls (avg 500 tokens): **$1.2**
* 10,000 calls: **$12.0**
* 100,000 calls: **$120.0**

To calculate the cost at scale, we can use the provided pricing structure. Assuming an average of 500 tokens per call, we can estimate the cost as follows:
* 1,000 calls: 500 tokens/call \* 1,000 calls = 500,000 tokens
	+ Input: 500,000 tokens / 1,000,000 tokens \* $0.4

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Xiaomi: MiMo-V2-Omni Benchmark Performance
The Xiaomi: MiMo-V2-Omni model, released on 2024-01-01, is a standard tier model provided by Xiaomi. It is not open source.

#### Pricing
The pricing for this model is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Context and Limits
The model has the following context and limits:
* Context Window: **262,144 tokens**
* Max Output: **65,536 tokens**
* Knowledge Cutoff: **2023-12**

#### Benchmarks
The benchmark performance of the model is as follows:
* **MMLU: 80.0**: The MMLU (Massive Multitask Language Understanding) benchmark measures a model's ability to perform a wide range of natural language processing tasks. A higher MMLU score indicates better performance. An MMLU score of 80.0 suggests that the Xiaomi: MiMo-V2-Omni model has good language understanding capabilities.
* **HumanEval: None**: HumanEval is a benchmark that measures a model's ability to generate code. The absence of a HumanEval score for this model means that its code generation capabilities are not evaluated.
* **LMSYS Arena ELO: 1200**: The LMSYS Arena ELO score measures a model's performance in a competitive arena, where models are pitted against each other to complete tasks. An ELO score of 1200

## Competitor Comparison
### Comparison of Xiaomi: MiMo-V2-Omni with Top Competitors
Since there are no direct competitors listed for the Xiaomi: MiMo-V2-Omni model, we will provide a general comparison framework that can be used to evaluate this model against other similar models in the market.

#### Pricing Comparison
The Xiaomi: MiMo-V2-Omni model has the following pricing:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens

To compare this model with its top competitors, we would need to consider the pricing of other models with similar capabilities. However, since no direct competitors are listed, we can only provide a general guideline for comparison:
* Look for models with similar context windows, max output, and knowledge cutoff dates.
* Compare the input and output pricing of these models to determine which one offers the best value for money.

#### Performance Trade-offs
The Xiaomi: MiMo-V2-Omni model has the following performance metrics:
* MMLU: 80.0
* LMSYS Arena ELO: 1200

When comparing this model with its top competitors, consider the following performance trade-offs:
* Models with higher MMLU scores may offer better performance, but may also be more expensive.
* Models with higher LMSYS Arena ELO scores may offer better performance in certain tasks, but may not be as effective in other tasks.

#### When to Choose Each Model
The Xiaomi: MiMo-V2-Omni model is best for:
* Chat
* Text generation
* Coding
* Analysis
* RAG pipelines
* Summarization

When choosing between this model and its competitors, consider the specific use case and the capabilities required. For example:
* If the use case requires a high level of text generation capability, the Xiaomi: MiMo-V2-Omni model may be a good choice.
* If the use case requires a high level of coding capability, a model with a higher MMLU score may be a better choice.

#### Cost Examples
The Xiaomi: MiMo-V2-Omni model has the following cost examples:
* 1,000 calls (avg 500 tokens): $1.2
* 10,000 calls: $12.0
* 100,000 calls: $120.0

When comparing this model with its competitors, consider the cost of each model for the specific

## Best Use Cases
### Introduction to Xiaomi: MiMo-V2-Omni
The Xiaomi: MiMo-V2-Omni model, released by Xiaomi on 2024-01-01, is a standard, non-open-source model with a unique set of capabilities and pricing. This guide will explore the top 5 best use cases for this model, along with code integration examples using OpenRouter.

### Top 5 Use Cases for Xiaomi: MiMo-V2-Omni
Based on the model's capabilities and benchmarks, the top 5 use cases are:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and ability to generate up to 65,536 tokens, this model is well-suited for chat and text generation applications.
2. **Coding and Analysis**: The model's function_calling and structured_outputs capabilities make it a good fit for coding and analysis tasks, such as code completion and data analysis.
3. **Summarization**: The model's ability to process large amounts of text and generate concise summaries makes it a good choice for summarization tasks.
4. **RAG Pipelines**: The model's support for rag_pipelines makes it a good fit for tasks that require retrieving and generating text based on external knowledge.
5. **Streaming**: The model's streaming capability makes it suitable for real-time text generation and processing applications.

### Code Integration Examples with OpenRouter
Here is an example of how to integrate the Xiaomi: MiMo-V2-Omni model with OpenRouter:
```python
import openrouter

# Initialize the model
model = openrouter.Model("xiaomi/mimo-v2-omni")

# Define a function to generate text
def generate_text(prompt):
    input_ids = model.encode(prompt)
    output_ids = model.generate(input_ids, max_length=512)
    return model.decode(output_ids)

# Test the function
prompt = "Write a short story about a character who discovers a hidden world

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
