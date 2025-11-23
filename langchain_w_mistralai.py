import langwatch
from langchain_w_mistralai import ChatMistralAI
from langchain_core.runnables import RunnableConfig
import os
import asyncio

from dotenv import load_dotenv

# load local .env (for development) — safe if .env doesn't exist
load_dotenv()

langwatch.setup(api_key=os.getenv("LANGWATCH_API_KEY"),)


# Read API key from environment; helpful message if missing
api_key = os.getenv("MISTRAL_API_KEY")
model = os.getenv("MODEL_NAME", "ministral-3b-latest")

client = ChatMistralAI(
    model=model,
    api_key=api_key,
    streaming=False,
    max_tokens=50,
    temperature=0.9,
    top_p=0.9,
)
langwatch.setup()

@langwatch.trace(name="Langchain - with Mistral AI Agent")
def call_mistral_api(user_input='What is the best French cheese and explain to me?'):
    chat_response = client.invoke(
      [{"role": "system", "content": "Always give best answer in completeness around 25 words."},
        {"role": "user", "content": user_input},],
      config=RunnableConfig(
            callbacks=[langwatch.get_current_trace().get_langchain_callback()]
        ),
    )
    return chat_response.content

if __name__ == "__main__":
    prompt ="What is the best French cheese and explain to me?"
    print(call_mistral_api(prompt))