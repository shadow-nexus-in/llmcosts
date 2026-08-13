# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-13
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. This model boasts an impressive set of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. Its architecture is designed to support a wide range of applications, particularly excelling in coding, analysis, retrieval-augmented generation (RAG), agents, multilingual tasks, and function calling. With a context window of 131,072 tokens and a maximum output of 4,096 tokens, Mistral Large 2 is well-suited for complex and nuanced tasks.

### Technical Strengths and Use Cases
The technical strengths of Mistral Large 2 are reflected in its benchmark scores: MMLU at 84.0, HumanEval at 92.0, LMSYS Arena ELO at 1225, and GSM8K at 93.0. These scores indicate the model's proficiency in understanding and generating human-like text, as well as its ability to perform well in coding and mathematical tasks. However, it's worth noting that Mistral Large 2 is not ideal for embeddings, bulk cheap processing, real-time applications requiring sub-100ms responses, or vision-heavy tasks. Its pricing model, with input costing $3.0 per 1M tokens and output costing $9.0 per 1M tokens, positions it as a premium offering, comparable to but differently priced than competitors like GPT-4o.

### Pricing and Cost Considerations
Developers considering Mistral Large 2 should be aware of its pricing structure and how it might impact their application's cost. For example, 1,000 calls averaging 500 tokens each would cost $6.0, scaling to $60.0 for 10,000 calls and $600.0 for 100,000 calls. In comparison, GPT

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

#### When to Use Cached Tokens
Cached tokens can be utilized without incurring any additional costs. This feature is beneficial when the same input tokens are used repeatedly, as it eliminates the need to pay for input tokens multiple times. However, the effectiveness of cached tokens depends on the specific use case and the frequency of repeated input tokens.

#### Batch API Savings
The pricing data does not specify any additional cost savings for batch inputs. This implies that the cost of processing batch inputs is the same as processing individual inputs, based on the input and output token counts.

#### Cost at Scale
The cost of using Mistral Large 2 at scale can be estimated based on the provided cost examples:
- **1,000 calls (avg 500 tokens)**: $6.0
- **10,000 calls**: $60.0
- **100,000 calls**: $600.0

To calculate the cost per call, we can divide the total cost by the number of calls:
- **1,000 calls**: $6.0 / 1,000 = $0.006 per call
- **10,000 calls**: $60.0 / 10,000 = $0.

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 84.0 |
| HumanEval | 92.0 |
| LMSYS Arena ELO | 1225 |
| ARC | 93.0 |

## Benchmark Analysis
### Mistral Large 2 Benchmark Performance Analysis
The Mistral Large 2 model, released by Mistral AI on 2024-07-24, is a premium, non-open-source model with a context window of 131,072 tokens and a maximum output of 4,096 tokens. 

#### Pricing
The pricing for Mistral Large 2 is as follows:
* Input: **$3.0 per 1M tokens**
* Output: **$9.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Benchmark Scores
The model's benchmark performance is measured by the following scores:
* **MMLU: 84.0** - The MMLU (Massive Multitask Language Understanding) benchmark evaluates a model's ability to perform a wide range of natural language understanding tasks. A higher MMLU score indicates better performance in tasks such as text classification, sentiment analysis, and question answering.
* **HumanEval: 92.0** - The HumanEval benchmark assesses a model's ability to generate code that is correct and functional. A higher HumanEval score indicates better performance in coding tasks.
* **LMSYS Arena ELO: 1225** - The LMSYS Arena ELO score is a measure of a model's performance in a competitive arena, where models are pitted against each other to solve tasks. A higher ELO score indicates better performance in a wide range of tasks.

#### Real-World Implications
The benchmark scores of Mistral Large 2 have the following implications for real-world use:
* **Coding and Analysis**: With a high

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts, making it best suited for tasks like coding, analysis, and multilingual applications.

#### Pricing Comparison
Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens. In comparison, its top competitor, GPT-4o, is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens.

| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

#### Performance Trade-offs
Mistral Large 2 has a context window of 131,072 tokens and a maximum output of 4,096 tokens, with a knowledge cutoff of 2024-07. Its performance is benchmarked as follows:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

While specific benchmark comparisons with GPT-4o are not provided, the choice between Mistral Large 2 and GPT-4o will depend on the specific requirements of the application, including budget, performance needs, and the types of tasks being performed.

#### Cost Examples
The cost of using Mistral Large 2 can be estimated as follows:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100,000 calls: $600.0

These costs are based on the input and output pricing and do not account for potential discounts or additional fees associated with GPT-4o or other competitors.

#### Choosing the Right Model
- **Mistral Large 2** is best for applications requiring advanced capabilities like function calling, multilingual support, and coding analysis, where its premium features and performance justify the

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. With its impressive capabilities in text, vision, function calling, JSON mode, streaming, and system prompts, it's best suited for tasks such as coding, analysis, RAG, agents, multilingual support, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Given its strengths and pricing model, here are the top 5 best use cases for Mistral Large 2, along with specific code integration examples mentioning OpenRouter:

1. **Coding and Development**: Mistral Large 2 excels in coding tasks, making it an ideal choice for automated coding, code review, and code generation. 
    ```python
    import openrouter
    model = openrouter.load_model("mistralai/mistral-large-2407")
    prompt = "Write a Python function to sort a list of integers."
    response = model.generate_text(prompt)
    print(response)
    ```
2. **Complex Analysis**: With its large context window of 131,072 tokens, Mistral Large 2 is well-suited for complex analysis tasks that require understanding and processing long pieces of text.
    ```python
    import openrouter
    model = openrouter.load_model("mistralai/mistral-large-2407")
    prompt = "Analyze the following text and provide a summary: [insert long text here]"
    response = model.generate_text(prompt)
    print(response)
    ```
3. **RAG (Retrieval-Augmented Generation)**: Mistral Large 2 supports RAG, which is useful for tasks that require generating text based on external knowledge.
    ```python
    import openrouter
    model = openrouter.load_model("mistralai/mistral-large-2407")
    prompt = "Use RAG

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
