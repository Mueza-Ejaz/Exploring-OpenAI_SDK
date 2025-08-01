#  `prompt_with_handoff_instructions()`:

##  What is it?

`prompt_with_handoff_instructions()` aik helper function hai jo agent ko yeh batata hai:

> "Agar tumhare paas aisi query aaye jo tumhara kaam nahi hai, to usay kisi aur agent ko handoff (forward) kar do."


## 🛠️ How does it work?

Jab aap kisi agent ko banate hain, aap uski instructions mein yeh function lagate hain:

```python
from agents.extensions.handoff_prompt import prompt_with_handoff_instructions

billing_agent = Agent(
    name="Billing Agent",
    instructions=prompt_with_handoff_instructions("Sirf billing ke sawalat ka jawab do.")
)
```

Yeh function us message mein yeh line automatically add karta hai:

> "Agar tum yeh kaam nahi kar saktay, to isay kisi aur agent ko handoff kar do."


##  Example

```python
from agents import Agent, Runner
from agents.extensions.handoff_prompt import prompt_with_handoff_instructions

billing_agent = Agent(
    name="Billing Agent",
    instructions=prompt_with_handoff_instructions("Sirf billing ke sawalat ka jawab do.")
)

support_agent = Agent(
    name="Support Agent",
    instructions=prompt_with_handoff_instructions("Sirf support ke sawalat ka jawab do.")
)

runner = Runner(agents=[billing_agent, support_agent])

response = runner.run("Mujhe internet support chahiye.")
print(response)
```

In this case, query **"Mujhe internet support chahiye"** billing agent reject karega, aur support agent usay answer karega.

##  Summary

`prompt_with_handoff_instructions()` = Agent ki training manual 📖 + Handoff feature 
Perfect for multi-agent systems 👍




