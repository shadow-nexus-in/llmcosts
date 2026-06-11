# Inception: Mercury 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-11
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Inception: Mercury 2
Inception: Mercury 2 (inception/mercury-2) is a standard-tier model provided by Inception, released on 2024-01-01. This model is not open source. From an architectural standpoint, specific details about the model's design are not provided, but its capabilities and performance metrics offer insights into its strengths and use cases. Inception: Mercury 2 is capable of handling a variety of tasks, including text generation, function calling, JSON mode, streaming, and producing structured outputs.

### Strengths and Use Cases
The main strengths of Inception: Mercury 2 lie in its ability to handle complex tasks such as chat, text generation, coding, analysis, RAG pipelines, and summarization. With a context window of 128,000 tokens and a maximum output of 50,000 tokens, this model is well-suited for applications requiring detailed and lengthy responses. Its performance is also reflected in its benchmarks, with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. However, it's essential to note the knowledge cutoff of 2023-12, indicating that the model's training data does not include information beyond this date. Pricing for the model includes $0.25 per 1M tokens for input and $0.75 per 1M tokens for output.

### Pricing and Cost Examples
Developers looking to integrate Inception: Mercury 2 into their applications should be aware of the pricing structure. The model charges $0.25 per 1M tokens for input and $0.75 per 1M tokens for output. There are no charges listed for cached input or batch input. To give developers a better understanding of the costs, examples are provided: 1,000 calls averaging 500 tokens would cost $0.5, 10,000 calls would cost $5.0, and 100

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.25 |
| Output | $0.75 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Inception: Mercury 2
#### Overview
Inception: Mercury 2 is a standard, non-open-source model provided by Inception, released on January 1, 2024. This analysis will delve into the cost structure, optimal usage scenarios, and scaling costs for this model.

#### Cost Structure
The pricing for Inception: Mercury 2 is as follows:
- **Input**: $0.25 per 1 million tokens
- **Output**: $0.75 per 1 million tokens
- **Cached Input**: No additional cost per 1 million tokens
- **Batch Input**: No additional cost per 1 million tokens

#### Optimal Usage Scenarios
- **Cached Tokens**: Since there is no additional cost for cached input tokens, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
- **Batch API Savings**: Although there is no direct cost savings mentioned for batch inputs, batching can still lead to efficiency gains in terms of API call reduction. However, the pricing does not differentiate between batch and non-batch inputs in terms of cost per token.

#### Cost at Scale
Given the average cost examples provided:
- **1,000 calls (avg 500 tokens)**: $0.5
- **10,000 calls**: $5.0
- **100,000 calls**: $50.0

These examples suggest a linear scaling of costs with the number of API calls. To estimate costs for different scenarios, we can use these examples as a baseline.

### Calculating Costs Based on Tokens
Given the input and output pricing:
- For every 1 million input tokens, the cost is $0.25.
- For every 1 million output tokens, the cost is $0.75.

To calculate the cost for a specific number of tokens, you can use the following formula:
\[ \text{Cost} = \left( \frac{\text{Input Tokens}}{1,000

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Inception: Mercury 2 Benchmark Performance Analysis
#### Model Overview
The Inception: Mercury 2 model, released on 2024-01-01, is a standard-tier model provided by Inception. It is not open source.

#### Pricing
The pricing for Inception: Mercury 2 is as follows:
* Input: $0.25 per 1M tokens
* Output: $0.75 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Context and Limits
The model has the following context and limits:
* Context Window: 128,000 tokens
* Max Output: 50,000 tokens
* Knowledge Cutoff: 2023-12

#### Benchmarks
The benchmark performance of Inception: Mercury 2 is as follows:
* MMLU: **80.0**
* HumanEval: **None**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

The MMLU score of 80.0 indicates the model's performance on a set of mathematical and logical tasks. A higher MMLU score generally indicates better performance on these types of tasks.

The LMSYS Arena ELO score of 1200 is a measure of the model's overall performance in a competitive setting. A higher ELO score indicates better performance compared to other models.

The lack of HumanEval and GSM8K scores means that the model's performance on these specific benchmarks is not available.

#### Real-World Use
The capabilities of Inception: Mercury 2 include:
* text
* function_calling
* json_mode
* streaming

## Competitor Comparison
### Inception: Mercury 2 Comparison
Since there are no direct competitors listed for the Inception: Mercury 2 model, we will provide a general overview of its features, pricing, and performance. This will help users understand when to choose this model and what to expect from it.

#### Model Overview
The Inception: Mercury 2 model is a standard-tier model provided by Inception, released on January 1, 2024. It is not open-source.

#### Pricing
The pricing for the Inception: Mercury 2 model is as follows:
* Input: $0.25 per 1M tokens
* Output: $0.75 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Performance and Limits
The model has the following performance characteristics and limits:
* Context Window: 128,000 tokens
* Max Output: 50,000 tokens
* Knowledge Cutoff: 2023-12
* Benchmarks:
	+ MMLU: 80.0
	+ LMSYS Arena ELO: 1200

#### Capabilities and Use Cases
The Inception: Mercury 2 model supports the following capabilities:
* text
* function_calling
* json_mode
* streaming
* structured_outputs
It is best suited for the following use cases:
* chat
* text_generation
* coding
* analysis
* rag_pipelines
* summarization

#### Cost Examples
The cost of using the Inception: Mercury 2 model can be estimated as follows:
* 1,000 calls (avg 500 tokens): $0.5
* 10,000 calls: $5.0
* 100,000 calls: $50.0

#### Choosing the Inception: Mercury 2 Model
Given the lack of direct competitors, the decision to choose the Inception: Mercury 2 model will depend on the specific requirements of your project. Consider the following factors:
* **Pricing**: If your project requires a large number of input or output tokens, the Inception: Mercury 2 model may be a cost-effective option.
* **Performance**: If your project requires a high level of performance, as measured by the MMLU and LMSYS Arena ELO benchmarks, the Inception: Mercury 2 model may be a good choice.
* **Capabilities**: If your

## Best Use Cases
### Introduction to Inception: Mercury 2
Inception: Mercury 2 is a powerful model released by Inception on 2024-01-01, offering a range of capabilities including text, function calling, JSON mode, streaming, and structured outputs. With its standard tier and non-open source status, it's essential to understand its pricing, context, and limits to maximize its potential.

### Pricing and Cost Examples
The pricing for Inception: Mercury 2 is as follows:
* Input: $0.25 per 1M tokens
* Output: $0.75 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

Cost examples:
* 1,000 calls (avg 500 tokens): $0.5
* 10,000 calls: $5.0
* 100,000 calls: $50.0

### Top 5 Best Use Cases for Inception: Mercury 2
Based on its capabilities and benchmarks, here are the top 5 best use cases for Inception: Mercury 2:

1. **Chat and Text Generation**: With its high MMLU score of 80.0 and support for text and structured outputs, Inception: Mercury 2 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: Its function calling and JSON mode capabilities make it an excellent choice for coding and analysis tasks, such as code completion and data analysis.
3. **Summarization**: Inception: Mercury 2's ability to process large context windows (up to 128,000 tokens) and generate structured outputs makes it a strong candidate for summarization tasks.
4. **RAG Pipelines**: Its support for streaming and structured outputs enables Inception: Mercury 2 to be used in RAG (Retrieve, Augment, Generate) pipelines for tasks like question answering and text generation.
5

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
