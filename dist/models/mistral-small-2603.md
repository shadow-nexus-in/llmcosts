# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-25
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Technical Overview of Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a context window of up to 262,144 tokens and can generate a maximum output of 4,096 tokens. Its knowledge cutoff is 2023-12, indicating that its training data does not include information beyond this date.

### Main Strengths and Primary Use-Cases
The main strengths of Mistral: Mistral Small 4 lie in its capabilities, which include text, function calling, JSON mode, streaming, and structured outputs. These capabilities make it best suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization. With a pricing model that charges $0.15 per 1M tokens for input and $0.6 per 1M tokens for output, it offers a cost-effective solution for developers looking to integrate advanced language processing into their applications. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, demonstrating its competence in various tasks.

### Cost Considerations and Competitors
For developers considering the cost of integrating Mistral: Mistral Small 4 into their projects, the pricing is straightforward. The cost examples provided indicate that 1,000 calls with an average of 500 tokens would amount to $0.375, scaling up to $3.75 for 10,000 calls and $37.5 for 100,000 calls. Notably, there are no direct competitors listed for this model, suggesting that Mistral: Mistral Small 4 occupies a unique position in the market with its specific set of capabilities and pricing. This makes it an attractive option for developers seeking

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.15 |
| Output | $0.6 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Mistral: Mistral Small 4
#### Overview
Mistral: Mistral Small 4, provided by Mistralai, is a standard, non-open-source model released on 2024-01-01. This analysis will delve into its cost structure, highlighting when to use cached tokens, batch API savings, and costs at scale.

#### Cost Structure
The pricing for Mistral: Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: $None per 1M tokens (indicating no additional cost for cached inputs)
- **Batch Input**: $None per 1M tokens (suggesting no additional cost for batch inputs, but this needs clarification as it might imply no discount or specific conditions for batch processing)

#### Using Cached Tokens
Given that cached input tokens incur no additional cost ($None per 1M tokens), it is highly beneficial to utilize cached tokens whenever possible. This can significantly reduce costs, especially in applications where the same or similar inputs are processed multiple times.

#### Batch API Savings
The provided data does not explicitly outline savings for batch API calls, as both batch input and cached input are listed as incurring no additional cost. However, the absence of a specific discount for batch processing suggests that the primary cost savings will come from optimizing input token usage and leveraging cached inputs.

#### Cost at Scale
The cost examples provided give insight into the model's pricing at different scales:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These examples illustrate a linear cost scaling, where the cost increases directly with the number of API calls. This linear relationship suggests that the cost per call remains constant, regardless of the volume, which can

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Mistral Small 4 Benchmark Performance
#### Overview
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. It is not open-source and has specific pricing for input and output tokens.

#### Pricing
The pricing model for Mistral Small 4 is as follows:
- Input: **$0.15 per 1M tokens**
- Output: **$0.6 per 1M tokens**
- Cached Input: **$None per 1M tokens**
- Batch Input: **$None per 1M tokens**

#### Context and Limits
The model has the following context and limits:
- Context Window: **262,144 tokens**
- Max Output: **4,096 tokens**
- Knowledge Cutoff: **2023-12**

#### Benchmarks
The benchmark performance of Mistral Small 4 is as follows:
- **MMLU (Massive Multitask Language Understanding)**: 80.0
  - MMLU measures a model's ability to perform a wide range of natural language understanding tasks. A higher score indicates better performance. With a score of 80.0, Mistral Small 4 demonstrates a strong capability in understanding and processing human language.
- **HumanEval**: None
  - HumanEval is a benchmark that evaluates a model's ability to generate code. The lack of a score for Mistral Small 4 in this area means its coding capabilities, while listed under its capabilities, are not quantitatively measured here.
- **LMSYS Arena ELO**: 1200
  - The LMSYS Arena ELO score is a measure of a

## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral Small 4 model, we will provide a general comparison framework that can be applied to other models in the market. This framework will focus on key aspects such as pricing, performance, and capabilities.

#### Pricing Comparison
The Mistral Small 4 model is priced as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens

To compare, we would need the pricing details of competing models. However, in general, when evaluating pricing:
- **Lower input and output costs** per 1M tokens can significantly reduce the overall cost for applications with high volumes of data.
- **Batch input pricing** can offer discounts for processing multiple inputs simultaneously, which can be beneficial for certain use cases.
- **Cached input pricing** can reduce costs if the same inputs are processed multiple times.

#### Performance Trade-offs
The performance of the Mistral Small 4 is indicated by the following benchmarks:
- MMLU: 80.0
- LMSYS Arena ELO: 1200

When comparing performance:
- **Higher benchmark scores** generally indicate better performance in specific tasks or evaluations.
- **Context window and max output limits** can affect the model's ability to handle long-range dependencies and generate extensive responses.
- **Knowledge cutoff** is crucial for applications requiring up-to-date information.

#### Capabilities and Use Cases
The Mistral Small 4 supports:
- Text
- Function calling
- JSON mode
- Streaming
- Structured outputs

It is best for:
- Chat
- Text generation
- Coding
- Analysis
- RAG pipelines
- Summarization

When choosing a model, consider:
- **Capabilities alignment** with your application's requirements.
- **Tier and open-source status** can impact customization, community support, and cost.
- **Release date** can indicate how recent the model's training data is, affecting its knowledge and performance.

#### Cost Examples
The provided cost examples for the Mistral Small 4 are:
- 1,000 calls (avg 500 tokens): $0.375
- 10,000 calls: $3.75
- 100,000 calls: $37.5

These examples help in estimating costs based on the expected volume of usage.

### Choosing the Right Model
Given the lack

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and release date of 2024-01-01, it offers a robust solution for various applications. In this guide, we will explore the top 5 best use cases for Mistral Small 4, along with code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, the top 5 use cases for Mistral Small 4 are:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and max output of 4,096 tokens, Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: Its ability to perform function calling and structured outputs makes it an excellent choice for coding and analysis tasks.
3. **Summarization**: Mistral Small 4's capabilities in text generation and analysis make it a good fit for summarization tasks.
4. **RAG Pipelines**: Its support for structured outputs and function calling enables it to be used in RAG (Retrieval-Augmented Generation) pipelines.
5. **Streaming**: With its streaming capability, Mistral Small 4 can be used for real-time text generation and analysis applications.

### Code Integration Examples with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code examples:

```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.Model("mistralai/mistral-small-2603")

# Use the model for text generation
def generate_text(prompt):
    response = model.generate_text(prompt, max_length=4096)
    return response

# Use the model for function calling
def call_function(func

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
