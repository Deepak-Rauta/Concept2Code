"""MINI PRACTICE TASK
To lock this into muscle memory, write a file named test_practice.py and solve these problems:

Problem 1: Create a fixture named guest_rsvp_data that returns a dictionary representing a user: {"name": "Rahul", "attending": True, "plus_one": False}.

Problem 2: Write a test named test_guest_is_attending that uses this fixture and asserts that the guest's attending status is True.

Problem 3: Write a second test named test_guest_has_no_plus_one that uses the same fixture and asserts that plus_one is False."""


import pytest
from typing import Dict, Any

# Task:- 01
@pytest.fixture
def guest_rsvp_data() -> Dict[str, Any]:
    """Fixture providing a standard list of user queries."""

    # Returning ONE dictionary that contating all the user's data.
    return {
        "name": "Rahul",
        "attending": True,
        "plus_one": False
    }

# Task:- 02
def test_guest_is_attending(guest_rsvp_data: Dict[str, Any]) -> None:
    """Test that the guest's attending status is True."""

    # We extract the value directly from the fixture data
    is_attending = guest_rsvp_data["attending"]

    # Assert that the extracted value is exactly True
    assert is_attending is True

# Task:- 03
def test_guest_has_no_plus_one(guest_rsvp_data: Dict[str, Any]) -> None:
    """Test that the guest is not bringing a plus one."""

    # Extract the specific value from the injected dictionary
    is_plus_one = guest_rsvp_data["plus_one"]

    # Assert that the extracted value is exactly False
    assert is_plus_one is False







