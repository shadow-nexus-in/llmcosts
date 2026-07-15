# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-15
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open-source. From an architectural standpoint, Mistral Small 4 is designed to handle a wide range of natural language processing tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens, making it suitable for complex tasks such as chat, text generation, coding, analysis, and summarization.

### Technical Specifications and Pricing
Technically, Mistral Small 4 has a context window of 262,144 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2023-12. The model's pricing is based on input and output tokens, with costs of $0.15 per 1M input tokens and $0.6 per 1M output tokens. There are no additional costs for cached input or batch input. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. These specifications and pricing make Mistral Small 4 a competitive option for developers looking for a robust language model for their applications, with estimated costs such as $0.375 for 1,000 calls (avg 500 tokens), $3.75 for 10,000 calls, and $37.5 for 100,000 calls.

### Use Cases and Competitors
Mistral Small 4 is best suited for applications involving chat, text generation, coding, analysis, RAG pipelines, and summarization, thanks to its robust capabilities and large context window. However, its limitations and areas where it is not recommended are not specified. As of the current data,

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.15 |
| Output | $0.6 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Mistral Small 4
#### Overview
The Mistral Small 4 model, provided by Mistralai, is a standard, non-open-source model released on 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* **Input**: $0.15 per 1M tokens
* **Output**: $0.6 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
* **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
* **Batch API**: With batch input being free, batching API calls can significantly reduce costs, especially for large-scale applications.

#### Cost at Scale
The cost examples provided are as follows:
* **1,000 calls (avg 500 tokens)**: $0.375
* **10,000 calls**: $3.75
* **100,000 calls**: $37.5

To put these numbers into perspective, the cost per call remains constant, indicating a linear scaling of costs with the number of API calls.

#### Cost Calculation
Based on the input and output pricing, we can calculate the cost per call as follows:
* Assume an average of 500 tokens per call (input + output).
* Input cost: 500 tokens / 1,000,000 tokens * $0.15 = $0.000075 per call (input)
* Output cost: 500 tokens / 1,000,000 tokens * $0.6 = $0.0003 per call (output)
* Total cost per call: $0.000075 (input) + $0.0003 (output

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
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. It is not open-source and has a specific pricing structure based on input and output tokens.

#### Pricing Structure
The pricing for Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: $None per 1M tokens
- **Batch Input**: $None per 1M tokens

#### Context and Limits
Key context and limit details:
- **Context Window**: 262,144 tokens
- **Max Output**: 4,096 tokens
- **Knowledge Cutoff**: 2023-12

#### Benchmark Performance
The model's performance is measured by the following benchmarks:
- **MMLU**: 80.0
- **HumanEval**: None
- **LMSYS Arena ELO**: 1200
- **GSM8K**: None

The **MMLU (Massive Multitask Language Understanding)** score of 80.0 indicates the model's ability to understand and perform a wide range of natural language tasks. A higher MMLU score suggests better performance in tasks that require understanding and generating human-like text.

The **LMSYS Arena ELO** score of 1200 is a measure of the model's competitive performance in a controlled environment, with higher scores indicating better performance relative to other models.

The absence of **HumanEval** and **GSM8K** scores limits the understanding of the model's performance

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral: Mistral Small 4 model, we will provide a general comparison framework that can be applied when evaluating this model against others in the market. This framework will cover price differences, performance trade-offs, and scenarios where one might choose the Mistral: Mistral Small 4 over its potential competitors.

#### Pricing Comparison
The pricing for the Mistral: Mistral Small 4 is as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens

To compare, one would need to look at the pricing structures of other models. Generally, prices can vary widely based on the provider, model capabilities, and intended use case. For instance, some models might charge based on the number of requests, computational resources used, or even offer flat rates for certain tiers of service.

#### Performance Trade-offs
The Mistral: Mistral Small 4 has the following benchmarks and capabilities:
- MMLU: 80.0
- LMSYS Arena ELO: 1200
- Context Window: 262,144 tokens
- Max Output: 4,096 tokens
- Capabilities: text, function_calling, json_mode, streaming, structured_outputs

When comparing performance, consider the following:
- **MMLU Score**: A higher score generally indicates better performance on a wide range of natural language understanding tasks.
- **LMSYS Arena ELO**: This score reflects the model's performance in a competitive setting, with higher scores indicating better performance.
- **Context Window and Max Output**: These parameters are crucial for determining the model's ability to handle long-range dependencies and generate extensive responses.

#### Choosing the Right Model
The Mistral: Mistral Small 4 is best for:
- Chat
- Text generation
- Coding
- Analysis
- RAG pipelines
- Summarization

It is not specified what it is not good for, but generally, the choice of model depends on the specific requirements of the project, including but not limited to:
- **Project Budget**: Models with lower costs per token or request might be more appealing for projects with tight budgets.
- **Performance Requirements**: Projects demanding high accuracy, long context windows, or specific capabilities like function calling might prioritize models with those strengths.
- **Use Case**: Different models excel in

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and release date of 2024-01-01, it offers a robust set of features for various applications.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and max output of 4,096 tokens, Mistral Small 4 is well-suited for chat and text generation applications. Its ability to understand and respond to user input makes it an ideal choice for conversational AI.
2. **Coding and Analysis**: Mistral Small 4's function calling and structured outputs capabilities make it a great tool for coding and analysis tasks. Its ability to generate code and provide structured outputs can help with tasks such as code completion and data analysis.
3. **Summarization**: With its high MMLU benchmark score of 80.0, Mistral Small 4 is capable of generating high-quality summaries of long pieces of text. Its ability to understand and condense complex information makes it an ideal choice for summarization tasks.
4. **RAG Pipelines**: Mistral Small 4's ability to generate text and provide structured outputs makes it a great tool for RAG (Retrieval-Augmented Generation) pipelines. Its ability to retrieve and generate text can help with tasks such as question answering and text generation.
5. **Streaming**: With its streaming capability, Mistral Small 4 can be used for real-time text generation and analysis applications. Its ability to process and generate text in real-time makes it an ideal choice for applications such as live chat and real-time analytics.

### Code Integration Examples with Open

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
