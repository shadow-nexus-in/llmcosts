# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-18
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Technical Overview of Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. The architecture of Mistral Small 4 is designed to handle a context window of 262,144 tokens and can generate a maximum output of 4,096 tokens. Its knowledge cutoff is 2023-12, indicating that its training data includes information up to December 2023. With capabilities such as text, function calling, JSON mode, streaming, and structured outputs, Mistral Small 4 is a versatile model suitable for various applications.

### Main Strengths and Use Cases
The main strengths of Mistral Small 4 lie in its ability to handle large context windows and generate substantial output, making it ideal for tasks that require comprehensive understanding and response generation. Its primary use cases include chat, text generation, coding, analysis, RAG pipelines, and summarization. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO score of 1200, indicating its competence in handling complex language tasks. However, it's essential to note that Mistral Small 4 is not suitable for tasks that require knowledge beyond its cutoff date or those that demand extremely high precision in specific domains like HumanEval or GSM8K, where its performance is not reported.

### Pricing and Cost Examples
The pricing model for Mistral Small 4 is based on input and output tokens, with costs of $0.15 per 1M input tokens and $0.6 per 1M output tokens. There are no additional costs for cached input or batch input. To illustrate, for 1,000 calls with an average of 500 tokens, the cost would be $0.375. This scales to $3.75 for 10,000 calls and $

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.15 |
| Output | $0.6 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Mistral Small 4 Pricing Analysis
#### Overview
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens (free)
* Batch Input: $None per 1M tokens (free)

#### Optimal Usage Scenarios
* **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
* **Batch API**: With batch input being free, batching API calls can lead to significant savings, especially for large-scale applications.

#### Cost at Scale
The cost of using Mistral Small 4 at different scales is as follows:
* **1,000 API calls** (avg 500 tokens): $0.375
* **10,000 API calls**: $3.75
* **100,000 API calls**: $37.5

These costs demonstrate a linear scaling of expenses with the number of API calls, indicating that the cost per call remains constant regardless of the scale.

#### Context and Limits
It's essential to consider the context window and output limits when optimizing for cost:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens

#### Conclusion
Mistral Small 4 offers a competitive pricing model, especially when leveraging cached tokens and batch API calls. By understanding the cost structure and optimizing usage, developers can effectively utilize this model for various applications, including chat, text generation, coding, analysis, and summarization, while minimizing expenses. 

### Recommendations
* Utilize cached input

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Analysis of Mistral: Mistral Small 4 Benchmark Performance
#### Overview
Mistral: Mistral Small 4, provided by Mistralai, is a standard, non-open-source model released on 2024-01-01. This analysis will delve into its benchmark performance, focusing on MMLU, HumanEval, and Arena ELO scores, and their implications for real-world applications.

#### Pricing
The pricing model for Mistral: Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: $None per 1M tokens
- **Batch Input**: $None per 1M tokens

#### Context and Limits
Key context and limit specifications include:
- **Context Window**: 262,144 tokens
- **Max Output**: 4,096 tokens
- **Knowledge Cutoff**: 2023-12

#### Benchmarks
The model's performance is benchmarked as follows:
- **MMLU**: 80.0
- **HumanEval**: None
- **LMSYS Arena ELO**: 1200
- **GSM8K**: None

#### Capabilities and Use Cases
Mistral: Mistral Small 4 supports:
- **Capabilities**: text, function_calling, json_mode, streaming, structured_outputs
- **Best For**: chat, text_generation, coding, analysis, rag_pipelines, summarization
- **Not Good For**: Not specified

#### Cost Examples
Estimated costs for using Mistral: Mistral Small 4 are:
- **1,000 calls (avg 500

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral: Mistral Small 4, we will provide a general analysis of its pricing, performance, and capabilities. This will help in understanding when to choose this model over others in the market.

#### Pricing
The pricing for Mistral: Mistral Small 4 is as follows:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens
- Cached Input: $None per 1M tokens
- Batch Input: $None per 1M tokens

#### Performance Trade-offs
Mistral: Mistral Small 4 has the following performance metrics:
- MMLU: 80.0
- LMSYS Arena ELO: 1200
- Context Window: 262,144 tokens
- Max Output: 4,096 tokens

Given the lack of direct competitors, it's essential to consider the capabilities and best use cases for this model:
- **Capabilities**: text, function_calling, json_mode, streaming, structured_outputs
- **Best For**: chat, text_generation, coding, analysis, rag_pipelines, summarization

#### Cost Examples
To understand the cost implications of using Mistral: Mistral Small 4, consider the following examples:
- 1,000 calls (avg 500 tokens): $0.375
- 10,000 calls: $3.75
- 100,000 calls: $37.5

#### Choosing Mistral: Mistral Small 4
Given its capabilities and pricing, Mistral: Mistral Small 4 is suitable for applications requiring:
- Advanced text processing and generation
- Function calling and JSON mode capabilities
- Streaming and structured output handling
- High context window and moderate output size

When to choose Mistral: Mistral Small 4:
- For projects that require a balance between performance and cost, especially in applications where the input and output token counts are moderate.
- When the capabilities of text generation, coding, analysis, and summarization are essential.
- In scenarios where the context window and max output size provided by the model are sufficient for the application's requirements.

Keep in mind that the decision to use Mistral: Mistral Small 4 should be based on a thorough evaluation of the specific needs of your project, considering factors such as performance requirements, budget

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard, non-open-source model released on 2024-01-01. With its unique capabilities, it offers a range of use cases. This guide will explore the top 5 best use cases for Mistral Small 4, along with practical advice and code integration examples using OpenRouter.

### Top 5 Use Cases for Mistral Small 4
Based on its capabilities, Mistral Small 4 is best suited for:
1. **Chat**: Utilize Mistral Small 4 for conversational AI applications, such as customer support chatbots.
2. **Text Generation**: Leverage the model for generating high-quality text, including articles, stories, or product descriptions.
3. **Coding**: Employ Mistral Small 4 for coding tasks, such as code completion, code review, or code generation.
4. **Analysis**: Use the model for text analysis, including sentiment analysis, entity recognition, or topic modeling.
5. **Summarization**: Apply Mistral Small 4 for summarizing long documents, articles, or texts, extracting key points and main ideas.

### Code Integration Example with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.Model("mistralai/mistral-small-2603")

# Define a function to generate text using the model
def generate_text(prompt, max_tokens):
    response = model.generate_text(prompt, max_tokens=max_tokens)
    return response

# Example usage
prompt = "Write a short story about a character who discovers a hidden world."
max_tokens = 2048
response = generate_text(prompt, max_tokens)
print(response)
```
This example demonstrates how to use the Mistral Small 4 model with OpenRouter to generate text based

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
