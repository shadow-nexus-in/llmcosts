# Mistral Large 2 API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated 2026-06-20
> Route cheapest: [OpenRouter](https://openrouter.ai/?ref=llmcosts)

## Overview
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model designed to cater to a wide range of applications, particularly in coding, analysis, and multilingual tasks. This model boasts an impressive architecture that supports capabilities such as text and vision processing, function calling, JSON mode, streaming, and system prompts. With a context window of 131,072 tokens and a maximum output of 4,096 tokens, Mistral Large 2 is well-suited for complex tasks that require extensive contextual understanding.

### Technical Strengths and Use Cases
The technical strengths of Mistral Large 2 are underscored by its benchmark scores: MMLU at 84.0, HumanEval at 92.0, LMSYS Arena ELO at 1225, and GSM8K at 93.0. These scores indicate the model's proficiency in various tasks, making it an ideal choice for developers working on projects that involve coding, analysis, and reasoning. The model's capabilities in function calling, JSON mode, and streaming further enhance its utility in real-world applications. However, it's essential to note that Mistral Large 2 is not recommended for tasks that require embeddings, bulk processing at low costs, real-time responses under 100ms, or vision-heavy applications.

### Pricing and Cost Considerations
Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, with no specified costs for cached input or batch input. For developers, this translates to $6.0 for 1,000 calls with an average of 500 tokens, $60.0 for 10,000 calls, and $600.0 for 100,000 calls. In comparison to its top competitor, GPT-4o, which is priced at $2.5/

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | $3.0 |
| Output | $9.0 |
| Cached Input | $None |
| Batch Input | $None |
| Batch Output | $None |

## Pricing Analysis
### Mistral Large 2 Pricing Analysis
#### Overview
Mistral Large 2, a premium model provided by Mistral AI, offers a range of capabilities including text, vision, function calling, and more. Released on 2024-07-24, this model is not open source. The pricing structure is based on input and output tokens, with specific rates for cached and batch inputs.

#### Cost Structure
The cost structure for Mistral Large 2 is as follows:
* Input: **$3.0 per 1M tokens**
* Output: **$9.0 per 1M tokens**
* Cached Input: **$0 per 1M tokens** (free)
* Batch Input: **$0 per 1M tokens** (free)

#### When to Use Cached Tokens
Cached tokens are free, making them an attractive option when possible. Use cached tokens when:
* The input data is repetitive or has been previously processed.
* The application can tolerate some latency in favor of cost savings.

#### Batch API Savings
Batch inputs are also free, offering significant savings for bulk processing. Use batch API calls when:
* Processing large volumes of data.
* The application can handle batched responses.

#### Cost at Scale
The cost of using Mistral Large 2 at scale is as follows:
* **1,000 calls (avg 500 tokens)**: **$6.0**
* **10,000 calls**: **$60.0**
* **100,000 calls**: **$600.0**

These costs demonstrate a linear scaling of expenses with the number of API calls.

#### Comparison to Top Competitors
Mistral Large 2's pricing is competitive, especially considering its capabilities and performance benchmarks (MMLU: 84.0, HumanEval: 92.0, LMSYS Arena ELO: 1225, GSM8K: 93.0). For example, GPT-4o charges

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | 84.0 |
| HumanEval | 92.0 |
| LMSYS Arena ELO | 1225 |
| ARC | 93.0 |

## Benchmark Analysis
### Analysis of Mistral Large 2 Benchmark Performance
#### Overview
Mistral Large 2, a premium model by Mistral AI, demonstrates strong performance across various benchmarks, including MMLU, HumanEval, and Arena ELO. This analysis will delve into the meaning of these scores and their implications for real-world use.

#### Benchmark Scores
* **MMLU (Massive Multitask Language Understanding)**: A score of 84.0 indicates that Mistral Large 2 has a high level of language understanding, capable of handling a wide range of tasks and topics.
* **HumanEval**: With a score of 92.0, Mistral Large 2 demonstrates excellent performance in evaluating and executing human-written code, showcasing its coding capabilities.
* **LMSYS Arena ELO**: An ELO score of 1225 suggests that Mistral Large 2 has a strong competitive edge in terms of its overall language modeling capabilities, outperforming many other models.

#### Real-World Implications
These benchmark scores imply that Mistral Large 2 is well-suited for tasks that require:
* Advanced language understanding and generation
* Coding and programming capabilities
* Multitask learning and adaptability

In real-world applications, Mistral Large 2 can be effectively used for:
* **Coding and analysis**: With its high HumanEval score, Mistral Large 2 can assist with code completion, debugging, and optimization.
* **RAG (Retrieve, Augment, Generate) tasks**: Its strong language understanding and generation capabilities make it suitable for RAG tasks, such as question answering and text summarization.
* **Agents and multilingual applications**: Mistral Large 2's high MMLU score and

## Competitor Comparison
### Comparison of Mistral Large 2 with Top Competitors
#### Overview
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model. It offers a range of capabilities including text, vision, function calling, JSON mode, streaming, and system prompts. This comparison will focus on its pricing, performance, and use cases against its top competitor, GPT-4o.

#### Pricing Comparison
| Model | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
| --- | --- | --- |
| Mistral Large 2 | $3.0 | $9.0 |
| GPT-4o | $2.5 | $10.0 |

Mistral Large 2 is priced at $3.0 per 1M input tokens and $9.0 per 1M output tokens, whereas GPT-4o is priced at $2.5 per 1M input tokens and $10.0 per 1M output tokens. For input-heavy tasks, GPT-4o is cheaper by $0.5 per 1M tokens, but for output-heavy tasks, Mistral Large 2 is cheaper by $1.0 per 1M tokens.

#### Performance Comparison
Mistral Large 2 has the following benchmark scores:
- MMLU: 84.0
- HumanEval: 92.0
- LMSYS Arena ELO: 1225
- GSM8K: 93.0

GPT-4o's benchmark scores are not provided, making a direct comparison challenging. However, Mistral Large 2's scores indicate strong performance in coding, analysis, and multilingual tasks.

#### Context and Limits
Mistral Large 2 has a context window of 131,072 tokens and a maximum output of 4,096 tokens. Its knowledge cutoff is 2024-07, ensuring it has access to information up to that date.

#### Capabilities and Use Cases
Mistral Large 2 is best suited for:
- Coding
- Analysis
- RAG (Retrieval-Augmented Generation)
- Agents
- Multilingual tasks
- Function calling

It is not recommended for:
- Embeddings
- Bulk cheap tasks
- Real-time tasks with sub-100ms latency
- Vision-heavy tasks

#### Cost

## Best Use Cases
### Introduction to Mistral Large 2
Mistral Large 2, released by Mistral AI on 2024-07-24, is a premium, non-open-source model that excels in various tasks, including coding, analysis, and function calling. With its impressive benchmarks, such as an MMLU score of 84.0 and a HumanEval score of 92.0, it's an ideal choice for applications requiring advanced language understanding and generation capabilities.

### Top 5 Best Use Cases for Mistral Large 2
Based on its capabilities and limitations, here are the top 5 best use cases for Mistral Large 2:

1. **Coding Assistance**: With its high HumanEval score, Mistral Large 2 is well-suited for coding tasks, such as code completion, code review, and code generation. You can integrate it with OpenRouter to provide coding assistance to developers.
   ```python
import openrouter

# Initialize OpenRouter with Mistral Large 2
router = openrouter.Router(model="mistralai/mistral-large-2407")

# Use the model for code completion
def complete_code(prompt):
    response = router.generate(prompt, max_tokens=1024)
    return response

# Test the function
print(complete_code("def hello_world():"))
```

2. **Text Analysis**: Mistral Large 2's high MMLU score indicates its ability to understand and analyze complex texts. You can use it for tasks like text summarization, sentiment analysis, and entity recognition.
   ```python
import openrouter

# Initialize OpenRouter with Mistral Large 2
router = openrouter.Router(model="mistralai/mistral-large-2407")

# Use the model for text summarization
def summarize_text(text):
    prompt = f"Summarize the following text: {text}"
    response = router.generate(prompt, max_tokens=512)
    return response

# Test the

## Frequently Asked Questions


---
*Data verified: 2026-04-08 | Confidence: medium*
*[Get API Access via OpenRouter](https://openrouter.ai/?ref=llmcosts)*
