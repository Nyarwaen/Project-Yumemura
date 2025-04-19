import pytest
from dvtools.prompt_sanitizer import sanitize_prompt, MAX_CHARS


def test_basic_trim():
    assert sanitize_prompt("  hello  ") == "hello"


def test_space_collapse():
    assert sanitize_prompt("hi   there") == "hi there"


def test_length_guard():
    long_text = "a" * (MAX_CHARS + 1)
    with pytest.raises(ValueError):
        sanitize_prompt(long_text)


def test_type_guard():
    with pytest.raises(TypeError):
        sanitize_prompt(42)  # not a string
