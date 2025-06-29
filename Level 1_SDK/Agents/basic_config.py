# uv add openai_agents python-dotenv agents
# uv add openai_agents agents
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, ModelSettings, function_tool



load_dotenv()

gemini_api_key = "AIzaSyA4tyWB3gj7Grsd4a6fpaoSgNtyuS0KOrM"
print(gemini_api_key)


# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")


# API provider
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
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

# Tuning Parameters
settings = ModelSettings(
    temperature=0.9,
    top_p=0.85,
    max_tokens=200
)


# Write Agent
guider = Agent(
    name = 'Guider Agent',
    instructions= 
    """ Ap aik guider agent hoo, jis me ap logo ko suggestions dogy,user kuch bhi poochy apny unhy suggestions daini hy k 
    apko ye karna chaiye wo nahi etc.""",
    model_settings=settings
)

response = Runner.run_sync(
    guider,
    input = 'Mujhy face care k bare me kuch suggestions do',
    run_config = config
    )


print(response.final_output)

# Run the agent output:
# AIzaSyA4tyWB3gj7Grsd4a6fpaoSgNtyuS0KOrM
# Zaroor, main aapko face care ke liye kuch suggestions deta hun:

# **Bunyadi (Basic) Cheezain:**

# *   **Saaf Safai (Cleansing):** Apne face ko din mein kam az kam do baar zaroor dhoyen, ek baar subah
#       aur ek baar sone se pehle. Apni skin type ke hisab se gentle cleanser use karen.
# *   **Moisturize:** Har baar face dhone ke baad moisturizer lagana na bhoolen, chahe aapki skin oily hi kyun na ho.
# *   **Sunscreen:** Ye sabse important hai! Ghar se bahar nikalne se pehle SPF 30 ya usse zyada wala sunscreen zaroor
#       lagayen, chahe mausam kaisa bhi ho.       
# *   **Makeup Utarna:** Raat ko sone se pehle makeup zaroor utaren. Makeup remover wipes ya cleansing oil istemal kar sakte.


