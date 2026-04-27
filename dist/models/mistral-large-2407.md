# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-27
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly in coding, analysis, and function calling. This model boasts an impressive architecture with a context window of 131,072 tokens and a maximum output of 4,096 tokens. Its knowledge cutoff is 2024-07, ensuring it is well-versed in information up to that point. With capabilities including text, vision, function calling, JSON mode, streaming, and system prompts, Mistral Large 2 is a versatile tool for developers.

### Technical Strengths and Use Cases
Mistral Large 2 demonstrates its technical prowess through its benchmark scores: 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These scores highlight the model's strengths in understanding and generating human-like text, making it suitable for tasks such as coding, analysis, and multilingual applications. Its ability to handle function calling and JSON mode also makes it an excellent choice for complex, data-driven tasks. However, it's worth noting that Mistral Large 2 is not recommended for embeddings, bulk cheap processing, real-time sub-100ms applications, or vision-heavy tasks.

### Pricing and Cost Considerations
The pricing for Mistral Large 2 is structured as follows: $3.0 per 1M tokens for input and $9.0 per 1M tokens for output. There are no specified costs for cached input or batch input. To give developers a better understanding of the costs involved, examples are provided: 1,000 calls averaging 500 tokens cost $6.0, scaling up to $60.0 for 10,000 calls and $600.0 for 100,000 calls. In

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
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. The pricing structure is based on input and output tokens, with specific considerations for cached and batch inputs.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
- **Input**: $3.0 per 1M tokens
- **Output**: $9.0 per 1M tokens
- **Cached Input**: $0 per 1M tokens (free)
- **Batch Input**: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option when the same input is used multiple times. This can significantly reduce costs in applications where inputs are repetitive or where the same prompt is used to generate multiple outputs.

#### Batch API Savings
Batch inputs are also free, which means processing multiple inputs at once does not incur additional costs beyond the standard input and output pricing. This can lead to significant savings when making a large number of API calls, as the cost per call decreases with the number of calls made in a batch.

#### Cost at Scale
The cost of using Mistral Large 2 at scale can be broken down as follows:
- **1,000 calls (avg 500 tokens)**: $6.0
- **10,000 calls**: $60.0
- **100,000 calls**: $600.0

These costs indicate a linear scaling of expenses with the number of API calls, suggesting that the pricing model does not offer discounts for larger volumes beyond the savings from batch processing and cached inputs.

#### Comparison with Competitors
Mistral Large 2's pricing can be compared with its top competitors, such as GPT-4o, which

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
* **HumanEval**: 92.0, measuring the model's ability to evaluate and execute human-written code, with higher scores indicating better performance.
* **LMSYS Arena ELO**: 1225, representing the model's competitive ranking in the LMSYS Arena, a benchmarking platform for large language models.
* **GSM8K**: 93.0, assessing the model's math problem-solving abilities, with higher scores indicating better performance.

#### Real-World Implications
These benchmark scores have significant implications for real-world use cases:
* **MMLU**: A score of 84.0 suggests that Mistral Large 2 can handle complex, open-ended tasks that require a deep understanding of language and context.
* **HumanEval**: With a score of 92.0, the model is well-suited for coding and programming tasks, such as code completion, code review, and code generation.
* **LMSYS Arena ELO**: An ELO score of 1225 indicates that Mistral Large 2 is a highly competitive model, capable of performing well in

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. This comparison will focus on its pricing, performance, and capabilities in relation to its top competitor, GPT-4o.

#### Pricing Comparison
The pricing for Mistral Large 2 and GPT-4o is as follows:
* Mistral Large 2:
	+ Input: $3.0 per 1M tokens
	+ Output: $9.0 per 1M tokens
* GPT-4o:
	+ Input: $2.5 per 1M tokens
	+ Output: $10.0 per 1M tokens

Mistral Large 2 is more expensive than GPT-4o in terms of input tokens, with a 20% higher cost ($3.0 vs $2.5 per 1M tokens). However, the output token cost is only 10% lower for GPT-4o ($10.0 vs $9.0 per 1M tokens).

#### Performance Trade-offs
The performance of Mistral Large 2 is measured through various benchmarks:
* MMLU: 84.0
* HumanEval: 92.0
* LMSYS Arena ELO: 1225
* GSM8K: 93.0

While the specific performance metrics for GPT-4o are not provided, the choice between Mistral Large 2 and GPT-4o will depend on the specific use case and the importance of these benchmark scores.

#### Capabilities and Use Cases
Mistral Large 2 supports the following capabilities:
* Text
* Vision
* Function calling
* JSON mode
* Streaming
* System prompts

It is best suited for tasks such as:
* Coding
* Analysis
* RAG (Retrieval-Augmented Generation)
* Agents
* Multilingual tasks
* Function calling

However, it is not recommended for:
* Embeddings
* Bulk cheap tasks
* Real-time tasks with latency under 100ms
* Vision-heavy tasks

#### Cost Examples
The estimated costs for using Mistral Large 2 are:
* 1,000 calls (avg 500 tokens): $6.0
* 10,000 calls: $60.0
*

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model that excels in various tasks, including coding, analysis, and function calling. With its impressive benchmarks, such as an MMLU score of 84.0 and a HumanEval score of 92.0, this model is a top choice for many applications. However, its pricing and limitations must be considered when deciding on its use.

### Pricing and Cost Examples
The pricing for Mistral Large 2 is as follows:
- Input: $3.0 per 1M tokens
- Output: $9.0 per 1M tokens
- Cached Input: $None per 1M tokens
- Batch Input: $None per 1M tokens

Some cost examples to consider:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100,000 calls: $600.0

### Top 5 Best Use Cases for Mistral Large 2
Given its capabilities and pricing, here are the top 5 best use cases for Mistral Large 2:

1. **Coding Assistance**: With its high HumanEval score, Mistral Large 2 is well-suited for coding tasks, such as code completion and code review. It can be integrated with OpenRouter to provide real-time coding assistance.
    ```python
import openrouter
from mistralai import MistralLarge2

# Initialize the model and OpenRouter
model = MistralLarge2()
router = openrouter.OpenRouter()

# Define a function to get coding assistance
def get_coding_assistance(prompt):
    # Use the model to generate code
    code = model.generate_code(prompt)
    # Use OpenRouter to route the code to the correct destination
    router.route_code(code)



## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
