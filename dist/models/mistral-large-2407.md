# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-25
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly in coding, analysis, and function calling. This model boasts an impressive architecture that supports capabilities such as text and vision processing, function calling, JSON mode, streaming, and system prompts. With a context window of 131,072 tokens and a maximum output of 4,096 tokens, Mistral Large 2 is well-suited for complex tasks that require extensive contextual understanding.

### Technical Strengths and Use Cases
The technical strengths of Mistral Large 2 are underscored by its benchmark scores: MMLU at 84.0, HumanEval at 92.0, LMSYS Arena ELO at 1225, and GSM8K at 93.0. These scores indicate the model's proficiency in handling multifaceted tasks, including coding challenges and analytical queries. The model's primary use cases include coding assistance, in-depth analysis, and applications that leverage its function calling and multilingual capabilities. However, it's essential to note that Mistral Large 2 is not optimized for tasks requiring embeddings, bulk processing at low costs, real-time responses under 100ms, or vision-heavy applications.

### Pricing and Cost Considerations
Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, with no specific pricing for cached input or batch input. For developers, estimating costs is straightforward: for example, 1,000 calls averaging 500 tokens each would cost $6.0, scaling to $60.0 for 10,000 calls and $600.0 for 100,000 calls. In comparison to its top competitor, GPT-4o, which is priced at $2.5/1M

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
Mistral Large 2, provided by Mistral AI, is a premium model released on 2024-07-24. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale for this model.

#### Cost Structure
The pricing for Mistral Large 2 is as follows:
* Input: **$3.0 per 1M tokens**
* Output: **$9.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### Optimal Usage Scenarios
* **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
* **Batch API Savings**: With batch input being free, batching API calls can significantly reduce costs. However, the actual cost savings will depend on the output token count, which is charged at **$9.0 per 1M tokens**.

#### Cost at Scale
The cost of using Mistral Large 2 at different scales is as follows:
* **1,000 API calls** (avg 500 tokens): **$6.0**
* **10,000 API calls**: **$60.0**
* **100,000 API calls**: **$600.0**

To estimate the cost at scale, we can use the average cost per call. However, the actual cost will depend on the input and output token counts.

#### Competitor Comparison
Mistral Large 2's pricing is comparable to its top competitor, GPT-4o, which charges **$2.5/1M input** and **$10.0/1M output**. While GPT-4o has a lower input cost, Mistral Large 2's free cached input and batch input can provide significant cost savings

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 84.0 |
| HumanEval | 92.0 |
| LMSYS Arena ELO | 1225 |
| ARC | 93.0 |

## Benchmark Analysis
### Mistral Large 2 Performance Analysis
#### Model Overview
The Mistral Large 2 model, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. It offers a range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, making it suitable for tasks such as coding, analysis, and multilingual applications.

#### Pricing Structure
The pricing for Mistral Large 2 is as follows:
- Input: $3.0 per 1M tokens
- Output: $9.0 per 1M tokens
- Cached Input: $None per 1M tokens
- Batch Input: $None per 1M tokens

#### Benchmark Performance
The model's performance is evaluated through several benchmarks:
- **MMLU (Massive Multitask Language Understanding)**: A score of 84.0 indicates the model's ability to understand and process a wide range of language tasks. A higher MMLU score suggests better performance in tasks that require a broad understanding of language.
- **HumanEval**: With a score of 92.0, Mistral Large 2 demonstrates strong performance in evaluating and executing human-written code, indicating its potential for coding and programming tasks.
- **LMSYS Arena ELO**: An ELO score of 1225 reflects the model's competitive performance in a variety of tasks and its ability to adapt to different scenarios, similar to how chess players are ranked.
- **GSM8K**: A score of 93.0 on the GSM8K benchmark, which focuses on math problem-solving, further highlights the model's capabilities in logical reasoning and mathematical tasks.

#### Real-

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. This comparison will focus on its pricing, performance, and capabilities relative to its top competitor, GPT-4o.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, whereas GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. For input-intensive tasks, GPT-4o is cheaper by $0.5 per 1M tokens. However, for output-intensive tasks, Mistral Large 2 is cheaper by $1.0 per 1M tokens.

#### Performance Comparison
Mistral Large 2 has the following benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

GPT-4o's benchmark scores are not provided in the data. Therefore, a direct performance comparison cannot be made. However, based on the provided scores, Mistral Large 2 demonstrates strong capabilities in coding, analysis, and multilingual tasks.

#### Capabilities and Limitations
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

However, it is not recommended for tasks that require:
- Embeddings
- Bulk cheap processing
- Real-time sub-100ms responses
- Vision-heavy tasks

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model that offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. With its high performance benchmarks (MMLU: 84.0, HumanEval: 92.0, LMSYS Arena ELO: 1225, GSM8K: 93.0), it is best suited for tasks such as coding, analysis, RAG, agents, multilingual support, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
1. **Coding and Software Development**: Given its high HumanEval score (92.0), Mistral Large 2 is particularly adept at coding tasks. It can be integrated into development environments to assist with code completion, debugging, and optimization.
2. **Complex Text Analysis**: With a context window of 131,072 tokens, Mistral Large 2 can handle extensive text analysis tasks, including document summarization, sentiment analysis, and information extraction.
3. **Multilingual Support**: Its capability for multilingual support makes it an ideal choice for applications that require text processing and understanding across different languages.
4. **Agent-Based Systems**: Mistral Large 2's support for agents and its function calling capability allow it to be used in the development of sophisticated agent-based systems that can interact with users and other systems effectively.
5. **RAG (Retrieve, Augment, Generate) Tasks**: The model's high performance in benchmarks suggests it can efficiently handle RAG tasks, which involve retrieving information, augmenting it, and generating new content based on the input.

### Code Integration Example with OpenRouter
To integrate Mistral Large 2 with OpenRouter for coding tasks, you might use the following Python example:
```python
import openrouter
from mistralai import Mist

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
