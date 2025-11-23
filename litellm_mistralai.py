import langwatch
from langchain_core.runnables import RunnableConfig
from litellm import completion
import os
import asyncio

from dotenv import load_dotenv

load_dotenv()

langwatch.setup(api_key=os.getenv("LANGWATCH_API_KEY"),)

api_key = os.getenv("MISTRAL_API_KEY")
model = os.getenv("MODEL_NAME", "ministral-3b-latest")
provider = os.getenv("LLM_PROVIDER", "mistral")

@langwatch.trace(name="LiteLLM - with Mistral AI Agent")
def call_mistral_api(user_input='What is the best French cheese and explain to me?'):
    if not api_key:
        raise EnvironmentError(
            "MISTRAL_API_KEY environment variable not set. Add it to a .env file or export it in your shell."
        )
    response = completion(
        model=provider + "/" + model,
        api_key=api_key,
        messages=[
            {"role": "system", "content": "Always give best answer in completeness around 25 words."},
            {"role": "user", "content": user_input},
        ],
        max_tokens=100,
    )
    return str(response.choices[0].message.content)

if __name__ == "__main__":
    prompt ="What is the best French cheese and explain to me?"
    print(call_mistral_api(prompt))