# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-19
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of natural language processing tasks with its capabilities including text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens.

### Technical Specifications and Use Cases
The technical specifications of Mistral Small 4 highlight its potential for various applications. With a context window of 262,144 tokens and a maximum output of 4,096 tokens, this model is well-suited for tasks that require understanding and generating lengthy texts. Its capabilities in text generation, coding, analysis, and summarization make it a versatile tool for developers. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its competence in handling complex language tasks. Mistral Small 4 is best utilized for chat, text generation, coding, analysis, RAG pipelines, and summarization tasks.

### Pricing and Cost Considerations
The pricing model for Mistral Small 4 is based on input and output tokens. Developers are charged $0.15 per 1 million input tokens and $0.6 per 1 million output tokens. There are no charges for cached input or batch input. To give developers a clearer picture, example costs are provided: $0.375 for 1,000 calls averaging 500 tokens, $3.75 for 10,000 calls, and $37.5 for 100,000 calls. With no direct competitors listed, Mistral Small 4 stands out as a unique offering in the market

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.15 |
| Output | $0.6 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Mistral: Mistral Small 4
#### Overview
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral: Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens (free)
* Batch Input: $None per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for repeated input sequences. If your application involves frequent reuse of the same input tokens, utilizing cached tokens can significantly reduce costs.

#### Batch API Savings
Batch input is also free, allowing for cost-effective processing of large input batches. By leveraging batch API capabilities, you can minimize the cost per token for large-scale applications.

#### Cost at Scale
The cost of using Mistral: Mistral Small 4 at scale is as follows:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

These costs demonstrate a linear scaling of expenses with the number of API calls, indicating that the cost per call remains constant regardless of the scale.

#### Example Cost Calculation
To calculate the cost for a specific use case, you can use the following formula:
Cost = (Number of Tokens * Input Cost per 1M Tokens) + (Number of Output Tokens * Output Cost per 1M Tokens)

For example, assuming an average input of 500 tokens and an output of 100 tokens per call:
* 1,000 calls: (500

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Benchmark Performance Analysis
#### Overview
Mistral Small 4, provided by Mistralai, is a standard-tier language model with a release date of 2024-01-01. This analysis will delve into the benchmark performance of Mistral Small 4, focusing on the MMLU, HumanEval, and Arena ELO scores, and their implications for real-world use.

#### Benchmark Scores
The benchmark scores for Mistral Small 4 are as follows:
* **MMLU (Massive Multitask Language Understanding)**: 80.0
* **HumanEval**: Not available
* **LMSYS Arena ELO**: 1200

#### Interpretation of Benchmark Scores
* **MMLU Score (80.0)**: The MMLU score measures a model's ability to perform a wide range of natural language processing tasks. A score of 80.0 indicates that Mistral Small 4 has a moderate level of language understanding, suitable for tasks such as text generation, chat, and analysis.
* **HumanEval**: Unfortunately, HumanEval scores are not available for Mistral Small 4. HumanEval is a benchmark that evaluates a model's ability to generate correct code in response to programming prompts. The lack of HumanEval scores makes it difficult to assess Mistral Small 4's coding capabilities.
* **LMSYS Arena ELO Score (1200)**: The LMSYS Arena ELO score is a measure of a model's overall performance in a competitive environment. An ELO score of 1200 is a moderate score, indicating that Mistral Small 4 has a reasonable level of language understanding and generation capabilities.

#### Real-World Imp

## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral Small 4, we will provide a general analysis of its features, pricing, and performance trade-offs. This will help users understand when to choose Mistral Small 4 and what to expect from this model.

#### Model Overview
* **Model:** Mistral Small 4 (mistralai/mistral-small-2603)
* **Provider:** Mistralai
* **Release Date:** 2024-01-01
* **Tier:** Standard
* **Open Source:** False

#### Pricing
The pricing for Mistral Small 4 is as follows:
* **Input:** $0.15 per 1M tokens
* **Output:** $0.6 per 1M tokens
* **Cached Input:** $None per 1M tokens
* **Batch Input:** $None per 1M tokens

#### Context and Limits
* **Context Window:** 262,144 tokens
* **Max Output:** 4,096 tokens
* **Knowledge Cutoff:** 2023-12

#### Benchmarks
* **MMLU:** 80.0
* **HumanEval:** None
* **LMSYS Arena ELO:** 1200
* **GSM8K:** None

#### Capabilities and Best Use Cases
Mistral Small 4 supports the following capabilities:
* text
* function_calling
* json_mode
* streaming
* structured_outputs

It is best suited for:
* chat
* text_generation
* coding
* analysis
* rag_pipelines
* summarization

#### Cost Examples
The estimated costs for using Mistral Small 4 are:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

#### Choosing Mistral Small 4
Given the lack of direct competitors, Mistral Small 4 can be considered a unique offering in the market. Its pricing and performance trade-offs make it an attractive option for users who require a standard-tier model with a large context window and support for various capabilities.

When to choose Mistral Small 4:
* You need a model with a large context window (262,144 tokens) for tasks that require understanding long pieces of text.
* You require support for function

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and release date of 2024-01-01, it offers a robust set of features for various applications.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and max output of 4,096 tokens, Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: Its ability to perform function calling and structured outputs makes it an excellent choice for coding and analysis tasks, such as code review and debugging.
3. **Summarization**: Mistral Small 4's capabilities in text generation and analysis make it a good fit for summarization tasks, such as summarizing long documents or articles.
4. **RAG Pipelines**: Its support for structured outputs and function calling makes it suitable for RAG (Retrieval-Augmented Generation) pipelines, which involve retrieving information from external sources and generating text based on that information.
5. **Streaming**: With its streaming capability, Mistral Small 4 can be used for real-time text generation and analysis applications, such as live chat or sentiment analysis.

### Code Integration Examples with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code examples:

```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.Model("mistralai/mistral-small-2603")

# Define a function to generate text using the model
def generate_text(prompt):
    response = model.generate_text(prompt, max_tokens=4096)
   

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
