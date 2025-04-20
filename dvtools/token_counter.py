"""
token_counter.py
----------------
Utility to estimate the token count of a string.

• If the optional `tiktoken` library is available, we use it
  (more accurate for OpenAI‑style models).
• Otherwise we fall back to a simple whitespace split.

This keeps the project usable even without extra wheels.
"""

from importlib import util
from typing import Any

# lazy import to avoid hard dependency
_tiktoken_spec = util.find_spec("tiktoken")
if _tiktoken_spec:
    import tiktoken  # type: ignore[attr-defined]
    _encoding: Any = tiktoken.get_encoding("cl100k_base")  # common default
else:
    _encoding = None


def count_tokens(text: str) -> int:
    """Return the approximate token count of *text*."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if _encoding:
        return len(_encoding.encode(text))
    # fallback: rough word count + punctuation
    return len(text.strip().split())
