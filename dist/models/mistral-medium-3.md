# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-10
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Technical Overview of Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that operates on a closed-source architecture. Its primary strengths lie in its versatility and performance across a range of tasks, including coding, analysis, and vision tasks. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, Mistral Medium 3 is well-suited for complex tasks that require significant input and output processing.

### Architecture and Capabilities
The architecture of Mistral Medium 3 supports a wide range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. This makes it an ideal choice for developers who need to perform tasks such as coding, summarization, and content generation. The model's performance is backed by strong benchmark scores, including an MMLU score of 80.0, a HumanEval score of 77.5, and an LMSYS Arena ELO score of 1200. However, it is not recommended for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms.

### Pricing and Cost Examples
The pricing for Mistral Medium 3 is as follows: $0.4 per 1M input tokens and $2.0 per 1M output tokens. There are no additional costs for cached input or batch input. To give developers a better idea of the costs involved, some examples are provided: 1,000 calls with an average of 500 tokens would cost $1.2, while 10,000 calls would cost $12.0, and 100,000 calls would cost $120.0. Compared to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers a competitive pricing model, making it a viable option for

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

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for repeated input sequences. If your application involves frequent reuse of the same input tokens, utilizing cached tokens can significantly reduce costs.

#### Batch API Savings
Similar to cached input, batch input is also free. This means that batching API calls can help minimize costs associated with input tokens. However, the actual cost savings will depend on the specific use case and the average token length of the input.

#### Cost at Scale
To understand the cost-effectiveness of Mistral Medium 3 at different scales, let's examine the provided cost examples:
- **1,000 calls (avg 500 tokens)**: $1.2
- **10,000 calls**: $12.0
- **100,000 calls**: $120.0

These examples suggest a linear cost scaling with the number of API calls. To estimate costs for other scenarios, we can use the input and output pricing as a basis. Assuming an average output size significantly smaller than the input (given the context window and max output limits), the input cost will dominate the total cost.

#### Competitor Comparison
Comparing Mistral Medium 3 with its top competitors:
- **Claude 3.5 Haiku**:
  -

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
The Mistral Medium 3 model, provided by Mistral AI, is a mid-tier language model released on April 17, 2025. It is not open source.

#### Pricing
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Context and Limits
The model has the following context and limits:
* Context Window: **131,072 tokens**
* Max Output: **16,384 tokens**
* Knowledge Cutoff: **2024-11**

#### Benchmarks
The model's benchmark performance is as follows:
* **MMLU: 80.0**: The MMLU (Massive Multitask Language Understanding) benchmark measures a model's ability to understand and generate human-like text. A higher MMLU score indicates better performance. With a score of 80.0, Mistral Medium 3 demonstrates strong language understanding capabilities.
* **HumanEval: 77.5**: The HumanEval benchmark evaluates a model's ability to write correct and functional code. A higher HumanEval score indicates better coding capabilities. With a score of 77.5, Mistral Medium 3 shows strong coding abilities.
* **LMSYS Arena ELO: 1200**: The LMSYS Arena ELO benchmark measures a model's overall performance in a competitive environment. A higher ELO score indicates better performance. With a score of 1200, Mist

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a unique set of capabilities and pricing. This comparison will delve into the price differences, performance trade-offs, and use cases for Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

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

Mistral Medium 3 offers a balance between input and output costs, while Claude 3.5 Haiku is more expensive on both fronts. GPT-4o Mini, on the other hand, is significantly cheaper for input but also has lower output costs.

#### Performance Trade-offs
The performance of each model can be evaluated using various benchmarks:
* **Mistral Medium 3**: MMLU (80.0), HumanEval (77.5), LMSYS Arena ELO (1200)
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

While the exact performance of Claude 3.5 Haiku and GPT-4o Mini is not available, Mistral Medium 3 demonstrates strong capabilities in coding, analysis, and vision tasks.

#### Capabilities and Use Cases
Mistral Medium 3 is best suited for:
* Coding
* Analysis
* RAG (Retrieval-Augmented Generation)
* Summarization
* Vision tasks
* Content generation
* Function calling

It is not recommended for:
* Frontier reasoning
* Bulk cheap tasks
* Simple classification
* Real-time sub-100ms tasks

#### Cost Examples
To illustrate the cost implications, consider the following examples:
* 1,000 calls (avg 500 tokens): $1.

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful language model suitable for a variety of applications. Released on 2025-04-17, it offers a balance between capability and cost, making it an attractive option for mid-tier projects. This guide will outline the top 5 best use cases for Mistral Medium 3, along with practical advice on integration, including examples with OpenRouter.

### Top 5 Use Cases for Mistral Medium 3

1. **Coding and Analysis**: With its strong performance in coding tasks, Mistral Medium 3 can be used for code review, code generation, and analysis. Its ability to understand and generate code makes it an excellent tool for developer assistance.
2. **Summarization and Content Generation**: The model's capabilities in text processing make it well-suited for summarizing long documents, generating content, and even assisting in creative writing tasks.
3. **Vision Tasks**: Mistral Medium 3 supports vision capabilities, allowing it to process and generate text based on visual inputs. This can be useful for applications like image description generation.
4. **RAG (Retrieval-Augmented Generation)**: The model can be used to retrieve information from a knowledge base and then generate text based on that information, making it useful for tasks that require both retrieval and generation capabilities.
5. **Function Calling**: With its function calling capability, Mistral Medium 3 can be integrated with external systems and APIs, enabling more complex and dynamic interactions.

### Integration Example with OpenRouter

To integrate Mistral Medium 3 with OpenRouter for a coding task, you might use the following approach:

```python
import openrouter

# Initialize OpenRouter with Mistral Medium 3
model = openrouter.Model(
    name="mistralai/mistral-medium-3",
    provider="Mistral AI",
    input_pricing=0.4,  # $

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
