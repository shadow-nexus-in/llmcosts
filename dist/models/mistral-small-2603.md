# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-04-20
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open-source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of tasks, including text generation, coding, analysis, and summarization, thanks to its capabilities in text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens.

### Technical Specifications and Use Cases
Mistral Small 4 is best utilized for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization. Its technical specifications, including a context window of 262,144 tokens and a maximum output of 4,096 tokens, make it suitable for complex tasks that require significant contextual understanding. The model's knowledge cutoff is 2023-12, indicating that its training data is current up to December 2023. Benchmarks show an MMLU score of 80.0 and an LMSYS Arena ELO score of 1200, demonstrating its capabilities in various linguistic and logical reasoning tasks.

### Pricing and Cost Considerations
The pricing for Mistral Small 4 is structured as follows: $0.15 per 1M tokens for input, $0.6 per 1M tokens for output, with no charges for cached input or batch input. For developers, estimating costs is straightforward, with examples provided: 1,000 calls averaging 500 tokens cost $0.375, 10,000 calls cost $3.75, and 100,000 calls cost $37.5. Given its capabilities and pricing, Mistral Small 4 is positioned as a competitive option for developers seeking a robust language model for a variety of applications, although

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
Mistral: Mistral Small 4 is a standard, non-open-source model provided by Mistralai, released on January 1, 2024. This analysis breaks down the cost structure, usage scenarios, and scalability of this model.

#### Cost Structure
The pricing for Mistral: Mistral Small 4 is as follows:
- **Input**: $0.15 per 1M tokens
- **Output**: $0.6 per 1M tokens
- **Cached Input**: No additional cost ($None per 1M tokens)
- **Batch Input**: No additional cost ($None per 1M tokens)

#### Usage Scenarios
- **Cached Tokens**: Since there is no additional cost for cached input tokens, it is always beneficial to use cached tokens when possible. This can significantly reduce the overall cost, especially in scenarios where the same input tokens are processed multiple times.
- **Batch API Savings**: Although there is no direct cost savings mentioned for batch input, processing inputs in batches can still lead to efficiency gains and potentially reduce the overall number of API calls needed, thereby indirectly saving costs.

#### Cost at Scale
The cost examples provided for Mistral: Mistral Small 4 are:
- **1,000 calls (avg 500 tokens)**: $0.375
- **10,000 calls**: $3.75
- **100,000 calls**: $37.5

These costs are calculated based on the average number of tokens per call and the pricing structure. For 1,000 calls with an average of 500 tokens per call, the total tokens processed would be 500,000 tokens. Assuming an even split between input and output tokens for simplicity (though actual costs may vary based on the specific input/output token ratio), the cost can be estimated as follows:
- **Input Tokens**: 250,000 tokens (assuming half of 500

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Benchmark Performance Analysis
#### Model Overview
The Mistral Small 4 model, provided by Mistralai, is a standard-tier language model with a release date of 2024-01-01. It is not open-source.

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

The MMLU score of **80.0** indicates the model's performance on a set of mathematical and logical tasks. A higher MMLU score generally corresponds to better performance on these tasks.

The LMSYS Arena ELO score of **1200** is a measure of the model's overall language understanding and generation capabilities. ELO scores are relative and comparative, with higher scores indicating better performance compared to other models.

The absence of HumanEval and GSM8K scores means that the model's performance on these specific benchmarks is not available.

#### Real-World Implications
In real-world use cases, the Mistral Small 

## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral: Mistral Small 4, we will provide a general analysis of its pricing, performance, and capabilities to help users decide when to choose this model.

#### Pricing
The pricing for Mistral: Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Performance Trade-offs
Mistral: Mistral Small 4 has the following performance metrics:
* MMLU: 80.0
* LMSYS Arena ELO: 1200
* Context Window: 262,144 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2023-12

These metrics indicate that Mistral: Mistral Small 4 has a moderate level of performance, with a relatively high context window and max output. However, the lack of direct competitors makes it difficult to compare its performance directly.

#### Capabilities and Use Cases
Mistral: Mistral Small 4 has the following capabilities:
* text
* function_calling
* json_mode
* streaming
* structured_outputs

It is best suited for the following use cases:
* chat
* text_generation
* coding
* analysis
* rag_pipelines
* summarization

#### Cost Examples
The cost of using Mistral: Mistral Small 4 can be estimated as follows:
* 1,000 calls (avg 500 tokens): $0.375
* 10,000 calls: $3.75
* 100,000 calls: $37.5

#### Choosing Mistral: Mistral Small 4
Based on its pricing, performance, and capabilities, Mistral: Mistral Small 4 may be a good choice for users who:
* Need a model with a moderate level of performance
* Require a high context window and max output
* Need to perform tasks such as chat, text generation, coding, analysis, and summarization
* Are willing to pay a premium for a model with a relatively high output price

However, users should note that the lack of direct competitors makes it difficult to compare the value proposition of Mistral: Mistral Small

## Best Use Cases
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful language model with a wide range of capabilities, including text generation, function calling, and structured outputs. With its standard tier and release date of 2024-01-01, it offers a robust set of features for various applications.

### Top 5 Best Use Cases for Mistral Small 4
Based on its capabilities and benchmarks, here are the top 5 best use cases for Mistral Small 4:

1. **Chat and Text Generation**: With its high context window of 262,144 tokens and max output of 4,096 tokens, Mistral Small 4 is well-suited for chat and text generation applications.
2. **Coding and Analysis**: Its capabilities in function calling and structured outputs make it an excellent choice for coding and analysis tasks, such as code completion and code review.
3. **Summarization and RAG Pipelines**: Mistral Small 4's ability to process large amounts of text and generate concise summaries makes it a great fit for summarization and RAG (Retrieve, Augment, Generate) pipelines.
4. **Streaming and Real-time Applications**: With its support for streaming, Mistral Small 4 can be used in real-time applications, such as live chatbots or real-time text analysis.
5. **JSON Mode and Structured Outputs**: Its ability to handle JSON mode and generate structured outputs makes it suitable for applications that require data exchange and processing in a structured format.

### Code Integration Examples with OpenRouter
To integrate Mistral Small 4 with OpenRouter, you can use the following code examples:

```python
import openrouter

# Initialize the Mistral Small 4 model
model = openrouter.MistralSmall4()

# Text generation example
input_text = "Hello, how are you?"
output = model.generate_text(input_text)
print(output)

# Function calling example
def add

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
