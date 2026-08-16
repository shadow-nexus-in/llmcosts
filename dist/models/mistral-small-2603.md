# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-16
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of tasks, including text generation, coding, analysis, and summarization, thanks to its capabilities in text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens.

### Technical Specifications and Use Cases
Technically, Mistral Small 4 boasts a context window of 262,144 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2023-12. The model's pricing is structured around input and output tokens, with costs of $0.15 per 1M input tokens and $0.6 per 1M output tokens. It is particularly suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. Given its capabilities and pricing, Mistral Small 4 is an attractive option for developers seeking a robust language model for a variety of text-based applications.

### Pricing and Cost Examples
The pricing model for Mistral Small 4 is straightforward, with input tokens costing $0.15 per 1M tokens and output tokens costing $0.6 per 1M tokens. There are no additional costs for cached input or batch input. To illustrate the cost implications, for 1,000 calls averaging 500 tokens, the cost would be $0.375. Scaling this up, 10,000 calls would cost $3.75, and 100,

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
Mistral Small 4, provided by Mistralai, is a standard tier model released on 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
- **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
- **Batch API Savings**: Although batch input is free, the actual cost savings come from reducing the number of API calls. By batching inputs, you can significantly lower your overall cost by minimizing the number of calls.

#### Cost at Scale
The cost examples provided are as follows:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These examples illustrate a linear cost increase with the number of API calls, indicating that the cost per call remains constant.

#### Cost Calculation
To calculate the cost, we can use the following formula:
- **Total Cost** = (Number of Input Tokens / 1,000,000) \* $0.15 + (Number of Output Tokens / 1,000,000) \* $0.6

Since the cost examples are based on the average number of tokens per call, we can estimate the cost per call as follows:
- **Cost per Call** = $0.375 / 1,000 calls = $0.000375

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
The Mistral Small 4 model, provided by Mistralai, is a standard-tier model released on 2024-01-01. It is not open-source and has a specific pricing structure based on input and output tokens.

#### Pricing Structure
The pricing for Mistral Small 4 is as follows:
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$None per 1M tokens** (not applicable)
* Batch Input: **$None per 1M tokens** (not applicable)

#### Context and Limits
The model has the following context and limits:
* Context Window: **262,144 tokens**
* Max Output: **4,096 tokens**
* Knowledge Cutoff: **2023-12** (model knowledge is current up to December 2023)

#### Benchmarks
The model's benchmark performance is as follows:
* MMLU: **80.0** (a measure of the model's ability to understand and generate human-like text)
* HumanEval: **None** (no data available for this benchmark)
* LMSYS Arena ELO: **1200** (a measure of the model's performance in a competitive arena, with higher scores indicating better performance)
* GSM8K: **None** (no data available for this benchmark)

#### Capabilities and Use Cases
Mistral Small 4 supports the following capabilities:
* text
* function_calling
* json_mode
* streaming
* structured_outputs

It is best suited for tasks such as:
* chat
* text_generation
* coding

## Competitor Comparison
### Mistral Small 4 Comparison
Since there are no direct competitors listed for the Mistral Small 4, we will provide a general overview of its features, pricing, and performance. This will help users understand its capabilities and make informed decisions about its potential use cases.

#### Pricing
The Mistral Small 4 is priced as follows:
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$None per 1M tokens** (not available)
* Batch Input: **$None per 1M tokens** (not available)

#### Performance and Capabilities
The Mistral Small 4 has the following performance metrics and capabilities:
* Context Window: **262,144 tokens**
* Max Output: **4,096 tokens**
* Knowledge Cutoff: **2023-12**
* MMLU: **80.0**
* LMSYS Arena ELO: **1200**
* Capabilities: **text**, **function_calling**, **json_mode**, **streaming**, **structured_outputs**
* Best for: **chat**, **text_generation**, **coding**, **analysis**, **rag_pipelines**, **summarization**

#### Cost Examples
The estimated costs for using the Mistral Small 4 are:
* 1,000 calls (avg 500 tokens): **$0.375**
* 10,000 calls: **$3.75**
* 100,000 calls: **$37.5**

#### Choosing the Mistral Small 4
Given the lack of direct competitors, the Mistral Small 4 can be considered for a wide range of applications, including:
* Chat and text generation
* Coding and analysis
* RAG pipelines and summarization

When to choose the Mistral Small 4:
* When you need a model with a large context window (**262,144 tokens**)
* When you require a model with a high MMLU score (**80.0**)
* When you need a model that supports **function_calling**, **json_mode**, **streaming**, and **structured_outputs**

Keep in mind that the Mistral Small 4 is a **standard** tier model, and its performance may vary depending on the specific use case and requirements. It is also important to note that the model is not **open source**, which may be a consideration for some users.

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on 2024-01-01, this model is part of the standard tier and is not open-source.

### Top 5 Best Use Cases for Mistral Small 4
Given its capabilities, here are the top 5 best use cases for Mistral Small 4, along with code integration examples using OpenRouter:

1. **Chat and Text Generation**: Mistral Small 4 excels in generating human-like text, making it ideal for chat applications.
   ```python
   import openrouter
   model = openrouter.load_model("mistralai/mistral-small-2603")
   response = model.generate_text("Hello, how are you?")
   print(response)
   ```
2. **Coding and Function Calling**: With its ability to understand and generate code, Mistral Small 4 can be used for automated coding tasks.
   ```python
   import openrouter
   model = openrouter.load_model("mistralai/mistral-small-2603")
   response = model.call_function("add", 2, 3)
   print(response)
   ```
3. **Analysis and Summarization**: Mistral Small 4 can analyze large texts and summarize them, making it useful for research and data analysis tasks.
   ```python
   import openrouter
   model = openrouter.load_model("mistralai/mistral-small-2603")
   response = model.summarize_text("Large text to summarize")
   print(response)
   ```
4. **RAG Pipelines**: Mistral Small 4 supports RAG (Retrieval-Augmented Generation) pipelines, which enable more accurate and informative text generation.
   ```python
   import openrouter
   model = openrouter.load_model("mistral

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
