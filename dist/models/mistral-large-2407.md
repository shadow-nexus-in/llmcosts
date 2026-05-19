# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-19
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly in coding, analysis, and multilingual tasks. With a context window of 131,072 tokens and a maximum output of 4,096 tokens, this model is capable of handling complex and lengthy inputs. Its architecture supports various capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Strengths and Use Cases
The Mistral Large 2 model boasts impressive benchmarks, with scores of 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These metrics indicate the model's strengths in coding, analysis, and other tasks that require a deep understanding of context and the ability to generate coherent and accurate outputs. The model is best suited for applications such as coding, analysis, retrieval-augmented generation (RAG), agents, multilingual tasks, and function calling. However, it may not be the most cost-effective option for tasks that require embeddings, bulk processing, real-time responses under 100ms, or vision-heavy workloads.

### Pricing and Cost Considerations
The pricing for Mistral Large 2 is as follows: $3.0 per 1M input tokens and $9.0 per 1M output tokens. There are no additional costs for cached input or batch input. To give developers a better understanding of the costs involved, examples are provided: 1,000 calls with an average of 500 tokens cost $6.0, while 10,000 calls cost $60.0, and 100,000 calls cost $600.0. In comparison to its top competitor, GPT-

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
Mistral Large 2 is a premium model offered by Mistral AI, released on 2024-07-24. This analysis will delve into the cost structure, usage scenarios, and scalability of this model.

#### Cost Structure
The pricing for Mistral Large 2 is as follows:
* Input: **$3.0 per 1M tokens**
* Output: **$9.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### Usage Scenarios
* **Cached Tokens**: Since cached input tokens are free, it is recommended to use them whenever possible to reduce costs. This can be particularly useful for applications with repetitive or similar input patterns.
* **Batch API**: With batch input being free, utilizing the batch API can lead to significant cost savings, especially for large-scale applications.

#### Cost at Scale
The cost of using Mistral Large 2 at different scales is as follows:
* **1,000 API calls** (avg 500 tokens): **$6.0**
* **10,000 API calls**: **$60.0**
* **100,000 API calls**: **$600.0**

To estimate the cost at scale, we can use the input and output pricing. Assuming an average of 500 tokens per call, the total tokens for 1,000 calls would be 500,000 tokens. Based on the pricing, this would translate to:
* Input: 500,000 tokens / 1,000,000 tokens per unit = 0.5 units \* $3.0 per unit = **$1.5**
* Output: Assuming an average output of 200 tokens per call (conservative estimate), the total output tokens for 1,000 calls would be 200,000 tokens.

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
* Input: **$3.0 per 1M tokens**
* Output: **$9.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Benchmark Performance
The model's benchmark performance is measured by the following metrics:
* **MMLU (Massive Multitask Language Understanding)**: 84.0 - This score indicates the model's ability to understand and perform a wide range of natural language processing tasks. A higher score suggests better performance in tasks such as text classification, sentiment analysis, and question answering.
* **HumanEval**: 92.0 - This score measures the model's ability to evaluate and execute human-written code. A higher score indicates better performance in coding tasks, such as code completion and code review.
* **LMSYS Arena ELO**: 1225 - This score represents the model's performance in a competitive arena, where it is pitted against other models in a variety of tasks. A higher ELO score indicates better overall performance and adaptability.
* **GSM8K**: 93.0 - This score measures the model's ability to solve math problems, specifically the Grade School Math (GSM) dataset.



## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, a premium model by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, it has a context window of 131,072 tokens and a max output of 4,096 tokens. In this comparison, we will evaluate Mistral Large 2 against its top competitor, GPT-4o, in terms of pricing, performance, and use cases.

#### Pricing Comparison
The pricing for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens

In comparison, GPT-4o is priced at:
* Input: $2.5 per 1M tokens
* Output: $10.0 per 1M tokens

Mistral Large 2 is more expensive than GPT-4o in terms of input pricing, but slightly cheaper in terms of output pricing.

#### Performance Comparison
Mistral Large 2 has the following benchmark scores:
* MMLU: 84.0
* HumanEval: 92.0
* LMSYS Arena ELO: 1225
* GSM8K: 93.0

While the benchmark scores for GPT-4o are not provided, Mistral Large 2's scores indicate strong performance in coding, analysis, and other tasks.

#### Performance Trade-offs
Mistral Large 2 has a larger context window (131,072 tokens) compared to other models, making it suitable for tasks that require longer input sequences. However, its max output limit of 4,096 tokens may be a constraint for tasks that require longer output sequences.

#### When to Choose Each Model
Mistral Large 2 is best suited for tasks that require:
* Coding and analysis
* Multilingual support
* Function calling
* Streaming and system prompts

On the other hand, GPT-4o may be a better choice for tasks that require:
* Lower input costs
* Higher output limits
* Real-time responses (although this is not a strong suit for either model)

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
* 1,000 calls (avg 500 tokens): $6.0
* 

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model that excels in various tasks, including coding, analysis, and function calling. With its capabilities in text, vision, and function calling, it's an ideal choice for applications requiring advanced language understanding and generation.

### Top 5 Best Use Cases for Mistral Large 2
Based on its capabilities and benchmarks, here are the top 5 best use cases for Mistral Large 2:

1. **Coding and Software Development**: With its high scores in HumanEval (92.0) and GSM8K (93.0), Mistral Large 2 is well-suited for coding tasks, such as code completion, code review, and code generation.
2. **Data Analysis and Insights**: Mistral Large 2's capabilities in text analysis and its high MMLU score (84.0) make it an excellent choice for data analysis, report generation, and insights extraction.
3. **Conversational Agents and Chatbots**: With its high LMSYS Arena ELO score (1225), Mistral Large 2 can be used to build conversational agents and chatbots that can understand and respond to user queries in a more human-like way.
4. **Multilingual Support and Translation**: Mistral Large 2's support for multilingual tasks makes it an ideal choice for applications requiring translation, language understanding, and generation in multiple languages.
5. **Function Calling and API Integration**: With its function calling capability, Mistral Large 2 can be used to integrate with external APIs and services, enabling more complex and dynamic applications.

### Code Integration Example with OpenRouter
To integrate Mistral Large 2 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Mistral Large 2 model
model = openrouter.Model("

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
