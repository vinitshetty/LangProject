import chainlit as cl
#import mistral as ms
import langchain_mistralai as lc
import os
import langwatch

from dotenv import load_dotenv
load_dotenv()


@cl.on_chat_start
async def start():
    await cl.Message(content="👋 Hi! I'm an AI bot. Ask me anything!").send()

@cl.on_message
async def handle_message(message: cl.Message):
    user_input = message.content

    # Stream a reply token-by-token
    msg = cl.Message(content="")  # empty placeholder message
    await msg.send()

    for token in lc.call_mistral_api(user_input):
        msg.content += token
        await msg.update()  # updates the already-sent message
