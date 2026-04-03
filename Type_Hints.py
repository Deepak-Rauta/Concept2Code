"""What are type hints in simple words?
Type hints are simply "labels" you put on your code to tell yourself, other developers, and your coding tools what kind of data should be living inside a variable or passing through a function."""

"""They are formalized syntax to indicate the expected data types of variables, arguments and return values, improving code readability and enabling static analysis"""



# Declaring Variable Types
# Variable_name: type = value
age: int = 24
is_active: bool = True
price: float = 19.99
name: str = "Alice"


"""Adding Type Hints to Functions
Arguments: Add : type after the argument name.

Return Type: Add -> type after the closing parenthesis and before the colon."""

# def function_name(arg: type) -> return_type:
def greet(user_name: str) -> str:
    return f"Hello, {user_name}"

name = greet("Deepak")
print(name)
# If a function returns nothing, you hint it with -> None.

"""Let's build a function that takes a list of names and returns a dictionary where the name is the key, and the length of the name is the value."""

# Step 1: Basic Version with Strict Hints
from typing import List, Dict

def map_name_lengths(names: List[str]) -> Dict[str, int]:
    result: Dict[str, int] = {}
    for name in names:
        result[name] = len(name)
    return result 
print(map_name_lengths(["Deepak", "Nita"]))

# Step 2: Improved Step-by-Step (Production Ready)
from typing import List, Dict

def map_name_length(names: List[str]) -> Dict[str, int]:
    """
    Takes a list of names and returns a mapping of the name to its character length.
    Skips any empty strings.
    """
    # Using dictionary comprehension for cleaner code
    # We omit hints for the internal variable because the return type already dictates it
    return {name: len(name) for name in names if name.strip() != ""}

print(map_name_length(["Deepak", "Nita", ""]))

# Task:-1 (The Bouncer)
from typing import List, Dict

def is_adult(age: int) -> bool:
    if age >= 18:
        return True
    else:
        return False
print(is_adult(10))

# Short trick
def is_adult(age: int) -> bool:
    return age >= 18

print(is_adult(10)) 
# Output: False

# Problem 2: Receipt Total
# Method:-1
def calculate_total(prices: List[float]) -> float:
    return sum(prices)
print(calculate_total([10.50, 5.00, 2.25]))

# Method:-2
from typing import List, Dict
def calculate_totals(prices: List[float]) -> float:
    total: float = 0.0  # Start with an empty total
    for price in prices:
        total += price  # Add each price to the total
    return total
print(calculate_totals([10.5, 2.5, 8.9]))
    
# Problem 3: Grade Lookup
def get_grade(students: Dict[str, int], student_name: str) -> int:
    # we use the student_name string as the key to look up the integer value
    return students[student_name]
grades = {"Alice": 95, "Bob": 80}
print(get_grade(grades, "Alice"))

"""students: Dict[str, int]
This tells anyone reading the code that the students argument must be a dictionary. Specifically, the keys must be strings (str for the names) and the values must be integers (int for the scores).

student_name: str
This ensures that the name we are searching for is passed as a string.

-> int
This guarantees that the function will output a whole number (the student's score)."""

"""💡 Interview Coach Bonus Tip: Edge Cases
In an interview, if you write the code above, the interviewer will almost certainly ask: "What happens if the student isn't in the dictionary?"

If you pass "Charlie" into the function above, Python will crash with a KeyError. To show you are a senior-level thinker, you can use the dictionary .get() method. However, because .get() returns None if the key doesn't exist, our return type hint has to change! We use Optional[int] to say "This will return an integer, OR it will return None."""

from typing import Dict, Optional
def get_grade_safe(students: Dict[str, int], student_name: str) -> Optional[int]:
    # .get() return None instead of crashing if the student is muissing
    return students.get(student_name)
print(get_grade_safe({"Alice": 95, "Bob": 80}, "Charlie"))
