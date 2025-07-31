#   `handoff_function`:

## 🔹 1. Handoff Function Kya Hai?

Jab user ka conversation **ek agent se doosre agent** ko transfer hota hai (isko **handoff** kehte hain), to system ke beech ek function
chalta hai — jiska koi bhi name ho sakta hy jaisy abhi  hum ny `handoff_function` rakha hy.

```python
def handoff_function(data: HandoffInputData) -> HandoffInputData:
    print(" Agent level handoff filter triggered")
    return data
```

### 🔸 Example:
Agar user pehle chatbot agent ke saath baat kar raha tha, aur ab AI agent ke paas bhejna hai, to handoff se pehle hum check kar sakte hain ke:
- User ne kya kaha
- Pehle kya messages thay
- Kya content modify karna chahiye ya context dena hai


## 🔹 2. Parameters & Return

###  `data: HandoffInputData`
Yeh parameter wo **saara structured data** hota hai jo handoff ke waqt pass kiya jata hai. Iske andar:
- Pehle ke messages
- Naye messages
- Metadata (jaise user ID, session ID)

###  `-> HandoffInputData`
Function end mein wahi data return karta hai — optionally tum us data ko modify bhi kar sakti ho (jaise kisi message ka content change karna, koi tag add karna, etc.)


## 🔹 4. Data ke Andar Kya Kya Hota Hai?

`HandoffInputData` ke andar kai important properties hoti hain:

| Field Name           | Explanation (Roman Urdu) |
|----------------------|--------------------------|
| `data.input_history` | Sirf wo messages jo input (user side) thay |
| `data.pre_handoff_items` | Wo messages jo handoff se pehle aaye |
| `data.new_items`     | Naye messages (jaise user ka abhi ka message) |
| `data.all_items`     | Pura chat history (input + output + system) |
| `data.metadata`      | Extra info (jaise user ID, location, agent type) |


### ✅ Example:
```python
for item in data.all_items:
    print(item.role, item.content)
```

Iska output kuch aise hoga:

```
user Hello
assistant Hi, how can I help?
user I want to transfer
```


## 🔹 5. Agar hum Data Ko Modify Karna Chahty Hy.

```python
def handoff_function(data: HandoffInputData) -> HandoffInputData:
    data.new_items[0].content = "Modified content"
    return data
```

Yahan humne user ka latest message k content ko change kar diya.


## 🔹 6. input_filter Kya Hota Hai?

Agar handoff ke waqt kisi **specific cheez ko filter** karna chahti ho (jaise sirf "user" ke messages pass karna), to input_filter mein logic likha jata hai.

```python
def handoff_function(data: HandoffInputData) -> HandoffInputData:
    user_inputs = [item for item in data.all_items if item.role == "user"]
    print(user_inputs)
    return data
```


