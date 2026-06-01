import json
import os

TEMPLATE_FILE = "prompt_templates.json"

DEFAULT_TEMPLATES = {
    "Email Polisher": {
        "system": "You are an expert executive assistant. Rewrite emails to be clear, concise, and professional.",
        "user": "Rewrite this email:\n\n{{text}}"
    },
    "Bullet Summarizer": {
        "system": "You summarize content into crisp bullet points.",
        "user": "Summarize the following into 5 bullets:\n\n{{text}}"
    },
    "Tutor Mode": {
        "system": "You are a patient tutor. Explain concepts step-by-step with simple examples.",
        "user": "Explain this topic:\n\n{{text}}"
    }
}

def ensure_templates_file():
    if not os.path.exists(TEMPLATE_FILE):
        with open(TEMPLATE_FILE, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_TEMPLATES, f, indent=2)

def load_templates():
    ensure_templates_file()
    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_template(name: str, system: str, user: str):
    templates = load_templates()
    templates[name] = {"system": system, "user": user}
    with open(TEMPLATE_FILE, "w", encoding="utf-8") as f:
        json.dump(templates, f, indent=2)

def delete_template(name: str):
    templates = load_templates()
    if name in templates:
        del templates[name]
    with open(TEMPLATE_FILE, "w", encoding="utf-8") as f:
        json.dump(templates, f, indent=2)
