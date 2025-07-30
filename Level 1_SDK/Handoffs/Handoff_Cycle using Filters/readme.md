# 🔁 Handoff Cycle with input_filters

## Example Scenario:

Jab koi user input dein, to HistoryAgent check kare.  
Agar woh input uske kaam ka nahi (yaani history ka sawal nahi) to woh handoff kare ScienceAgent ko.  
Phir ScienceAgent bhi agar na samjhe to MathAgent ko handoff kare.  
Agar MathAgent bhi nahi samjhe to woh dobara HistoryAgent ko handoff kare.

Yeh cycle ban jaata hai:
`History → Science → Math → History → ...`


### 1. **Handoff**
Jab aik agent kisi doosray agent ko kaam de deta hai, isay `handoff()` kehtay hain.

Syntax:
```python
handoff(agent=ScienceAgent, input_filter=history_input_filter)
```

Yahan:
- `agent=` jis agent ko next bhejna hai
- `input_filter=` aik chhota function hota hai jo input ko modify karta hai before handoff


### 2. **Input Filter**
Yeh aik function hota hai jo handoff se pehle input ko change karta hai.

Example:
```python
def history_input_filter(input: HandoffInputData) -> HandoffInputData:
    print("📘 History Input Filter Triggered")
    input.input_history = "What is gravity?"
    return input
```

Yahan `input.input_history` aik property hai `HandoffInputData` class ki, jo user ka previous query ya context hold karta hai.

---

## ⚙️ Execution Code Summary:

```python
async def main():
    result = await Runner.run(
        starting_agent=history_agent,
        input="Who discovered Newton's Laws?",
        run_config=config,
        hooks=MyHooks()
    )
```

- Yahan `input=` se user ka sawal pass kiya gaya hai.
- Yehi sawal baad mein `input_filter` function mein `input` ya `x` variable ke zariye modify hota hai.
- Variable ka naam alag ho sakta hai, lekin data wahi hota hai jo user ne diya hota hai.


### 3. **Hooks** – Jaise Logging / Debugging ka kaam
```python
class MyHooks(RunHooks):
    async def on_handoff(self, context, from_agent, to_agent):
        print(f"👋 {from_agent.name} handed off to {to_agent.name}")
```

Yeh optional class hoti hai jo track karti hai ke handoff kab aur kahan hua.

---

### 4. **Cycle Problem (Error)**
Agar har agent ke input filter aise design hon ke woh input ko irrelevant bana dein, to koi bhi agent us input ko accept nahi karega — aur system phir `infinite loop` mein chala jaata hai:

```python
RecursionError: maximum recursion depth exceeded
```

Yani cycle bar bar chalta hai:  
`History → Science → Math → History → Science → ...` — bina rukay.

---

### 5. ❗ Solution to Break the Cycle:

Cycle todhne ke kuch tareeqay:

✅ **Marker Add Karna**:  
Input ke andar `forwarded: True` jaisa flag bhejna, jisse agla agent samajh jaye ke pehle bhi yeh input pass ho chuka hai.

✅ **Depth Count**:  
Ek counter rakhna ke handoff 3 se zyada na ho.

✅ **Smart Input Filters**:  
Har filter ko realistic banao, taake next agent us input ko samajh jaye.


🎯 **Final Lesson:**
Handoff system strong hai lekin risky bhi. Agar filters ya logic galat ho, to AI cycle mein phans jata hai.

Isliye:
- Har agent ko smart banao
- Har input filter meaningful banao
- Aur cycle break karne ka system zaroor lagao.



