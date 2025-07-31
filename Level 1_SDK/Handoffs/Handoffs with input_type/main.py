import os, asyncio
from dotenv import load_dotenv
from pydantic import BaseModel
from agents import (
    Agent,
    RunContextWrapper,
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


# ✅ Step 1: Define input type
class MyInput(BaseModel):
    name: str

# ✅ Step 2: Agent jo kaam karega jab handoff hoga
my_agent = Agent(
    name="GreetingAgent",
    instructions="Say hello using the user's name.",
    handoff_description="Greets the user."
)

# ✅ Step 3: Handoff function (input receive karega)
def handle(ctx: RunContextWrapper, input: MyInput):
    print(f"Hello, {input.name}! 👋")

# ✅ Step 4: Handoff create karo (sirf class name dena hai, instance nahi)
my_handoff = handoff(
    agent=my_agent,
    on_handoff=handle,
    input_type=MyInput
)

# ✅ Step 5: Triage agent jo handoff karega
main_agent = Agent(
    name="MainAgent",
    instructions="If someone says hello, hand off to GreetingAgent.",
    handoffs=[my_handoff]
)

# ✅ Step 6: Run the agent
async def run():
    await Runner.run(
        starting_agent=main_agent,
        input="Hello, my name is Mueza.",
        run_config=config
    )

asyncio.run(run())


# output:
# Hello, Mueza! 👋



