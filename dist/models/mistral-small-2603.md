# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-26
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open-source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process and generate human-like text, making it suitable for applications such as chat, text generation, coding, analysis, and summarization.

### Technical Specifications and Use Cases
Technically, Mistral Small 4 boasts a context window of 262,144 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2023-12. This means it can understand and respond to complex, lengthy inputs up to a certain limit. The model's pricing is based on input and output tokens, with costs of $0.15 per 1M tokens for input and $0.6 per 1M tokens for output. With its capabilities, Mistral Small 4 is best utilized for tasks that require in-depth text analysis, generation, or manipulation, such as coding assistance, text summarization, and conversational AI. Its performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its competence in various linguistic tasks.

### Cost Considerations and Competitors
For developers considering the integration of Mistral Small 4 into their applications, understanding the cost structure is crucial. The cost examples provided indicate that 1,000 calls with an average of 500 tokens would amount to $0.375, scaling up to $37.5 for 100,000 calls. Given its unique set of capabilities and performance benchmarks, Mistral Small 4 does not have direct competitors listed, positioning it as a distinct offering in the market for developers

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
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* **Input**: $0.15 per 1M tokens
* **Output**: $0.6 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
* **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
* **Batch API Savings**: Although batch input is free, the cost savings come from reducing the number of API calls. This can be beneficial for large-scale applications where the number of API calls can be significantly reduced.

#### Cost at Scale
The cost of using Mistral Small 4 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: $0.375
* **10,000 calls**: $3.75
* **100,000 calls**: $37.5

These costs indicate a linear increase in cost with the number of API calls, with no discounts for larger volumes.

#### Conclusion
Mistral Small 4 offers a competitive pricing structure, especially when utilizing cached input tokens and batch API calls. However, the costs can add up quickly at scale, with 100,000 API calls costing $37.5. It is essential to carefully evaluate the cost-benefit analysis and consider the capabilities and limitations of the model to ensure optimal usage and cost-effectiveness.

#### Capabilities and Limitations
Mistral Small 4 is capable of:
* Text
* Function calling


## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Benchmark Analysis
#### Overview
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. It is not open source.

#### Pricing Model
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
The benchmark performance of Mistral Small 4 is as follows:
* MMLU: **80.0**
* HumanEval: **None**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

The MMLU score of 80.0 indicates the model's ability to understand and generate human-like text. A higher MMLU score generally corresponds to better performance in natural language understanding and generation tasks.

The LMSYS Arena ELO score of 1200 is a measure of the model's performance in a competitive setting, where it is pitted against other models. A higher ELO score indicates better performance.

The lack of HumanEval and GSM8K scores makes it difficult to assess the model's performance in specific areas, such as coding and math problem-solving.

#### Real-World Use
In real-world use, Mistral Small 4

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral: Mistral Small 4, we will provide a general comparison framework that can be applied when evaluating this model against other similar models in the market.

#### Pricing Comparison
Mistral: Mistral Small 4 pricing is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens

When comparing prices, consider the following:
* **Input Cost**: If a competitor offers a lower input cost per 1M tokens, it may be more cost-effective for applications with large input requirements.
* **Output Cost**: If a competitor offers a lower output cost per 1M tokens, it may be more cost-effective for applications with large output requirements.

#### Performance Trade-offs
Mistral: Mistral Small 4 performance is measured by the following benchmarks:
* MMLU: 80.0
* LMSYS Arena ELO: 1200

When evaluating performance trade-offs, consider the following:
* **MMLU Score**: A higher MMLU score indicates better performance on a range of natural language processing tasks. If a competitor has a higher MMLU score, it may be a better choice for applications requiring advanced language understanding.
* **LMSYS Arena ELO**: A higher LMSYS Arena ELO score indicates better performance in a competitive evaluation framework. If a competitor has a higher LMSYS Arena ELO score, it may be a better choice for applications requiring high-level language generation capabilities.

#### Context and Limits
Mistral: Mistral Small 4 has the following context and limits:
* Context Window: 262,144 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2023-12

When evaluating context and limits, consider the following:
* **Context Window**: If a competitor has a larger context window, it may be better suited for applications requiring longer input sequences.
* **Max Output**: If a competitor has a higher max output limit, it may be better suited for applications requiring longer output sequences.
* **Knowledge Cutoff**: If a competitor has a more recent knowledge cutoff, it may be better suited for applications requiring up-to-date information.

#### Capabilities and Best Use Cases
Mistral: Mistral Small 4 has the following capabilities:
* text,

## Best Use Cases
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a powerful model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on January 1, 2024, this standard-tier model offers a unique set of features that make it suitable for various applications.

### Top 5 Best Use Cases for Mistral: Mistral Small 4
Based on its capabilities and pricing, here are the top 5 best use cases for Mistral: Mistral Small 4:

1. **Chat and Text Generation**: With its text generation capabilities, Mistral: Mistral Small 4 is ideal for chat applications, such as customer support bots or virtual assistants.
2. **Coding and Analysis**: The model's ability to perform function calling and structured outputs makes it suitable for coding tasks, such as code completion or code review, as well as data analysis.
3. **Summarization and RAG Pipelines**: Mistral: Mistral Small 4's capabilities in text generation and structured outputs make it a good fit for summarization tasks and RAG (Retrieve, Augment, Generate) pipelines.
4. **Content Creation**: The model's text generation capabilities can be used for content creation, such as generating articles, blog posts, or social media content.
5. **Conversational AI**: With its ability to generate human-like text, Mistral: Mistral Small 4 can be used to build conversational AI applications, such as voice assistants or chatbots.

### Code Integration Examples with OpenRouter
To integrate Mistral: Mistral Small 4 with OpenRouter, you can use the following code examples:

```python
import openrouter

# Initialize the OpenRouter client
client = openrouter.Client("mistralai/mistral-small-2603")

# Define a function to generate text using Mistral: Mistral Small 4


## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
