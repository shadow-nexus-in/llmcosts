# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-25
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly in coding, analysis, and function calling. This model boasts an impressive architecture with a context window of 131,072 tokens and a maximum output of 4,096 tokens. Its capabilities extend to text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Strengths and Use Cases
Mistral Large 2 demonstrates its strengths through various benchmarks: achieving 84.0 on MMLU, 92.0 on HumanEval, 1225 on LMSYS Arena ELO, and 93.0 on GSM8K. These scores underscore its potential for coding, analysis, and other complex tasks. The model is best utilized for applications involving coding, analysis, retrieval-augmented generation (RAG), agents, multilingual support, and function calling. However, it's not recommended for tasks requiring embeddings, bulk cheap processing, real-time responses under 100ms, or vision-heavy applications.

### Pricing and Cost Efficiency
The pricing model for Mistral Large 2 is structured as follows: $3.0 per 1M input tokens and $9.0 per 1M output tokens. There are no specified costs for cached input or batch input. To illustrate the cost efficiency, consider that 1,000 calls averaging 500 tokens each would cost $6.0, scaling to $60.0 for 10,000 calls and $600.0 for 100,000 calls. In comparison to its top competitor, GPT-4o, which charges $2.5/1M input and $10.0/1M output, Mistral Large 2 offers a competitive pricing strategy, especially considering its robust capabilities and

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
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. The pricing structure is based on input and output tokens.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
* **Input**: $3.0 per 1M tokens
* **Output**: $9.0 per 1M tokens
* **Cached Input**: No additional cost ($None per 1M tokens)
* **Batch Input**: No additional cost ($None per 1M tokens)

This indicates that using cached input tokens does not incur any extra cost, which can be beneficial for applications where the same input is processed multiple times. Similarly, batch input does not have an additional cost, which can lead to significant savings when making multiple API calls.

#### When to Use Cached Tokens
Cached tokens should be utilized when the same input is processed repeatedly. Since there is no additional cost for cached input tokens, this can help reduce the overall cost of using the Mistral Large 2 model.

#### Batch API Savings
The lack of additional cost for batch input suggests that making batch API calls can be an effective way to reduce costs. By processing multiple inputs in a single API call, users can avoid the overhead costs associated with individual API calls.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: $6.0
* **10,000 calls**: $60.0
* **100,000 calls**: $600.0

These costs demonstrate a linear relationship between the number of API calls and the total cost. This suggests that the cost per call remains constant, regardless of the scale.

#### Comparison to Top Competitors


## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 84.0 |
| HumanEval | 92.0 |
| LMSYS Arena ELO | 1225 |
| ARC | 93.0 |

## Benchmark Analysis
### Mistral Large 2 Benchmark Performance Analysis
#### Model Overview
The Mistral Large 2 model, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. It has a context window of 131,072 tokens and can generate up to 4,096 tokens as output.

#### Pricing
The pricing for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Benchmark Performance
The model's benchmark performance is measured across several metrics:
* **MMLU (Massive Multitask Language Understanding)**: 84.0 - This score indicates the model's ability to understand and perform a wide range of natural language processing tasks. A higher score suggests better performance in tasks such as text classification, sentiment analysis, and question answering.
* **HumanEval**: 92.0 - This score evaluates the model's ability to generate human-like code and perform programming tasks. A higher score indicates better performance in coding and programming-related tasks.
* **LMSYS Arena ELO**: 1225 - This score measures the model's performance in a competitive environment, where it is pitted against other models in a series of tasks. A higher ELO score indicates better overall performance and competitiveness.
* **GSM8K**: 93.0 - This score assesses the model's ability to solve math problems and perform quantitative reasoning tasks. A higher score suggests better performance in math-related tasks.

#### Real-World Implications
The benchmark

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, offered by Mistral AI, is a premium, non-open-source model released on 2024-07-24. It boasts an impressive set of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, making it suitable for coding, analysis, RAG, agents, multilingual tasks, and function calling.

#### Pricing Comparison
The pricing for Mistral Large 2 is as follows:
- Input: $3.0 per 1M tokens
- Output: $9.0 per 1M tokens

In comparison, its top competitor, GPT-4o, is priced at:
- Input: $2.5 per 1M tokens
- Output: $10.0 per 1M tokens

#### Performance Trade-offs
Mistral Large 2 demonstrates strong performance across various benchmarks:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

While specific benchmark scores for GPT-4o are not provided, the choice between Mistral Large 2 and GPT-4o will depend on the specific requirements of the task, including budget constraints, performance needs, and the nature of the input and output.

#### Context and Limits
Mistral Large 2 has the following context and limits:
- Context Window: 131,072 tokens
- Max Output: 4,096 tokens
- Knowledge Cutoff: 2024-07

These specifications are crucial for determining the model's suitability for specific tasks, especially those requiring extensive context or output.

#### Capabilities and Best Use Cases
Mistral Large 2 is best suited for:
- Coding
- Analysis
- RAG
- Agents
- Multilingual tasks
- Function calling

It is not recommended for:
- Embeddings
- Bulk cheap processing
- Real-time sub-100ms applications
- Vision-heavy tasks

#### Cost Examples
To illustrate the cost implications:
- 1,000 calls (avg 500 tokens): $6.0
- 10,000 calls: $60.0
- 100,000 calls: $600.0

#### Choosing the Right Model
When deciding between Mistral Large 2 and its competitors

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. With its robust capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts, it is best suited for tasks such as coding, analysis, retrieval-augmented generation (RAG), agents, multilingual support, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Given its capabilities and pricing structure, here are the top 5 best use cases for Mistral Large 2, along with examples of how to integrate it with OpenRouter:

1. **Coding and Development**: Mistral Large 2 excels in coding tasks, making it an ideal choice for developers looking to automate code generation, code review, or even learn from its outputs. 
    ```python
    import openrouter
    # Assuming you have an OpenRouter instance
    or_instance = openrouter.OpenRouter()
    prompt = "Write a Python function to sort a list of integers."
    response = or_instance.query(model="mistralai/mistral-large-2407", prompt=prompt)
    print(response)
    ```
2. **Complex Analysis**: With its large context window of 131,072 tokens and the ability to handle up to 4,096 output tokens, Mistral Large 2 is well-suited for in-depth analysis tasks, such as analyzing long documents or generating detailed reports.
    ```python
    import openrouter
    or_instance = openrouter.OpenRouter()
    document = "Your long document text here..."
    prompt = f"Analyze the following document: {document}. Provide a summary and key points."
    response = or_instance.query(model="mistralai/mistral-large-2407", prompt=prompt)
    print(response)
    ```
3. **Multilingual Support**: Given its mult

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
