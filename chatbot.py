import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise RuntimeError(
        "GROQ_API_KEY not found. Add it to .env or set it in the environment before running app.py."
    )

client = Groq(api_key=groq_api_key)

def chat_with_ai(user_input, history):
    messages = [
        {"role": "system", "content": "You are a helpful AI assistant."}
    ]

    if history:
        messages.extend(history)

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.7
    )

    return response.choices[0].message.content