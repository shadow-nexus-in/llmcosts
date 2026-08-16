# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-16
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Technical Overview of Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that operates on a closed-source architecture. Its primary strengths lie in its balanced performance across various tasks, including coding, analysis, and content generation. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, Mistral Medium 3 is capable of handling complex and lengthy inputs, making it suitable for tasks that require in-depth understanding and generation of text.

### Architecture and Capabilities
The model's architecture supports a wide range of capabilities, including text and vision tasks, function calling, JSON mode, streaming, and system prompts. These capabilities make Mistral Medium 3 a versatile tool for developers, allowing them to leverage its strengths in areas such as coding, summarization, and content generation. The model's performance is further reflected in its benchmark scores, with an MMLU score of 80.0, HumanEval score of 77.5, and LMSYS Arena ELO score of 1200. However, it is not recommended for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms.

### Pricing and Cost Examples
Mistral Medium 3 is priced at $0.4 per 1M input tokens and $2.0 per 1M output tokens. This pricing model makes it a competitive option for developers who require a balanced performance across various tasks. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 10,000 calls would cost $12.0, and 100,000 calls would cost $120.0. Compared to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers a unique balance of performance and pricing, making

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale for this model.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
- **Input**: $0.4 per 1M tokens
- **Output**: $2.0 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

This indicates that using cached input and batch processing can significantly reduce costs, as these features are provided at no additional charge.

#### Optimal Usage Scenarios
- **Cached Tokens**: Since cached input is free, it is highly recommended to use cached tokens whenever possible. This can significantly reduce costs for repeated or similar queries.
- **Batch API**: Similarly, utilizing batch API calls can help minimize costs, as batch input is also free. This is particularly beneficial for large-scale applications where multiple queries can be processed together.

#### Cost at Scale
To understand the cost-effectiveness of Mistral Medium 3 at different scales, let's examine the provided cost examples:
- **1,000 calls (avg 500 tokens)**: $1.2
- **10,000 calls**: $12.0
- **100,000 calls**: $120.0

These examples suggest a linear cost scaling, where the cost increases directly with the number of API calls. This linear relationship indicates that the cost per call remains constant, regardless of the scale.

#### Comparison with Competitors
Mistral Medium 3's pricing can be compared to its top competitors:
- **Claude 3.5 Haiku**: $0.8/1M input, $4.0/1

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This analysis will delve into its benchmark performance, focusing on MMLU, HumanEval, and Arena ELO scores, and what these metrics mean for real-world applications.

#### Benchmark Scores
- **MMLU (Massive Multitask Language Understanding)**: 80.0
  The MMLU score indicates the model's ability to understand and perform a wide range of natural language tasks. A score of 80.0 suggests that Mistral Medium 3 has a strong foundation in language understanding, capable of handling complex tasks with a high degree of accuracy.
- **HumanEval**: 77.5
  HumanEval measures the model's ability to generate code that is both correct and readable, simulating human coding skills. A score of 77.5 indicates that Mistral Medium 3 is proficient in coding tasks, though it may struggle with highly complex or nuanced coding challenges.
- **LMSYS Arena ELO**: 1200
  The Arena ELO score reflects the model's performance in competitive scenarios, such as debate or argumentation tasks. An ELO score of 1200 places Mistral Medium 3 in a respectable position, suggesting it can hold its own in most competitive linguistic tasks, though it may not outperform top-tier models.

#### Real-World Implications
These benchmark scores imply that Mistral Medium 3 is well-suited for tasks such as:
- **Coding and Analysis**: With a strong HumanEval score, it's adept at generating code and can

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance between price and performance. This comparison will analyze its pricing, performance, and capabilities against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

#### Pricing Comparison
The pricing for each model is as follows:
* **Mistral Medium 3**:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* **Claude 3.5 Haiku**:
	+ Input: $0.8 per 1M tokens (100% more than Mistral Medium 3)
	+ Output: $4.0 per 1M tokens (100% more than Mistral Medium 3)
* **GPT-4o Mini**:
	+ Input: $0.15 per 1M tokens (62.5% less than Mistral Medium 3)
	+ Output: $0.6 per 1M tokens (70% less than Mistral Medium 3)

#### Performance Trade-offs
The performance of each model can be evaluated using various benchmarks:
* **Mistral Medium 3**: MMLU (80.0), HumanEval (77.5), LMSYS Arena ELO (1200)
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

While the performance data for Claude 3.5 Haiku and GPT-4o Mini is not available, Mistral Medium 3's benchmarks indicate a strong performance in coding and analysis tasks.

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
* RAG (Retrieval-Augmented Generation)
* Summarization
* Vision tasks
* Content generation
* Function calling

However, it is not recommended for:
* Frontier reasoning
* Bulk cheap tasks
* Simple classification
* Real-time sub-100ms tasks

#### Cost Examples
The cost of using Mistral Medium 3 can be

## Best Use Cases
### Practical Advice for Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful model with a wide range of capabilities, including text, vision, function calling, and more. Given its pricing and capabilities, here are the top 5 best use cases for Mistral Medium 3, along with specific code integration examples mentioning OpenRouter.

#### 1. **Coding and Analysis**
Mistral Medium 3 excels in coding and analysis tasks, making it ideal for applications such as code review, code generation, and data analysis. When integrating with OpenRouter, you can leverage Mistral Medium 3's capabilities to analyze and generate code for various tasks.
```python
import openrouter
from mistralai import MistralMedium3

# Initialize Mistral Medium 3 model
model = MistralMedium3()

# Define a function to generate code using Mistral Medium 3
def generate_code(prompt):
    input_tokens = openrouter.tokenize(prompt)
    output = model.generate(input_tokens, max_length=16384)
    return openrouter.detokenize(output)

# Example usage
prompt = "Generate a Python function to calculate the area of a rectangle"
code = generate_code(prompt)
print(code)
```
#### 2. **Summarization and Content Generation**
Mistral Medium 3 is well-suited for summarization and content generation tasks, such as summarizing long documents, generating articles, or creating social media posts. With OpenRouter, you can integrate Mistral Medium 3 to generate high-quality content.
```python
import openrouter
from mistralai import MistralMedium3

# Initialize Mistral Medium 3 model
model = MistralMedium3()

# Define a function to summarize content using Mistral Medium 3
def summarize_content(text):
    input_tokens = openrouter.tokenize(text)
    output = model.generate(input_tokens, max_length=16384)
    return openrouter.det

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
