# -*- coding: utf-8 -*-
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.environ.get("GEMINI_API_KEY")

if not API_KEY:
    print("❌ GEMINI_API_KEY not found.")
    exit()

client = genai.Client(api_key=API_KEY)

MODEL = "gemini-flash-latest"
PROMPT = "Write a one-sentence tagline for an AI bootcamp."


def test_temperature(temp: float, runs: int = 3):
    print(f"\n{'=' * 55}")
    print(f"Temperature: {temp}")
    print(f"{'=' * 55}")

    for i in range(runs):
        response = client.models.generate_content(
            model=MODEL,
            contents=PROMPT,
            config=types.GenerateContentConfig(
                temperature=temp
            )
        )

        print(f"  Run {i + 1}: {response.text.strip()}")


if __name__ == "__main__":
    print(f'Prompt: "{PROMPT}"')

    test_temperature(0.1)
    test_temperature(0.9)