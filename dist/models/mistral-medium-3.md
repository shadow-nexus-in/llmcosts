# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-02
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance between performance and cost. As a non-open source model, it provides a unique set of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, Mistral Medium 3 is well-suited for a variety of tasks, including coding, analysis, and content generation.

### Architecture and Strengths
The architecture of Mistral Medium 3 is designed to support its diverse set of capabilities. Its strengths lie in its ability to handle complex tasks, such as function calling and vision tasks, with a high degree of accuracy. The model's performance is reflected in its benchmark scores, including an MMLU score of 80.0, a HumanEval score of 77.5, and an LMSYS Arena ELO score of 1200. While it may not be the best choice for tasks that require frontier reasoning or simple classification, Mistral Medium 3 excels in areas that require a deeper understanding of context and nuance.

### Pricing and Use Cases
Mistral Medium 3 is priced at $0.4 per 1M input tokens and $2.0 per 1M output tokens. This makes it a competitive option for developers who need to process large amounts of data. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 10,000 calls would cost $12.0. In comparison to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers a unique set of capabilities at a competitive price point. Its primary use cases include coding, analysis, summarization, and vision

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.4 |
| Output | $2.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Mistral Medium 3 Pricing Analysis
#### Overview
Mistral Medium 3, a mid-tier model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2025-04-17, this model is not open source. The pricing structure is based on input and output tokens, with specific rates for cached and batch inputs.

#### Cost Structure
The cost structure for Mistral Medium 3 is as follows:
* **Input**: $0.4 per 1M tokens
* **Output**: $2.0 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for reducing costs. However, the decision to use cached tokens should be based on the specific use case and the trade-off between cost savings and potential performance impacts. Since cached tokens are free, they can be used to minimize costs when:
* The input data is repetitive or has a high degree of similarity.
* The model is being used for tasks that do not require real-time processing.

#### Batch API Savings
Batch inputs are also free, which can lead to significant cost savings when processing large volumes of data. To maximize batch API savings:
* Batch similar tasks together to minimize the number of API calls.
* Optimize batch sizes to balance processing time and cost savings.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: $1.2
* **10,000 calls**: $12.0
* **100,000 calls**: $120.0

These costs demonstrate a linear scaling of costs with the number of API calls, indicating that the pricing model is straightforward and easy to predict.

#### Comparison to

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Medium 3 Benchmark Performance Analysis
#### Model Overview
The Mistral Medium 3 model, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. The model's knowledge cutoff is 2024-11.

#### Pricing
The pricing for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Benchmark Performance
The model's benchmark performance is measured by the following metrics:
* **MMLU (Massive Multitask Language Understanding)**: 80.0 - This score indicates the model's ability to understand and perform a wide range of natural language processing tasks. A higher score suggests better performance.
* **HumanEval**: 77.5 - This score evaluates the model's ability to generate human-like code and understand programming concepts. A higher score indicates better coding capabilities.
* **LMSYS Arena ELO**: 1200 - This score measures the model's performance in a competitive arena, where it is pitted against other models. A higher score suggests better overall performance.

#### Real-World Implications
The benchmark scores suggest that Mistral Medium 3 is a capable model for a variety of tasks, including:
* Coding and analysis
* Text and vision tasks
* Summarization and content generation
* Function calling and JSON mode

However, the model may not be suitable for:
* Frontier reasoning and complex tasks

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

Mistral Medium 3 is more expensive than GPT-4o Mini but cheaper than Claude 3.5 Haiku for both input and output.

#### Performance Trade-offs
The performance of each model can be evaluated using various benchmarks:
* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

Without benchmark data for Claude 3.5 Haiku and GPT-4o Mini, it's challenging to make a direct comparison. However, Mistral Medium 3's scores indicate strong performance in coding and analysis tasks.

#### Capabilities and Use Cases
Mistral Medium 3 supports various capabilities, including:
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

On the other hand, it is not recommended for:
* Frontier reasoning
* Bulk cheap tasks
* Simple classification
* Real-time sub-100ms tasks

#### Cost Examples

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. This model is best suited for tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling.

### Top 5 Best Use Cases for Mistral Medium 3
Given its capabilities and pricing, here are the top 5 best use cases for Mistral Medium 3:

1. **Coding and Software Development**: With its strong coding capabilities, Mistral Medium 3 can be used for tasks such as code completion, code review, and code generation. For example, you can use it with OpenRouter to generate code snippets for a specific task.
    ```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Generate code snippet
code_snippet = model.generate_code("Write a Python function to sort a list of numbers")
print(code_snippet)
```

2. **Text Analysis and Summarization**: Mistral Medium 3 can be used for text analysis and summarization tasks, such as summarizing long documents or analyzing customer feedback. You can use it with OpenRouter to analyze text data and generate summaries.
    ```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Analyze text data
text_data = "This is a sample text data"
analysis = model.analyze_text(text_data)
print(analysis)

# Generate summary
summary = model.summarize_text(text_data)
print(summary)
```

3. **Content Generation**: With its strong content generation capabilities, Mistral Medium 3 can be used for tasks such as generating blog posts, articles, or social media

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
