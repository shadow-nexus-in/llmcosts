# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-15
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of tasks, including but not limited to text generation, function calling, and structured output generation. Its capabilities encompass text, function_calling, json_mode, streaming, and structured_outputs, making it a versatile tool for developers.

### Strengths and Use Cases
The main strengths of Mistral Small 4 lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens. This capability, combined with its support for streaming and structured outputs, makes it particularly suited for applications such as chat, text generation, coding, analysis, and summarization. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its proficiency in handling complex linguistic tasks. Developers can leverage Mistral Small 4 for rag_pipelines, further enhancing its utility in comprehensive data analysis and processing pipelines.

### Pricing and Cost Considerations
The pricing model for Mistral Small 4 is based on input and output tokens, with costs set at $0.15 per 1M input tokens and $0.6 per 1M output tokens. There are no specified costs for cached input or batch input. For example, 1,000 calls with an average of 500 tokens per call would cost $0.375, scaling up to $3.75 for 10,000 calls and $37.5 for 100,000 calls. Given its capabilities and pricing structure, Mistral Small 4 is positioned as a competitive option for developers seeking a robust language model for a variety of applications, although it currently has no direct competitors listed

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
Mistral: Mistral Small 4, provided by Mistralai, is a standard, non-open-source model released on 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and scaling costs for this model.

#### Cost Structure
The pricing for Mistral: Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: No charge ($None per 1M tokens)
- **Batch Input**: No charge ($None per 1M tokens)

This structure indicates that the primary cost drivers are the input and output token counts. Cached and batch inputs are not charged, suggesting that optimizing for these can significantly reduce costs.

#### When to Use Cached Tokens
Given that cached input tokens incur no charge, it is highly beneficial to utilize cached tokens whenever possible. This can be particularly effective in scenarios where the same or similar inputs are processed multiple times, such as in chat applications or text generation tasks where user queries may overlap or have similar contexts.

#### Batch API Savings
The absence of a charge for batch inputs implies that processing inputs in batches can lead to cost savings, primarily by reducing the overhead associated with individual API calls. This strategy can be especially useful for applications that can accumulate inputs over time before processing them in bulk.

#### Cost at Scale
To understand the cost implications of using Mistral: Mistral Small 4 at scale, let's examine the provided cost examples:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These examples illustrate a linear scaling of costs with the number of API calls, indicating that the cost per call remains constant regardless of the

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Analysis
#### Overview
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. It is not open source.

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
The benchmark performance of Mistral Small 4 is:
* MMLU: **80.0**
* HumanEval: **None**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

The MMLU score of 80.0 indicates the model's performance on a set of math and logic problems. A higher score generally indicates better performance. The LMSYS Arena ELO score of 1200 is a measure of the model's overall language understanding and generation capabilities, with higher scores indicating better performance.

The lack of HumanEval and GSM8K scores means that the model's performance on these specific benchmarks is unknown.

#### Capabilities and Use Cases
Mistral Small 4 supports the following capabilities:
* text
* function_calling
* json_mode
* streaming
* structured_outputs

It is best suited for:
* chat
* text

## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral Small 4 model, we will provide a general comparison framework that can be applied when evaluating this model against other similar models in the market.

#### Pricing Comparison
The Mistral Small 4 model is priced as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens

To compare, we would need the pricing information of the competitor models. However, we can establish a baseline for evaluation:
- **Input Cost**: Competitor models with lower input costs per 1M tokens may offer better value for applications with large input sizes.
- **Output Cost**: Models with lower output costs per 1M tokens may be more suitable for applications requiring extensive text generation.

#### Performance Trade-offs
The Mistral Small 4 model has the following performance characteristics:
- **MMLU**: 80.0
- **LMSYS Arena ELO**: 1200
- **Context Window**: 262,144 tokens
- **Max Output**: 4,096 tokens

When comparing with competitor models, consider the following trade-offs:
- **Performance vs. Cost**: Models with higher performance metrics (e.g., MMLU, LMSYS Arena ELO) may justify higher costs for applications requiring superior performance.
- **Context Window and Max Output**: Models with larger context windows and higher max output limits may be more suitable for applications requiring longer input and output sequences.

#### Choosing the Right Model
To choose between the Mistral Small 4 model and its competitors, consider the following factors:
- **Application Requirements**: Align the model's capabilities (e.g., text, function_calling, json_mode, streaming, structured_outputs) with the specific needs of your application.
- **Budget Constraints**: Evaluate the cost examples provided (e.g., $0.375 for 1,000 calls, $3.75 for 10,000 calls) against your budget and expected usage.
- **Performance Needs**: Assess whether the model's performance characteristics meet the requirements of your application.

### Example Use Cases
The Mistral Small 4 model is best suited for applications such as:
- Chat
- Text generation
- Coding
- Analysis
- RAG pipelines
- Summarization

When evaluating competitor models, consider whether they offer similar capabilities and performance characteristics that align with your

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on 2024-01-01, this model is part of the standard tier and is not open source.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities, the top 5 best use cases for Mistral Small 4 are:

1. **Chat and Text Generation**: With its ability to generate high-quality text, Mistral Small 4 is well-suited for chat applications, content generation, and text summarization.
2. **Coding and Analysis**: The model's function calling and structured output capabilities make it an excellent choice for coding tasks, such as code completion, code review, and data analysis.
3. **RAG Pipelines**: Mistral Small 4's ability to handle complex queries and generate structured outputs makes it a good fit for RAG (Retrieve, Augment, Generate) pipelines.
4. **Summarization**: The model's text generation capabilities can be leveraged for summarizing long documents, articles, or research papers.
5. **Streaming and Real-time Applications**: With its support for streaming, Mistral Small 4 can be used in real-time applications, such as live chat, sentiment analysis, or event detection.

### Code Integration Example with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following example code:
```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.Model("mistralai/mistral-small-2603")

# Define a function to generate text
def generate_text(prompt):
    # Use the model to generate text
    output = model.generate_text(prompt, max_length=4096)
    return output

# Test the function
prompt = "Write a short

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
