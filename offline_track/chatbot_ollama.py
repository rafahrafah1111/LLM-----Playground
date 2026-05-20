# -*- coding: utf-8 -*-
import ollama

MODEL_NAME = "phi3"

def chat():
    # This list IS our context window.
    # Every message we add here gets sent to the model on every call.
    conversation_history = []

    print(f"\n🤖 Chatbot powered by {MODEL_NAME}")
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
            "content": user_input
        })

        response = ollama.chat(
            model=MODEL_NAME,
            messages=conversation_history
        )

        assistant_reply = response["message"]["content"]

        conversation_history.append({
            "role": "assistant",
            "content": assistant_reply
        })

        print(f"\n🤖 Bot: {assistant_reply}")


if __name__ == "__main__":
    chat()