import os
import asyncio
from pydantic import BaseModel
from dotenv import load_dotenv
from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
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



# Structured output model
class PersonalInfo(BaseModel):
    name: str
    age: int
    subject: str

# Agent creation
agent = Agent(
    name="PersonalInfo Agent",
    instructions="Extract name, age, and subject from the user's message.",
    output_type=PersonalInfo,
    model=model,
)

# Main function
async def main():
    user_input = "My name is Mueza, I am 21 years old, and I love the subject of QA automation tsting."

    result = await Runner.run(
        starting_agent=agent,
        input=user_input
    )

    # Structured Output
    print("Structured Response:\n", result.final_output)
    print("\nName:", result.final_output.name)
    print("Age:", result.final_output.age)
    print("Subject:", result.final_output.subject)



# Run the script
if __name__ == "__main__":
    asyncio.run(main())



# output:
# Structured Response:
#  name='Mueza' age=21 subject='QA automation tsting'

# Name: Mueza
# Age: 21
# Subject: QA automation tsting


