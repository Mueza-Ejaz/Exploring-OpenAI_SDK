import os, asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, function_tool

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in .env file.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)


config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)


# Tool 1: 
@function_tool(name_override="add_google")
def add_google(a,b) -> float:
    """Adds two numbers """
    return a + b
   

# Tool 2: 
@function_tool(name_override="math_numpy")
def add_numpy(a, b) -> float:
    """Uses a multiply of two numbers."""

    result = a*b
    return result


# Tool 3: 
@function_tool(name_override="math_sphinx")
def add_sphinx(a, b) -> str:
    """Returns a subtract of two numbers as a string."""
    result = a - b
    return f"The result of subtracting {a} and {b} is {result}."




calculator = Agent(
    name="Calculator_Agent",
    instructions="""
                    You are a calculator agent that can perform basic arithmetic operations.""",
    tools=[add_google, add_numpy, add_sphinx],
)



async def main():

    input = "10 and 5 are numbers. What is the sum , subraction and multiplication of these two numbers?"

    result = await Runner.run(calculator, input, run_config=config)

    print("\n Final Output:\n")
    print(result.final_output)

asyncio.run(main())







