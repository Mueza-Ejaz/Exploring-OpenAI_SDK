import os
import asyncio
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

# Sub-agent 1: Booking Expert
booking_agent = Agent(
    name="Booking Agent",
    instructions="Help users with bookings only.",
    model=model
)

# Sub-agent 2: Refund Expert
refund_agent = Agent(
    name="Refund Agent",
    instructions="Help users with refund requests only.",
    model=model
)

# Main agent: Triage/Support Agent = Decide karta hai k kis agent ko kaam dena hai
triage_agent = Agent(
    name="Support Agent",
    instructions=(
        "You're a support agent. Talk to the user and decide whether to hand off.\n"
        "If they ask about booking or travel, hand off to Booking Agent.\n"
        "If they ask about canceling, refund, or getting money back, hand off to Refund Agent.\n"
        "Otherwise, ask them for more information."
    ),
    model=model,
    handoffs=[booking_agent, refund_agent]
)

# Async main function
async def main():
    print("=== Support Agent Handoff Test ===")
    user_input = "I want to book a flight to Korea."

    result = await Runner.run(
        starting_agent=triage_agent,
        input= user_input
    )

    print("\n=== Final Output ===")
    print(result.final_output)



# Run the main function
if __name__ == "__main__":
    asyncio.run(main())



# output:

# === Support Agent Handoff Test ===

# === Final Output ===
# Okay, I will connect you with a booking agent who can help you book your flight to Korea. Please wait a moment.




