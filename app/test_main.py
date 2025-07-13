import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("Sreda1@", False),
        ("Pass@word1", True),
        ("Pass@word1ThisisMyPassword", False),
        ("pass@word1", False),
        ("Pass@word", False),
        ("Password1", False),
        ("Pass@  word1", False),
        ("Pass*word1", False),
        ("", False)
    ],
    ids=[
        "less than 8 characters",
        "correct password",
        "too large password",
        "without uppercase letter",
        "without digits",
        "without spec character",
        "password with spaces",
        "incorrect spec character",
        "empty string"
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    result = check_password(password)

    assert result == expected_result
