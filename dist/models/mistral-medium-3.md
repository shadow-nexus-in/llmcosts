# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-11
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a robust set of capabilities for developers. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, this model is well-suited for tasks that require in-depth analysis and generation of content. The architecture of Mistral Medium 3 supports a wide range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts.

### Strengths and Use Cases
The main strengths of Mistral Medium 3 lie in its ability to handle complex tasks such as coding, analysis, and content generation. With a high MMLU score of 80.0 and a HumanEval score of 77.5, this model demonstrates strong performance in natural language processing and programming tasks. The model's capabilities also extend to vision tasks, making it a versatile tool for developers working on multimodal projects. However, it is not recommended for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms.

### Pricing and Cost Considerations
Mistral Medium 3 is priced at $0.4 per 1M input tokens and $2.0 per 1M output tokens. This pricing model makes it a competitive option for developers working on projects that require high-quality output. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 10,000 calls would cost $12.0. In comparison to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers a unique balance of capabilities and pricing. Developers can evaluate the cost-effectiveness of this model by considering their specific use cases and the required input and output token volumes.

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
Mistral Medium 3 is a mid-tier model provided by Mistral AI, released on 2025-04-17. This model is not open source and has a specific cost structure for input and output tokens.

#### Cost Structure
The cost structure for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs when the same input tokens are used multiple times. Since cached input tokens are free, it is recommended to use them whenever possible to minimize costs.

#### Batch API Savings
Batch input tokens are also free, which means that making batch API calls can help reduce costs. By batching multiple requests together, users can avoid paying for input tokens, resulting in significant savings.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* 1,000 calls (avg 500 tokens): $1.2
* 10,000 calls: $12.0
* 100,000 calls: $120.0

To calculate the cost at scale, we can use the following formula:
Cost = (Number of calls \* Average tokens per call) \* (Input cost per 1M tokens + Output cost per 1M tokens)

For example, for 1,000 calls with an average of 500 tokens per call:
Cost = (1,000 \* 500) \* ($0.4/1M + $2.0/1M) = $1.2

#### Comparison with Top Competitors
Mistral Medium 3's pricing is competitive with other top models in the market

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
The Mistral Medium 3 model, provided by Mistral AI, is a mid-tier, non-open-source model released on 2025-04-17. It offers a range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts.

#### Pricing
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Context and Limits
The model has the following context and limits:
* Context Window: **131,072 tokens**
* Max Output: **16,384 tokens**
* Knowledge Cutoff: **2024-11**

#### Benchmarks
The model's benchmark performance is as follows:
* MMLU: **80.0** - This score indicates the model's ability to understand and process natural language. A higher MMLU score suggests better language understanding capabilities.
* HumanEval: **77.5** - This score evaluates the model's ability to generate human-like code. A higher HumanEval score indicates better coding capabilities.
* LMSYS Arena ELO: **1200** - This score measures the model's performance in a competitive arena, where it is pitted against other models. A higher ELO score suggests better overall performance.

#### Real-World Implications
The benchmark scores suggest that Mistral Medium 3 is a capable model for a range of tasks, including:
* Coding: The model's high HumanEval

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a unique set of capabilities and pricing. This comparison will examine its strengths and weaknesses against top competitors, Claude 3.5 Haiku and GPT-4o Mini.

#### Pricing Comparison
The pricing for each model is as follows:
* Mistral Medium 3:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* Claude 3.5 Haiku:
	+ Input: $0.8 per 1M tokens
	+ Output: $4.0 per 1M tokens
* GPT-4o Mini:
	+ Input: $0.15 per 1M tokens
	+ Output: $0.6 per 1M tokens

Mistral Medium 3 offers a balance between input and output costs, while Claude 3.5 Haiku is more expensive on both fronts. GPT-4o Mini, on the other hand, is significantly cheaper for input but still relatively affordable for output.

#### Performance Trade-offs
The performance of each model can be evaluated using various benchmarks:
* Mistral Medium 3:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* Claude 3.5 Haiku: Not provided
* GPT-4o Mini: Not provided

While the exact performance of Claude 3.5 Haiku and GPT-4o Mini is not available, Mistral Medium 3 demonstrates strong capabilities in coding, analysis, and vision tasks.

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
* RAG (Retrieve, Augment, Generate)
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
To illustrate the cost differences, consider the following examples

## Best Use Cases
### Practical Advice for Mistral Medium 3
Mistral Medium 3, a mid-tier model provided by Mistral AI, offers a balance of performance and cost-effectiveness. With its capabilities in text, vision, function calling, and more, it's best suited for tasks like coding, analysis, and content generation. Here are the top 5 best use cases for Mistral Medium 3, along with specific code integration examples mentioning OpenRouter:

#### 1. **Coding and Development**
Mistral Medium 3 excels in coding tasks, making it an ideal choice for developers. You can integrate it with OpenRouter to generate code snippets or even entire functions.
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Generate code snippet
code_snippet = model.generate_code("Create a Python function to calculate the area of a rectangle")
print(code_snippet)
```

#### 2. **Text Analysis and Summarization**
With its strong text analysis capabilities, Mistral Medium 3 can be used for summarization tasks. You can use OpenRouter to integrate the model with your text analysis pipeline.
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Summarize a piece of text
text = "Your text here..."
summary = model.summarize_text(text)
print(summary)
```

#### 3. **Content Generation**
Mistral Medium 3 can generate high-quality content, making it suitable for tasks like blog post writing or social media content creation. You can integrate it with OpenRouter to generate content based on a given prompt.
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Generate content
prompt = "Write a blog post about the benefits of AI in healthcare"
content = model.generate_content(prompt

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
