def calculate_score(a, b):
    """Adds two numbers but caps the result at 100."""
    result = a + b
    if result > 100:
        return 100
    return result