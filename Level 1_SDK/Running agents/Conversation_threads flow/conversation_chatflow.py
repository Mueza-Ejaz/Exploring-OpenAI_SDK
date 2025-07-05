import os, json ,asyncio
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

# Summary Agent (Summarize Urdu text)
summarizer = Agent(
    name="Summarizer",
    instructions="Summarize the user's last message in one short line.",
    model=model
)


# Conversation flow
async def simple_conversation():
    print("\n Conversation Start\n")


    #  Turn 1 — Translation
    turn1 = await Runner.run(
        starting_agent=translator,
        input="Translate this: I love learning new things."
    )


    print(" User (Turn 1): Translate this: I love learning new things.")
    print(" Translator Output:", turn1.final_output, "\n")



    #  Turn 2 — Summary using to_input_list()

    context = turn1.to_input_list()   # previous input/output yaad rakhna
    context.append({"role": "user", "content": "Now summarize it."})

    turn2 = await Runner.run(
        starting_agent=summarizer,
        input=context
    )

    print(" User (Turn 2): Now summarize it.")
    print(" Summarizer Output:", turn2.final_output)



# Run it
if __name__ == "__main__":
    asyncio.run(simple_conversation())


