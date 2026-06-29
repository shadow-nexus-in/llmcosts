# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-29
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of tasks, including text generation, coding, analysis, and more, thanks to its capabilities in text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens.

### Technical Specifications and Use Cases
The model's technical specifications highlight its robustness and flexibility. With a context window of 262,144 tokens and a maximum output of 4,096 tokens, Mistral Small 4 is well-suited for complex tasks such as chat, text generation, coding, and analysis. Its capabilities in function calling, JSON mode, and streaming further enhance its utility in real-world applications. The model's knowledge cutoff is 2023-12, indicating that its training data is current up to that point. Benchmarks show an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, demonstrating its performance capabilities. Mistral Small 4 is best utilized for tasks that require in-depth text understanding and generation, such as chatbots, content creation, and code completion.

### Pricing and Cost Considerations
The pricing model for Mistral Small 4 is based on input and output tokens. Developers are charged $0.15 per 1M input tokens and $0.6 per 1M output tokens. There are no charges for cached input or batch input. To give developers a better understanding of the costs involved, examples are provided: 1,000 calls averaging 500 tokens cost $0.375, while 10,000 calls cost $3.75, and 

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
Mistral Small 4, provided by Mistralai, is a standard, non-open-source model released on 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and scaling costs for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

This structure indicates that the primary cost drivers are the input and output token counts. Cached and batch inputs are not charged, suggesting that optimizing for these can significantly reduce costs.

#### Optimal Usage Scenarios
- **Cached Tokens**: Since cached input tokens are free, it's highly beneficial to use cached tokens whenever possible. This can be particularly useful in applications where the same input data is processed multiple times, such as in chatbots or text analysis pipelines.
- **Batch API Savings**: Although the pricing does not specify a direct cost savings for batch inputs, the fact that batch inputs are free suggests that processing inputs in batches can help reduce overall costs by minimizing the number of API calls.

#### Cost at Scale
The provided cost examples give insight into the cost structure at different scales:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These examples illustrate a linear scaling of costs with the number of API calls, indicating that the cost per call remains constant regardless of the volume.

#### Calculating Costs
To understand the cost implications better, let's consider the cost components:
- For every 1M input tokens, the cost is $0.15.
-

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Mistral Small 4 Benchmark Performance
The Mistral Small 4 model, provided by Mistralai, demonstrates the following benchmark performance:
* **MMLU (Massive Multitask Language Understanding) Score: 80.0** - This score indicates the model's ability to understand and generate human-like text across a wide range of tasks and topics. A higher MMLU score suggests better performance in tasks that require a broad understanding of language.
* **HumanEval Score: None** - HumanEval is a benchmark that evaluates a model's ability to generate correct and functional code. The absence of a HumanEval score for Mistral Small 4 makes it difficult to assess its coding capabilities directly.
* **LMSYS Arena ELO Score: 1200** - The LMSYS Arena ELO score is a measure of a model's performance in a competitive environment, where it is pitted against other models. An ELO score of 1200 suggests that Mistral Small 4 has a moderate level of competence in tasks that require strategic thinking and adaptability.

### Real-World Implications
Given its benchmark performance, Mistral Small 4 can be expected to perform well in real-world applications that require:
* **Text generation**: With a high MMLU score, Mistral Small 4 is likely to generate coherent and contextually relevant text.
* **Chat and conversation**: The model's capabilities in text generation and its context window of 262,144 tokens make it suitable for engaging in natural-sounding conversations.
* **Coding and analysis**: Although the HumanEval score is not available, the model's support for function calling and structured outputs suggests that it may be useful for coding tasks, especially

## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral Small 4 model, we will provide a general analysis of its features, pricing, and performance trade-offs. This will help users understand when to choose the Mistral Small 4 model and what to expect from it.

#### Model Overview
The Mistral Small 4 model is a standard-tier model provided by Mistralai, released on January 1, 2024. It is not open-source.

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
It is best suited for:
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
Since there are no direct competitors listed, the decision to choose the Mistral Small 4 model depends on the specific use case and requirements. Consider the following factors:
* **Context Window**: If your application requires a large context window (262,144 tokens), the Mistral Small 4 model may be a good choice.
* **Output Size**: If your application requires a moderate output size (up to 4,096 tokens), the Mistral Small 4 model may be suitable.
* **Pricing**: If your budget is limited,

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on 2024-01-01, this model is part of the standard tier and is not open-source.

### Pricing Model
The pricing for Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its ability to generate human-like text, Mistral Small 4 is well-suited for chat applications, such as customer support chatbots or virtual assistants.
2. **Coding and Analysis**: Mistral Small 4's function calling and structured outputs capabilities make it a great tool for coding and analysis tasks, such as code completion, code review, and data analysis.
3. **Summarization**: Mistral Small 4's text generation capabilities also make it suitable for summarization tasks, such as summarizing long documents or articles.
4. **RAG Pipelines**: Mistral Small 4's ability to handle structured outputs makes it a great tool for RAG (Retrieval-Augmented Generation) pipelines, which involve retrieving information from a database and generating text based on that information.
5. **Streaming**: Mistral Small 4's streaming capability makes it suitable for real-time applications, such as live chat or live text generation.

### Code Integration Example with OpenRouter
Here is an example of how to integrate Mistral Small 4 with OpenRouter:
```python
import openrouter



## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
