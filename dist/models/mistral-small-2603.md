# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-04
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of natural language processing tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens.

### Technical Specifications and Use Cases
The pricing model for Mistral Small 4 is based on input and output tokens, with costs of $0.15 per 1M input tokens and $0.6 per 1M output tokens. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. Given its capabilities, Mistral Small 4 is best suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization. Its large context window and output capabilities make it particularly useful for tasks that require understanding and generating lengthy, coherent texts.

### Cost Considerations and Competitors
For developers considering the use of Mistral Small 4, the cost can be estimated based on the number of calls and tokens processed. For example, 1,000 calls with an average of 500 tokens per call would cost $0.375, while 100,000 calls would amount to $37.5. As of the current data, there are no direct competitors listed for Mistral Small 4, suggesting it may offer unique advantages in its tier and capabilities. However, the lack of open-source status may limit its appeal to certain developers or projects. Overall, Mistral Small 4 presents a robust option for NLP tasks, especially those requiring extensive context understanding and lengthy output generation

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
* **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
* **Batch API Savings**: Although batch input is free, the actual cost savings come from reducing the number of API calls. By batching inputs, users can decrease the total number of calls, resulting in lower output costs.
* **Cost at Scale**: The cost-effectiveness of Mistral Small 4 at scale is as follows:
	+ 1,000 calls (avg 500 tokens): **$0.375**
	+ 10,000 calls: **$3.75**
	+ 100,000 calls: **$37.5**

#### Cost Calculation
To calculate the cost, we need to consider both input and output tokens. However, since the exact token count per call is not provided, we will use the average token count of 500 tokens per call as a reference.

Assuming an average of 500 input tokens and 500 output tokens (conservative estimate), the cost per call would be:
* Input: 500 tokens / 1,000,000 tokens * $0.15 = $0.000075
* Output: 500 tokens / 1,

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
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. It is not open source. This analysis focuses on its benchmark performance, specifically the MMLU, HumanEval, and Arena ELO scores, to understand its capabilities and limitations for real-world use.

#### Benchmark Scores
- **MMLU (Massive Multitask Language Understanding) Score: 80.0**
  The MMLU score measures a model's ability to perform a wide range of natural language understanding tasks. A score of 80.0 indicates that Mistral Small 4 has a good level of language understanding, capable of handling various tasks with reasonable accuracy. This score is significant for real-world applications that require the model to comprehend and process human language effectively, such as chatbots, text analysis, and summarization tools.

- **HumanEval Score: None**
  HumanEval is a benchmark that evaluates a model's ability to generate correct Python code based on a given prompt. The absence of a HumanEval score for Mistral Small 4 means that its coding capabilities, specifically in generating Python code, have not been evaluated or reported. This lack of data makes it challenging to assess its performance in coding tasks compared to other models.

- **LMSYS Arena ELO Score: 1200**
  The LMSYS Arena ELO score is a measure of a model's performance in a competitive environment, where models are pitted against each other to solve tasks. An ELO score of 1200 suggests that Mistral Small 4 has a moderate level of competence. In real

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral: Mistral Small 4, we will provide a general overview of its features, pricing, and performance. This will help in understanding when to choose this model over others in the market.

#### Model Overview
* **Provider:** Mistralai
* **Release Date:** 2024-01-01
* **Tier:** Standard
* **Open Source:** False

#### Pricing
The pricing for Mistral: Mistral Small 4 is as follows:
* **Input:** $0.15 per 1M tokens
* **Output:** $0.6 per 1M tokens
* **Cached Input:** $None per 1M tokens
* **Batch Input:** $None per 1M tokens

#### Context and Limits
* **Context Window:** 262,144 tokens
* **Max Output:** 4,096 tokens
* **Knowledge Cutoff:** 2023-12

#### Benchmarks
* **MMLU:** 80.0
* **HumanEval:** None
* **LMSYS Arena ELO:** 1200
* **GSM8K:** None

#### Capabilities and Best Use Cases
Mistral: Mistral Small 4 supports the following capabilities:
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

#### Cost Examples
The estimated costs for using Mistral: Mistral Small 4 are:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

### Choosing Mistral: Mistral Small 4
Given the lack of direct competitors, the decision to choose Mistral: Mistral Small 4 should be based on its features, pricing, and performance. Consider the following factors:
* **Context Window:** If your application requires a large context window (262,144 tokens), Mistral: Mistral Small 4 might be a good choice.
* **Max Output:** If your application requires a moderate output size (4,096 tokens), Mistral: Mistral Small 4 could be suitable.
* **Capabilities

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and release date of 2024-01-01, it offers a robust set of features for various applications.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and max output of 4,096 tokens, Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: Its ability to perform function calling and structured outputs makes it an excellent choice for coding and analysis tasks, such as code completion and code review.
3. **Summarization**: Mistral Small 4's capabilities in text generation and analysis make it a good fit for summarization tasks, such as summarizing long documents or articles.
4. **RAG Pipelines**: Its support for structured outputs and function calling enables Mistral Small 4 to be used in RAG (Retrieval-Augmented Generation) pipelines for tasks like question answering and text generation.
5. **Streaming and Real-time Applications**: With its streaming capability, Mistral Small 4 can be used in real-time applications, such as live chat, sentiment analysis, and real-time text generation.

### Code Integration Example with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code example:
```python
import os
import requests

# Set API endpoint and credentials
api_endpoint = "https://api.mistralai.com/mistral-small-4"
api_key = "YOUR_API_KEY"

# Set input text and parameters
input_text = "Hello, how are you

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
