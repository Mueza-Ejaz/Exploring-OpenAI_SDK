import os, asyncio
from dotenv import load_dotenv
from agents import Agent, HandoffInputData, RunHooks, Runner, AsyncOpenAI, OpenAIChatCompletionsModel,RunConfig, enable_verbose_stdout_logging, function_tool, handoff


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



# ------------------- Filter Functions ------------------- #

def history_input_filter(x: HandoffInputData) -> HandoffInputData:
    print("📘 [bold yellow]History Input Filter Triggered")
    x.input_history = "What is gravity?"
    return x

def science_input_filter(x: HandoffInputData) -> HandoffInputData:
    print("🔬 [bold green]Science Input Filter Triggered")
    x.input_history = "What is 9 + 10?"
    return x

def math_input_filter(x: HandoffInputData) -> HandoffInputData:
    print("➗ [bold blue]Math Input Filter Triggered")
    x.input_history = "Who was Napoleon?"
    return x

# ------------------- Agents ------------------- #

# Step 1: First define agents without handoffs
history_agent = Agent(
    name="HistoryAgent",
    instructions="You are an expert in History. If question is about science, handoff to ScienceAgent.",
)

science_agent = Agent(
    name="ScienceAgent",
    instructions="You are a Science expert. Handoff to MathAgent if it's a math question.",
)

math_agent = Agent(
    name="MathAgent",
    instructions="You are a Math genius. If it's a history question, handoff to HistoryAgent.",
)

# Step 2: Now assign handoffs with actual Agent objects
history_agent.handoffs = [
    handoff(agent=science_agent, input_filter=history_input_filter)
]

science_agent.handoffs = [
    handoff(agent=math_agent, input_filter=science_input_filter)
]

math_agent.handoffs = [
    handoff(agent=history_agent, input_filter=math_input_filter)
]

# ------------------- Hooks ------------------- #

class MyHooks(RunHooks):
    async def on_handoff(self, context, from_agent, to_agent):
        print(f"[bold cyan]👋 {from_agent.name} handed off to {to_agent.name}")

# ------------------- Main ------------------- #

async def main():
    result = await Runner.run(
        starting_agent=history_agent,
        input="Who discovered Newton's Laws?",
        run_config=config,
        hooks=MyHooks()
    )
    print("\n🏁 [bold magenta]Final Output:", result.final_output)

if __name__ == "__main__":
    asyncio.run(main())  # ✅ Correct async execution



# output:
# 🏁 [bold magenta]Final Output: Newton's Laws of Motion were discovered by Isaac Newton.






