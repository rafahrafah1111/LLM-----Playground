# LLM Playground

A hands-on AI engineering playground built during JOSA AI Bootcamp 2026.

This project explores the fundamentals of working with Large Language Models (LLMs) through practical experiments using both local and cloud-based models.

---

## Overview

The project compares different AI model workflows and introduces core AI engineering concepts including:

* Local LLMs with Ollama
* Cloud LLMs with Gemini API
* Context windows & conversational memory
* Temperature & randomness testing
* Prompt engineering
* Grounding techniques
* Structured JSON outputs
* Persona-based prompting

---

## Tech Stack

* Python
* Ollama
* Gemini API
* Git & GitHub

---

## Project Structure

```bash
week1-ai-bootcamp/
│
├── offline_track/
│   ├── chatbot_ollama.py
│   ├── temperature_test.py
│   └── temp_test2.py
│
├── online_track/
│   ├── chatbot_gemini.py
│   └── temperature_gemini.py
│
├── lab_challenges/
│   ├── challenge_1_json.py
│   ├── challenge_2_grounding.py
│   └── challenge_3_persona.py
│
├── test_env.py
├── .gitignore
└── README.md
```

---

## Features

### Offline LLM Experiments

Run open-source language models locally using Ollama.

### Gemini API Integration

Interact with cloud-hosted LLMs through Google's Gemini API.

### Temperature Testing

Explore how model creativity changes with different temperature values.

### Structured Outputs

Generate clean JSON responses for reliable downstream processing.

### Prompt Engineering

Experiment with:

* Personas
* Constraints
* Grounding
* Response formatting

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/rafahrafah1111/week1-ai-bootcamp.git
cd week1-ai-bootcamp
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Ollama Setup (Offline Models)

Install Ollama:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Pull a model:

```bash
ollama pull phi3
```

Run the chatbot:

```bash
python offline_track/chatbot_ollama.py
```

---

## Gemini API Setup

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Run the Gemini chatbot:

```bash
python online_track/chatbot_gemini.py
```

---

## Learning Goals

This project was built to understand:

* How LLMs manage context
* Differences between local and cloud inference
* Prompt engineering fundamentals
* AI system behavior and limitations
* Practical AI engineering workflows

---

## Future Improvements

* Add RAG pipeline
* Add vector database integration
* Add tool-calling agents
* Add memory systems
* Build a simple frontend UI

---

## Author

Built by Rafah Alnabulsy during JOSA AI Bootcamp 2026.
