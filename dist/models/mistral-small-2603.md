# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-16
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open-source. From an architectural standpoint, Mistral: Mistral Small 4 is designed to handle a variety of natural language processing tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens, making it suitable for complex tasks.

### Technical Specifications and Use Cases
The model's technical specifications highlight its prowess in handling extensive inputs and generating substantial outputs. With a context window of 262,144 tokens and a maximum output of 4,096 tokens, Mistral: Mistral Small 4 is geared towards applications requiring in-depth text analysis and generation. Its pricing model is based on input and output tokens, with costs of $0.15 per 1M tokens for input and $0.6 per 1M tokens for output. The model is best suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization, leveraging its capabilities in function calling and structured outputs. Benchmarks show an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its performance in various evaluation metrics.

### Pricing and Competitiveness
In terms of pricing, Mistral: Mistral Small 4 offers a cost-effective solution for developers, with examples including $0.375 for 1,000 calls averaging 500 tokens, $3.75 for 10,000 calls, and $37.5 for 100,000 calls. The model's pricing is straightforward, with no costs for cached input or batch input. Without direct competitors listed, Mistral: Mist

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.15 |
| Output | $0.6 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Mistral: Mistral Small 4
#### Overview
Mistral: Mistral Small 4 is a standard-tier model provided by Mistralai, released on January 1, 2024. This model is not open source and has a specific cost structure based on input and output tokens.

#### Cost Structure
The cost structure for Mistral: Mistral Small 4 is as follows:
* **Input**: $0.15 per 1M tokens
* **Output**: $0.6 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs when the same input is used multiple times. Since cached input is free, it is recommended to use cached tokens whenever possible to minimize costs.

#### Batch API Savings
Batch input is also free, which means that making batch API calls can help reduce costs. By batching multiple requests together, users can take advantage of the free batch input pricing and save on costs.

#### Cost at Scale
The cost of using Mistral: Mistral Small 4 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: $0.375
* **10,000 calls**: $3.75
* **100,000 calls**: $37.5

These costs are based on the average number of tokens per call and can be used to estimate the total cost of using the model for large-scale applications.

#### Example Cost Calculation
To calculate the cost of using Mistral: Mistral Small 4, we can use the following formula:
Cost = (Number of Input Tokens / 1,000,000) \* $0.15 + (Number of Output Tokens / 1,000,000) \* $0.6

For example, if we make

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Benchmark Analysis
The Mistral Small 4 model, provided by Mistralai, offers a standard tier performance with the following benchmark scores:
* **MMLU (Massive Multitask Language Understanding) Score: 80.0** - This score indicates the model's ability to understand and process natural language across a wide range of tasks. A higher MMLU score suggests better performance in tasks such as text classification, sentiment analysis, and question answering. With a score of 80.0, Mistral Small 4 demonstrates a strong foundation in language understanding.
* **HumanEval Score: None** - HumanEval is a benchmark that evaluates a model's ability to generate code that passes unit tests. The absence of a HumanEval score for Mistral Small 4 makes it difficult to assess its coding capabilities directly. However, its inclusion in the "BEST FOR" list for coding tasks suggests that it may still be suitable for such applications.
* **LMSYS Arena ELO Score: 1200** - The LMSYS Arena ELO score is a measure of a model's performance in a competitive environment, where it is pitted against other models in various tasks. An ELO score of 1200 indicates that Mistral Small 4 has a moderate level of performance, suggesting it can hold its own in a variety of tasks but may struggle against more advanced models.

### Real-World Implications
For real-world use, these benchmark scores imply the following:
* **Language Understanding:** With an MMLU score of 80.0, Mistral Small 4 is capable of handling a wide range of language understanding tasks, making it suitable for applications such as chatbots, text

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral: Mistral Small 4, we will provide a general comparison framework that can be applied to other models in the market. This framework will cover price differences, performance trade-offs, and scenarios where one might prefer Mistral: Mistral Small 4 over others.

#### Pricing Comparison
Mistral: Mistral Small 4 is priced as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens

Without direct competitors, it's challenging to provide a direct price comparison. However, when evaluating other models, consider the following:
- **Input Cost**: Compare the cost per 1M tokens for input. If another model offers a lower input cost, it might be more economical for applications with large input sizes.
- **Output Cost**: Similarly, compare the output cost. Models with lower output costs per 1M tokens might be preferable for applications that generate extensive outputs.

#### Performance Trade-offs
Mistral: Mistral Small 4 has the following benchmarks:
- MMLU: 80.0
- LMSYS Arena ELO: 1200

When comparing with other models, consider:
- **MMLU Score**: A higher MMLU score generally indicates better performance on a wide range of natural language understanding tasks. If another model has a significantly higher MMLU score, it might offer better performance, potentially justifying higher costs.
- **LMSYS Arena ELO**: This score reflects performance in a competitive arena. Higher scores indicate better performance in tasks that require strategic thinking and problem-solving.

#### Choosing the Right Model
Consider the following scenarios when deciding between Mistral: Mistral Small 4 and potential competitors:
- **Chat, Text Generation, and Coding**: Mistral: Mistral Small 4 is well-suited for these tasks due to its capabilities in text, function calling, and structured outputs.
- **Analysis and Summarization**: Its strengths in text analysis and generation make it a good choice for tasks requiring summarization and analysis.
- **RAG Pipelines**: With its support for retrieval-augmented generation (RAG) pipelines, Mistral: Mistral Small 4 can be a good fit for applications that require combining retrieval and generation capabilities.

#### Cost Considerations
When evaluating the cost of using Mistral

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on January 1, 2024, this model is part of the standard tier and is not open source.

### Pricing Model
The pricing for Mistral Small 4 is based on input and output tokens. The costs are as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities, here are the top 5 best use cases for Mistral Small 4:

1. **Chat**: Mistral Small 4 is well-suited for chat applications, given its ability to understand and generate human-like text. Its context window of 262,144 tokens allows for extended conversations.
2. **Text Generation**: With its strong text generation capabilities, Mistral Small 4 can be used for content creation, such as writing articles or generating product descriptions.
3. **Coding**: Mistral Small 4's function calling and structured outputs capabilities make it a good fit for coding tasks, such as generating code snippets or assisting with programming projects.
4. **Analysis**: The model's ability to process and analyze large amounts of text data makes it suitable for tasks like text analysis, sentiment analysis, and topic modeling.
5. **Summarization**: Mistral Small 4 can be used to summarize long pieces of text, extracting key points and main ideas, thanks to its text generation and analysis capabilities.

### Code Integration Example with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following example code:
```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.Model("mistralai/mistral-small-

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
