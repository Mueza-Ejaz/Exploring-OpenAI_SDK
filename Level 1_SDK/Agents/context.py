import os
import asyncio
from dataclasses import dataclass
from dotenv import load_dotenv
from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    RunContextWrapper,
    function_tool,
    set_tracing_disabled
)

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

#  Define Context Dataclass
@dataclass
class StudentContext:
    name: str
    subject: str

#  Tool using Context
@function_tool
async def study_advice(ctx: RunContextWrapper[StudentContext]) -> str:
    user = ctx.context
    return f"Hello {user.name}! Since you're studying {user.subject}, here's a useful study tip for you: Stay consistent and practice regularly."

# Create the Agent
agent = Agent[StudentContext](
    name="Study Advisor",
    tools=[study_advice],
    model=model,
)

# Main function to run the agent
async def main():
    context = StudentContext(
        name="Mueza",
        subject="Math"
    )

    result = await Runner.run(
        starting_agent=agent,
        input="Please give me advice",
        context=context
    )

    print("Agent Response:\n", result.final_output)

# Run the script
if __name__ == "__main__":
    asyncio.run(main())


# output:
# Agent Response:
# Hello Mueza! Since you're studying Math, here's a useful study tip for you: Stay consistent and practice regularly.


