# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-17
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open-source and is part of the Mistral family, specifically `mistralai/mistral-small-2603`. Its architecture is designed to handle a wide range of tasks, including text generation, coding, analysis, and more, with capabilities such as text, function calling, JSON mode, streaming, and structured outputs.

### Technical Specifications and Strengths
Technically, Mistral Small 4 boasts a context window of 262,144 tokens and can generate up to 4,096 tokens as output. The knowledge cutoff for this model is 2023-12, indicating it was trained on data up to that point. The pricing model includes input costs at $0.15 per 1M tokens and output costs at $0.6 per 1M tokens, with no specified costs for cached input or batch input. Benchmarks show an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, demonstrating its capabilities. Its main strengths lie in its versatility and performance across various tasks, making it suitable for applications like chat, text generation, coding, and summarization.

### Use Cases and Cost Considerations
Mistral Small 4 is best utilized for tasks that require a balance of understanding, generation, and analysis capabilities, such as chatbots, text generation tools, coding assistants, and summarization software. The cost of using Mistral Small 4 can be estimated based on the number of calls and tokens processed. For example, 1,000 calls averaging 500 tokens each would cost $0.375, scaling up to $37.5 for 100,000 calls. With no direct competitors listed, Mistral Small 4 stands out as a unique offering in the market, providing a robust set

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
Mistral: Mistral Small 4 is a standard-tier model provided by Mistralai, released on 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale for this model.

#### Cost Structure
The pricing for Mistral: Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens (free)
* Batch Input: $None per 1M tokens (free)

#### Optimal Usage Scenarios
Given the cost structure, it is optimal to use:
* **Cached tokens** when possible, as they are free. This can significantly reduce costs for repeated or similar inputs.
* **Batch API calls** when feasible, as they are also free. This can help reduce the overall cost per call.

#### Cost at Scale
The cost of using Mistral: Mistral Small 4 at scale is as follows:
* **1,000 calls** (avg 500 tokens): $0.375
* **10,000 calls**: $3.75
* **100,000 calls**: $37.5

These costs demonstrate a linear scaling of expenses with the number of API calls, indicating that the cost per call remains constant regardless of the volume.

#### Cost Breakdown
To understand the cost breakdown, let's consider the average cost per token:
* Input: $0.15 per 1M tokens = $0.00015 per token
* Output: $0.6 per 1M tokens = $0.0006 per token

For an average call with 500 tokens, the cost would be:
* Input: 500 tokens \* $0.00015 per token = $0.075
*

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
Mistral Small 4 is a standard-tier model provided by Mistralai, released on January 1, 2024. It is not open source.

#### Pricing
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

#### Benchmarks
The benchmark performance of Mistral Small 4 is as follows:
* MMLU: **80.0**
* HumanEval: **None**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

The MMLU score of 80.0 indicates the model's ability to understand and process natural language. A higher MMLU score generally corresponds to better language understanding capabilities.

The LMSYS Arena ELO score of 1200 is a measure of the model's performance in a competitive environment. ELO scores are used to rank models based on their performance, with higher scores indicating better performance.

The lack of HumanEval and GSM8K scores means that the model's performance on these specific benchmarks is not available.

#### Real-World Use
For real-world use, the MMLU score of 80.0 suggests that Mistral Small 4 can be effective in applications

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral: Mistral Small 4 model, we will provide a general comparison framework that can be applied to other models in the market. This framework will consider key factors such as pricing, performance, and capabilities.

#### Pricing Comparison
The Mistral: Mistral Small 4 model is priced as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens

To compare, we would need the pricing information of its top competitors. However, since this information is not provided, we can only outline the factors to consider when evaluating pricing:
- Input cost per 1M tokens
- Output cost per 1M tokens
- Any discounts for batch inputs or cached inputs

#### Performance Trade-offs
The performance of the Mistral: Mistral Small 4 model can be evaluated based on its benchmarks:
- MMLU: 80.0
- LMSYS Arena ELO: 1200

When comparing with competitors, consider the following:
- MMLU scores: Higher scores generally indicate better performance.
- LMSYS Arena ELO scores: Higher scores indicate better performance in specific tasks.
- Other benchmarks such as HumanEval and GSM8K, if available.

#### Capabilities and Use Cases
The Mistral: Mistral Small 4 model supports the following capabilities:
- text
- function_calling
- json_mode
- streaming
- structured_outputs

It is best suited for tasks such as:
- chat
- text_generation
- coding
- analysis
- rag_pipelines
- summarization

When choosing a model, consider the specific requirements of your project and select a model that supports the necessary capabilities.

#### Cost Examples
The cost of using the Mistral: Mistral Small 4 model can be estimated based on the number of calls and average token count:
- 1,000 calls (avg 500 tokens): $0.375
- 10,000 calls: $3.75
- 100,000 calls: $37.5

When comparing with competitors, consider the cost estimates for similar usage scenarios.

### Conclusion
While there are no direct competitors listed for the Mistral: Mistral Small 4 model, this comparison framework provides a structured approach to evaluating its pricing, performance, and capabilities against other

## Best Use Cases
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and release date of 2024-01-01, this model is well-suited for various applications. In this section, we will explore the top 5 best use cases for Mistral: Mistral Small 4, along with specific code integration examples and mentions of OpenRouter.

### Top 5 Best Use Cases for Mistral: Mistral Small 4
The following are the top 5 best use cases for Mistral: Mistral Small 4, considering its capabilities and limitations:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and max output of 4,096 tokens, Mistral: Mistral Small 4 is ideal for chat and text generation applications. For example, you can integrate Mistral with OpenRouter to generate human-like responses to user input.
2. **Coding and Analysis**: Mistral: Mistral Small 4's function calling and structured outputs capabilities make it suitable for coding and analysis tasks. You can use Mistral to generate code snippets or analyze large datasets.
3. **Summarization**: With its ability to process large amounts of text, Mistral: Mistral Small 4 can be used for summarization tasks, such as summarizing long documents or articles.
4. **RAG Pipelines**: Mistral: Mistral Small 4's support for RAG (Retrieval-Augmented Generation) pipelines makes it a good choice for applications that require generating text based on external knowledge sources.
5. **Streaming and Real-time Applications**: Mistral: Mistral Small 4's streaming capability allows it to process and generate text in real-time, making it suitable for applications such as live chat or real-time text

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
