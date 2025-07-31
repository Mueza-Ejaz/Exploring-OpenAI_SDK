import os, asyncio
from dotenv import load_dotenv
from agents import (
    Agent,
    HandoffInputData,
    Runner, 
    AsyncOpenAI, 
    OpenAIChatCompletionsModel,
    RunConfig,
    handoff, 
    # enable_verbose_stdout_logging, 
)



load_dotenv()

# Enable detailed logging to show all internal steps (like tool usage, handoffs, and agent actions) in the console
# enable_verbose_stdout_logging()



#  Load Gemini API Key
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in .env file.")

#  External Client and Model Setup
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

#  Run Config
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,
)


#  Input filter function
def handoff_function(data: HandoffInputData) -> HandoffInputData:
    print("🔍 Agent level handoff filter triggered")
    return data  # Yahan aap modify bhi kar sakte hain input ko

#  Sub agent: addition ke liye
addition_agent = Agent(
    name="Addition Agent",
    instructions="Add karna ata hai.",
    model=model,
)

#  Main agent: jo handoff karega addition agent ko
math_agent = Agent(
    name="Math Agent",
    instructions="Agar input addition ka ho to addition agent ko handoff karo.",
    model=model,
    handoffs=[
        handoff(
            agent=addition_agent,
            input_filter=handoff_function  # ✅ Yahan lagta hai input filter agent-level par
        )
    ]
)

#  Run the agent
result = Runner.run_sync(
    starting_agent=math_agent,
    input="Add 4 + 4"
)
print(result.final_output)




