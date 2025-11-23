from mistralai import Mistral
import os
from dotenv import load_dotenv

# load local .env (for development) — safe if .env doesn't exist
load_dotenv()

# Read API key from environment; helpful message if missing
api_key = os.getenv("MISTRAL_API_KEY")
model = os.getenv("MODEL_NAME", "ministral-3b-latest")

if not api_key:
    raise EnvironmentError(
        "MISTRAL_API_KEY environment variable not set. Add it to a .env file or export it in your shell."
    )

client = Mistral(api_key=api_key)

def call_mistral_api(user_input='What is the best French cheese and explain to me?'):
    chat_response = client.chat.complete(
        model= model,
        messages = [
            {
                "role": "system",
                "content": "Always give best answer in completeness around 25 words.",
            },
            {
                "role": "user",
                "content": user_input,
            },
        ],
        max_tokens=50,
        temperature=0.9,
        top_p=0.9,
        n=1,
        timeout_ms=30000,
    )
    return chat_response.choices[0].message.content

print(call_mistral_api())