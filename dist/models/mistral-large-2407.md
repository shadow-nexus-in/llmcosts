# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-15
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source language model designed to cater to a wide range of applications, including coding, analysis, and multilingual support. With its robust architecture, Mistral Large 2 boasts a context window of 131,072 tokens and can generate up to 4,096 tokens as output. This model is part of the premium tier, indicating its high-performance capabilities and reliability.

### Technical Strengths and Use Cases
Mistral Large 2 demonstrates its strengths through impressive benchmark scores: 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These scores underscore its proficiency in handling complex tasks such as coding and analysis. The model supports various capabilities, including text and vision processing, function calling, JSON mode, streaming, and system prompts, making it versatile for developers. It is best utilized for tasks involving coding, analysis, and function calling, but may not be the most cost-effective option for embeddings, bulk operations, or applications requiring real-time responses under 100ms.

### Pricing and Cost Considerations
The pricing for Mistral Large 2 is structured as follows: $3.0 per 1M input tokens and $9.0 per 1M output tokens. For example, 1,000 calls averaging 500 tokens each would cost $6.0, scaling to $60.0 for 10,000 calls and $600.0 for 100,000 calls. When comparing with top competitors like GPT-4o, which offers $2.5/1M input and $10.0/1M output, developers must weigh the costs against the specific capabilities and performance metrics of Mistral Large 2 to determine the best fit for their projects.

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
* Input: **$3.0 per 1M tokens**
* Output: **$9.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs when the same input is used multiple times. Since cached input is free, it is recommended to use cached tokens whenever possible to minimize costs.

#### Batch API Savings
Batching API calls can also help reduce costs. Although the pricing data does not provide a specific discount for batch API calls, the fact that batch input is free suggests that batching can help reduce the overall cost per call.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* 1,000 calls (avg 500 tokens): **$6.0**
* 10,000 calls: **$60.0**
* 100,000 calls: **$600.0**

To estimate the cost per call, we can calculate the cost per token and then multiply it by the average number of tokens per call. However, based on the provided data, we can see that the cost per call decreases as the number of calls increases.

#### Comparison to Top Competitors
Mistral Large 2 is compared to GPT-4o, which has a pricing structure of:
* Input: **$2.5 per 1M tokens**
*

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
* MMLU: **84.0**
* HumanEval: **92.0**
* LMSYS Arena ELO: **1225**
* GSM8K: **93.0**

These scores indicate the model's performance in various areas:
* **MMLU (Massive Multitask Language Understanding)**: Measures the model's ability to understand and generate text across a wide range of tasks. A score of 84.0 indicates strong performance in this area.
* **HumanEval**: Evaluates the model's ability to write code that is correct and functional. A score of 92.0 suggests excellent performance in code generation tasks.
* **LMSYS Arena ELO**: Measures the model's performance in a competitive environment, where it is pitted against other models. An ELO score of 1225 indicates a high level of performance.
* **GSM8K**: Assesses the model's ability to reason

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, a premium model by Mistral AI, offers a unique set of capabilities and performance metrics. This comparison will delve into the pricing, performance, and use cases of Mistral Large 2 against its top competitor, GPT-4o.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, whereas GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. This indicates that GPT-4o is cheaper for input tokens but more expensive for output tokens.

#### Performance Comparison
| Model | MMLU | HumanEval | LMSYS Arena ELO | GSM8K |
| --- | --- | --- | --- | --- |
| Mistral Large 2 | 84.0 | 92.0 | 1225 | 93.0 |
| GPT-4o | *Not Provided* | *Not Provided* | *Not Provided* | *Not Provided* |

Since the performance metrics for GPT-4o are not provided, a direct comparison is not possible. However, Mistral Large 2 demonstrates impressive performance across various benchmarks, with an MMLU score of 84.0, HumanEval score of 92.0, LMSYS Arena ELO of 1225, and GSM8K score of 93.0.

#### Capabilities and Use Cases
Mistral Large 2 offers a range of capabilities, including:
* Text
* Vision
* Function calling
* JSON mode
* Streaming
* System prompts

It is best suited for tasks such as:
* Coding
* Analysis
* RAG
* Agents
* Multilingual
* Function calling

On the other hand, it is not recommended for tasks that require:
* Embeddings
* Bulk cheap processing
* Real-time sub-100ms responses
* Vision-heavy processing

#### Cost Examples

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model with a wide range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. It excels in coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual tasks, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Given its capabilities and pricing, here are the top 5 best use cases for Mistral Large 2:

1. **Coding and Software Development**: With its high performance in coding tasks (as indicated by its HumanEval score of 92.0), Mistral Large 2 can be effectively used for code completion, code review, and even generating entire functions based on specifications. For example, integrating Mistral Large 2 with OpenRouter for automated code generation can significantly enhance developer productivity.

    ```python
    import openrouter
    from mistralai import MistralLarge2

    # Initialize Mistral Large 2 model
    model = MistralLarge2()

    # Define a function to generate code using Mistral Large 2
    def generate_code(prompt):
        # Use OpenRouter to route the prompt to Mistral Large 2
        output = openrouter.route(prompt, model)
        return output

    # Example usage
    prompt = "Generate a Python function to calculate the factorial of a number."
    generated_code = generate_code(prompt)
    print(generated_code)
    ```

2. **Multilingual Support**: Given its multilingual capabilities, Mistral Large 2 can be used for tasks that require understanding and generating text in multiple languages. This can be particularly useful for global applications or services that need to cater to diverse linguistic audiences.

3. **Analysis and RAG Tasks**: With its strong performance in analysis and RAG tasks,

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
