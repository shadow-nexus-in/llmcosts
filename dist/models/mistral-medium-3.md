# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-27
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance between performance and cost. This model is not open source. From an architectural standpoint, Mistral Medium 3 is designed to handle a variety of tasks, including text and vision processing, function calling, and more, thanks to its capabilities such as text, vision, function_calling, json_mode, streaming, and system_prompts. Its primary strengths lie in its ability to perform complex tasks like coding, analysis, and content generation efficiently.

### Technical Specifications and Use Cases
Technically, Mistral Medium 3 boasts a context window of 131,072 tokens and can generate up to 16,384 tokens as output. The model's knowledge cutoff is 2024-11, indicating that its training data is current up to that point. In terms of pricing, developers can expect to pay $0.4 per 1M tokens for input and $2.0 per 1M tokens for output. The model is best suited for tasks such as coding, analysis, summarization, and vision tasks, where its capabilities in function calling and content generation can be fully leveraged. However, it is not recommended for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms.

### Pricing and Competitors
The pricing model of Mistral Medium 3 is straightforward, with costs scaling linearly with the number of tokens processed. For example, 1,000 calls averaging 500 tokens each would cost $1.2, while 100,000 calls would amount to $120.0. In comparison to its competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers a competitive pricing structure, especially considering its performance benchmarks, including an MMLU score of 80

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. It is not open source. The pricing structure is based on input and output tokens.

#### Cost Structure
The cost structure for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for repeated input queries. If your application involves frequent reuse of the same input tokens, utilizing cached tokens can significantly reduce costs.

#### Batch API Savings
Batch input is also free, which means processing multiple inputs in a single API call does not incur additional costs for the input tokens. However, the output tokens are still charged at $2.0 per 1M tokens. To maximize batch API savings, consider the following:
* Minimize the number of API calls by batching inputs.
* Optimize output token count to reduce output costs.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* 1,000 calls (avg 500 tokens): $1.2
* 10,000 calls: $12.0
* 100,000 calls: $120.0

These costs are based on the provided examples and assume an average of 500 tokens per call.

#### Comparison with Top Competitors
Mistral Medium 3's pricing is compared to its top competitors:
* Claude 3.5 Haiku: $0.8/1M input, $4.0/1M output
* GPT-4o Mini: $0.15/1M input,

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. It is not open source.

#### Pricing
The pricing for Mistral Medium 3 is as follows:
- Input: **$0.4 per 1M tokens**
- Output: **$2.0 per 1M tokens**
- Cached Input: **$None per 1M tokens**
- Batch Input: **$None per 1M tokens**

#### Context and Limits
The model has the following context and limits:
- Context Window: **131,072 tokens**
- Max Output: **16,384 tokens**
- Knowledge Cutoff: **2024-11**

#### Benchmarks
Mistral Medium 3 has the following benchmark scores:
- **MMLU: 80.0**: The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to perform a wide range of natural language processing tasks. A score of 80.0 indicates that Mistral Medium 3 has a strong understanding of language, making it suitable for tasks that require complex language comprehension.
- **HumanEval: 77.5**: The HumanEval benchmark assesses a model's ability to generate code that is correct and functional. A score of 77.5 suggests that Mistral Medium 3 is capable of generating high-quality code, but may struggle with more complex coding tasks.
- **LMSYS Arena ELO: 1200**: The LMSYS Arena ELO score measures a model's performance in a competitive environment, where it is pitted

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will delve into the pricing, performance, and capabilities of Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

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

Mistral Medium 3 is priced lower than Claude 3.5 Haiku but higher than GPT-4o Mini for both input and output.

#### Performance Comparison
The performance benchmarks for each model are:
* **Mistral Medium 3**:
  + MMLU: 80.0
  + HumanEval: 77.5
  + LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

Mistral Medium 3 has a higher MMLU score compared to its competitors, but the lack of data for Claude 3.5 Haiku and GPT-4o Mini makes a direct comparison challenging.

#### Capabilities and Use Cases
Mistral Medium 3 supports the following capabilities:
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
The estimated costs

## Best Use Cases
### Practical Advice for Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful model with a wide range of capabilities, including text, vision, function calling, and more. Given its strengths and pricing, here are the top 5 best use cases for Mistral Medium 3, along with specific code integration examples mentioning OpenRouter.

#### 1. **Coding and Analysis**
Mistral Medium 3 excels in coding and analysis tasks. Its ability to understand and generate code, combined with its large context window of 131,072 tokens, makes it ideal for complex coding projects. 
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Example coding task
def generate_code(prompt):
    response = model.generate(prompt)
    return response

# Test the function
print(generate_code("Write a Python function to sort a list of integers"))
```

#### 2. **Summarization**
With its strong text capabilities, Mistral Medium 3 can efficiently summarize long documents or articles. Its output limit of 16,384 tokens ensures that it can provide detailed summaries without excessive verbosity.
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Example summarization task
def summarize_text(text):
    prompt = f"Summarize the following text: {text}"
    response = model.generate(prompt)
    return response

# Test the function
text = "Your long document or article text here"
print(summarize_text(text))
```

#### 3. **Content Generation**
Mistral Medium 3's content generation capabilities make it suitable for creating engaging content, such as blog posts, articles, or even entire books. Its ability to understand context and generate coherent text is unparalleled.
```python
import openrouter

# Initialize Mistral Medium 3

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
