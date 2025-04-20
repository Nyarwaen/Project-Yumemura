"""
Minimal LangChain call routed through OpenRouter.

Expects `secrets/.env` to contain:
    OPENROUTER_API_KEY=sk‑...

Run with:  python scripts/test_openrouter.py
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# load secrets/.env
load_dotenv(Path(__file__).parent.parent / "secrets" / ".env")

from langchain_core.messages import HumanMessage
from langchain_community.chat_models import ChatOpenAI

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise RuntimeError("OPENROUTER_API_KEY not set in secrets/.env")

# ChatOpenAI will auto‑read OPENAI_API_BASE from OpenRouter’s endpoint
llm = ChatOpenAI(
    model="deepseek/deepseek-chat-v3-0324",
    openai_api_key=api_key,
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0.2,
)

response = llm.invoke([HumanMessage(content="Hello, OpenRouter!")])
print("Assistant:", response.content)
