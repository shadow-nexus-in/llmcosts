# NVIDIA: Nemotron 3 Super API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-03
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super, released on 2024-01-01, is a high-performance model developed by Nvidia. This standard-tier model is not open source and is identified by the name `nvidia/nemotron-3-super-120b-a12b`. With its robust architecture, the Nemotron 3 Super excels in various tasks, including text generation, coding, analysis, and summarization. Its capabilities extend to handling text, function calling, JSON mode, streaming, and structured outputs, making it a versatile tool for developers.

### Technical Specifications and Pricing
The Nemotron 3 Super boasts an impressive context window of 262,144 tokens and can generate up to 4,096 tokens as output. Its knowledge cutoff is 2023-12, ensuring it has a broad and up-to-date understanding of the world. In terms of pricing, the model costs $0.1 per 1M tokens for input and $0.5 per 1M tokens for output. For example, 1,000 calls with an average of 500 tokens would cost $0.3, while 10,000 calls would amount to $3.0, and 100,000 calls would be $30.0. The model's performance is reflected in its benchmarks, with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200.

### Use Cases and Competitors
The Nemotron 3 Super is best suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization. Its strengths lie in its ability to handle complex tasks with ease, making it an ideal choice for developers working on projects that require advanced language understanding and generation capabilities. Currently, there are no direct competitors listed for the Nemotron 3 Super, solidifying its position as a unique and powerful tool in the market. With its

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
The NVIDIA Nemotron 3 Super is a standard-tier model provided by Nvidia, released on January 1, 2024. This model is not open source and has a specific pricing structure based on input and output tokens.

#### Cost Structure
The cost structure for the NVIDIA Nemotron 3 Super is as follows:
* **Input**: $0.1 per 1M tokens
* **Output**: $0.5 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs when the same input is used multiple times. Since cached input is free, it is recommended to use cached tokens whenever possible to minimize input costs.

#### Batch API Savings
Batch input is also free, which means that making batch API calls can help reduce costs. By batching multiple requests together, users can take advantage of the free batch input pricing and reduce their overall costs.

#### Cost at Scale
The cost of using the NVIDIA Nemotron 3 Super at scale is as follows:
* **1,000 calls (avg 500 tokens)**: $0.3
* **10,000 calls**: $3.0
* **100,000 calls**: $30.0

These costs demonstrate a linear scaling of costs with the number of API calls, indicating that the pricing structure is straightforward and easy to predict.

#### Context and Limits
The NVIDIA Nemotron 3 Super has the following context and limits:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12

These limits should be taken into account when designing applications that use the NVIDIA Nemotron 3 Super to ensure that they are used within the recommended guidelines.

#### Cap

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### NVIDIA Nemotron 3 Super Benchmark Analysis
#### Overview
The NVIDIA Nemotron 3 Super is a standard, non-open-source model released by Nvidia on January 1, 2024. This analysis will delve into its benchmark performance, focusing on the MMLU, HumanEval, and Arena ELO scores, and explain their implications for real-world use.

#### Benchmark Scores
- **MMLU (Massive Multitask Language Understanding) Score: 80.0**
  The MMLU score evaluates a model's ability to perform a wide range of natural language processing tasks. A score of 80.0 indicates that the NVIDIA Nemotron 3 Super has a strong foundation in understanding and generating human-like text across various tasks. This suggests it can be effectively used for applications requiring broad language understanding, such as chatbots, text generation, and analysis.

- **HumanEval Score: None**
  The HumanEval benchmark assesses a model's ability to generate correct code based on human-written prompts. Unfortunately, without a HumanEval score, it's challenging to directly compare the Nemotron 3 Super's coding capabilities to other models. However, given its listing under "BEST FOR" as suitable for coding, it implies the model has some level of proficiency in this area, albeit unquantified in this context.

- **LMSYS Arena ELO Score: 1200**
  The Arena ELO score is a measure of a model's performance in a competitive environment, often involving tasks that require strategic thinking and problem-solving. An ELO score of 1200 suggests that the Nemotron 3 Super has a moderate level of competence in such tasks. For real-world applications, this means the model can handle

## Competitor Comparison
### NVIDIA Nemotron 3 Super Comparison
#### Introduction
The NVIDIA Nemotron 3 Super is a standard-tier model released by Nvidia on 2024-01-01. With no direct competitors listed, this comparison will focus on the model's pricing, performance, and capabilities to help users determine when to choose this model.

#### Pricing
The NVIDIA Nemotron 3 Super pricing is as follows:
* Input: $0.1 per 1M tokens
* Output: $0.5 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Performance Trade-offs
The model's performance is measured by the following benchmarks:
* MMLU: 80.0
* LMSYS Arena ELO: 1200
While there are no direct competitors, these benchmarks indicate the model's capabilities in various tasks.

#### Capabilities and Use Cases
The NVIDIA Nemotron 3 Super supports the following capabilities:
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
To help estimate costs, the following examples are provided:
* 1,000 calls (avg 500 tokens): $0.3
* 10,000 calls: $3.0
* 100,000 calls: $30.0

#### Choosing the NVIDIA Nemotron 3 Super
Given the lack of direct competitors, the decision to choose this model depends on the specific use case and requirements. Consider the following factors:
* **Context Window**: 262,144 tokens, suitable for tasks requiring a large input context.
* **Max Output**: 4,096 tokens, suitable for tasks requiring a moderate output length.
* **Knowledge Cutoff**: 2023-12, suitable for tasks that do not require knowledge beyond this date.
* **Capabilities**: Supports a range of capabilities, including text, function_calling, and structured_outputs.

In conclusion, the NVIDIA Nemotron 3 Super is a standard-tier model with a unique set of capabilities and pricing. While there are no direct competitors, users can evaluate this model based on their specific requirements and use cases.

## Best Use Cases
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super is a powerful language model released by Nvidia on 2024-01-01. With its impressive capabilities, including text generation, function calling, and structured outputs, it is an ideal choice for various applications. In this guide, we will explore the top 5 best use cases for the NVIDIA Nemotron 3 Super, along with code integration examples using OpenRouter.

### Top 5 Use Cases for NVIDIA Nemotron 3 Super
#### 1. **Chat and Text Generation**
The NVIDIA Nemotron 3 Super excels in chat and text generation tasks, making it suitable for conversational AI applications. With its large context window of 262,144 tokens, it can engage in lengthy conversations while maintaining context.

#### 2. **Coding and Analysis**
The model's ability to perform function calling and generate structured outputs makes it an excellent choice for coding and analysis tasks. It can be used to generate code snippets, analyze code quality, and even assist in debugging.

#### 3. **Summarization and RAG Pipelines**
The NVIDIA Nemotron 3 Super is well-suited for summarization tasks, thanks to its ability to process large amounts of text and generate concise summaries. It can also be used in RAG (Retrieval-Augmented Generation) pipelines to improve the accuracy of generated text.

#### 4. **Text Analysis and Insights**
With its impressive capabilities in text analysis, the NVIDIA Nemotron 3 Super can be used to gain insights from large datasets. It can perform tasks such as sentiment analysis, entity recognition, and topic modeling.

#### 5. **Streaming and Real-time Applications**
The model's support for streaming and real-time applications makes it an excellent choice for applications that require immediate responses, such as live chatbots or real-time text analysis.

### Code Integration Examples with OpenRouter
To integrate the NVIDIA Nemotron 3 Super with OpenRouter, you

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
