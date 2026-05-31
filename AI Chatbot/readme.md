# 🤖 Project 1: AI Chatbot (LLM-Powered Assistant)

## 🎯 Project Goal

Build a working AI chatbot that:

- Accepts user input
- Uses a Large Language Model (LLM)
- Maintains conversation context
- Runs locally in a web UI
- Can be extended into a real product

### What You'll Learn

- ✅ LLM Fundamentals
- ✅ Prompt Engineering
- ✅ API Integration
- ✅ Basic Frontend Development
- ✅ End-to-End AI Application Workflow

---

# 📌 Project Overview

## What You'll Build

A simple AI Chat Assistant using:

- Python
- Groq API
- Gradio

By the end of this project, you'll have:

- ✔ A running chatbot
- ✔ Editable system prompts
- ✔ Clean code structure
- ✔ A foundation for future AI applications

---

# 🛠️ Step-by-Step Implementation

## Step 1: Setup Your Environment

### Create Project Folder

```bash
mkdir project-01-ai-chatbot
cd project-01-ai-chatbot
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```txt
groq
gradio
python-dotenv
```

---

## Step 2: Add API Key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_api_key_here
```

---

## Step 3: Create the Chatbot UI

Create `app.py`

```python
import gradio as gr
from chatbot import chat_with_ai

def respond(message, history):
    history = history or []

    reply = chat_with_ai(message, history)

    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": reply})

    return history, ""

with gr.Blocks() as demo:
    gr.Markdown("# 🤖 AI Chatbot")

    chatbot = gr.Chatbot()
    msg = gr.Textbox(
        placeholder="Ask me anything..."
    )

    clear = gr.Button("Clear")

    msg.submit(
        respond,
        [msg, chatbot],
        [chatbot, msg]
    )

    clear.click(
        lambda: [],
        None,
        chatbot
    )

demo.launch()
```

---

## Step 4: Create Chatbot Logic

Create `chatbot.py`

```python
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def chat_with_ai(message, history):
    messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant."
        }
    ]

    for item in history:
        messages.append(item)

    messages.append(
        {
            "role": "user",
            "content": message
        }
    )

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=messages
    )

    return response.choices[0].message.content
```

---

## Step 5: Run the Project

```bash
python app.py
```

---

# 🚀 Result

Your AI chatbot is now live!

Features:

- Conversational AI
- Context-aware responses
- Local web interface
- Groq-powered LLM inference
- Easy to extend with new features

---

# 📂 Project Structure

```text
project-01-ai-chatbot/
│
├── app.py
├── chatbot.py
├── .env
├── requirements.txt
└── README.md
```

---

# 🔮 Future Improvements

- Add chat history persistence
- Support multiple LLMs
- Add streaming responses
- Implement authentication
- Add document Q&A
- Integrate vector databases (RAG)
- Deploy to cloud platforms

---

## 📚 Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Backend Logic |
| Groq API | LLM Inference |
| Gradio | Web Interface |
| python-dotenv | Environment Variable Management |

---

### Project Status

✅ Completed  
🚀 Ready for Extension into Advanced AI Applications
