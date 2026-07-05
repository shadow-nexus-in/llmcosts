# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-05
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance between performance and cost. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, this model is well-suited for a variety of tasks, including coding, analysis, and content generation. The model's capabilities include text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Architecture and Strengths
The architecture of Mistral Medium 3 is not publicly disclosed, but its performance can be gauged through its benchmarks. It achieves an MMLU score of 80.0, a HumanEval score of 77.5, and an LMSYS Arena ELO rating of 1200. These scores indicate that the model excels in tasks that require complex reasoning and problem-solving. The model's primary strengths lie in its ability to handle long-range dependencies and generate coherent text, making it ideal for tasks such as summarization, analysis, and content generation. With a pricing structure of $0.4 per 1M input tokens and $2.0 per 1M output tokens, Mistral Medium 3 offers a competitive option for developers who require a balance between performance and cost.

### Use Cases and Cost Considerations
Mistral Medium 3 is best suited for tasks that require complex reasoning, such as coding, analysis, and content generation. It is not recommended for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms. The cost of using Mistral Medium 3 can be estimated using the provided pricing structure. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 10,000 calls would cost $12.0, and 100

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.4 |
| Output | $2.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Mistral Medium 3
#### Overview
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and scalability of this model.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
* **Input**: $0.4 per 1M tokens
* **Output**: $2.0 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
* **Cached Tokens**: Since cached input tokens are free, it's highly beneficial to utilize cached tokens whenever possible. This can significantly reduce costs, especially for applications with repetitive or similar input patterns.
* **Batch API Savings**: Although batch input is free, the primary cost savings come from reducing the number of API calls. By batching inputs, you can minimize the overhead costs associated with individual API calls, leading to more efficient and cost-effective processing.

#### Cost at Scale
The cost of using Mistral Medium 3 at various scales is as follows:
* **1,000 calls (avg 500 tokens)**: $1.2
* **10,000 calls**: $12.0
* **100,000 calls**: $120.0

These costs demonstrate a linear scaling of expenses with the number of API calls. This linearity suggests that the cost per call remains constant, making it easier to predict and budget for large-scale applications.

#### Comparison with Competitors
Mistral Medium 3's pricing is competitive, especially considering its capabilities and performance benchmarks. For example:
* **Claude 3.5 Haiku**: $0.8/1M input, $4.0/1M output
* **GPT-4o Mini

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Medium 3 Benchmark Performance Analysis
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. The model's pricing is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens

#### Benchmark Scores
The model's performance is measured by the following benchmark scores:
* **MMLU (80.0)**: The MMLU (Measuring Massive Multitask Language Understanding) score evaluates a model's ability to understand and generate human-like text across a wide range of tasks. A higher score indicates better performance. With a score of 80.0, Mistral Medium 3 demonstrates strong language understanding capabilities.
* **HumanEval (77.5)**: The HumanEval score assesses a model's ability to generate code that is both correct and readable. A higher score indicates better coding capabilities. With a score of 77.5, Mistral Medium 3 shows promising coding abilities.
* **LMSYS Arena ELO (1200)**: The LMSYS Arena ELO score measures a model's overall performance in a competitive environment, with higher scores indicating better performance. An ELO score of 1200 suggests that Mistral Medium 3 is a strong competitor in the mid-tier range.

#### Real-World Implications
The benchmark scores indicate that Mistral Medium 3 is well-suited for tasks that require:
* Strong language understanding (e.g., text analysis, summarization)
* Coding capabilities (e.g.,

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will analyze its pricing, performance, and capabilities against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

#### Pricing Comparison
The pricing for each model is as follows:
* **Mistral Medium 3**:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* **Claude 3.5 Haiku**:
	+ Input: $0.8 per 1M tokens
	+ Output: $4.0 per 1M tokens
* **GPT-4o Mini**:
	+ Input: $0.15 per 1M tokens
	+ Output: $0.6 per 1M tokens

Mistral Medium 3 is priced lower than Claude 3.5 Haiku but higher than GPT-4o Mini for both input and output tokens.

#### Performance Trade-offs
The performance of each model can be evaluated based on the provided benchmarks:
* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

While the benchmarks for Claude 3.5 Haiku and GPT-4o Mini are not available, Mistral Medium 3 demonstrates strong performance with an MMLU score of 80.0 and a HumanEval score of 77.5.

#### Capabilities and Use Cases
Mistral Medium 3 supports a range of capabilities, including:
* Text
* Vision
* Function calling
* JSON mode
* Streaming
* System prompts

It is best suited for tasks such as:
* Coding
* Analysis
* RAG
* Summarization
* Vision tasks
* Content generation
* Function calling

However, it is not recommended for:
* Frontier reasoning
* Bulk cheap tasks
* Simple classification
* Real-time sub

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. This model is best suited for tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling.

### Top 5 Best Use Cases for Mistral Medium 3
Given its capabilities and limitations, here are the top 5 best use cases for Mistral Medium 3:

1. **Coding and Development**: With its strong coding capabilities, Mistral Medium 3 can be used for tasks such as code completion, code review, and code generation. For example, you can use it to integrate with OpenRouter for generating API documentation:
    ```python
import openrouter

# Initialize Mistral Medium 3 model
model = mistralai.MistralMedium3()

# Define a function to generate API documentation
def generate_api_docs(endpoint):
    # Use Mistral Medium 3 to generate documentation
    docs = model.generate_text(f"Generate API documentation for {endpoint}")
    return docs

# Integrate with OpenRouter
router = openrouter.OpenRouter()
router.add_endpoint("/api/docs", generate_api_docs)
```

2. **Analysis and Summarization**: Mistral Medium 3 can be used for text analysis and summarization tasks, such as summarizing long documents or analyzing customer feedback. For example:
    ```python
# Define a function to summarize text
def summarize_text(text):
    # Use Mistral Medium 3 to summarize text
    summary = model.generate_text(f"Summarize the following text: {text}")
    return summary
```

3. **Content Generation**: With its strong text generation capabilities, Mistral Medium 3 can be used for content generation tasks such as writing articles,

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
