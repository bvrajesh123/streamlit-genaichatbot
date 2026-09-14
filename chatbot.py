from openai import OpenAI
from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv(".env", override=True)

# OpenAI Client
openai_client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Gemini Client
gemini_client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def openai_chatbot_response(messages):
    response = openai_client.chat.completions.create(
        model="gpt-5-mini",
        messages=messages
    )

    return response.choices[0].message.content


def gemini_chatbot_response(messages):

    conversation = ""

    for msg in messages:
        if msg["role"] == "system":
            conversation += f"System: {msg['content']}\n"
        elif msg["role"] == "user":
            conversation += f"User: {msg['content']}\n"
        elif msg["role"] == "assistant":
            conversation += f"Assistant: {msg['content']}\n"

    response = gemini_client.models.generate_content(
        model="gemini-3.6-flash",
        contents=conversation
    )

    return response.text