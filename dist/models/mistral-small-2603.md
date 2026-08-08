# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-08
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open-source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of natural language processing tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens, making it suitable for complex tasks.

### Technical Specifications and Use Cases
Technically, Mistral Small 4 has a context window of 262,144 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2023-12. The model's pricing is based on input and output tokens, with costs of $0.15 per 1M tokens for input and $0.6 per 1M tokens for output. The model excels in tasks such as chat, text generation, coding, analysis, RAG pipelines, and summarization, thanks to its robust capabilities. Its performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its competence in handling a wide range of language tasks.

### Pricing and Cost Considerations
For developers considering integrating Mistral Small 4 into their applications, the pricing model is straightforward. The cost for using the model can be estimated based on the number of calls and the average number of tokens per call. For example, 1,000 calls with an average of 500 tokens per call would cost $0.375, while 10,000 calls would cost $3.75, and 100,000 calls would amount to $37.5. Given its capabilities and pricing structure, Mistral Small 4 is a viable option for projects

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
Mistral Small 4, provided by Mistralai, is a standard tier model with a release date of 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* **Input**: $0.15 per 1M tokens
* **Output**: $0.6 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
Given the cost structure, it's essential to understand when to utilize cached tokens and batch API calls to minimize costs.

* **Cached Tokens**: Since cached input tokens are free, it's beneficial to use them whenever possible. This can significantly reduce costs for repeated input sequences.
* **Batch API Calls**: With batch input being free, batching API calls can lead to substantial savings, especially for large-scale applications.

#### Cost at Scale
To illustrate the cost implications at scale, let's examine the provided cost examples:
* **1,000 calls (avg 500 tokens)**: $0.375
* **10,000 calls**: $3.75
* **100,000 calls**: $37.5

These examples demonstrate a linear cost increase with the number of API calls. It's crucial to consider these costs when designing applications that rely on Mistral Small 4.

#### Cost Calculation
To calculate the cost for a specific use case, you can use the following formula:
Cost = (Number of Input Tokens / 1,000,000) \* $0.15 + (Number of Output Tokens / 1,000,000) \* $0.6

For instance, if you have an application with an average input of 

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Analysis
#### Model Overview
The Mistral Small 4 model, provided by Mistralai, is a standard-tier model released on 2024-01-01. It is not open source.

#### Pricing Structure
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

#### Benchmark Performance
The benchmark performance of Mistral Small 4 is:
* MMLU: **80.0**
* HumanEval: **None**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

The MMLU score of 80.0 indicates the model's performance on a range of natural language understanding tasks. A higher MMLU score generally corresponds to better performance.

The LMSYS Arena ELO score of 1200 is a measure of the model's performance in a competitive arena, where it is pitted against other models. An ELO score of 1200 is a relatively moderate score, indicating that the model is capable but may not be the top performer in all scenarios.

The lack of HumanEval and GSM8K scores means that the model's performance on these specific benchmarks is unknown.

#### Real-World Implications
For real-world use,

## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral Small 4 model, we will provide a general analysis of the model's features, pricing, and performance. This will help users understand the value proposition of the Mistral Small 4 and make informed decisions about its adoption.

#### Model Overview
The Mistral Small 4 model is a standard-tier model provided by Mistralai, released on 2024-01-01. It is not open-source.

#### Pricing
The pricing for the Mistral Small 4 model is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Context and Limits
The model has the following context and limits:
* Context Window: 262,144 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2023-12

#### Benchmarks
The model's performance is measured by the following benchmarks:
* MMLU: 80.0
* LMSYS Arena ELO: 1200

#### Capabilities and Best Use Cases
The Mistral Small 4 model supports the following capabilities:
* text
* function_calling
* json_mode
* streaming
* structured_outputs
It is best suited for the following use cases:
* chat
* text_generation
* coding
* analysis
* rag_pipelines
* summarization

#### Cost Examples
The estimated costs for using the Mistral Small 4 model are:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

#### Choosing the Mistral Small 4 Model
Since there are no direct competitors listed, the decision to choose the Mistral Small 4 model depends on the specific requirements of the project. Users should consider the following factors:
* The model's capabilities and features align with the project's needs.
* The pricing is competitive with other models in the market (although no direct competitors are listed).
* The performance benchmarks (MMLU and LMSYS Arena ELO) indicate that the model can deliver the required level of accuracy and performance.

In summary, the Mistral

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and release date of 2024-01-01, it offers a robust set of features for various applications.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and ability to generate up to 4,096 tokens, Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: Its function calling and structured outputs capabilities make it an excellent choice for coding and analysis tasks, such as code completion and data analysis.
3. **Summarization and RAG Pipelines**: Mistral Small 4's ability to process large amounts of text and generate concise summaries makes it a great fit for summarization and RAG (Retrieve, Augment, Generate) pipelines.
4. **Streaming and Real-time Applications**: With its streaming capability, Mistral Small 4 can be used for real-time applications, such as live chat or text-based interfaces.
5. **JSON Mode and Structured Outputs**: Its JSON mode and structured outputs capabilities make it suitable for applications that require structured data, such as data processing and integration.

### Code Integration Example with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.Model("mistralai/mistral-small-2603")

# Define a function to generate text using the model
def generate_text(prompt):
    # Use the model to generate text
    output = model.generate

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
