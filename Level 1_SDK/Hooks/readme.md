# Hooks Lifecycle:

##   Hook kya hota hai?
"Jab koi kaam ho raha ho, us waqt hum us moment ko pakar ke us par kuch apna kaam kar sakein." Ye ek function hota hai ya method, jo kisi
event par chalta hai — bina manually call kiye hue.


## Event kya hoti hai?

- Agent ka start hona
- Agent ka end hona
- Tool ka start hona
- Tool ka end hona
- Error aana etc.


## Hook ka kaam kya hota hai?
"Kisi bhi event ke waqt automatically chalu ho jana." Jaise hi agent start hota hai, hook khud ba khud chal jaata hai, hume manually call nahi karna padta.


##  Hooks k Kitne Types hote hain?

### 1️⃣ RunHooks – (System Level Hooks)

- Ye **automatically** har agent, tool, step pe chalte hain.
- Agar aap kuch bhi manually set na karo, to bhi SDK ye RunHooks laga deta hai.

```python
if hooks is None:
    hooks = RunHooks()  #  SDK khud laga deta hai
```

 Hamesha active  
 Aapko kuch nahi karna padta



### 2️⃣ AgentHooks – (Sirf Specific Agent k liye)

- Ye tabhi chalte hain jab aap **manually** agent ko hooks assign karo.
- Agar aap hooks=... nahi dogi → ye bilkul nahi chalenge.

```python
agent = Agent(
    name="my_agent",
    llm=model,
    tools=[...],
    hooks=MyCustomHooks()  #  Yeh zaroori hai
)
```

 **Yeh manual dena zaroori hai**, warna SDK ignore kar dega



##   Hooks kab chalaye jaate hain?

| Function         | Kab chalta hai                    | SDK kya deta hai                     |
|------------------|-----------------------------------|--------------------------------------|
| `on_start`       | Jab agent start ho                | `context`, `agent`                   |
| `on_tool_start`  | Jab tool chalne wala ho           | `context`, `agent`, `tool`           |
| `on_tool_end`    | Jab tool chal gaya ho             | `context`, `agent`, `tool`, `result` |
| `on_end`         | Jab agent final jawab de          | `context`, `agent`, `output`         |
| `on_handoff`     | Jab ek agent dusre ko kaam de     | `context`, `from_agent`, `to_agent`  |
| `on_agent_start` | Jab runner agent ko start kare    | `context`, `agent`                   |
| `on_agent_end`   | Jab runner agent ko complete kare | `context`, `agent`, `output`         |




##  SDK values khud deta hai

Aap function sirf likhti ho, values aapko dene ki zarurat nahi. SDK khud deta hai:

Example:

```python
async def on_tool_end(self, context, agent, tool, result):
    print("Tool ka result:", result)
```

Aapko:
- `context` milta hai → user ki info/memory
- `agent` → wo agent jo chal raha hai
- `tool` → wo tool jo use hua
- `result` → tool ka output

Agar parameters ka order ya naam galat likha → **TypeError** aayega



##  Kya RunHooks aur AgentHooks Abstract Classes hain?

>  Nahi, ye simple base classes hain.

Unme methods hote hain jinke andar sirf `pass` hota hai — yani kuch na karo, koi error nahi.

```python
class RunHooks:
    async def on_start(self, context, agent):
        pass
```

-  Aap override karo to aapka code chalega
-  Agar override na karo to bhi koi issue nahi


##  Example:

```python
class MyHooks(AgentHooks):
    async def on_tool_end(self, context, agent, tool, result):
        print(f"Tool ka result: {result}")
```

Aur phir agent ko assign karo:

```python
agent = Agent(
    name="my_agent",
    llm=model,
    tools=[...],
    hooks=MyHooks()  #  Ye zaroor dena
)
```


##  Example:

Sochiye: Aapne ek wedding planner hire kiya hai. Jab:
- Guest aaye → planner gate open kare
- Cake aaye → lights dim kare
- Couple jaaye → fireworks chalay

Planner har event pe **automatically react karta hai**  
Waise hi **hooks bhi agent ke events pe kaam karte hain.**




