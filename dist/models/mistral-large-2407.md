# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-03
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, including coding, analysis, and function calling. This model boasts an impressive architecture with a context window of 131,072 tokens and a maximum output of 4,096 tokens. Its capabilities extend to text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Strengths and Use Cases
Mistral Large 2 demonstrates its strengths through various benchmarks: it achieves an MMLU score of 84.0, a HumanEval score of 92.0, an LMSYS Arena ELO of 1225, and a GSM8K score of 93.0. These scores indicate the model's proficiency in coding, analysis, and other complex tasks. Its best use cases include coding, analysis, RAG (Retrieve, Augment, Generate), agents, multilingual tasks, and function calling. However, it is not recommended for embeddings, bulk cheap operations, real-time sub-100ms applications, or vision-heavy tasks.

### Pricing and Cost Considerations
The pricing for Mistral Large 2 is structured as follows: $3.0 per 1M input tokens and $9.0 per 1M output tokens. There are no specified costs for cached input or batch input. To give developers a better understanding of the costs involved, example costs are provided: 1,000 calls averaging 500 tokens cost $6.0, 10,000 calls cost $60.0, and 100,000 calls cost $600.0. In comparison to its top competitor, GPT-4o, which charges $2.5/1M input and $10.0/1M output, Mistral Large 2 offers competitive

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
Mistral Large 2 is a premium model offered by Mistral AI, released on 2024-07-24. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following scenarios:
* **Cached Tokens**: Utilize cached input tokens whenever possible, as they are free. This is ideal for applications with repetitive or similar input prompts.
* **Batch API Calls**: Leverage batch input to reduce costs, as it is also free. This is suitable for applications that can process multiple inputs simultaneously.

#### Cost at Scale
The cost of using Mistral Large 2 at various scales is as follows:
* **1,000 API Calls**: $6.0 (avg 500 tokens per call)
* **10,000 API Calls**: $60.0
* **100,000 API Calls**: $600.0

To estimate costs for custom scenarios, consider the average number of input and output tokens per call. For example, if your application averages 200 input tokens and 100 output tokens per call, the cost per call would be:
* Input: 200 tokens / 1,000,000 tokens * $3.0 = $0.0006
* Output: 100 tokens / 1,000,000 tokens * $9.0 = $0.0009
* Total Cost per Call: $0.0006 + $0.0009 = $0.0015

For 1,

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
The Mistral Large 2 model, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. It is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens.

#### Benchmark Performance
The model's performance is measured by the following benchmarks:
* **MMLU (Massive Multitask Language Understanding)**: 84.0 - This score indicates the model's ability to understand and generate human-like language across a wide range of tasks. A higher score suggests better performance in tasks such as text classification, sentiment analysis, and language translation.
* **HumanEval**: 92.0 - This score evaluates the model's ability to write correct and functional code in response to programming prompts. A higher score indicates better performance in coding tasks, such as code completion and code generation.
* **LMSYS Arena ELO**: 1225 - This score measures the model's performance in a competitive arena, where it is pitted against other models in a series of tasks. A higher ELO score indicates better overall performance and adaptability.

#### Real-World Implications
The benchmark scores suggest that the Mistral Large 2 model is well-suited for tasks that require:
* Strong language understanding and generation capabilities (MMLU: 84.0)
* Accurate and functional code generation (HumanEval: 92.0)
* Adaptability and competitiveness in a wide range of tasks (LMSYS Arena ELO: 1225)

#### Cost Analysis
The model's pricing is as follows:
* Input: $3.0 per 

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, offered by Mistral AI, is a premium, non-open-source model released on 2024-07-24. This comparison will focus on its pricing, performance, and capabilities relative to its top competitors, specifically GPT-4o.

#### Pricing Comparison
The pricing for Mistral Large 2 and GPT-4o is as follows:
- **Mistral Large 2**:
  - Input: $3.0 per 1M tokens
  - Output: $9.0 per 1M tokens
- **GPT-4o**:
  - Input: $2.5 per 1M tokens
  - Output: $10.0 per 1M tokens

Mistral Large 2 is more expensive than GPT-4o in terms of input costs but slightly cheaper for output costs.

#### Performance Trade-offs
Mistral Large 2 has the following benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

Without specific benchmark scores for GPT-4o in the provided data, a direct comparison of performance is challenging. However, the choice between Mistral Large 2 and GPT-4o may depend on the specific use case and the importance of performance metrics like those mentioned.

#### Capabilities and Use Cases
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
- Bulk cheap operations
- Real-time operations under 100ms
- Vision-heavy tasks

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100,000 calls: $600.0

These costs are based on the pricing model and do not account for potential discounts or custom pricing

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, a premium model provided by Mistral AI, offers a wide range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. With its high performance benchmarks, such as an MMLU score of 84.0 and a HumanEval score of 92.0, it is best suited for tasks like coding, analysis, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
1. **Coding Assistance**: Mistral Large 2 excels in coding tasks, making it an ideal choice for developers looking for assistance with code completion, debugging, and optimization. Its high HumanEval score indicates its ability to understand and generate human-like code.
2. **Complex Analysis**: With its large context window of 131,072 tokens, Mistral Large 2 can handle complex analysis tasks that require understanding long pieces of text. This makes it suitable for tasks like research paper summarization, technical document analysis, and more.
3. **RAG (Retrieve, Augment, Generate) Tasks**: Mistral Large 2's ability to handle JSON mode and function calling makes it well-suited for RAG tasks, where it can retrieve information from external sources, augment it, and then generate human-like text based on the retrieved information.
4. **Multilingual Support**: As a model that supports multilingual capabilities, Mistral Large 2 can be used for tasks that require understanding and generating text in multiple languages. This makes it a valuable tool for global businesses and organizations.
5. **Agent-Based Systems**: With its ability to handle system prompts and function calling, Mistral Large 2 can be integrated into agent-based systems, where it can interact with users, understand their requests, and perform tasks on their behalf.

### Code Integration Example with OpenRouter
To integrate Mistral Large 2 with OpenRouter, you can use the following code example:


## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
