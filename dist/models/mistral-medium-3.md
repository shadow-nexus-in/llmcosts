# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-28
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance between performance and cost. As a non-open source model, it is designed to provide reliable and efficient processing for a variety of tasks. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, Mistral Medium 3 is capable of handling complex inputs and generating substantial responses. Its knowledge cutoff is 2024-11, ensuring that it has been trained on a vast amount of data up to that point.

### Architecture and Strengths
Mistral Medium 3 boasts an impressive set of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. Its strengths lie in its ability to perform tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling. The model's architecture is designed to support these use cases, with a pricing structure that reflects its mid-tier positioning: $0.4 per 1M input tokens and $2.0 per 1M output tokens. Benchmarks such as MMLU (80.0), HumanEval (77.5), and LMSYS Arena ELO (1200) demonstrate the model's capabilities, although it is not well-suited for tasks like frontier reasoning, bulk cheap tasks, simple classification, or real-time sub-100ms responses.

### Use Cases and Cost Considerations
Developers can leverage Mistral Medium 3 for a range of applications, from coding and analysis to vision tasks and content generation. The model's pricing structure makes it an attractive option for those who require a balance between performance and cost. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 10,000 calls would cost $12.0, and 100

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.4 |
| Output | $2.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Mistral Medium 3
#### Overview
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. It is not open source. This analysis breaks down the cost structure, optimal usage scenarios, and provides cost estimates at scale.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
- **Input**: $0.4 per 1M tokens
- **Output**: $2.0 per 1M tokens
- **Cached Input**: No charge ($None per 1M tokens)
- **Batch Input**: No charge ($None per 1M tokens)

#### Optimal Usage Scenarios
- **Cached Tokens**: Since there is no charge for cached input tokens, it is highly beneficial to utilize cached tokens whenever possible to minimize costs.
- **Batch API Savings**: Although batch input is listed as having no charge, the actual cost savings come from optimizing the input and output token counts per API call. This can lead to significant reductions in the total number of tokens processed, thus lowering the overall cost.

#### Cost at Scale
Given the average cost per call and the pricing structure, we can estimate costs at different scales:
- **1,000 calls (avg 500 tokens)**: $1.2
- **10,000 calls**: $12.0
- **100,000 calls**: $120.0

These estimates are based on the provided cost examples and assume an average token count per call that aligns with the pricing structure.

#### Comparison with Competitors
Mistral Medium 3's pricing is competitive, especially considering its capabilities and performance benchmarks:
- **Claude 3.5 Haiku**: $0.8/1M input, $4.0/1M output
- **GPT-4o Mini**: $0.15/1M input, $0.6/1M output

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Mistral Medium 3 Benchmark Performance
#### Model Overview
The Mistral Medium 3 model, released by Mistral AI on 2025-04-17, is a mid-tier model with the following key characteristics:
* **Model Name:** Mistral Medium 3 (mistralai/mistral-medium-3)
* **Provider:** Mistral AI
* **Release Date:** 2025-04-17
* **Tier:** Mid
* **Open Source:** False

#### Pricing
The pricing for Mistral Medium 3 is as follows:
* **Input:** $0.4 per 1M tokens
* **Output:** $2.0 per 1M tokens
* **Cached Input:** $None per 1M tokens
* **Batch Input:** $None per 1M tokens

#### Context and Limits
The model has the following context and limits:
* **Context Window:** 131,072 tokens
* **Max Output:** 16,384 tokens
* **Knowledge Cutoff:** 2024-11

#### Benchmarks
The model's benchmark performance is as follows:
* **MMLU:** 80.0
* **HumanEval:** 77.5
* **LMSYS Arena ELO:** 1200
* **GSM8K:** None

#### Capabilities and Use Cases
Mistral Medium 3 supports the following capabilities:
* Text
* Vision
* Function calling
* JSON mode
* Streaming
* System prompts

It is best suited for tasks such as:
* Coding
* Analysis
* RAG (Retrieval-Augmented Generation)
* Summarization
* Vision tasks


## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a unique set of capabilities and pricing. This comparison will delve into the details of Mistral Medium 3 and its top competitors, Claude 3.5 Haiku and GPT-4o Mini, highlighting their differences in pricing, performance, and use cases.

#### Pricing Comparison
The pricing models of these three competitors are as follows:

* **Mistral Medium 3**:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* **Claude 3.5 Haiku**:
	+ Input: $0.8 per 1M tokens (100% more than Mistral Medium 3)
	+ Output: $4.0 per 1M tokens (100% more than Mistral Medium 3)
* **GPT-4o Mini**:
	+ Input: $0.15 per 1M tokens (62.5% less than Mistral Medium 3)
	+ Output: $0.6 per 1M tokens (70% less than Mistral Medium 3)

#### Performance Trade-offs
The performance of these models can be evaluated using various benchmarks:

* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

While the exact performance metrics for Claude 3.5 Haiku and GPT-4o Mini are not available, Mistral Medium 3's benchmarks suggest a strong performance in coding, analysis, and other tasks.

#### Context and Limits
The context window and output limits for Mistral Medium 3 are:

* **Context Window**: 131,072 tokens
* **Max Output**: 16,384 tokens
* **Knowledge Cutoff**: 2024-11

These limits are not provided for Claude 3.5 Haiku and GPT-4o Mini, making it difficult to compare their capabilities directly.

#### Capabilities and Use Cases
Mistral Medium 3 is best suited for tasks such as

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful language model released on 2025-04-17. With its mid-tier pricing and extensive capabilities, it's an attractive option for various applications. This guide will explore the top 5 best use cases for Mistral Medium 3, along with code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Medium 3
Based on its capabilities and pricing, the top 5 use cases for Mistral Medium 3 are:

1. **Coding and Analysis**: Mistral Medium 3 excels in coding tasks, making it suitable for code review, code generation, and analysis. Its `function_calling` capability allows for seamless integration with external functions.
2. **Summarization and Content Generation**: With its strong text capabilities, Mistral Medium 3 is ideal for summarization, content generation, and text analysis tasks.
3. **Vision Tasks**: Mistral Medium 3's `vision` capability enables it to process and generate images, making it suitable for image classification, object detection, and image generation tasks.
4. **RAG (Retrieve, Augment, Generate) Tasks**: Mistral Medium 3's `rag` capability allows it to retrieve information, augment existing text, and generate new content, making it suitable for tasks like question answering and text completion.
5. **Complex Text Analysis**: Mistral Medium 3's `analysis` capability enables it to perform complex text analysis tasks, such as sentiment analysis, entity recognition, and topic modeling.

### Code Integration Examples with OpenRouter
To integrate Mistral Medium 3 with OpenRouter, you can use the following code examples:
```python
import openrouter

# Initialize OpenRouter with Mistral Medium 3
router = openrouter.Router(model="mistralai/mistral-medium-3")

# Example 1: Coding task - Generate a Python function

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
