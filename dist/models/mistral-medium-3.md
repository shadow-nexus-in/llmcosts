# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-29
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance between performance and cost. This model is not open source, and its pricing is structured around input and output tokens. Developers are charged $0.4 per 1 million input tokens and $2.0 per 1 million output tokens. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, Mistral Medium 3 is designed to handle a wide range of tasks, from coding and analysis to vision tasks and content generation.

### Architecture and Strengths
The architecture of Mistral Medium 3 supports multiple capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. Its strengths are reflected in its benchmark scores, with an MMLU score of 80.0, a HumanEval score of 77.5, and an LMSYS Arena ELO score of 1200. These scores indicate that Mistral Medium 3 is well-suited for tasks that require complex reasoning and generation. However, it may not be the best choice for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms. With its knowledge cutoff at 2024-11, developers should be aware of the model's limitations when working with more recent data.

### Use Cases and Cost Considerations
Mistral Medium 3 is best used for tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling. The cost of using this model can be estimated based on the number of calls and tokens. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 10,000 calls would cost $12.0, and 100,000 calls would cost $120.

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
Mistral Medium 3 is a mid-tier model provided by Mistral AI, released on 2025-04-17. This model is not open source and offers a range of capabilities, including text, vision, function calling, and more.

#### Cost Structure
The cost structure for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs when the same input is used multiple times. Since cached input is free, it is recommended to use cached tokens whenever possible to minimize costs.

#### Batch API Savings
Batch input is also free, which means that making batch API calls can help reduce costs. By batching multiple requests together, users can avoid paying for input tokens multiple times.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: **$1.2**
* **10,000 calls**: **$12.0**
* **100,000 calls**: **$120.0**

These costs are based on the average number of tokens per call and can be used to estimate the total cost of using the model at scale.

#### Comparison to Competitors
Mistral Medium 3 is priced competitively with other models in the market. For example:
* Claude 3.5 Haiku: **$0.8/1M input**, **$4.0/1M output**
* GPT-4o Mini: **$0.15/1M input**, **$0.6/1M output**

Overall,

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
The Mistral Medium 3 model, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. The model is not open source.

#### Pricing
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Benchmark Performance
The benchmark performance of Mistral Medium 3 is measured by the following metrics:
* **MMLU (Massive Multitask Language Understanding)**: 80.0 - This score indicates the model's ability to understand and generate human-like language across a wide range of tasks. A higher MMLU score suggests better language understanding capabilities.
* **HumanEval**: 77.5 - This score evaluates the model's ability to write correct and functional code in response to a given prompt. A higher HumanEval score indicates better coding capabilities.
* **LMSYS Arena ELO**: 1200 - This score measures the model's performance in a competitive arena, where it is pitted against other models in a series of tasks. A higher LMSYS Arena ELO score suggests better overall performance and adaptability.

#### Real-World Implications
The benchmark performance of Mistral Medium 3 has the following implications for real-world use:
* **Coding and analysis**: With a high HumanEval score, Mistral Medium 3

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a unique set of capabilities and pricing. This comparison will delve into the details of Mistral Medium 3 and its top competitors, Claude 3.5 Haiku and GPT-4o Mini, highlighting their differences in pricing, performance, and use cases.

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

Mistral Medium 3 offers a balanced pricing approach, with input costs 50% of Claude 3.5 Haiku and output costs 3.33 times that of GPT-4o Mini.

#### Performance Comparison
The performance of each model can be evaluated using various benchmarks:
* Mistral Medium 3:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* Claude 3.5 Haiku and GPT-4o Mini benchmarks are not provided for direct comparison.

However, based on the available data, Mistral Medium 3 demonstrates strong performance in coding, analysis, and vision tasks.

#### Context and Limits
The context window and maximum output for Mistral Medium 3 are:
* Context Window: 131,072 tokens
* Max Output: 16,384 tokens

These limits are not provided for Claude 3.5 Haiku and GPT-4o Mini, making it difficult to compare their capabilities directly.

#### Capabilities and Use Cases
Mistral Medium 3 supports a wide range of capabilities, including:
* text
* vision
* function_calling
* json_mode
* streaming
* system_prompts

It is best suited for tasks such as:
* coding
* analysis
* rag
* summarization
* vision

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. This model is best suited for tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling.

### Top 5 Best Use Cases for Mistral Medium 3
Based on its capabilities and limitations, here are the top 5 best use cases for Mistral Medium 3:

1. **Coding and Software Development**: With its strong coding capabilities, Mistral Medium 3 can be used for tasks such as code completion, code review, and code generation. For example, you can use it to integrate with OpenRouter to generate code snippets for routing configurations.
   ```python
import openrouter

# Define the routing configuration
config = {
    "router": "Cisco",
    "version": "15.2",
    "interfaces": [
        {"name": "GigabitEthernet0/0", "ip": "10.0.0.1/24"}
    ]
}

# Use Mistral Medium 3 to generate the code snippet
mistral_medium_3 = MistralAI(model="mistral-medium-3")
code_snippet = mistral_medium_3.generate_code(config)

print(code_snippet)
```

2. **Text Analysis and Summarization**: Mistral Medium 3 can be used for text analysis and summarization tasks such as sentiment analysis, entity recognition, and text summarization. For example, you can use it to analyze customer feedback and generate a summary of the key points.
   ```python
import mistralai

# Define the text to analyze
text = "This product is amazing! The customer service is top-notch."

# Use Mistral Medium 3 to analyze the text

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
