# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-13
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a wide range of natural language processing tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens.

### Technical Specifications and Use Cases
The model's technical specifications highlight its potential for various applications. With a context window of 262,144 tokens and a maximum output of 4,096 tokens, Mistral Small 4 is suited for tasks requiring extensive input processing and detailed output generation. Its capabilities make it best for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization. The pricing model for Mistral Small 4 includes charges of $0.15 per 1M tokens for input and $0.6 per 1M tokens for output. This pricing structure suggests that developers should consider the input and output token counts when planning their application's budget. The model's benchmarks, such as an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, provide further insight into its performance capabilities.

### Cost Considerations and Competitors
For developers planning to integrate Mistral Small 4 into their applications, understanding the cost implications is crucial. The provided cost examples indicate that 1,000 calls with an average of 500 tokens would cost $0.375, scaling up to $37.5 for 100,000 calls. These costs are based on the input and output pricing, emphasizing the importance of optimizing token usage. As of the current data, there are no direct competitors

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
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* **Input**: $0.15 per 1M tokens
* **Output**: $0.6 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following scenarios:
* **Cached Tokens**: Utilize cached input tokens whenever possible, as they are free. This can significantly reduce costs for repeated or similar input queries.
* **Batch API**: Leverage batch input for multiple queries at once, as it is also free. This can lead to substantial cost savings for large-scale applications.

#### Cost at Scale
The costs for Mistral Small 4 at various scales are:
* **1,000 calls** (avg 500 tokens): $0.375
* **10,000 calls**: $3.75
* **100,000 calls**: $37.5

These costs demonstrate a linear relationship with the number of API calls, indicating that the cost per call remains constant regardless of the scale.

#### Cost Savings
By utilizing cached input tokens and batch API calls, users can potentially reduce their costs. However, the provided pricing structure does not offer explicit discounts for these scenarios. The cost savings will primarily come from minimizing the number of input tokens and API calls.

#### Conclusion
Mistral Small 4 offers a straightforward pricing structure with costs based on input and output tokens. By understanding the cost structure and leveraging cached input tokens and batch API calls, users can optimize their usage

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Mistral Small 4 Benchmark Performance
The Mistral Small 4 model, provided by Mistralai, has a set of benchmark scores that indicate its performance in various tasks. Here's a breakdown of what these scores mean for real-world use:

#### MMLU Score: 80.0
The MMLU (Massive Multitask Language Understanding) score measures a model's ability to perform a wide range of natural language processing tasks. A score of 80.0 indicates that Mistral Small 4 has a strong foundation in language understanding, which is beneficial for tasks like text generation, chat, and analysis.

#### HumanEval Score: None
The HumanEval score is not available for Mistral Small 4. HumanEval is a benchmark that evaluates a model's ability to generate code that passes human-written tests. The absence of this score means that the model's coding capabilities are not directly comparable to other models using this benchmark.

#### LMSYS Arena ELO Score: 1200
The LMSYS Arena ELO score is a measure of a model's performance in a competitive environment, where it is pitted against other models in a series of tasks. An ELO score of 1200 indicates that Mistral Small 4 has a moderate level of performance in this arena. For real-world use, this score suggests that the model can hold its own in tasks that require a balance of language understanding and generation capabilities.

### Real-World Implications
The benchmark scores of Mistral Small 4 suggest that it is well-suited for tasks that require strong language understanding, such as:

* Text generation
* Chat
* Analysis
* Summarization

However, the lack of a

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral: Mistral Small 4 model, we will provide a general comparison framework that can be used to evaluate this model against potential competitors. 

#### Pricing Comparison
The pricing for Mistral: Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

To compare, potential competitors would need to be evaluated based on their pricing structures for input and output tokens. 

#### Performance Trade-offs
The performance of Mistral: Mistral Small 4 can be evaluated based on its benchmarks:
* MMLU: 80.0
* LMSYS Arena ELO: 1200

Competitors would need to be evaluated based on similar benchmarks to determine their performance trade-offs. 

#### Context and Limits
The context and limits of Mistral: Mistral Small 4 are:
* Context Window: 262,144 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2023-12

Competitors would need to be evaluated based on their context windows, maximum output, and knowledge cutoffs to determine their suitability for specific use cases. 

#### Capabilities and Best Use Cases
Mistral: Mistral Small 4 has the following capabilities:
* text
* function_calling
* json_mode
* streaming
* structured_outputs

It is best suited for:
* chat
* text_generation
* coding
* analysis
* rag_pipelines
* summarization

Competitors would need to be evaluated based on their capabilities and best use cases to determine their suitability for specific applications. 

#### Cost Examples
The cost examples for Mistral: Mistral Small 4 are:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

Competitors would need to be evaluated based on their cost structures to determine the most cost-effective option for specific use cases. 

### Conclusion
Since there are no direct competitors listed for the Mistral: Mistral Small 4 model, a general comparison framework has been provided. To

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, coding, analysis, and more. With its standard tier and release date of 2024-01-01, it offers a robust set of features for various applications.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its ability to process up to 262,144 tokens in its context window and generate up to 4,096 tokens in output, Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: Its capabilities in function calling, JSON mode, and structured outputs make it an excellent choice for coding and analysis tasks, such as code completion and data analysis.
3. **Summarization and RAG Pipelines**: Mistral Small 4's ability to process large amounts of text and generate concise summaries makes it a great fit for summarization tasks and RAG (Retrieval-Augmented Generation) pipelines.
4. **Streaming and Real-time Applications**: With its support for streaming, Mistral Small 4 can be used in real-time applications, such as live chatbots or streaming text analysis.
5. **OpenRouter Integration**: Mistral Small 4 can be integrated with OpenRouter for advanced routing and networking applications, such as network configuration and optimization.

### Code Integration Examples with OpenRouter
Here are some code integration examples with OpenRouter:
```python
import openrouter
from mistralai import MistralSmall4

# Initialize Mistral Small 4 model
model = MistralSmall4()

# Define a function to generate text using Mistral Small 4
def generate_text(prompt):
    input_ids = model.encode(prompt)
    output_ids =

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
