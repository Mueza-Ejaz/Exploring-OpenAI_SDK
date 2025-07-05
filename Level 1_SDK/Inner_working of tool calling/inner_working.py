import os, json ,asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, function_tool


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

#  1. Weather Check Tool:
# # Prompt 1: What's the weather going to be like in Dubai tomorrow afternoon?

# @function_tool
# def get_weather(location: str, datetime: str) -> str:
#     """
#     Yeh function hamey batata hy ke kisi specific jaga par kisi specific waqt ya din ka mausam kiya hoga.

#     Args:
#         location (str): Us jaga ka naam jahan ka mausam maloom karna hai (e.g., "Dubai/ Karachi").
#         datetime (str): Waqt ya din jiska mausam maloom karna hai (e.g., "tomorrow").

        
#     Returns:
#         str: Mausam ka chhota aur asaan sa khulasa.
#     """

#     return f"The weather in {location} on {datetime} is expected to be sunny with mild temperatures."       

#------------------------------------------------------------------------------------------------------------------------------//


# # Prompt 2: Find me some good Chinese restaurants near downtown that are open right now.

# @function_tool
# def find_restaurants(cuisine: str, location: str, open_now: bool) -> str:
#     """
#     Ye function kisi area me specific cuisine ke ache restaurants find karta hai.

#     Args:
#         cuisine (str): Food type (e.g., "Chinese").
#         location (str): Area ya city (e.g., "downtown").
#         open_now (bool): Kya sirf open restaurants chahiye? True ya False.

#     Returns:
#         str: Restaurants ki list jo match karti ho.
#     """
#     return f"Here are some good {cuisine} restaurants near {location} that are currently {'open' if open_now else 'closed'}."

#------------------------------------------------------------------------------------------------------------------------------//


# # Prompt 3: Send an email to Sarah about the project deadline being moved to next Wednesday.

# @function_tool
# def send_email(recipient_name: str, message_topic: str, message_detail: str) -> str:
#     """
#     Ye function kisi shakhs ko ek informative email bhejta hai.

#     Args:
#         recipient_name (str): Jis shakhs ko email bhejni hai (e.g., "Sarah").
#         message_topic (str): Kis topic ke bare me email hai (e.g., "project deadline").
#         message_detail (str): Email ka asal paighaam ya detail (e.g., "The project deadline has been moved to next Wednesday").

#     Returns:
#         str: Confirmation k, email bhej di gayi.
#     """
#     return f"Email sent to {recipient_name} regarding '{message_topic}'.\nMessage: {message_detail}"

#------------------------------------------------------------------------------------------------------------------------------//


# # Prompt 4: Schedule a meeting with the marketing team for this Friday at 2 PM about the new campaign.

# @function_tool
# def schedule_meeting(team: str, datetime: str, topic: str) -> str:
#     """
#     Ye function kisi team ke sath ek meeting schedule karta hai.

#     Args:
#         team (str): Team ya department (e.g., "marketing team").
#         datetime (str): Date and time (e.g., "Friday at 2 PM").
#         topic (str): Meeting kis topic par hai.

#     Returns:
#         str: Confirmation message.
#     """
#     return f"Meeting scheduled with the {team} on {datetime} regarding '{topic}'."

#------------------------------------------------------------------------------------------------------------------------------//

# Prompt 5: I want to buy a wireless Bluetooth headphones under $100 with good reviews.

@function_tool
def find_products(product_type: str, max_price: float, min_rating: float) -> str:
    """
    Ye function online products dhoondta hai jo price aur rating criteria match karte hoon.

    Args:
        product_type (str): Jo item chahiye (e.g., "wireless Bluetooth headphones").
        max_price (float): Max price budget (e.g., 100).
        min_rating (float): Minimum rating required (e.g., 4.0).

    Returns:
        str: List of matching products.
    """
    return f"Found some {product_type} under ${max_price} with rating above {min_rating}."



# ----- Main Function -----
async def main():
    agent = Agent(
        name="Product_finder Agent",
        instructions="You are a helpful agent that assists users in finding products based on their requirements.",
        model=model,
        tools=[find_products]
    )


    input = "I want to buy a wireless Bluetooth headphones under $100 with good reviews."
    result = await Runner.run(agent, input, run_config=config)


    print(" Final Output:")

    print("\n Tool Parameters JSON Schema:\n")
    print(json.dumps(agent.tools[0].params_json_schema, indent=4, ensure_ascii=False))

    print("\n Agent Response:\n")
    print(result.final_output)


# Run the main function
if __name__ == "__main__":
    asyncio.run(main())




