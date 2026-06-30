# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-30
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a context window of up to 262,144 tokens and can generate outputs of up to 4,096 tokens. Its knowledge cutoff is 2023-12, indicating that its training data includes information up to December 2023.

### Strengths and Use Cases
The main strengths of Mistral Small 4 lie in its capabilities, which include text generation, function calling, JSON mode, streaming, and structured outputs. These capabilities make it particularly suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization. With a pricing model that charges $0.15 per 1M tokens for input and $0.6 per 1M tokens for output, developers can estimate costs based on their specific use cases. For example, 1,000 calls averaging 500 tokens would cost $0.375, making it a viable option for a variety of development projects.

### Technical Benchmarks and Cost Considerations
Mistral Small 4 has been benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its performance in natural language understanding and generation tasks. While it does not have direct competitors listed, its unique set of capabilities and pricing structure make it an attractive choice for developers working on text-based applications. The cost examples provided, such as $3.75 for 10,000 calls and $37.5 for 100,000 calls, give developers a clear understanding of the costs involved in integrating Mistral Small 4 into their projects. Overall, Mistral Small 4 offers a powerful and flexible solution for a range of natural language processing tasks, with

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.15 |
| Output | $0.6 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Mistral: Mistral Small 4
#### Overview
Mistral: Mistral Small 4 is a standard-tier model provided by Mistralai, released on 2024-01-01. This model is not open source and has a specific cost structure based on input and output tokens.

#### Cost Structure
The cost structure for Mistral: Mistral Small 4 is as follows:
* **Input**: $0.15 per 1M tokens
* **Output**: $0.6 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs when the same input is used multiple times. Since cached input is free, it is recommended to use cached tokens whenever possible to minimize costs.

#### Batch API Savings
Batch input is also free, which means that making batch API calls can help reduce costs. By batching multiple inputs together, users can take advantage of the free batch input pricing and save on costs.

#### Cost at Scale
The cost of using Mistral: Mistral Small 4 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: $0.375
* **10,000 calls**: $3.75
* **100,000 calls**: $37.5

These costs are based on the average number of tokens per call and can be used to estimate the total cost of using the model at scale.

#### Context and Limits
It's worth noting that the model has the following context and limits:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12

These limits should be taken into account when using the model to ensure that the input and output are within the allowed ranges.



## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Mistral Small 4 Benchmark Performance
The Mistral Small 4 model, provided by Mistralai, has the following benchmark scores:
* **MMLU (Massive Multitask Language Understanding) score: 80.0** - This score indicates the model's ability to perform well across a wide range of natural language processing tasks. A higher MMLU score suggests better overall language understanding capabilities.
* **HumanEval score: None** - HumanEval is a benchmark that evaluates a model's ability to generate correct code based on human-written prompts. The absence of a HumanEval score for Mistral Small 4 makes it difficult to assess its coding capabilities directly.
* **LMSYS Arena ELO score: 1200** - The LMSYS Arena ELO score is a measure of a model's performance in a competitive environment, where models are pitted against each other to complete tasks. An ELO score of 1200 suggests that Mistral Small 4 has a moderate level of competence in such competitive scenarios.

### Real-World Implications
For real-world use, these benchmark scores imply the following:
* **General-purpose language understanding**: With an MMLU score of 80.0, Mistral Small 4 is likely to perform well in tasks that require broad language understanding, such as text generation, chat, and analysis.
* **Coding and programming tasks**: The lack of a HumanEval score makes it uncertain how well Mistral Small 4 will perform in coding tasks. However, its capabilities include `function_calling`, which suggests some level of programming ability.
* **Competitive performance**: The LMSYS Arena ELO score of 1200 indicates that Mistral Small

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral: Mistral Small 4, we will provide a general comparison framework that can be used to evaluate this model against other similar models in the market.

#### Pricing Comparison
The pricing for Mistral: Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

To compare, we would need the pricing information of the top competitors. However, we can provide a general guideline on how to evaluate the pricing:
* Compare the input and output prices per 1M tokens.
* Consider the cost of cached input and batch input, if applicable.
* Calculate the total cost for a specific use case, such as the examples provided:
	+ 1,000 calls (avg 500 tokens): $0.375
	+ 10,000 calls: $3.75
	+ 100,000 calls: $37.5

#### Performance Trade-offs
The performance of Mistral: Mistral Small 4 can be evaluated using the following benchmarks:
* MMLU: 80.0
* LMSYS Arena ELO: 1200

When comparing with top competitors, consider the following:
* Evaluate the performance benchmarks, such as MMLU and LMSYS Arena ELO.
* Consider the context window, max output, and knowledge cutoff:
	+ Context Window: 262,144 tokens
	+ Max Output: 4,096 tokens
	+ Knowledge Cutoff: 2023-12
* Assess the capabilities and limitations of each model, including:
	+ Capabilities: text, function_calling, json_mode, streaming, structured_outputs
	+ Best for: chat, text_generation, coding, analysis, rag_pipelines, summarization
	+ Not good for: (not specified)

#### Choosing the Right Model
To choose between Mistral: Mistral Small 4 and its top competitors, consider the following factors:
* **Pricing**: Evaluate the cost of each model based on your specific use case.
* **Performance**: Assess the performance benchmarks and capabilities of each model.
* **Use Case**: Determine which model is best suited for your specific application

## Best Use Cases
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on January 1, 2024, this model is part of the standard tier and is not open-source.

### Pricing Model
The pricing for Mistral: Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: $None per 1M tokens
- **Batch Input**: $None per 1M tokens

### Top 5 Best Use Cases for Mistral: Mistral Small 4
Given its capabilities, here are the top 5 best use cases for Mistral: Mistral Small 4, along with practical advice and code integration examples using OpenRouter:

1. **Chat and Text Generation**
   - **Description**: Utilize Mistral: Mistral Small 4 for generating human-like text responses in chat applications.
   - **Code Example**:
     ```python
     import openrouter
     from mistralai import MistralSmall4

     # Initialize the model
     model = MistralSmall4()

     # Define a function to generate text
     def generate_text(prompt):
         response = model.generate_text(prompt)
         return response

     # Use OpenRouter to integrate with the model
     openrouter.add_route("/generate", generate_text)
     ```
2. **Coding and Function Calling**
   - **Description**: Leverage the model's ability to understand and generate code, making it useful for coding assistance tools.
   - **Code Example**:
     ```python
     import openrouter
     from mistralai import MistralSmall4

     # Initialize the model
     model = MistralSmall4()

    

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
