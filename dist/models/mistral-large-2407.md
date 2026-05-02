# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-02
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Technical Overview of Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly in coding, analysis, and multilingual tasks. The model boasts an impressive architecture that supports capabilities such as text, vision, function calling, JSON mode, streaming, and system prompts. With a context window of 131,072 tokens and a maximum output of 4,096 tokens, Mistral Large 2 is well-suited for complex and demanding tasks.

### Strengths and Use Cases
The primary strengths of Mistral Large 2 lie in its exceptional performance in coding, analysis, and function calling tasks, as evidenced by its high benchmark scores: MMLU (84.0), HumanEval (92.0), LMSYS Arena ELO (1225), and GSM8K (93.0). Its capabilities make it an ideal choice for applications that require advanced text and vision processing, such as coding assistants, data analysis, and multilingual support. However, it is not recommended for tasks that require embeddings, bulk processing at low costs, real-time responses under 100ms, or vision-heavy workloads.

### Pricing and Cost Considerations
Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, with no additional costs for cached or batch inputs. This pricing model translates to $6.0 for 1,000 calls with an average of 500 tokens, $60.0 for 10,000 calls, and $600.0 for 100,000 calls. In comparison to its top competitor, GPT-4o, which is priced at $2.5/1M input and $10.0/1M output, Mistral Large 2 offers a competitive pricing structure, making it

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
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source and has a specific cost structure that will be analyzed in detail.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
- **Input**: $3.0 per 1M tokens
- **Output**: $9.0 per 1M tokens
- **Cached Input**: No additional cost ($None per 1M tokens)
- **Batch Input**: No additional cost ($None per 1M tokens)

This indicates that the primary cost factors are the input and output tokens. Cached and batch inputs do not incur additional costs, suggesting that utilizing these features can lead to significant savings.

#### When to Use Cached Tokens
Cached tokens can be particularly useful when dealing with repetitive or similar inputs, as they do not incur any additional cost. This feature can be beneficial in applications where the same or similar prompts are used multiple times, such as in coding, analysis, or chatbots.

#### Batch API Savings
While the pricing does not specify a direct cost savings for batch inputs, the fact that batch inputs are listed as $None per 1M tokens suggests that there might be indirect savings, such as reduced overhead or more efficient processing. However, without explicit cost savings, the primary benefit of batch processing in this context may be related to efficiency and throughput rather than direct cost reduction.

#### Cost at Scale
To understand the cost implications of using Mistral Large 2 at scale, let's examine the provided cost examples:
- **1,000 calls (avg 500 tokens)**: $6.0
- **10,000 calls**: $60.0
- **100,000 calls**: $600.0

These examples suggest a linear scaling

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 84.0 |
| HumanEval | 92.0 |
| LMSYS Arena ELO | 1225 |
| ARC | 93.0 |

## Benchmark Analysis
### Analysis of Mistral Large 2 Benchmark Performance
The Mistral Large 2 model, released by Mistral AI on 2024-07-24, is a premium, non-open-source model with a context window of 131,072 tokens and a maximum output of 4,096 tokens. The model's pricing is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens

#### Benchmark Scores
The model's benchmark performance is as follows:
* **MMLU (Massive Multitask Language Understanding)**: 84.0
	+ The MMLU score measures a model's ability to perform a wide range of natural language processing tasks. A higher score indicates better performance. With a score of 84.0, Mistral Large 2 demonstrates strong language understanding capabilities.
* **HumanEval**: 92.0
	+ The HumanEval score evaluates a model's ability to generate code that is correct and functional. A higher score indicates better performance. With a score of 92.0, Mistral Large 2 shows excellent code generation capabilities.
* **LMSYS Arena ELO**: 1225
	+ The LMSYS Arena ELO score measures a model's performance in a competitive environment, where models are pitted against each other to solve tasks. A higher score indicates better performance. With a score of 1225, Mistral Large 2 demonstrates strong competitive performance.
* **GSM8K**: 93.0
	+ The GSM8K score evaluates a model's ability to solve math problems. A higher score indicates better performance. With a score of 93.0

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. This comparison will focus on its pricing, performance, and capabilities in relation to its top competitors, specifically GPT-4o.

#### Pricing Comparison
| Model | Input Price per 1M Tokens | Output Price per 1M Tokens |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, whereas GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. This indicates that GPT-4o is cheaper for input tokens but more expensive for output tokens compared to Mistral Large 2.

#### Performance Trade-offs
Mistral Large 2 has the following benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

These scores are not directly comparable to GPT-4o without the latter's benchmark data. However, they suggest that Mistral Large 2 has strong performance across various tasks.

#### Capabilities and Use Cases
Mistral Large 2 supports the following capabilities:
- text
- vision
- function_calling
- json_mode
- streaming
- system_prompts

It is best suited for tasks such as:
- coding
- analysis
- rag
- agents
- multilingual
- function_calling

However, it is not recommended for:
- embeddings
- bulk_cheap
- real_time_sub_100ms
- vision_heavy

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100,000 calls: $600.0

#### Choosing Between Mistral Large 2 and GPT-4o
When deciding between Mistral

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. With its robust capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, it is best suited for tasks such as coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual tasks, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Given its capabilities and pricing structure, here are the top 5 best use cases for Mistral Large 2:

1. **Coding and Software Development**: With its high HumanEval score of 92.0, Mistral Large 2 is ideal for coding tasks, such as code completion, code review, and code generation. Its ability to understand and generate code in multiple programming languages makes it a valuable tool for software development teams.
2. **Complex Analysis and Reasoning**: Mistral Large 2's high MMLU score of 84.0 and LMSYS Arena ELO of 1225 indicate its ability to perform complex analysis and reasoning tasks. It can be used for tasks such as data analysis, research paper summarization, and decision-making.
3. **Multilingual Support**: With its multilingual capabilities, Mistral Large 2 can be used for tasks such as language translation, language understanding, and text generation in multiple languages.
4. **RAG and Information Retrieval**: Mistral Large 2's ability to perform RAG tasks makes it suitable for information retrieval and question-answering tasks. It can be used to retrieve relevant information from a large corpus of text and generate answers to user queries.
5. **Function Calling and API Integration**: Mistral Large 2's function calling capability allows it to integrate with external APIs and services. This makes it suitable for tasks such as data processing, workflow automation, and

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
