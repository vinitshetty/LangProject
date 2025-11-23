import chainlit as cl
import mistral as ms
import langchain_w_mistralai as lc
import langchain_litellm_mistralai as ll
import litellm_mistralai as lt
import os
import langwatch

from dotenv import load_dotenv
load_dotenv()


@cl.on_chat_start
async def start():
    await cl.Message(content="👋 Hi! I'm an AI bot integrating MistralAI with LangWatch for Monitoring and Evals. \n I have 4 Modes of integrating MistralAI with LangWatch and your front-end App: 1. Directly Call Mistral APIs. \n 2. Use LiteLLM for agnostic integration with MistralAI \n 3. Use LangChain without LiteLLM \n 4. LangChain with LiteLLM").send()
    
@cl.on_message
async def handle_message(message: cl.Message):
    user_input = message.content

    # Stream a reply token-by-token
    msg = cl.Message(content="")  # empty placeholder message
    await msg.send()

    #change call_mistral_api option from lc. to ms. or ll or lt.
    
    for token in lt.call_mistral_api(user_input):
        msg.content += token
        await msg.update()  # updates the already-sent message
