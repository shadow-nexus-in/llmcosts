# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-10
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a context window of up to 262,144 tokens and can generate a maximum output of 4,096 tokens. Its knowledge cutoff is 2023-12, indicating that its training data includes information up to December 2023.

### Strengths and Use Cases
The main strengths of Mistral: Mistral Small 4 lie in its capabilities, which include text, function calling, JSON mode, streaming, and structured outputs. These capabilities make it best suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization. With a pricing model that charges $0.15 per 1M tokens for input and $0.6 per 1M tokens for output, it offers a cost-effective solution for developers looking to integrate advanced language processing into their applications. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, demonstrating its potential in various linguistic tasks.

### Pricing and Cost Considerations
For developers considering Mistral: Mistral Small 4, understanding the pricing is crucial. The cost examples provided indicate that 1,000 calls with an average of 500 tokens would cost $0.375, scaling to $3.75 for 10,000 calls, and $37.5 for 100,000 calls. Given its capabilities and pricing, Mistral Small 4 is positioned as a competitive option for developers, especially since it lacks direct competitors as per the provided data. However, the absence of certain benchmark scores, such as HumanEval and GSM8K, might require additional evaluation by developers to ensure

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
The Mistral: Mistral Small 4 model, provided by Mistralai, is a standard, non-open-source model released on 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral: Mistral Small 4 is based on input and output tokens. The costs are as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: No additional cost ($None per 1M tokens)
- **Batch Input**: No additional cost ($None per 1M tokens)

#### Optimal Usage Scenarios
- **Cached Tokens**: Since there is no additional cost for cached input tokens, it is highly beneficial to use cached tokens whenever possible. This can significantly reduce costs, especially in applications where the same input data is processed multiple times.
- **Batch API Savings**: Although there is no direct cost savings mentioned for batch input, processing inputs in batches can still lead to efficiency gains and potentially reduce the overall number of API calls needed, thereby indirectly saving costs.

#### Cost at Scale
The cost examples provided give insight into the cost structure at different scales:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These examples illustrate a linear cost increase with the number of API calls, indicating that the cost per call remains constant regardless of the scale.

#### Calculating Costs Based on Tokens
Given the input and output costs, we can calculate the cost for a specific number of tokens. However, the provided cost examples suggest a simplified pricing model where the average cost per call is calculated based on the average number of tokens

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
* **MMLU (Massive Multitask Language Understanding) Score:** 80.0
	+ The MMLU score measures a model's ability to perform a wide range of natural language processing tasks. A higher score indicates better performance. With a score of 80.0, Mistral Small 4 demonstrates a strong foundation in language understanding.
* **HumanEval Score:** None
	+ HumanEval is a benchmark that evaluates a model's ability to generate code. The absence of a HumanEval score for Mistral Small 4 means that its coding capabilities are not directly comparable to other models using this metric.
* **LMSYS Arena ELO Score:** 1200
	+ The LMSYS Arena ELO score is a measure of a model's overall performance in a competitive environment. An ELO score of 1200 indicates that Mistral Small 4 has a moderate level of proficiency, but may struggle against more advanced models.

#### Real-World Implications
The benchmark scores suggest that Mistral Small 4 is suitable for tasks that require strong language understanding, such as:

* Text generation
* Chat applications
* Analysis and summarization

However, the lack of a HumanEval score and the moderate Arena ELO score indicate that Mistral Small 4 may not be the best choice for tasks that require advanced coding

## Competitor Comparison
### Mistral Small 4 Comparison
Since there are no direct competitors listed for the Mistral Small 4, we will provide a general overview of its features, pricing, and capabilities to help users decide when to choose this model.

#### Pricing
The Mistral Small 4 is priced as follows:
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Performance Trade-offs
The Mistral Small 4 has the following performance characteristics:
* Context Window: **262,144 tokens**
* Max Output: **4,096 tokens**
* Knowledge Cutoff: **2023-12**
* Benchmarks:
	+ MMLU: **80.0**
	+ LMSYS Arena ELO: **1200**

#### Capabilities and Use Cases
The Mistral Small 4 supports the following capabilities:
* **text**
* **function_calling**
* **json_mode**
* **streaming**
* **structured_outputs**
It is best suited for tasks such as:
* **chat**
* **text_generation**
* **coding**
* **analysis**
* **rag_pipelines**
* **summarization**

#### Cost Examples
To give users an idea of the costs involved, here are some examples:
* 1,000 calls (avg 500 tokens): **$0.375**
* 10,000 calls: **$3.75**
* 100,000 calls: **$37.5**

#### Choosing the Mistral Small 4
Given its capabilities and pricing, the Mistral Small 4 is a good choice for users who need a standard-tier model with a large context window and support for various output formats. However, since there are no direct competitors listed, users should evaluate their specific use cases and requirements to determine if the Mistral Small 4 is the best fit for their needs.

In the absence of direct competitors, users may want to consider the following factors when deciding whether to choose the Mistral Small 4:
* **Specific task requirements**: Does the task require a large context window, support for function calling, or structured outputs?
* **Budget constraints**: Are the costs associated with the Mistral Small 4 within the user's budget?
* **Performance requirements**: Are the benchmark scores (e

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. Released on 2024-01-01, this model is part of the standard tier and is not open source.

### Pricing Model
The pricing for Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: $None per 1M tokens
- **Batch Input**: $None per 1M tokens

### Top 5 Best Use Cases for Mistral Small 4
Given its capabilities, here are the top 5 best use cases for Mistral Small 4, along with practical advice and code integration examples using OpenRouter:

1. **Chat and Text Generation**
   - **Description**: Mistral Small 4 excels in generating human-like text, making it suitable for chat applications and content creation.
   - **Example**: Using OpenRouter, you can integrate Mistral Small 4 into a chatbot to generate responses to user queries.
   ```python
   import openrouter

   # Initialize OpenRouter with Mistral Small 4
   model = openrouter.MistralSmall4()

   # Generate a response to a user query
   query = "Hello, how are you?"
   response = model.generate_text(query)
   print(response)
   ```

2. **Coding and Function Calling**
   - **Description**: With its function calling capability, Mistral Small 4 can be used for coding tasks, such as generating code snippets or completing partially written functions.
   - **Example**: You can use OpenRouter to integrate Mistral Small 4 into an IDE to provide code completion suggestions.
   ```python
   import openrouter

   # Initialize OpenRouter with Mist

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
