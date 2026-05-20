# -*- coding: utf-8 -*-
import ollama

MODEL_NAME = "phi3"
PROMPT = "Write a one-sentence tagline for an AI bootcamp."

def test_temperature(temp: float, runs: int = 3):
    print(f"\n{'=' * 55}")
    print(f"Temperature: {temp}")
    print(f"{'=' * 55}")
    for i in range(runs):
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": PROMPT}],
            options={"temperature": temp}
        )
        print(f"  Run {i + 1}: {response['message']['content'].strip()}")

if __name__ == "__main__":
    print(f'Prompt: "{PROMPT}"')
    print("\nObserve: at temp=0.1 outputs are nearly identical.")
    print("         at temp=0.9 outputs diverge significantly.\n")

    test_temperature(0.1)
    test_temperature(0.9)

    print("\n\nDiscussion questions:")
    print("  - For a banking chatbot, which temperature would you use?")
    print("  - For a creative writing assistant, which would you use?")
    print("  - What happens if you set temperature=0.0 exactly?")