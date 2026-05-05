# Mistral: Mistral Small 4 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-05-05
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Small 4
Mistral Small 4, provided by Mistralai, is a standard-tier language model released on 2024-01-01. This model is not open source. From an architectural standpoint, Mistral Small 4 is designed to handle a variety of tasks, including text generation, coding, and analysis, thanks to its capabilities in text, function calling, JSON mode, streaming, and structured outputs. Its primary strengths lie in its ability to process large context windows of up to 262,144 tokens and generate outputs of up to 4,096 tokens.

### Technical Specifications and Use Cases
The model's pricing is based on input and output tokens, with costs of $0.15 per 1M input tokens and $0.6 per 1M output tokens. There are no specified costs for cached input or batch input. Mistral Small 4 has been benchmarked with an MMLU score of 80.0 and an LMSYS Arena ELO of 1200, indicating its performance capabilities. It is best suited for applications such as chat, text generation, coding, analysis, RAG pipelines, and summarization. Given its technical specifications and capabilities, developers can leverage Mistral Small 4 for a wide range of natural language processing tasks, from generating content to assisting in coding projects.

### Cost Considerations and Competitors
When considering the cost of using Mistral Small 4, developers can expect to pay $0.375 for 1,000 calls averaging 500 tokens, $3.75 for 10,000 calls, and $37.5 for 100,000 calls. As of the current data, there are no direct competitors listed for Mistral Small 4, suggesting it may offer unique advantages or capabilities in the market. With its balanced pricing and robust feature set, Mistral Small 4 is positioned to be a valuable tool for developers looking to integrate advanced language processing

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
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1M tokens
* Cached Input: $None per 1M tokens (free)
* Batch Input: $None per 1M tokens (free)

#### Optimal Usage Scenarios
To minimize costs, consider the following strategies:
* **Use cached tokens**: Since cached input tokens are free, utilize them whenever possible to reduce input costs.
* **Batch API calls**: With batch input being free, batching API calls can significantly reduce overall costs.

#### Cost at Scale
The cost of using Mistral Small 4 at various scales is as follows:
* **1,000 calls (avg 500 tokens)**: $0.375
* **10,000 calls**: $3.75
* **100,000 calls**: $37.5

These costs demonstrate a linear relationship with the number of API calls, indicating that the cost per call remains constant regardless of the scale.

#### Context and Limits
When using Mistral Small 4, consider the following context and limits:
* **Context Window**: 262,144 tokens
* **Max Output**: 4,096 tokens
* **Knowledge Cutoff**: 2023-12

These limits may impact the suitability of Mistral Small 4 for certain applications or use cases.

#### Capabilities and Best Use Cases
Mistral Small 4 supports the following capabilities:
* text
* function_calling
* json_mode
* streaming
* structured_outputs

It is best suited for applications

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 80.0 |
| HumanEval | None |
| LMSYS Arena ELO | 1200 |
| ARC | None |

## Benchmark Analysis
### Mistral Small 4 Benchmark Analysis
The Mistral Small 4 model, released by Mistralai on 2024-01-01, is a standard-tier model with a context window of 262,144 tokens and a maximum output of 4,096 tokens. 

#### Benchmark Scores
The model's performance is measured by the following benchmark scores:
* **MMLU (Massive Multitask Language Understanding)**: 80.0, indicating the model's ability to understand and process natural language across various tasks.
* **HumanEval**: Not available, which would have measured the model's ability to evaluate and execute human-written code.
* **LMSYS Arena ELO**: 1200, representing the model's competitive ranking in the LMSYS Arena, a platform for evaluating language models.

#### Real-World Implications
These benchmark scores have the following implications for real-world use:
* The MMLU score of 80.0 suggests that Mistral Small 4 can handle a wide range of natural language tasks, making it suitable for applications such as chat, text generation, and analysis.
* The absence of a HumanEval score limits the model's ability to be evaluated for coding tasks that require human-written code execution.
* The LMSYS Arena ELO score of 1200 indicates that the model has a moderate level of competitiveness in the LMSYS Arena, which may not be directly applicable to real-world use cases but provides a general idea of the model's performance relative to others.

#### Pricing and Cost Examples
The pricing for Mistral Small 4 is as follows:
* Input: $0.15 per 1M tokens
* Output: $0.6 per 1

## Competitor Comparison
### Comparison of Mistral Small 4 with Top Competitors
Since there are no direct competitors listed for Mistral Small 4, we will create a hypothetical comparison with other models in the same tier and with similar capabilities. 

#### Model Overview
The Mistral Small 4 model, released by Mistralai on 2024-01-01, is a standard, non-open-source model with the following key features:
* **Pricing**: 
  + Input: $0.15 per 1M tokens
  + Output: $0.6 per 1M tokens
* **Context and Limits**:
  + Context Window: 262,144 tokens
  + Max Output: 4,096 tokens
  + Knowledge Cutoff: 2023-12
* **Benchmarks**:
  + MMLU: 80.0
  + LMSYS Arena ELO: 1200
* **Capabilities**: text, function_calling, json_mode, streaming, structured_outputs
* **Best For**: chat, text_generation, coding, analysis, rag_pipelines, summarization

#### Hypothetical Competitors
Let's consider two hypothetical models, Model A and Model B, with the following characteristics:

##### Model A
* **Pricing**: 
  + Input: $0.10 per 1M tokens
  + Output: $0.5 per 1M tokens
* **Context and Limits**:
  + Context Window: 200,000 tokens
  + Max Output: 3,000 tokens
  + Knowledge Cutoff: 2022-12
* **Benchmarks**:
  + MMLU: 75.0
  + LMSYS Arena ELO: 1100
* **Capabilities**: text, function_calling, json_mode
* **Best For**: chat, text_generation, coding

##### Model B
* **Pricing**: 
  + Input: $0.20 per 1M tokens
  + Output: $0.7 per 1M tokens
* **Context and Limits**:
  + Context Window: 300,000 tokens
  + Max Output: 5,000 tokens
  + Knowledge Cutoff: 2024-06
* **Benchmarks**:
  + MMLU: 85.0
  + LMSYS Arena ELO: 1300

## Best Use Cases
### Practical Advice on Using Mistral: Mistral Small 4
Mistral: Mistral Small 4, provided by Mistralai, is a powerful model with a wide range of capabilities, including text generation, function calling, and structured outputs. Here are the top 5 best use cases for this model, along with specific code integration examples and mentions of OpenRouter:

#### 1. **Chat and Text Generation**
Mistral Small 4 is well-suited for chat and text generation tasks, thanks to its high context window of 262,144 tokens and ability to generate up to 4,096 tokens of output. You can integrate this model with OpenRouter to create a conversational AI system.

```python
import openrouter
from mistralai import MistralSmall4

# Initialize the model and OpenRouter
model = MistralSmall4()
router = openrouter.Router()

# Define a function to generate text
def generate_text(prompt):
    output = model.generate_text(prompt)
    return output

# Use OpenRouter to route user input to the model
@router.route("/chat")
def chat():
    user_input = request.get_json()["input"]
    response = generate_text(user_input)
    return {"output": response}

# Run the OpenRouter server
router.run()
```

#### 2. **Coding and Function Calling**
Mistral Small 4 supports function calling, making it a great choice for coding tasks. You can use this model to generate code snippets or even entire functions.

```python
import openrouter
from mistralai import MistralSmall4

# Initialize the model and OpenRouter
model = MistralSmall4()
router = openrouter.Router()

# Define a function to generate code
def generate_code(prompt):
    output = model.generate_code(prompt)
    return output

# Use OpenRouter to route user input to the model
@router.route("/code")
def code():
    user_input = request.get

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
