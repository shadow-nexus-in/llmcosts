# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-18
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance between performance and cost. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, this model is well-suited for a variety of tasks, including coding, analysis, and content generation. The model's architecture is designed to support multiple capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts.

### Technical Specifications and Pricing
From a technical standpoint, Mistral Medium 3 has a knowledge cutoff of 2024-11 and has achieved notable benchmarks, including an MMLU score of 80.0 and a HumanEval score of 77.5. The model's pricing is as follows: $0.4 per 1M input tokens and $2.0 per 1M output tokens. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 10,000 calls would cost $12.0, and 100,000 calls would cost $120.0. Compared to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers competitive pricing for its input and output tokens.

### Use Cases and Limitations
Mistral Medium 3 is best suited for tasks that require a balance between performance and cost, such as coding, analysis, and content generation. However, it may not be the best choice for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms. With its robust capabilities and competitive pricing, Mistral Medium 3 is a viable option for developers looking for a mid-tier model that can handle a variety of tasks. Its limitations, including a context window of 131,072 tokens and

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.4 |
| Output | $2.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Mistral Medium 3 Pricing Analysis
#### Overview
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option when possible. However, the context window is limited to 131,072 tokens, and the knowledge cutoff is 2024-11. Therefore, cached tokens should be used for:
* Frequently asked questions or common queries within the knowledge cutoff.
* Applications where the input data is largely static or repetitive.

#### Batch API Savings
Batch input is also free, which can lead to significant cost savings when making multiple API calls. To maximize batch API savings:
* Group multiple requests together to reduce the number of API calls.
* Use batch input for applications with a high volume of requests, such as data processing or content generation.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* 1,000 calls (avg 500 tokens): $1.2
* 10,000 calls: $12.0
* 100,000 calls: $120.0

These costs demonstrate a linear scaling of costs with the number of API calls.

#### Comparison to Top Competitors
Mistral Medium 3's pricing is competitive with other mid-tier models:
* Claude 3.5 Haiku: $0.8/1M input, $4.0/1

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Mistral Medium 3 Benchmark Performance
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
* **MMLU (Massive Multitask Language Understanding)**: A score of 80.0 indicates that Mistral Medium 3 has a strong understanding of language, with the ability to perform well on a wide range of tasks.
* **HumanEval**: A score of 77.5 suggests that the model is capable of generating human-like code, with a high degree of accuracy and coherence.
* **LMSYS Arena ELO**: An ELO score of 1200 indicates that the model has a moderate level of competence in competitive coding tasks, with the ability to solve problems

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will examine the pricing, performance, and capabilities of Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

#### Pricing Comparison
The pricing for each model is as follows:
* Mistral Medium 3:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* Claude 3.5 Haiku:
	+ Input: $0.8 per 1M tokens (100% more than Mistral Medium 3)
	+ Output: $4.0 per 1M tokens (100% more than Mistral Medium 3)
* GPT-4o Mini:
	+ Input: $0.15 per 1M tokens (62.5% less than Mistral Medium 3)
	+ Output: $0.6 per 1M tokens (70% less than Mistral Medium 3)

#### Performance Comparison
The performance of each model can be evaluated using various benchmarks:
* Mistral Medium 3:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* Claude 3.5 Haiku: Not provided
* GPT-4o Mini: Not provided

#### Capabilities and Use Cases
Mistral Medium 3 is capable of:
* Text, vision, function calling, JSON mode, streaming, and system prompts
* Best for: coding, analysis, RAG, summarization, vision tasks, content generation, and function calling
* Not good for: frontier reasoning, bulk cheap tasks, simple classification, and real-time sub 100ms tasks

#### Cost Examples
The cost of using Mistral Medium 3 for various scenarios is as follows:
* 1,000 calls (avg 500 tokens): $1.2
* 10,000 calls: $12.0
* 100,000 calls: $120.0

#### Choosing the Right Model
Based on the pricing and performance comparison,

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful language model released on 2025-04-17. With its mid-tier pricing and extensive capabilities, it's an attractive option for various applications. Here, we'll explore the top 5 best use cases for Mistral Medium 3, along with code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Medium 3
1. **Coding and Analysis**: Mistral Medium 3 excels in coding tasks, making it ideal for code completion, debugging, and analysis. Its high MMLU score of 80.0 and HumanEval score of 77.5 demonstrate its proficiency in these areas.
2. **Summarization and Content Generation**: With its strong text capabilities, Mistral Medium 3 is well-suited for summarization and content generation tasks. Its context window of 131,072 tokens allows for processing large amounts of text.
3. **Vision Tasks**: Mistral Medium 3's vision capabilities make it a great choice for image-related tasks, such as image classification, object detection, and image generation.
4. **RAG (Retrieval-Augmented Generation) Tasks**: Mistral Medium 3's ability to perform RAG tasks makes it suitable for applications that require retrieving and generating text based on external knowledge sources.
5. **Function Calling and API Integration**: Mistral Medium 3's function calling capability allows for seamless integration with external APIs and services, making it a great choice for applications that require interacting with external systems.

### Code Integration Example with OpenRouter
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Define a function to generate code
def generate_code(prompt):
    # Use Mistral Medium 3 to generate code
    response = model.generate_text(prompt, max_tokens=1024)
    return

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
