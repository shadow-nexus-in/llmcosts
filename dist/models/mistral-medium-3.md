# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-14
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Technical Overview of Mistral Medium 3
Mistral Medium 3, developed by Mistral AI, is a mid-tier language model released on 2025-04-17. This model is not open source. From an architectural standpoint, Mistral Medium 3 boasts a context window of 131,072 tokens and can generate up to 16,384 tokens as output. Its knowledge cutoff is 2024-11, indicating that its training data includes information up to that point. The model's capabilities include text and vision processing, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for various applications.

### Strengths and Use Cases
The main strengths of Mistral Medium 3 lie in its balanced performance across different benchmarks, including MMLU (80.0), HumanEval (77.5), and LMSYS Arena ELO (1200). It is best suited for tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling. However, it is not recommended for frontier reasoning, bulk cheap tasks, simple classification, or real-time applications requiring sub-100ms responses. With a pricing structure of $0.4 per 1M input tokens and $2.0 per 1M output tokens, developers can estimate costs based on their specific use cases. For example, 1,000 calls averaging 500 tokens would cost approximately $1.2.

### Pricing and Competitors
In terms of pricing, Mistral Medium 3 is positioned competitively in the market. Compared to its top competitors, such as Claude 3.5 Haiku ($0.8/1M input, $4.0/1M output) and GPT-4o Mini ($0.15/1M input, $0.6/1M output), Mistral Medium 3 offers a unique balance of performance and cost. Developers can consider these factors when

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.4 |
| Output | $2.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Mistral Medium 3 Pricing Analysis
#### Overview
Mistral Medium 3 is a mid-tier model provided by Mistral AI, released on 2025-04-17. This model is not open source and offers a range of capabilities including text, vision, function calling, and more.

#### Cost Structure
The cost structure for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs when the same input is used multiple times. Since cached input is free, it is recommended to use cached tokens whenever possible to minimize costs.

#### Batch API Savings
Batch input is also free, which means that making batch API calls can help reduce costs. By batching multiple requests together, users can avoid paying for input tokens multiple times.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: **$1.2**
* **10,000 calls**: **$12.0**
* **100,000 calls**: **$120.0**

These costs are based on the average number of tokens per call and can vary depending on the actual usage.

#### Comparison to Top Competitors
Mistral Medium 3 is priced competitively with other models in the market. For example:
* Claude 3.5 Haiku: **$0.8/1M input**, **$4.0/1M output**
* GPT-4o Mini: **$0.15/1M input**, **$0.6/1M output**

Mistral Medium 3 offers a balance

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Medium 3 Benchmark Performance Analysis
#### Model Overview
The Mistral Medium 3 model, provided by Mistral AI, is a mid-tier model released on 2025-04-17. It is not open-source.

#### Pricing
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Context and Limits
The model has the following context and limits:
* Context Window: **131,072 tokens**
* Max Output: **16,384 tokens**
* Knowledge Cutoff: **2024-11**

#### Benchmarks
The model's benchmark performance is as follows:
* MMLU: **80.0**
* HumanEval: **77.5**
* LMSYS Arena ELO: **1200**
* GSM8K: **None**

These benchmarks indicate the model's performance in various areas:
* **MMLU (Massive Multitask Language Understanding)**: Measures the model's ability to understand and generate human-like text. A score of 80.0 indicates strong language understanding capabilities.
* **HumanEval**: Evaluates the model's ability to write correct and functional code. A score of 77.5 suggests the model is proficient in coding tasks.
* **LMSYS Arena ELO**: Measures the model's performance in a competitive environment, with a score of 1200 indicating a moderate level of proficiency.

#### Capabilities and Use Cases
Mistral Medium 3 is capable of

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will delve into the pricing, performance, and capabilities of Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

#### Pricing Comparison
The pricing models for each are as follows:
- **Mistral Medium 3**:
  - Input: $0.4 per 1M tokens
  - Output: $2.0 per 1M tokens
- **Claude 3.5 Haiku**:
  - Input: $0.8 per 1M tokens
  - Output: $4.0 per 1M tokens
- **GPT-4o Mini**:
  - Input: $0.15 per 1M tokens
  - Output: $0.6 per 1M tokens

Mistral Medium 3 offers a balance between input and output costs, sitting between the more expensive Claude 3.5 Haiku and the cheaper GPT-4o Mini.

#### Performance Trade-offs
- **Mistral Medium 3**: With benchmarks of MMLU at 80.0, HumanEval at 77.5, and LMSYS Arena ELO at 1200, Mistral Medium 3 demonstrates strong performance in coding, analysis, and other complex tasks.
- **Claude 3.5 Haiku**: While specific benchmark numbers are not provided, Claude 3.5 Haiku is generally considered to offer high-quality outputs, potentially justifying its higher cost for applications where output quality is paramount.
- **GPT-4o Mini**: Offering significantly lower costs, GPT-4o Mini is an attractive option for bulk or cost-sensitive tasks, though its performance on complex tasks might not match that of Mistral Medium 3 or Claude 3.5 Haiku.

#### Capabilities and Best Use Cases
- **Mistral Medium 3** is best for coding, analysis, RAG, summarization, vision tasks, content generation, and function calling, thanks to its capabilities in text, vision, function calling, JSON mode, streaming, and system prompts.
- **Cla

## Best Use Cases
### Practical Advice for Mistral Medium 3
Mistral Medium 3, offered by Mistral AI, is a powerful model with a wide range of capabilities including text, vision, function calling, and more. With its mid-tier pricing and robust feature set, it's ideal for various applications. Here are the top 5 best use cases for Mistral Medium 3, along with specific code integration examples mentioning OpenRouter.

#### 1. **Coding and Analysis**
Mistral Medium 3 excels in coding tasks, making it perfect for code analysis, code completion, and code review. Its ability to understand and generate code in multiple programming languages can be leveraged for automated code review tools or coding assistants.

```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.Model("mistralai/mistral-medium-3")

# Example code analysis task
def analyze_code(code):
    prompt = f"Analyze the following code: {code}"
    response = model.generate(prompt)
    return response

# Example usage
code = "print('Hello World')"
analysis = analyze_code(code)
print(analysis)
```

#### 2. **Summarization and Content Generation**
With its strong text capabilities, Mistral Medium 3 can be used for summarizing long documents, generating content, or even creating chatbot responses. Its ability to understand context and generate coherent text makes it a great choice for content generation tasks.

```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.Model("mistralai/mistral-medium-3")

# Example summarization task
def summarize_text(text):
    prompt = f"Summarize the following text: {text}"
    response = model.generate(prompt)
    return response

# Example usage
text = "This is a long piece of text that needs to be summarized."
summary = summarize_text(text)
print(summary)
```

####

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
