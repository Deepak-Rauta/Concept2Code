"""Union: Specifies that a variable can be one of multiple distinct types. Union[int, str] means "this is either an integer or a string."

Optional: Specifies that a variable is either a specific type, or None.

Callable: Specifies that a variable is a function (or a method/class) that can be invoked with (). It defines the expected input arguments and the expected return type."""

# How to use Union:-
from typing import Union
# Can hold a number like 404 or a string like "Not Found"
error_code: Union[int, str]

# How to use Optional:
# Import it from typing. Wrap the type that might be there.
from typing import Optional
# Can be a User object, or None if the user isn't logged in
# current_user: Optional[User]

# How to use Callable:
# Callable takes two arguments in its brackets: a list of input types, and the return type.
# Syntax: Callable[[ArgType1, ArgType2], ReturnType]
from typing import Callable
# A function that takes two ints and returns an int
math_operation: Callable[[int, int], int]


# Practical Code
# Example 1:- Optional (Handling Ambiguity Safety)

from typing import Optional

def find_index(items: list[str], target: str) -> Optional[int]:
    """Return the index if found, otherwise return None."""
    try:
        return items.index(target) # It tries to find the position of the target in the list
    except ValueError:
        return None

# IDE forces us tyo check for None before using the result!
result = find_index(["apple", "Banana"], "Orange")
if result is not None:
    print(f"Found at index {result + 1}")
else:
    print("Item not found.")

# Optional[int]  # = int OR None

# Example 2: Union (Accepting Multiple Types)
from typing import Union
def process_payment(amount: Union[int, str]) -> str:
    """Accepts amount as an integer and string"""
    if isinstance(amount, str):
        if not amount.isdigit():
            raise ValueError("Invalid amount string")
        amount = int(amount)

    return f"Processing ${amount}.00"

print(process_payment(50))
print(process_payment("150"))

# Example 3: Callable (Passing Functions)
from typing import Callable

def add(x: int, y: int) -> int:
    return x + y

def excecute_math(a: int, b: int, operation: Callable[[int, int], int]) -> int:
    """Takes two number and a function, then excecute the functions."""
    print("Excecuting operation...")
    return operation(a, b)

# Passing the 'add' function as an argument
total = excecute_math(10, 5, add)
print(total)


"""5. REAL-WORLD REFACTOR TASK
Scenario: We have an old script that pulls a user ID from a messy database. The ID might be a number, a string, or completely missing. We need to normalize it into an integer, or return None if it's invalid.

BEFORE (Bad Code: Confusing, no hints, prone to runtime crashes):"""
def normalize_id(raw_id):
    if raw_id is None:
        return None
    if type(raw_id) == str:
        if raw_id.isnumeric():
            return int(raw_id)
        else:
            return None
    return raw_id

# AFTER (Clean Code: Explicit, safe, self-documenting):
from typing import Union, Optional

def normalize_id(raw_id: Union[int, str, None]) -> Optional[int]:
    """Converts a raw string or int ID into an integer.
    Returns None if the ID is Missing or invalid
    """
    if raw_id is None:
        return None
    
    if isinstance(raw_id, str):
        if raw_id.isnumeric():
            return int(raw_id)
        return None   # String wasn't a number
    
    return raw_id  # It's already an int

# Mistake 1: Misusing Optional vs Union
# Wrong: data: Optional[int, str] (Optional only takes ONE type).
# Correct: data: Union[int, str] or data: Optional[Union[int, str]].

# Mistake 2: Forgetting None in Union
# If a variable can be an int, a string, or missing, Union[int, str] is a lie.
# Correct: Union[int, str, None] (or explicitly Optional[Union[int, str]]).

# Mistake 3: Incorrect Callable Syntax
# Wrong: Callable[int, str] (Missing the list brackets for arguments).
# Correct: Callable[[int], str].

# Problem:-1
from typing import Optional

def get_user_email(user_data: dict, user_id: int) -> Optional[str]:
    """fatches the user's emial by ID.
       Returns the email string if found, otherwise return None.
    """
    # The .get() method looks for the key (user_id).
    # If the key doesn't exist, it automatically returns None!
    # This perfectly matches our Optional[str] return type.

    return user_data.get(user_id)

database = {1: "deepak@test.com"}
target_id = 1

result = get_user_email(database, target_id) 

print(f"Result: {result}")
