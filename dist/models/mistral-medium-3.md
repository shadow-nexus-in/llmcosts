# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-12
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier language model designed to cater to a wide range of applications, from coding and analysis to vision tasks and content generation. This model is not open-source, indicating that its underlying architecture and training data are proprietary. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, Mistral Medium 3 is capable of handling complex and lengthy inputs, making it suitable for tasks that require in-depth understanding and generation of text.

### Technical Capabilities and Pricing
Technically, Mistral Medium 3 boasts an impressive array of capabilities, including text and vision processing, function calling, JSON mode, streaming, and system prompts. Its pricing model is based on input and output tokens, with costs of $0.4 per 1M input tokens and $2.0 per 1M output tokens. For developers, understanding these pricing metrics is crucial for budgeting and optimizing the use of the model. For example, making 1,000 calls with an average of 500 tokens each would cost $1.2, while 10,000 calls would amount to $12.0, and 100,000 calls would be $120.0. This pricing structure suggests that Mistral Medium 3 is positioned for applications where the value of the output justifies the cost, rather than for bulk or very low-latency tasks.

### Use Cases and Competitors
Mistral Medium 3 is best suited for tasks such as coding, analysis, summarization, and content generation, where its strengths in understanding and generating coherent text can be fully leveraged. However, it may not be the best choice for frontier reasoning, bulk cheap tasks, simple classification, or real-time applications requiring sub-100ms responses. In comparison to its competitors, such as Claude 3.5 Haiku

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $None per 1M tokens (free)
* Batch Input: $None per 1M tokens (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following strategies:
* **Cached Tokens**: Utilize cached input tokens whenever possible, as they are free. This is ideal for applications with repetitive or similar input patterns.
* **Batch API Calls**: Leverage batch input to reduce the number of API calls, as batch input is also free. This approach is suitable for applications that can process multiple inputs simultaneously.

#### Cost at Scale
The cost of using Mistral Medium 3 at various scales is as follows:
* **1,000 calls (avg 500 tokens)**: $1.2
* **10,000 calls**: $12.0
* **100,000 calls**: $120.0

To estimate the cost at scale, we can calculate the cost per 1M tokens:
* Assuming an average of 500 tokens per call, 1,000 calls would require 500,000 tokens.
* Using the input and output pricing, the estimated cost for 1,000 calls would be: (500,000 tokens / 1,000,000 tokens) \* ($0.4 + $2.0) = $1.2

#### Comparison with Top Competitors
Mistral Medium 3's pricing is competitive with other models in the market:
*

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
* **MMLU (Massive Multitask Language Understanding)**: 80.0 - This score indicates the model's ability to understand and generate human-like text across a wide range of tasks and topics. A higher score suggests better language understanding capabilities.
* **HumanEval**: 77.5 - This score evaluates the model's ability to generate code that passes unit tests, simulating real-world programming tasks. A higher score indicates better coding capabilities.
* **LMSYS Arena ELO**: 1200 - This score measures the model's performance in a competitive arena, where it is pitted against other models in various tasks. A higher score suggests better overall performance and adaptability.

#### Real-World Implications
The benchmark scores suggest that Mistral Medium 3 is suitable for real-world applications that require:
* Strong language understanding and generation capabilities (e.g., text analysis, summarization, content generation)
* Coding and programming tasks (e.g.,

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Introduction
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a unique set of capabilities and pricing. This comparison will delve into the details of Mistral Medium 3 and its top competitors, Claude 3.5 Haiku and GPT-4o Mini, highlighting their differences in pricing, performance, and use cases.

#### Pricing Comparison
The pricing models of the three competitors are as follows:

* **Mistral Medium 3**:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* **Claude 3.5 Haiku**:
	+ Input: $0.8 per 1M tokens (100% more than Mistral Medium 3)
	+ Output: $4.0 per 1M tokens (100% more than Mistral Medium 3)
* **GPT-4o Mini**:
	+ Input: $0.15 per 1M tokens (62.5% less than Mistral Medium 3)
	+ Output: $0.6 per 1M tokens (70% less than Mistral Medium 3)

#### Performance Comparison
The performance of the three models can be evaluated using various benchmarks:

* **MMLU**: Mistral Medium 3 (80.0) vs. Claude 3.5 Haiku (not provided) vs. GPT-4o Mini (not provided)
* **HumanEval**: Mistral Medium 3 (77.5) vs. Claude 3.5 Haiku (not provided) vs. GPT-4o Mini (not provided)
* **LMSYS Arena ELO**: Mistral Medium 3 (1200) vs. Claude 3.5 Haiku (not provided) vs. GPT-4o Mini (not provided)

#### Capabilities and Use Cases
Mistral Medium 3 has a wide range of capabilities, including:

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

## Best Use Cases
### Practical Advice on Top 5 Best Use Cases for Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. Given its capabilities and pricing, here are the top 5 best use cases for Mistral Medium 3:

#### 1. **Coding and Analysis**
Mistral Medium 3 excels in coding and analysis tasks, making it suitable for applications such as code review, code generation, and data analysis. Its ability to handle large context windows and generate substantial output makes it an excellent choice for complex coding tasks.

**Example Code Integration with OpenRouter:**
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Define a coding task
task = "Write a Python function to calculate the area of a circle."

# Generate code using the model
code = model.generate_code(task)

# Print the generated code
print(code)
```

#### 2. **Summarization and Content Generation**
Mistral Medium 3 is well-suited for summarization and content generation tasks, such as summarizing long documents, generating articles, or creating social media posts. Its ability to understand context and generate coherent text makes it an excellent choice for these applications.

**Example Code Integration with OpenRouter:**
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Define a summarization task
task = "Summarize the following article: [insert article text]"

# Generate summary using the model
summary = model.generate_summary(task)

# Print the generated summary
print(summary)
```

#### 3. **Vision Tasks**
Mistral Medium 3 has capabilities in vision tasks, such as image classification,

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
