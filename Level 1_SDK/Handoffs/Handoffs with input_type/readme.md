#  Handoff with input_type:

## 🔹 1. Handoff Kya Hai?

**Handoff** aik method hota hai jismein aik agent doosray agent ko kaam "transfer" karta hai — bilkul jaise aik insan doosray ko kaam de deta hai.

Programming mein:
```python
handoff(
    agent=target_agent,
    on_handoff=handler_function
)
```

 Yahan:
- `agent` = Jis agent ko kaam diya ja raha hai
- `on_handoff` = Wo function jo handoff ke waqt run hota hai


## 🔹 2. Handoff Mein Kya Pass Hota Hai?

LLM agent jab handoff karta hai to 2 cheezein bhejta hai:

| Key         | Kya Hota Hai                                         |
|-------------|------------------------------------------------------|
| `name`      | Jis agent ko kaam diya gaya                          |
| `arguments` | Input data jo us agent ko kaam karne ke liye chahiye |

Example JSON:
```json
{
  "name": "MathAgent",
  "arguments": {
    "question": "What is x squared?"
  }
}
```

## 🔹 3. input_type Kya Hai?

`input_type` batata hai ke tumhara input kis format mein aayega.  
Agar tum structured input dena chahti ho — jaise `question`, `topic`, `name` — to tumhein `input_type` banana zaroori hota hai.

Example:
```python
class MyInput(BaseModel):
    question: str
    topic: str

handoff(
    agent=some_agent,
    on_handoff=handle,
    input_type=MyInput
)
```

Iske bina system nahi samajh payega ke input data ka structure kya hai.

---

## 🔹 4. ctx Kya Hai?

`ctx` ka full naam hai **RunContextWrapper**

Yeh system ka context hota hai — yani:
- User kaun hai
- Kis agent ne kaam bheja
- System memory kya hai
- Last input kya tha
- Output kahan bhejna hai

Function mein hamesha `ctx` pehla argument hota hai.

```python
def greet(ctx):
    print(ctx.input)  # system input ya state show karega
```


## 🔹 5. pydantic aur BaseModel Kya Hote Hain?

- **`pydantic`** ek Python library hai jo input data ko validate karti hai.
- **`BaseModel`** us library ka base class hai jisse hum input ka structure define karte hain.

Example:
```python
from pydantic import BaseModel

class MyInput(BaseModel):
    name: str
    age: int
```

Yahan `name` string hona chahiye, aur `age` number — agar galat input aaya to system error dega.


## 🔹 6. Important Rule – Function aur input_type Matching

| Function Format                              | input_type Required?   | Valid? |
|----------------------------------------------|------------------------|--------|
| `def handler(ctx)`                           |  Nahi                  |  OK    |
| `def handler(ctx, input: MyInput)`           | ✅ Haan                |  OK   |
| `def handler(ctx)` + input_type dia          |  Galat                 |  Error |
| `def handler(ctx, input)` without input_type |  Galat                 |  Error |



## ✅ Full Working Example

```python
from agents import Agent, handoff, Runner, RunContextWrapper
from pydantic import BaseModel
import asyncio

# Step 1: Input structure define karo
class MyInput(BaseModel):
    name: str

# Step 2: GreetAgent banayein
greet_agent = Agent(
    name="GreetAgent",
    instructions="Greet users by name.",
    handoff_description="Says hello."
)

# Step 3: Handoff handler define karein
def greet(ctx: RunContextWrapper, input: MyInput):
    print(f"Hello, {input.name}! 👋")

# Step 4: Handoff create karein with input_type
greet_handoff = handoff(
    agent=greet_agent,
    on_handoff=greet,
    input_type=MyInput
)

# Step 5: MainAgent jo handoff karega
main_agent = Agent(
    name="MainAgent",
    instructions="Pass greeting queries.",
    handoffs=[greet_handoff]
)

# Step 6: System run karein
async def run():
    await Runner.run(
        starting_agent=main_agent,
        input="Say hello to Ayesha"
    )

asyncio.run(run())
```



##  Summary:

| Concept       | Explanation (Simple Words)                             |
|---------------|--------------------------------------------------------|
| `handoff`     | Ek agent doosray ko kaam transfer karta hai            |
| `ctx`         | System ki info jaise user, memory, agent state         |
| `input_type`  | Batata hai ke input ka structure kya hoga              |
| `pydantic`    | Input data ko validate karta hai                       |
| `BaseModel`   | Tumhara input ka structure define karta hai            |





