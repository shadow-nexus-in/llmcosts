# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-19
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance between performance and cost. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, this model is well-suited for a variety of tasks, including coding, analysis, and content generation. The model's capabilities include text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Architecture and Strengths
The architecture of Mistral Medium 3 is designed to support a wide range of applications, with a focus on mid-level complexity tasks. The model's strengths lie in its ability to handle complex inputs and generate high-quality outputs, as evidenced by its benchmark scores: MMLU (80.0), HumanEval (77.5), and LMSYS Arena ELO (1200). While it may not be the best choice for frontier reasoning, bulk cheap tasks, simple classification, or real-time sub-100ms tasks, it excels in areas such as coding, analysis, and vision tasks. The pricing model for Mistral Medium 3 is as follows: $0.4 per 1M input tokens and $2.0 per 1M output tokens.

### Use Cases and Cost Considerations
Mistral Medium 3 is best utilized for tasks that require a balance between complexity and cost. Its capabilities make it an ideal choice for applications such as coding, analysis, summarization, and content generation. When considering the cost, developers can expect to pay $1.2 for 1,000 calls (avg 500 tokens), $12.0 for 10,000 calls, and $120.0 for 100,000 calls. In comparison to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini,

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### Optimal Usage Scenarios
* **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
* **Batch API Calls**: Batch input is also free, making it an attractive option for large-scale API calls. However, the cost savings will primarily come from reducing the number of output tokens.

#### Cost at Scale
The cost examples provided are:
* **1,000 calls (avg 500 tokens)**: **$1.2**
* **10,000 calls**: **$12.0**
* **100,000 calls**: **$120.0**

To put these costs into perspective, let's calculate the cost per 1M tokens for each scenario:
* Assuming an average of 500 tokens per call, 1,000 calls would be approximately 0.5M tokens.
* For 1,000 calls, the cost is **$1.2**, which translates to **$2.4 per 1M tokens** (input and output combined).
* For 10,000 calls, the cost is **$12.0**, which is **$1.2 per 1M tokens** (input and output combined), assuming 10,000 calls * 500 tokens = 5M tokens.


## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Mistral Medium 3 Benchmark Performance
The Mistral Medium 3 model, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. The model's pricing is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens

#### Benchmark Scores
The model's benchmark performance is as follows:
* **MMLU (Massive Multitask Language Understanding)**: 80.0 - This score indicates the model's ability to perform well across a wide range of natural language processing tasks. A higher score suggests better performance in understanding and generating human-like language.
* **HumanEval**: 77.5 - This score evaluates the model's ability to generate correct and functional code in response to programming prompts. A higher score indicates better coding capabilities.
* **LMSYS Arena ELO**: 1200 - This score measures the model's performance in a competitive arena, where it is pitted against other models in a variety of tasks. A higher ELO score suggests better overall performance and adaptability.

#### Real-World Implications
These benchmark scores have significant implications for real-world use:
* The high MMLU score suggests that Mistral Medium 3 is well-suited for tasks that require a deep understanding of language, such as text analysis, summarization, and content generation.
* The strong HumanEval score indicates that the model is capable of generating high-quality code, making it a good choice for coding tasks and software development.
* The LMSYS Arena ELO score of 1200

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will evaluate Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini, in terms of pricing, performance, and use cases.

#### Pricing Comparison
The pricing for each model is as follows:
* Mistral Medium 3:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* Claude 3.5 Haiku:
	+ Input: $0.8 per 1M tokens (100% more than Mistral Medium 3)
	+ Output: $4.0 per 1M tokens (100% more than Mistral Medium 3)
* GPT-4o Mini:
	+ Input: $0.15 per 1M tokens (62.5% less than Mistral Medium 3)
	+ Output: $0.6 per 1M tokens (70% less than Mistral Medium 3)

#### Performance Trade-offs
The performance of each model can be evaluated using the provided benchmarks:
* Mistral Medium 3:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* Claude 3.5 Haiku and GPT-4o Mini benchmarks are not provided, making a direct comparison challenging. However, based on the pricing, it can be inferred that Claude 3.5 Haiku may offer higher performance, while GPT-4o Mini may be more suitable for budget-conscious applications.

#### Use Cases and Recommendations
Mistral Medium 3 is best suited for:
* Coding
* Analysis
* RAG (Retrieve, Augment, Generate)
* Summarization
* Vision tasks
* Content generation
* Function calling

It is not recommended for:
* Frontier reasoning
* Bulk cheap tasks
* Simple classification
* Real-time sub-100ms tasks

In contrast, Claude 3.5 Haiku may be a better choice for applications that require higher performance and are willing to pay a premium. G

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. This model is best suited for tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling.

### Top 5 Best Use Cases for Mistral Medium 3
Based on its capabilities and limitations, here are the top 5 best use cases for Mistral Medium 3:

1. **Coding and Development**: With its strong performance in coding tasks, Mistral Medium 3 can be used for code completion, code review, and code generation. For example, you can use it with OpenRouter to generate code snippets in response to user input.
   ```python
# Example of using Mistral Medium 3 with OpenRouter for code generation
import openrouter

# Initialize the model
model = openrouter.Model("mistralai/mistral-medium-3")

# Define a function to generate code
def generate_code(prompt):
    response = model.generate_text(prompt, max_tokens=1024)
    return response

# Test the function
print(generate_code("Write a Python function to sort a list of integers"))
```

2. **Text Analysis and Summarization**: Mistral Medium 3 can be used for text analysis and summarization tasks, such as summarizing long documents or analyzing user feedback.
   ```python
# Example of using Mistral Medium 3 for text summarization
import openrouter

# Initialize the model
model = openrouter.Model("mistralai/mistral-medium-3")

# Define a function to summarize text
def summarize_text(text):
    prompt = f"Summarize the following text: {text}"
    response = model.generate_text(prompt, max_tokens=512)


## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
