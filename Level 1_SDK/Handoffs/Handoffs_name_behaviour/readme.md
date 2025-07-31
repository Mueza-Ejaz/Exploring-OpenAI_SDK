#  Triage Agent Handoff Issue – Name vs. Instructions:

## 📌 Summary

Hum ne ek `triage_agent` banaya jo decide karta hai ke user ka sawal kis expert agent ko bhejna hai:

- `math_expert_agent` → Maths ke sawalat solve karta hai  
- `physics_expert_agent` → Physics ke concepts handle karta hai  

Yeh dono agents `triage_agent` ke andar registered hain via handoffs.

### ❗ Bug: Naam ka Ghalat Istemaal

Hum ne agents ke naam galti se ulte rakh diye:

```python
# Ghalat Configuration
math_expert_agent = Agent(
    name="Physicist",  # ❌ Yeh hona chahiye tha "Mathematician"
    instructions="You are an expert in mathematics..."
)

physics_expert_agent = Agent(
    name="Mathematician",  # ❌ Yeh hona chahiye tha "Physicist"
    instructions="You are an expert in physics..."
)
```

🔁 Ab jo sawal **physics ka tha**, woh chala gaya **math agent** ke paas, aur jo **maths ka sawal tha**, woh chala gaya **physics agent** ke paas.

Yeh baat custom hooks (`on_start` / `on_end`) se pata chali jo print kar rahe thay:

```
Math Agent is started.
Math Agent is ended.
```

##  Aisa Kyun Hua?

LLM (Language Model) jab decide karta hai ke sawal kis agent ko bhejna hai, to woh **sirf agent ka name dekhta hai**, instructions nahi.

Yani agar naam "Physicist" hai, to LLM sochta hai ke yeh physics wala agent hai — chahe uski instructions kuch bhi keh rahi hoon.

###  Sahi Configuration

```python
math_expert_agent = Agent(
    name="Mathematician",  # ✅ Ab sahi hai
    instructions="You are an expert in mathematics..."
)

physics_expert_agent = Agent(
    name="Physicist",  # ✅ Ab sahi hai
    instructions="You are an expert in physics..."
)
```

##  Summary:

> **LLM jab agent select karta hai to sirf uska `name` dekhta hai — instructions baad mein use hoti hain jab agent run karta hai.**

-  Isliye hamesha agent ka **naam aur kaam (instructions)** match hone chahiye warna handoff galat ho jata hai.


