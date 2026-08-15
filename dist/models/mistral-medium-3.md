# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-15
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, developed by Mistral AI, is a mid-tier language model released on 2025-04-17. This model is not open source. From an architectural standpoint, Mistral Medium 3 is designed to handle a wide range of tasks, including coding, analysis, and vision tasks, thanks to its capabilities in text, vision, function calling, JSON mode, streaming, and system prompts. Its primary strengths lie in its ability to process complex tasks with a large context window of 131,072 tokens and a maximum output of 16,384 tokens.

### Technical Specifications and Use Cases
The pricing model for Mistral Medium 3 is based on input and output tokens, with costs of $0.4 per 1M input tokens and $2.0 per 1M output tokens. The model's performance is benchmarked with scores of 80.0 on MMLU, 77.5 on HumanEval, and an ELO rating of 1200 on LMSYS Arena. It is best utilized for tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling. However, it is not recommended for frontier reasoning, bulk cheap tasks, simple classification, or real-time tasks requiring responses under 100ms. The knowledge cutoff for this model is 2024-11, indicating that it may not have information on events or developments after this date.

### Cost Considerations and Competitors
For developers considering the use of Mistral Medium 3, the cost can be estimated based on the number of calls and tokens processed. For example, 1,000 calls with an average of 500 tokens would cost approximately $1.2, while 10,000 calls would cost $12.0, and 100,000 calls would cost $120.0. In comparison to its competitors, such as Claude 3.5

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
- **Input**: $0.4 per 1M tokens
- **Output**: $2.0 per 1M tokens
- **Cached Input**: $0 per 1M tokens (free)
- **Batch Input**: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Given that cached input tokens are free, it is highly beneficial to utilize cached tokens whenever possible. This can significantly reduce costs, especially for applications with repetitive or similar input sequences.

#### Batch API Savings
Although batch input is listed as free, the actual cost savings come from the reduced overhead of making fewer API calls. To maximize batch API savings, consider the following:
- **Batch Size**: Optimize batch sizes to minimize the number of API calls while staying within the context window limit of 131,072 tokens.
- **Output Limit**: Be mindful of the max output limit of 16,384 tokens to avoid unnecessary additional API calls.

#### Cost at Scale
The cost examples provided are as follows:
- **1,000 calls (avg 500 tokens)**: $1.2
- **10,000 calls**: $12.0
- **100,000 calls**: $120.0

To estimate costs at scale, we can calculate the cost per call:
- Assuming an average of 500 tokens per call, the total tokens per 1,000 calls would be 500,000 tokens.
- Using the input and output pricing, we can estimate the cost per call:
  - Input cost: 500,000 tokens / 1,000,000

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
Mistral Medium 3, a model provided by Mistral AI, offers a balance of performance and cost for various real-world applications. Released on April 17, 2025, this mid-tier model is not open source.

#### Pricing
The pricing structure for Mistral Medium 3 is as follows:
- **Input**: $0.4 per 1M tokens
- **Output**: $2.0 per 1M tokens
- **Cached Input**: $None per 1M tokens
- **Batch Input**: $None per 1M tokens

#### Context and Limits
Key limitations and capabilities include:
- **Context Window**: 131,072 tokens
- **Max Output**: 16,384 tokens
- **Knowledge Cutoff**: 2024-11

#### Benchmarks
Mistral Medium 3's performance is measured by the following benchmarks:
- **MMLU (Massive Multitask Language Understanding)**: 80.0
  - Indicates the model's ability to understand and perform a wide range of language tasks. A higher score suggests better multitask learning capabilities.
- **HumanEval**: 77.5
  - Measures the model's ability to evaluate and execute human-written code. This score reflects the model's coding and problem-solving capabilities.
- **LMSYS Arena ELO**: 1200
  - Represents the model's competitive performance in a controlled environment, similar to a chess rating. A higher ELO score indicates better performance against other models.

#### Capabilities and Use Cases
Mistral Medium 3 supports:
- **Capabilities**: text, vision, function_calling

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will delve into the pricing, performance, and use cases of Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

#### Pricing Comparison
The pricing models of the three competitors are as follows:
* **Mistral Medium 3**:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* **Claude 3.5 Haiku**:
	+ Input: $0.8 per 1M tokens
	+ Output: $4.0 per 1M tokens
* **GPT-4o Mini**:
	+ Input: $0.15 per 1M tokens
	+ Output: $0.6 per 1M tokens

Mistral Medium 3 offers a balanced pricing model, sitting between the expensive Claude 3.5 Haiku and the cost-effective GPT-4o Mini.

#### Performance Trade-offs
The performance of each model can be evaluated using various benchmarks:
* **Mistral Medium 3**: MMLU (80.0), HumanEval (77.5), LMSYS Arena ELO (1200)
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

While the exact performance of Claude 3.5 Haiku and GPT-4o Mini is not available, Mistral Medium 3's benchmark scores indicate a strong performance in coding, analysis, and other tasks.

#### Capabilities and Use Cases
Mistral Medium 3 supports a wide range of capabilities, including:
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
* Real-time tasks with

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. This guide will outline the top 5 best use cases for Mistral Medium 3, along with practical advice and code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Medium 3
Based on its capabilities and pricing, the top 5 use cases for Mistral Medium 3 are:

1. **Coding and Analysis**: Mistral Medium 3 excels in coding tasks, making it suitable for code generation, code review, and analysis. Its function calling capability allows for dynamic interaction with external systems.
2. **Summarization and Content Generation**: With its strong text capabilities, Mistral Medium 3 can be used for summarizing large documents, generating content, and creating text-based products.
3. **Vision Tasks**: Mistral Medium 3's vision capabilities make it suitable for image analysis, object detection, and image generation tasks.
4. **RAG (Retrieve, Augment, Generate) Tasks**: Mistral Medium 3's ability to retrieve information, augment existing text, and generate new text makes it well-suited for RAG tasks.
5. **Complex Text Analysis**: Mistral Medium 3's context window of 131,072 tokens and max output of 16,384 tokens make it suitable for complex text analysis tasks that require a deep understanding of the input text.

### Code Integration Example with OpenRouter
To integrate Mistral Medium 3 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the OpenRouter client
client = openrouter.Client(api_key="YOUR_API_KEY")

# Define the input prompt
prompt = "Generate a summary of the following text: [insert text

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
