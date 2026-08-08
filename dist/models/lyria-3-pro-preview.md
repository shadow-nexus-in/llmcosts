# Google: Lyria 3 Pro Preview API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-08
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Google: Lyria 3 Pro Preview
The Google: Lyria 3 Pro Preview, released by Google on 2024-01-01, is a standard-tier model that is not open source. This model is identified by the name `google/lyria-3-pro-preview`. From an architectural standpoint, the specifics of its internal design are not detailed in the provided data, but its capabilities and performance metrics offer insights into its strengths and potential applications. The model supports a range of capabilities including text, function calling, JSON mode, streaming, and structured outputs, making it versatile for various tasks.

### Technical Strengths and Use Cases
The Google: Lyria 3 Pro Preview demonstrates its main strengths through its performance benchmarks, such as achieving an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. These metrics, combined with its extensive context window of 1,048,576 tokens and a maximum output of 65,536 tokens, suggest the model is well-suited for complex and lengthy text generation, analysis, and coding tasks. Its capabilities make it an ideal choice for applications like chat, text generation, coding, analysis, RAG pipelines, and summarization. The model's pricing structure, with $0.0 per 1M tokens for both input and output, indicates a potentially cost-effective solution for developers, as evidenced by the cost examples provided, showing $0.0 costs for 1,000, 10,000, and 100,000 calls.

### Deployment and Limitations
Given its technical specifications and capabilities, the Google: Lyria 3 Pro Preview is positioned for a variety of use cases that benefit from its advanced text processing and generation capabilities. However, its knowledge cutoff of 2023-12 means that information or events after this date are not included in its training data, which could be a limitation for applications requiring very recent information. Despite the lack of direct

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.0 |
| Output | $0.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Google: Lyria 3 Pro Preview
#### Overview
The Google: Lyria 3 Pro Preview model is a standard, non-open-source model released by Google on 2024-01-01. This analysis will delve into the cost structure, usage scenarios, and scalability of this model.

#### Cost Structure
The pricing for Google: Lyria 3 Pro Preview is as follows:
* Input: **$0.0 per 1M tokens**
* Output: **$0.0 per 1M tokens**
* Cached Input: **$None per 1M tokens** (indicating no additional cost for cached inputs)
* Batch Input: **$None per 1M tokens** (suggesting no specific pricing for batch inputs)

Given the cost structure, it's essential to note that the model does not incur costs based on the number of tokens for input or output. This unique pricing model suggests that the primary consideration for cost optimization is not the volume of data processed but rather the number of API calls.

#### Using Cached Tokens
Since there is no additional cost for cached inputs (**$None per 1M tokens**), utilizing cached tokens can be beneficial when the same inputs are processed multiple times. However, the pricing structure does not differentiate between cached and non-cached inputs in terms of cost, making the decision to use cached tokens more about efficiency and less about direct cost savings.

#### Batch API Savings
The pricing does not specify savings for batch API calls (**$None per 1M tokens**), which implies that the cost, if any, is not directly tied to the batch size in terms of tokens. Any savings from batching would likely come from reduced overhead in making API calls, rather than a per-token cost reduction.

#### Cost at Scale
The cost examples provided show that the cost remains **$0.0** for:
* 1,000 calls (avg 500 tokens)
* 10,000 calls
*

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Google: Lyria 3 Pro Preview Benchmark Performance
#### Overview
The Google: Lyria 3 Pro Preview model, released by Google on 2024-01-01, is a standard-tier model that is not open source. This analysis will delve into the benchmark performance of this model, focusing on the MMLU, HumanEval, and Arena ELO scores, and their implications for real-world use.

#### Benchmark Scores
The model's benchmark scores are as follows:
- **MMLU (Massive Multitask Language Understanding)**: 80.0
- **HumanEval**: None
- **LMSYS Arena ELO**: 1200
- **GSM8K**: None

The MMLU score of 80.0 indicates the model's ability to understand and perform a wide range of natural language processing tasks. A higher MMLU score suggests better performance in tasks such as text classification, sentiment analysis, and question answering.

The HumanEval score is not available for this model, which means we cannot directly compare its coding abilities to other models.

The LMSYS Arena ELO score of 1200 provides insight into the model's competitive performance in a controlled environment. In the context of language models, a higher ELO score generally indicates better performance in tasks that require strategic thinking and adaptability.

#### Real-World Implications
The benchmark scores suggest that the Google: Lyria 3 Pro Preview model is capable of handling complex natural language processing tasks, as evidenced by its MMLU score. However, the lack of HumanEval score limits our understanding of its coding abilities.

In real-world applications, this model may excel in tasks such as:
* Text generation


## Competitor Comparison
### Comparison of Google: Lyria 3 Pro Preview with Top Competitors
Since there are no direct competitors listed for the Google: Lyria 3 Pro Preview, we will provide a general overview of its features, pricing, and performance. This will help users understand its capabilities and make informed decisions when choosing a model for their specific use cases.

#### Model Overview
The Google: Lyria 3 Pro Preview is a standard-tier model released by Google on 2024-01-01. It is not open-source and has the following key features:

* **Pricing**:
	+ Input: $0.0 per 1M tokens
	+ Output: $0.0 per 1M tokens
	+ Cached Input: $None per 1M tokens
	+ Batch Input: $None per 1M tokens
* **Context and Limits**:
	+ Context Window: 1,048,576 tokens
	+ Max Output: 65,536 tokens
	+ Knowledge Cutoff: 2023-12
* **Benchmarks**:
	+ MMLU: 80.0
	+ LMSYS Arena ELO: 1200
* **Capabilities**: text, function_calling, json_mode, streaming, structured_outputs
* **Best For**: chat, text_generation, coding, analysis, rag_pipelines, summarization

#### Performance Trade-Offs
Since there are no direct competitors, we will discuss the general trade-offs of using the Google: Lyria 3 Pro Preview:

* **Free Usage**: The model offers free usage for input and output tokens, making it an attractive option for users with limited budgets.
* **Large Context Window**: The model's context window of 1,048,576 tokens allows for processing long sequences of text, making it suitable for tasks like text generation and analysis.
* **Limited Knowledge Cutoff**: The model's knowledge cutoff of 2023-12 may limit its ability to provide up-to-date information on recent events or developments.

#### When to Choose Google: Lyria 3 Pro Preview
Based on its features and capabilities, the Google: Lyria 3 Pro Preview is suitable for:

* **Chat and Text Generation**: The model's free usage and large context window make it an excellent choice for chat and text generation tasks.
* **Coding and Analysis**: The model's function_calling and structured_outputs capabilities make it suitable for coding and

## Best Use Cases
### Introduction to Google: Lyria 3 Pro Preview
The Google: Lyria 3 Pro Preview model, released on 2024-01-01, is a powerful tool with a wide range of capabilities, including text generation, function calling, and structured outputs. With its large context window of 1,048,576 tokens and max output of 65,536 tokens, it is well-suited for various applications.

### Top 5 Best Use Cases for Google: Lyria 3 Pro Preview
Based on its capabilities and benchmarks, here are the top 5 best use cases for the Google: Lyria 3 Pro Preview model:

1. **Chat and Text Generation**: With its high MMLU benchmark score of 80.0, this model is ideal for generating human-like text and engaging in conversations.
2. **Coding and Analysis**: The model's ability to perform function calling and generate structured outputs makes it suitable for coding tasks, such as code completion and code review.
3. **Summarization and RAG Pipelines**: The Google: Lyria 3 Pro Preview model can be used to summarize long pieces of text and integrate with RAG (Retrieve, Augment, Generate) pipelines for more complex tasks.
4. **Streaming and Real-time Applications**: The model's support for streaming and JSON mode makes it a good fit for real-time applications, such as live chatbots or streaming data analysis.
5. **Research and Development**: With its high context window and max output, this model can be used for research and development purposes, such as exploring new language models and fine-tuning existing ones.

### Code Integration Examples with OpenRouter
To integrate the Google: Lyria 3 Pro Preview model with OpenRouter, you can use the following code examples:

```python
import openrouter

# Initialize the OpenRouter client
client = openrouter.Client()

# Define the model and its parameters
model_name = "google/lyria-3

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: estimated*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
