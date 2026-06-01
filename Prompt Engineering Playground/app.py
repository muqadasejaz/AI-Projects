import gradio as gr
from llm_engine import run_prompt, list_models
from templates import load_templates, save_template, delete_template

# Populate model dropdown from GROQ API when possible, otherwise fall back
try:
    MODEL_OPTIONS = list_models()
except Exception:
    MODEL_OPTIONS = ["llama-3.3-70b-versatile", "gemma2-9b-it"]

def refresh_templates():
    templates = load_templates()
    return gr.Dropdown(choices=list(templates.keys()), value=None)

def apply_template(template_name):
    if not template_name:
        return "", ""
    templates = load_templates()
    t = templates.get(template_name, {})
    return t.get("system", ""), t.get("user", "")

def generate(system_prompt, user_prompt, model, temperature, max_tokens):
    if not user_prompt.strip():
        return "Please enter a user prompt."
    return run_prompt(system_prompt, user_prompt, model, temperature, max_tokens)

def save_current_template(name, system_prompt, user_prompt):
    if not name.strip():
        return "Template name is required.", refresh_templates()
    save_template(name.strip(), system_prompt, user_prompt)
    return f"Saved template: {name}", refresh_templates()

def delete_selected_template(name):
    if not name:
        return "Select a template to delete.", refresh_templates()
    delete_template(name)
    return f"Deleted template: {name}", refresh_templates()

with gr.Blocks() as demo:
    gr.Markdown("# 🧪 Prompt Engineering Playground")
    gr.Markdown("Experiment with system prompts, user prompts, temperature, and templates.")

    with gr.Row():
        template_dropdown = gr.Dropdown(label="Templates", choices=list(load_templates().keys()), value=None)
        load_btn = gr.Button("Load Template")
        del_btn = gr.Button("Delete Template")

    system_prompt = gr.Textbox(label="System Prompt (Role/Instructions)", lines=6, placeholder="e.g., You are a helpful AI assistant...")
    user_prompt = gr.Textbox(label="User Prompt", lines=8, placeholder="Ask something...")

    with gr.Row():
        # default to first available model
        default_model = MODEL_OPTIONS[0] if MODEL_OPTIONS else "groq-1"
        model = gr.Dropdown(label="Model", choices=MODEL_OPTIONS, value=default_model)
        temperature = gr.Slider(label="Temperature", minimum=0.0, maximum=1.5, value=0.7, step=0.1)
        max_tokens = gr.Slider(label="Max Tokens", minimum=50, maximum=2000, value=400, step=50)

    output = gr.Textbox(label="Model Response", lines=12)

    with gr.Row():
        run_btn = gr.Button("Run Prompt ✅")
        clear_btn = gr.Button("Clear")

    gr.Markdown("## 💾 Save a Template")
    template_name = gr.Textbox(label="Template Name", placeholder="e.g., My Blog Outline Generator")
    save_btn = gr.Button("Save Template")

    status = gr.Textbox(label="Status", interactive=False)

    # Actions
    run_btn.click(generate, [system_prompt, user_prompt, model, temperature, max_tokens], output)

    clear_btn.click(lambda: ("", "", ""), None, [system_prompt, user_prompt, output])

    load_btn.click(apply_template, template_dropdown, [system_prompt, user_prompt])

    save_btn.click(save_current_template, [template_name, system_prompt, user_prompt], [status, template_dropdown])

    del_btn.click(delete_selected_template, template_dropdown, [status, template_dropdown])

demo.launch()
