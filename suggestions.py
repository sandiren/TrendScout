import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env
#load_dotenv()
#openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_suggestion(keyword):
    return "💡 GPT suggestions are currently disabled. Add OpenAI integration to enable."