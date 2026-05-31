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
    msg = gr.Textbox(placeholder="Ask me anything...")
    clear = gr.Button("Clear")

    msg.submit(respond, [msg, chatbot], [chatbot, msg])
    clear.click(lambda: [], None, chatbot)

demo.launch()