# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-05
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed for a wide range of applications, including coding, analysis, and multilingual support. This model boasts a context window of 131,072 tokens and can generate up to 4,096 output tokens. With a knowledge cutoff of 2024-07, Mistral Large 2 is equipped with the latest information available up to that point. Its architecture supports various capabilities such as text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Strengths and Use Cases
Mistral Large 2 demonstrates its technical prowess through impressive benchmark scores: 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These scores underscore its potential for coding, analysis, and other complex tasks. The model is best utilized for applications requiring advanced text processing, function calling, and multilingual support. However, it may not be the ideal choice for tasks that require embeddings, bulk processing at low costs, real-time responses under 100ms, or vision-heavy workloads. Developers can leverage Mistral Large 2's strengths in areas like coding assistance, data analysis, and agent development, where its capabilities can significantly enhance productivity and accuracy.

### Pricing and Cost Considerations
The pricing for Mistral Large 2 is structured as follows: $3.0 per 1M input tokens and $9.0 per 1M output tokens. There are no specified costs for cached input or batch input. To put this into perspective, 1,000 calls averaging 500 tokens each would cost $6.0, scaling to $60.0 for 10,000 calls and $600.0 for 100

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
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. The pricing structure is based on input and output tokens.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached input tokens are free, making them an attractive option when possible. Use cached tokens when:
* The input data is repetitive or has a high overlap between requests.
* The application can tolerate some delay in updating the input data.

#### Batch API Savings
Batch input tokens are also free. To maximize savings, use batch API calls when:
* Processing large volumes of data.
* The application can handle batch processing without significant performance degradation.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* 1,000 API calls (avg 500 tokens): $6.0
* 10,000 API calls: $60.0
* 100,000 API calls: $600.0

To estimate the cost at scale, consider the average number of tokens per call and the ratio of input to output tokens. Based on the provided cost examples, the cost per call appears to be relatively constant, suggesting a linear scaling of costs with the number of API calls.

#### Comparison to Top Competitors
Mistral Large 2's pricing is competitive with top competitors like GPT-4o, which charges $2.5/1M input and $10.0/1M

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
The Mistral Large 2 model, released by Mistral AI on 2024-07-24, is a premium, non-open-source model with a context window of 131,072 tokens and a maximum output of 4,096 tokens. Its knowledge cutoff is 2024-07.

#### Pricing
The pricing for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Benchmark Performance
The model's benchmark performance is:
* MMLU: **84.0** - This score indicates the model's ability to understand and process mathematical and logical concepts. A higher score suggests better performance in tasks that require mathematical reasoning and problem-solving.
* HumanEval: **92.0** - This score measures the model's ability to evaluate and execute human-written code. A higher score suggests better performance in coding tasks and programming-related applications.
* LMSYS Arena ELO: **1225** - This score is a measure of the model's overall performance in a competitive arena, where it is pitted against other models. A higher score indicates better performance and a higher ranking in the arena.
* GSM8K: **93.0** - This score is not explicitly defined in the provided data, but it is likely a measure of the model's performance on a specific benchmark or task.

#### Real-World Implications
The benchmark scores suggest that Mistral Large 2 is a strong performer in tasks that require

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. This comparison will focus on its pricing, performance, and capabilities against its top competitor, GPT-4o.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, whereas GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. This indicates that GPT-4o is cheaper for input tokens but more expensive for output tokens.

#### Performance Comparison
Mistral Large 2 has the following benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

In contrast, the benchmark scores for GPT-4o are not provided. However, based on the available data, Mistral Large 2 demonstrates strong performance across various benchmarks.

#### Capabilities and Use Cases
Mistral Large 2 supports the following capabilities:
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
- Multilingual
- Function calling

On the other hand, it is not recommended for tasks that require:
- Embeddings
- Bulk cheap processing
- Real-time sub-100ms processing
- Vision-heavy tasks

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100,000 calls: $600.0

#### Choosing Between Mistral Large 2 and GPT-4o

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium model released on 2024-07-24. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts, making it suitable for tasks such as coding, analysis, and multilingual support.

### Top 5 Best Use Cases for Mistral Large 2
Given its capabilities and pricing, here are the top 5 best use cases for Mistral Large 2:

1. **Coding and Development**: With its high scores in HumanEval (92.0) and GSM8K (93.0), Mistral Large 2 is well-suited for coding tasks, such as code completion, code review, and bug fixing. Its ability to understand and generate code in multiple languages makes it an ideal choice for developers.
2. **Analysis and Research**: The model's high MMLU score (84.0) and large context window (131,072 tokens) make it suitable for in-depth analysis and research tasks, such as text analysis, sentiment analysis, and information retrieval.
3. **RAG (Retrieve, Augment, Generate) Tasks**: Mistral Large 2's ability to retrieve information, augment existing text, and generate new text makes it well-suited for RAG tasks, such as question answering, text summarization, and content generation.
4. **Agents and Chatbots**: With its ability to understand and respond to user input, Mistral Large 2 can be used to build conversational agents and chatbots that can engage with users in multiple languages.
5. **Multilingual Support**: The model's support for multiple languages makes it an ideal choice for applications that require language translation, language detection, and multilingual text analysis.

### Code Integration Examples with OpenRouter
To integrate Mistral Large 2 with OpenRouter, you can use the following code examples:

```python

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
