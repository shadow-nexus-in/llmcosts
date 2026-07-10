# NVIDIA: Nemotron 3 Super API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-07-10
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super is a powerful language model developed by Nvidia, released on January 1, 2024. This model, identified as `nvidia/nemotron-3-super-120b-a12b`, operates under a standard tier and is not open-source. It boasts an impressive architecture that enables it to handle a wide range of tasks, from text generation and chat to coding and analysis. With its robust capabilities, including text, function calling, JSON mode, streaming, and structured outputs, the Nemotron 3 Super is poised to be a versatile tool for developers.

### Technical Specifications and Strengths
Technically, the Nemotron 3 Super has a context window of 262,144 tokens and can generate up to 4,096 tokens as output. Its knowledge cutoff is December 2023, ensuring it has a broad and up-to-date understanding of the world. The model's pricing is structured around input and output tokens, with costs of $0.1 per 1M tokens for input and $0.5 per 1M tokens for output. Benchmarks show an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating strong performance in various linguistic and logical tasks. The model is best suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization, leveraging its capabilities in handling complex and structured data.

### Use Cases and Cost Considerations
Developers can utilize the Nemotron 3 Super for a variety of use cases, given its broad range of capabilities. However, it's essential to consider the cost implications of using this model. For example, 1,000 calls with an average of 500 tokens per call would cost $0.3, while 10,000 calls would amount to $3.0, and 100,000 calls would total $30.

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.1 |
| Output | $0.5 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### NVIDIA Nemotron 3 Super Pricing Analysis
#### Overview
The NVIDIA Nemotron 3 Super is a standard, non-open-source model released by Nvidia on January 1, 2024. This analysis will delve into the cost structure, usage scenarios, and scalability of this model.

#### Cost Structure
The pricing for the NVIDIA Nemotron 3 Super is as follows:
* Input: **$0.1 per 1M tokens**
* Output: **$0.5 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### Usage Scenarios
* **Cached Tokens**: Since cached input tokens are free, it is recommended to use cached tokens whenever possible to minimize costs.
* **Batch API Savings**: Batch input is also free, making it an attractive option for large-scale API calls. However, the cost savings will depend on the output tokens, which are charged at **$0.5 per 1M tokens**.

#### Cost at Scale
The cost of using the NVIDIA Nemotron 3 Super model at different scales is as follows:
* **1,000 API calls** (avg 500 tokens): **$0.3**
* **10,000 API calls**: **$3.0**
* **100,000 API calls**: **$30.0**

These costs are based on the average number of tokens per call and the pricing structure outlined above.

#### Context and Limits
It's essential to consider the context window and output limits when using the NVIDIA Nemotron 3 Super model:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12

#### Capabilities and Best Use Cases
The NVIDIA Nemotron 3 Super model supports the following capabilities:
* text
* function_calling
* json

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### NVIDIA Nemotron 3 Super Benchmark Analysis
#### Overview
The NVIDIA Nemotron 3 Super is a standard, non-open-source model released by Nvidia on January 1, 2024. This analysis focuses on its benchmark performance, pricing, and capabilities to provide insights into its real-world applications.

#### Pricing
The model's pricing structure is as follows:
* Input: **$0.1 per 1M tokens**
* Output: **$0.5 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Benchmarks
The model's performance is measured by the following benchmarks:
* **MMLU (Massive Multitask Language Understanding)**: 80.0 - This score indicates the model's ability to understand and perform a wide range of natural language processing tasks. A higher MMLU score suggests better performance in tasks such as text classification, sentiment analysis, and question answering.
* **HumanEval**: None - HumanEval is a benchmark that evaluates a model's ability to write and execute code. The absence of a HumanEval score makes it difficult to assess the model's coding capabilities.
* **LMSYS Arena ELO**: 1200 - The LMSYS Arena ELO score measures a model's performance in a competitive environment, where it is pitted against other models. An ELO score of 1200 indicates that the model is a strong competitor, but its exact ranking is unclear without more context.
* **GSM8K**: None - The GSM8K benchmark evaluates a model's ability to solve math problems. The lack of a GSM8K score limits our understanding of

## Competitor Comparison
### NVIDIA Nemotron 3 Super Comparison
#### Introduction
The NVIDIA Nemotron 3 Super is a standard-tier language model released by Nvidia on January 1, 2024. With its impressive capabilities and competitive pricing, it's essential to compare it with other top models in the market. Since there are no direct competitors listed, we'll analyze the Nemotron 3 Super's features, pricing, and performance to determine its strengths and weaknesses.

#### Pricing
The Nemotron 3 Super's pricing structure is as follows:
* Input: $0.1 per 1M tokens
* Output: $0.5 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Performance
The model's performance is measured by various benchmarks:
* MMLU: 80.0
* LMSYS Arena ELO: 1200

#### Capabilities and Limits
The Nemotron 3 Super supports the following capabilities:
* Text
* Function calling
* JSON mode
* Streaming
* Structured outputs

It has the following limits:
* Context Window: 262,144 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2023-12

#### Best Use Cases
The Nemotron 3 Super is best suited for:
* Chat
* Text generation
* Coding
* Analysis
* RAG pipelines
* Summarization

#### Cost Examples
The estimated costs for using the Nemotron 3 Super are:
* 1,000 calls (avg 500 tokens): $0.3
* 10,000 calls: $3.0
* 100,000 calls: $30.0

#### Comparison with Other Models
Although there are no direct competitors listed, we can still analyze the Nemotron 3 Super's strengths and weaknesses:
* **Strengths:**
	+ Competitive pricing for input and output tokens
	+ High context window and max output limits
	+ Supports various capabilities, including function calling and structured outputs
* **Weaknesses:**
	+ No cached input or batch input pricing options
	+ Limited knowledge cutoff (2023-12)
	+ No HumanEval or GSM8K benchmark scores

#### Conclusion
The NVIDIA Nemotron 3 Super is a powerful language model with competitive pricing and impressive capabilities. While it has some limitations, such as

## Best Use Cases
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super is a powerful model released by Nvidia on 2024-01-01, categorized under the standard tier. This model is not open-source and offers a range of capabilities including text, function calling, JSON mode, streaming, and structured outputs.

### Top 5 Best Use Cases for NVIDIA Nemotron 3 Super
Given its capabilities, the NVIDIA Nemotron 3 Super is best suited for the following use cases:

1. **Chat and Text Generation**: With its ability to handle large context windows (up to 262,144 tokens) and generate up to 4,096 tokens of output, this model is ideal for chatbots and text generation tasks.
2. **Coding and Analysis**: The model's function calling capability and support for structured outputs make it suitable for coding tasks and in-depth analysis of text data.
3. **Summarization**: Its ability to process large amounts of text and generate concise summaries makes it a good fit for summarization tasks.
4. **RAG Pipelines**: The model's support for retrieval-augmented generation (RAG) pipelines enables it to effectively handle complex, information-dense tasks.
5. **Streaming**: With its streaming capability, the NVIDIA Nemotron 3 Super can handle real-time text data, making it suitable for applications that require immediate processing and response.

### Code Integration Example with OpenRouter
To integrate the NVIDIA Nemotron 3 Super with OpenRouter, you can use the following example code:
```python
import openrouter

# Initialize the model
model = openrouter.Model(
    name="nvidia/nemotron-3-super-120b-a12b",
    provider="nvidia",
    input_type="text",
    output_type="text"
)

# Define a function to generate text
def generate_text(prompt):
    # Set the input parameters
    input_params = {
        "prompt": prompt,
        "

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
