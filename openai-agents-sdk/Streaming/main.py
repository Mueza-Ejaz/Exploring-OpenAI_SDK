import os
import asyncio
from dotenv import load_dotenv, find_dotenv
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, RunConfig
from openai.types.responses import ResponseTextDeltaEvent

# Load .env file
load_dotenv(find_dotenv())

# Even though you're using Gemini, this prevents fallback errors
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "dummy_key")

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)

config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True
)

async def main():
    agent = Agent(
        name="Helper Agent",
        instructions="Agar koi apsy kuch question kare to uska jawab do.",
        model=model  # don't forget this line!
    )


    result = Runner.run_streamed(agent, input="Please tell me what's the weather in Karachi.",  run_config=config)

    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)

if __name__ == "__main__":
    asyncio.run(main())
