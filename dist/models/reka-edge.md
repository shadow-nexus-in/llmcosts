# Reka Edge API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-05
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Reka Edge
Reka Edge, provided by Rekaai, is a standard-tier model released on 2024-01-01. This model is not open source. From an architectural standpoint, Reka Edge is designed to handle a variety of tasks, including text generation, function calling, and more, thanks to its capabilities in text, function_calling, json_mode, streaming, and structured_outputs. Its primary strengths lie in its ability to process large context windows of up to 16,384 tokens and generate outputs of the same length, making it suitable for complex tasks.

### Technical Specifications and Use Cases
Technically, Reka Edge operates with a knowledge cutoff of 2023-12, meaning it has been trained on data up to this point. The model's pricing is based on input and output tokens, with both costing $0.1 per 1M tokens. There are no additional costs for cached input or batch input. Reka Edge's capabilities make it best suited for applications such as chat, text generation, coding, analysis, rag_pipelines, and summarization. Its performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its proficiency in handling a range of tasks, especially those requiring extensive context understanding and generation capabilities.

### Cost and Competitiveness
In terms of cost, using Reka Edge can be estimated based on the number of calls and tokens processed. For example, 1,000 calls averaging 500 tokens would cost $0.1, scaling up to $10.0 for 100,000 calls. This pricing model makes Reka Edge a competitive option for developers looking to integrate advanced language processing capabilities into their applications without incurring exorbitant costs. With no direct competitors listed, Reka Edge stands out in its class, offering a unique combination of features, performance, and pricing that can cater to a wide range of

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.1 |
| Output | $0.1 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Reka Edge Pricing Analysis
#### Overview
Reka Edge, a standard-tier model provided by Rekaai, offers a unique pricing structure that incentivizes efficient use of its API. Released on 2024-01-01, this model is not open source.

#### Cost Structure
The cost structure for Reka Edge is as follows:
* **Input**: $0.1 per 1M tokens
* **Output**: $0.1 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

This structure indicates that using cached input and batch API calls can significantly reduce costs.

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for repeated input queries. If your application involves frequent queries with the same or similar input, utilizing cached tokens can eliminate input costs.

#### Batch API Savings
Batch input is also free, which means that submitting multiple input queries in a single API call can help reduce costs. By batching API calls, you can avoid paying for individual input queries, leading to significant savings.

#### Cost at Scale
The cost of using Reka Edge at scale is as follows:
* **1,000 calls (avg 500 tokens)**: $0.1
* **10,000 calls**: $1.0
* **100,000 calls**: $10.0

These costs demonstrate a linear relationship between the number of API calls and the total cost.

#### Context and Limits
Reka Edge has the following context and limits:
* **Context Window**: 16,384 tokens
* **Max Output**: 16,384 tokens
* **Knowledge Cutoff**: 2023-12

These limits are essential to consider when designing your application to ensure efficient and cost-effective use of the Reka Edge API.

#### Capabilities and Use Cases
Reka Edge is capable of:
* Text

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Reka Edge Benchmark Performance Analysis
#### Model Overview
The Reka Edge model, provided by Rekaai, is a standard-tier model released on 2024-01-01. It is not open-source.

#### Pricing
The pricing for Reka Edge is as follows:
* Input: **$0.1 per 1M tokens**
* Output: **$0.1 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Context and Limits
The model has the following context and limits:
* Context Window: **16,384 tokens**
* Max Output: **16,384 tokens**
* Knowledge Cutoff: **2023-12**

#### Benchmarks
The benchmark performance of Reka Edge is as follows:
* MMLU: **80.0**
* HumanEval: **None**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

The MMLU score of 80.0 indicates the model's ability to understand and process mathematical and logical concepts. A higher MMLU score generally corresponds to better performance in tasks that require mathematical and logical reasoning.

The LMSYS Arena ELO score of 1200 is a measure of the model's overall performance in a competitive benchmarking environment. A higher ELO score indicates better performance compared to other models.

The lack of HumanEval and GSM8K scores makes it difficult to assess the model's performance in specific areas such as coding and mathematical problem-solving.

#### Capabilities and Use Cases
Reka Edge supports the following capabilities:
* text
* function_calling
* json_mode

## Competitor Comparison
### Reka Edge Comparison
Since there are no direct competitors listed for Reka Edge, we will provide a general overview of its features, pricing, and performance. This will help users understand when to choose Reka Edge and what to expect from the model.

#### Model Overview
* **Provider:** Rekaai
* **Release Date:** 2024-01-01
* **Tier:** Standard
* **Open Source:** False

#### Pricing
The pricing for Reka Edge is as follows:
* **Input:** $0.1 per 1M tokens
* **Output:** $0.1 per 1M tokens
* **Cached Input:** $None per 1M tokens
* **Batch Input:** $None per 1M tokens

#### Context and Limits
Reka Edge has the following context and limits:
* **Context Window:** 16,384 tokens
* **Max Output:** 16,384 tokens
* **Knowledge Cutoff:** 2023-12

#### Benchmarks
Reka Edge has the following benchmark scores:
* **MMLU:** 80.0
* **LMSYS Arena ELO:** 1200

#### Capabilities and Best Use Cases
Reka Edge supports the following capabilities:
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
Here are some cost examples for using Reka Edge:
* 1,000 calls (avg 500 tokens): $0.1
* 10,000 calls: $1.0
* 100,000 calls: $10.0

#### Choosing Reka Edge
Since there are no direct competitors listed, Reka Edge can be considered for its unique combination of capabilities, pricing, and performance. Users should evaluate Reka Edge based on their specific use cases and requirements, considering factors such as context window, max output, and knowledge cutoff. If Reka Edge meets their needs and budget, it can be a suitable choice for a wide range of applications, including chat, text generation, coding, and analysis.

## Best Use Cases
### Introduction to Reka Edge
Reka Edge is a standard-tier model provided by Rekaai, released on 2024-01-01. It is not open-source and offers a range of capabilities including text, function calling, JSON mode, streaming, and structured outputs.

### Top 5 Best Use Cases for Reka Edge
Based on its capabilities, Reka Edge is best suited for the following use cases:

1. **Chat and Text Generation**: With its ability to handle text and generate human-like responses, Reka Edge can be used to build conversational AI models.
2. **Coding and Analysis**: Reka Edge's function calling and structured outputs capabilities make it suitable for coding and analysis tasks, such as code completion and code review.
3. **Summarization**: Reka Edge can be used for summarization tasks, such as summarizing long pieces of text into shorter, more digestible versions.
4. **RAG Pipelines**: Reka Edge's ability to handle JSON mode and streaming makes it a good fit for RAG (Retrieve, Augment, Generate) pipelines, which involve retrieving information from a database, augmenting it, and generating text based on the retrieved information.
5. **Streaming and Real-time Analysis**: Reka Edge's streaming capability makes it suitable for real-time analysis tasks, such as analyzing log data or sensor readings.

### Code Integration Examples with OpenRouter
To integrate Reka Edge with OpenRouter, you can use the following code example:
```python
import os
import openrouter

# Initialize the OpenRouter client
client = openrouter.Client(api_key="YOUR_API_KEY")

# Define the Reka Edge model
model = client.models.get("rekaai/reka-edge")

# Define the input text
input_text = "This is an example input text."

# Define the function to call
def generate_text(input_text):
    # Call the Reka Edge model
    response = model.generate_text(input_text

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
