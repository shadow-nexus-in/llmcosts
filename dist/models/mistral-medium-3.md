# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-25
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Technical Overview of Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a robust set of capabilities for developers. Its architecture is designed to handle a wide range of tasks, including text and vision processing, function calling, and more. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, Mistral Medium 3 is well-suited for complex tasks that require significant input and output processing.

### Strengths and Use-Cases
The main strengths of Mistral Medium 3 lie in its ability to handle tasks such as coding, analysis, and content generation. It is also capable of performing vision tasks, summarization, and function calling. The model's capabilities are further enhanced by its support for features like JSON mode, streaming, and system prompts. With a pricing structure of $0.4 per 1M input tokens and $2.0 per 1M output tokens, Mistral Medium 3 offers a cost-effective solution for developers who need to process large amounts of data. For example, 1,000 calls with an average of 500 tokens would cost $1.2, while 10,000 calls would cost $12.0.

### Comparison and Cost Considerations
In comparison to its top competitors, such as Claude 3.5 Haiku and GPT-4o Mini, Mistral Medium 3 offers a unique set of capabilities and pricing. While Claude 3.5 Haiku charges $0.8/1M input and $4.0/1M output, and GPT-4o Mini charges $0.15/1M input and $0.6/1M output, Mistral Medium 3 provides a more balanced approach with its pricing. Additionally, Mistral Medium 3 has a higher MMLU benchmark score of 80.0, indicating

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $0.4 |
| Output | $2.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Pricing Analysis for Mistral Medium 3
#### Overview
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. It is not open source. The pricing structure is based on input and output tokens.

#### Cost Structure
The cost structure for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option for reducing costs. Use cached tokens when:
* The input data is repetitive or has a high degree of similarity.
* The model is being used for tasks that require minimal input variation.

#### Batch API Savings
Batch input is also free, which can lead to significant cost savings when making multiple API calls. To maximize batch API savings:
* Group multiple requests into a single batch whenever possible.
* Optimize batch size to minimize the number of API calls while maximizing the number of requests per call.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* 1,000 calls (avg 500 tokens): $1.2
* 10,000 calls: $12.0
* 100,000 calls: $120.0

These costs can be broken down into input and output costs. Assuming an average of 500 tokens per call:
* 1,000 calls: 500,000 tokens
	+ Input cost: 500,000 tokens / 1,000,000 tokens per $0.4 = $0.2
	+ Output cost: assuming an average output of 100 tokens per call (conservative estimate), 100,000 tokens / 

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
The Mistral Medium 3 model, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. The model is not open source.

#### Pricing
The pricing for Mistral Medium 3 is as follows:
* Input: **$0.4 per 1M tokens**
* Output: **$2.0 per 1M tokens**
* Cached Input: **$None per 1M tokens**
* Batch Input: **$None per 1M tokens**

#### Benchmark Performance
The benchmark performance of Mistral Medium 3 is measured by the following metrics:
* **MMLU (Massive Multitask Language Understanding)**: 80.0 - This score indicates the model's ability to understand and perform a wide range of natural language processing tasks. A higher MMLU score suggests better performance in tasks such as text classification, sentiment analysis, and question answering.
* **HumanEval**: 77.5 - This score evaluates the model's ability to generate human-like code and perform programming tasks. A higher HumanEval score indicates better performance in coding and programming-related tasks.
* **LMSYS Arena ELO**: 1200 - This score measures the model's performance in a competitive arena, where it is pitted against other models in a variety of tasks. A higher ELO score suggests better overall performance and competitiveness.

#### Real-World Implications
The benchmark performance of Mistral Medium 3 suggests that it is well-suited for tasks such as:
* Coding and programming
* Analysis and

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a unique set of capabilities and pricing. This comparison will delve into the details of Mistral Medium 3 versus its top competitors, Claude 3.5 Haiku and GPT-4o Mini, highlighting price differences, performance trade-offs, and use cases for each model.

#### Pricing Comparison
The pricing for each model is as follows:
* **Mistral Medium 3**:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* **Claude 3.5 Haiku**:
	+ Input: $0.8 per 1M tokens
	+ Output: $4.0 per 1M tokens
* **GPT-4o Mini**:
	+ Input: $0.15 per 1M tokens
	+ Output: $0.6 per 1M tokens

Mistral Medium 3 offers a balance between input and output costs, while Claude 3.5 Haiku is more expensive on both fronts. GPT-4o Mini, on the other hand, is significantly cheaper for input but also for output.

#### Performance Trade-offs
The performance of each model can be evaluated using various benchmarks:
* **Mistral Medium 3**: MMLU (80.0), HumanEval (77.5), LMSYS Arena ELO (1200)
* **Claude 3.5 Haiku**: Not provided
* **GPT-4o Mini**: Not provided

While the exact performance of Claude 3.5 Haiku and GPT-4o Mini is not available, Mistral Medium 3 demonstrates strong capabilities in coding, analysis, and other tasks.

#### Capabilities and Use Cases
Each model has its strengths and weaknesses:
* **Mistral Medium 3**: Best for coding, analysis, RAG, summarization, vision tasks, content generation, and function calling. Not suitable for frontier reasoning, bulk cheap tasks, simple classification, or real-time sub-100ms tasks.
* **Claude 3.5 Haiku**: Capabilities not provided
* **GPT-4o Mini**: Capabilities not provided

Given the information available,

## Best Use Cases
### Introduction to Mistral Medium 3
Mistral Medium 3, provided by Mistral AI, is a powerful language model with a wide range of capabilities, including text, vision, function calling, and more. Released on 2025-04-17, this model is well-suited for various tasks such as coding, analysis, and content generation.

### Top 5 Best Use Cases for Mistral Medium 3
Based on its capabilities and limitations, here are the top 5 best use cases for Mistral Medium 3:

1. **Coding and Development**: With its strong coding capabilities, Mistral Medium 3 can be used for tasks such as code completion, code review, and code generation. For example, you can use it with OpenRouter to generate code snippets:
   ```python
import openrouter

# Initialize the model
model = openrouter.Model("mistralai/mistral-medium-3")

# Generate code snippet
def generate_code(prompt):
    response = model.generate(prompt, max_tokens=100)
    return response

print(generate_code("Write a Python function to sort a list"))
```

2. **Text Analysis and Summarization**: Mistral Medium 3 can be used for text analysis and summarization tasks, such as summarizing long documents or analyzing customer feedback. For example:
   ```python
import openrouter

# Initialize the model
model = openrouter.Model("mistralai/mistral-medium-3")

# Summarize text
def summarize_text(text):
    prompt = f"Summarize the following text: {text}"
    response = model.generate(prompt, max_tokens=200)
    return response

print(summarize_text("This is a long piece of text that needs to be summarized"))
```

3. **Content Generation**: With its strong content generation capabilities, Mistral Medium 3 can be used for tasks such as writing articles, generating product descriptions, and creating social media

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
