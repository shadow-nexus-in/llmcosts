# Mistral Medium 3 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-17
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Technical Overview of Mistral Medium 3
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model that offers a robust set of capabilities for developers. Its architecture is designed to handle a wide range of tasks, including text and vision processing, function calling, and JSON mode. With a context window of 131,072 tokens and a maximum output of 16,384 tokens, Mistral Medium 3 is well-suited for tasks that require in-depth analysis and generation of content. The model's knowledge cutoff is 2024-11, ensuring that it has a solid foundation of knowledge up to that point.

### Main Strengths and Primary Use-Cases
Mistral Medium 3 excels in tasks such as coding, analysis, RAG, summarization, vision tasks, content generation, and function calling. Its strengths are reflected in its benchmark scores, including an MMLU score of 80.0, a HumanEval score of 77.5, and an LMSYS Arena ELO score of 1200. However, it is not recommended for tasks that require frontier reasoning, bulk cheap tasks, simple classification, or real-time responses under 100ms. Developers can leverage Mistral Medium 3's capabilities to build applications that require in-depth analysis, content generation, and vision tasks, among others. The model's pricing is competitive, with input costs of $0.4 per 1M tokens and output costs of $2.0 per 1M tokens.

### Pricing and Cost Examples
The pricing for Mistral Medium 3 is as follows: $0.4 per 1M tokens for input, $2.0 per 1M tokens for output, with no costs for cached input or batch input. To give developers a better idea of the costs involved, some examples are provided: 1,000 calls with an average of 500 tokens would cost

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
Mistral Medium 3, provided by Mistral AI, is a mid-tier model with a release date of 2025-04-17. It is not open source. The pricing structure for this model is based on input and output tokens.

#### Cost Structure
The cost structure for Mistral Medium 3 is as follows:
* Input: $0.4 per 1M tokens
* Output: $2.0 per 1M tokens
* Cached Input: $0 per 1M tokens (free)
* Batch Input: $0 per 1M tokens (free)

#### When to Use Cached Tokens
Cached tokens can be used to reduce costs when the same input is used multiple times. Since cached input is free, it is recommended to use cached tokens whenever possible to minimize costs.

#### Batch API Savings
Batching API calls can also help reduce costs. Although the pricing for batch input is listed as $0 per 1M tokens, the actual cost savings come from reducing the number of API calls. By batching calls, users can take advantage of the free batch input pricing and reduce their overall costs.

#### Cost at Scale
The cost of using Mistral Medium 3 at scale is as follows:
* 1,000 calls (avg 500 tokens): $1.2
* 10,000 calls: $12.0
* 100,000 calls: $120.0

To calculate the cost per call, we can divide the total cost by the number of calls:
* 1,000 calls: $1.2 / 1,000 = $0.0012 per call
* 10,000 calls: $12.0 / 10,000 = $0.0012 per call
* 100,000 calls: $120.0 / 100,000 = $0.0012 per call

As shown

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
Mistral Medium 3, a mid-tier model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2025-04-17, this model is not open source.

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
Mistral Medium 3 has the following benchmark scores:
* **MMLU: 80.0** - This score indicates the model's performance on a set of tasks that require reasoning and understanding of natural language. A higher score suggests better performance.
* **HumanEval: 77.5** - This score measures the model's ability to generate human-like code. A higher score indicates better coding capabilities.
* **LMSYS Arena ELO: 1200** - This score represents the model's performance in a competitive arena, with higher scores indicating better performance.

#### Real-World Implications
The benchmark scores suggest that Mistral Medium 3 is suitable for tasks that require:
* Reasoning and understanding of natural language (MMLU: 80.0)
* Generating human-like code (HumanEval: 

## Competitor Comparison
### Comparison of Mistral Medium 3 with Top Competitors
#### Overview
Mistral Medium 3, released by Mistral AI on 2025-04-17, is a mid-tier model with a context window of 131,072 tokens and a maximum output of 16,384 tokens. This comparison will analyze the pricing, performance, and capabilities of Mistral Medium 3 against its top competitors, Claude 3.5 Haiku and GPT-4o Mini.

#### Pricing Comparison
The pricing for each model is as follows:
* Mistral Medium 3:
	+ Input: $0.4 per 1M tokens
	+ Output: $2.0 per 1M tokens
* Claude 3.5 Haiku:
	+ Input: $0.8 per 1M tokens (100% more than Mistral Medium 3)
	+ Output: $4.0 per 1M tokens (100% more than Mistral Medium 3)
* GPT-4o Mini:
	+ Input: $0.15 per 1M tokens (62.5% less than Mistral Medium 3)
	+ Output: $0.6 per 1M tokens (70% less than Mistral Medium 3)

#### Performance Comparison
The performance benchmarks for each model are:
* Mistral Medium 3:
	+ MMLU: 80.0
	+ HumanEval: 77.5
	+ LMSYS Arena ELO: 1200
* Claude 3.5 Haiku: Not provided
* GPT-4o Mini: Not provided

#### Capabilities and Use Cases
Mistral Medium 3 is best suited for tasks such as:
* Coding
* Analysis
* RAG (Retrieve, Augment, Generate)
* Summarization
* Vision tasks
* Content generation
* Function calling

It is not recommended for:
* Frontier reasoning
* Bulk cheap tasks
* Simple classification
* Real-time tasks with sub-100ms latency

#### Cost Examples
The cost of using Mistral Medium 3 for different scenarios is:
* 1,000 calls (avg 500 tokens): $1.2
* 10,000 calls: $12.0
* 100,000 calls: $120.0

#### Choosing the Right Model
Based on the pricing and performance comparison, here are some

## Best Use Cases
### Practical Advice for Mistral Medium 3
Mistral Medium 3, offered by Mistral AI, is a mid-tier model with a wide range of capabilities, including text, vision, function calling, JSON mode, streaming, and system prompts. Given its strengths and pricing, here are the top 5 best use cases for Mistral Medium 3, along with specific code integration examples mentioning OpenRouter.

#### 1. **Coding and Analysis**
Mistral Medium 3 excels in coding and analysis tasks. Its high MMLU score of 80.0 and HumanEval score of 77.5 make it an ideal choice for tasks that require in-depth code understanding and generation. 
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Example coding task
def generate_code(prompt):
    response = model.generate(prompt)
    return response

# Test the function
print(generate_code("Write a Python function to sort a list of integers"))
```

#### 2. **Summarization and Content Generation**
With its strong text capabilities, Mistral Medium 3 is well-suited for summarization and content generation tasks. Its context window of 131,072 tokens allows for the processing of large documents.
```python
import openrouter

# Initialize Mistral Medium 3 model
model = openrouter.MistralMedium3()

# Example summarization task
def summarize_text(text):
    prompt = f"Summarize the following text: {text}"
    response = model.generate(prompt)
    return response

# Test the function
text = "Your large document text here"
print(summarize_text(text))
```

#### 3. **Vision Tasks**
Mistral Medium 3's vision capabilities make it a good choice for tasks such as image classification, object detection, and image generation.
```python
import openrouter

# Initialize Mistral Medium

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
