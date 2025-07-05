# final_output & output_type:

## final_outpu` kya hota hai?

`final_output` woh result hota hai jo Agent run hone ke baad return karta hai.
Iska format depend karta hai ke `output_type` define kiya gaya hai ya nahi:

| Condition                               | Agent ka Output                | `final_output` ka Type        |
| --------------------------------------- | ------------------------------ | ----------------------------- |
| `output_type` **define nahi** kiya gaya | Plain text (natural language)  | `str`                         |
| `output_type` **define** kiya gaya      | Structured output (jaise JSON) | `YourModel` (Pydantic object) |

---

##  `final_output` ka Type

SDK `final_output` ka type fix nahi karta Kyunkay isy pehle se nahi pata hota ke kaunsa agent complete karega task.

Is liye usually iska type `Any` hota hai.


##  Example – Jab `output_type` define nahi kiya gaya ho

```python
from openai import Agent

agent = Agent(
    name="SimpleAgent",
    instructions="Tell a short joke."
    # output_type nahi diya
)

result = agent.run()
print(result.final_output)
```

### 🔹 Output:

```
"Why don't scientists trust atoms? Because they make up everything!"
```

Yahan `final_output` sirf ek `str` hai.

---

##  Example – Jab `output_type` define kiya gaya ho

```python
from openai import Agent
from pydantic import BaseModel

class JokeOutput(BaseModel):
    setup: str
    punchline: str

agent = Agent(
    name="JokeAgent",
    instructions="Return a joke in JSON format with setup and punchline.",
    output_type=JokeOutput
)

result = agent.run()
print(result.final_output.setup)
print(result.final_output.punchline)
```

### 🔹 Output:

```json
{
  "setup": "Why don't skeletons fight each other?",
  "punchline": "They don't have the guts."
}
```

Ab `final_output` ek structured `JokeOutput` object hai, jisko fields se access kiya ja sakta hai.

---

## output_type ke liye Pydantic kyun use karte hain?

Pydantic use karne ke faide:

* ✅ AI ke structured output ko **validate** kar sakte hain
* ✅ **Schema ka structure ensure** hota hai
* ✅ Dot notation se data **asaani se access** karte hain (`object.field`)
* ✅ Agar format mein error ho to wo **early catch** ho jata hai



