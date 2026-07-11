# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-11
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of tasks, including text generation, coding, and analysis, thanks to its capabilities in text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens.

### Technical Specifications and Pricing
Technically, Mistral Small 4 operates with a context window of 262,144 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2023-12. The pricing model for Mistral Small 4 is based on input and output tokens. Developers are charged $0.15 per 1M input tokens and $0.6 per 1M output tokens. There are no charges for cached input or batch input. The model has been benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. These specifications and pricing make Mistral Small 4 suitable for applications such as chat, text generation, coding, analysis, and summarization.

### Use Cases and Cost Considerations
Mistral Small 4 is best utilized for tasks that require extensive text processing, function calling, and structured output capabilities. It is particularly suited for chat, text generation, coding, analysis, RAG pipelines, and summarization tasks. The cost of using Mistral Small 4 can be estimated based on the number of calls and average tokens per call. For example, 1,000 calls with an average of 500 tokens per call would cost $0.375, while 10,000 calls would cost $3.75, and

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
Mistral Small 4, provided by Mistralai, is a standard, non-open-source model released on 2024-01-01. This analysis breaks down the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
- **Cached Tokens**: Since cached input tokens are free, it's highly beneficial to utilize cached tokens whenever possible. This can significantly reduce costs, especially for applications with repetitive or similar input patterns.
- **Batch API Calls**: With batch input being free, making batch API calls can lead to substantial savings, especially for high-volume usage scenarios. This is ideal for applications that can process data in batches.

#### Cost at Scale
The cost examples provided give insight into the cost structure at different scales:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These examples illustrate a linear cost increase with the number of API calls, indicating that the cost per call remains constant regardless of the volume.

#### Cost Calculation
To understand the cost breakdown, let's calculate the cost for an average scenario:
- Assume an average input of 500 tokens per call.
- For 1,000 calls, the total input tokens would be 500,000 tokens.
- Given the input cost is $0.15 per 1M tokens, the cost for 500,000 tokens would be $0.075 (500,000 / 

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Mistral: Mistral Small 4 Benchmark Performance
#### Model Overview
The Mistral: Mistral Small 4 model, provided by Mistralai, is a standard-tier model released on January 1, 2024. It is not open-source.

#### Pricing Structure
The pricing for this model is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Context and Limits
The model has the following context and limits:
* Context Window: 262,144 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: December 2023

#### Benchmark Performance
The benchmark performance of the model is as follows:
* MMLU: 80.0
* HumanEval: None
* LMSYS Arena ELO: 1200
* GSM8K: None

#### Interpretation of Benchmark Scores
* **MMLU (Massive Multitask Language Understanding) Score**: An MMLU score of 80.0 indicates the model's ability to understand and perform a wide range of natural language tasks. A higher score generally indicates better performance.
* **HumanEval Score**: Unfortunately, no HumanEval score is available for this model. HumanEval is a benchmark that evaluates a model's ability to write correct Python code. A high HumanEval score would indicate the model's proficiency in coding tasks.
* **LMSYS Arena ELO Score**: An LMSYS Arena ELO score of 1200 is a measure of the model's overall

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral: Mistral Small 4 model, we will provide a general overview of its features, pricing, and performance. This will help users understand the value proposition of this model and make informed decisions about its adoption.

#### Model Overview
The Mistral: Mistral Small 4 model is a standard, non-open-source model released by Mistralai on 2024-01-01. It has a context window of 262,144 tokens and can generate up to 4,096 output tokens.

#### Pricing
The pricing for the Mistral: Mistral Small 4 model is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Performance Trade-offs
The model has the following benchmark scores:
* MMLU: 80.0
* LMSYS Arena ELO: 1200

These scores indicate that the model has a moderate level of performance, suitable for a variety of applications.

#### Capabilities and Best Use Cases
The Mistral: Mistral Small 4 model supports the following capabilities:
* text
* function_calling
* json_mode
* streaming
* structured_outputs

It is best suited for the following applications:
* chat
* text_generation
* coding
* analysis
* rag_pipelines
* summarization

#### Cost Examples
The estimated costs for using the Mistral: Mistral Small 4 model are:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

### Choosing the Mistral: Mistral Small 4 Model
Given the lack of direct competitors, the decision to choose the Mistral: Mistral Small 4 model depends on the specific requirements of the project. If the project requires a standard, non-open-source model with a moderate level of performance and support for a variety of capabilities, the Mistral: Mistral Small 4 model may be a good choice.

However, users should carefully evaluate the pricing and performance trade-offs to ensure that the model meets their needs and budget. Additionally, users should consider

## Best Use Cases
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on 2024-01-01, this model is classified as a standard, non-open source model.

### Pricing Model
The pricing for Mistral: Mistral Small 4 is based on input and output tokens. The costs are as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens

### Top 5 Best Use Cases for Mistral: Mistral Small 4
Given its capabilities, here are the top 5 best use cases for Mistral: Mistral Small 4:

1. **Chat and Text Generation**: With its ability to generate human-like text and engage in conversations, Mistral: Mistral Small 4 is ideal for chatbots and virtual assistants.
2. **Coding and Analysis**: The model's function calling and structured outputs capabilities make it suitable for coding tasks, such as code completion and analysis.
3. **Summarization**: Mistral: Mistral Small 4 can be used to summarize long pieces of text, extracting key points and main ideas.
4. **RAG Pipelines**: The model's ability to generate text and engage in conversations makes it a good fit for RAG (Retrieve, Augment, Generate) pipelines.
5. **Streaming**: With its support for streaming, Mistral: Mistral Small 4 can be used for real-time text generation and analysis.

### Code Integration Example with OpenRouter
To integrate Mistral: Mistral Small 4 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the OpenRouter client
client = openrouter.Client()

# Set the model and provider
model = "mistralai/m

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
