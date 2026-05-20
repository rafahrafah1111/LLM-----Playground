# -*- coding: utf-8 -*-
from google import genai
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
API_KEY = os.environ.get("GEMINI_API_KEY")

if not API_KEY:
    print("❌ GEMINI_API_KEY not found in .env file.")
    print("   Make sure your .env file has: GEMINI_API_KEY=your_key_here")
    exit()

# Initialize the client
client = genai.Client(api_key=API_KEY)

MODEL = "gemini-flash-latest"


def chat():
    conversation_history = []

    print(f"\n🌐 Chatbot powered by {MODEL}")
    print("Commands:  'quit' to exit  |  'reset' to clear history\n")
    print("-" * 50)

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "quit":
            print("\n👋 Goodbye!")
            break

        if user_input.lower() == "reset":
            conversation_history = []
            print("\n🧹 Conversation history cleared!")
            continue

        conversation_history.append({
            "role": "user",
            "parts": [{"text": user_input}]
        })

        response = client.models.generate_content(
            model=MODEL,
            contents=conversation_history
        )

        assistant_reply = response.text

        conversation_history.append({
            "role": "model",
            "parts": [{"text": assistant_reply}]
        })

        print(f"\n🤖 Gemini: {assistant_reply}")


if __name__ == "__main__":
    chat()