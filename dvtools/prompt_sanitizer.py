"""
prompt_sanitizer.py
-------------------

Phase 3 utility.

Purpose
~~~~~~~
Given a raw user prompt, return a cleaned version that is safe for
down‑stream model consumption.  Early features:

1. Trim leading / trailing whitespace.
2. Collapse repeated spaces and newlines.
3. Reject prompts that exceed a hard length limit
   (to protect model context).

Usage
~~~~~
>>> from tools.prompt_sanitizer import sanitize_prompt
>>> clean = sanitize_prompt("  Hello   world  ")
>>> print(clean)          # -> "Hello world"

This stub will grow as we add regex filters, profanity checks, and
injection‑prevention rules.
"""

MAX_CHARS = 8_000  # absolute upper bound for any prompt


def sanitize_prompt(raw: str) -> str:
    """Return a trimmed, deduplicated prompt or raise ValueError."""
    if not isinstance(raw, str):
        raise TypeError("Prompt must be a string")

    cleaned = " ".join(raw.strip().split())

    if len(cleaned) > MAX_CHARS:
        raise ValueError(f"Prompt exceeds {MAX_CHARS} characters")

    return cleaned
