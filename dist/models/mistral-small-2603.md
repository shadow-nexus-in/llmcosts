# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-13
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard tier language model released on 2024-01-01. This model is not open source. The architecture of Mistral Small 4 is designed to handle a context window of up to 262,144 tokens and can generate a maximum output of 4,096 tokens. With a knowledge cutoff of 2023-12, this model is well-suited for a variety of natural language processing tasks.

### Strengths and Use Cases
The main strengths of Mistral Small 4 lie in its capabilities, which include text, function calling, JSON mode, streaming, and structured outputs. These features make it an ideal choice for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization. The model's pricing structure is based on input and output tokens, with costs of $0.15 per 1M input tokens and $0.6 per 1M output tokens. This pricing model allows developers to estimate costs based on their specific use cases. For example, 1,000 calls with an average of 500 tokens would cost $0.375, while 10,000 calls would cost $3.75.

### Technical Specifications and Competitors
From a technical standpoint, Mistral Small 4 has achieved notable benchmarks, including an MMLU score of 80.0 and an LMSYS Arena ELO rating of 1200. While there are no direct competitors listed for this model, its unique combination of capabilities and pricing make it a compelling choice for developers working on a range of NLP tasks. With its robust feature set and flexible pricing structure, Mistral Small 4 is well-positioned to support a variety of applications, from chat and text generation to coding and analysis. As the NLP landscape continues to evolve, models like Mistral Small 4 are

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
The Mistral Small 4 model, provided by Mistralai, is a standard, non-open-source model released on January 1, 2024. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* **Input**: $0.15 per 1M tokens
* **Output**: $0.6 per 1M tokens
* **Cached Input**: No additional cost
* **Batch Input**: No additional cost

#### Optimal Usage Scenarios
To minimize costs, consider the following scenarios:
* **Cached Tokens**: Since there is no additional cost for cached input, it is recommended to use cached tokens whenever possible to reduce input costs.
* **Batch API Savings**: Although there is no explicit cost savings for batch input, batching API calls can still reduce the overall number of calls, resulting in lower output costs.

#### Cost at Scale
The cost of using Mistral Small 4 at scale is as follows:
* **1,000 API calls** (avg 500 tokens): $0.375
* **10,000 API calls**: $3.75
* **100,000 API calls**: $37.5

These costs demonstrate a linear relationship with the number of API calls, indicating that the cost per call remains constant.

#### Conclusion
Mistral Small 4 offers a competitive pricing structure, with opportunities for cost savings through the use of cached tokens and batch API calls. The model's capabilities, including text, function calling, and structured outputs, make it well-suited for applications such as chat, text generation, coding, and analysis. As the number of API calls increases, the total cost scales linearly, making it essential to optimize usage and minimize unnecessary calls to ensure cost-effectiveness.

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Benchmark Analysis
#### Overview
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. It is not open-source and has a specific pricing structure for input and output tokens.

#### Pricing Structure
The pricing for Mistral Small 4 is as follows:
* Input: **$0.15 per 1M tokens**
* Output: **$0.6 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Context and Limits
The model has the following context and limits:
* Context Window: **262,144 tokens**
* Max Output: **4,096 tokens**
* Knowledge Cutoff: **2023-12**

#### Benchmark Performance
The benchmark performance of Mistral Small 4 is as follows:
* MMLU: **80.0**
* HumanEval: **None**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

The MMLU score of 80.0 indicates the model's performance on a specific set of tasks, with higher scores generally indicating better performance. The LMSYS Arena ELO score of 1200 provides a relative ranking of the model's performance compared to other models, with higher scores indicating better performance.

The lack of HumanEval and GSM8K scores makes it difficult to directly compare the model's performance on specific tasks, such as coding and math problem-solving.

#### Real-World Use Implications
The benchmark scores have the following implications for real-world use:
* The MMLU score

## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for the Mistral Small 4 model, we will provide a general comparison framework that can be applied to similar models in the market. This will help in understanding the price differences, performance trade-offs, and scenarios where each model might be preferred.

#### Model Overview
The Mistral Small 4, provided by Mistralai, is a standard-tier model released on 2024-01-01. It is not open-source and has the following pricing structure:
- Input: $0.15 per 1M tokens
- Output: $0.6 per 1M tokens
- Cached Input: $None per 1M tokens
- Batch Input: $None per 1M tokens

#### Performance and Capabilities
The model boasts a context window of 262,144 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2023-12. Its performance benchmarks include:
- MMLU: 80.0
- LMSYS Arena ELO: 1200

It supports various capabilities such as text, function calling, JSON mode, streaming, and structured outputs, making it suitable for applications like chat, text generation, coding, analysis, RAG pipelines, and summarization.

#### Cost Examples
To understand the cost implications, consider the following examples:
- 1,000 calls (avg 500 tokens): $0.375
- 10,000 calls: $3.75
- 100,000 calls: $37.5

#### Comparison Framework
When comparing the Mistral Small 4 with potential competitors, consider the following factors:
1. **Pricing Structure**: Compare the input and output costs per 1M tokens. Models with lower costs might be more economical for large-scale applications.
2. **Performance Benchmarks**: Evaluate the competitors' MMLU, HumanEval, LMSYS Arena ELO, and GSM8K scores to determine their performance relative to the Mistral Small 4.
3. **Context Window and Max Output**: Consider the limitations of each model in terms of context window size and maximum output. Models with larger context windows or higher max output might be more suitable for complex tasks.
4. **Capabilities and Best Use Cases**: Assess the capabilities of each model, such as text, function calling, and streaming, to determine which one aligns best

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and non-open source status, it's essential to understand its best use cases and integration examples.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities, the top 5 best use cases for Mistral Small 4 are:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens, Mistral Small 4 is ideal for generating human-like text and engaging in conversations.
2. **Coding and Analysis**: Its ability to perform function calling and structured outputs makes it suitable for coding tasks, such as code completion and analysis.
3. **Summarization**: Mistral Small 4's text generation capabilities can be leveraged for summarizing long documents and extracting key information.
4. **RAG Pipelines**: Its support for Retrieval-Augmented Generation (RAG) pipelines enables it to generate text based on external knowledge sources.
5. **Streaming**: With its streaming capability, Mistral Small 4 can process and generate text in real-time, making it suitable for applications like live chatbots.

### Code Integration Example with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.Model("mistralai/mistral-small-2603")

# Define a function to generate text
def generate_text(prompt):
    # Use the model to generate text
    output = model.generate_text(prompt, max_length=4096)
    return output

# Test the function
prompt = "Write a short story about a character who discovers a hidden world."
output = generate_text(prompt)
print(output)
```
Note that

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
