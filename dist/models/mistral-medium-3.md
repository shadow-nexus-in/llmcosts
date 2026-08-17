# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-17
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, developed by Mistral AI and released on 2025-04-17, is a mid-tier language model that offers a robust set of capabilities for various applications. Its architecture, although not open-source, is designed to handle a wide range of tasks, including text and vision processing, function calling, and more. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, Mistral Medium 3 is well-suited for tasks that require understanding and generating lengthy, complex content.

### Technical Strengths and Use-Cases
The model's strengths are reflected in its benchmark scores: 80.0 on MMLU, 77.5 on HumanEval, and an ELO rating of 1200 in the LMSYS Arena. These metrics indicate that Mistral Medium 3 excels in coding, analysis, and tasks that involve reasoning and understanding. Its capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, make it an ideal choice for applications such as summarization, content generation, and vision tasks. However, it may not be the best fit for tasks that require frontier reasoning, bulk cheap processing, simple classification, or real-time responses under 100ms.

### Pricing and Cost Considerations
Mistral Medium 3 is priced at $0.4 per 1M input tokens and $2.0 per 1M output tokens, with no additional costs for cached or batch input. This pricing structure makes it competitive with other models in its tier, such as Claude 3.5 Haiku and GPT-4o Mini. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 10,000 calls would cost $12.0, and 100,000 calls would cost $120.0. When evaluating the cost-effect

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This model is not open source. The pricing structure is based on input and output tokens.

#### Cost Structure
The cost structure for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $None per 1M tokens (free)
* Batch Input: $None per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for reducing costs. However, the use of cached tokens is not explicitly defined in the provided data. It is assumed that cached tokens can be used when the input is repeated or similar, allowing for cost savings.

#### Batch API Savings
Batch input is also free, which can lead to significant cost savings when making multiple API calls with the same input. This can be particularly useful for applications where the same input is used multiple times, such as in data processing or analysis tasks.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* 1,000 calls (avg 500 tokens): $1.2
* 10,000 calls: $12.0
* 100,000 calls: $120.0

These costs demonstrate a linear scaling of costs with the number of API calls.

#### Comparison to Competitors
Mistral Medium 3's pricing can be compared to its top competitors:
* Claude 3.5 Haiku: $0.8/1M input, $4.0/1M output
* GPT-4o Mini: $0.15/1M input, $0.6/1M output

Mistral Medium

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Medium 3 Benchmark Performance Analysis
#### Model Overview
The Mistral Medium 3 model, provided by Mistral AI, was released on 2025-04-17. It is a mid-tier model, not open source, with a context window of 131,072 tokens and a maximum output of 16,384 tokens.

#### Pricing
The pricing for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Benchmark Performance
The model's benchmark performance is measured by the following scores:
* **MMLU (Massive Multitask Language Understanding)**: 80.0, indicating the model's ability to understand and perform a wide range of natural language tasks.
* **HumanEval**: 77.5, measuring the model's ability to evaluate and execute human-written code.
* **LMSYS Arena ELO**: 1200, representing the model's competitive performance in a large-scale language model benchmark.

#### Real-World Implications
These benchmark scores have significant implications for real-world use:
* The high MMLU score suggests that Mistral Medium 3 is capable of handling complex language tasks, making it suitable for applications such as coding, analysis, and content generation.
* The HumanEval score indicates that the model can effectively evaluate and execute human-written code, which is useful for tasks like function calling and code summarization.
* The LMSYS Arena ELO score demonstrates the model's competitive performance, implying that it can hold its own against other

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a unique set of capabilities and pricing. This comparison will delve into the details of Mistral Medium 3 versus its top competitors, Claude 3.5 Haiku and GPT-4o Mini, highlighting price differences, performance trade-offs, and scenarios where each model is best suited.

#### Pricing Comparison
The pricing structure of each model is as follows:
* **Mistral Medium 3**:
  + Input: $0.4 per 1M tokens
  + Output: $2.0 per 1M tokens
* **Claude 3.5 Haiku**:
  + Input: $0.8 per 1M tokens
  + Output: $4.0 per 1M tokens
* **GPT-4o Mini**:
  + Input: $0.15 per 1M tokens
  + Output: $0.6 per 1M tokens

Mistral Medium 3 offers a balanced pricing approach, sitting between the more expensive Claude 3.5 Haiku and the significantly cheaper GPT-4o Mini.

#### Performance and Capabilities
* **Mistral Medium 3**:
  + Context Window: 131,072 tokens
  + Max Output: 16,384 tokens
  + Benchmarks: MMLU (80.0), HumanEval (77.5), LMSYS Arena ELO (1200)
  + Capabilities: text, vision, function_calling, json_mode, streaming, system_prompts
  + Best for: coding, analysis, rag, summarization, vision_tasks, content_generation, function_calling
* **Claude 3.5 Haiku** and **GPT-4o Mini**'s specific capabilities and benchmarks are not provided for direct comparison, but their pricing suggests different value propositions.

#### Choosing the Right Model
* **Mistral Medium 3** is ideal for tasks that require a balance of performance and cost, such as coding, analysis, and content generation, where its mid-tier pricing and robust capabilities make it an attractive choice.
* **Claude 3.5 Haiku** might be preferred for applications where high-end performance is necessary, and budget is less

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful model with a wide range of capabilities including text, vision, function calling, and more. Released on 2025-04-17, it offers a balance between performance and cost, making it suitable for various applications. Here, we'll explore the top 5 best use cases for Mistral Medium 3, along with practical advice and code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Medium 3
1. **Coding and Analysis**: Given its high scores in HumanEval (77.5) and MMLU (80.0), Mistral Medium 3 is well-suited for coding tasks, code analysis, and code generation. It can be used to automate coding tasks, provide code reviews, or even assist in code debugging.
2. **Summarization and Content Generation**: With its strong text capabilities, Mistral Medium 3 can be used for summarizing long documents, generating content, or even creating chatbot responses. Its ability to understand and generate human-like text makes it a great tool for content creation tasks.
3. **Vision Tasks**: Mistral Medium 3 supports vision capabilities, making it useful for tasks such as image classification, object detection, and image generation. It can be integrated with OpenRouter for tasks that require both text and vision capabilities.
4. **RAG (Retrieval-Augmented Generation)**: Mistral Medium 3's support for RAG tasks makes it suitable for applications that require generating text based on external knowledge. This can be particularly useful in question-answering systems or chatbots that need to provide accurate and up-to-date information.
5. **Function Calling and JSON Mode**: With its ability to call functions and parse JSON, Mistral Medium 3 can be used to automate tasks that involve interacting with external APIs or processing JSON data. This makes it a great

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
