# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-29
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, including coding, analysis, and multilingual support. This model boasts a context window of 131,072 tokens and can generate up to 4,096 tokens as output. With a knowledge cutoff of 2024-07, Mistral Large 2 is well-equipped to handle tasks that require extensive contextual understanding and the ability to process large amounts of information.

### Technical Strengths and Use Cases
Mistral Large 2's architecture supports various capabilities such as text and vision processing, function calling, JSON mode, streaming, and system prompts. Its strengths are reflected in its benchmark scores: MMLU at 84.0, HumanEval at 92.0, LMSYS Arena ELO at 1225, and GSM8K at 93.0. These scores indicate the model's proficiency in handling complex tasks, coding challenges, and mathematical problems. The model is best suited for applications involving coding, analysis, retrieval-augmented generation (RAG), agents, multilingual tasks, and function calling. However, it may not be the ideal choice for tasks requiring embeddings, bulk processing at low costs, real-time responses under 100ms, or vision-heavy applications.

### Pricing and Cost Considerations
The pricing for Mistral Large 2 is structured as follows: $3.0 per 1M input tokens and $9.0 per 1M output tokens. There are no specified costs for cached input or batch input. To give developers a clearer picture, example costs include $6.0 for 1,000 calls averaging 500 tokens, $60.0 for 10,000 calls, and $600.0 for 100,000 calls. In comparison to its top competitor, GPT-

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
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is well-suited for coding, analysis, and multilingual applications.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
* **Input**: $3.0 per 1M tokens
* **Output**: $9.0 per 1M tokens
* **Cached Input**: $0 per 1M tokens (free)
* **Batch Input**: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for applications where input tokens can be reused. This can be particularly useful in scenarios where the same input is used multiple times, such as in chatbots or virtual assistants.

#### Batch API Savings
Batch input is also free, which means that making API calls in batches can significantly reduce costs. This is ideal for applications that require processing large amounts of data in parallel, such as data analysis or machine learning workflows.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: $6.0
* **10,000 calls**: $60.0
* **100,000 calls**: $600.0

These costs demonstrate a linear scaling of costs with the number of API calls, indicating that the cost per call remains constant regardless of the scale.

#### Comparison to Top Competitors
Mistral Large 2's pricing is competitive with top competitors like GPT-4o, which charges $2.5/1M input and $10.0/1M output. While GPT-4o's input cost is lower, Mistral Large 2's free

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 84.0 |
| HumanEval | 92.0 |
| LMSYS Arena ELO | 1225 |
| ARC | 93.0 |

## Benchmark Analysis
### Mistral Large 2 Benchmark Performance Analysis
#### Overview
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is designed for various applications such as coding, analysis, and multilingual tasks.

#### Pricing
The pricing for Mistral Large 2 is as follows:
- Input: **$3.0 per 1M tokens**
- Output: **$9.0 per 1M tokens**
- Cached Input: **$None per 1M tokens**
- Batch Input: **$None per 1M tokens**

#### Benchmark Scores
Mistral Large 2 has achieved the following benchmark scores:
- **MMLU: 84.0** - The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to perform a wide range of natural language processing tasks. A higher MMLU score indicates better performance in understanding and generating human-like language.
- **HumanEval: 92.0** - The HumanEval benchmark assesses a model's ability to write correct and functional code based on human-provided specifications. A higher HumanEval score suggests stronger coding capabilities.
- **LMSYS Arena ELO: 1225** - The LMSYS Arena ELO score measures a model's performance in a competitive environment, where it is pitted against other models in various tasks. A higher ELO score indicates better overall performance and adaptability.
- **GSM8K: 93.0** - The GSM8K benchmark evaluates a model's ability to reason and solve math problems. A

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, a premium model provided by Mistral AI, is a powerful language model with a wide range of capabilities, including text, vision, function calling, and more. Released on 2024-07-24, it offers a unique set of features and performance metrics. In this comparison, we will evaluate Mistral Large 2 against its top competitors, focusing on price differences, performance trade-offs, and use cases.

#### Pricing Comparison
The pricing for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens

In comparison, GPT-4o, a top competitor, offers:
* Input: $2.5 per 1M tokens
* Output: $10.0 per 1M tokens

Mistral Large 2 is more expensive in terms of input tokens, but its output token price is slightly lower than GPT-4o.

#### Performance Comparison
Mistral Large 2 boasts impressive benchmark scores:
* MMLU: 84.0
* HumanEval: 92.0
* LMSYS Arena ELO: 1225
* GSM8K: 93.0

While the benchmark scores for GPT-4o are not provided, Mistral Large 2's scores indicate strong performance in various tasks, including coding, analysis, and multilingual support.

#### Capabilities and Limitations
Mistral Large 2 offers a wide range of capabilities, including:
* Text
* Vision
* Function calling
* JSON mode
* Streaming
* System prompts

However, it is not suitable for:
* Embeddings
* Bulk cheap processing
* Real-time sub-100ms processing
* Vision-heavy tasks

#### Cost Examples
To illustrate the cost of using Mistral Large 2, consider the following examples:
* 1,000 calls (avg 500 tokens): $6.0
* 10,000 calls: $60.0
* 100,000 calls: $600.0

#### Choosing the Right Model
When deciding between Mistral Large 2 and its competitors, consider the following factors:
* **Price sensitivity**: If input token cost is a significant concern, GPT-4o might be a more attractive option. However,

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. With its robust capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, it is best suited for coding, analysis, RAG (Retrieve, Augment, Generate), agents, multilingual tasks, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Given its capabilities and pricing structure, here are the top 5 best use cases for Mistral Large 2:

1. **Coding Assistance**: With high scores in HumanEval (92.0) and GSM8K (93.0), Mistral Large 2 is ideal for coding tasks, such as code completion, code review, and code generation.
2. **Complex Analysis**: Its high MMLU score (84.0) and large context window (131,072 tokens) make it suitable for complex analysis tasks, such as text analysis, sentiment analysis, and data analysis.
3. **Multilingual Support**: As it supports multilingual tasks, Mistral Large 2 can be used for language translation, language understanding, and language generation.
4. **RAG and Agents**: With its capabilities in RAG and agents, Mistral Large 2 can be used for tasks such as question answering, dialogue systems, and chatbots.
5. **Function Calling**: Its ability to perform function calling makes it suitable for tasks such as API integration, data processing, and automation.

### Code Integration Examples with OpenRouter
To integrate Mistral Large 2 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the OpenRouter client
client = openrouter.Client("mistralai/mistral-large-2407")

# Define a function to call the model
def call_model(prompt):
    response = client

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
