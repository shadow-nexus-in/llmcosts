# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-28
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of natural language processing tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to perform well in chat, text generation, coding, analysis, RAG pipelines, and summarization tasks.

### Technical Specifications and Use Cases
Technically, Mistral Small 4 operates with a context window of 262,144 tokens and can generate up to 4,096 tokens as output. Its knowledge cutoff is 2023-12, indicating that its training data does not include information beyond this date. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. Given its capabilities, Mistral Small 4 is best utilized for applications such as chatbots, text generation, coding assistance, data analysis, and document summarization. However, specific tasks it is not well-suited for are not listed, suggesting a broad applicability within the NLP domain.

### Pricing and Cost Considerations
The pricing for Mistral Small 4 is structured around input and output tokens. Developers are charged $0.15 per 1M input tokens and $0.6 per 1M output tokens. There are no additional costs for cached input or batch input. To illustrate, for 1,000 calls averaging 500 tokens, the cost would be $0.375, scaling to $3.75 for 10,000 calls, and $37.5 for 100,000 calls. With no direct competitors listed, Mistral Small 4 presents a unique offering in the market, balancing performance with a structured pricing model that

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
The Mistral Small 4 model, provided by Mistralai, is a standard, non-open-source model released on 2024-01-01. This analysis will delve into the cost structure, usage scenarios, and cost savings of using this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$None per 1M tokens** (free)
* Batch Input: **$None per 1M tokens** (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs when the same input is used multiple times. Since cached input is free, it is recommended to use cached tokens whenever possible to minimize costs.

#### Batch API Savings
The batch input pricing is **$None per 1M tokens**, which means that batch API calls are free. This can lead to significant cost savings when making multiple API calls with the same input.

#### Cost at Scale
The cost of using Mistral Small 4 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: **$0.375**
* **10,000 calls**: **$3.75**
* **100,000 calls**: **$37.5**

These costs are calculated based on the average number of tokens per call and the input and output pricing.

#### Conclusion
The Mistral Small 4 model offers a cost-effective solution for text-based applications, with a pricing structure that incentivizes the use of cached tokens and batch API calls. By understanding the cost structure and using these features effectively, users can minimize their costs and maximize their ROI.

### Recommendations
* Use cached tokens whenever possible to reduce costs
* Utilize batch API calls to take advantage of free input pricing
* Opt

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Benchmark Analysis
#### Model Overview
The Mistral Small 4 model, provided by Mistralai, is a standard-tier model released on 2024-01-01. It is not open-source and has the following pricing structure:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Benchmark Performance
The model's benchmark performance is as follows:
* **MMLU (Massive Multitask Language Understanding) score: 80.0** - This score indicates the model's ability to understand and perform a wide range of natural language tasks. A higher score generally corresponds to better performance.
* **HumanEval score: None** - HumanEval is a benchmark that evaluates a model's ability to generate code. The lack of a score for this benchmark means that the model's coding capabilities are not well-defined.
* **LMSYS Arena ELO score: 1200** - The LMSYS Arena ELO score is a measure of a model's performance in a competitive environment. An ELO score of 1200 is relatively moderate, indicating that the model can hold its own in certain tasks but may struggle with more complex or nuanced challenges.

#### Real-World Implications
For real-world use, these benchmark scores have the following implications:
* The MMLU score of 80.0 suggests that the Mistral Small 4 model is capable of handling a variety of natural language tasks, making it suitable for applications such as chat, text generation, and analysis.
* The lack of

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral: Mistral Small 4, we will create a hypothetical comparison with other models in the standard tier. 

#### Model Overview
* **Mistral: Mistral Small 4 (mistralai/mistral-small-2603)**
	+ Provider: Mistralai
	+ Release Date: 2024-01-01
	+ Tier: standard
	+ Open Source: False
	+ Pricing:
		- Input: $0.15 per 1M tokens
		- Output: $0.6 per 1M tokens
		- Cached Input: $None per 1M tokens
		- Batch Input: $None per 1M tokens
	+ Context & Limits:
		- Context Window: 262,144 tokens
		- Max Output: 4,096 tokens
		- Knowledge Cutoff: 2023-12
	+ Benchmarks:
		- MMLU: 80.0
		- LMSYS Arena ELO: 1200
	+ Capabilities: text, function_calling, json_mode, streaming, structured_outputs
	+ Best For: chat, text_generation, coding, analysis, rag_pipelines, summarization

#### Hypothetical Competitors
For the purpose of this comparison, let's consider two hypothetical models, **Model A** and **Model B**, with the following characteristics:

* **Model A**
	+ Pricing:
		- Input: $0.10 per 1M tokens
		- Output: $0.5 per 1M tokens
	+ Context & Limits:
		- Context Window: 131,072 tokens
		- Max Output: 2,048 tokens
	+ Benchmarks:
		- MMLU: 70.0
		- LMSYS Arena ELO: 1000
* **Model B**
	+ Pricing:
		- Input: $0.20 per 1M tokens
		- Output: $0.8 per 1M tokens
	+ Context & Limits:
		- Context Window: 524,288 tokens
		- Max Output: 8,192 tokens
	+ Benchmarks:
		- MML

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on January 1, 2024, this standard-tier model is not open-source and offers a context window of 262,144 tokens and a maximum output of 4,096 tokens.

### Pricing Model
The pricing for Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its ability to generate human-like text and its large context window, Mistral Small 4 is well-suited for chat applications and text generation tasks.
2. **Coding and Analysis**: Mistral Small 4's function calling and structured outputs capabilities make it a great choice for coding and analysis tasks, such as code completion and code review.
3. **Summarization**: The model's ability to generate concise and accurate summaries makes it a great choice for summarization tasks, such as summarizing long documents or articles.
4. **RAG Pipelines**: Mistral Small 4's support for RAG (Retrieval-Augmented Generation) pipelines makes it a great choice for tasks that require retrieving and generating text based on external knowledge sources.
5. **Streaming and Real-time Applications**: With its support for streaming and real-time outputs, Mistral Small 4 is well-suited for applications that require real-time text generation, such as live chat or real-time analytics.

### Code Integration Example with OpenRouter
Here

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
