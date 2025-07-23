#   Parallel Tool Calls:

##  `parallel_tool_calls` kya hota hai?

`parallel_tool_calls` aik feature hai jo LLMs (Language Learning Models) jaise GPT-4 ya Gemini me use hota hai. Iska kaam decide karna hota hai ke:

**"Kya multiple tools ek hi waqt me chalayen (parallel), ya aik aik karke (sequence)?"**


##   Default Behavior (jab `parallel_tool_calls` False hota hai)

By default:
- LLM sirf **ek tool per turn** chala sakta hai.
- Agar user kahe ke "weather aur currency dono batao", to:
  - Pehle **weather** wala tool chalega,
  - Uske baad **currency** wala,
  - Dono alag alag steps me.


##   Jab `parallel_tool_calls = True` hota hai

Agar aap likhein:

```python
parallel_tool_calls = True
```

To model **multiple tools ko ek hi waqt me run karega** — yani parallel execution.

### ✅ Fayde:
- **Speed**: Time kam lagta hai.
- **Efficiency**: Kam messages me zyada kaam ho jata hai.
- **Less Looping**: User ko baar baar kehna nahi padta "ab ye karo, ab wo karo".


##   Example (OpenAI SDK - GPT-4)

```python
response = client.chat.completions.create(
  model="gpt-4-1106-preview",
  tools=[weather_tool, currency_tool],
  messages=[
    {"role": "user", "content": "Karachi ka weather aur dollar ka rate batao."}
  ],
  tool_choice="auto",
  parallel_tool_calls=True  #  Dono tools aik sath chalengay
)
```


##   Gemini ke sath Masla

>   **Gemini models (jaise gemini-1.5-flash ya 2.0) `parallel_tool_calls = True` support nahi karte**

Agar aap isko use karne ki koshish karo, to error milega:

```json
Error: Parallel tool calls are not supported.
```

###   Solution:
Gemini ke liye ye likhna chahiye:
```python
parallel_tool_calls = False
```


##  Summary:

| Feature              | GPT-4 (OpenAI)     | Gemini (Google)     |
|----------------------|--------------------|----------------------|
| Parallel Tool Calls  |  Supported         |  Supported nahi     |
| Setting              | `True` ya `False`  |  Sirf `False`         |
| Error on True?       |  Nahi              |  Haan (400 error)   |



##  Real World Example:

**User ka message**:  
_"Karachi ka weather aur USD to PKR ka rate batao."_

| Setting                     | Behavior                       |
|---------------------------- |--------------------------------|
| `parallel_tool_calls=True`  | Dono tools aik sath chalengay  |
| `parallel_tool_calls=False` | Pehle ek, phir doosra chalega  |



##   Best Practices:

-   OpenAI ke GPT-4 models ke sath `parallel_tool_calls=True` use karo fast response ke liye.
-   Gemini ke sath isay mat use karo, warna error milega.




