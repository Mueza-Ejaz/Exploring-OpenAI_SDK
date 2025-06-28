# Notes: How to Configure LLM Providers (Other than OpenAI) in Agents SDK


##  Why Configure LLM Providers?
By default, Agents SDK uses OpenAI’s models (like GPT-4).  
But if you want to use **Google Gemini**, **Anthropic Claude**, or **Mistral**, you need to configure it manually.

SDK allows configuration at three levels:


## 1. ✅ Agent-Level Configuration

**Use:** When only one specific agent should use a different model (e.g., Gemini).

```python
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel

client = AsyncOpenAI(
    api_key="your_gemini_key",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

agent = Agent(
    name="HaikuBot",
    instructions="You only respond in haikus.",
    model=OpenAIChatCompletionsModel(model="gemini-2.0", openai_client=client)
)
```

---

## 2. ✅ Run-Level Configuration

**Use:** When all agents in a single run should use the same model.

```python
from agents import Runner, RunConfig

run_config = RunConfig(
    default_model=OpenAIChatCompletionsModel(model="gemini-2.0", openai_client=client)
)

result = await Runner.run(
    agents=[agent1, agent2],
    input="Help me plan a vacation.",
    config=run_config
)
```

---

## 3. ✅ Global-Level Configuration

**Use:** When you want to set a default model for the whole application.

```python
from agents import set_global_default_model

set_global_default_model(
    OpenAIChatCompletionsModel(model="gemini-2.0", openai_client=client)
)

# Now agents use Gemini by default
agent = Agent(
    name="SmartBot",
    instructions="Answer clearly and kindly."
)
```

---

## 🔚 Final Summary

| Level           | Scope                       | When to Use?                     |
|-----------------|-----------------------------|----------------------------------|
| Agent-Level     | Single agent only           | When each agent needs a different model |
| Run-Level       | One run (multiple agents)   | All agents use same model temporarily |
| Global-Level    | Entire project              | Always use the same model        |
---

## ❓ Common Confusion: Does `openai-agents` only support OpenAI models?

### ✅ Short Answer: No, it supports others too!

When you install the SDK using:

```bash
uv add openai-agents
```

You are installing **OpenAI's official multi-agent orchestration framework** — also known as the **Agents SDK**.

### 🔸 By default:
It is configured to work with **OpenAI models** like GPT-3.5 and GPT-4 automatically.

### 🔸 But it is flexible:
It also supports **any other LLM provider** that follows the **OpenAI-style API format**.

### ✅ Examples of Supported Providers:

| Provider            | Supported | Notes                                                |
|---------------------|-----------|------------------------------------------------------|
| OpenAI (GPT-4)      | ✅ Yes    | Default — no setup needed                            |
| Google Gemini       | ✅ Yes    | Needs custom API key and base URL                    |
| Anthropic Claude    | ✅ Yes    | Use OpenAI-compatible wrapper client                 |
| Mistral             | ✅ Yes    | Compatible via OpenAI-style APIs                     |

### ✅ So what does SDK really do?
- Defines and manages agents
- Coordinates multi-agent workflows
- Lets you plug in **any LLM provider** that supports the same API pattern

### 🔚 Conclusion:
Even though it's called `openai-agents`, this SDK is designed to be **open and flexible**, not limited to OpenAI only. You can 
use it with various LLMs like Gemini, Claude, Mistral — as long as their APIs are compatible.




