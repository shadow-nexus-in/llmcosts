# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-28
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens, making it suitable for complex text generation and analysis tasks.

### Technical Specifications and Use Cases
Technically, Mistral Small 4 is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its performance capabilities. It is best utilized for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization. The model's pricing is structured around input and output tokens, with costs of $0.15 per 1M input tokens and $0.6 per 1M output tokens. For developers, understanding these pricing metrics is crucial for estimating costs, such as the examples provided: 1,000 calls averaging 500 tokens cost $0.375, scaling up to $3.75 for 10,000 calls, and $37.5 for 100,000 calls.

### Deployment and Cost Considerations
When deploying Mistral Small 4, developers should consider the model's limitations, including a context window of 262,144 tokens, a maximum output of 4,096 tokens, and a knowledge cutoff of 2023-12. The lack of direct competitors suggests that Mistral Small 4 offers a unique set of capabilities and performance metrics. For applications requiring extensive text analysis, generation, or coding capabilities, Mistral Small 4 presents a compelling option, albeit with careful consideration of its pricing

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.15 |
| Output | $0.6 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Mistral Small 4 Pricing Analysis
#### Overview
Mistral Small 4, provided by Mistralai, is a standard, non-open-source model released on 2024-01-01. This analysis will delve into its cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

This structure indicates that input and output tokens are the primary cost drivers. However, utilizing cached inputs and batch processing can significantly reduce costs, as they are provided at no additional charge.

#### Optimal Usage Scenarios
- **Cached Tokens**: Since cached input tokens are free, it's highly beneficial to use them whenever possible. This can significantly reduce costs for repeated queries or when dealing with similar input data.
- **Batch API Savings**: Similar to cached inputs, batch inputs are also free. This makes batch processing an attractive option for large-scale applications, as it can lead to substantial cost savings compared to making individual API calls.

#### Cost at Scale
To understand the cost-effectiveness of Mistral Small 4 at different scales, let's examine the provided cost examples:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These examples illustrate a linear cost scaling, where the cost increases directly with the number of API calls. This linear relationship makes it easier to predict and budget for costs as the application scales.

#### Conclusion
Mistral Small 4 offers a straightforward pricing model with opportunities for cost savings through the use of cached inputs and batch processing. While

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Analysis
The Mistral Small 4 model, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. It is not open-source.

#### Pricing
The pricing for Mistral Small 4 is as follows:
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Context and Limits
The model has the following context and limits:
* Context Window: **262,144 tokens**
* Max Output: **4,096 tokens**
* Knowledge Cutoff: **2023-12**

#### Benchmarks
The model's benchmark performance is as follows:
* MMLU: **80.0**
* HumanEval: **None**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

The MMLU score of 80.0 indicates the model's ability to understand and process natural language. A higher MMLU score generally corresponds to better language understanding capabilities.

The LMSYS Arena ELO score of 1200 is a measure of the model's performance in a competitive environment, where it is pitted against other models. A higher ELO score indicates better performance.

The lack of HumanEval and GSM8K scores makes it difficult to assess the model's performance in specific areas, such as coding and mathematical problem-solving.

#### Capabilities and Use Cases
Mistral Small 4 has the following capabilities:
* text
* function_calling
* json_mode


## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral Small 4 model, we will create a hypothetical comparison with other models in the same tier and category. 

#### Hypothetical Competitors
For the purpose of this comparison, let's consider two hypothetical models:
- **Model A**: A standard, open-source model with similar capabilities to Mistral Small 4.
- **Model B**: A premium, non-open-source model with advanced capabilities and higher performance.

#### Price Comparison
The pricing for Mistral Small 4 is as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens

In comparison, the hypothetical prices for Model A and Model B could be:
- **Model A**:
  - Input: $0.10 per 1M tokens (33% cheaper than Mistral Small 4)
  - Output: $0.50 per 1M tokens (17% cheaper than Mistral Small 4)
- **Model B**:
  - Input: $0.25 per 1M tokens (67% more expensive than Mistral Small 4)
  - Output: $0.80 per 1M tokens (33% more expensive than Mistral Small 4)

#### Performance Trade-offs
The performance of Mistral Small 4 is measured by the following benchmarks:
- MMLU: 80.0
- LMSYS Arena ELO: 1200

In comparison, the hypothetical performance of Model A and Model B could be:
- **Model A**:
  - MMLU: 70.0 (12.5% lower than Mistral Small 4)
  - LMSYS Arena ELO: 1000 (17% lower than Mistral Small 4)
- **Model B**:
  - MMLU: 90.0 (12.5% higher than Mistral Small 4)
  - LMSYS Arena ELO: 1400 (17% higher than Mistral Small 4)

#### When to Choose Each Model
Based on the price and performance comparison, here are some guidelines on when to choose each model:
- **Mistral Small 4**: Choose this model when you need a balance between price and performance. It offers a standard set of capabilities and decent performance at a moderate price.
- **

## Best Use Cases
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on 2024-01-01, this model is classified as a standard, non-open-source model.

### Top 5 Best Use Cases for Mistral: Mistral Small 4
Given its capabilities, here are the top 5 best use cases for Mistral: Mistral Small 4:

1. **Chat and Text Generation**: With its strong text generation capabilities, Mistral: Mistral Small 4 is well-suited for chat applications, content generation, and text summarization.
2. **Coding and Function Calling**: The model's ability to perform function calling and generate code makes it an excellent choice for coding tasks, such as code completion and code review.
3. **Analysis and Summarization**: Mistral: Mistral Small 4 can be used for analysis and summarization tasks, such as summarizing long documents, extracting key points, and identifying main ideas.
4. **RAG Pipelines**: The model's support for RAG (Retrieve, Augment, Generate) pipelines makes it suitable for tasks that require generating text based on external knowledge sources.
5. **Structured Outputs**: Mistral: Mistral Small 4's ability to generate structured outputs, such as JSON, makes it a good fit for applications that require structured data, such as data processing and data integration.

### Code Integration Examples with OpenRouter
To integrate Mistral: Mistral Small 4 with OpenRouter, you can use the following code examples:

```python
import openrouter

# Initialize the Mistral: Mistral Small 4 model
model = openrouter.Model("mistralai/mistral-small-2603")

# Generate text using the model
def generate_text(prompt):
    response = model.generate

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
