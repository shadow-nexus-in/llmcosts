# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-16
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly excelling in coding, analysis, and function calling tasks. This model boasts a context window of 131,072 tokens and can generate up to 4,096 tokens as output. Its architecture supports various capabilities including text and vision processing, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Strengths and Use Cases
Mistral Large 2 demonstrates its prowess through impressive benchmark scores: 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These scores underscore its effectiveness in handling complex tasks, especially those requiring coding and analytical capabilities. Its primary use cases include coding assistance, in-depth analysis, and tasks that benefit from its function calling and multilingual support. However, it's not recommended for applications focused on embeddings, bulk processing at low costs, real-time responses under 100ms, or vision-heavy tasks.

### Pricing and Cost Considerations
The pricing model for Mistral Large 2 is structured as follows: $3.0 per 1M input tokens and $9.0 per 1M output tokens. There are no specified costs for cached input or batch input. To give developers a clearer picture, example costs include $6.0 for 1,000 calls averaging 500 tokens, $60.0 for 10,000 calls, and $600.0 for 100,000 calls. When comparing with top competitors like GPT-4o, which offers $2.5/1M input and $10.0/1M output, developers must weigh the costs against the unique strengths and capabilities of Mistral

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
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. The pricing structure for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### Cost Structure
The cost of using Mistral Large 2 is primarily determined by the number of input and output tokens. The model's context window is 131,072 tokens, and the maximum output is 4,096 tokens. 

#### Cached Tokens and Batch API Savings
Cached input tokens are free, which can significantly reduce costs for applications that involve repeated input sequences. Similarly, batch input is also free, making it an attractive option for bulk processing. However, the actual cost savings from caching and batching will depend on the specific use case and the proportion of repeated or batched inputs.

#### Cost at Scale
To illustrate the cost of using Mistral Large 2 at scale, consider the following examples:
* 1,000 API calls with an average of 500 tokens per call: $6.0
* 10,000 API calls: $60.0
* 100,000 API calls: $600.0

These examples suggest a linear scaling of costs with the number of API calls. To estimate the cost of using Mistral Large 2 for a specific application, it's essential to consider the average number of tokens per call and the total number of calls.

#### Comparison with Top Competitors
Mistral Large 2's pricing is comparable to its top competitors, such as GPT-4o,

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 84.0 |
| HumanEval | 92.0 |
| LMSYS Arena ELO | 1225 |
| ARC | 93.0 |

## Benchmark Analysis
### Analysis of Mistral Large 2 Benchmark Performance
#### Model Overview
The Mistral Large 2 model, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. It has a context window of 131,072 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2024-07.

#### Pricing
The pricing for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Benchmark Performance
The benchmark performance of Mistral Large 2 is:
* MMLU: 84.0
* HumanEval: 92.0
* LMSYS Arena ELO: 1225
* GSM8K: 93.0

These benchmarks indicate the model's performance in various areas:
* **MMLU (Massive Multitask Language Understanding)**: A score of 84.0 indicates that Mistral Large 2 has a strong understanding of language, but may struggle with certain tasks that require more nuanced or specialized knowledge.
* **HumanEval**: A score of 92.0 suggests that Mistral Large 2 is highly effective at evaluating and generating human-like text, making it well-suited for tasks such as coding, analysis, and writing.
* **LMSYS Arena ELO**: An ELO score of 1225 indicates that Mistral Large 2 has a high level of competence in a wide range of tasks, but may not be the top

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, a premium model by Mistral AI, offers a unique blend of capabilities, including text, vision, function calling, and more. Released on 2024-07-24, it stands out in the market with its performance and pricing. This comparison will delve into the specifics of Mistral Large 2 versus its top competitor, GPT-4o, focusing on price differences, performance trade-offs, and scenarios where each model is the better choice.

#### Pricing Comparison
| Model | Input Price per 1M Tokens | Output Price per 1M Tokens |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, whereas GPT-4o is priced at $2.5 per 1M input tokens but $10.0 per 1M output tokens. This indicates that for input-heavy tasks, GPT-4o might be more cost-effective, but for tasks where output is more significant, Mistral Large 2 offers a better deal.

#### Performance Trade-offs
Mistral Large 2 boasts impressive benchmarks:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

While specific benchmarks for GPT-4o are not provided, the choice between these models will often depend on the specific requirements of the task at hand. Mistral Large 2's capabilities in coding, analysis, and function calling make it a strong contender for tasks that require these skills.

#### Capabilities and Best Use Cases
Mistral Large 2 is best suited for:
- Coding
- Analysis
- RAG (Retrieval-Augmented Generation)
- Agents
- Multilingual tasks
- Function calling

It is not recommended for:
- Embeddings
- Bulk cheap operations
- Real-time operations under 100ms
- Vision-heavy tasks

#### Cost Examples
For Mistral Large 2, the costs are as follows:
- 1,000 calls (avg 500 tokens): $6

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium model with a wide range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. Released on 2024-07-24, this model excels in coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual tasks, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Given its capabilities and pricing, here are the top 5 best use cases for Mistral Large 2:

1. **Coding Assistance**: With its high scores in HumanEval (92.0) and LMSYS Arena ELO (1225), Mistral Large 2 is ideal for coding tasks, such as code completion, code review, and code generation.
2. **Complex Analysis**: The model's large context window (131,072 tokens) and high MMLU score (84.0) make it suitable for complex analysis tasks, such as text summarization, sentiment analysis, and data analysis.
3. **RAG and Agents**: Mistral Large 2's capabilities in RAG and agents make it a great choice for tasks that require generating text based on external knowledge, such as chatbots, virtual assistants, and content generation.
4. **Multilingual Support**: With its multilingual capabilities, Mistral Large 2 can be used for tasks that require language translation, language understanding, and language generation.
5. **Function Calling and JSON Mode**: The model's ability to call functions and parse JSON data makes it suitable for tasks that require integrating with external APIs, such as data processing, data validation, and data transformation.

### Code Integration Examples with OpenRouter
To integrate Mistral Large 2 with OpenRouter, you can use the following code examples:
```python
import openrouter

# Initialize the Mistral Large 2 model
model =

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
