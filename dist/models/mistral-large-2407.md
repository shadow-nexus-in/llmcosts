# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-28
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. This model boasts an impressive architecture that supports a wide range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. With a context window of 131,072 tokens and a maximum output of 4,096 tokens, Mistral Large 2 is well-suited for complex tasks that require a deep understanding of the input context.

### Technical Strengths and Use Cases
Mistral Large 2 demonstrates its strengths through various benchmarks, achieving scores of 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These results indicate that the model excels in tasks such as coding, analysis, and function calling. Its capabilities make it an ideal choice for applications that involve multilingual support, agents, and RAG (Retrieve, Augment, Generate) tasks. However, it is not recommended for tasks that require embeddings, bulk processing at a low cost, real-time responses under 100ms, or vision-heavy workloads.

### Pricing and Cost Considerations
The pricing for Mistral Large 2 is structured as follows: $3.0 per 1M input tokens and $9.0 per 1M output tokens. There are no additional costs for cached input or batch input. To illustrate the cost, 1,000 calls with an average of 500 tokens would cost $6.0, while 10,000 calls would cost $60.0, and 100,000 calls would cost $600.0. In comparison to its top competitor, GPT-4o, which charges $2.5/1M input and $10.0/1M output, Mistral Large 

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
Mistral Large 2 is a premium model offered by Mistral AI, released on 2024-07-24. This model is not open source and has a unique pricing structure. The following analysis will break down the cost structure, provide guidance on when to use cached tokens, discuss batch API savings, and examine the cost at scale.

#### Cost Structure
The pricing for Mistral Large 2 is as follows:
* Input: **$3.0 per 1M tokens**
* Output: **$9.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (no additional cost)
* Batch Input: **$0 per 1M tokens** (no additional cost)

#### Cached Tokens
Since cached input tokens do not incur any additional cost, it is recommended to use cached tokens whenever possible to minimize expenses.

#### Batch API Savings
Although batch input tokens do not have a specified cost, it is essential to note that the cost examples provided suggest a linear scaling of costs with the number of API calls. Therefore, batch API calls may not provide direct savings, but they can still help optimize costs by reducing the number of individual API requests.

#### Cost at Scale
The cost examples provided illustrate the cost of using Mistral Large 2 at different scales:
* **1,000 calls (avg 500 tokens)**: **$6.0**
* **10,000 calls**: **$60.0**
* **100,000 calls**: **$600.0**

To estimate the cost of using Mistral Large 2, we can calculate the cost per call based on the average number of tokens per call. Assuming an average of 500 tokens per call, the cost per call can be estimated as follows:
* **1,000 calls**: **$6.0 / 1,000 calls = $0.006 per call**
*

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
The Mistral Large 2 model, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. It is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens.

#### Benchmark Scores
The model's performance is measured by the following benchmark scores:
* **MMLU (Massive Multitask Language Understanding)**: 84.0, indicating the model's ability to understand and generate human-like text across a wide range of tasks and topics.
* **HumanEval**: 92.0, measuring the model's ability to write correct and functional code in response to programming prompts.
* **LMSYS Arena ELO**: 1225, representing the model's competitive performance in a large-scale language model benchmarking arena.
* **GSM8K**: 93.0, evaluating the model's math problem-solving abilities.

#### Real-World Implications
These benchmark scores suggest that Mistral Large 2 is:
* Suitable for coding tasks, with a high HumanEval score indicating strong programming abilities.
* Effective in analysis tasks, given its high MMLU score.
* Competitive in large-scale language model benchmarks, as evidenced by its LMSYS Arena ELO score.
* Capable of handling math problems, with a high GSM8K score.

#### Capabilities and Limitations
Mistral Large 2 supports various capabilities, including:
* Text and vision processing
* Function calling and JSON mode
* Streaming and system prompts
It is best suited for tasks such as:
* Coding and analysis
* Multilingual support
*

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. It offers a range of capabilities including text, vision, function calling, and more, making it suitable for tasks like coding, analysis, and multilingual support. This comparison will focus on its pricing, performance, and trade-offs against its top competitor, GPT-4o.

#### Pricing Comparison
| Model | Input Price per 1M tokens | Output Price per 1M tokens |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, whereas GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. This indicates that while GPT-4o is cheaper for input, Mistral Large 2 is more cost-effective for output.

#### Performance Comparison
Mistral Large 2 has the following benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

In contrast, specific benchmark scores for GPT-4o are not provided in the data. However, considering the general performance of models in this tier, Mistral Large 2's scores suggest high capabilities in coding, analysis, and other tasks it's best suited for.

#### Context and Limits
Mistral Large 2 has a context window of 131,072 tokens and a max output of 4,096 tokens, with a knowledge cutoff of 2024-07. These specifications are not directly compared to GPT-4o due to lack of data but are crucial for understanding the model's limitations and suitability for specific tasks.

#### Capabilities and Best Use Cases
Mistral Large 2 supports a wide range of capabilities including text, vision, function calling, and more, making it best for:
- Coding
- Analysis
- RAG (Retrieval-Augmented Generation)
- Agents
- Mult

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, a premium model provided by Mistral AI, offers a robust set of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. With its release on 2024-07-24, it has established itself as a powerful tool for various applications, particularly in coding, analysis, and multilingual tasks.

### Top 5 Best Use Cases for Mistral Large 2
Given its capabilities and pricing structure, here are the top 5 best use cases for Mistral Large 2:

1. **Coding and Development**: Mistral Large 2 excels in coding tasks, making it an ideal choice for developers looking to automate code generation, code review, or even assist in complex coding projects. Its high score in HumanEval (92.0) demonstrates its proficiency in coding tasks.

2. **Advanced Analysis**: With its strong performance in analysis tasks, Mistral Large 2 can be utilized for in-depth analysis of large datasets, providing insights that might be challenging for humans to discern. Its context window of 131,072 tokens allows for the analysis of extensive texts.

3. **RAG (Retrieval-Augmented Generation) Tasks**: Mistral Large 2's ability to handle RAG tasks efficiently makes it suitable for applications that require generating text based on external knowledge sources. This is particularly useful in tasks that demand up-to-date and accurate information.

4. **Multilingual Support**: Given its multilingual capabilities, Mistral Large 2 can be employed in projects that require support for multiple languages. This makes it an excellent choice for global applications or services targeting diverse linguistic audiences.

5. **Function Calling and Automation**: With its function calling capability, Mistral Large 2 can automate complex workflows by integrating with external services or APIs. This feature, combined with its ability to handle JSON mode and streaming, makes it versatile for a wide range of automation tasks.

### Code

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
