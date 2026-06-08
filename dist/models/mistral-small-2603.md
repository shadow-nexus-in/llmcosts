# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-08
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of tasks, including text generation, coding, analysis, and summarization, thanks to its capabilities in text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens, making it suitable for complex and lengthy tasks.

### Technical Specifications and Use Cases
The model's technical specifications highlight its robustness, with a context window of 262,144 tokens and a maximum output of 4,096 tokens. The knowledge cutoff is 2023-12, indicating that the model's training data is current up to December 2023. Mistral Small 4 excels in tasks such as chat, text generation, coding, analysis, RAG pipelines, and summarization. Its performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, demonstrating its capabilities in natural language understanding and generation. However, its limitations and areas where it is not well-suited are not explicitly listed, suggesting a broad applicability with careful consideration of its context and output limits.

### Pricing and Cost Considerations
The pricing model for Mistral Small 4 is based on input and output tokens, with costs of $0.15 per 1M input tokens and $0.6 per 1M output tokens. There are no additional costs for cached input or batch input. Example costs include $0.375 for 1,000 calls averaging 500 tokens, $3.75 for 10,000 calls, and $37.5 for 100,000

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
Mistral Small 4, provided by Mistralai, is a standard-tier model released on 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$0.00 per 1M tokens** (free)
* Batch Input: **$0.00 per 1M tokens** (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following strategies:
* **Cached Tokens**: Utilize cached input tokens whenever possible, as they are free. This is ideal for applications with repetitive or similar input patterns.
* **Batch API Calls**: Leverage batch input to reduce the number of API calls, as batch input is free. This is suitable for applications that can process multiple inputs simultaneously.

#### Cost at Scale
The cost of using Mistral Small 4 at various scales is as follows:
* **1,000 API calls** (avg 500 tokens): **$0.375**
* **10,000 API calls**: **$3.75**
* **100,000 API calls**: **$37.50**

These costs demonstrate a linear scaling of expenses with the number of API calls, indicating that the cost per call remains constant.

#### Conclusion
Mistral Small 4 offers a competitive pricing structure, particularly when utilizing cached input tokens and batch API calls. By understanding the cost structure and optimal usage scenarios, developers can effectively integrate this model into their applications while minimizing expenses. As the number of API calls increases, the total cost scales linearly, making it essential to consider these costs when designing and deploying applications that rely on Mistral Small 

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Mistral: Mistral Small 4 Benchmark Performance
#### Overview
Mistral: Mistral Small 4 is a standard-tier model provided by Mistralai, released on January 1, 2024. It is not open-source and has a specific pricing structure based on input and output tokens.

#### Pricing Structure
The pricing for Mistral: Mistral Small 4 is as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens
- Cached Input: $None per 1M tokens
- Batch Input: $None per 1M tokens

#### Benchmark Performance
The model's performance is measured through several benchmarks:
- **MMLU (Massive Multitask Language Understanding)**: 80.0
  - MMLU measures a model's ability to understand and perform a wide range of tasks. A higher MMLU score indicates better performance across multiple tasks. With a score of 80.0, Mistral: Mistral Small 4 demonstrates a good level of understanding and performance across various tasks.
- **HumanEval**: None
  - HumanEval is a benchmark that evaluates a model's ability to write and execute code based on human-written tests. The lack of a HumanEval score for Mistral: Mistral Small 4 makes it difficult to assess its coding capabilities directly.
- **LMSYS Arena ELO**: 1200
  - The LMSYS Arena ELO score is a measure of a model's competitive performance in a controlled environment, similar to how chess players are ranked. An ELO score of 1200 suggests that Mistral: Mistral Small 4

## Competitor Comparison
### Mistral Small 4 Comparison
Since there are no direct competitors listed for the Mistral Small 4 model, we will provide a general overview of its features, pricing, and performance. This will help users understand when to choose this model and what trade-offs to expect.

#### Model Overview
The Mistral Small 4 model is a standard, non-open-source model provided by Mistralai, released on January 1, 2024. It has the following key features:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12
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

#### Choosing the Mistral Small 4 Model
Given the lack of direct competitors, the decision to choose the Mistral Small 4 model will depend on your specific use case and requirements. Consider the following factors:
* **Context Window**: If you need to process large amounts of text, the Mistral Small 4 model's context window of 262,144 tokens may be suitable.
* **Max Output**: If you need to generate long outputs, the model's max output of 4,096 tokens may be sufficient.
* **Capabilities**: If you need a model that supports text, function_calling, json_mode, streaming, and structured_outputs, the Mistral Small 4 model may be a good choice.
* **Pricing**: If you are looking for a model with a relatively low input

## Best Use Cases
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4 is a powerful language model provided by Mistralai, released on 2024-01-01. This model is classified as a standard, non-open source model. With its impressive capabilities, including text, function calling, JSON mode, streaming, and structured outputs, it is best suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization.

### Pricing and Cost Considerations
The pricing for Mistral: Mistral Small 4 is as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens
- Cached Input: $None per 1M tokens
- Batch Input: $None per 1M tokens

To give you a better understanding of the costs involved, consider the following examples:
- 1,000 calls (avg 500 tokens): $0.375
- 10,000 calls: $3.75
- 100,000 calls: $37.5

### Top 5 Best Use Cases for Mistral: Mistral Small 4
Given its capabilities and pricing, here are the top 5 best use cases for Mistral: Mistral Small 4:

1. **Chat Applications**: With its strong text generation capabilities, Mistral: Mistral Small 4 is well-suited for chat applications, including customer support and virtual assistants.
2. **Text Summarization**: The model's ability to process large amounts of text and generate concise summaries makes it an excellent choice for text summarization tasks.
3. **Coding and Analysis**: Mistral: Mistral Small 4's function calling and structured outputs capabilities make it a great tool for coding and analysis tasks, such as code completion and data analysis.
4. **RAG Pipelines**: The model's support for RAG pipelines makes it an

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
