#  `raw_responses` 

##  What is `raw_responses`?

`raw_responses` ek special list hoti hai jo har agent run ke baad SDK ke result object me hoti hai. Yeh list model (GPT ya Gemini) se
aane wale **asli/original responses** ko store karti hai — bina kisi polish ya changes ke Yani jo LLM ne backend pe 
generate kiya, wo original JSON/raw message yahan milta hai.



## Explanation

###  Step 1: User Input

Aap koi input bhejte ho agent ko, jaise:

```python
input = "Summarize: The cat is sleeping under the table."
```

###  Step 2: Agent → LLM Call

Agent yeh input LLM ko bhejta hai.
LLM return karta hai ek raw message, jo kuch aisa ho sakta hai:

```json
{
  "message": "The cat is under the table.",
  "finish_reason": "stop",
  "usage": {
    "prompt_tokens": 12,
    "completion_tokens": 7,
    "total_tokens": 19
  }
}
```

###  Step 3: SDK Parsing

SDK is raw response ko:

* Internally parse karta hai
* Final output mein use karta hai
* Lekin asli response ko bhi preserve karta hai

###  Step 4: Store in `raw_responses`

Original ModelResponse objects store ho jaate hain result.raw\_responses mein:

```python
for response in result.raw_responses:
    print(response)
```

Output ho sakta hai:

```
ModelResponse(message='The cat is under the table.', finish_reason='stop', tokens=19, ...)
```


##  Why Use `raw_responses`?

| Feature      | Explanation                                                               |
| ------------ | ------------------------------------------------------------------------- |
| ✅ Debugging  | Agar output galat lag raha ho, yahan se model ka asli jawab dekh sakte ho |
| ✅ History    | Har turn ka original LLM response save hota hai                           |
| ✅ Tool Calls | Agar koi plugin/tool call hua ho, uska structure bhi yahan milega         |



## Code Example

```python
result = Runner.run_sync(agent=my_agent, input="Define AI")

print("Final Output:", result.final_output)

print("--- Raw Responses ---")
for raw in result.raw_responses:
    print(raw)
```

### Output:

```
Final Output: AI stands for Artificial Intelligence...
--- Raw Responses ---
ModelResponse(message='AI stands for...', tokens=22, finish_reason='stop')
```


##  Summary:

* Jab agent model se baat karta hai, to original reply `raw_responses` mein save hota hai.
* Aap ise dekh ke model ki asli soch aur token usage jaise data samajh sakte ho.
* Perfect for debugging, analysis aur full traceability.
