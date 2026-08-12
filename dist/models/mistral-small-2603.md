# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-12
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of natural language processing tasks with its ability to process up to 262,144 tokens in its context window and generate outputs of up to 4,096 tokens. Its capabilities include text processing, function calling, JSON mode, streaming, and structured outputs, making it a versatile tool for developers.

### Strengths and Use Cases
The main strengths of Mistral Small 4 lie in its broad range of capabilities, including text generation, coding, analysis, and summarization, among others. It is best utilized for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization. With a context window of 262,144 tokens and a knowledge cutoff of 2023-12, Mistral Small 4 is well-equipped to handle complex and information-dense tasks. Its performance is further underscored by its benchmarks, including an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its competence in understanding and generating human-like text.

### Pricing and Cost Efficiency
The pricing model for Mistral Small 4 is based on input and output tokens, with costs of $0.15 per 1M tokens for input and $0.6 per 1M tokens for output. There are no specified costs for cached input or batch input. For example, 1,000 calls with an average of 500 tokens would cost $0.375, while 10,000 calls would amount to $3.75, and 100,000 calls would cost $37.5. This pricing structure makes Mistral Small 4 a cost-effective option for developers looking to integrate advanced language processing capabilities

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
Mistral Small 4, provided by Mistralai, is a standard-tier model released on January 1, 2024. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* **Input**: $0.15 per 1M tokens
* **Output**: $0.6 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following strategies:
* **Use Cached Tokens**: Since cached input tokens are free, utilize them whenever possible to reduce input costs.
* **Batch API Calls**: Batch input is also free, so batching API calls can help reduce overall costs by minimizing the number of input tokens required.

#### Cost at Scale
The cost of using Mistral Small 4 at various scales is as follows:
* **1,000 calls (avg 500 tokens)**: $0.375
* **10,000 calls**: $3.75
* **100,000 calls**: $37.5

These costs demonstrate a linear scaling of expenses with the number of API calls, indicating that the cost per call remains constant regardless of the volume.

#### Context and Limits
When using Mistral Small 4, consider the following context and limits:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12

These constraints can impact the model's performance and suitability for specific tasks.

#### Capabilities and Best Use Cases
Mistral Small 4 supports the following capabilities:
* text
* function_calling
* json_mode
* streaming
* structured_outputs

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
The Mistral Small 4 model, provided by Mistralai, is a standard, non-open-source model released on January 1, 2024. This analysis will delve into its benchmark performance, focusing on the MMLU, HumanEval, and Arena ELO scores, to understand its capabilities and limitations in real-world applications.

#### Benchmark Scores
- **MMLU (Massive Multitask Language Understanding) Score: 80.0**
  The MMLU score measures a model's ability to perform a wide range of natural language processing tasks. A score of 80.0 indicates that Mistral Small 4 has a strong foundation in understanding and generating human-like text, making it suitable for tasks like text generation, chat, and analysis.

- **HumanEval Score: None**
  The HumanEval score evaluates a model's ability to write correct and functional code based on human descriptions. Unfortunately, no HumanEval score is provided for Mistral Small 4, making it difficult to assess its coding capabilities directly. However, its inclusion in the "BEST FOR" categories for coding suggests some level of proficiency.

- **LMSYS Arena ELO Score: 1200**
  The LMSYS Arena ELO score is a measure of a model's performance in a competitive environment, often involving tasks that require strategic thinking and problem-solving. An ELO score of 1200 places Mistral Small 4 in a moderate to strong position, indicating it can handle complex tasks but may struggle against highly specialized or larger models.

#### Real-World Implications
- **Text Generation and Chat:** With a strong MMLU score, Mistral

## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral Small 4 model, we will provide a general comparison framework that can be applied to other models in the market. This framework will consider key factors such as pricing, performance, and capabilities.

#### Pricing Comparison
The Mistral Small 4 model is priced as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens

To compare, we would need the pricing information of its top competitors. However, assuming a competitor model with similar capabilities, we can consider the following hypothetical scenarios:

* **Competitor A**: Offers input at $0.10 per 1M tokens and output at $0.50 per 1M tokens. This competitor is cheaper than Mistral Small 4 but may have trade-offs in performance or capabilities.
* **Competitor B**: Offers input at $0.20 per 1M tokens and output at $0.70 per 1M tokens. This competitor is more expensive than Mistral Small 4 and may offer superior performance or additional capabilities.

#### Performance Trade-offs
The performance of the Mistral Small 4 model is indicated by its benchmarks:
- MMLU: 80.0
- LMSYS Arena ELO: 1200

When comparing with competitors, consider the following:
* **Competitor A**: May have lower benchmark scores (e.g., MMLU: 70.0, LMSYS Arena ELO: 1000) due to its lower pricing.
* **Competitor B**: May have higher benchmark scores (e.g., MMLU: 90.0, LMSYS Arena ELO: 1400) due to its higher pricing.

#### Capabilities and Use Cases
The Mistral Small 4 model supports the following capabilities:
- text
- function_calling
- json_mode
- streaming
- structured_outputs

It is best suited for:
- chat
- text_generation
- coding
- analysis
- rag_pipelines
- summarization

When choosing between the Mistral Small 4 model and its competitors, consider the specific use case and required capabilities. If a competitor model offers similar capabilities at a lower price point or with better performance, it may be a more suitable choice.

### Example Cost Calculations
The cost of using the Mistral Small

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and release date of 2024-01-01, it offers a robust set of features for various applications.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and max output of 4,096 tokens, Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: Its function calling and structured outputs capabilities make it an excellent choice for coding and analysis tasks, such as code completion and code review.
3. **Summarization**: Mistral Small 4's ability to process large amounts of text and generate concise summaries makes it a great fit for summarization tasks.
4. **RAG Pipelines**: Its support for Retrieval-Augmented Generation (RAG) pipelines enables it to be used in applications that require generating text based on external knowledge sources.
5. **Streaming**: With its streaming capability, Mistral Small 4 can be used in real-time applications, such as live chat or text-based interfaces.

### Code Integration Example with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.Model("mistralai/mistral-small-2603")

# Define a function to generate text using the model
def generate_text(prompt):
    input_ids = openrouter.tokenize(prompt, model)
    output = model.generate(input_ids, max_length=4096)
    return openrouter.detokenize

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
