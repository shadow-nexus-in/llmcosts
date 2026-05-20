# Xiaomi: MiMo-V2-Omni API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-20
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Xiaomi: MiMo-V2-Omni
The Xiaomi: MiMo-V2-Omni model, released by Xiaomi on 2024-01-01, is a standard tier language model that is not open source. This model is identified by the name `xiaomi/mimo-v2-omni`. With its specific architecture, MiMo-V2-Omni is designed to handle a wide range of natural language processing tasks. Its main strengths include a large context window of 262,144 tokens and the ability to generate up to 65,536 tokens as output.

### Technical Capabilities and Use Cases
Xiaomi: MiMo-V2-Omni supports various capabilities such as text, function calling, JSON mode, streaming, and structured outputs. These features make it suitable for multiple use cases, including chat, text generation, coding, analysis, RAG pipelines, and summarization. The model's pricing is based on input and output tokens, with costs of $0.4 per 1M tokens for input and $2.0 per 1M tokens for output. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO score of 1200, indicating its potential for handling complex language tasks. However, its limitations, such as a knowledge cutoff of 2023-12, should be considered when choosing this model for specific applications.

### Pricing and Cost Considerations
When using Xiaomi: MiMo-V2-Omni, developers should be aware of the pricing structure to estimate costs. For example, 1,000 calls with an average of 500 tokens will cost $1.2, while 10,000 calls will cost $12.0, and 100,000 calls will cost $120.0. Understanding these costs and the model's capabilities, including its strengths in text generation and analysis, can help developers make informed decisions about when to

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
The Xiaomi: MiMo-V2-Omni model is a standard, non-open source model released by Xiaomi on 2024-01-01. This analysis will break down the cost structure, provide guidance on when to use cached tokens, discuss batch API savings, and examine the cost at scale for 1,000, 10,000, and 100,000 API calls.

#### Cost Structure
The cost structure for Xiaomi: MiMo-V2-Omni is as follows:
* **Input**: $0.4 per 1M tokens
* **Output**: $2.0 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

#### Using Cached Tokens
Since cached input tokens are free, it is highly recommended to use them whenever possible. This can significantly reduce the overall cost of using the model, especially for applications where the same input tokens are used repeatedly.

#### Batch API Savings
Batch input is also free, which means that batching API calls can help reduce the cost associated with input tokens. However, the output cost remains the same, so the savings will depend on the specific use case and the ratio of input to output tokens.

#### Cost at Scale
The cost examples provided are:
* **1,000 calls (avg 500 tokens)**: $1.2
* **10,000 calls**: $12.0
* **100,000 calls**: $120.0

These examples illustrate a linear increase in cost with the number of API calls. To estimate the cost for a specific use case, we can calculate the total number of input and output tokens and apply the corresponding costs.

#### Example Calculation
Assuming an average of 500 input tokens and 200 output tokens per call, the cost for 1,000 calls

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
The Xiaomi: MiMo-V2-Omni model, released by Xiaomi on 2024-01-01, is a standard-tier model with a context window of 262,144 tokens and a maximum output of 65,536 tokens. The model's pricing is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens

#### Benchmark Scores
The model's benchmark performance is as follows:
* **MMLU (Massive Multitask Language Understanding) Score**: 80.0
	+ The MMLU score measures a model's ability to understand and generate text across a wide range of tasks and domains. A higher MMLU score indicates better performance.
* **HumanEval Score**: None
	+ The HumanEval score measures a model's ability to generate code that is correct and functional. The absence of a HumanEval score for this model indicates that its code generation capabilities are not well-established.
* **LMSYS Arena ELO Score**: 1200
	+ The LMSYS Arena ELO score measures a model's performance in a competitive environment, where models are pitted against each other to complete tasks. An ELO score of 1200 indicates that the model is a strong competitor, but its exact ranking is not well-established.

#### Real-World Implications
The benchmark scores suggest that the Xiaomi: MiMo-V2-Omni model is:
* Suitable for tasks that require strong language understanding, such as chat, text generation, and analysis.
* Less suitable for tasks that require code generation, such as

## Competitor Comparison
### Comparison of Xiaomi: MiMo-V2-Omni with Top Competitors
Since there are no direct competitors listed for the Xiaomi: MiMo-V2-Omni, we will provide a general overview of its features, pricing, and performance. This will help users understand when to choose this model and what trade-offs to expect.

#### Pricing
The Xiaomi: MiMo-V2-Omni is priced as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$None per 1M tokens** (not available)
* Batch Input: **$None per 1M tokens** (not available)

#### Performance
The model's performance is measured by the following benchmarks:
* MMLU: **80.0**
* LMSYS Arena ELO: **1200**
Note that HumanEval and GSM8K benchmarks are not available.

#### Capabilities and Use Cases
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

#### Cost Examples
To give users an idea of the costs involved, here are some examples:
* 1,000 calls (avg 500 tokens): **$1.2**
* 10,000 calls: **$12.0**
* 100,000 calls: **$120.0**

#### Choosing the Xiaomi: MiMo-V2-Omni
Given the lack of direct competitors, users should consider the following factors when deciding whether to choose the Xiaomi: MiMo-V2-Omni:
* **Context Window**: If your application requires a large context window (up to 262,144 tokens), this model may be a good choice.
* **Output Size**: If your application requires generating large outputs (up to 65,536 tokens), this model may be suitable.
* **Knowledge Cutoff**: If your application requires knowledge up to 2023-12, this model may be a good choice.
* **Capabilities**: If your application requires any of the supported capabilities (text, function_calling, json_mode, streaming, structured_outputs), this model may be a good fit.

In summary, the Xiaomi:

## Best Use Cases
### Introduction to Xiaomi: MiMo-V2-Omni
The Xiaomi: MiMo-V2-Omni model, released by Xiaomi on 2024-01-01, is a standard, non-open-source model with a unique set of capabilities. This guide will explore the top 5 best use cases for this model, along with code integration examples using OpenRouter.

### Top 5 Use Cases for Xiaomi: MiMo-V2-Omni
Based on the model's capabilities, the following are the top 5 use cases:

1. **Text Generation**: With its high MMLU score of 80.0, the Xiaomi: MiMo-V2-Omni model is well-suited for text generation tasks, such as writing articles, creating chatbot responses, or generating product descriptions.
2. **Coding**: The model's ability to perform function calling and structured outputs makes it a good fit for coding tasks, such as generating code snippets, debugging, or providing code completion suggestions.
3. **Analysis**: The Xiaomi: MiMo-V2-Omni model can be used for analysis tasks, such as data analysis, sentiment analysis, or text summarization, due to its high context window of 262,144 tokens.
4. **Chat**: With its capabilities in text generation and function calling, the model can be used to build conversational AI systems, such as chatbots or virtual assistants.
5. **Summarization**: The model's ability to process large amounts of text and generate concise summaries makes it a good fit for summarization tasks, such as summarizing long documents or articles.

### Code Integration Examples with OpenRouter
To integrate the Xiaomi: MiMo-V2-Omni model with OpenRouter, you can use the following code examples:

```python
import openrouter

# Initialize the Xiaomi: MiMo-V2-Omni model
model = openrouter.Model("xiaomi/mimo-v2-omni")

# Text generation

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
