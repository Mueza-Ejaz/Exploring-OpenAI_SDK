#  Streaming in SDK:

##  What is Streaming?

**Streaming** ka matlab hai:  
> AI ka response aapko **real-time** mein part-by-part milta hai, instead of waiting for the full response at the end.

##  Methods:

### ✅ 1. `Runner.run_streamed()`

- Is method se aap AI agent ko **streaming mode** mein run karte ho.  
- Ye return karta hai: `RunResultStreaming` object.

### ✅ 2. `RunResultStreaming.stream_events()`
- Is method se aapko milta hai ek **event stream** — yani real-time updates from AI.  
- Ye return karta hai multiple `StreamEvent` objects.


##  What is a StreamEvent?

**StreamEvent** ek real-time update hota hai — ye batata hai:
- AI kya kar raha hai?
- Kis stage pe hai?
- Kya complete hua?


##  `event.type` — Kya Hai?

> `event.type` batata hai **ye event kis nature ka hai** — yani kis type ka signal aaya hai AI se.

###  Common Values:

| `event.type`             | Matlab kya hai?                                   |
|--------------------------|----------------------------------------------------|
| `"raw_response_event"`   | AI har lafz/token bhej raha hai (typing effect)    |
| `"stream_event"`         | AI ne koi kaam complete kiya (tool/message)        |
| `"agent_updated_event"`  | AI ka role/agent change hua                        |


##  `event.item.type` — Kya Hai?

> Jab `event.type == "stream_event"` hota hai, tab `event.item` milta hai.  
> `event.item.type` batata hai **exactly kya kaam complete hua**.

###  Common Item Types:

| `event.item.type`         | Matlab |
|---------------------------|--------|
| `"message_output_item"`   | AI ne message complete kar liya |
| `"tool_call_output_item"` | Tool run ho gaya, result mil gaya |
| `"error"`                 | Koi error aayi |

---

##  Example Code

```python
async for event in result.stream_events():

    if event.type == "raw_response_event":
        print("Typing:", event.data.delta)

    elif event.type == "stream_event":
        if event.item.type == "message_output_item":
            print("Message:", event.item.output)
        elif event.item.type == "tool_call_output_item":
            print("Tool Output:", event.item.output)

    elif event.type == "agent_updated_event":
        print("Agent switched!")
```


## Kab Kya Use Karna Hai?

| Situation                             | Use This |
|---------------------------------------|----------|
| Typing effect chahiye (har lafz live) | `event.type == "raw_response_event"` |
| Message/tool result chahiye           | `event.type == "stream_event"` + `event.item.type` |
| Agent switch check karna ho           | `event.type == "agent_updated_event"` |





