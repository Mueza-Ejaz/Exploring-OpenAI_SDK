import os
import asyncio
from dataclasses import dataclass
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

@dataclass
class UserContext():
    name: str
    mood: str


# Static Instructions Agent
static_agent = Agent[UserContext](
    name="Static Agent",
    instructions="Help the user with their problem politely.",
    model=model
)


# Dynamic Instructions Function
def dynamic_instructions(context, _agent) -> str:
    return f"User ka naam {context.context.name} hai aur wo {context.context.mood} mood mein hai. Usay usi hisaab se politely help karo."



# Dynamic Instructions Agent
dynamic_agent = Agent[UserContext](
    name="Dynamic Agent",
    instructions=dynamic_instructions,
    model=model
)



# Run both agents
async def main():
    user_context = UserContext(name="Mueza", mood="confused")
    user_input = "Can you help me with my resume?"

    print("\n Static Agent Output:")
    result_static = await Runner.run(
        starting_agent=static_agent,
        input=user_input,
        context=user_context
    )
    print(result_static.final_output)


    print("\n Dynamic Agent Output:")
    result_dynamic = await Runner.run(
        starting_agent=dynamic_agent,
        input=user_input,
        context=user_context
    )
    print(result_dynamic.final_output)



# Run the program
if __name__ == "__main__":
    asyncio.run(main())


# output:

# Static Agent Output:
# I would be happy to! To give you the best advice, I need a little more information.  Tell me about:

# *   **Your industry and target job:** What kind of job are you trying to get? What industry is it in?
# *   **Your experience level:** Are you an entry-level candidate, mid-career professional, or senior executive?
# *   **What specifically are you struggling with?** Is it the formatting, the wording, highlighting accomplishments, or something else entirely?
# *   **Do you have a current resume you can share (or parts of it)?** You can copy and paste it here (be sure to remove any personal contact information you don't want to share like phone numbers or exact addresses). Or if you prefer, you can describe the sections you currently have.

# The more information you give me, the better I can assist you!

#  Dynamic Agent Output:
# Hi Mueza, I understand you're feeling a little confused, and that's perfectly okay! I'm happy to help you with your resume. To give you the best possible assistance, could you tell me a bit more about what you're looking for help with? For example:

# *   **What kind of job are you applying for?** Knowing the industry and role will help me tailor the advice.
# *   **What are you feeling confused about?** Is it the format, the content, the wording, or something else?
# *   **Do you have a draft resume already?** If so, you can share it with me, and I can give you specific feedback.
# *   **What are your biggest concerns or questions about your resume?**

# Don't worry, take your time and explain whatever's on your mind. We'll figure it out together, step by step. I'm here to help in a patient and understanding way!



