import os
from dotenv import load_dotenv, find_dotenv
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, RunConfig, function_tool



# Load .env file
load_dotenv(find_dotenv())


gemini_api_key = os.getenv("GEMINI_API_KEY")

# Set up the API provider
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Define the AI model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)

# Configure the run
config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True
)

@function_tool
def giaic_class_detail():
    return "After the Eid-ul-Azha the is going to be start at thursday 19 june"

class_Agent = Agent(
        name = "Giaic Agent",
        instructions= "Agr tumsy koi poochy k giaic ki classes kab sy start hy to bata daina.",
        tools = [giaic_class_detail]
)


Agent_response = Runner.run_sync(
        class_Agent,
        input= "giaic ki classes kabsy start hongi.",
        run_config= config
)

print(Agent_response.final_output)
