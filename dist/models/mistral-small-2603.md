# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-03
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of tasks, including text generation, coding, analysis, and summarization, thanks to its capabilities in text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens.

### Technical Specifications and Use Cases
Mistral Small 4 is best utilized for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization. The model's pricing is structured around input and output tokens, with costs of $0.15 per 1M input tokens and $0.6 per 1M output tokens. There are no specified costs for cached input or batch input. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200. With a knowledge cutoff of 2023-12, Mistral Small 4 is well-suited for tasks that require a strong understanding of data up to the end of 2023.

### Cost Considerations and Competitors
For developers considering integrating Mistral Small 4 into their applications, cost is an essential factor. The cost examples provided indicate that 1,000 calls with an average of 500 tokens would amount to $0.375, scaling up to $3.75 for 10,000 calls and $37.5 for 100,000 calls. Notably, there are no direct competitors listed for Mistral Small 4, suggesting a unique position in the market. However, its capabilities and pricing structure make it an

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.15 |
| Output | $0.6 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Mistral Small 4 Pricing Analysis
#### Overview
Mistral Small 4, provided by Mistralai, is a standard-tier model with a release date of 2024-01-01. This analysis will delve into the cost structure, optimal usage scenarios, and cost savings at scale for this model.

#### Cost Structure
The pricing for Mistral Small 4 is as follows:
* **Input**: $0.15 per 1M tokens
* **Output**: $0.6 per 1M tokens
* **Cached Input**: $None per 1M tokens (free)
* **Batch Input**: $None per 1M tokens (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following strategies:
* **Use cached tokens**: Since cached input tokens are free, utilize them whenever possible to reduce input costs.
* **Batch API calls**: With batch input being free, batching API calls can significantly reduce costs, especially for large volumes of requests.

#### Cost at Scale
The cost examples provided are:
* **1,000 calls (avg 500 tokens)**: $0.375
* **10,000 calls**: $3.75
* **100,000 calls**: $37.5

These examples illustrate the cost savings at scale. As the number of API calls increases, the cost per call decreases, making it more economical to use the model for large-scale applications.

#### Context and Limits
It's essential to be aware of the model's context window and output limits:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12

These limits may impact the model's performance and cost-effectiveness for specific use cases.

#### Capabilities and Best Use Cases
Mistral Small 4 is capable of:
* Text
* Function calling
* JSON mode
* Streaming
* Structured

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Analysis
#### Model Overview
The Mistral Small 4 model, provided by Mistralai, is a standard-tier language model released on 2024-01-01. It is not open-source.

#### Pricing Structure
The pricing for Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Context and Limits
The model has the following context and limits:
* Context Window: 262,144 tokens
* Max Output: 4,096 tokens
* Knowledge Cutoff: 2023-12

#### Benchmark Performance
The benchmark performance of Mistral Small 4 is:
* MMLU: 80.0
* HumanEval: None
* LMSYS Arena ELO: 1200
* GSM8K: None

The MMLU score of 80.0 indicates the model's performance on a set of tasks that measure its ability to understand and generate human-like language. A higher MMLU score generally indicates better performance.

The LMSYS Arena ELO score of 1200 is a measure of the model's performance in a competitive setting, where it is pitted against other models. An ELO score of 1200 is a relatively moderate score, indicating that the model is capable of competing with other models, but may not be the top performer.

The lack of HumanEval and GSM8K scores makes it difficult to fully assess the model's capabilities in areas such as coding and mathematical problem-solving.



## Competitor Comparison
### Comparison of Mistral: Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral: Mistral Small 4, we will provide a general overview of the model's pricing, performance, and capabilities, highlighting its strengths and weaknesses.

#### Model Overview
* **Model:** Mistral: Mistral Small 4 (mistralai/mistral-small-2603)
* **Provider:** Mistralai
* **Release Date:** 2024-01-01
* **Tier:** Standard
* **Open Source:** False

#### Pricing
The pricing for Mistral: Mistral Small 4 is as follows:
* **Input:** $0.15 per 1M tokens
* **Output:** $0.6 per 1M tokens
* **Cached Input:** $None per 1M tokens
* **Batch Input:** $None per 1M tokens

#### Context and Limits
* **Context Window:** 262,144 tokens
* **Max Output:** 4,096 tokens
* **Knowledge Cutoff:** 2023-12

#### Benchmarks
The model's performance on various benchmarks is:
* **MMLU:** 80.0
* **HumanEval:** None
* **LMSYS Arena ELO:** 1200
* **GSM8K:** None

#### Capabilities and Use Cases
Mistral: Mistral Small 4 supports the following capabilities:
* **Text**
* **Function calling**
* **JSON mode**
* **Streaming**
* **Structured outputs**

It is best suited for:
* **Chat**
* **Text generation**
* **Coding**
* **Analysis**
* **RAG pipelines**
* **Summarization**

#### Cost Examples
The estimated costs for using Mistral: Mistral Small 4 are:
* **1,000 calls (avg 500 tokens):** $0.375
* **10,000 calls:** $3.75
* **100,000 calls:** $37.5

#### Choosing Mistral: Mistral Small 4
Since there are no direct competitors listed, the decision to choose Mistral: Mistral Small 4 depends on the specific requirements of your project. Consider the following factors:
* **Pricing:** If your project requires a moderate to high volume of input and output tokens, the pricing of Mistral: Mistral Small 4 may be

## Best Use Cases
### Practical Advice on Top 5 Use Cases for Mistral Small 4
Mistral Small 4, provided by Mistralai, is a powerful model with a wide range of capabilities, including text generation, function calling, and structured outputs. Here are the top 5 best use cases for this model, along with specific code integration examples mentioning OpenRouter:

#### 1. **Chat and Text Generation**
Mistral Small 4 excels in chat and text generation tasks, making it an ideal choice for conversational AI applications. To integrate this model with OpenRouter for chat purposes, you can use the following example:
```python
import openrouter
from mistralai import MistralSmall4

# Initialize the model and OpenRouter
model = MistralSmall4()
router = openrouter.Router()

# Define a chat function
def chat(input_text):
    output = model.generate_text(input_text, max_length=4096)
    return output

# Integrate with OpenRouter
router.add_endpoint("/chat", chat)

# Run the chat application
router.run()
```
Cost estimate: For 1,000 chat interactions (avg 500 tokens), the cost would be approximately $0.375 (based on $0.15 per 1M tokens input and $0.6 per 1M tokens output).

#### 2. **Coding and Function Calling**
Mistral Small 4 supports function calling, making it suitable for coding tasks. To integrate this model with OpenRouter for coding purposes, you can use the following example:
```python
import openrouter
from mistralai import MistralSmall4

# Initialize the model and OpenRouter
model = MistralSmall4()
router = openrouter.Router()

# Define a coding function
def code_generate(input_code):
    output = model.call_function(input_code, max_length=4096)
    return output

# Integrate with OpenRouter
router.add_endpoint("/code", code

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
