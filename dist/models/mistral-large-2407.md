# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-23
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly excelling in coding, analysis, and function calling tasks. Its architecture is geared towards handling complex inputs and generating coherent, contextually relevant outputs. With a context window of 131,072 tokens and a maximum output of 4,096 tokens, Mistral Large 2 is well-suited for tasks that require understanding and processing large amounts of text.

### Technical Capabilities and Pricing
Mistral Large 2 boasts an impressive array of capabilities, including text and vision processing, function calling, JSON mode, streaming, and system prompts. Its strengths are reflected in its benchmark scores: 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. The model is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, with no charges for cached or batch inputs. For developers, this translates to $6.0 for 1,000 calls averaging 500 tokens, $60.0 for 10,000 calls, and $600.0 for 100,000 calls. Compared to its top competitor, GPT-4o, which charges $2.5/1M input and $10.0/1M output, Mistral Large 2 offers competitive pricing for its premium services.

### Use Cases and Limitations
Given its capabilities, Mistral Large 2 is best utilized for coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual tasks, and function calling. However, it is not recommended for embeddings, bulk cheap processing, real-time applications requiring sub-100ms response times, or vision

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $3.0 |
| Output | $9.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Mistral Large 2 Pricing Analysis
#### Overview
Mistral Large 2, a premium model provided by Mistral AI, offers a unique set of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. The pricing structure is based on input and output tokens, with specific considerations for cached and batch inputs.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
- **Input**: $3.0 per 1M tokens
- **Output**: $9.0 per 1M tokens
- **Cached Input**: $0 per 1M tokens (free)
- **Batch Input**: $0 per 1M tokens (free)

#### Cost Optimization Strategies
- **Cached Tokens**: Since cached input tokens are free, utilizing cached tokens whenever possible can significantly reduce costs. This is particularly beneficial for applications where the same input data is processed multiple times.
- **Batch API Savings**: Although the pricing does not explicitly mention a discount for batch inputs, the fact that batch inputs are listed as $0 per 1M tokens suggests that there might be an implicit benefit to batching, such as reduced overhead costs per call. However, based on the provided data, there's no direct cost savings from batching mentioned.

#### Cost at Scale
Given the average cost examples, we can infer the cost at different scales:
- **1,000 calls (avg 500 tokens)**: $6.0
- **10,000 calls**: $60.0
- **100,000 calls**: $600.0

To understand the cost per call, let's calculate based on the average tokens per call and the pricing structure:
- Assuming an average of 500 tokens per call, and considering both input and output costs. For simplicity, let's assume the output is significantly less than the input, so the primary cost comes from the input tokens.

####

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 84.0 |
| HumanEval | 92.0 |
| LMSYS Arena ELO | 1225 |
| ARC | 93.0 |

## Benchmark Analysis
### Mistral Large 2 Benchmark Performance Analysis
#### Model Overview
The Mistral Large 2 model, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. It offers a range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, making it suitable for applications such as coding, analysis, and multilingual tasks.

#### Pricing
The pricing for Mistral Large 2 is as follows:
- Input: $3.0 per 1M tokens
- Output: $9.0 per 1M tokens
- Cached Input: $None per 1M tokens
- Batch Input: $None per 1M tokens

#### Context and Limits
The model has a context window of 131,072 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff date of 2024-07.

#### Benchmark Performance
The model's benchmark performance is as follows:
- **MMLU (Massive Multitask Language Understanding)**: 84.0 - This score indicates the model's ability to understand and perform a wide range of natural language tasks. A higher score suggests better performance in tasks such as text classification, sentiment analysis, and question answering.
- **HumanEval**: 92.0 - This score evaluates the model's ability to generate human-like code. A higher score indicates better performance in coding tasks, such as code completion and code generation.
- **LMSYS Arena ELO**: 1225 - This score measures the model's performance in a competitive environment, where it is pitted against other models. A higher score indicates better performance and a higher ranking in the

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, a premium model offered by Mistral AI, is a powerful tool with a wide range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, it stands out for its performance in coding, analysis, and multilingual tasks. However, its pricing and performance trade-offs need to be considered against its top competitors.

#### Pricing Comparison
Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens. In comparison, GPT-4o, one of its top competitors, is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. 

| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

#### Performance Trade-offs
Mistral Large 2 boasts impressive benchmarks:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

These metrics indicate strong performance in various tasks, particularly in coding and analysis. However, the choice between Mistral Large 2 and its competitors should be based on specific use cases and requirements.

#### When to Choose Each Model
- **Mistral Large 2** is best for tasks that require advanced coding, analysis, and multilingual capabilities. Its support for function calling, JSON mode, and streaming makes it versatile for complex applications. It's not recommended for embeddings, bulk cheap operations, or real-time applications requiring sub-100ms responses.
- **GPT-4o** might be more economical for applications where input token cost is a significant factor, given its lower input price. However, its output price is higher, which could impact overall cost for applications with large output requirements.

#### Cost Examples
For Mistral Large 2, the cost can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
-

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model that excels in various tasks, including coding, analysis, and function calling. With its robust capabilities and high performance benchmarks (MMLU: 84.0, HumanEval: 92.0, LMSYS Arena ELO: 1225, GSM8K: 93.0), it is an ideal choice for applications requiring advanced language understanding and generation.

### Top 5 Best Use Cases for Mistral Large 2
Given its capabilities and limitations, here are the top 5 best use cases for Mistral Large 2:

1. **Coding Assistance**: Mistral Large 2 can be used to develop intelligent coding assistants that provide real-time suggestions, code completion, and debugging support. Its high performance on HumanEval (92.0) makes it an excellent choice for coding-related tasks.
2. **Advanced Text Analysis**: With its large context window (131,072 tokens) and high MMLU score (84.0), Mistral Large 2 is well-suited for advanced text analysis tasks, such as sentiment analysis, entity recognition, and text summarization.
3. **Multilingual Support**: As a multilingual model, Mistral Large 2 can be used to develop applications that require support for multiple languages, such as language translation, language detection, and cross-lingual information retrieval.
4. **Function Calling and API Integration**: Mistral Large 2's function calling capability allows it to integrate with external APIs and services, making it an excellent choice for applications that require interaction with external systems. For example, it can be used to integrate with OpenRouter for routing and navigation tasks.
5. **Conversational Agents**: With its high performance on LMSYS Arena ELO (1225) and GSM8K (93.0), Mist

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
