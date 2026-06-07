# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-07
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open-source. From a technical standpoint, Mistral Small 4 is designed with a context window of 262,144 tokens and a maximum output of 4,096 tokens. Its knowledge cutoff is 2023-12, indicating that its training data is current up to December 2023. The model's architecture supports various capabilities, including text, function calling, JSON mode, streaming, and structured outputs.

### Strengths and Use Cases
Mistral Small 4 demonstrates its strengths through its benchmark scores, including an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. Although it lacks scores for HumanEval and GSM8K, its capabilities and best-use cases suggest it is well-suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization. The model's pricing structure, with input costing $0.15 per 1M tokens and output costing $0.6 per 1M tokens, positions it for cost-effective use in these areas. Developers can leverage Mistral Small 4 for a wide range of tasks, from generating human-like text to assisting in coding projects, all while considering its cost implications, such as $0.375 for 1,000 calls averaging 500 tokens.

### Pricing and Competitors
The pricing model for Mistral Small 4 is straightforward, with costs calculated based on input and output tokens. For example, 10,000 calls would cost $3.75, and 100,000 calls would cost $37.5. Notably, there are no direct competitors listed for Mistral Small 4, suggesting it occupies a unique position in the market. This lack of direct competition, combined with its capabilities and pricing

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
Mistral: Mistral Small 4, provided by Mistralai, is a standard, non-open-source model released on January 1, 2024. This analysis will delve into the cost structure, optimal usage scenarios, and scalability of this model.

#### Cost Structure
The pricing for Mistral: Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: No additional cost per 1M tokens
- **Batch Input**: No additional cost per 1M tokens

#### Optimal Usage Scenarios
- **Cached Tokens**: Since there is no additional cost for cached input tokens, it is highly beneficial to use cached tokens whenever possible. This can significantly reduce costs, especially in applications where the same input data is processed multiple times.
- **Batch API Savings**: Although there is no direct cost savings mentioned for batch input, processing inputs in batches can still lead to efficiency gains and potentially reduce the overall cost by minimizing the number of API calls.

#### Cost at Scale
The costs for Mistral: Mistral Small 4 at different scales are as follows:
- **1,000 API Calls (avg 500 tokens)**: $0.375
- **10,000 API Calls**: $3.75
- **100,000 API Calls**: $37.5

These costs indicate a linear scaling with the number of API calls, suggesting that the cost per call remains constant regardless of the volume.

#### Conclusion
Mistral: Mistral Small 4 offers a straightforward pricing model with potential for cost savings through the use of cached input tokens and efficient batch processing. Its capabilities in text, function calling, JSON mode, streaming, and structured outputs make it suitable for a variety of applications, including chat, text generation, coding,

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Benchmark Analysis
#### Model Overview
The Mistral Small 4 model, provided by Mistralai, is a standard, non-open-source model released on January 1, 2024. 

#### Pricing Structure
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

#### Benchmark Performance
The benchmark performance of Mistral Small 4 is as follows:
* MMLU: **80.0**
* HumanEval: **None**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

The MMLU score of 80.0 indicates the model's ability to understand and process mathematical and logical concepts. A higher MMLU score generally corresponds to better performance in tasks that require mathematical and logical reasoning.

The LMSYS Arena ELO score of 1200 is a measure of the model's overall language understanding and generation capabilities. ELO scores are typically used to rank models in a competitive setting, with higher scores indicating better performance.

The lack of HumanEval and GSM8K scores means that the model's performance on these specific benchmarks is not available.

#### Real-World Implications
In real-world use, the Mistral Small 4 model's

## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral Small 4 model, we will provide a general comparison framework that can be applied to other models in the market. This framework will consider price differences, performance trade-offs, and use cases where one model might be preferred over another.

#### Pricing Comparison
The Mistral Small 4 model is priced as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens

To compare, we would need the pricing information of competing models. However, we can establish a baseline for comparison:
- **Input Cost**: $0.15 per 1M tokens for Mistral Small 4. Competitors with lower input costs might be more attractive for applications with large input sizes.
- **Output Cost**: $0.6 per 1M tokens for Mistral Small 4. Models with lower output costs could be more suitable for applications requiring extensive output generation.

#### Performance Trade-offs
The performance of the Mistral Small 4 is benchmarked as follows:
- MMLU: 80.0
- LMSYS Arena ELO: 1200

When comparing with competitors, consider the following:
- **MMLU Score**: A higher MMLU score indicates better performance. If a competitor has a significantly higher MMLU score, it might be preferred for applications requiring advanced language understanding.
- **LMSYS Arena ELO**: A higher ELO score suggests better performance in competitive benchmarks. Competitors with higher ELO scores might be more suitable for applications where competitive performance is crucial.

#### Context and Limits
The Mistral Small 4 has the following context and limits:
- **Context Window**: 262,144 tokens
- **Max Output**: 4,096 tokens
- **Knowledge Cutoff**: 2023-12

Competitors with larger context windows or higher max output limits might be preferred for applications requiring more extensive input processing or output generation. Similarly, models with more recent knowledge cutoffs could be more suitable for applications needing the most up-to-date information.

#### Capabilities and Use Cases
The Mistral Small 4 supports the following capabilities:
- text
- function_calling
- json_mode
- streaming
- structured_outputs

It is best suited for:
- chat
- text_generation
- coding
- analysis
- rag_p

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and closed-source model, it offers a unique set of features that can be integrated into various applications.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and ability to generate up to 4,096 tokens, Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: Mistral Small 4's function calling and structured outputs capabilities make it an excellent choice for coding and analysis tasks, such as code completion and code review.
3. **Summarization and RAG Pipelines**: Its ability to generate structured outputs and perform text generation tasks makes it a good fit for summarization and RAG (Retrieve, Augment, Generate) pipelines.
4. **Content Creation**: With its text generation capabilities, Mistral Small 4 can be used for content creation tasks, such as generating articles, blog posts, and social media content.
5. **Conversational AI**: Its chat and text generation capabilities, combined with its ability to perform function calling, make it a good choice for conversational AI applications, such as virtual assistants and chatbots.

### Code Integration Examples with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code examples:

```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.MistralSmall4()

# Generate text based on a prompt
prompt = "Write a short story about a character who discovers a hidden world."
response = model.generate_text(prompt

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
