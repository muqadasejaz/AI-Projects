# 🧪 Project 02: Prompt Engineering Playground

## 🎯 Project Goal

Build a Prompt Engineering Playground web application that allows users to:

* Enter a System Prompt (role/instructions)
* Enter a User Prompt
* Adjust Temperature and Max Tokens
* Choose a Model
* Save and Reuse Prompt Templates
* View AI Responses Instantly in a Clean UI

### What You'll Learn

* ✅ Prompt Engineering Fundamentals
* ✅ Controlling Model Behavior (System vs User Prompts)
* ✅ Sampling Controls (Temperature)
* ✅ Safe Prompting Patterns
* ✅ Building Reusable AI Tools

---

# 📖 Project Overview

## What You'll Build

A Prompt Engineering Playground using:

* Python
* Groq API
* Gradio
* python-dotenv

By the end of this project, you'll have:

* ✔ A Working Prompt Lab UI
* ✔ A Template Library (JSON-Based)
* ✔ A Reusable Safe Prompt Wrapper
* ✔ A Foundation for Advanced LLM Applications

---

# 🛠️ Step-by-Step Implementation

## Step 1: Setup Your Environment

### Create Project Folder

```bash
mkdir prompt-playground
cd prompt-playground
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

### Install Dependencies

Using pip:

```bash
pip install groq gradio python-dotenv
```

Or using a requirements file:

```bash
pip install -r requirements.txt
```

Example `requirements.txt`

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

## Step 3: Create the Prompt Engine (LLM Logic)

Create a file named:

```text
llm_engine.py
```

Add the Prompt Engine code provided in the project guide.

### Why This Matters

* The System Prompt defines the model's role and behavior.
* Safety rules help prevent unsafe or inappropriate outputs.
* Temperature controls creativity and randomness.
* Max Tokens controls response length.
* Model selection allows experimentation across different LLMs.

---

## Step 4: Add Template Storage (Save & Load Prompts)

Create:

```text
templates.py
```

Add the Template Storage code provided in the project guide.

### Why This Matters

Prompt engineering is an iterative process.

Templates allow users to:

* Save successful prompts
* Reuse proven prompt patterns
* Build a personal prompt library
* Increase productivity when working with LLMs

---

## Step 5: Build the Web Interface

Create:

```text
app.py
```

Add the Gradio UI code provided in the project guide.

### Features Included

* Prompt Template Library
* Save Templates
* Delete Templates
* Load Existing Templates
* Model Selection
* Temperature Control
* Max Token Control
* Instant Response Generation
* Clean Interactive Interface

---

## Step 6: Run the Project

```bash
python app.py
```

Open the Gradio URL shown in the terminal.

Your Prompt Engineering Playground is now running locally.

---

# 🧪 Testing Ideas

## 1. Role Shift Test

### System Prompt

```text
You are a strict reviewer. Be blunt.
```

### User Prompt

```text
Review this product idea: AI study planner.
```

Observe how the model changes its personality and response style.

---

## 2. Temperature Experiment

Run the same prompt using:

### Temperature = 0.0

* Highly deterministic
* Consistent responses

### Temperature = 0.7

* Balanced responses
* Good for most use cases

### Temperature = 1.3

* Creative and diverse outputs
* Useful for brainstorming

---

## 3. Structured Output Test

### System Prompt

```text
Return valid JSON only.
```

### User Prompt

```text
Extract tasks from this text:
```

Observe how prompt instructions influence output formatting.

---

# 📂 Project Structure

```text
prompt-playground/
│
├── app.py
├── llm_engine.py
├── templates.py
├── prompt_templates.json
├── .env
├── requirements.txt
└── README.md
```

---

# 🚀 Features

* Dynamic Model Selection
* System Prompt Control
* User Prompt Control
* Temperature Adjustment
* Max Token Control
* Prompt Templates
* Save & Load Functionality
* Built-In Safety Wrapper
* Local Web Interface
* Reusable Prompt Engineering Framework

---

# 📚 Technologies Used

| Technology    | Purpose               |
| ------------- | --------------------- |
| Python        | Application Logic     |
| Groq API      | LLM Inference         |
| Gradio        | Web Interface         |
| python-dotenv | Environment Variables |
| JSON          | Template Storage      |

---


## ✅ Project Status

Completed and Ready for Extension

This project serves as a practical foundation for advanced AI applications, agents, copilots, and workflow automation systems.
