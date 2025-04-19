"""
response_cleaner.py
-------------------
Phase 3 utility #2.

For now:
* Strip any leading "assistant:" / "model:" prefix
* Collapse duplicated whitespace
"""

import re

def clean_response(raw: str) -> str:
    if not isinstance(raw, str):
        raise TypeError("Response must be a string")

    # drop prefixes like "assistant:" or "model:"
    cleaned = re.sub(r"^(assistant|model)\s*:\s*", "", raw.strip(), flags=re.I)
    # collapse internal whitespace
    return " ".join(cleaned.split())
