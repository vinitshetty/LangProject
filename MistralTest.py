api_key='C0UM1RJVzGuPWVPG234T2o5Nd6fBHKUl'

import os
from mistralai import Mistral
import json
#api_key = os.environ["MISTRAL_API_KEY"]
model = "ministral-3b-latest"

client = Mistral(api_key=api_key)
'''
chat_response = client.chat.complete(
    model= model,
    messages = [
        {
            "role": "system",
            "content": "Always give best answer in less than 10 words.",
        },
        {
            "role": "user",
            "content": "What is the best French cheese and explain to me?",
        },
    ],
    max_tokens=50,
    temperature=0.7,
    top_p=0.9,
    n=1,
    timeout_ms=30000,
)
'''

for chunk in client.chat.stream(
    model=model,
    messages=[
        {"role": "system", "content": "Always give best answer in completeness around 25 words."},
        {"role": "user", "content": "What is the best French cheese and explain to me?"},
    ],
    max_tokens=50,
    temperature=0.9,
    top_p=0.9,
    n=1,
    timeout_ms=30000,
):
    print(chunk.data.choices[0].delta.content, end="", flush=True)
