# Handoff Mechanism:

##  What is `handoff`?
`handoff` ek mechanism hai jisme ek agent (Agent A) apna task kisi doosre agent (Agent B) ko transfer karta hai — jese math-related query 
math expert ko de dena.Yeh architecture multi-agent collaboration ke liye use hota hai.


## 🏗 Core Components:

### 1. Agent
Yeh ek **LLM-based assistant** hota hai jo instructions aur tools ke sath define kiya jata hai.

```python
agent = Agent(
    name="Math Agent",
    instructions="Answer math-related questions",
    tools=[],
    model=model
)
```

### 2. Runner
Runner ek **control loop** hota hai jo agents ke beech conversations manage karta hai:
- User sy input leta hai
- Agent ko call karta hai
- Agent se output check karta hai
- Tool ya handoff call detect karta hai
- Jab tak `final_output` nahi milta, loop chalta rehta hai

```python
runner = autoloop(agent=triage_agent)
```


##  Handoff Configuration

### `handoff()` Function

```python
from openai import handoff

math_tool = handoff(
    agent=math_agent,
    tool_name_override="solve_math_problem",
    tool_description_override="Use this to solve math problems"
)
```

### Parameters Explained

| Parameter                   | Description                                               |
|-----------------------------|-----------------------------------------------------------|
| `agent`                     | Jo agent is handoff mein receive karega (target agent)    |
| `tool_name_override`        | Tool ka naam jo user-facing show hoga                     |
| `tool_description_override` | Description of the tool                                   |
| `input_type`                | Schema of the input to pass                               |
| `input_filter`              | Yeh decide karta hai ke agent ko kaunsa context diya jaye |
| `on_handoff`                | Optional callback jab handoff trigger ho                  |



##  Built-in Input Filters

`input_filter` ka role yeh hota hai ke **sub-agent ko sirf relevant context** diya jaye. Kuch built-in filters:

- `remove_all_tools`       → tool call history hata deta hai
- `remove_system_messages` → system prompts ko hata deta hai
- `remove_agent_messages`  → sirf user ke messages forward karta hai

**Custom filter example:**

```python
def only_user(HandoffInputData):
    user_msgs = [m for m in HandoffInputData.thread if m.role == "user"]
    return HandoffInputData(thread=user_msgs)
```

---

## 🤖 Agent Example:

```python
triage_agent = Agent(
    name="Triage Agent",
    instructions=(
        "Answer user questions. "
        "If it's math, hand off to the math agent. "
        "If it's physics, hand off to the physics agent."
    ),
    handoffs=[math_tool, physics_tool],
    model=model
)
```


## 🔄 How the Agent Loop Works:

####  Step 1: User Input

```text
User: "2 + 2 kya hota hai?"
```

####  Step 2: Triage Agent Execution

Runner prepares system prompt:

```text
You are a triage agent...
User: 2 + 2 kya hota hai?
```

LLM internally decides:

- Should I answer myself?
- Or should I call a tool (handoff)?

####   Step 3: Handoff Triggered

Agar LLM ne handoff tool call kiya:

```json
{"tool_call": "solve_math_problem", "arguments": {"question": "2 + 2"}}
```

To runner:

- Input filter lagata hai
- Filtered thread ko **Math Agent** ko de deta hai

####  Step 4: Sub-Agent Response

Math Agent ke instructions ke sath:

```text
You are a math expert. User: 2 + 2 kya hota hai?
```

LLM Output:

```text
2 + 2 = 4
```

Ye `final_output` hota hai → loop yahin rukta hai.


##   Multiple Handoffs Scenario

Agar agent A → B → C tak handoff hota hai:

- Runner sab ko call karta hai
- Jab tak koi agent `final_output` nahi deta, loop chalta rehta hai
- Ye recursive, intelligent delegation system hai





