# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-14
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a wide range of natural language processing (NLP) tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens, making it suitable for complex text generation and analysis tasks.

### Main Strengths and Use-Cases
The main strengths of Mistral Small 4 include its large context window, substantial output generation capabilities, and support for various input and output formats. Its primary use-cases are chat, text generation, coding, analysis, RAG pipelines, and summarization, leveraging its capabilities in handling large contexts and generating coherent text. With a context window of 262,144 tokens and a max output of 4,096 tokens, Mistral Small 4 is well-suited for tasks that require understanding and generating long pieces of text. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its competence in handling a variety of NLP tasks.

### Pricing and Cost Considerations
Mistral Small 4 is priced at $0.15 per 1M tokens for input and $0.6 per 1M tokens for output. There are no additional costs for cached input or batch input. For developers, this pricing model means that the cost of using Mistral Small 4 will primarily depend on the volume of input and output tokens. For example, 1,000 calls with an average of 500 tokens will cost $0.375, while 10,000 calls will

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
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$None per 1M tokens** (free)
* Batch Input: **$None per 1M tokens** (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following scenarios:
* **Cached Tokens**: Use cached input tokens when possible, as they are free. This is ideal for applications with repetitive or similar input prompts.
* **Batch API Calls**: Leverage batch input to reduce costs, as batch input is free. This is suitable for applications that can process multiple inputs simultaneously.

#### Cost at Scale
The cost of using Mistral Small 4 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: **$0.375**
* **10,000 calls**: **$3.75**
* **100,000 calls**: **$37.5**

These costs demonstrate a linear scaling of expenses with the number of API calls. It is essential to consider these costs when designing applications that rely heavily on Mistral Small 4.

#### Context and Limits
Keep in mind the following context and limits when using Mistral Small 4:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12

#### Capabilities and Best Use Cases
Mistral Small 4 is capable of:
* text
* function_calling
*

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
The Mistral Small 4 model, provided by Mistralai, is a standard, non-open-source model released on 2024-01-01. 

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
The benchmark performance of Mistral Small 4 is as follows:
* MMLU: **80.0**
* HumanEval: **None**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

The **MMLU (Massive Multitask Language Understanding) score** of 80.0 indicates the model's ability to perform well across a wide range of natural language processing tasks. A higher MMLU score generally corresponds to better performance in tasks such as text classification, sentiment analysis, and question answering.

The **LMSYS Arena ELO score** of 1200 is a measure of the model's performance in a competitive environment, where it is pitted against other models. An ELO score of 1200 is relatively moderate, indicating that the model is capable of holding its own against other models, but may not be the top performer in

## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral Small 4 model, we will create a hypothetical comparison with other models in the market. For the purpose of this comparison, let's assume we have two top competitors: Model A and Model B.

#### Model A
* Provider: Competitor A
* Tier: premium
* Open Source: False
* Pricing:
	+ Input: $0.20 per 1M tokens
	+ Output: $0.80 per 1M tokens
* Context & Limits:
	+ Context Window: 512,000 tokens
	+ Max Output: 8,192 tokens
	+ Knowledge Cutoff: 2023-12
* Benchmarks:
	+ MMLU: 85.0
	+ HumanEval: 80.0
	+ LMSYS Arena ELO: 1400
* Capabilities: text, function_calling, json_mode, streaming
* Best For: chat, text_generation, coding

#### Model B
* Provider: Competitor B
* Tier: standard
* Open Source: True
* Pricing:
	+ Input: $0.10 per 1M tokens
	+ Output: $0.40 per 1M tokens
* Context & Limits:
	+ Context Window: 131,072 tokens
	+ Max Output: 2,048 tokens
	+ Knowledge Cutoff: 2022-12
* Benchmarks:
	+ MMLU: 75.0
	+ HumanEval: None
	+ LMSYS Arena ELO: 1000
* Capabilities: text, json_mode
* Best For: chat, text_generation

### Comparison Summary
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) | Context Window | MMLU |
| --- | --- | --- | --- | --- |
| Mistral Small 4 | $0.15 | $0.60 | 262,144 | 80.0 |
| Model A | $0.20 | $0.80 | 512,000 | 85.0 |
| Model B | $0.10 | $0.40 | 131,072 | 75.0 |

### Price Differences
Mistral Small 4 is priced competitively,

## Best Use Cases
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on January 1, 2024, this model is part of the standard tier and is not open-source.

### Pricing Model
The pricing for Mistral: Mistral Small 4 is as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens
- Cached Input: $None per 1M tokens
- Batch Input: $None per 1M tokens

### Top 5 Best Use Cases for Mistral: Mistral Small 4
Based on its capabilities, here are the top 5 best use cases for Mistral: Mistral Small 4:

1. **Chat and Text Generation**: With its ability to handle text and generate human-like responses, Mistral: Mistral Small 4 is well-suited for chat applications and text generation tasks.
2. **Coding and Analysis**: The model's function calling and structured outputs capabilities make it a great fit for coding and analysis tasks, such as code completion and data analysis.
3. **Summarization**: Mistral: Mistral Small 4's ability to process and generate text makes it suitable for summarization tasks, such as summarizing long documents or articles.
4. **RAG Pipelines**: The model's support for retrieval-augmented generation (RAG) pipelines makes it a great fit for tasks that require generating text based on external knowledge sources.
5. **Streaming and Real-time Applications**: With its support for streaming, Mistral: Mistral Small 4 can be used for real-time applications, such as live chat or streaming text generation.

### Code Integration Example with OpenRouter
Here is an example of how to integrate Mistral: Mistral

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
