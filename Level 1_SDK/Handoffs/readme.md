#  Multi-Agent System with handoffs

Yeh project ek multi-agent system ko explain karta hai jahan aik main agent (jaise `TriageAgent`) tools ka use karta hai aur agar zarurat ho to
kisi aur agent (sub-agent ya handoff agent) ko control de deta hai taake wo query ka hissa solve kare.


###  1. Agent kya hota hai?
Agent aik intelligent worker hota hai jo:
- User ki query samajhta hai
- Tools ka use karta hai
- Decision leta hai
- Aur zarurat par kisi aur agent ko kaam de sakta hai


Do tarah ke agents hote hain:
- `TriageAgent` (main agent)
- Sub-agents (jaise `TranslatorAgent`, etc.)


###  2. Tool kya hota hai?
Tool aik chhoti utility ya function hoti hai jo agent kisi kaam ke liye use karta hai.

Examples:
- `weather_tool` → mausam batata hai
- `translate_tool` → text translate karta hai



### 🔁 3. Handoff kya hota hai?
Agar user ki query ka koi hissa kisi aur agent se related ho, to:
- `TriageAgent` pehle apna tool chalata hai
- Phir control handoff karta hai kisi aur agent ko (jaise `TranslatorAgent`) ko



###  4. Reasoning aur Final Output

- Tools ka result sirf agent ke thinking (reasoning) ke liye hota hai.
- Agar handoff hota hai, to sirf **last agent ka jawab** user ko diya jata hai.
- Pehle wale tool ka result **user ko nahi dikhaya jata** jab tak manually include na kiya jaye.



###  5. Example Scenario

**User Query:**
> "Mujhe kal ka mausam batao aur usay Urdu mein translate karo."

**System ka Flow:**
1. `TriageAgent` detect karta hai ke "weather" ki request hai → `weather_tool` chalata hai
2. Result: "Tomorrow will be sunny." → (ye sirf internal reasoning ke liye use hota hai)
3. Phir wo detect karta hai ke "translate" bhi karna hai → handoff karta hai `TranslatorAgent` ko
4. `TranslatorAgent` `translate_tool` use karke answer deta hai: "Kal ka mausam dhoopdaar hoga."
5. **Final output sirf ye translated message hota hai**

💡 Yaad rahe: Pehle wale `weather_tool` ka output show nahi hota jab tak aap manually na dikhao.

---

###  6. Intermediate Results kaise nikalein?

Agar aapko har step ka record chahiye to:

#### ✅ `result.messages` ka use karo
Yeh ek list hoti hai jismein sab agents ke messages hote hain.

Example:
```python
for msg in result.messages:
    print(f"{msg['agent']} said: {msg['message']}")
```

Output:
```
TriageAgent said: Weather is sunny.
TranslatorAgent said: Kal ka mausam dhoopdaar hoga.
```

####   `AgentHooks` ka use karo
Agar aapko tool ya message execution ka real-time track chahiye to hooks ka use karo.

Example:
```python
def on_tool_call(agent_name, tool_name, input_data):
    print(f"{agent_name} ne {tool_name} use kiya with input: {input_data}")

runner = Runner(agents=..., hooks={"on_tool_call": on_tool_call})
```


