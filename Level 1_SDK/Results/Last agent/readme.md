
# `last_agent`:

##  What is `last_agent`?

`last_agent` aik property hoti hai jo yeh batati hai ke kaunsa agent **sabse aakhri mein run hua** aur kisne **final output** diya.

Yeh un situations mein bohot useful hota hai jab aapke paas **multiple agents** hote hain jo ek doosre ko handoff karte hain.


##  Use Case: Triage Agent Handling Input

Sochiye ke aapke paas yeh agents maujood hain:

*  `HRAgent` – HR related queries
*  `LangAgent` – Grammar/language based questions
*  `TravelAgent` – Ticketing/travel related queries

In sab agents ko aap ek main agent (`TriageAgent`) ke under **tools** ke taur pe register karte ho:

```python
TriageAgent(
    tools=[
        LangAgent(),
        HRAgent(),
        TravelAgent()
    ]
)
```


##  Flow Explanation:

1. `Runner.run()` start hota hai `TriageAgent` ke saath
2. `TriageAgent` user ka input check karta hai
3. Wo input ko appropriate agent (jaise `LangAgent`) ko handoff karta hai
4. Final agent response deta hai
5. SDK `last_agent` property mein us agent ka reference store karta hai



##  Example Walkthrough

###  Step 1: First Input

```python
first_input = "Tell me what is a verb"

first_result = Runner.run_sync(
    starting_agent=TriageAgent,
    input=first_input
)

print(" Final output of first turn:", first_result.final_output)
print(" Last agent that responded:", first_result.last_agent.name)
```

**Output:**

```
 Final output of first turn: A verb is a word that shows action like "run", "eat", or "write".
 Last agent that responded: LangAgent
```


###  Step 2: Follow-up Input using `last_agent`

```python
second_input = "Give me more examples of verbs."

second_result = Runner.run_sync(
    starting_agent=first_result.last_agent,  # Using LangAgent
    input=second_input
)

print(" Second output (follow-up):", second_result.final_output)
```

**Output:**

```
 Second output (follow-up): Sure! Examples of verbs include: jump, sleep, write, talk, and read.
```


## Summary

| Step | Action                                                    |
| ---- | --------------------------------------------------------- |
| 1️⃣  | User sends: `"Tell me what is a verb?"`                   |
| 2️⃣  | `TriageAgent` analyzes and hands off to `LangAgent`       |
| 3️⃣  | `LangAgent` responds with a grammar explanation           |
| 4️⃣  | SDK stores `last_agent = LangAgent`                       |
| 5️⃣  | Follow-up goes directly to `LangAgent` using `last_agent` |



##  Tip

`last_agent` ko use kar ke aapka multi-agent system **more intelligent and smooth** ban jata hai. Aap user ka context easily carry forward kar sakte ho.


