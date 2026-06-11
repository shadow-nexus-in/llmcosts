# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-11
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to process and generate human-like text based on the input it receives, leveraging its capabilities in natural language processing. Its primary strengths lie in its ability to handle a wide range of tasks, including but not limited to chat, text generation, coding, analysis, and summarization, thanks to its support for text, function calling, JSON mode, streaming, and structured outputs.

### Technical Specifications and Use Cases
Technically, Mistral Small 4 boasts a context window of 262,144 tokens and can generate up to 4,096 tokens as output. Its knowledge cutoff is 2023-12, indicating that its training data includes information up to December 2023. The model has been benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, demonstrating its proficiency in various linguistic tasks. Given its capabilities, Mistral Small 4 is best utilized for applications such as chatbots, text generation, coding assistance, data analysis, and content summarization. However, its pricing model, which includes $0.15 per 1M tokens for input and $0.6 per 1M tokens for output, should be considered when planning for large-scale deployments.

### Pricing and Cost Considerations
The pricing for Mistral Small 4 is structured around input and output tokens, with costs of $0.15 per 1M tokens for input and $0.6 per 1M tokens for output. For developers planning to integrate this model into their applications, cost examples provided by Mistralai indicate that 1,000 calls (averaging 500 tokens per call) would cost $0.375, scaling up to

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.15 |
| Output | $0.6 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Mistral Small 4
#### Overview
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings opportunities for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens (free)
* Batch Input: $None per 1M tokens (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following strategies:
* **Cached Tokens**: Since cached input tokens are free, it's beneficial to use them whenever possible. This can be particularly useful for applications with repetitive or similar input patterns.
* **Batch API Calls**: With batch input tokens being free, batching API calls can lead to significant cost savings. This approach is ideal for applications that can process multiple inputs simultaneously.

#### Cost at Scale
The cost examples provided are as follows:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

To put these costs into perspective, let's calculate the cost per 1M tokens for each scenario:
* 1,000 calls (avg 500 tokens): 500,000 tokens / 1,000 calls = 500 tokens per call. Assuming an average output of 500 tokens per call, the total tokens processed would be 1,000,000 tokens (500 input + 500 output). The cost would be $0.15 (input) + $0.6 (output) = $0.75 per 1M tokens.
* 10,000 calls: Assuming the same token

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Benchmark Performance Analysis
#### Model Overview
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

The MMLU score of **80.0** indicates the model's performance on a set of mathematical and logical tasks. A higher score generally indicates better performance.
The LMSYS Arena ELO score of **1200** is a measure of the model's performance in a competitive setting, with higher scores indicating better performance. For real-world use, this score suggests that Mistral Small 4 can hold its own in tasks that require strategic thinking and problem-solving.

The lack of HumanEval and GSM8K scores makes it difficult to assess the model's performance on specific tasks such as coding and mathematical problem-solving.

#### Capabilities and Use Cases
Mistral

## Competitor Comparison
### Mistral Small 4 Comparison
Since there are no direct competitors listed for the Mistral Small 4 model, we will provide a general overview of its features, pricing, and performance. This will help users understand its capabilities and make informed decisions about its use.

#### Model Overview
The Mistral Small 4 model is a standard, non-open-source model provided by Mistralai, released on January 1, 2024. Its key features include:

* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: December 2023
* **Capabilities**: text, function_calling, json_mode, streaming, structured_outputs
* **Best For**: chat, text_generation, coding, analysis, rag_pipelines, summarization

#### Pricing
The pricing for the Mistral Small 4 model is as follows:

* **Input**: $0.15 per 1M tokens
* **Output**: $0.6 per 1M tokens
* **Cached Input**: $None per 1M tokens
* **Batch Input**: $None per 1M tokens

#### Cost Examples
To help estimate costs, here are some examples:

* **1,000 calls (avg 500 tokens)**: $0.375
* **10,000 calls**: $3.75
* **100,000 calls**: $37.5

#### Performance
The Mistral Small 4 model has the following benchmark scores:

* **MMLU**: 80.0
* **LMSYS Arena ELO**: 1200

Note that HumanEval and GSM8K benchmark scores are not available.

#### Choosing the Mistral Small 4 Model
Given the lack of direct competitors, the Mistral Small 4 model can be considered for a wide range of applications, including:

* Chat and text generation
* Coding and analysis
* RAG pipelines and summarization

However, users should carefully evaluate their specific use case and consider factors such as input and output token counts, context window requirements, and performance needs before selecting the Mistral Small 4 model.

In the absence of direct competitors, users may want to consider other models that offer similar capabilities and pricing structures. It is essential to weigh the trade-offs between different models and choose the one that best fits their specific requirements and budget.

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on 2024-01-01, this model is part of the standard tier and is not open source.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities, the following are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and ability to generate up to 4,096 tokens of output, Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: The model's ability to perform function calling and generate structured outputs makes it a good fit for coding and analysis tasks, such as code completion and data analysis.
3. **Summarization**: Mistral Small 4's text generation capabilities and high context window make it suitable for summarization tasks, such as summarizing long documents or articles.
4. **RAG Pipelines**: The model's ability to generate structured outputs and perform function calling makes it a good fit for RAG (Retrieve, Augment, Generate) pipelines, which involve retrieving information from a knowledge base, augmenting it, and generating text based on it.
5. **Streaming**: With its support for streaming, Mistral Small 4 can be used for real-time text generation and analysis applications, such as live chat or sentiment analysis.

### Code Integration Example with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.Model("mistralai/mistral-small-2603")

# Define a function to generate text using the model
def generate_text(prompt):


## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
