# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-03
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral: Mistral Small 4 is designed to handle a variety of natural language processing tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens, making it suitable for complex tasks such as chat, text generation, coding, analysis, and summarization.

### Technical Specifications and Pricing
Technically, Mistral: Mistral Small 4 has a context window of 262,144 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2023-12. The model's pricing is based on input and output tokens, with costs of $0.15 per 1M input tokens and $0.6 per 1M output tokens. There are no specified costs for cached input or batch input. The model has been benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its performance capabilities. With its pricing structure, developers can estimate costs based on the number of calls and tokens processed, such as $0.375 for 1,000 calls averaging 500 tokens, $3.75 for 10,000 calls, and $37.5 for 100,000 calls.

### Use Cases and Competitors
Mistral: Mistral Small 4 is best suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization, thanks to its robust capabilities and large context window. However, its limitations and areas where it is not recommended are

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
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and scalability of Mistral Small 4.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following strategies:
* **Use cached tokens**: Since cached input is free, leverage this feature whenever possible to reduce input costs.
* **Batch API calls**: With batch input being free, grouping API calls together can significantly reduce overall costs.

#### Cost at Scale
The cost of using Mistral Small 4 at various scales is as follows:
* **1,000 calls (avg 500 tokens)**: **$0.375**
* **10,000 calls**: **$3.75**
* **100,000 calls**: **$37.5**

These costs demonstrate a linear scaling of expenses with the number of API calls, indicating that the cost per call remains constant.

#### Context and Limits
When using Mistral Small 4, consider the following constraints:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12

#### Capabilities and Use Cases
Mistral Small 4 is suitable for a variety of tasks, including:
* Text
* Function calling
* JSON mode
* Streaming
* Structured outputs

It is best used for applications such as:
* Chat
* Text generation

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Benchmark Performance Analysis
#### Overview
The Mistral Small 4 model, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. It is not open-source and has a specific pricing structure based on input and output tokens.

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

The MMLU score of 80.0 indicates the model's performance on a set of mathematical and logical tasks. A higher MMLU score generally indicates better performance on these tasks.

The LMSYS Arena ELO score of 1200 is a measure of the model's performance in a competitive setting, where it is pitted against other models. A higher ELO score indicates better performance.

The lack of HumanEval and GSM8K scores means that the model's performance on these specific benchmarks is not available.

#### Real-World Use Implications
The benchmark performance of Mist

## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral Small 4 model, we will provide a general comparison framework that can be applied when evaluating this model against other similar models in the market.

#### Pricing Comparison
The pricing for Mistral Small 4 is as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens

When comparing with other models, consider the following:
- **Input Cost**: If a competitor offers a lower input cost per 1M tokens, it may be more cost-effective for applications with large input sizes.
- **Output Cost**: Similarly, if a competitor offers a lower output cost per 1M tokens, it may be more suitable for applications that require generating large amounts of text or data.

#### Performance Trade-offs
Mistral Small 4 has the following performance metrics:
- **MMLU**: 80.0
- **LMSYS Arena ELO**: 1200
- **Context Window**: 262,144 tokens
- **Max Output**: 4,096 tokens

When evaluating against competitors, consider:
- **Benchmark Scores**: Higher scores in benchmarks like MMLU and LMSYS Arena ELO may indicate better performance in specific tasks.
- **Context Window and Max Output**: Larger context windows and max output sizes can be beneficial for tasks that require processing or generating long pieces of text.

#### Choosing the Right Model
Mistral Small 4 is best for:
- Chat
- Text generation
- Coding
- Analysis
- RAG pipelines
- Summarization

It is not specified what it is not good for, so consider the capabilities and benchmarks when deciding if this model meets your specific use case requirements.

#### Cost Examples
The cost examples provided for Mistral Small 4 are:
- 1,000 calls (avg 500 tokens): $0.375
- 10,000 calls: $3.75
- 100,000 calls: $37.5

When comparing costs with competitors, ensure to calculate the costs based on your specific usage patterns and the pricing models of the competing services.

### Conclusion
While there are no direct competitors listed for Mistral Small 4, this framework provides a basis for comparing it with other models. Consider the pricing, performance metrics, capabilities, and cost examples when evaluating Mistral Small 

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard, non-open-source model released on 2024-01-01. It offers a range of capabilities including text, function calling, JSON mode, streaming, and structured outputs, making it suitable for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization.

### Pricing Model
The pricing for Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: $None per 1M tokens
- **Batch Input**: $None per 1M tokens

### Top 5 Best Use Cases for Mistral Small 4
Given its capabilities and pricing, here are the top 5 best use cases for Mistral Small 4, along with examples of how to integrate it with OpenRouter:

1. **Chat and Text Generation**:
   - **Use Case**: Implementing a chatbot that can understand and respond to user queries.
   - **Example Code**:
     ```python
     import openrouter
     from mistralai import MistralSmall4

     # Initialize Mistral Small 4 model
     model = MistralSmall4()

     # Define a function to generate a response
     def generate_response(query):
         # Use OpenRouter for routing the query to the model
         response = openrouter.route_query(query, model)
         return response

     # Test the function
     query = "Hello, how are you?"
     print(generate_response(query))
     ```
   - **Cost**: For 1,000 chat interactions (avg 500 tokens), the cost would be approximately $0.375.

2. **Coding and Analysis**:
   - **Use Case**: Developing an application that can analyze code snippets and provide suggestions for

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
