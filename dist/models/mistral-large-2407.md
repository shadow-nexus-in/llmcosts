# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-14
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly those requiring advanced capabilities such as text, vision, function calling, and more. With a context window of 131,072 tokens and a maximum output of 4,096 tokens, Mistral Large 2 is well-suited for tasks that demand both breadth and depth of understanding. Its architecture, while not fully detailed here, supports complex interactions through capabilities like JSON mode, streaming, and system prompts.

### Technical Strengths and Use Cases
The technical strengths of Mistral Large 2 are underscored by its benchmark performance: achieving 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These scores indicate a high level of competence in areas such as coding, analysis, and multilingual support. The model is best utilized for applications involving coding, analysis, retrieval-augmented generation (RAG), agents, and function calling, where its advanced capabilities can be fully leveraged. However, it is not recommended for tasks requiring embeddings, bulk cheap processing, real-time responses under 100ms, or vision-heavy applications.

### Pricing and Cost Considerations
The pricing model for Mistral Large 2 is based on input and output tokens, with costs of $3.0 per 1M input tokens and $9.0 per 1M output tokens. For developers, understanding these costs is crucial for budgeting and planning. For example, 1,000 calls averaging 500 tokens each would cost $6.0, scaling up to $60.0 for 10,000 calls and $600.0 for 100,000 calls. When comparing with competitors like GPT-4o, which

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
Mistral Large 2, provided by Mistral AI, is a premium model released on 2024-07-24. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale.

#### Cost Structure
The pricing for Mistral Large 2 is as follows:
* Input: **$3.0 per 1M tokens**
* Output: **$9.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following strategies:
* **Use cached tokens**: Since cached input tokens are free, utilize them whenever possible to reduce input costs.
* **Batch API calls**: With batch input tokens being free, batching API calls can lead to significant cost savings.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* **1,000 API calls** (avg 500 tokens): **$6.0**
* **10,000 API calls**: **$60.0**
* **100,000 API calls**: **$600.0**

To put this into perspective, assuming an average of 500 tokens per call, the cost per call can be broken down as follows:
* Input cost: **$3.0 per 1M tokens** = **$0.003 per token**
* Output cost: **$9.0 per 1M tokens** = **$0.009 per token**
* Assuming an average output of 200 tokens per call (conservative estimate), the output cost per call would be: **200 tokens \* $0.009 per token** = **$1.80 per call**
* Input cost per call (500 tokens): **500 tokens \* $0.

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
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. The pricing for this model is as follows:
- Input: $3.0 per 1M tokens
- Output: $9.0 per 1M tokens

#### Benchmark Scores
The model's performance is measured by several benchmark scores:
- **MMLU (Massive Multitask Language Understanding)**: 84.0. This score indicates the model's ability to understand and process a wide range of language tasks. A higher MMLU score suggests better performance in tasks such as text analysis, question answering, and language translation.
- **HumanEval**: 92.0. This score evaluates the model's ability to generate code that is correct and functional. A higher HumanEval score indicates better performance in coding tasks, making Mistral Large 2 suitable for applications such as code completion and code review.
- **LMSYS Arena ELO**: 1225. This score measures the model's performance in a competitive environment, where it is pitted against other models in a series of tasks. A higher LMSYS Arena ELO score suggests better overall performance and adaptability.

#### Real-World Implications
The benchmark scores suggest that Mistral Large 2 is well-suited for real-world applications that require:
- Advanced language understanding and processing (MMLU: 84.0)
- Code generation and review (HumanEval: 92.0)
- Competitive performance in a variety of tasks

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. This comparison will focus on its pricing, performance, and capabilities in relation to its top competitors, specifically GPT-4o.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, whereas GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. This indicates that while GPT-4o is cheaper for input, Mistral Large 2 is more cost-effective for output.

#### Performance Trade-offs
Mistral Large 2 has the following benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

These scores suggest that Mistral Large 2 excels in coding, analysis, and multilingual tasks. However, without direct comparison data for GPT-4o, it's challenging to assess the performance differences between the two models directly.

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
- Multilingual tasks
- Function calling

On the other hand, it is not recommended for:
- Embeddings
- Bulk cheap tasks
- Real-time tasks requiring sub-100ms response times
- Vision-heavy tasks

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. With its impressive capabilities in coding, analysis, and function calling, it stands out as a powerful tool for various applications. This guide will explore the top 5 best use cases for Mistral Large 2, along with practical advice and code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Large 2
1. **Coding and Development**: Mistral Large 2 excels in coding tasks, making it an ideal choice for developers. Its ability to understand and generate code in multiple languages can significantly enhance development productivity.
2. **Data Analysis**: With its strong analytical capabilities, Mistral Large 2 can be used for data analysis, providing insights and patterns that might be difficult to discern manually.
3. **Question Answering and RAG (Retrieve, Augment, Generate)**: The model's performance in question answering and RAG tasks is notable, making it suitable for applications that require generating human-like responses based on a knowledge base.
4. **Multilingual Support**: Given its multilingual capabilities, Mistral Large 2 can be applied in scenarios where support for multiple languages is necessary, such as in global customer service chatbots.
5. **Function Calling and Integration**: Its ability to call functions and integrate with other systems makes Mistral Large 2 a valuable asset for automating complex workflows and tasks.

### Code Integration Example with OpenRouter
To integrate Mistral Large 2 with OpenRouter for a coding task, you might use the following approach:
```python
import openrouter

# Initialize the Mistral Large 2 model
model = openrouter.Model(
    name="mistralai/mistral-large-2407",
    provider="Mistral AI",
    input_token_cost=3.0,
    output_token_cost=9.

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
