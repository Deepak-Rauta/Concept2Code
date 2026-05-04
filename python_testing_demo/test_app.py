# STEP 1: IMPORTING THE TARGET
# We cannot test code if we cannot see it.
# This line tells python: "Go into the file named 'app.py
# and bring the 'calculate_score' function into this file
# so we can use it"
from app import calculate_score

# STEP 2: THE "HAPPY PATH" TEST
# We name the function starting with 'test_' so pytest knows 
# to run it. "Normal" means we are testing how the function 
# behaves under standard, expected conditions.

def test_calculate_score_normal():
    # The 'assert' keyword is the judge.
    # It evaluates the expression on its right.
    # We call our function with 10 and 20. 
    # If the function returns 30, it becomes: assert 30 == 30 (True -> Pass).
    # If it returns 25, it becomes: assert 25 == 30 (False -> Fail!).
    # Test a standard case
    assert calculate_score(10, 20) == 30

# STEP 3: THE "BOUNDARY" TEST
# Bugs almost always happen at the edges of our logic.
# Our app's rule is "max score is 100". 
# What happens if the inputs add up to exactly 100?

def test_calculate_score_at_limit():
    # Test the boundary logic (exactly 100)
    assert calculate_score(50, 50) == 100

# STEP 4: THE "EDGE CASE" (EXCEEDING LIMIT) TEST
# Now we test what happens when we break the normal rules.
# The user inputs numbers that total more than 100.

def test_calculate_score_exceeds_limit():
    # Test the 'cap' logic (result should not be 150)
    assert calculate_score(80, 70) == 100



"""Let's quickly break down exactly what this beautiful green text means:

collected 3 items: pytest scanned your folder, found test_app.py, and successfully identified your 3 separate test functions inside of it.

. . .: Each green dot represents one passing test. If you had 500 tests, you'd see 500 dots flying across the screen!

[100%]: Every single test you wrote successfully verified the logic in your app.py file."""