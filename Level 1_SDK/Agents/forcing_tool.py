import asyncio, os
from dotenv import load_dotenv
from agents import ( Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, ModelSettings, function_tool, set_tracing_disabled)

# Load environment variables
load_dotenv()
set_tracing_disabled(True)

# Get GEMINI API key 
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not set in .env")

# Set up the API client and model 
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",  
    openai_client=client
)



@function_tool
def calculator() -> str:
    answer = 7 * 6
    return f"7 * 6 = {answer}"


agent = Agent(
    name="CalcAgent",
    instructions="Use the calculator tool to do math. Don’t solve by yourself.",
    model=model,
    tools=[calculator],
    model_settings=ModelSettings(tool_choice="calculator"),
    tool_use_behavior="stop_on_first_tool"
)


async def main():
    result = await Runner.run(
        agent,
        input="What is 7 times 6?"
    )

    print("\n Final Answer From Agent:")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())

# output:

# Final Answer From Agent:
# 7 * 6 = 42



