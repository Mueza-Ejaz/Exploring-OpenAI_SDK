#  Streaming in Agents SDK:

## Streaming Kya Hai?

###  Basic Idea:
Aam tor par jab hum `Runner.run()` use karty hy, to agent ka **poora result ek hi baar me milta hai**.

Lekin agar hum `Runner.run_streamed()` use kary, to humhe **real-time updates** milti hain — jaise jaise agent sochta hai aur response likhta hai
jaisy koi type kar raha hoo or hamey dikh raha hoo.


###  Example:
Socho hum AI agent se keh rahy hun:  
**"HTML, CSS aur JavaScript par aik paragraph likho."**  

- `Runner.run()` me: Agent pura sochta hai aur akhir me poora jawab deta hai.
- `Runner.run_streamed()` me: humhy har sentence **live dikhai deta hai**, jaise chat me typing dikh rahi ho.


##  SDK Me Streaming Kaise Use Karte Hain?

### 🔹 Step 1: Agent ko streaming mode me run karo

```python
result = await Runner.run_streamed(agent, input="Explain recursion")
```

➡️ Ye `RunResultStreaming` object return karega.

---

### 🔹 Step 2: Live updates daikhny ke liye stream_events ka use kary

```python
async for event in result.stream_events():
    print(event)
```

➡ Is loop se humhy `StreamEvent` milte hain — har event me ek chhoti update hoti hai.


##  Explaination:

### 1. `Runner.run_streamed()`
Agent ko streaming mode me chalatay hai aur humhy `RunResultStreaming` milta hai.


### 2. `RunResultStreaming`
Ek khaas object hai jo streaming ka result rakhta hai.  
Isay samjho ek **live TV channel** jahan hum naye naye updates dekh sakty hy.


### 3. `result.stream_events()`
Ye ek async generator hai, live updates deta hai step-by-step.

```python
async for event in result.stream_events():
    print(event)
```

Hum dekh sakty hy:
- Agent kya soch raha hai
- Output ka part-by-part likhna
- Tools ka use
- Kis agent ne jawab diya


### 4. `StreamEvent`
Ye har chhoti update ko show karta hai — jaise:

- Ek sentence generate hua
- Tool use hua
- Final jawab aaya
- Ya koi error hua

Har event ke andar ye ho sakta hai:

```python
event.output        # Output ka ek tukra
event.agent_name    # Kis agent ne kaha
event.type          # Kis type ka event hai (output, thought, etc.)
```

---

## Example:

```python
result = await Runner.run_streamed(agent, "What is recursion?")

async for event in result.stream_events():
    if event.type == "agent_output":
        print("Agent said:", event.output)
```


## Summary:

| methods                | working                                      |
|------------------------|---------------------------------------------|
| `Runner.run_streamed()` | Agent ko live mode me chalata hai           |
| `RunResultStreaming`    | Streaming ka result rakhta hai              |
| `stream_events()`       | Har update step-by-step deta hai            |
| `StreamEvent`           | Har chhoti update (thought, output, etc.)   |





