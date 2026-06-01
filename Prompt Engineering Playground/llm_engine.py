import os
from dotenv import load_dotenv
import groq
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

DEFAULT_SAFETY_RULES = """
You must follow these rules:
- If the user asks for illegal, harmful, or disallowed instructions, refuse briefly.
- If the user provides personal data, do not reveal or store it.
- If unsure, ask a clarifying question.
- Keep answers concise unless asked for depth.
"""

def run_prompt(system_prompt: str, user_prompt: str, model: str, temperature: float, max_tokens: int):
    # Combine user-defined system prompt with safety rules
    final_system = f"{DEFAULT_SAFETY_RULES.strip()}\n\n{system_prompt.strip()}"

    messages = [
        {"role": "system", "content": final_system},
        {"role": "user", "content": user_prompt.strip()}
    ]

    try:
        resp = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )

        return resp.choices[0].message.content
    except groq.NotFoundError as e:
        return f"Model '{model}' not found or you do not have access to it. Error: {e}"
    except Exception as e:
        return f"Request failed: {e}"


def list_models():
    """Return a list of available model ids from the Groq API.

    Tries a few common SDK entry points and falls back to sensible defaults.
    """
    try:
        # Preferred: client.models.list()
        if hasattr(client, "models") and hasattr(client.models, "list"):
            res = client.models.list()
            names = []
            if hasattr(res, "data"):
                for m in res.data:
                    if isinstance(m, dict):
                        names.append(m.get("id"))
                    else:
                        names.append(getattr(m, "id", None))
            elif isinstance(res, dict) and "data" in res:
                for m in res["data"]:
                    names.append(m.get("id"))
            elif isinstance(res, list):
                for m in res:
                    names.append(m.get("id") if isinstance(m, dict) else getattr(m, "id", None))
            return [n for n in names if n]

        # Alternate: client.list_models()
        if hasattr(client, "list_models"):
            res = client.list_models()
            if isinstance(res, dict) and "data" in res:
                return [m.get("id") for m in res["data"] if "id" in m]
            if hasattr(res, "data"):
                return [getattr(m, "id", getattr(m, "name", None)) for m in res.data]

        # Low-level request fallback
        try:
            res = client.request("GET", "/models")
            if isinstance(res, dict) and "data" in res:
                return [m.get("id") for m in res["data"] if "id" in m]
        except Exception:
            pass
    except Exception:
        pass

    # Final fallback model names
    return ["llama-3.3-70b-versatile", "gemma2-9b-it"]
