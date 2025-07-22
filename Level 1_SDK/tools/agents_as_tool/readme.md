#  Agent Tools:

`.as_tool()` ka kya role hota hai jab hum ek agent ko tool banana chahte hain — aur yeh kyu zaroori hai.


##  Agent kya hota hai?

Agent aik smart assistant hota hai jisko hum specific kaam ke liye instructions dete hain. Jaise:

```python
english_agent = Agent(
    name="English Linguistic",
    instructions="You are expert in English language",
    model=model
)
```

Yeh `english_agent` English language ka expert hai. **Lekin yeh abhi tak sirf agent hai, tool nahi bana.**


##  Kya hum agent ko direct tool bana kar use kar sakte hain?

```python
tools = [english_agent]  #  Galat tareeqa
```

**Nahi!** Aise use karne se system ko yeh samajh nahi aata ke:
- Tool ka naam kya hai?
- Iska kaam kya hai?
- Isay kis tarah call kiya jaye?



## ✅ Sahi tareeqa: `.as_tool()` ka use karo

Jab agent ko tool banana ho, to yeh tareeqa sahi hai:

```python
tools = [
    english_agent.as_tool(
        tool_name="translate_to_english",
        tool_description="Translate the user's message to English"
    )
]
```

Is tarah system samajh jata hai ke yeh ab ek **tool** hai jo kisi kaam ke liye banaya gaya hai.


##  `.as_tool()` karta kya hai?

`.as_tool()` agent ko ek **callable tool** bana deta hai:
- Ek naam assign karta hai
- Description deta hai
- Isay doosray agent (jaise orchestrator) ke zariye call karna possible banata hai


##  Orchestrator Agent kya hota hai?

Orchestrator agent woh hota hai jo **baaki tools ya agents ko manage** karta hai.  
Woh khud kaam nahi karta — bas dekhta hai ke kaunsa tool kis waqt use karna hai.

Example:

```python
orchestrator_agent = Agent(
    name="orchestrator_agent",
    instructions="You are a translation agent. Use tools to translate.",
    tools=[
        english_agent.as_tool(
            tool_name="translate_to_english",
            tool_description="Translate to English"
        ),
        urdu_agent.as_tool(
            tool_name="translate_to_urdu",
            tool_description="Translate to Urdu"
        )
    ],
    model=model
)
```

Yahan orchestrator agent sirf tools ko call kar raha hai — khud translation nahi kar raha.


##  Aakhri baat

Jab bhi kisi agent ko tools ke andar use karna ho, hamesha `.as_tool()` use karo.  
Yeh SDK ko help karta hai agent ko sahi tareeke se samajhne aur use karne mein.



