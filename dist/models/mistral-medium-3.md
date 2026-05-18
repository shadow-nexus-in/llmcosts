# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-18
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance between performance and cost. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, this model is well-suited for a variety of tasks, including coding, analysis, and content generation. The model's capabilities include text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Architecture and Strengths
The architecture of Mistral Medium 3 is designed to support a wide range of applications, with a focus on mid-level complexity tasks. The model's strengths lie in its ability to handle complex inputs and generate high-quality outputs, as evidenced by its benchmark scores: MMLU (80.0), HumanEval (77.5), and LMSYS Arena ELO (1200). The model is particularly well-suited for tasks that require a deep understanding of context and nuance, such as summarization, vision tasks, and function calling. With a knowledge cutoff of 2024-11, the model is equipped to handle tasks that require up-to-date information, but may not be suitable for tasks that require very recent knowledge.

### Pricing and Use Cases
The pricing for Mistral Medium 3 is as follows: $0.4 per 1M input tokens and $2.0 per 1M output tokens. This makes it a competitive option for developers who need to process large amounts of data. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 10,000 calls would cost $12.0. In comparison to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers a unique balance of performance and cost. However

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
Mistral Medium 3 is a mid-tier model provided by Mistral AI, released on 2025-04-17. This model is not open source and has a specific cost structure based on input and output tokens.

#### Cost Structure
The cost structure for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs when the same input is used multiple times. Since cached input is free, it is recommended to use cached tokens whenever possible to minimize costs.

#### Batch API Savings
Batching API calls can also help reduce costs. Although the pricing data does not provide a specific discount for batch API calls, the fact that batch input is free suggests that batching can help reduce the overall cost per call.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* 1,000 calls (avg 500 tokens): $1.2
* 10,000 calls: $12.0
* 100,000 calls: $120.0

To calculate the cost per call, we can divide the total cost by the number of calls:
* 1,000 calls: $1.2 / 1,000 = $0.0012 per call
* 10,000 calls: $12.0 / 10,000 = $0.0012 per call
* 100,000 calls: $120.0 / 100,000 = $0.0012 per call

The cost per call remains constant at $0.0012 per call, regardless of the number of calls. This suggests

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Medium 3 Benchmark Analysis
#### Model Overview
The Mistral Medium 3 model, released by Mistral AI on 2025-04-17, is a mid-tier, non-open-source model. It is capable of handling various tasks, including coding, analysis, and vision tasks.

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
* MMLU: **80.0** - This score indicates the model's ability to understand and generate human-like language. A higher score means better performance.
* HumanEval: **77.5** - This score measures the model's ability to write correct and functional code. A higher score means better coding capabilities.
* LMSYS Arena ELO: **1200** - This score represents the model's overall performance in a competitive arena. A higher score means better performance compared to other models.

#### Real-World Implications
The benchmark scores have the following implications for real-world use:
* The MMLU score of **80.0** indicates that Mistral Medium 3 is capable of understanding and generating human-like language, making it suitable for tasks such as content generation and text

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will delve into the pricing, performance, and capabilities of Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

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
* Claude 3.5 Haiku: Not provided
* GPT-4o Mini: Not provided

Given the lack of benchmark data for the competitors, it's challenging to make a direct comparison. However, Mistral Medium 3's benchmarks suggest it is a capable model for tasks such as coding, analysis, and content generation.

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

On the other hand, it is not recommended for:
* Frontier reasoning
* Bulk cheap tasks
* Simple classification

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. This model is best suited for tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling.

### Top 5 Best Use Cases for Mistral Medium 3
Based on its capabilities and pricing, here are the top 5 best use cases for Mistral Medium 3:

1. **Coding and Development**: With its strong performance in coding tasks, Mistral Medium 3 can be used for code completion, code review, and code generation. For example, you can use it with OpenRouter to generate code snippets in response to user input.
    ```python
import openrouter

# Initialize OpenRouter with Mistral Medium 3
router = openrouter.OpenRouter(model="mistralai/mistral-medium-3")

# Define a function to generate code snippets
def generate_code(prompt):
    response = router.generate_text(prompt, max_tokens=1024)
    return response

# Test the function
print(generate_code("Write a Python function to sort a list of integers"))
```

2. **Text Analysis and Summarization**: Mistral Medium 3 can be used for text analysis and summarization tasks, such as summarizing long documents or extracting key points from a piece of text.
    ```python
import openrouter

# Initialize OpenRouter with Mistral Medium 3
router = openrouter.OpenRouter(model="mistralai/mistral-medium-3")

# Define a function to summarize text
def summarize_text(text):
    prompt = f"Summarize the following text: {text}"
    response = router.generate_text(prompt, max_tokens=512)
    return response

# Test the function

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
