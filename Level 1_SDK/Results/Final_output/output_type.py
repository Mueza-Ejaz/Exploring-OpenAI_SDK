import os, asyncio
from pydantic import BaseModel
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig


# Load the environment variables from the .env file
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")


# Initialize the external client for Gemini API using AsyncOpenAI
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)



# define AI model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)


# Configure the run
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)


# Translator Agent (English ➜ Urdu)
translator = Agent(
    name="Translator",
    instructions="Translate English text into Urdu.",
    model=model
)


# Define structured output model
class Intro(BaseModel):
    name: str
    hobby: str

# Create agent with output_type
intro_agent = Agent(
    name="IntroAgent",
    instructions="Return your name and hobby in JSON format with fields 'name' and 'hobby'.",
    output_type=Intro
)

#  Run the agent
result = Runner.run_sync(
    starting_agent=intro_agent,
    input="Who are you?"
)

#  Print structured output
print("Name:", result.final_output.name)
print("Hobby:", result.final_output.hobby)