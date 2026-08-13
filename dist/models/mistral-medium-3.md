# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-13
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance of performance and cost. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, this model is well-suited for a variety of tasks, including coding, analysis, and content generation. The model's architecture supports multiple capabilities, such as text, vision, function calling, JSON mode, streaming, and system prompts.

### Technical Strengths and Use Cases
Mistral Medium 3 excels in tasks that require a combination of natural language understanding and generation. Its strengths are reflected in its benchmark scores, including an MMLU score of 80.0 and a HumanEval score of 77.5. The model is best used for tasks such as coding, analysis, summarization, and vision tasks, where its capabilities can be fully leveraged. However, it may not be the best choice for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms. With a pricing structure of $0.4 per 1M input tokens and $2.0 per 1M output tokens, developers can estimate costs based on their specific use cases, such as $1.2 for 1,000 calls with an average of 500 tokens.

### Cost Considerations and Competitors
When evaluating the cost-effectiveness of Mistral Medium 3, developers should consider their specific use cases and compare prices with other models. For example, Claude 3.5 Haiku and GPT-4o Mini offer different pricing structures, with Claude 3.5 Haiku charging $0.8/1M input and $4.0/1M output, and GPT-4o Mini charging $0.15/1M input and $0.6/1M output

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. This analysis breaks down the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
* **Input**: $0.4 per 1M tokens
* **Output**: $2.0 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
* **Cached Tokens**: Since cached input tokens are free, it's highly beneficial to utilize cached tokens whenever possible to minimize input costs.
* **Batch API Savings**: Although batch input is free, the primary cost savings come from reducing the number of API calls. This can be achieved by batching multiple requests together, reducing the overall number of calls and consequently the output costs.

#### Cost at Scale
The cost of using Mistral Medium 3 at different scales is as follows:
* **1,000 calls (avg 500 tokens)**: $1.2
* **10,000 calls**: $12.0
* **100,000 calls**: $120.0

These costs can be broken down into input and output costs. Assuming an average of 500 tokens per call:
* **1,000 calls**: 500,000 tokens
	+ Input cost: 500,000 tokens / 1,000,000 tokens per $0.4 = $0.2
	+ Output cost: assuming an average output of 100 tokens per call (conservative estimate), 100,000 tokens / 1,000,000 tokens per $2.0 = $0.2 (underestimation, as actual output cost may vary)
	+ Total cost

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
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. The model's pricing is as follows:
- Input: $0.4 per 1M tokens
- Output: $2.0 per 1M tokens

#### Benchmark Scores
The model's performance is measured by the following benchmark scores:
- **MMLU (Massive Multitask Language Understanding)**: 80.0
  - MMLU measures a model's ability to understand and generate human-like text across a wide range of tasks and topics. A higher MMLU score indicates better language understanding capabilities.
- **HumanEval**: 77.5
  - HumanEval evaluates a model's ability to generate code that is both correct and readable. A higher HumanEval score suggests better coding capabilities.
- **LMSYS Arena ELO**: 1200
  - LMSYS Arena ELO measures a model's performance in a competitive environment, where it is pitted against other models in various tasks. A higher ELO score indicates better overall performance.

#### Real-World Implications
These benchmark scores have significant implications for real-world use cases:
- **Coding and Analysis**: With a high HumanEval score, Mistral Medium 3 is well-suited for coding tasks, such as code generation and analysis.
- **Text and Vision Tasks**: The model's high MMLU score and support for vision tasks make it a good fit for applications involving text and image processing.
- **Content Generation**:

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

Mistral Medium 3 offers a balance between input and output costs, while Claude 3.5 Haiku is the most expensive option. GPT-4o Mini, on the other hand, is the most cost-effective choice.

#### Performance Trade-offs
The performance of each model can be evaluated using the provided benchmarks:
* **Mistral Medium 3**:
  + MMLU: 80.0
  + HumanEval: 77.5
  + LMSYS Arena ELO: 1200
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

While the exact performance of Claude 3.5 Haiku and GPT-4o Mini is not available, Mistral Medium 3 demonstrates strong capabilities in coding, analysis, and vision tasks.

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
* RAG
* Summarization
* Vision tasks
* Content generation
* Function calling

However, it is not recommended for:
* Frontier reasoning
* Bulk cheap

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful language model with a wide range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. Released on 2025-04-17, this model is best suited for tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling.

### Top 5 Best Use Cases for Mistral Medium 3
Based on its capabilities and limitations, here are the top 5 best use cases for Mistral Medium 3:

1. **Coding and Software Development**: With its strong performance in coding tasks, Mistral Medium 3 can be used for code completion, code review, and code generation. For example, you can use it to integrate with OpenRouter for automated code review:
    ```python
import openrouter

# Initialize Mistral Medium 3 model
model = mistralai.MistralMedium3()

# Define a code review function
def review_code(code):
    # Use Mistral Medium 3 to review the code
    output = model(code)
    # Use OpenRouter to analyze the output
    analysis = openrouter.analyze(output)
    return analysis

# Test the code review function
code = "def hello_world(): print('Hello World!')"
analysis = review_code(code)
print(analysis)
```
2. **Text Analysis and Summarization**: Mistral Medium 3 can be used for text analysis and summarization tasks, such as summarizing long documents or analyzing customer feedback. For example:
    ```python
import mistralai

# Initialize Mistral Medium 3 model
model = mistralai.MistralMedium3()

# Define a text summarization function
def summarize_text(text):
    # Use Mistral Medium 3 to summarize the text
    summary = model(text)
    return summary

# Test

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
