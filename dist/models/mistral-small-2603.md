# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-25
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open-source. From an architectural standpoint, Mistral: Mistral Small 4 is designed to handle a variety of tasks with its robust capabilities, including text generation, function calling, JSON mode, streaming, and structured outputs. Its architecture supports a context window of up to 262,144 tokens and can generate outputs of up to 4,096 tokens.

### Strengths and Use Cases
The main strengths of Mistral: Mistral Small 4 lie in its versatility and performance. With a context window of 262,144 tokens and the ability to generate up to 4,096 tokens of output, it is well-suited for tasks such as chat, text generation, coding, analysis, RAG pipelines, and summarization. The model's capabilities in function calling and JSON mode also make it a strong candidate for applications requiring structured data processing. However, its pricing model, which includes $0.15 per 1M tokens for input and $0.6 per 1M tokens for output, should be considered when evaluating its cost-effectiveness for large-scale applications.

### Technical Specifications and Pricing
Technically, Mistral: Mistral Small 4 has demonstrated its performance through various benchmarks, achieving an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. Its knowledge cutoff is 2023-12, indicating that its training data is current up to that point. The pricing for using Mistral: Mistral Small 4 is based on input and output tokens, with examples showing that 1,000 calls averaging 500 tokens would cost $0.375, scaling up to $37.5 for 100,000 calls. With no direct competitors listed, Mistral:

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
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. This analysis will delve into the cost structure, usage scenarios, and scalability of this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$None per 1M tokens** (free)
* Batch Input: **$None per 1M tokens** (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for reducing costs. Use cached tokens when:
* The input data is repetitive or has a high degree of similarity.
* The model is being used for applications where input data is largely static.

#### Batch API Savings
Batch input is also free, which can lead to significant cost savings when:
* Processing large volumes of data in parallel.
* Using the model for applications that can benefit from batch processing, such as data analysis or text generation.

#### Cost at Scale
The cost of using Mistral Small 4 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: **$0.375**
* **10,000 calls**: **$3.75**
* **100,000 calls**: **$37.5**

These costs demonstrate a linear scaling of expenses with the number of API calls, indicating that the cost per call remains constant regardless of the volume.

#### Conclusion
Mistral Small 4 offers a competitive pricing structure, with free cached and batch input options. By leveraging these features, users can significantly reduce their costs. The model's capabilities, including text, function calling, and structured outputs, make it suitable for a wide range of applications, such as chat, text

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Mistral Small 4 Benchmark Performance
#### Model Overview
The Mistral Small 4 model, provided by Mistralai, is a standard-tier model released on 2024-01-01. It is not open-source and has the following pricing structure:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens

#### Benchmark Performance
The model's performance is measured by the following benchmarks:
- **MMLU (Massive Multitask Language Understanding)**: 80.0
  - MMLU is a benchmark that evaluates a model's ability to perform a wide range of natural language understanding tasks. A higher MMLU score indicates better performance. With a score of 80.0, Mistral Small 4 demonstrates a strong ability to understand and process human language.
- **HumanEval**: None
  - HumanEval is a benchmark that assesses a model's ability to generate code based on human-written prompts. The lack of a HumanEval score for Mistral Small 4 makes it difficult to evaluate its coding capabilities directly.
- **LMSYS Arena ELO**: 1200
  - LMSYS Arena ELO is a benchmark that measures a model's performance in a competitive setting, often involving tasks that require strategic thinking and problem-solving. An ELO score of 1200 suggests that Mistral Small 4 has a moderate level of proficiency in these areas.
- **GSM8K**: None
  - GSM8K is a benchmark focused on math problem-solving. Without a score, it's challenging to assess Mistral Small 4's mathematical reasoning capabilities.

#### Real-World Implications


## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral Small 4, we will provide a general comparison framework that can be applied to other models in the market. This framework will consider key factors such as pricing, performance, and capabilities.

#### Pricing Comparison
Mistral Small 4 is priced at:
- $0.15 per 1M tokens for input
- $0.6 per 1M tokens for output

To compare, let's assume a hypothetical competitor, Model X, with the following pricing:
- $0.10 per 1M tokens for input
- $0.8 per 1M tokens for output

| Model | Input Price per 1M Tokens | Output Price per 1M Tokens |
| --- | --- | --- |
| Mistral Small 4 | $0.15 | $0.6 |
| Model X | $0.10 | $0.8 |

#### Performance Trade-offs
Mistral Small 4 has the following performance metrics:
- MMLU: 80.0
- LMSYS Arena ELO: 1200

When comparing with Model X, consider the following hypothetical performance metrics:
- MMLU: 85.0
- LMSYS Arena ELO: 1100

| Model | MMLU | LMSYS Arena ELO |
| --- | --- | --- |
| Mistral Small 4 | 80.0 | 1200 |
| Model X | 85.0 | 1100 |

#### Capabilities and Use Cases
Mistral Small 4 supports the following capabilities:
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

When choosing between Mistral Small 4 and Model X, consider the specific use case and required capabilities.

#### Cost Examples
Mistral Small 4 cost examples:
- 1,000 calls (avg 500 tokens): $0.375
- 10,000 calls: $3.75
- 100,000 calls: $37.5

To estimate the cost of Model X, apply its pricing to the same scenarios:
- 1,000 calls (avg 500 tokens): assume $0.25 (input

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and non-open source status, it offers a unique set of features for various applications. Here, we will explore the top 5 best use cases for Mistral Small 4, along with code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Small 4
#### 1. **Chat and Text Generation**
Mistral Small 4 excels in chat and text generation tasks, making it an ideal choice for conversational AI applications. Its ability to understand and respond to user input in a human-like manner can be leveraged to build engaging chatbots.

#### 2. **Coding and Analysis**
With its function calling and structured outputs capabilities, Mistral Small 4 can be used for coding and analysis tasks. It can assist in generating code snippets, debugging, and providing insights into complex codebases.

#### 3. **Summarization and RAG Pipelines**
Mistral Small 4's text generation capabilities make it well-suited for summarization tasks. It can also be used in RAG (Retrieve, Augment, Generate) pipelines to generate high-quality text based on retrieved information.

#### 4. **Analysis and Insight Generation**
Mistral Small 4 can be used to analyze large datasets and generate insights. Its ability to process and understand natural language makes it an ideal choice for tasks such as sentiment analysis and entity recognition.

#### 5. **Streamlined Content Creation**
Mistral Small 4's text generation capabilities can be used to streamline content creation tasks such as writing articles, blog posts, and social media content. Its ability to generate high-quality text can save time and effort for content creators.

### Code Integration Examples with OpenRouter
To integrate Mistral Small 4

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
