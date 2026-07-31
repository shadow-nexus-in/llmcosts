# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-31
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. This model boasts an impressive architecture that supports a wide range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. With a context window of 131,072 tokens and a maximum output of 4,096 tokens, Mistral Large 2 is well-suited for complex tasks that require a deep understanding of context and the ability to generate lengthy, coherent responses.

### Strengths and Use Cases
Mistral Large 2 demonstrates its strengths through various benchmarks, achieving scores of 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These results indicate that the model excels in coding, analysis, and other tasks that require a high level of cognitive ability. Its capabilities make it an ideal choice for applications such as coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual tasks, and function calling. However, it is not recommended for tasks that require embeddings, bulk processing at a low cost, real-time responses under 100ms, or vision-heavy workloads.

### Pricing and Cost Considerations
The pricing for Mistral Large 2 is structured as follows: $3.0 per 1M input tokens and $9.0 per 1M output tokens. There are no specified costs for cached input or batch input. To put this into perspective, the cost examples provided indicate that 1,000 calls with an average of 500 tokens would cost $6.0, while 10,000 calls would cost $60.0, and 100,000 calls would cost $600.0. When comparing Mistral Large 2 to its top competitors, such as

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $3.0 |
| Output | $9.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Mistral Large 2 Pricing Analysis
#### Overview
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. The pricing structure is based on input and output tokens, with specific considerations for cached and batch inputs.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
- **Input**: $3.0 per 1M tokens
- **Output**: $9.0 per 1M tokens
- **Cached Input**: No additional cost ($None per 1M tokens)
- **Batch Input**: No additional cost ($None per 1M tokens)

#### Using Cached Tokens
Cached tokens can be utilized without incurring additional costs. This feature is beneficial for applications where the same input tokens are repeatedly used, as it eliminates the need for redundant input token costs.

#### Batch API Savings
While the pricing data does not specify a direct discount for batch inputs, the absence of an additional cost for batch inputs implies that the standard input cost applies. However, the lack of a specific batch discount suggests that savings may not be directly proportional to the batch size. It is essential to consider the average token count per call when estimating costs for batch API usage.

#### Cost at Scale
To understand the cost implications of using Mistral Large 2 at scale, let's examine the provided cost examples:
- **1,000 calls (avg 500 tokens)**: $6.0
- **10,000 calls**: $60.0
- **100,000 calls**: $600.0

These examples illustrate a linear cost scaling, where the cost increases directly with the number of API calls. This linear relationship suggests that the cost per call remains constant, regardless of the scale.

#### Comparison with Top Competitors
Mistral Large 2's pricing can

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 84.0 |
| HumanEval | 92.0 |
| LMSYS Arena ELO | 1225 |
| ARC | 93.0 |

## Benchmark Analysis
### Mistral Large 2 Benchmark Performance Analysis
#### Overview
Mistral Large 2, a premium model provided by Mistral AI, demonstrates strong performance across various benchmarks. Released on 2024-07-24, this model is well-suited for tasks such as coding, analysis, and function calling.

#### Benchmark Scores
The model's performance can be evaluated through the following benchmark scores:
* **MMLU (Massive Multitask Language Understanding)**: 84.0 - This score indicates the model's ability to understand and generate human-like text across a wide range of tasks and domains. A higher MMLU score suggests better performance in tasks that require a deep understanding of language.
* **HumanEval**: 92.0 - This score measures the model's ability to generate correct and functional code in response to programming prompts. A high HumanEval score indicates strong coding capabilities.
* **LMSYS Arena ELO**: 1225 - This score represents the model's performance in a competitive arena, where it is pitted against other models in a variety of tasks. A higher ELO score suggests better overall performance and adaptability.

#### Real-World Implications
These benchmark scores have significant implications for real-world use:
* **Coding and Development**: With a high HumanEval score, Mistral Large 2 is well-suited for coding tasks, such as generating functions or classes, and can be a valuable tool for developers.
* **Analysis and Reasoning**: The model's strong MMLU score indicates its ability to understand complex text and generate coherent responses, making it suitable for tasks that require in-depth analysis and reasoning.
* **Multilingual Support**: As a multilingual model, Mistral Large 

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. This comparison will focus on its pricing, performance, and use cases versus its top competitors, specifically GPT-4o.

#### Pricing Comparison
| Model | Input Price per 1M tokens | Output Price per 1M tokens |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens. In contrast, GPT-4o is priced at $2.5 per 1M input tokens but $10.0 per 1M output tokens. For applications where input token usage is high and output is relatively low, GPT-4o might be more cost-effective. However, for scenarios with significant output, Mistral Large 2 offers a better price point.

#### Performance Trade-offs
Mistral Large 2 boasts impressive benchmarks:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

These scores indicate strong performance in coding, analysis, and other cognitive tasks. While specific benchmarks for GPT-4o are not provided, the choice between Mistral Large 2 and GPT-4o may depend on the specific requirements of the application, such as the need for function calling, multilingual support, or vision capabilities.

#### Context and Limits
Mistral Large 2 has a context window of 131,072 tokens and a max output of 4,096 tokens, with a knowledge cutoff of 2024-07. These specifications suggest it is well-suited for complex, long-form text processing and generation tasks. GPT-4o's specifications are not provided, but this information would be crucial in determining which model is more appropriate for specific use cases.

#### Capabilities and Use Cases
Mistral Large 2 is best for:
- Coding

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. With its robust capabilities in text, vision, function calling, JSON mode, streaming, and system prompts, it is best suited for tasks such as coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual support, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Given its strengths and pricing model, here are the top 5 best use cases for Mistral Large 2, along with specific code integration examples mentioning OpenRouter:

1. **Coding and Development**: Mistral Large 2 excels in coding tasks, making it ideal for automated code generation, code review, and code optimization. 
    ```python
    import openrouter
    model = openrouter.load_model("mistralai/mistral-large-2407")
    prompt = "Write a Python function to sort a list of integers."
    response = model.generate_text(prompt)
    print(response)
    ```
    **Cost Estimate**: For 1,000 coding requests (avg 500 tokens), the estimated cost would be $6.0.

2. **Complex Analysis**: With its large context window of 131,072 tokens, Mistral Large 2 is well-suited for complex analysis tasks that require understanding and processing long pieces of text.
    ```python
    import openrouter
    model = openrouter.load_model("mistralai/mistral-large-2407")
    prompt = "Analyze the themes present in the novel 'To Kill a Mockingbird'."
    response = model.generate_text(prompt)
    print(response)
    ```
    **Cost Estimate**: For in-depth analysis of 100 documents (avg 10,000 tokens each), considering input and output costs, the estimated cost would be significantly higher due to

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
