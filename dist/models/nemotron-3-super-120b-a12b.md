# NVIDIA: Nemotron 3 Super API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-11
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super is a powerful language model developed by Nvidia, released on January 1, 2024. This model, identified as `nvidia/nemotron-3-super-120b-a12b`, is part of the standard tier and is not open-source. With its robust architecture, the Nemotron 3 Super is designed to handle a wide range of tasks, including text generation, coding, analysis, and more. Its capabilities include text processing, function calling, JSON mode, streaming, and structured outputs, making it a versatile tool for developers.

### Technical Specifications and Pricing
Technically, the Nemotron 3 Super boasts a context window of 262,144 tokens and can generate up to 4,096 tokens as output. Its knowledge cutoff is December 2023, ensuring it has a broad and up-to-date understanding of the world. In terms of pricing, the model charges $0.1 per 1M tokens for input and $0.5 per 1M tokens for output. There are no charges for cached input or batch input. The model's performance is benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, demonstrating its capabilities. For developers, the cost of using this model can be estimated, for example, at $0.3 for 1,000 calls averaging 500 tokens, scaling to $3.0 for 10,000 calls and $30.0 for 100,000 calls.

### Use Cases and Competitors
The NVIDIA Nemotron 3 Super is best suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization, thanks to its comprehensive set of capabilities. However, its limitations and areas where it is not recommended are not specified. Notably, there are no direct competitors listed for the Nemotron 3 Super

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
The NVIDIA Nemotron 3 Super is a standard, non-open-source model provided by Nvidia, released on January 1, 2024. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale for this model.

#### Cost Structure
The pricing for the NVIDIA Nemotron 3 Super model is as follows:
- **Input**: $0.1 per 1M tokens
- **Output**: $0.5 per 1M tokens
- **Cached Input**: No additional cost per 1M tokens
- **Batch Input**: No additional cost per 1M tokens

#### Optimal Usage Scenarios
- **Cached Tokens**: Since there is no additional cost for cached input tokens, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
- **Batch API Savings**: Although there is no direct cost savings mentioned for batch input, processing inputs in batches can still lead to efficiency gains and potentially reduce the overall number of API calls needed, indirectly saving on output costs.

#### Cost at Scale
The provided cost examples give insight into the cost structure at different scales:
- **1,000 calls (avg 500 tokens)**: $0.3
- **10,000 calls**: $3.0
- **100,000 calls**: $30.0

These examples suggest a linear cost scaling with the number of API calls, which is consistent with the input and output pricing model.

#### Cost Calculation
To understand the cost structure better, let's calculate the cost for an average scenario:
- Assume an average input size of 500 tokens per call.
- For 1,000 calls, the total input tokens would be 500,000 tokens.
- Given the pricing, 1M tokens cost $0.1 for input and $0.5 for output. Thus, for 500,000 tokens, the cost would be:


## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### NVIDIA Nemotron 3 Super Benchmark Analysis
#### Model Overview
The NVIDIA Nemotron 3 Super is a standard, non-open-source model released by Nvidia on January 1, 2024. This model has a context window of 262,144 tokens and can generate up to 4,096 tokens as output.

#### Pricing Structure
The pricing for the NVIDIA Nemotron 3 Super is as follows:
* Input: $0.1 per 1M tokens
* Output: $0.5 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Benchmark Performance
The model's performance is measured by the following benchmarks:
* **MMLU (Massive Multitask Language Understanding)**: 80.0 - This score indicates the model's ability to understand and perform a wide range of natural language tasks. A higher MMLU score suggests better performance in tasks such as text classification, sentiment analysis, and question answering.
* **HumanEval**: None - HumanEval is a benchmark that evaluates a model's ability to generate code. The absence of a HumanEval score for the NVIDIA Nemotron 3 Super makes it difficult to assess its coding capabilities.
* **LMSYS Arena ELO**: 1200 - The LMSYS Arena ELO score measures a model's performance in a competitive environment, where it is pitted against other models. An ELO score of 1200 indicates that the NVIDIA Nemotron 3 Super is a strong performer, but its exact ranking is unclear without more context.
* **GSM8K**: None - The GSM8K benchmark evaluates a model's ability to solve

## Competitor Comparison
### NVIDIA Nemotron 3 Super Comparison
#### Overview
The NVIDIA Nemotron 3 Super is a standard-tier model released by Nvidia on 2024-01-01. With no direct competitors listed, this comparison will focus on the model's features, pricing, and performance trade-offs to help determine when to choose this model.

#### Pricing
The NVIDIA Nemotron 3 Super pricing is as follows:
* Input: **$0.1 per 1M tokens**
* Output: **$0.5 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Performance Trade-offs
The model's performance is measured by the following benchmarks:
* MMLU: **80.0**
* LMSYS Arena ELO: **1200**
While there are no direct competitors, these benchmarks provide insight into the model's capabilities.

#### Context and Limits
The model has the following context and limits:
* Context Window: **262,144 tokens**
* Max Output: **4,096 tokens**
* Knowledge Cutoff: **2023-12**

#### Capabilities and Best Use Cases
The NVIDIA Nemotron 3 Super supports the following capabilities:
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
The following cost examples illustrate the model's pricing:
* 1,000 calls (avg 500 tokens): **$0.3**
* 10,000 calls: **$3.0**
* 100,000 calls: **$30.0**

#### Choosing the NVIDIA Nemotron 3 Super
Given the lack of direct competitors, the NVIDIA Nemotron 3 Super is a strong choice for applications that require its supported capabilities, such as chat, text generation, and coding. However, consider the following:
* If your application requires a larger context window or higher output limits, you may need to explore other options.
* If your budget is a concern, the model's pricing may be a factor in your decision.
* If you require a model with more extensive knowledge or a more recent knowledge cutoff, you may need to consider other options.

Ultimately, the NVIDIA Nemotron 3 Super is a powerful model with a range of capabilities, and

## Best Use Cases
### Introduction to NVIDIA Nemotron 3 Super
The NVIDIA Nemotron 3 Super is a powerful language model released by Nvidia on 2024-01-01. With its capabilities in text, function calling, JSON mode, streaming, and structured outputs, it is best suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization.

### Top 5 Best Use Cases for NVIDIA Nemotron 3 Super
#### 1. **Chat and Text Generation**
Given its strengths in text generation and chat, the Nemotron 3 Super can be used to build conversational AI models that can engage in meaningful discussions with users. For example, integrating it with OpenRouter for routing user queries to the most relevant chatbot response:
```python
import openrouter

# Initialize Nemotron 3 Super model
model = openrouter.load_model("nvidia/nemotron-3-super-120b-a12b")

# Define a chat function
def chat(query):
    response = model.generate_text(query, max_length=2048)
    return response

# Route user queries to the chat function
openrouter.route("/chat", chat)
```

#### 2. **Coding and Analysis**
The Nemotron 3 Super can be used for coding tasks such as code completion, code review, and code analysis. Its function calling capability allows it to execute code and provide feedback. For example:
```python
import openrouter

# Initialize Nemotron 3 Super model
model = openrouter.load_model("nvidia/nemotron-3-super-120b-a12b")

# Define a code analysis function
def analyze_code(code):
    result = model.execute_function("analyze_code", code)
    return result

# Route code analysis requests to the analyze_code function
openrouter.route("/analyze_code", analyze_code)
```

#### 3. **RAG Pipelines and Summarization**
The Nemotron 3 Super

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
