# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-30
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of natural language processing tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens, making it suitable for complex and lengthy text generation tasks.

### Technical Specifications and Use Cases
Mistral Small 4 is best utilized for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization. Its technical specifications include a context window of 262,144 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2023-12. The model's pricing is based on input and output tokens, with costs of $0.15 per 1M input tokens and $0.6 per 1M output tokens. Benchmarks for the model include an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its performance capabilities. With its diverse range of capabilities and competitive pricing, Mistral Small 4 is an attractive option for developers seeking a robust language model for their applications.

### Pricing and Cost Examples
The pricing model for Mistral Small 4 is straightforward, with costs calculated based on the number of input and output tokens. For example, 1,000 calls with an average of 500 tokens per call would cost $0.375, while 10,000 calls would cost $3.75, and 100,000 calls would cost $37.5. These cost examples demonstrate the scalability of the model's pricing, making it accessible for both small-scale

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
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and scalability of this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* **Input**: $0.15 per 1M tokens
* **Output**: $0.6 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
* **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
* **Batch API**: Although batch input is free, the cost savings come from reduced overhead and potentially faster processing times. However, the actual cost per token remains the same as the input cost.
* **Cost at Scale**: The cost examples provided are:
	+ 1,000 calls (avg 500 tokens): $0.375
	+ 10,000 calls: $3.75
	+ 100,000 calls: $37.5

#### Cost Calculation
To understand the cost structure, let's calculate the cost for a single API call with an average of 500 tokens:
* Input cost: 500 tokens / 1,000,000 tokens * $0.15 = $0.000075
* Output cost: Assuming an average output of 500 tokens (although the max output is 4,096 tokens), the output cost would be: 500 tokens / 1,000,000 tokens * $0.6 = $0.0003
* Total cost per call: $0.000075 (input) + $0.0003 (output) = $0.000

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Benchmark Analysis
The Mistral Small 4 model, provided by Mistralai, offers a unique set of capabilities and performance metrics. This analysis will delve into the benchmark performance of Mistral Small 4, focusing on the MMLU, HumanEval, and Arena ELO scores, and their implications for real-world use.

#### Benchmark Scores
* **MMLU (Massive Multitask Language Understanding) Score: 80.0** - The MMLU score measures a model's ability to perform a wide range of natural language processing tasks. A score of 80.0 indicates that Mistral Small 4 has a strong foundation in language understanding, making it suitable for tasks like text generation, chat, and analysis.
* **HumanEval Score: None** - HumanEval is a benchmark that evaluates a model's ability to generate code. The absence of a HumanEval score for Mistral Small 4 means that its coding capabilities, although listed as a capability, are not quantitatively measured in this benchmark.
* **LMSYS Arena ELO Score: 1200** - The LMSYS Arena ELO score is a measure of a model's overall performance in a competitive environment. An ELO score of 1200 suggests that Mistral Small 4 has a moderate level of performance, indicating it can handle a variety of tasks but may not excel in highly competitive or complex scenarios.

#### Real-World Implications
The benchmark scores suggest that Mistral Small 4 is well-suited for tasks that require strong language understanding, such as:
* Text generation
* Chat applications
* Analysis and summarization

However, the lack of a HumanEval score and a moderate

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral: Mistral Small 4 model, we will provide a general comparison framework that can be used to evaluate this model against other similar models in the market.

#### Pricing Comparison
The Mistral: Mistral Small 4 model is priced as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens

To compare this model with its top competitors, we would need to consider the pricing of similar models. However, since no direct competitors are listed, we can provide a general guideline for comparison:
* Look for models with similar capabilities, such as text generation, function calling, and structured outputs.
* Compare the pricing of these models based on input and output tokens.
* Consider the cost examples provided for the Mistral: Mistral Small 4 model:
	+ 1,000 calls (avg 500 tokens): $0.375
	+ 10,000 calls: $3.75
	+ 100,000 calls: $37.5

#### Performance Trade-offs
The Mistral: Mistral Small 4 model has the following performance characteristics:
* Context Window: 262,144 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2023-12
* Benchmarks:
	+ MMLU: 80.0
	+ LMSYS Arena ELO: 1200

When comparing this model with its top competitors, consider the following performance trade-offs:
* Context window size: A larger context window can support more complex and longer input sequences, but may increase the computational cost.
* Max output size: A larger max output size can support more detailed and longer output sequences, but may increase the computational cost.
* Knowledge cutoff: A more recent knowledge cutoff can provide more up-to-date information, but may not be available for all models.
* Benchmarks: Compare the performance of the models on various benchmarks, such as MMLU and LMSYS Arena ELO.

#### Choosing the Right Model
The Mistral: Mistral Small 4 model is best for:
* Chat
* Text generation
* Coding
* Analysis
* RAG pipelines
* Summarization

When choosing a model, consider the specific use case and requirements:
* If the use case requires a

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on 2024-01-01, this model is part of the standard tier and is not open source.

### Pricing Model
The pricing for Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its strong text generation capabilities, Mistral Small 4 is well-suited for chat applications, such as customer support chatbots or virtual assistants.
2. **Coding and Analysis**: Mistral Small 4's ability to perform function calling and structured outputs makes it a good fit for coding and analysis tasks, such as code review or data analysis.
3. **Summarization**: The model's text generation capabilities also make it suitable for summarization tasks, such as summarizing long documents or articles.
4. **RAG Pipelines**: Mistral Small 4's support for structured outputs and function calling makes it a good fit for RAG (Retrieve, Augment, Generate) pipelines, which involve retrieving information from a knowledge base, augmenting it, and generating text based on it.
5. **Streaming**: With its support for streaming, Mistral Small 4 can be used for real-time text generation and analysis applications, such as live chat or real-time data analysis.

### Code Integration Example with OpenRouter
Here is an example of how to integrate Mistral Small 4 with OpenRouter

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
