# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-18
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance between performance and cost. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, this model is well-suited for a variety of tasks, including coding, analysis, and content generation. The model's capabilities include text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Strengths and Use Cases
The main strengths of Mistral Medium 3 lie in its ability to handle complex tasks such as coding, analysis, and vision tasks. Its high benchmark scores, including an MMLU score of 80.0 and a HumanEval score of 77.5, demonstrate its capabilities in these areas. Additionally, its LMSYS Arena ELO score of 1200 indicates its competitive performance in large-scale language modeling tasks. However, it is not recommended for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms.

### Pricing and Cost Considerations
Mistral Medium 3 is priced at $0.4 per 1M input tokens and $2.0 per 1M output tokens. This makes it a competitive option for developers who need to process large amounts of data. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 10,000 calls would cost $12.0, and 100,000 calls would cost $120.0. Compared to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers a unique balance of performance and cost, making it an attractive option for developers who need a reliable and efficient language model for their applications.

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
* **Input**: $0.4 per 1M tokens
* **Output**: $2.0 per 1M tokens
* **Cached Input**: $0 per 1M tokens (free)
* **Batch Input**: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for repeated input sequences. If your application involves frequent reuse of the same input, utilizing cached tokens can significantly reduce costs.

#### Batch API Savings
Batch input is also free, which means that batching API calls can help reduce the overall cost by minimizing the number of input tokens charged. This is particularly beneficial for applications that can process data in bulk.

#### Cost at Scale
The cost of using Mistral Medium 3 at different scales is as follows:
* **1,000 calls (avg 500 tokens)**: $1.2
* **10,000 calls**: $12.0
* **100,000 calls**: $120.0

These costs can be broken down into input and output costs. Assuming an average of 500 tokens per call, the total tokens for each scale would be:
* **1,000 calls**: 500,000 tokens
* **10,000 calls**: 5,000,000 tokens
* **100,000 calls**: 50,000,000 tokens

Using the pricing structure, the estimated costs can be calculated as follows:
* **Input (500,000 tokens / 1,000,000 tokens per $0.4)**: $0

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
The Mistral Medium 3 model, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. The model's knowledge cutoff is 2024-11.

#### Pricing
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Benchmark Performance
The model's benchmark performance is measured by the following scores:
* **MMLU: 80.0** - The MMLU (Massive Multitask Language Understanding) score measures the model's ability to perform a wide range of natural language processing tasks. A higher score indicates better performance.
* **HumanEval: 77.5** - The HumanEval score measures the model's ability to evaluate and execute human-written code. A higher score indicates better performance.
* **LMSYS Arena ELO: 1200** - The LMSYS Arena ELO score measures the model's performance in a competitive arena, where models are pitted against each other to complete tasks. A higher score indicates better performance.

#### Real-World Implications
The benchmark scores indicate that Mistral Medium 3 is a capable model for a wide range of tasks, including:
* Coding: The model's high HumanEval score indicates that it is well-suited for coding tasks.
* Analysis: The

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will delve into the pricing, performance, and capabilities of Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

#### Pricing Comparison
The pricing models of the three competitors are as follows:
* **Mistral Medium 3**:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* **Claude 3.5 Haiku**:
	+ Input: $0.8 per 1M tokens
	+ Output: $4.0 per 1M tokens
* **GPT-4o Mini**:
	+ Input: $0.15 per 1M tokens
	+ Output: $0.6 per 1M tokens

Mistral Medium 3 offers a balanced pricing model, with input costs 50% of Claude 3.5 Haiku and output costs 3.33 times that of GPT-4o Mini.

#### Performance Trade-offs
The performance of each model can be evaluated using the following benchmarks:
* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

While the exact performance of Claude 3.5 Haiku and GPT-4o Mini is not available, Mistral Medium 3 demonstrates strong capabilities in coding, analysis, and vision tasks.

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
*

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful model released on 2025-04-17. It is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This model excels in various tasks, including coding, analysis, and content generation.

### Top 5 Best Use Cases for Mistral Medium 3
Based on its capabilities and benchmarks, here are the top 5 best use cases for Mistral Medium 3:

1. **Coding and Development**: With its high scores in HumanEval (77.5) and MMLU (80.0), Mistral Medium 3 is well-suited for coding tasks, such as code completion, code review, and bug fixing.
2. **Text Analysis and Summarization**: The model's ability to process large context windows and generate high-quality output makes it ideal for text analysis and summarization tasks.
3. **Vision Tasks**: Mistral Medium 3 supports vision capabilities, allowing it to be used for image classification, object detection, and other computer vision tasks.
4. **Content Generation**: The model's capabilities in text generation and content creation make it suitable for tasks such as writing articles, generating product descriptions, and creating chatbot responses.
5. **Function Calling and API Integration**: With its support for function calling and JSON mode, Mistral Medium 3 can be used to integrate with external APIs and services, such as OpenRouter, to retrieve and process data.

### Code Integration Example with OpenRouter
Here is an example of how to integrate Mistral Medium 3 with OpenRouter using Python:
```python
import requests

# Set API endpoint and credentials
endpoint = "https://api.openrouter.com/v1/"
api_key = "YOUR_API_KEY"

# Define a function to call the OpenRouter API
def get_route(origin, destination):
    url

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
