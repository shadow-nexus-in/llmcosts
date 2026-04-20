# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-20
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, including coding, analysis, and multilingual support. This model boasts an impressive architecture that supports capabilities such as text and vision processing, function calling, JSON mode, streaming, and system prompts. With a context window of 131,072 tokens and a maximum output of 4,096 tokens, Mistral Large 2 is well-suited for complex tasks that require a deep understanding of the input context.

### Technical Strengths and Use Cases
Mistral Large 2 demonstrates its technical prowess through its benchmark scores: MMLU at 84.0, HumanEval at 92.0, LMSYS Arena ELO at 1225, and GSM8K at 93.0. These scores indicate the model's exceptional performance in various areas, making it a top choice for tasks like coding, analysis, and function calling. The model's capabilities are further enhanced by its support for multilingual applications and its ability to handle system prompts. However, it's worth noting that Mistral Large 2 is not recommended for use cases that require embeddings, bulk processing at low costs, real-time responses under 100ms, or vision-heavy tasks.

### Pricing and Cost Considerations
The pricing for Mistral Large 2 is structured as follows: $3.0 per 1M input tokens and $9.0 per 1M output tokens. There are no specified costs for cached input or batch input. To give developers a better understanding of the costs involved, example scenarios have been provided: 1,000 calls averaging 500 tokens would cost $6.0, while 10,000 calls would amount to $60.0, and 100,000 calls would total $600.0. In comparison to its top

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $3.0 |
| Output | $9.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Mistral Large 2
#### Overview
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. With a release date of 2024-07-24, this model is positioned as a high-end solution for tasks such as coding, analysis, and multilingual support.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
- **Input**: $3.0 per 1M tokens
- **Output**: $9.0 per 1M tokens
- **Cached Input**: $None per 1M tokens (indicating no additional cost for cached inputs)
- **Batch Input**: $None per 1M tokens (suggesting that batch inputs are also not charged extra)

#### When to Use Cached Tokens
Given that cached input tokens do not incur an additional cost, it is advisable to utilize cached tokens whenever possible to minimize expenses. This approach can be particularly beneficial for applications where the same input data is processed multiple times.

#### Batch API Savings
Although the pricing data does not specify a direct discount for batch API calls, the fact that batch input is listed as $None per 1M tokens implies that Mistral AI does not charge extra for batching. This can lead to significant savings when making a large number of API calls, as the cost per call can be reduced by optimizing the batch size.

#### Cost at Scale
To understand the cost implications of using Mistral Large 2 at scale, let's examine the provided cost examples:
- **1,000 calls (avg 500 tokens)**: $6.0
- **10,000 calls**: $60.0
- **100,000 calls**: $600.0

These examples suggest a linear scaling of costs with the number of API calls. To estimate the cost per token, we can use the average token count per call. For

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
The Mistral Large 2 model, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. It offers a range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts.

#### Pricing
The pricing for Mistral Large 2 is as follows:
* Input: $3.0 per 1M tokens
* Output: $9.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Context and Limits
The model has the following context and limits:
* Context Window: 131,072 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2024-07

#### Benchmark Performance
The benchmark performance of Mistral Large 2 is as follows:
* MMLU: 84.0
* HumanEval: 92.0
* LMSYS Arena ELO: 1225
* GSM8K: 93.0

These benchmarks indicate the model's performance in various areas:
* **MMLU (Massive Multitask Language Understanding)**: Measures the model's ability to understand and generate human-like text. A score of 84.0 indicates strong language understanding capabilities.
* **HumanEval**: Evaluates the model's ability to write correct and functional code. A score of 92.0 suggests excellent coding capabilities.
* **LMSYS Arena ELO**: Measures the model's performance in a competitive environment, with a higher score indicating better performance. A score of

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, a premium model provided by Mistral AI, is a powerful language model with a wide range of capabilities, including text, vision, function calling, and more. Released on 2024-07-24, it offers a unique set of features and performance metrics. In this comparison, we will evaluate Mistral Large 2 against its top competitor, GPT-4o, in terms of pricing, performance, and use cases.

#### Pricing Comparison
The pricing for Mistral Large 2 and GPT-4o is as follows:
* Mistral Large 2:
	+ Input: $3.0 per 1M tokens
	+ Output: $9.0 per 1M tokens
* GPT-4o:
	+ Input: $2.5 per 1M tokens
	+ Output: $10.0 per 1M tokens

Mistral Large 2 is more expensive than GPT-4o in terms of input pricing, but slightly cheaper in terms of output pricing.

#### Performance Comparison
The performance metrics for Mistral Large 2 are:
* MMLU: 84.0
* HumanEval: 92.0
* LMSYS Arena ELO: 1225
* GSM8K: 93.0

While the performance metrics for GPT-4o are not provided, we can infer that Mistral Large 2 has a strong performance profile, with high scores in various benchmarks.

#### Context and Limits
Mistral Large 2 has the following context and limits:
* Context Window: 131,072 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2024-07

These limits indicate that Mistral Large 2 is suitable for tasks that require a large context window and moderate output length.

#### Capabilities and Use Cases
Mistral Large 2 has a wide range of capabilities, including:
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
* Agents
* Multilingual
* Function calling

However, it is not recommended for tasks that require:
* Embeddings
* Bulk cheap processing
* Real-time sub-100ms processing
*

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, provided by Mistral AI, is a premium, non-open-source model released on 2024-07-24. With its robust capabilities in text, vision, function calling, JSON mode, streaming, and system prompts, it is best suited for tasks such as coding, analysis, RAG (Retrieval-Augmented Generation), agents, multilingual support, and function calling.

### Top 5 Best Use Cases for Mistral Large 2
Given its capabilities and limitations, here are the top 5 best use cases for Mistral Large 2, along with practical advice and code integration examples using OpenRouter:

1. **Coding and Development**: Mistral Large 2 excels in coding tasks, making it an ideal choice for developers looking to automate code generation, code review, or even assist in coding interviews.
   - **Example**: Using OpenRouter to integrate Mistral Large 2 for automated code completion.
   ```python
   import openrouter

   # Initialize OpenRouter with Mistral Large 2
   model = openrouter.MistralLarge2()

   # Function to generate code based on a prompt
   def generate_code(prompt):
       response = model.generate(prompt)
       return response

   # Example usage
   prompt = "Write a Python function to sort a list in ascending order."
   print(generate_code(prompt))
   ```

2. **Multilingual Support**: With its multilingual capabilities, Mistral Large 2 can be used for translation services, multilingual chatbots, or content generation in various languages.
   - **Example**: Using Mistral Large 2 via OpenRouter for translating English text to Spanish.
   ```python
   import openrouter

   # Initialize OpenRouter with Mistral Large 2
   model = openrouter.MistralLarge2()

   # Function to translate English to Spanish
   def translate_to_spanish(text):


## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
