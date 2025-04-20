from dvtools.token_counter import count_tokens


def test_basic_count():
    assert count_tokens("Hello world") >= 2


def test_type_guard():
    import pytest
    with pytest.raises(TypeError):
        count_tokens(123)
