# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-07
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open-source. The architecture of Mistral Small 4 is designed to handle a variety of tasks, including text generation, coding, and analysis, with capabilities such as text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens.

### Technical Specifications and Pricing
Technically, Mistral Small 4 is priced based on input and output tokens. The pricing model is as follows: $0.15 per 1M input tokens and $0.6 per 1M output tokens. There are no specified costs for cached input or batch input. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. The knowledge cutoff for this model is 2023-12, indicating that its training data is current up to December 2023. The capabilities of Mistral Small 4 make it best suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization.

### Use Cases and Cost Considerations
Given its capabilities and pricing structure, Mistral Small 4 is a viable option for developers looking to integrate advanced language processing into their applications without incurring excessive costs. For example, 1,000 calls with an average of 500 tokens per call would cost $0.375, while 10,000 calls would amount to $3.75, and 100,000 calls would be $37.5. With no direct competitors listed, Mistral Small 4 stands out as a unique offering in the market. However, its suitability for specific tasks would depend on the

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
Mistral Small 4, provided by Mistralai, is a standard tier model with a release date of 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$0.00 per 1M tokens** (free)
* Batch Input: **$0.00 per 1M tokens** (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following strategies:
* **Cached Tokens**: Utilize cached input tokens whenever possible, as they are **free**. This is ideal for applications with repetitive or similar input patterns.
* **Batch API**: Leverage batch input for multiple requests, as it is also **free**. This approach can significantly reduce costs for high-volume API calls.

#### Cost at Scale
The cost examples provided are:
* **1,000 calls (avg 500 tokens)**: **$0.375**
* **10,000 calls**: **$3.75**
* **100,000 calls**: **$37.5**

To estimate costs at scale, we can extrapolate from the provided examples. Assuming an average of 500 tokens per call, the cost per call is **$0.000375** (0.15/1M \* 500/1M + 0.6/1M \* 500/1M).

#### Cost Calculation
For a large number of API calls, the cost can be calculated as follows:
* **1,000 calls**: 1,000 \* 500 tokens/call \* ($0.15/1M + $0.6/

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
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. It is not open source. The model's pricing is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Benchmark Performance
The model's benchmark performance is measured by the following scores:
* **MMLU (Massive Multitask Language Understanding)**: 80.0 - This score indicates the model's ability to understand and perform a wide range of natural language processing tasks. A higher score generally indicates better performance.
* **HumanEval**: None - This score is not available for Mistral Small 4. HumanEval is a benchmark that evaluates a model's ability to generate code that is correct and functional.
* **LMSYS Arena ELO**: 1200 - This score is a measure of the model's performance in a competitive arena, where it is pitted against other models. An ELO score of 1200 is a relatively modest score, indicating that the model may not be as competitive as others in certain tasks.
* **GSM8K**: None - This score is not available for Mistral Small 4. GSM8K is a benchmark that evaluates a model's ability to reason and solve math problems.

#### Real-World Implications
The benchmark scores for Mistral Small 4 have the following implications for real-world use:
* The MMLU score of

## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral Small 4 model, we will provide a general comparison framework that can be applied to other models in the market. This framework will focus on key aspects such as pricing, performance, and capabilities.

#### Pricing Comparison
The Mistral Small 4 model is priced as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens

To compare, we would need the pricing information of competitor models. However, we can establish a general guideline for comparison:
- **Lower Input Price**: Models with lower input prices per 1M tokens may be more cost-effective for applications with large input sizes.
- **Lower Output Price**: Models with lower output prices per 1M tokens may be more suitable for applications requiring extensive output generation.

#### Performance Trade-offs
Mistral Small 4 has the following performance metrics:
- MMLU: 80.0
- LMSYS Arena ELO: 1200
- Context Window: 262,144 tokens
- Max Output: 4,096 tokens

When comparing with other models, consider the following:
- **Higher MMLU Score**: Indicates better performance on a wide range of natural language understanding tasks.
- **Higher LMSYS Arena ELO**: Suggests superior performance in competitive benchmarking scenarios.
- **Larger Context Window**: Beneficial for tasks requiring longer input sequences.
- **Larger Max Output**: Suitable for applications needing more extensive output generation.

#### Capabilities and Best Use Cases
Mistral Small 4 supports:
- Text
- Function calling
- JSON mode
- Streaming
- Structured outputs

It is best suited for:
- Chat
- Text generation
- Coding
- Analysis
- RAG pipelines
- Summarization

When choosing between models, consider the specific capabilities and use cases your application requires.

#### Cost Examples
The cost of using Mistral Small 4 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $0.375
- 10,000 calls: $3.75
- 100,000 calls: $37.5

Compare these estimates with the costs of competitor models to determine the most cost-effective option for your specific use case.

### Conclusion
While direct competitors for the Mistral Small

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a robust language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on 2024-01-01, this model is part of the standard tier and is not open source.

### Top 5 Best Use Cases for Mistral Small 4
Given its capabilities, Mistral Small 4 is best suited for the following applications:

1. **Chat and Text Generation**: With its ability to handle large context windows (up to 262,144 tokens) and generate up to 4,096 output tokens, Mistral Small 4 is ideal for chatbots and text generation tasks.
2. **Coding and Analysis**: The model's function calling and structured outputs capabilities make it suitable for coding tasks, such as code completion and code analysis.
3. **Summarization**: Mistral Small 4's ability to process large amounts of text and generate concise summaries makes it a good fit for text summarization tasks.
4. **RAG Pipelines**: The model's support for retrieval-augmented generation (RAG) pipelines enables it to be used in applications that require generating text based on external knowledge sources.
5. **Streaming**: With its streaming capability, Mistral Small 4 can be used in real-time applications, such as live chat or text-based interfaces.

### Code Integration Example with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.Model("mistralai/mistral-small-2603")

# Define a function to generate text using the model
def generate_text(prompt):
    inputs = openrouter.Input(prompt)
    outputs = model.generate(inputs, max_length=4096)
    return outputs.text

# Test the function
prompt = "

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
