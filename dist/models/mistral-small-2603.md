# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-08
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral: Mistral Small 4 is designed to handle a wide range of natural language processing tasks with its robust capabilities, including text generation, function calling, JSON mode, streaming, and structured outputs. Its architecture is optimized for performance, with a context window of 262,144 tokens and a maximum output of 4,096 tokens, making it suitable for applications requiring extensive text analysis and generation.

### Strengths and Use Cases
The primary strengths of Mistral: Mistral Small 4 lie in its versatility and performance. With capabilities such as text generation, function calling, and structured outputs, this model is best suited for applications like chat, text generation, coding, analysis, RAG pipelines, and summarization. Its benchmark scores, including an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, demonstrate its competence in handling complex language tasks. However, it's essential to note that its performance may be limited by its knowledge cutoff of 2023-12. Developers can leverage Mistral: Mistral Small 4 for building intelligent systems that require advanced language understanding and generation capabilities.

### Pricing and Cost Considerations
The pricing model for Mistral: Mistral Small 4 is based on input and output tokens. Developers are charged $0.15 per 1M input tokens and $0.6 per 1M output tokens. There are no charges for cached input or batch input. To give developers a better understanding of the costs, examples are provided: 1,000 calls with an average of 500 tokens cost $0.375, while 10,000 calls and 100,000 calls cost $3.75 and

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
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: No additional cost ($None per 1M tokens)
- **Batch Input**: No additional cost ($None per 1M tokens)

#### Optimal Usage Scenarios
- **Cached Tokens**: Since there is no additional cost for cached input tokens, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
- **Batch API Savings**: Although there is no direct cost savings mentioned for batch input, the absence of additional cost implies that batching can be an efficient way to process multiple inputs without incurring extra charges for the input itself. However, the primary cost consideration will still be based on the output tokens generated.

#### Cost at Scale
The cost examples provided give insight into the cost structure at different scales:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These examples suggest a linear scaling of costs with the number of API calls, which is expected given the per-token pricing model.

#### Calculating Costs
To understand the cost implications better, let's consider the cost per token:
- **Input Cost per Token**: $0.15 / 1,000,000 tokens = $0.00000015 per token
- **Output Cost per Token**: $0.6 / 1,000,000 tokens = $0.000000

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

The MMLU score of 80.0 indicates the model's performance on a set of mathematical and logical tasks. A higher MMLU score generally indicates better performance in these areas.

The LMSYS Arena ELO score of 1200 is a measure of the model's performance in a competitive environment, with higher scores indicating better performance. In this case, the score of 1200 suggests that Mistral Small 4 has a moderate level of performance.

The lack of HumanEval and GSM8K scores makes it difficult to evaluate the model's performance in these specific areas.

#### Capabilities and Use Cases
Mistral Small 4 has the

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral: Mistral Small 4, we will provide a general overview of its features, pricing, and performance. This will help users understand the model's strengths and weaknesses and make informed decisions.

#### Model Overview
* **Model:** Mistral: Mistral Small 4 (mistralai/mistral-small-2603)
* **Provider:** Mistralai
* **Release Date:** 2024-01-01
* **Tier:** Standard
* **Open Source:** False

#### Pricing
The pricing for Mistral: Mistral Small 4 is as follows:
* **Input:** $0.15 per 1M tokens
* **Output:** $0.6 per 1M tokens
* **Cached Input:** $None per 1M tokens
* **Batch Input:** $None per 1M tokens

#### Performance and Capabilities
Mistral: Mistral Small 4 has the following performance metrics and capabilities:
* **Context Window:** 262,144 tokens
* **Max Output:** 4,096 tokens
* **Knowledge Cutoff:** 2023-12
* **Benchmarks:**
	+ MMLU: 80.0
	+ LMSYS Arena ELO: 1200
* **Capabilities:** text, function_calling, json_mode, streaming, structured_outputs
* **Best For:** chat, text_generation, coding, analysis, rag_pipelines, summarization

#### Cost Examples
The estimated costs for using Mistral: Mistral Small 4 are:
* **1,000 calls (avg 500 tokens):** $0.375
* **10,000 calls:** $3.75
* **100,000 calls:** $37.5

#### Choosing Mistral: Mistral Small 4
Since there are no direct competitors listed, Mistral: Mistral Small 4 can be considered for a wide range of applications, including:
* Chat and text generation
* Coding and analysis
* RAG pipelines and summarization

However, users should carefully evaluate the model's performance metrics, capabilities, and pricing to ensure it meets their specific needs and budget.

#### Future Considerations
As new models are released, it's essential to compare their features, pricing, and performance to Mistral: Mistral Small

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on January 1, 2024, this model is part of the standard tier and is not open-source.

### Pricing Model
The pricing for Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and ability to generate up to 4,096 tokens of output, Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: Mistral Small 4's function calling and structured outputs capabilities make it a good fit for coding and analysis tasks, such as code completion and data analysis.
3. **Summarization**: The model's ability to process large amounts of text and generate concise summaries makes it a good choice for summarization tasks.
4. **RAG Pipelines**: Mistral Small 4's support for RAG (Retrieve, Augment, Generate) pipelines makes it a good fit for applications that require generating text based on external knowledge sources.
5. **Streaming**: With its streaming capability, Mistral Small 4 can be used for real-time text generation and processing applications.

### Code Integration Example with OpenRouter
Here is an example of how to integrate Mistral Small 4 with OpenRouter:
```python
import openrouter

# Initialize the Mistral Small 4 model

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
