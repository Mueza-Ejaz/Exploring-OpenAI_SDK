#  `to_input_list()`:

##  `to_input_list()` Kya Hai?

`to_input_list()` ek utility method hai jo `RunResult` object par call ki jati hai.

###  Maqsad:

Ye method:

* Hamara **original input**
* Aur agent ke tamam **outputs** (messages, tools, reasoning)
  ko mila kar ek **nayi input list** banata hai, jo agle run me use hoti hai. Is se multi-turn ya loop-based conversations maintain karna asaan ho jata hai.


##  Agent Run Life Cycle:

### 1.  Start Input

Hum agent ko input dete hain `Runner.run()` ya `Runner.run_sync()` se:

input = "Hello!"
result = Runner.run_sync(agent, input=input)

### 2. Agent Processing:

Agent ye kaam karta hai;

* Message generate karta hai (reply).
* Tool call karta hai (agar zarurat ho).
* Handoff ya reasoning deta hai.

Ye sab cheeze SDK internally **RunItems** ke zariye track karta hai:

| RunItem Type         | Kya Kaam Karta Hai         |
| -------------------- | -------------------------- |
| `MessageOutputItem`  | Agent ka jawab             |
| `ToolCallItem`       | Tool ko call karna         |
| `ToolCallOutputItem` | Tool ka result             |
| `HandoffCallItem`    | Handoff ki request         |
| `HandoffOutputItem`  | Handoff ka jawab           |
| `ReasoningItem`      | Agent ka sochne ka process |



### 3.  Result Tayyar Hota Hai

Jab run complete hota hai, to sab RunItems `result.new_items` me store ho jate hain.



### 4.  `to_input_list()` Call Karna

next_input = result.to_input_list()


Is method se:

* Original input liya jata hai
* Agent ke outputs extract kiye jate hain
* Sab combine karke ek clean structured list milti hai



### 5.  Naya User Input Add Karna

Hum new user message is tarah add karte hain:

next_input.append({"role": "user", "content": "Continue..."})


### 6.  Doosra Agent Run Full Context ke Sath:

Ab hum agent ko wapas run karte hain poore conversation ke sath;

Runner.run_sync(agent, input=next_input)


##  Example (Poora Code):

*First Run*
result = Runner.run_sync(agent, input="Hello!")


**Context extract karna*

next_input = result.to_input_list()

**Naya message add karna*

next_input.append({"role": "user", "content": "Continue..."})

**Second Run*

Runner.run_sync(agent, input=next_input)


## Summary:

| Concept           | Explanation                                         |
| ----------------- | --------------------------------------------------- |
| `to_input_list()` | Pehle input aur outputs ko combine karta hai        |
| Use Case          | Next run ke liye context ready karta hai            |
| Benefit           | Multi-turn chat aur looping scenarios me useful hai |



