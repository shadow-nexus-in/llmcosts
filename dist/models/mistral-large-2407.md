# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-27
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly in coding, analysis, and multilingual tasks. This model boasts an impressive architecture that supports various capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. With a context window of 131,072 tokens and a maximum output of 4,096 tokens, Mistral Large 2 is well-suited for tasks that require in-depth understanding and generation of content.

### Technical Strengths and Use Cases
Mistral Large 2 demonstrates its strengths through its benchmark scores: 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These scores indicate the model's proficiency in handling complex tasks, coding challenges, and multilingual inputs. Its primary use cases include coding assistance, in-depth analysis, and tasks that involve function calling, making it a valuable tool for developers and researchers. However, it's worth noting that Mistral Large 2 is not recommended for tasks that require embeddings, bulk processing at a low cost, real-time responses under 100ms, or vision-heavy applications.

### Pricing and Cost Considerations
The pricing model for Mistral Large 2 is based on input and output tokens, with costs of $3.0 per 1M input tokens and $9.0 per 1M output tokens. There are no specified costs for cached input or batch input. To give developers a better understanding of the costs involved, examples are provided: 1,000 calls averaging 500 tokens cost $6.0, 10,000 calls cost $60.0, and 100,000 calls cost $600.0. When comparing Mistral Large 2

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
Mistral Large 2 is a premium model offered by Mistral AI, released on 2024-07-24. This analysis will delve into the cost structure, usage scenarios, and cost savings opportunities for this model.

#### Cost Structure
The pricing for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### Cost Savings Opportunities
* **Cached Tokens**: Since cached input tokens are free, it is recommended to use cached tokens whenever possible to reduce costs.
* **Batch API**: Batch input is also free, which means that batching API calls can lead to significant cost savings.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* **1,000 API calls** (avg 500 tokens): $6.0
* **10,000 API calls**: $60.0
* **100,000 API calls**: $600.0

These costs can be broken down into input and output costs. Assuming an average of 500 tokens per call, the total number of tokens for each scenario would be:
* 1,000 calls: 500,000 tokens
* 10,000 calls: 5,000,000 tokens
* 100,000 calls: 50,000,000 tokens

Using the pricing structure, we can estimate the input and output costs:
* 1,000 calls: (500,000 tokens / 1,000,000) \* $3.0 (input) + (assuming 100,000 output tokens / 1,000,000) \* $9.0 (output) = $1.5 + $0

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 84.0 |
| HumanEval | 92.0 |
| LMSYS Arena ELO | 1225 |
| ARC | 93.0 |

## Benchmark Analysis
### Analysis of Mistral Large 2 Benchmark Performance
The Mistral Large 2 model, released by Mistral AI on 2024-07-24, is a premium, non-open-source model with a context window of 131,072 tokens and a maximum output of 4,096 tokens. 

#### Benchmark Scores
The model's performance is measured by the following benchmark scores:
* **MMLU (Massive Multitask Language Understanding)**: 84.0, indicating the model's ability to understand and process a wide range of natural language tasks.
* **HumanEval**: 92.0, measuring the model's ability to evaluate and execute human-written code, with higher scores indicating better performance.
* **LMSYS Arena ELO**: 1225, representing the model's competitive ranking in the LMSYS Arena, a platform for evaluating language models. A higher ELO score indicates better performance compared to other models.
* **GSM8K**: 93.0, evaluating the model's performance on math problems, with higher scores indicating better math reasoning abilities.

#### Real-World Implications
These benchmark scores have significant implications for real-world use:
* The high **HumanEval** score (92.0) suggests that Mistral Large 2 is well-suited for coding and programming tasks, making it a strong choice for applications that require code generation or evaluation.
* The **MMLU** score (84.0) indicates that the model has a good understanding of natural language, but may not be the best choice for extremely complex or nuanced tasks.
* The **LMSYS Arena ELO** score (1225) suggests that Mistral Large 2 is a competitive model,

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, a premium model provided by Mistral AI, is a powerful language model with a wide range of capabilities, including text, vision, function calling, and more. In this comparison, we will evaluate Mistral Large 2 against its top competitor, GPT-4o, in terms of pricing, performance, and use cases.

#### Pricing Comparison
The pricing for Mistral Large 2 and GPT-4o is as follows:
* Mistral Large 2:
	+ Input: $3.0 per 1M tokens
	+ Output: $9.0 per 1M tokens
* GPT-4o:
	+ Input: $2.5 per 1M tokens
	+ Output: $10.0 per 1M tokens

Mistral Large 2 is more expensive than GPT-4o in terms of input tokens, but slightly cheaper in terms of output tokens.

#### Performance Comparison
The performance of Mistral Large 2 and GPT-4o can be evaluated based on their benchmark scores:
* Mistral Large 2:
	+ MMLU: 84.0
	+ HumanEval: 92.0
	+ LMSYS Arena ELO: 1225
	+ GSM8K: 93.0
* GPT-4o: No benchmark scores provided

Based on the available data, Mistral Large 2 has a strong performance profile, with high scores in multiple benchmarks.

#### Context and Limits
The context window and maximum output of Mistral Large 2 are:
* Context Window: 131,072 tokens
* Max Output: 4,096 tokens

These limits are not provided for GPT-4o, making it difficult to compare the two models in terms of context and output capabilities.

#### Capabilities and Use Cases
Mistral Large 2 has a wide range of capabilities, including:
* Text
* Vision
* Function calling
* JSON mode
* Streaming
* System prompts

It is best suited for use cases such as:
* Coding
* Analysis
* RAG
* Agents
* Multilingual
* Function calling

On the other hand, GPT-4o's capabilities and use cases are not provided.

#### Cost Examples
The cost of using Mistral Large 2 can

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. With its robust capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, it is best suited for tasks such as coding, analysis, RAG (Retrieve, Augment, Generate), agents, multilingual support, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Given its strengths and pricing structure, here are the top 5 best use cases for Mistral Large 2, along with specific code integration examples mentioning OpenRouter:

1. **Coding and Development Assistance**: Mistral Large 2 excels in coding tasks, making it an excellent choice for development assistance. For example, integrating it with OpenRouter for automated code review and suggestion:
    ```python
    import openrouter
    from mistralai import MistralLarge2

    # Initialize Mistral Large 2 model
    model = MistralLarge2()

    # Define a function to get code suggestions
    def get_code_suggestions(prompt):
        # Use OpenRouter to route the prompt to Mistral Large 2
        output = openrouter.route(prompt, model)
        return output

    # Example usage
    prompt = "Write a Python function to sort a list of integers."
    suggestions = get_code_suggestions(prompt)
    print(suggestions)
    ```
    **Cost Estimate**: For 1,000 calls (avg 500 tokens), the cost would be approximately $6.0.

2. **Multilingual Support and Analysis**: With its multilingual capabilities, Mistral Large 2 can be used for text analysis across different languages. Integrating it with OpenRouter for multilingual text analysis:
    ```python
    import openrouter
    from mistralai import MistralLarge2

    # Initialize Mistral

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
