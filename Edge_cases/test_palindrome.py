import pytest
from palindrome import is_palindrome

# My parameters are just the input string and the expected boolean (True/False)
@pytest.mark.parametrize("text, expected", [
    # Normal Cases
    ("racecar", True),  # Reads the same backwards
    ("hello", False),   # Does NOT read the same backwrads

    # Edge Cases
    ("", True),   # An empty string technically a palindrome
    ("a", True),  # A single letter is technically a palindrome
])

def test_is_palindrome_scenarios(text, expected):
    # 1. We pass the text into our functions
    result = is_palindrome(text)

    # 2. We assert that the result matches what we expected
    assert result == expected