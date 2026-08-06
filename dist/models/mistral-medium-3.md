# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-08-06
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a balance between performance and cost. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, this model is well-suited for a variety of tasks, including coding, analysis, and content generation. The model's capabilities include text, vision, function calling, JSON mode, streaming, and system prompts, making it a versatile tool for developers.

### Technical Strengths and Use Cases
Mistral Medium 3's main strengths lie in its ability to handle complex tasks such as coding, summarization, and vision tasks. Its high scores on benchmarks like MMLU (80.0) and HumanEval (77.5) demonstrate its capabilities in these areas. Additionally, its LMSYS Arena ELO score of 1200 indicates a strong performance in competitive evaluations. However, it is not recommended for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms. With a pricing structure of $0.4 per 1M input tokens and $2.0 per 1M output tokens, developers can expect to pay $1.2 for 1,000 calls with an average of 500 tokens, making it a cost-effective option for many use cases.

### Pricing and Competitors
In terms of pricing, Mistral Medium 3 is competitive with other mid-tier models. For example, Claude 3.5 Haiku charges $0.8 per 1M input tokens and $4.0 per 1M output tokens, while GPT-4o Mini charges $0.15 per 1M input tokens and $0.6 per 1M output tokens. However, Mistral Medium 3's unique combination of capabilities and performance make it a strong choice for developers

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. This analysis will delve into the cost structure, optimal usage scenarios, and cost-effectiveness at scale.

#### Cost Structure
The pricing for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### Optimal Usage Scenarios
* **Cached Tokens**: Since cached input tokens are free, it is highly recommended to utilize cached tokens whenever possible to minimize costs.
* **Batch API**: With batch input being free, batching API calls can significantly reduce costs, especially for large-scale applications.

#### Cost at Scale
The cost of using Mistral Medium 3 at various scales is as follows:
* **1,000 calls (avg 500 tokens)**: $1.2
* **10,000 calls**: $12.0
* **100,000 calls**: $120.0

To put these numbers into perspective, let's calculate the cost per call:
* **1,000 calls**: $1.2 / 1,000 calls = $0.0012 per call
* **10,000 calls**: $12.0 / 10,000 calls = $0.0012 per call
* **100,000 calls**: $120.0 / 100,000 calls = $0.0012 per call

The cost per call remains constant at $0.0012, indicating a linear cost structure.

#### Comparison with Top Competitors
Mistral Medium 3's pricing is compared to its top competitors:
* **Claude 3.5 Haiku**: $0.8

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | 77.5 |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Medium 3 Benchmark Performance Analysis
#### Overview
Mistral Medium 3, a mid-tier model provided by Mistral AI, offers a balance of performance and cost. Released on 2025-04-17, this model is not open source.

#### Pricing
The pricing structure for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $None per 1M tokens
* Batch Input: $None per 1M tokens

#### Context and Limits
The model has the following context and limits:
* Context Window: 131,072 tokens
* Max Output: 16,384 tokens
* Knowledge Cutoff: 2024-11

#### Benchmarks
The benchmark performance of Mistral Medium 3 is:
* MMLU: 80.0
* HumanEval: 77.5
* LMSYS Arena ELO: 1200
* GSM8K: None

These benchmarks indicate the model's performance in various areas:
* **MMLU (Massive Multitask Language Understanding)**: A score of 80.0 indicates that Mistral Medium 3 has a strong understanding of natural language, making it suitable for tasks that require comprehension and generation of human-like text.
* **HumanEval**: A score of 77.5 suggests that the model is capable of generating code that is correct and functional, but may require some fine-tuning for specific tasks.
* **LMSYS Arena ELO**: An ELO score of 1200 indicates that the model has a moderate level of competence in a competitive

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will delve into the pricing, performance, and capabilities of Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

#### Pricing Comparison
The pricing for each model is as follows:
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
Performance benchmarks for each model are:
- **Mistral Medium 3**:
  - MMLU: 80.0
  - HumanEval: 77.5
  - LMSYS Arena ELO: 1200
- **Claude 3.5 Haiku**: Not provided
- **GPT-4o Mini**: Not provided

Given the available data, Mistral Medium 3 demonstrates strong performance across various benchmarks, but direct comparisons to its competitors are limited due to missing benchmark data for Claude 3.5 Haiku and GPT-4o Mini.

#### Capabilities and Use Cases
Mistral Medium 3 supports a wide range of capabilities, including:
- Text
- Vision
- Function calling
- JSON mode
- Streaming
- System prompts

It is best suited for tasks such as:
- Coding
- Analysis
- RAG (Retrieval-Augmented Generation)
- Summarization
- Vision tasks
- Content generation
- Function calling

However, it is not recommended for:
- Frontier reasoning
- Bulk cheap tasks
- Simple

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a mid-tier model released on 2025-04-17. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. This model is best suited for tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling.

### Top 5 Best Use Cases for Mistral Medium 3
Given its capabilities and limitations, here are the top 5 best use cases for Mistral Medium 3:

1. **Coding and Development**: With its high performance in coding tasks, Mistral Medium 3 can be used for code completion, code review, and code generation. For example, you can integrate it with OpenRouter to generate code snippets based on user input.
   ```python
import openrouter

def generate_code(prompt):
    # Initialize Mistral Medium 3 model
    model = openrouter.MistralMedium3()
    
    # Generate code based on the prompt
    code = model.generate_code(prompt)
    
    return code

# Example usage
prompt = "Generate a Python function to sort a list of integers"
print(generate_code(prompt))
```

2. **Text Analysis and Summarization**: Mistral Medium 3 can be used for text analysis and summarization tasks, such as summarizing long documents or analyzing user feedback.
   ```python
import openrouter

def summarize_text(text):
    # Initialize Mistral Medium 3 model
    model = openrouter.MistralMedium3()
    
    # Summarize the text
    summary = model.summarize_text(text)
    
    return summary

# Example usage
text = "This is a long piece of text that needs to be summarized."
print(summarize_text(text))
```

3. **Content Generation**: With its ability to generate high-quality text,

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
