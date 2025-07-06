#  Original_Input:

##  What is `original_input`?

Jab aap `Runner.run()` ya `Runner.run_sync()` function call karte hain, to aap jo **input** agent kobhejte hain (jaise koi question ya command), usi
input ko SDK internally `original_input` property mein save karta hai.Yeh wahi **user ka actual message** hota hai jo agent ne receive kiya
tha — bina kisi processing ke.


##  Why is `original_input` useful?

Most of the time aapko `original_input` ki zarurat nahi hoti, lekin kuch special use-cases mein yeh kaafi helpful ho sakta hai:

| Use-case     | Reason                                          |
| ------------ | ----------------------------------------------- |
| ✅ Debugging  | Dekhne ke liye ke user ne kya input diya tha    |
| ✅ Re-running | Same input future mein dobara run karne ke liye |
| ✅ Logging    | Chat ya task history record karne ke liye       |
| ✅ Analytics  | Compare karne ke liye between input and output  |



## Example :

```python
from agents import Agent, Runner

# Agent
my_agent = Agent(
    name="SimpleAgent",
    instructions="Answer short and clearly."
)

# Run
result = Runner.run_sync(
    starting_agent=my_agent,
    input="What is AI?"
)

# Output
print(" Final Output:", result.final_output)
print(" Original Input:", result.original_input)
```

### Output:

```
 Final Output: AI stands for Artificial Intelligence.
 Original Input: What is AI?
```


##  Summary:

* `original_input` = User ka jo original message tha, wohi input agent ko mila tha.
* Har run ke result mein yeh field milti hai.


```python
result.original_input
```


