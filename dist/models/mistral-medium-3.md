# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-06
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance of performance and cost. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, this model is capable of handling complex tasks. The pricing structure is as follows: $0.4 per 1M input tokens and $2.0 per 1M output tokens. Notably, Mistral Medium 3 is not open source.

### Architecture and Strengths
The architecture of Mistral Medium 3 supports a wide range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. Its strengths lie in its ability to perform tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling. The model's performance is backed by benchmarks, including an MMLU score of 80.0, a HumanEval score of 77.5, and an LMSYS Arena ELO of 1200. However, it is not well-suited for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms.

### Use Cases and Cost Considerations
Developers can leverage Mistral Medium 3 for various applications, considering its capabilities and limitations. For example, the model can be used for coding tasks, analysis, and content generation. The cost of using Mistral Medium 3 can be estimated based on the provided pricing structure. For instance, 1,000 calls with an average of 500 tokens would cost $1.2, while 10,000 calls would cost $12.0, and 100,000 calls would cost $120.0. When comparing Mistral Medium 3 to its competitors, such as Claude 3.5 Haiku and GPT-4o Mini,

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and scaling costs for this model.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
- **Input**: $0.4 per 1M tokens
- **Output**: $2.0 per 1M tokens
- **Cached Input**: $None per 1M tokens (free)
- **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
- **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
- **Batch API**: Given that batch input is free, batching API calls can significantly reduce costs, especially for large-scale applications.

#### Cost at Scale
The costs for Mistral Medium 3 at different scales are as follows:
- **1,000 calls (avg 500 tokens)**: $1.2
- **10,000 calls**: $12.0
- **100,000 calls**: $120.0

These costs indicate a linear scaling of expenses with the number of API calls, suggesting that the cost per call remains constant regardless of the scale.

#### Comparison with Competitors
Mistral Medium 3's pricing is competitive, especially considering its capabilities and performance benchmarks. For comparison:
- **Claude 3.5 Haiku**: $0.8/1M input, $4.0/1M output
- **GPT-4o Mini**: $0.15/1M input, $0.6/1M output

While GPT-4o Mini offers significantly lower input costs, the output costs of Mistral Medium 3 are more competitive, especially when considering

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
Mistral Medium 3, a mid-tier model provided by Mistral AI, offers a balance of performance and cost. Released on 2025-04-17, this model is not open source.

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
Mistral Medium 3 has the following benchmark scores:
* **MMLU: 80.0** - This score indicates the model's performance on a set of tasks that require a combination of natural language understanding and generation. A higher score means better performance.
* **HumanEval: 77.5** - This score measures the model's ability to generate code that is correct and functional. A higher score indicates better coding abilities.
* **LMSYS Arena ELO: 1200** - This score represents the model's performance in a competitive arena, where it is pitted against other models. A higher score means better performance relative to other models.

#### Real-World Implications
The benchmark scores suggest that Mistral Medium 3 is suitable for tasks that require:
* Strong natural language understanding and generation (MMLU: 80.0)


## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will delve into the pricing, performance, and capabilities of Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

#### Pricing Comparison
The pricing models for each are as follows:
- **Mistral Medium 3**:
  - Input: $0.4 per 1M tokens
  - Output: $2.0 per 1M tokens
- **Claude 3.5 Haiku**:
  - Input: $0.8 per 1M tokens
  - Output: $4.0 per 1M tokens
- **GPT-4o Mini**:
  - Input: $0.15 per 1M tokens
  - Output: $0.6 per 1M tokens

#### Performance Trade-offs
- **Mistral Medium 3**: Offers a balance between price and performance, with benchmarks showing an MMLU score of 80.0 and a HumanEval score of 77.5.
- **Claude 3.5 Haiku**: Pricier than Mistral Medium 3 but may offer superior performance in certain tasks, considering its higher cost.
- **GPT-4o Mini**: The most cost-effective option, with significantly lower input and output costs, but its performance may not match that of Mistral Medium 3 or Claude 3.5 Haiku in complex tasks.

#### Capabilities and Best Use Cases
- **Mistral Medium 3**: Suitable for coding, analysis, RAG, summarization, vision tasks, content generation, and function calling. Not recommended for frontier reasoning, bulk cheap tasks, simple classification, or real-time sub-100ms tasks.
- **Claude 3.5 Haiku** and **GPT-4o Mini**: Specific capabilities and best use cases are not provided, but their pricing suggests Claude 3.5 Haiku may be positioned for high-end applications, while GPT-4o Mini is geared towards cost-sensitive use cases.

#### Cost Examples
For Mistral Medium 3:
- 1,000 calls

## Best Use Cases
### Practical Advice on Top 5 Best Use Cases for Mistral Medium 3
Mistral Medium 3, a mid-tier model provided by Mistral AI, offers a balance of capabilities and pricing. With its release on 2025-04-17, it has established itself as a versatile tool for various applications. Here are the top 5 best use cases for Mistral Medium 3, along with specific code integration examples mentioning OpenRouter:

#### 1. **Coding and Analysis**
Mistral Medium 3 excels in coding and analysis tasks, making it an ideal choice for developers and data analysts. Its `function_calling` capability allows for seamless integration with OpenRouter, enabling the execution of custom functions within the model.
```python
import openrouter

# Initialize OpenRouter with Mistral Medium 3
openrouter.init(model="mistralai/mistral-medium-3")

# Define a custom function to analyze data
def analyze_data(data):
    # Use Mistral Medium 3 to analyze the data
    result = openrouter.call(function_name="analyze", input_data=data)
    return result

# Call the custom function with sample data
data = {"key": "value"}
result = analyze_data(data)
print(result)
```
#### 2. **Summarization and Content Generation**
With its `summarization` and `content_generation` capabilities, Mistral Medium 3 can be used to create concise summaries and generate high-quality content. Its `json_mode` capability allows for easy integration with OpenRouter, enabling the processing of JSON data.
```python
import openrouter
import json

# Initialize OpenRouter with Mistral Medium 3
openrouter.init(model="mistralai/mistral-medium-3")

# Define a custom function to summarize text
def summarize_text(text):
    # Use Mistral Medium 3 to summarize the text
    input_data = {"text": text}
    result = openrouter

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
