# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-01
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a robust set of capabilities for developers. With its architecture designed to handle a wide range of tasks, Mistral Medium 3 excels in areas such as coding, analysis, and content generation. Its capabilities include text and vision processing, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for various applications.

### Technical Strengths and Use Cases
The model's main strengths lie in its ability to handle complex tasks with a context window of 131,072 tokens and a maximum output of 16,384 tokens. Its performance is backed by benchmark scores, including an MMLU score of 80.0, a HumanEval score of 77.5, and an LMSYS Arena ELO score of 1200. Mistral Medium 3 is best suited for tasks such as coding, analysis, summarization, and vision tasks, where its capabilities can be fully utilized. However, it is not recommended for frontier reasoning, bulk cheap tasks, simple classification, or real-time applications requiring sub-100ms response times.

### Pricing and Cost Considerations
Mistral Medium 3 is priced at $0.4 per 1M input tokens and $2.0 per 1M output tokens, with no additional costs for cached or batch input. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 10,000 calls would cost $12.0, and 100,000 calls would cost $120.0. Compared to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers a competitive pricing model, making it an attractive option for developers who require a robust and versatile model for their applications. With

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a specific cost structure. This analysis will delve into the details of its pricing, including the cost structure, the use of cached tokens, batch API savings, and the cost at scale.

#### Cost Structure
The cost structure for Mistral Medium 3 is as follows:
- **Input**: $0.4 per 1M tokens
- **Output**: $2.0 per 1M tokens
- **Cached Input**: $0 per 1M tokens (free)
- **Batch Input**: $0 per 1M tokens (free)

This indicates that using cached input or batch input does not incur additional costs beyond the initial input and output costs.

#### Using Cached Tokens
Given that cached input tokens are free, it is highly beneficial to utilize cached tokens whenever possible. This can significantly reduce costs, especially for applications where the same input data is processed multiple times. However, the feasibility of using cached tokens depends on the specific use case and the nature of the input data.

#### Batch API Savings
While the pricing for batch input is listed as $0 per 1M tokens, the actual cost savings from using batch API calls come from reducing the overhead of individual API requests. The cost examples provided do not directly reflect the savings from batch processing but indicate a linear scaling of costs with the number of API calls. To achieve batch API savings, it's essential to understand that the primary savings come from reduced overhead rather than a discounted rate per token.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale can be broken down as follows:
- **1,000 calls (avg 500 tokens)**: $1.2
- **10,000 calls**: $12.0
- **100,000 calls**: $120.0

These costs reflect a linear increase with the number

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Medium 3 Benchmark Performance Analysis
#### Overview
Mistral Medium 3, a mid-tier model provided by Mistral AI, offers a balance of performance and cost. Released on 2025-04-17, this model is not open source.

#### Pricing
The pricing for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Context and Limits
The model has the following context and limits:
* Context Window: 131,072 tokens
* Max Output: 16,384 tokens
* Knowledge Cutoff: 2024-11

#### Benchmarks
The benchmark performance of Mistral Medium 3 is:
* MMLU: 80.0
* HumanEval: 77.5
* LMSYS Arena ELO: 1200
* GSM8K: None

These benchmarks indicate the model's performance in various areas:
* **MMLU (Massive Multitask Language Understanding)**: A score of 80.0 suggests that Mistral Medium 3 has a strong understanding of language across multiple tasks.
* **HumanEval**: A score of 77.5 indicates that the model is capable of generating code that is correct and functional, but may not always be optimal or efficient.
* **LMSYS Arena ELO**: An ELO score of 1200 suggests that the model has a moderate level of competence in a competitive environment, but may struggle against more advanced models.

#### Real-World Implications

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. Its pricing is as follows:
- Input: $0.4 per 1M tokens
- Output: $2.0 per 1M tokens

#### Competitor Analysis
Mistral Medium 3's top competitors are Claude 3.5 Haiku and GPT-4o Mini. Here's a comparison of their pricing and capabilities:

##### Claude 3.5 Haiku
- Provider: Unknown
- Pricing:
  - Input: $0.8 per 1M tokens (100% increase from Mistral Medium 3)
  - Output: $4.0 per 1M tokens (100% increase from Mistral Medium 3)
- Claude 3.5 Haiku is more expensive than Mistral Medium 3, with a higher cost per input and output token.

##### GPT-4o Mini
- Provider: Unknown
- Pricing:
  - Input: $0.15 per 1M tokens (62.5% decrease from Mistral Medium 3)
  - Output: $0.6 per 1M tokens (70% decrease from Mistral Medium 3)
- GPT-4o Mini is significantly cheaper than Mistral Medium 3, with a lower cost per input and output token.

#### Performance Trade-Offs
While pricing is an essential factor, performance trade-offs should also be considered:
- **Mistral Medium 3**: Offers a balance between price and performance, with a context window of 131,072 tokens and a maximum output of 16,384 tokens.
- **Claude 3.5 Haiku**: May offer better performance or capabilities to justify its higher price, but specific details are not provided.
- **GPT-4o Mini**: Its lower price may come with performance trade-offs, such as a smaller context window or reduced capabilities.

#### Choosing the Right Model
Based on the data, here are some guidelines for choosing between Mistral Medium 3 and its top competitors:
- **Choose Mistral Medium 3** for:
  - Coding, analysis, RAG, summarization, vision tasks, content generation, and function calling

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful language model released on 2025-04-17. With its mid-tier pricing and extensive capabilities, it's an attractive option for various applications. This guide will explore the top 5 best use cases for Mistral Medium 3, along with code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Medium 3
Based on its capabilities and benchmarks, the top 5 use cases for Mistral Medium 3 are:

1. **Coding and Analysis**: With its high scores in HumanEval (77.5) and MMLU (80.0), Mistral Medium 3 is well-suited for coding tasks, such as code completion, code review, and analysis.
2. **Summarization and Content Generation**: Its capabilities in text and vision tasks make it an excellent choice for summarizing long documents, generating content, and creating text-based outputs.
3. **RAG (Retrieve, Augment, Generate) Tasks**: Mistral Medium 3's ability to handle function calling and json mode makes it a good fit for RAG tasks, which involve retrieving information, augmenting it, and generating new content.
4. **Vision Tasks**: With its support for vision tasks, Mistral Medium 3 can be used for image classification, object detection, and other computer vision applications.
5. **Function Calling and API Integration**: Its ability to handle function calling and json mode makes it an excellent choice for integrating with external APIs and services.

### Code Integration Examples with OpenRouter
To integrate Mistral Medium 3 with OpenRouter, you can use the following code examples:
```python
import openrouter

# Initialize the Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Example 1: Coding and Analysis
def code_analysis(code):
    output = model.generate(text=code,

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
