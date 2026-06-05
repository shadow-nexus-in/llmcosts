# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-05
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a wide range of natural language processing tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens, making it suitable for complex tasks such as chat, text generation, coding, analysis, and summarization.

### Technical Specifications and Pricing
Technically, Mistral Small 4 is characterized by its performance benchmarks, including an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. The model's pricing is based on input and output tokens, with costs of $0.15 per 1M input tokens and $0.6 per 1M output tokens. There are no specified costs for cached input or batch input. For developers, understanding these pricing metrics is crucial for estimating the cost of integrating Mistral Small 4 into their applications. For example, 1,000 calls with an average of 500 tokens would cost $0.375, while 10,000 calls would amount to $3.75, and 100,000 calls would cost $37.5.

### Use Cases and Competitors
Mistral Small 4 is best suited for applications involving chat, text generation, coding, analysis, RAG pipelines, and summarization, thanks to its robust capabilities and large context window. However, its limitations, such as a knowledge cutoff of 2023-12, should be considered when choosing this model for specific tasks. Currently, there are no direct competitors listed for Mistral Small 4, making it a unique offering in

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
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens (free)
* Batch Input: $None per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option when possible. However, the context window limit of 262,144 tokens and the max output limit of 4,096 tokens should be considered when deciding whether to utilize cached tokens.

#### Batch API Savings
Batch input is also free, which can lead to significant cost savings when making multiple API calls. By batching API requests, users can reduce the overall cost per call.

#### Cost at Scale
The cost of using Mistral Small 4 at scale is as follows:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

To calculate the cost per call, we can divide the total cost by the number of calls:
* 1,000 calls: $0.375 / 1,000 = $0.000375 per call
* 10,000 calls: $3.75 / 10,000 = $0.000375 per call
* 100,000 calls: $37.5 / 100,000 = $0.000375 per call

As shown, the cost per call remains constant at $0.000375, indicating a linear

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
The Mistral Small 4 model, provided by Mistralai, is a standard-tier language model with a release date of 2024-01-01. This analysis will delve into its benchmark performance, focusing on the MMLU, HumanEval, and Arena ELO scores, to understand its capabilities and limitations for real-world applications.

#### Pricing
The pricing structure for Mistral Small 4 is as follows:
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
The benchmark performance of Mistral Small 4 is as follows:
* MMLU: **80.0**
* HumanEval: **None**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

The **MMLU (Massive Multitask Language Understanding) score** of 80.0 indicates the model's ability to perform a wide range of natural language processing tasks. A higher MMLU score suggests better performance in understanding and generating human-like language.

The **HumanEval score** is not available for this model, which would have provided insights into its coding capabilities and ability to generate correct and functional code.

The **LMSYS Arena ELO score** of 1200 is a

## Competitor Comparison
### Mistral Small 4 Comparison
Since there are no direct competitors listed for the Mistral Small 4, we will provide a general comparison framework that can be applied to other models in the market. This framework will cover price differences, performance trade-offs, and scenarios where the Mistral Small 4 might be the preferred choice.

#### Pricing Comparison
The Mistral Small 4 is priced at:
- $0.15 per 1M tokens for input
- $0.6 per 1M tokens for output

To compare, we would need the pricing of competitor models. However, we can establish a baseline for what to look for in competitors:
- Input pricing per 1M tokens
- Output pricing per 1M tokens
- Any discounts for cached input or batch input

#### Performance Trade-offs
The Mistral Small 4 has the following performance benchmarks:
- MMLU: 80.0
- LMSYS Arena ELO: 1200

When comparing to competitors, consider the following:
- MMLU scores for language understanding
- LMSYS Arena ELO for competitive performance
- Other benchmarks like HumanEval and GSM8K if available

#### Choosing the Mistral Small 4
The Mistral Small 4 is best for:
- Chat
- Text generation
- Coding
- Analysis
- RAG pipelines
- Summarization

It offers capabilities in:
- Text
- Function calling
- JSON mode
- Streaming
- Structured outputs

With a context window of 262,144 tokens and a max output of 4,096 tokens, it's suitable for applications requiring substantial input and output handling.

#### Cost Considerations
The cost examples provided are:
- 1,000 calls (avg 500 tokens): $0.375
- 10,000 calls: $3.75
- 100,000 calls: $37.5

When evaluating competitors, consider the cost per call or token, taking into account the specific use case and volume of usage.

### Conclusion
While direct competitors are not listed, the Mistral Small 4's pricing, performance, and capabilities provide a solid foundation for comparison. When evaluating alternative models, consider the trade-offs between price, performance benchmarks, and the specific requirements of your application. The Mistral Small 4's strengths in text generation, coding, and analysis, combined with its structured output capabilities, make it a compelling choice

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and release date of 2024-01-01, it offers a robust set of features for various applications.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and max output of 4,096 tokens, Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: Its capabilities in function calling and structured outputs make it an excellent choice for coding and analysis tasks, such as code completion and code review.
3. **Summarization**: Mistral Small 4's ability to process large amounts of text and generate concise summaries makes it a great fit for summarization tasks.
4. **RAG Pipelines**: Its support for Retrieval-Augmented Generation (RAG) pipelines enables Mistral Small 4 to be used in applications that require generating text based on external knowledge sources.
5. **Streaming and Real-time Applications**: With its streaming capability, Mistral Small 4 can be used in real-time applications, such as live chat or live text generation.

### Code Integration Example with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.Model("mistralai/mistral-small-2603")

# Define a function to generate text using the model
def generate_text(prompt):
    # Create a request to the model
    request = openrouter.Request(
        model=model,
        input=p

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
