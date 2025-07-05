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


#  No output_type here
simple_agent = Agent(
    name="PlainAgent",
    instructions="Write a short joke in one line.",
    output_type=None   # No output type specified

)

# Running the agent
result = Runner.run_sync(
    starting_agent=simple_agent,
    input="Tell me a joke"
)

print("Without output_type:", result.final_output)