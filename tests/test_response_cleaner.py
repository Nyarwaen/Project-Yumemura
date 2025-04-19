import pytest
from dvtools.response_cleaner import clean_response


def test_strip_prefix():
    assert clean_response("assistant:  Hello!") == "Hello!"
    assert clean_response("MODEL:Hi") == "Hi"


def test_collapse_spaces():
    assert clean_response("Hi    there") == "Hi there"


def test_type_guard():
    with pytest.raises(TypeError):
        clean_response(123)
