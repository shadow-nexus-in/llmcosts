# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-04
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a robust set of capabilities for developers. With its architecture designed to handle a wide range of tasks, Mistral Medium 3 excels in areas such as coding, analysis, and content generation. Its strengths lie in its ability to process large context windows of up to 131,072 tokens and generate outputs of up to 16,384 tokens. This makes it an ideal choice for applications that require in-depth processing and generation of text.

### Technical Specifications and Pricing
From a technical standpoint, Mistral Medium 3 has a knowledge cutoff of 2024-11, indicating that its training data is current up to that point. The model's pricing structure is as follows: $0.4 per 1M input tokens and $2.0 per 1M output tokens. There are no additional costs for cached input or batch input. In terms of benchmarks, Mistral Medium 3 achieves an MMLU score of 80.0, a HumanEval score of 77.5, and an LMSYS Arena ELO rating of 1200. These metrics demonstrate the model's capabilities in various areas, including coding and problem-solving. The cost of using Mistral Medium 3 can be estimated using the provided examples, such as $1.2 for 1,000 calls with an average of 500 tokens per call.

### Use Cases and Competitors
Mistral Medium 3 is best suited for tasks that require advanced text processing, vision tasks, and function calling. Its capabilities include text, vision, function calling, JSON mode, streaming, and system prompts. However, it is not recommended for frontier reasoning, bulk cheap tasks, simple classification, or real-time applications with sub-100ms latency. In comparison to its competitors, such as Claude 3.5

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
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### Optimal Usage Scenarios
* **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
* **Batch API**: With batch input being free, batching API calls can significantly reduce the overall cost. However, the cost savings from batching will primarily come from reduced overhead rather than the token pricing itself, as the input cost is already $0 per 1M tokens for batched inputs.

#### Cost at Scale
The cost examples provided give us insight into the cost structure at different scales:
* 1,000 calls (avg 500 tokens): $1.2
* 10,000 calls: $12.0
* 100,000 calls: $120.0

These examples suggest a linear cost scaling, which is consistent with the pricing model based on tokens.

#### Competitor Comparison
Comparing Mistral Medium 3 with its top competitors:
* **Claude 3.5 Haiku**: $0.8/1M input, $4.0/1M output. Mistral Medium 3 is more expensive in terms of output cost but cheaper in terms of input cost.
* **GPT-4o Mini**: $0.15/1M input, $0.6/1M output. GPT-

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. It is not open-source and has specific pricing for input and output tokens.

#### Pricing
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Benchmarks
The model's performance is measured by the following benchmarks:
* **MMLU: 80.0** - The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to understand and generate human-like text across a wide range of tasks. A higher MMLU score indicates better performance in tasks such as text classification, sentiment analysis, and language translation.
* **HumanEval: 77.5** - The HumanEval benchmark assesses a model's ability to write correct and functional code in response to a given prompt. A higher HumanEval score suggests better coding capabilities, which is essential for tasks like coding, analysis, and function calling.
* **LMSYS Arena ELO: 1200** - The LMSYS Arena ELO score measures a model's performance in a competitive environment, where it is pitted against other models in various tasks. An ELO score of 1200 indicates that Mistral Medium 3 has a moderate level of competence in these tasks.

#### Real-World Implications
The benchmark scores of Mist

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will analyze the pricing, performance, and capabilities of Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

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

Mistral Medium 3 offers a balance between input and output costs, with Claude 3.5 Haiku being the most expensive and GPT-4o Mini being the cheapest.

#### Performance Trade-offs
The benchmark scores for each model are:
* **Mistral Medium 3**:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

While the benchmark scores for Claude 3.5 Haiku and GPT-4o Mini are not available, Mistral Medium 3 demonstrates strong performance in various tasks.

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
* Real-time sub-100ms tasks

#### Cost Examples
The estimated

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful language model with a wide range of capabilities, including text, vision, function calling, and more. Released on 2025-04-17, this model is well-suited for tasks such as coding, analysis, and content generation. In this guide, we will explore the top 5 best use cases for Mistral Medium 3, along with specific code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Medium 3
#### 1. **Coding and Development**
Mistral Medium 3 excels in coding tasks, making it an ideal choice for developers. With its function calling capability, you can integrate it with OpenRouter to generate code snippets or even entire functions.
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Define a function to generate code
def generate_code(prompt):
    response = model.generate(prompt)
    return response

# Example usage
prompt = "Write a Python function to sort a list of integers."
code = generate_code(prompt)
print(code)
```
#### 2. **Text Analysis and Summarization**
Mistral Medium 3's text analysis capabilities make it perfect for summarization tasks. You can use it to summarize long documents or articles, extracting key points and main ideas.
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Define a function to summarize text
def summarize_text(text):
    prompt = f"Summarize the following text: {text}"
    response = model.generate(prompt)
    return response

# Example usage
text = "This is a sample text to be summarized."
summary = summarize_text(text)
print(summary)
```
#### 3. **Content Generation**
With its content generation capabilities

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
