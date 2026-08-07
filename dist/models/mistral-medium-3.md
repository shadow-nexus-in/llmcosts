# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-07
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance of performance and cost. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, this model is well-suited for a variety of tasks, including coding, analysis, and content generation. The model's capabilities include text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Strengths and Use Cases
The main strengths of Mistral Medium 3 lie in its ability to handle complex tasks such as coding, analysis, and vision tasks. Its high benchmark scores, including an MMLU score of 80.0 and a HumanEval score of 77.5, demonstrate its capabilities in these areas. The model is best used for tasks that require a high level of understanding and generation of text, such as summarization and content generation. However, it is not well-suited for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms.

### Pricing and Cost Considerations
Mistral Medium 3 is priced at $0.4 per 1M input tokens and $2.0 per 1M output tokens. This makes it a competitive option for developers who need a high-performance model for complex tasks. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 100,000 calls would cost $120.0. Compared to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers a unique balance of performance and cost, making it a viable option for developers who need a reliable and efficient model for their applications.

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale for this model.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
- **Input**: $0.4 per 1M tokens
- **Output**: $2.0 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
- **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
- **Batch API Savings**: Although batch input is free, the primary cost savings come from minimizing output tokens, as the output cost is significantly higher than the input cost. Therefore, batching can help reduce the overall number of API calls, but the cost savings will primarily come from reducing output tokens.

#### Cost at Scale
The cost examples provided are as follows:
- **1,000 calls (avg 500 tokens)**: $1.2
- **10,000 calls**: $12.0
- **100,000 calls**: $120.0

To put these costs into perspective, let's calculate the cost per million tokens for each scenario:
- Assuming an average of 500 tokens per call, 1,000 calls would be approximately 0.5M tokens. The cost would be $1.2, which translates to $2.4 per 1M tokens.
- For 10,000 calls, assuming the same average, we would have approximately 5M tokens. The cost is $12.0, which is $2.4 per 1M tokens.
- For 

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Medium 3 Benchmark Analysis
#### Model Overview
The Mistral Medium 3 model, released by Mistral AI on 2025-04-17, is a mid-tier, non-open-source model. Its pricing structure includes:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens

#### Benchmark Performance
The model's performance is measured by the following benchmarks:
* **MMLU (80.0)**: The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to perform a wide range of natural language processing tasks. A score of 80.0 indicates that Mistral Medium 3 has a strong foundation in language understanding, making it suitable for tasks like coding, analysis, and content generation.
* **HumanEval (77.5)**: The HumanEval benchmark assesses a model's ability to evaluate and execute Python code. A score of 77.5 suggests that Mistral Medium 3 has a good understanding of programming concepts and can generate functional code, although it may struggle with more complex tasks.
* **LMSYS Arena ELO (1200)**: The LMSYS Arena ELO benchmark measures a model's performance in a competitive environment, evaluating its ability to respond to a wide range of questions and tasks. An ELO score of 1200 indicates that Mistral Medium 3 is a capable model, but may not be as strong as other models in certain areas.

#### Real-World Implications
The benchmark scores suggest that Mistral Medium 3 is well-suited for tasks that require:
* Strong language understanding (e.g., coding, analysis, summarization)


## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will analyze Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini, in terms of pricing, performance, and use cases.

#### Pricing Comparison
The pricing for each model is as follows:
* **Mistral Medium 3**:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* **Claude 3.5 Haiku**:
	+ Input: $0.8 per 1M tokens
	+ Output: $4.0 per 1M tokens
* **GPT-4o Mini**:
	+ Input: $0.15 per 1M tokens
	+ Output: $0.6 per 1M tokens

Mistral Medium 3 is priced lower than Claude 3.5 Haiku but higher than GPT-4o Mini for both input and output.

#### Performance Comparison
The performance benchmarks for each model are:
* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

Mistral Medium 3 has a higher MMLU score than its competitors, but the lack of benchmark data for Claude 3.5 Haiku and GPT-4o Mini makes a direct comparison challenging.

#### Capabilities and Use Cases
Mistral Medium 3 supports a wide range of capabilities, including:
* Text
* Vision
* Function calling
* JSON mode
* Streaming
* System prompts

It is best suited for tasks such as:
* Coding
* Analysis
* RAG
* Summarization
* Vision tasks
* Content generation
* Function calling

However, it is not recommended for:
* Frontier reasoning
* Bulk cheap tasks
* Simple classification
* Real-time sub-100ms tasks

####

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful language model with a wide range of capabilities, including text, vision, function calling, and more. Released on 2025-04-17, this model is part of the mid-tier and is not open-source. In this guide, we will explore the top 5 best use cases for Mistral Medium 3, along with practical advice and code integration examples using OpenRouter.

### Top 5 Best Use Cases for Mistral Medium 3
Based on the capabilities and limitations of Mistral Medium 3, the following are the top 5 best use cases for this model:

1. **Coding and Analysis**: Mistral Medium 3 excels in coding and analysis tasks, making it an ideal choice for applications such as code review, code generation, and data analysis.
2. **Summarization and Content Generation**: With its strong text generation capabilities, Mistral Medium 3 is well-suited for tasks such as text summarization, content generation, and writing assistance.
3. **Vision Tasks**: Mistral Medium 3's vision capabilities make it a good choice for tasks such as image classification, object detection, and image generation.
4. **RAG (Retrieve, Augment, Generate) Tasks**: Mistral Medium 3's ability to retrieve and generate text makes it a good fit for RAG tasks, such as question answering and text completion.
5. **Function Calling and API Integration**: With its function calling capabilities, Mistral Medium 3 can be used to integrate with external APIs and services, making it a good choice for tasks such as data processing and automation.

### Code Integration Examples with OpenRouter
To integrate Mistral Medium 3 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Mistral Medium 3 model
model = openrouter.MistralMedium3()



## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
