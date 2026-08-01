# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-01
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open-source. From an architectural standpoint, Mistral Small 4 is designed to handle a wide range of natural language processing tasks with its robust capabilities, including text generation, function calling, JSON mode, streaming, and structured outputs. Its strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens, making it suitable for complex tasks.

### Technical Capabilities and Use Cases
The primary use cases for Mistral: Mistral Small 4 include chat, text generation, coding, analysis, RAG pipelines, and summarization. It boasts a context window of 262,144 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2023-12. The model's technical capabilities are further highlighted by its benchmark scores, including an MMLU score of 80.0 and an LMSYS Arena ELO score of 1200. However, it's essential to note the areas where it may not perform optimally, as indicated by the lack of direct competitors and specific benchmark scores like HumanEval and GSM8K.

### Pricing and Cost Considerations
The pricing for Mistral: Mistral Small 4 is structured around input and output tokens. Developers are charged $0.15 per 1M input tokens and $0.6 per 1M output tokens. There are no charges for cached input or batch input. To put this into perspective, the cost examples provided indicate that 1,000 calls with an average of 500 tokens would cost $0.375, scaling up to $3.75 for 10,000 calls and $37.5 for 100,000 calls. Understanding these pricing

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
Mistral Small 4, provided by Mistralai, is a standard tier model released on 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: No additional cost ($None per 1M tokens)
- **Batch Input**: No additional cost ($None per 1M tokens)

This structure indicates that the primary cost drivers are the input and output token counts. Cached and batch inputs do not incur additional costs, suggesting potential savings through efficient usage patterns.

#### When to Use Cached Tokens
Given that cached input tokens do not incur any additional cost, it is beneficial to use cached tokens whenever possible. This can significantly reduce the overall cost, especially in scenarios where the same input is processed multiple times. However, the specific implementation and availability of cached tokens are not detailed in the provided data.

#### Batch API Savings
The absence of additional costs for batch input suggests that processing inputs in batches can be an efficient way to reduce costs. By batching API calls, users can potentially minimize the overhead associated with individual requests, leading to cost savings. However, the exact nature of these savings is not quantifiable without more detailed information on batch processing limits and efficiency gains.

#### Cost at Scale
The provided cost examples give insight into the cost structure at different scales:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These examples suggest a linear cost scaling, where the cost increases directly with the number of API calls. This linear relationship indicates that the cost

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

#### Pricing
The pricing for Mistral Small 4 is as follows:
- Input: **$0.15 per 1M tokens**
- Output: **$0.6 per 1M tokens**
- Cached Input: **$None per 1M tokens**
- Batch Input: **$None per 1M tokens**

#### Context and Limits
The model has the following context and limits:
- Context Window: **262,144 tokens**
- Max Output: **4,096 tokens**
- Knowledge Cutoff: **2023-12**

#### Benchmarks
The model's benchmark performance is as follows:
- **MMLU: 80.0**: This score indicates the model's performance on a specific set of tasks, with higher scores representing better performance. An MMLU score of 80.0 suggests that Mistral Small 4 has a good level of performance, but the exact meaning depends on the specific tasks and comparisons.
- **HumanEval: None**: The lack of a HumanEval score means that the model's performance on human evaluation tasks is not available.
- **LMSYS Arena ELO: 1200**: The LMSYS Arena ELO score is a measure of the model's performance in a competitive arena, with higher scores indicating better performance. An ELO score of 1200 suggests that Mistral Small 4 has a moderate level of performance in this arena.

#### Real-World Implications
For real-world use,

## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral Small 4 model, we will provide a general analysis of its pricing, performance, and capabilities to help users decide when to choose this model.

#### Pricing
The Mistral Small 4 model is priced as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Performance Trade-offs
The Mistral Small 4 model has the following performance characteristics:
* Context Window: 262,144 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2023-12
* Benchmarks:
	+ MMLU: 80.0
	+ LMSYS Arena ELO: 1200

#### Capabilities and Use Cases
The Mistral Small 4 model supports the following capabilities:
* Text
* Function calling
* JSON mode
* Streaming
* Structured outputs
It is best suited for the following use cases:
* Chat
* Text generation
* Coding
* Analysis
* RAG pipelines
* Summarization

#### Cost Examples
The estimated costs for using the Mistral Small 4 model are:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

#### Choosing the Mistral Small 4 Model
Based on its pricing, performance, and capabilities, the Mistral Small 4 model is a good choice for users who need a standard-tier model with a large context window and support for various capabilities such as text, function calling, and structured outputs. However, users should consider the following factors when deciding whether to choose this model:
* The model's knowledge cutoff is 2023-12, which may not be suitable for applications that require more recent knowledge.
* The model's performance on certain benchmarks such as HumanEval and GSM8K is not available, which may be a concern for users who need to evaluate the model's performance on these specific tasks.
* The model is not open-source, which may be a limitation for users who need to customize or modify the model for their specific use cases.

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on 2024-01-01, this model is part of the standard tier and is not open source.

### Pricing Model
The pricing for Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities, here are the top 5 best use cases for Mistral Small 4:

1. **Chat**: With its ability to generate human-like text, Mistral Small 4 is well-suited for chat applications. For example, you can use it to power a chatbot that responds to user queries.
2. **Text Generation**: Mistral Small 4 can be used for text generation tasks such as writing articles, creating content, and more. Its ability to generate coherent and context-specific text makes it an ideal choice for such tasks.
3. **Coding**: Mistral Small 4's function calling capability makes it a great tool for coding tasks. You can use it to generate code snippets, complete partial code, and more.
4. **Analysis**: With its ability to process and analyze large amounts of text data, Mistral Small 4 is well-suited for analysis tasks such as sentiment analysis, entity recognition, and more.
5. **Summarization**: Mistral Small 4 can be used to summarize long pieces of text into concise and meaningful summaries. This makes it an ideal choice for applications such as news summarization, document summarization, and more.

### Code Integration Example with OpenRouter
Here is

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
