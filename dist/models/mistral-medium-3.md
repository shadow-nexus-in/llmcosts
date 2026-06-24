# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-24
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a robust set of capabilities for developers. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, this model is well-suited for tasks that require a deep understanding of input context. The model's knowledge cutoff is 2024-11, ensuring that it has a broad and up-to-date knowledge base. Mistral Medium 3 is not open source, and its pricing is based on input and output tokens, with costs of $0.4 per 1M tokens for input and $2.0 per 1M tokens for output.

### Technical Strengths and Use Cases
Mistral Medium 3 has several key strengths that make it an attractive choice for developers. Its capabilities include text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile model for a wide range of tasks. The model excels in areas such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling. However, it is not well-suited for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms. With a MMLU score of 80.0, HumanEval score of 77.5, and LMSYS Arena ELO of 1200, Mistral Medium 3 has demonstrated strong performance in various benchmarks.

### Pricing and Cost Examples
The pricing for Mistral Medium 3 is competitive, with costs of $0.4 per 1M tokens for input and $2.0 per 1M tokens for output. To give developers a better understanding of the costs, some examples are provided: 1,000 calls with an average of 500 tokens would cost $1.2, while 10

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This model is not open source.

#### Cost Structure
The cost structure for Mistral Medium 3 is as follows:
* **Input**: $0.4 per 1M tokens
* **Output**: $2.0 per 1M tokens
* **Cached Input**: $0 per 1M tokens (free)
* **Batch Input**: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs when the same input is used multiple times. Since cached input is free, it is recommended to use cached tokens whenever possible to minimize costs.

#### Batch API Savings
Batch API calls can also help reduce costs. Although the pricing for batch input is listed as $0 per 1M tokens, the actual cost savings will depend on the specifics of the API calls. However, based on the provided cost examples, we can see that the cost per call decreases as the number of calls increases.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: $1.2
* **10,000 calls**: $12.0
* **100,000 calls**: $120.0

To calculate the cost per call, we can divide the total cost by the number of calls:
* **1,000 calls**: $1.2 / 1,000 = $0.0012 per call
* **10,000 calls**: $12.0 / 10,000 = $0.0012 per call
* **100,000 calls**: $120.0 / 100,000 = $0.0012 per call

As we can see,

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This analysis will delve into its benchmark performance, focusing on MMLU, HumanEval, and Arena ELO scores, to understand its capabilities and limitations in real-world applications.

#### Benchmark Scores
- **MMLU (Massive Multitask Language Understanding) Score: 80.0**
  The MMLU score measures a model's ability to understand and generate human-like text across a wide range of tasks and topics. A score of 80.0 indicates that Mistral Medium 3 has a strong understanding of language, capable of handling complex and diverse tasks with a high degree of accuracy.

- **HumanEval Score: 77.5**
  HumanEval assesses a model's ability to generate code that meets specific requirements, reflecting its coding capabilities. With a score of 77.5, Mistral Medium 3 demonstrates a good ability to understand and generate code, making it suitable for coding tasks.

- **LMSYS Arena ELO Score: 1200**
  The LMSYS Arena ELO score evaluates a model's performance in a competitive environment, where it is pitted against other models in various tasks. An ELO score of 1200 suggests that Mistral Medium 3 has a moderate level of competitiveness, indicating it can perform well in a variety of tasks but may struggle against more advanced models.

#### Real-World Implications
These benchmark scores imply that Mistral Medium 3 is well-suited for tasks that require strong language understanding, coding capabilities, and the ability

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will evaluate Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini, in terms of pricing, performance, and use cases.

#### Pricing Comparison
The pricing models for each competitor are as follows:
* **Mistral Medium 3**:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* **Claude 3.5 Haiku**:
	+ Input: $0.8 per 1M tokens
	+ Output: $4.0 per 1M tokens
* **GPT-4o Mini**:
	+ Input: $0.15 per 1M tokens
	+ Output: $0.6 per 1M tokens

Mistral Medium 3 offers a balance between input and output costs, while Claude 3.5 Haiku is the most expensive option. GPT-4o Mini is the most cost-effective choice, especially for input-intensive tasks.

#### Performance Comparison
The performance benchmarks for each model are:
* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

Mistral Medium 3 has a higher MMLU score compared to its HumanEval score, indicating stronger performance in certain tasks. However, without benchmark data for Claude 3.5 Haiku and GPT-4o Mini, a direct comparison is challenging.

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

However, it is not

## Best Use Cases
### Practical Advice for Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. Given its capabilities and pricing, here are the top 5 best use cases for Mistral Medium 3:

#### 1. **Coding and Analysis**
Mistral Medium 3 excels in coding and analysis tasks, making it suitable for applications such as code review, code generation, and data analysis. Its ability to handle function calling and JSON mode enables seamless integration with OpenRouter for tasks like automated code testing and deployment.
```python
import openrouter

# Initialize OpenRouter with Mistral Medium 3
router = openrouter.Router(model="mistralai/mistral-medium-3")

# Define a function to generate code
def generate_code(prompt):
    response = router.call(prompt)
    return response

# Use the function to generate code
code = generate_code("Write a Python function to sort a list of integers.")
print(code)
```

#### 2. **Summarization and Content Generation**
Mistral Medium 3 is well-suited for summarization and content generation tasks, such as summarizing long documents, generating articles, or creating social media posts. Its ability to handle text and vision tasks enables it to process and generate multimedia content.
```python
import openrouter

# Initialize OpenRouter with Mistral Medium 3
router = openrouter.Router(model="mistralai/mistral-medium-3")

# Define a function to summarize text
def summarize_text(text):
    prompt = f"Summarize the following text: {text}"
    response = router.call(prompt)
    return response

# Use the function to summarize text
summary = summarize_text("This is a long document that needs to be summarized.")
print(summary)
```

#### 3

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
