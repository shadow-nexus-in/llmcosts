# NVIDIA: Nemotron 3 Super API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-02
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super is a powerful language model developed by Nvidia, released on January 1, 2024. This model, identified as `nvidia/nemotron-3-super-120b-a12b`, operates on a standard tier and is not open-source. With its robust architecture, the Nemotron 3 Super is designed to handle a wide range of tasks, including text generation, coding, analysis, and more. Its capabilities include text processing, function calling, JSON mode, streaming, and structured outputs, making it a versatile tool for developers.

### Technical Specifications and Strengths
Technically, the Nemotron 3 Super boasts a context window of 262,144 tokens and can produce a maximum output of 4,096 tokens. Its knowledge cutoff is December 2023, ensuring it has a broad and up-to-date understanding of the world. The model's pricing is structured around input and output tokens, with costs of $0.1 per 1M input tokens and $0.5 per 1M output tokens. Benchmarks show the model achieving an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, demonstrating its capabilities. The Nemotron 3 Super's main strengths lie in its ability to handle complex tasks such as chat, text generation, coding, analysis, and summarization, thanks to its advanced architecture and large context window.

### Use Cases and Cost Considerations
The NVIDIA Nemotron 3 Super is best utilized for applications that require in-depth text analysis, generation, and processing. It is particularly suited for chat, text generation, coding, analysis, RAG pipelines, and summarization tasks. When considering the cost, developers can expect to pay $0.1 per 1M input tokens and $0.5 per 1M output tokens. For example, 1,000 calls with an average of

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
* Input: **$0.1 per 1M tokens**
* Output: **$0.5 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### Optimal Usage Scenarios
Given the cost structure, it is optimal to use:
* **Cached Input** whenever possible, as it is free.
* **Batch Input** for large-scale API calls, as it is also free.

#### Batch API Savings
The batch API savings can be significant, as the input cost is waived for batch inputs. However, the output cost remains at **$0.5 per 1M tokens**.

#### Cost at Scale
The cost at scale for the NVIDIA Nemotron 3 Super is as follows:
* **1,000 calls (avg 500 tokens)**: **$0.3**
* **10,000 calls**: **$3.0**
* **100,000 calls**: **$30.0**

These costs demonstrate a linear scaling of costs with the number of API calls.

#### Context and Limits
The model has the following context and limits:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12

These limits should be considered when designing applications that utilize the NVIDIA Nemotron 3 Super.

#### Capabilities and Best Use Cases
The model has the following capabilities:
* **Text**
* **Function calling

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
The NVIDIA Nemotron 3 Super is a standard, non-open-source model released by Nvidia on 2024-01-01. This analysis will delve into its benchmark performance, focusing on the MMLU, HumanEval, and Arena ELO scores, and explain their implications for real-world use.

#### Benchmark Performance
The model's benchmark performance is as follows:
* **MMLU (Massive Multitask Language Understanding) Score**: 80.0
* **HumanEval Score**: Not available
* **LMSYS Arena ELO Score**: 1200

These benchmarks provide insights into the model's capabilities:
* The **MMLU score** of 80.0 indicates the model's ability to understand and perform a wide range of natural language processing tasks. A higher score suggests better performance. In this case, the Nemotron 3 Super demonstrates a strong foundation in language understanding.
* The **HumanEval score** is not available, which means we cannot directly assess the model's coding abilities or its capacity to generate human-like code.
* The **LMSYS Arena ELO score** of 1200 is a measure of the model's performance in a competitive environment, where it is pitted against other models. An ELO score of 1200 suggests that the Nemotron 3 Super is a capable model, but its exact standing in the competitive landscape is unclear without more context.

#### Real-World Implications
The benchmark scores have the following implications for real-world use:
* The strong MMLU score suggests that the Nemotron 3 Super is suitable for tasks that require a deep understanding of natural language, such as text generation

## Competitor Comparison
### Comparison of NVIDIA: Nemotron 3 Super with Top Competitors
Since there are no direct competitors listed for the NVIDIA: Nemotron 3 Super, we will provide a general overview of its features, pricing, and performance. This will help users understand when to choose this model and what trade-offs to expect.

#### Model Overview
The NVIDIA: Nemotron 3 Super is a standard-tier model released by Nvidia on 2024-01-01. It is not open-source and has the following key features:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12
* **Capabilities**: text, function_calling, json_mode, streaming, structured_outputs
* **Best For**: chat, text_generation, coding, analysis, rag_pipelines, summarization

#### Pricing
The pricing for the NVIDIA: Nemotron 3 Super is as follows:
* **Input**: $0.1 per 1M tokens
* **Output**: $0.5 per 1M tokens
* **Cached Input**: $None per 1M tokens
* **Batch Input**: $None per 1M tokens

#### Cost Examples
Here are some cost examples for using the NVIDIA: Nemotron 3 Super:
* **1,000 calls (avg 500 tokens)**: $0.3
* **10,000 calls**: $3.0
* **100,000 calls**: $30.0

#### Performance
The NVIDIA: Nemotron 3 Super has the following benchmark scores:
* **MMLU**: 80.0
* **LMSYS Arena ELO**: 1200

#### Choosing the NVIDIA: Nemotron 3 Super
Given the lack of direct competitors, the NVIDIA: Nemotron 3 Super is a strong choice for applications that require:
* Large context windows (262,144 tokens)
* High maximum output (4,096 tokens)
* Support for text, function_calling, json_mode, streaming, and structured_outputs
* Use cases such as chat, text_generation, coding, analysis, rag_pipelines, and summarization

However, users should be aware of the following:
* The model is not open-source, which may limit customization and transparency.
* The knowledge cutoff is 2023-12, which may not reflect the latest developments in certain domains.
* The pricing may be

## Best Use Cases
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super is a powerful model released by Nvidia on 2024-01-01. With its capabilities in text, function calling, JSON mode, streaming, and structured outputs, it is best suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization.

### Top 5 Best Use Cases for NVIDIA Nemotron 3 Super
Given its capabilities, here are the top 5 best use cases for the NVIDIA Nemotron 3 Super:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and ability to generate up to 4,096 tokens, the Nemotron 3 Super is ideal for chatbots and text generation applications.
2. **Coding and Analysis**: The model's function calling and structured outputs capabilities make it suitable for coding and analysis tasks, such as code completion and code review.
3. **RAG Pipelines**: The Nemotron 3 Super's ability to handle JSON mode and streaming makes it a good fit for RAG (Retrieval-Augmented Generation) pipelines, which involve retrieving and generating text based on user input.
4. **Summarization**: With its high MMLU benchmark score of 80.0, the Nemotron 3 Super is well-suited for summarization tasks, such as summarizing long documents or articles.
5. **Conversational AI**: The model's capabilities in text, function calling, and structured outputs make it a good fit for conversational AI applications, such as virtual assistants or customer support chatbots.

### Code Integration Example with OpenRouter
To integrate the Nemotron 3 Super with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Nemotron 3 Super model
model = openrouter.Model("nvidia/nemotron-3-super-120b-a12b")

# Define

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
