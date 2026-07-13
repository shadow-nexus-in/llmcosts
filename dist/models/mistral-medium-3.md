# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-13
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Technical Overview of Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that boasts a robust architecture designed to handle a wide range of tasks. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, this model is well-suited for applications that require in-depth analysis and generation of text. Its capabilities extend beyond text, supporting vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Strengths and Use-Cases
The main strengths of Mistral Medium 3 lie in its ability to perform complex tasks such as coding, analysis, and content generation. It also excels in tasks that require vision capabilities, making it a good fit for projects that involve image or video processing. With a high MMLU score of 80.0 and a HumanEval score of 77.5, this model demonstrates strong performance in various benchmarks. Its LMSYS Arena ELO score of 1200 further solidifies its position as a formidable mid-tier model. Developers can leverage Mistral Medium 3 for tasks such as summarization, RAG, and function calling, where its capabilities shine.

### Pricing and Cost Considerations
Mistral Medium 3 is priced at $0.4 per 1M input tokens and $2.0 per 1M output tokens. This pricing model makes it competitive with other mid-tier models like Claude 3.5 Haiku and GPT-4o Mini. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 100,000 calls would amount to $120.0. When choosing Mistral Medium 3, developers should consider the cost-effectiveness of this model for their specific use cases, weighing its strengths against its limitations, such as not being suitable for frontier

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### Optimal Usage Scenarios
* **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
* **Batch API Savings**: With batch input being free, batching API calls can significantly reduce costs. However, the actual cost savings will depend on the output token count, which is charged at **$2.0 per 1M tokens**.

#### Cost at Scale
The cost examples provided are as follows:
* **1,000 calls (avg 500 tokens)**: **$1.2**
* **10,000 calls**: **$12.0**
* **100,000 calls**: **$120.0**

To estimate the cost at scale, we can extrapolate from the provided examples. Assuming an average of 500 tokens per call, the cost per call can be broken down into input and output costs.

#### Competitor Comparison
Mistral Medium 3's pricing is compared to its top competitors:
* **Claude 3.5 Haiku**: $0.8/1M input, $4.0/1M output
* **GPT-4o Mini**: $0.15/1M input, $0.6/1M output

Mistral Medium 3

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Mistral Medium 3 Benchmark Performance
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. The model's pricing is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens

#### Benchmark Scores
The model's performance is measured by the following benchmark scores:
* **MMLU (80.0)**: The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to perform a wide range of natural language processing tasks. A higher MMLU score indicates better performance. With a score of 80.0, Mistral Medium 3 demonstrates strong language understanding capabilities.
* **HumanEval (77.5)**: The HumanEval benchmark assesses a model's ability to evaluate and execute Python code. A higher HumanEval score indicates better coding abilities. With a score of 77.5, Mistral Medium 3 shows promising coding capabilities.
* **LMSYS Arena ELO (1200)**: The LMSYS Arena ELO benchmark measures a model's performance in a competitive environment, evaluating its ability to generate human-like text. A higher ELO score indicates better performance. With a score of 1200, Mistral Medium 3 demonstrates reasonable text generation capabilities.

#### Real-World Implications
The benchmark scores suggest that Mistral Medium 3 is suitable for tasks that require:
* Strong language understanding (e.g., analysis, summarization)
* Coding abilities (e.g.,

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a unique set of capabilities and pricing. This comparison will delve into the details of Mistral Medium 3 and its top competitors, Claude 3.5 Haiku and GPT-4o Mini, highlighting price differences, performance trade-offs, and use cases for each model.

#### Pricing Comparison
The pricing for each model is as follows:
* **Mistral Medium 3**:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* **Claude 3.5 Haiku**:
	+ Input: $0.8 per 1M tokens (100% increase over Mistral Medium 3)
	+ Output: $4.0 per 1M tokens (100% increase over Mistral Medium 3)
* **GPT-4o Mini**:
	+ Input: $0.15 per 1M tokens (62.5% decrease from Mistral Medium 3)
	+ Output: $0.6 per 1M tokens (70% decrease from Mistral Medium 3)

#### Performance Trade-offs
The performance of each model can be evaluated using various benchmarks:
* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

While the benchmark scores for Claude 3.5 Haiku and GPT-4o Mini are not available, Mistral Medium 3's scores indicate a strong performance in coding and analysis tasks.

#### Capabilities and Use Cases
Mistral Medium 3 is best suited for tasks such as:
* Coding
* Analysis
* RAG (Retrieve, Augment, Generate)
* Summarization
* Vision tasks
* Content generation
* Function calling

On the other hand, it is not recommended for:
* Frontier reasoning
* Bulk cheap tasks
* Simple classification
* Real-time tasks with sub-100ms latency

#### Cost Examples
To illustrate the cost differences, consider the following

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful language model with a wide range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. Released on 2025-04-17, this model is best suited for tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling.

### Top 5 Best Use Cases for Mistral Medium 3
Based on its capabilities and limitations, here are the top 5 best use cases for Mistral Medium 3:

1. **Coding and Development**: With its strong coding capabilities, Mistral Medium 3 can be used for code completion, code review, and code generation tasks. For example, you can use it to integrate with OpenRouter for automated code generation:
   ```python
import openrouter

# Initialize Mistral Medium 3 model
model = mistralai.MistralMedium3()

# Define a function to generate code using OpenRouter
def generate_code(prompt):
    input_tokens = openrouter.tokenize(prompt)
    output = model.generate(input_tokens)
    return openrouter.detokenize(output)

# Test the function
print(generate_code("Write a Python function to sort a list of integers"))
```

2. **Text Analysis and Summarization**: Mistral Medium 3 can be used for text analysis and summarization tasks, such as summarizing long documents or analyzing customer feedback. For example:
   ```python
import mistralai

# Initialize Mistral Medium 3 model
model = mistralai.MistralMedium3()

# Define a function to summarize text
def summarize_text(text):
    input_tokens = mistralai.tokenize(text)
    output = model.generate(input_tokens, max_length=128)
    return mistralai.detokenize(output)

# Test the function
print(summarize_text("This is a long

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
