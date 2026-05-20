# -*- coding: utf-8 -*-
import ollama
import json

# ─── STEP 1: WITHOUT JSON enforcement — show the problem ─────────────────────
print("=" * 60)
print("STEP 1: WITHOUT JSON enforcement")
print("=" * 60)

bad_response = ollama.chat(
    model="phi3",
    messages=[{
        "role": "user",
        "content": "Tell me about the city of Amman."
    }]
)

print(bad_response["message"]["content"])

print("\n👆 This is the problem — unstructured prose.")
print("   Your code cannot reliably extract data from this.\n")

# ─── STEP 2: WITH JSON enforcement — the fix ─────────────────────────────────
print("=" * 60)
print("STEP 2: WITH JSON enforcement")
print("=" * 60)

good_response = ollama.chat(
    model="phi3",
    messages=[
        {
            "role": "system",
            "content": (
                "You are a JSON API. "
                "Output ONLY valid raw JSON. "
                "Do not use markdown. "
                "Do not use backticks."
            )
        },
        {
            "role": "user",
            "content": (
                "Tell me about the city of Amman in this JSON format:\n"
                "{\n"
                '  "city": "...",\n'
                '  "country": "...",\n'
                '  "population_million": 0,\n'
                '  "top_3_facts": ["...", "...", "..."]\n'
                "}"
            )
        }
    ]
)

raw = good_response["message"]["content"].strip()

raw = raw.replace("```json", "")
raw = raw.replace("```", "")

print(raw)

# ─── STEP 3: Parse and use the structured data ────────────────────────────────
print("\n" + "=" * 60)
print("STEP 3: Parsing the JSON output")
print("=" * 60)

try:
    data = json.loads(raw)

    print("✅ Parsed successfully!")

    print(f"\nCity:        {data['city']}")
    print(f"Country:     {data['country']}")
    print(f"Population:  {data['population_million']}M")

    print("\nTop 3 facts:")

    for fact in data["top_3_facts"]:
        print(f"  - {fact}")

except json.JSONDecodeError as e:
    print(f"❌ Parse failed: {e}")

    print("\nThe model added extra text or backticks around the JSON.")
    print("Fix: add this line to the system prompt:")
    print("  'Do not use markdown. Do not use backticks. Output raw JSON only.'")