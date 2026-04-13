"""__len__(self): A special method that defines what happens when you pass your object to Python's built-in len() function. It must return an integer.

__getitem__(self, index): A special method that defines what happens when you use square brackets [] to access an item. It must return the item at that index (or raise an error).
"""

"""Under the Hood:When you write Python code, the interpreter translates your clean syntax into method calls:
len(obj) ---> translates to ---> obj.__len__()
obj[index] ---> translates to ---> obj.__getitem__(index)"""


# 3. STEP-BY-STEP BREAKDOWN
# Let's see what happens when we build a simple object step-by-step.

# Step A: The Raw Class (Limitations)

class SimpleWrapper:
    def __init__(self, data):
        self.data = data

my_obj = SimpleWrapper(['A', 'B', 'C'])
# len(my_obj) ---> TypeError:- object of type 'SimpleWrapper' has no len()
# my_obj[0]    -> TypeError: 'SimpleWrapper' object is not subscriptable

# Step B: Adding __len__
class WrapperWithLen:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)
    
my_obj = WrapperWithLen(['A', 'B', 'C'])
print(len(my_obj))
# print(my_obj[0]) ---> Still fails!

# Step C: Adding __getitem__
class FullWrapper:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):
        return self.data[index]
    
my_obj = FullWrapper(['A', 'B', 'C'])
print(my_obj[1]) # Output:- 'B'

# And magically iteration works!
for item in my_obj:
    print(item)

# 4. PRACTICAL CODE
# Let's build a Guest List scenario.
from dataclasses import dataclass

@dataclass
class Guest:
    name: str
    status: str
    rsvp: bool

class GuestList:
    def __init__(self):
        self._guests = [] # Private internal list

    def add_guest(self, guest: Guest):
        self._guests.append(guest)

    def __len__(self):
        """Returns the total number of guests"""
        return len(self._guests)
    
    def __getitem__(self, index):
        """Allows indexing into the guest list."""
        return self._guests[index]
    
# --- Usages ---
g1 = GuestList()
g1.add_guest(Guest("Alice", "VIP", True))
g1.add_guest(Guest("Bob", "Standard", False))
g1.add_guest(Guest("Charlie", "Standard", True))

print(f"Total Guest: {len(g1)}") # Uses __len__
print(f"First Guest: {g1[0].name}") # Uses __getitem__

print("\nIterating through guests:")
for guest in g1:
    print(f"- {guest.name} (RSVP: {guest.rsvp})")

# Interview Question:-
""""
What is __len__?" Answer: A magic method that defines an object's length. It's called internally by Python's len() function.

"What is __getitem__?" Answer: A magic method that enables element access via square brackets []. It dictates what obj[index] returns.

"How does Python handle indexing internally?" Answer: Python translates obj[key] into obj.__getitem__(key). If you pass a slice like obj[1:3], Python creates a slice object and passes that as the key to __getitem__.

"Why are these important in ML?" Answer: They allow for lazy-loading data. We can represent massive datasets memory-efficiently by defining the dataset's size via __len__ and reading only specific data points from storage via __getitem__ when requested during mini-batch generation.

"""
# 8. MINI PRACTICE TASK
"""Problem 1: Add Slicing Support
Update __getitem__ so that if a user passes a slice (e.g., gl[0:2]), it returns a new GuestList instance containing only those guests, rather than a plain Python list.
Hint: Check if isinstance(index, slice)."""

from dataclasses import dataclass

@dataclass
class Guest:
    name: str
    status: str
    rsvp: bool

class GuestList:
    def __init__(self):
        self._guests = [] # Private internal list

    # Adds a Guest object to the list
    def add_guest(self, guest: Guest):
        self._guests.append(guest)

    def __len__(self):
        """Returns the total number of guests"""
        return len(self._guests)
    
    def __getitem__(self, index):
        """
        Problem-1: Handle both single indexing and slicing.
        Returns a single Guest for integers, or a new GuestList for slices.
        """
        # Checks if input is a slice like 0:2
        if isinstance(index, slice):
            # Create a new empty GuestList
            sub_list = GuestList()
            # Slice the internal list and assign it to the new object
            sub_list._guests = self._guests[index] # Copy sliced data
            return sub_list # Return new object
        else:
            # Handle standard integer indexing
            return self._guests[index] # Return a single guest
        
    # Filtering Logic    
    def get_rsvped(self):
        """
        Problem 2: Custom filtering.
        Returns a new GuestList containing only guests who RSVP'd.
        """
        # Returns only guests who RSVP = True
        rsvp_list = GuestList()
        # Use list comprehension to filter the internal list
        rsvp_list._guests = [guest for guest in self._guests if guest.rsvp]
        return rsvp_list

    # String representation
    def __repr__(self):
        """A helpful string representation for debugging."""
        return f"<GuestList: {len(self)} guests>"


# ==========================================
# TEST HARNESS & EXPECTED OUTPUTS
# ==========================================

# 1. Setup the data
gl = GuestList()
gl.add_guest(Guest("Alice", "VIP", True))
gl.add_guest(Guest("Bob", "Standard", False))
gl.add_guest(Guest("Charlie", "Standard", True))

print("--- Testing Problem 1: Slicing ---")
sub_list = gl[0:2]
print(f"Type of sliced object: {type(sub_list)}") # Expected: <class '__main__.GuestList'>
print(f"Length of sliced object: {len(sub_list)}")  # Expected: 2
print(f"Contents: {sub_list._guests}")

print("\n--- Testing Problem 2: Filtering ---")
rsvp_list = gl.get_rsvped()
print(f"Type of filtered object: {type(rsvp_list)}") # Expected: <class '__main__.GuestList'>
print(f"Length of filtered object: {len(rsvp_list)}") # Expected: 2 (Alice and Charlie)
print(f"Contents: {rsvp_list._guests}")