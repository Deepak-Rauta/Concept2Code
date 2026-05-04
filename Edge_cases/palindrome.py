"""The Function to test: is_palindrome(text) (Returns True if the string reads the same backward as forward, otherwise False).

Your Task:
Create a test file and use @pytest.mark.parametrize to test these scenarios:

Normal palindrome: "racecar" -> True

Normal non-palindrome: "hello" -> False

Edge case: Empty string: "" -> True (An empty string is technically a palindrome)

Edge case: Single character: "a" -> True

Edge case: Palindrome with spaces/mixed case (if your function handles it): "Race car" -> False (unless you strip and lower it)."""

# Practical Code:-
def is_palindrome(text):
    # This check if the original text is equal to the reversed text
    return text == text[::-1]
