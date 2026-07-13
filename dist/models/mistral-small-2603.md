# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-13
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of tasks, including text generation, function calling, and structured outputs. Its capabilities are diverse, supporting text, function_calling, json_mode, streaming, and structured_outputs, making it a versatile tool for developers.

### Strengths and Use Cases
The main strengths of Mistral Small 4 lie in its ability to perform well in chat, text_generation, coding, analysis, rag_pipelines, and summarization tasks. With a context window of 262,144 tokens and a maximum output of 4,096 tokens, it is well-suited for applications that require generating or processing significant amounts of text. The model's pricing is based on input and output tokens, with costs of $0.15 per 1M input tokens and $0.6 per 1M output tokens. This pricing structure makes it accessible for a range of use cases, from small-scale development projects to larger applications.

### Technical Specifications and Pricing
Technically, Mistral Small 4 has a knowledge cutoff of 2023-12 and achieves an MMLU score of 80.0, along with an LMSYS Arena ELO of 1200. For developers considering the cost, examples include $0.375 for 1,000 calls averaging 500 tokens, $3.75 for 10,000 calls, and $37.5 for 100,000 calls. Given its capabilities and pricing, Mistral Small 4 is positioned as a competitive option for tasks that require robust text processing and generation capabilities, although it does not have direct competitors listed. Its performance metrics and pricing structure make it an attractive choice for applications where text analysis and generation are core functionalities.

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
Mistral Small 4, provided by Mistralai, is a standard, non-open-source model released on 2024-01-01. This analysis breaks down its cost structure, usage scenarios, and scalability.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* **Input**: $0.15 per 1M tokens
* **Output**: $0.6 per 1M tokens
* **Cached Input**: No additional cost ($None per 1M tokens)
* **Batch Input**: No additional cost ($None per 1M tokens)

#### Usage Scenarios
* **Cached Tokens**: Since there is no additional cost for cached input tokens, it is always beneficial to use cached tokens when possible. This can significantly reduce the overall cost of API calls.
* **Batch API Savings**: Although there is no direct cost savings for batch input, batching can still improve efficiency and reduce the number of API calls needed. However, the cost will be calculated based on the total number of input and output tokens.

#### Cost at Scale
The cost of using Mistral Small 4 at different scales is as follows:
* **1,000 calls (avg 500 tokens)**: $0.375
* **10,000 calls**: $3.75
* **100,000 calls**: $37.5

These costs demonstrate a linear relationship with the number of API calls, indicating that the cost per call remains constant.

#### Context and Limits
It's essential to consider the context window and output limits when using Mistral Small 4:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12

These limits can impact the effectiveness of the model for specific use cases.

#### Capabilities and Best Use Cases
Mistral Small 4 supports various capabilities,

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Benchmark Analysis
The Mistral Small 4 model, provided by Mistralai, is a standard, non-open-source model released on January 1, 2024. This analysis will delve into its benchmark performance, focusing on the MMLU, HumanEval, and Arena ELO scores, and explore their implications for real-world use.

#### Benchmark Scores
- **MMLU (Massive Multitask Language Understanding) Score**: 80.0
  The MMLU score is a measure of a model's ability to understand and perform a wide range of natural language processing tasks. A score of 80.0 indicates that Mistral Small 4 has a good level of language understanding, capable of handling various tasks with reasonable accuracy. However, the exact implications depend on the specific tasks and the baseline scores for comparison.

- **HumanEval Score**: None
  HumanEval is a benchmark that evaluates a model's ability to generate code based on human-written tests. The lack of a HumanEval score for Mistral Small 4 makes it difficult to assess its coding capabilities directly against other models. This absence of data may indicate that the model is not optimized or tested for code generation tasks.

- **LMSYS Arena ELO Score**: 1200
  The LMSYS Arena ELO score is a measure of a model's performance in a competitive setting, often involving tasks that require strategic thinking, problem-solving, and sometimes coding. An ELO score of 1200 suggests that Mistral Small 4 has a moderate level of proficiency in these areas. For context, ELO scores are used in chess and other competitive games to measure the relative skill levels of players. In the

## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral Small 4 model, we will provide a general comparison framework that can be applied to other models in the market. This framework will consider key factors such as pricing, performance, and capabilities.

#### Pricing Comparison
The Mistral Small 4 model is priced as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens

To compare, let's consider a hypothetical competitor model, "Competitor X", with the following pricing:
- Input: $0.20 per 1M tokens
- Output: $0.50 per 1M tokens

Based on these prices, the Mistral Small 4 model is more expensive for output tokens but cheaper for input tokens compared to Competitor X.

#### Performance Trade-offs
The Mistral Small 4 model has the following performance metrics:
- MMLU: 80.0
- LMSYS Arena ELO: 1200

Competitor X may have different performance metrics, such as:
- MMLU: 75.0
- LMSYS Arena ELO: 1100

In this scenario, the Mistral Small 4 model has a higher MMLU score and LMSYS Arena ELO rating, indicating better performance. However, the actual performance difference may vary depending on the specific use case and application.

#### Capabilities and Use Cases
The Mistral Small 4 model supports the following capabilities:
- text
- function_calling
- json_mode
- streaming
- structured_outputs

It is best suited for applications such as:
- chat
- text_generation
- coding
- analysis
- rag_pipelines
- summarization

When choosing between the Mistral Small 4 model and Competitor X, consider the specific requirements of your project. If you need a model with strong performance and a wide range of capabilities, the Mistral Small 4 model may be a better choice. However, if you prioritize cost-effectiveness and are willing to compromise on performance, Competitor X may be a more suitable option.

#### Cost Examples
The cost of using the Mistral Small 4 model can be estimated as follows:
- 1,000 calls (avg 500 tokens): $0.375
- 10,000 calls: $3.75
- 

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on 2024-01-01, this model is part of the standard tier and is not open-source.

### Pricing Model
The pricing for Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its ability to generate human-like text, Mistral Small 4 is ideal for chat applications, content generation, and text summarization.
2. **Coding and Function Calling**: Mistral Small 4's function calling capability makes it suitable for coding tasks, such as generating code snippets, debugging, and code review.
3. **Analysis and Summarization**: This model can be used for data analysis, report generation, and summarization of large documents.
4. **RAG Pipelines**: Mistral Small 4's ability to handle structured outputs makes it a good fit for RAG (Retrieval-Augmented Generation) pipelines, which involve retrieving information from a knowledge base and generating text based on that information.
5. **Streaming and Real-time Applications**: With its support for streaming, Mistral Small 4 can be used for real-time applications, such as live chat, sentiment analysis, and event detection.

### Code Integration Example with OpenRouter
Here's an example of how to integrate Mistral Small 4 with OpenRouter:
```python
import openrouter

# Initialize the Mistral

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
