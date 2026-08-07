# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-07
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium large language model released on 2024-07-24. This model is not open source. The architecture of Mistral Large 2 is designed to handle a wide range of tasks, including coding, analysis, and function calling, with a context window of 131,072 tokens and a maximum output of 4,096 tokens. Its knowledge cutoff is 2024-07, ensuring it has access to a vast amount of information up to that point.

### Strengths and Use Cases
Mistral Large 2 demonstrates its strengths through various benchmarks: achieving 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These scores indicate its capabilities in understanding and generating human-like text, coding, and problem-solving. The model is best utilized for tasks such as coding, analysis, and function calling, and it supports multilingual inputs. However, it is not recommended for tasks requiring embeddings, bulk cheap processing, real-time responses under 100ms, or vision-heavy applications. Its pricing model charges $3.0 per 1M input tokens and $9.0 per 1M output tokens.

### Pricing and Competitors
The pricing for Mistral Large 2 is structured around input and output tokens, with no charges for cached or batch inputs. For example, 1,000 calls averaging 500 tokens each would cost $6.0, scaling up to $60.0 for 10,000 calls and $600.0 for 100,000 calls. In comparison to its top competitors, such as GPT-4o which charges $2.5/1M input and $10.0/1M output, Mistral Large 2 offers a competitive pricing model. Developers should consider these costs

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
Mistral Large 2, provided by Mistral AI, is a premium model released on 2024-07-24. This analysis will delve into the cost structure, usage scenarios, and scaling costs for this model.

#### Cost Structure
The pricing for Mistral Large 2 is as follows:
- **Input**: $3.0 per 1M tokens
- **Output**: $9.0 per 1M tokens
- **Cached Input**: $0 per 1M tokens (free)
- **Batch Input**: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for repeated input sequences. If your application involves frequent reuse of the same input, utilizing cached tokens can significantly reduce costs.

#### Batch API Savings
Batching API calls can lead to substantial savings. Since batch input is free, grouping multiple requests together can minimize the cost associated with input tokens. However, the output cost remains the same, so this strategy is most effective when the output size is relatively small compared to the input.

#### Cost at Scale
To understand the cost implications of using Mistral Large 2 at scale, let's examine the provided cost examples:
- **1,000 calls (avg 500 tokens)**: $6.0
- **10,000 calls**: $60.0
- **100,000 calls**: $600.0

These examples illustrate a linear scaling of costs with the number of API calls, indicating that the cost per call remains constant regardless of the volume.

#### Comparison with Top Competitors
Mistral Large 2's pricing can be compared to its top competitor, GPT-4o:
- **GPT-4o**: $2.5/1M input, $10.0/1M output

While GPT-4o offers a lower input cost, Mist

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 84.0 |
| HumanEval | 92.0 |
| LMSYS Arena ELO | 1225 |
| ARC | 93.0 |

## Benchmark Analysis
### Mistral Large 2 Benchmark Analysis
#### Model Overview
The Mistral Large 2 model, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts.

#### Pricing
The pricing for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Context and Limits
The model has a context window of 131,072 tokens, a maximum output of 4,096 tokens, and a knowledge cutoff of 2024-07.

#### Benchmarks
The model's benchmark performance is as follows:
* MMLU: 84.0
* HumanEval: 92.0
* LMSYS Arena ELO: 1225
* GSM8K: 93.0

These benchmarks indicate the model's performance in various areas:
* **MMLU (Massive Multitask Language Understanding)**: A score of 84.0 indicates the model's ability to understand and generate human-like text across a wide range of tasks and domains.
* **HumanEval**: A score of 92.0 suggests that the model is highly effective in evaluating and generating code that is similar to human-written code.
* **LMSYS Arena ELO**: A score of 1225 indicates the model's competitive performance in a large-scale language model benchmark, with higher scores indicating better performance.
* **

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. This comparison will focus on its pricing, performance, and capabilities in relation to its top competitors, specifically GPT-4o.

#### Pricing Comparison
| Model | Input Price per 1M tokens | Output Price per 1M tokens |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens. In contrast, GPT-4o is priced at $2.5 per 1M input tokens but $10.0 per 1M output tokens. This indicates that while GPT-4o is cheaper for input, it is more expensive for output compared to Mistral Large 2.

#### Performance Trade-offs
Mistral Large 2 has the following benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

These scores are not directly comparable to GPT-4o without its benchmark data. However, Mistral Large 2's high scores in HumanEval and GSM8K suggest strong performance in coding and mathematical reasoning tasks.

#### Capabilities and Best Use Cases
Mistral Large 2 supports a wide range of capabilities, including:
- Text
- Vision
- Function calling
- JSON mode
- Streaming
- System prompts

It is best suited for tasks such as:
- Coding
- Analysis
- RAG (Retrieval-Augmented Generation)
- Agents
- Multilingual tasks
- Function calling

However, it is not recommended for:
- Embeddings
- Bulk cheap processing
- Real-time sub-100ms applications
- Vision-heavy tasks

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100,000 calls: $

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model that excels in various tasks, including coding, analysis, and function calling. With its impressive benchmarks, such as an MMLU score of 84.0 and a HumanEval score of 92.0, it's a powerful tool for developers and analysts.

### Top 5 Best Use Cases for Mistral Large 2
Based on its capabilities and limitations, here are the top 5 best use cases for Mistral Large 2:

1. **Coding Assistance**: With its high HumanEval score, Mistral Large 2 is well-suited for coding tasks, such as code completion, code review, and code generation. For example, you can use it to generate code snippets in various programming languages, including Python, Java, and C++.
2. **Data Analysis**: Mistral Large 2's analysis capabilities make it an excellent choice for data analysis tasks, such as data visualization, data mining, and data interpretation. You can use it to analyze large datasets, identify patterns, and generate insights.
3. **RAG (Retrieval-Augmented Generation)**: Mistral Large 2's support for RAG makes it an excellent choice for tasks that require retrieving and generating text based on external knowledge. For example, you can use it to generate text summaries of long documents or to answer questions based on a large corpus of text.
4. **Multilingual Support**: With its multilingual capabilities, Mistral Large 2 can be used for tasks that require language translation, language understanding, and language generation. For example, you can use it to translate text from one language to another or to generate text in multiple languages.
5. **Function Calling**: Mistral Large 2's support for function calling makes it an excellent choice for tasks that require executing external functions or APIs

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
