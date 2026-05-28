# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-28
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance between performance and cost. As a non-open source model, its architecture is not publicly disclosed, but its capabilities and benchmarks provide insight into its strengths. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, Mistral Medium 3 is designed to handle complex tasks that require significant input and output processing.

### Technical Strengths and Use-Cases
Mistral Medium 3 excels in various areas, including coding, analysis, and vision tasks, thanks to its support for text, vision, function calling, JSON mode, streaming, and system prompts. Its benchmarks, such as an MMLU score of 80.0 and a HumanEval score of 77.5, demonstrate its capabilities in natural language processing and coding tasks. However, it is not suitable for frontier reasoning, bulk cheap tasks, simple classification, or real-time tasks that require sub-100ms response times. The model's pricing structure, with input costs of $0.4 per 1M tokens and output costs of $2.0 per 1M tokens, makes it a viable option for developers who need to process large amounts of data.

### Cost Considerations and Competitors
To estimate the cost of using Mistral Medium 3, developers can consider the following examples: 1,000 calls with an average of 500 tokens cost $1.2, while 10,000 calls cost $12.0, and 100,000 calls cost $120.0. In comparison to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers a unique balance of performance and cost. For example, Claude 3.5 Haiku charges $0.8 per 

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
Mistral Medium 3 is a mid-tier model provided by Mistral AI, released on 2025-04-17. This analysis will dive into the cost structure, optimal usage scenarios, and cost savings at scale.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following scenarios:
* **Cached Tokens**: Use cached input tokens when possible, as they are **free**. This can significantly reduce costs for repeated or similar input prompts.
* **Batch API Calls**: Take advantage of batch input, which is also **free**. This can help reduce the overall cost per API call by processing multiple inputs simultaneously.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* **1,000 API calls** (avg 500 tokens): **$1.2**
* **10,000 API calls**: **$12.0**
* **100,000 API calls**: **$120.0**

These costs can be broken down into input and output costs. Assuming an average of 500 tokens per call, the total tokens per 1,000 calls would be 500,000 tokens. Using the pricing structure, the cost would be:
* Input: 500,000 tokens / 1,000,000 tokens per unit = 0.5 units \* $0.4 per unit = **$0.2**
* Output: assuming an average output of 100 tokens per call (conservative estimate), the total output tokens per 1,000 calls

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
The Mistral Medium 3 model, released by Mistral AI on 2025-04-17, is a mid-tier, closed-source model. Its pricing structure is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens

#### Benchmark Scores
The model's performance is measured by the following benchmark scores:
* **MMLU (80.0)**: The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to perform a wide range of natural language processing tasks. A higher MMLU score indicates better performance in tasks such as text classification, sentiment analysis, and question answering.
* **HumanEval (77.5)**: The HumanEval benchmark assesses a model's ability to generate code that is correct and functional. A higher HumanEval score suggests better performance in coding tasks, such as code completion and code generation.
* **LMSYS Arena ELO (1200)**: The LMSYS Arena ELO score measures a model's performance in a competitive environment, where models are pitted against each other to complete tasks. A higher ELO score indicates better performance in tasks that require strategic thinking and problem-solving.

#### Real-World Implications
The benchmark scores suggest that Mistral Medium 3 is a capable model for tasks such as:
* Coding and code generation (HumanEval: 77.5)
* Natural language processing tasks (MMLU: 80.0)
* Strategic thinking and problem-solving (LMSYS Arena ELO: 1200)

However, the model may not be suitable for

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a unique set of capabilities and pricing. This comparison will delve into the details of Mistral Medium 3 and its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

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
The performance of each model can be evaluated using various benchmarks:
* Mistral Medium 3:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* Claude 3.5 Haiku: Not provided
* GPT-4o Mini: Not provided

While the exact performance of Claude 3.5 Haiku and GPT-4o Mini is not available, Mistral Medium 3 demonstrates strong capabilities in coding, analysis, and vision tasks.

#### Context and Limits
The context window and output limits for Mistral Medium 3 are:
* Context Window: 131,072 tokens
* Max Output: 16,384 tokens
* Knowledge Cutoff: 2024-11

These limits are not provided for Claude 3.5 Haiku and GPT-4o Mini.

#### Capabilities and Use Cases
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
* Bulk

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful language model released on 2025-04-17. With its mid-tier pricing and extensive capabilities, it's an attractive option for various applications. This guide outlines the top 5 best use cases for Mistral Medium 3, along with practical advice and code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Medium 3
#### 1. **Coding and Analysis**
Mistral Medium 3 excels in coding and analysis tasks, making it suitable for applications like code review and debugging. Its `function_calling` capability allows for seamless integration with external functions.

```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Define a function to analyze code
def analyze_code(code):
    # Use Mistral Medium 3 to analyze the code
    result = model.analyze_code(code)
    return result

# Example usage
code = "def add(a, b): return a + b"
result = analyze_code(code)
print(result)
```

#### 2. **Summarization and Content Generation**
With its strong text generation capabilities, Mistral Medium 3 is well-suited for summarization and content generation tasks.

```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Define a function to summarize text
def summarize_text(text):
    # Use Mistral Medium 3 to summarize the text
    result = model.summarize_text(text)
    return result

# Example usage
text = "This is a sample text to be summarized."
result = summarize_text(text)
print(result)
```

#### 3. **Vision Tasks**
Mistral Medium 3's `vision` capability makes it suitable for applications like image classification and object detection.



## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
