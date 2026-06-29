# NVIDIA: Nemotron 3 Super API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-29
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super, released on 2024-01-01, is a cutting-edge language model developed by Nvidia. This model, identified as `nvidia/nemotron-3-super-120b-a12b`, operates under a standard tier and is not open-source. With its robust architecture, the Nemotron 3 Super is designed to handle a wide range of tasks, including but not limited to text generation, coding, analysis, and summarization. Its capabilities extend to function calling, JSON mode, streaming, and structured outputs, making it a versatile tool for developers.

### Technical Specifications and Pricing
Technically, the Nemotron 3 Super boasts a context window of 262,144 tokens and can generate up to 4,096 tokens as output. Its knowledge cutoff is 2023-12, ensuring that its training data is current up to that point. The pricing model for this service is based on input and output tokens. Developers are charged $0.1 per 1M tokens for input and $0.5 per 1M tokens for output. There are no specified charges for cached input or batch input. This pricing structure suggests that the model is optimized for applications where the output is significantly larger than the input, such as text generation tasks. The model's benchmarks show an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating strong performance in certain linguistic and logical reasoning tasks.

### Use Cases and Cost Considerations
The Nemotron 3 Super is best suited for applications like chat, text generation, coding, analysis, and summarization, thanks to its advanced capabilities. However, its suitability for other tasks not listed under "BEST FOR" should be evaluated on a case-by-case basis. To give developers a clearer picture of the costs involved, examples are provided: 1,000 calls averaging 500 tokens each would

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
The NVIDIA Nemotron 3 Super is a standard, non-open-source model released by Nvidia on January 1, 2024. This analysis will delve into the cost structure, usage scenarios, and cost savings opportunities for this model.

#### Cost Structure
The pricing for the NVIDIA Nemotron 3 Super is as follows:
* Input: $0.1 per 1M tokens
* Output: $0.5 per 1M tokens
* Cached Input: $None per 1M tokens (free)
* Batch Input: $None per 1M tokens (free)

#### Cost Savings Opportunities
##### Cached Tokens
Cached input tokens are free, making it an attractive option for applications with repetitive input sequences. When to use cached tokens:
* Applications with high input token reuse
* Real-time systems with limited computational resources
* Scenarios where input data remains relatively static

##### Batch API Savings
Batch input is also free, allowing for significant cost savings when processing large volumes of data in parallel. Consider batch API for:
* High-throughput applications
* Data processing pipelines with large input datasets
* Scenarios where concurrent processing is feasible

#### Cost at Scale
The cost of using the NVIDIA Nemotron 3 Super at various scales is as follows:
* 1,000 API calls (avg 500 tokens): $0.3
* 10,000 API calls: $3.0
* 100,000 API calls: $30.0

These costs demonstrate a linear scaling of expenses with the number of API calls, indicating that the pricing model is straightforward and easy to predict.

#### Conclusion
The NVIDIA Nemotron 3 Super offers a competitive pricing model with opportunities for cost savings through cached input tokens and batch API processing. By understanding the cost structure and leveraging these savings opportunities, developers can optimize their expenses and make the most of this powerful model for applications such as chat, text

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### NVIDIA Nemotron 3 Super Analysis
#### Overview
The NVIDIA Nemotron 3 Super is a standard, non-open-source model released by Nvidia on 2024-01-01. This model is priced based on input and output tokens, with specific costs for different usage scenarios.

#### Pricing Structure
The pricing for the NVIDIA Nemotron 3 Super is as follows:
* Input: **$0.1 per 1M tokens**
* Output: **$0.5 per 1M tokens**
* Cached Input: **$None per 1M tokens** (not applicable)
* Batch Input: **$None per 1M tokens** (not applicable)

#### Context and Limits
The model has the following context and limits:
* Context Window: **262,144 tokens**
* Max Output: **4,096 tokens**
* Knowledge Cutoff: **2023-12** (model training data is limited to this date)

#### Benchmark Performance
The benchmark performance of the NVIDIA Nemotron 3 Super is as follows:
* MMLU: **80.0** - This score indicates the model's performance on a specific set of natural language processing tasks. A higher MMLU score generally corresponds to better performance.
* HumanEval: **None** - This benchmark is not available for this model.
* LMSYS Arena ELO: **1200** - This score represents the model's performance in a competitive arena, with higher scores indicating better performance.
* GSM8K: **None** - This benchmark is not available for this model.

#### Capabilities and Use Cases
The NVIDIA Nemotron 3 Super supports the following capabilities:
* text
* function_calling
* json_mode


## Competitor Comparison
### NVIDIA Nemotron 3 Super Comparison
#### Introduction
The NVIDIA Nemotron 3 Super is a standard-tier model released by Nvidia on 2024-01-01. With its unique capabilities and pricing structure, it's essential to understand its strengths and weaknesses compared to other models in the market.

#### Pricing Structure
The Nemotron 3 Super has the following pricing structure:
* Input: $0.1 per 1M tokens
* Output: $0.5 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Performance Trade-offs
Given the lack of direct competitors, we'll focus on the model's capabilities and limitations:
* **Context Window**: 262,144 tokens, suitable for most chat and text generation applications
* **Max Output**: 4,096 tokens, sufficient for summarization and analysis tasks
* **Knowledge Cutoff**: 2023-12, which may limit its ability to provide information on very recent events or developments

#### Benchmarks
The Nemotron 3 Super has the following benchmark scores:
* **MMLU**: 80.0, indicating a strong performance in multi-task learning
* **LMSYS Arena ELO**: 1200, suggesting a moderate level of competence in a competitive environment

#### Capabilities and Use Cases
The Nemotron 3 Super is best suited for:
* Chat
* Text generation
* Coding
* Analysis
* RAG pipelines
* Summarization

#### Cost Examples
To give you a better understanding of the costs involved:
* 1,000 calls (avg 500 tokens): $0.3
* 10,000 calls: $3.0
* 100,000 calls: $30.0

#### Choosing the Nemotron 3 Super
Given the lack of direct competitors, the Nemotron 3 Super is a strong choice for applications that require:
* A large context window
* Moderate to high output lengths
* Strong multi-task learning capabilities
* A balance between input and output costs

However, if your application requires:
* Very recent knowledge (post-2023-12)
* Extremely high output lengths
* A more extensive range of capabilities

you may need to consider other models or wait for future releases.

### Conclusion
The NVIDIA Nemotron 3 Super is a capable model with a unique set of strengths and

## Best Use Cases
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super is a powerful language model released by Nvidia on 2024-01-01. With its standard tier and closed-source architecture, it offers a range of capabilities, including text generation, function calling, and structured outputs. In this guide, we will explore the top 5 best use cases for the NVIDIA Nemotron 3 Super, along with practical advice and code integration examples using OpenRouter.

### Top 5 Use Cases for NVIDIA Nemotron 3 Super
1. **Chat and Text Generation**: The Nemotron 3 Super excels in generating human-like text, making it an ideal choice for chat applications.
2. **Coding and Analysis**: With its ability to understand and generate code, the model is suitable for coding tasks, such as code completion and analysis.
3. **Summarization**: The Nemotron 3 Super can effectively summarize long pieces of text, making it a great tool for content summarization.
4. **RAG Pipelines**: The model's ability to handle structured outputs and function calling makes it a good fit for RAG (Retrieve, Augment, Generate) pipelines.
5. **Function Calling and JSON Mode**: The Nemotron 3 Super can execute functions and handle JSON data, making it a versatile tool for a range of applications.

### Code Integration Examples with OpenRouter
To integrate the Nemotron 3 Super with OpenRouter, you can use the following code example:
```python
import openrouter

# Initialize the Nemotron 3 Super model
model = openrouter.Model("nvidia/nemotron-3-super-120b-a12b")

# Define a function to generate text
def generate_text(prompt):
    output = model.generate_text(prompt, max_tokens=4096)
    return output

# Test the function
prompt = "Write a short story about a character who discovers a hidden world."
print(generate_text(prompt))
``

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
