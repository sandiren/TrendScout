import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_suggestion(keyword: str) -> str:
    """Return an AI-generated suggestion for the keyword if API key is set."""
    if not openai.api_key:
        return "💡 GPT suggestions are currently disabled. Set OPENAI_API_KEY in your .env file."

    try:
        chat = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "Provide a short SEO keyword suggestion."},
                     {"role": "user", "content": keyword}],
            max_tokens=20,
        )
        return chat.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ OpenAI error: {e}"
