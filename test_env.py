# -*- coding: utf-8 -*-
from dotenv import load_dotenv
import os

load_dotenv()

key = os.environ.get("GEMINI_API_KEY")

if key:
    print(f"✅ Key loaded! First 10 chars: {key[:10]}...")
else:
    print("❌ Key not found. Check your .env file.")