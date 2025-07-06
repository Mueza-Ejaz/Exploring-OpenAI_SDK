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


## Conclusion:

- Jab agent kisi input par kaam karta hai, wo internally multiple steps perform karta hai — jaise message banana, tool call karna, reasoning apply karna, etc.

- Har step ka record SDK RunItems ke zariye maintain karta hai — ye ek internal list hoti hai jo har action ko object ki form me save karti hai (jaise MessageOutputItem, ToolCallItem, etc.).

- Jab agent ka run complete ho jata hai, to ye sari RunItems list RunResult object ke andar new_items ke through milti hai.

- Agar aap next turn me agent ko run karna chahte ho (multi-turn ya loop logic) to aapko pehle run ka pura context dena hota hai.

- Ye kaam result.to_input_list() karta hai:

- Ye original input + generated outputs ko combine karta hai

- Ek structured input list banata hai

- Jise agle run me use kiya ja sakta hai

- Is list me aap naya user message bhi append() kar sakte ho, taake agent context samajh kar response de.

- Yani, to_input_list() is the bridge jo agent ke pehle run aur agle run ke beech context maintain karta hai — bina kisi manual duplication ke.


## Imortant point:

result.new_items ek list hoti hai jo agent ke run ke dauraan kiye gaye tamam steps ka record hoti hai. Isme har step ek specific object ke form me save hota hai, jaise MessageOutputItem (agent ka reply), ToolCallItem (tool call), ToolCallOutputItem (tool ka result), aur ReasoningItem (agent ka sochne ka process). Ye list humein yeh samajhne mein madad karti hai ke agent ne input ke response mein kaun kaun se actions liye. Is list ko hum inspect kar sakte hain, filter kar sakte hain, aur to_input_list() ke zariye agle agent run ke liye context bhi ready kar sakte hain.




