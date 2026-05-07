"""CORE THEORY
What is a pytest fixture?
A fixture is a function that provides a fixed baseline (like data or system state) upon which tests can reliably execute.

The @pytest.fixture Decorator
Just like the decorators used to wrap logging or validation logic around a function, @pytest.fixture wraps a standard Python function and registers it with pytest's internal system. It tells pytest: "Hey, this function doesn't run a test; it provides data or state for tests."

How It Provides Reusable Data & Automation
Instead of writing data = load_data() inside every single test, you write it once in a fixture. Pytest automatically handles executing the setup before your test runs, passing the result into your test, and running any teardown code after the test finishes.

Scope Basics
By default, fixtures have a function-level scope. This means the setup and teardown logic runs fresh for every single test function that uses it, guaranteeing zero cross-contamination between tests."""

# -> List[Dict[str, str]]: - type hint for the return value.
# Which means A List contating dictionry objects. where keys are string(str) and values are strings (str)

import pytest
from typing import List, Dict

# 1. Create the fixture
@pytest.fixture
def mock_user_queries() -> List[Dict[str, str]]:
    """Fixture providing a standard list of user queries."""
    # When a test requests this fixture, it will execute this code 
    # and return this exact list of dictionaries.
    return [
        {"query": "book ticket"},
        {"query": "cancel reservation"},
        {"query": "check vanue location"},
        {"query": "RSVP yes"},
        {"query": "talk to human agent"}
    ]

# Create the test function
# Pytest looks at the arguments of this test function. 
# It sees 'mock_user_queries'. It says, "I have a fixture with that exact name!"
def test_query_count(mock_user_queries: List[Dict[str, str]]) -> None:
    """Test that the data source always provide exactly 5 queries."""

    # Pytest runs the fixture in the background, grabs the returned list, 
    # and injects it right here. 'mock_user_queries' is now the actual list of data

    # The fixture data is injected autometically
    query_count = len(mock_user_queries)

    # 3. Assert the result
    # If it is 5, the test PASSES. If it is 4 or 6, the test FAILS.
    assert query_count == 5

# Pytest sees the same argument name again. 
# It runs the fixture a SECOND time, creating a brand new, fresh list for this test.
def test_specific_query_exists(mock_user_queries: List[Dict[str, str]]) -> None:
    """Test that a specific booking intent exists in the dataset."""

    # We can reuse the exact same fixture in a different test!
    # List comprehension: We loop through the injected list of dictionaries
    # and extract just the string values associated with the "query" key.
    # Result: ['book ticket', 'cancel reservation', ...]
    queries = [q["query"] for q in mock_user_queries]

    
    # We verify that "book ticket" is one of those extracted strings.
    assert "book ticket" in queries






























































































































































    