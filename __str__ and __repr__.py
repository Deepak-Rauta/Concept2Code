"""1. INTUITION FIRST
What happens by default?
If you create a class in Python and try to print an instance of it, Python doesn't know what information is important to you. So, it gives you the default object representation, which looks like this: <__main__.MyClass object at 0x7fa2b8c9d1a0>. That is just the class name and its physical memory address—not very helpful!"""

"""__str__ (String Representation): Its goal is to be readable. It is meant for end-users or for formatting output in a UI/CLI.

__repr__ (Official Representation): Its goal is to be unambiguous. It is meant for developers, logging, and debugging. A good __repr__ should contain all the information necessary to recreate the object."""

"""When is each called?

__str__ is triggered when you use print(object), str(object), or f-strings like f"{object}".

__repr__ is triggered when you inspect the object in the interactive Python shell, when you print a list/dictionary containing the object, or when you use repr(object)."""

"""The Fallback Rule
Python has a built-in safety net: If you do not define __str__, Python will automatically use __repr__ as a fallback. (However, the reverse is not true. If you only define __str__, the interactive console will still show the ugly memory address). Because of this, always write a __repr__ first!"""

# Step 1: No Representation (The Default)
class User:
    def __init__(self, name):
        self.name = name

u = User("ALice")
print(u)

# Step 2: Adding __str__ (Better for users)
class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"User: {self.name}"
    
u = User("Deepak")
print(u)

# Step 3: Adding __repr__ (Better for developers)
class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"User: {self.name}"
    
    def __repr__(self):
        return f"User(name='{self.name}')"
    
u = User("Deepak Rauta")

# If typed in a REPL/console:
# >>> u
# Output: User(name='Deepak Rauta')

# 4. PRACTICAL CODE: The Wedding Concierge Bot

import logging

class Guest:
    def __init__(self, name: str, status: str, rsvp: bool):
        self.name = name
        self.status = status
        self.rsvp = rsvp

    # For the End-User (Readable)
    def __str__(self):
        return f"{self.name} ({self.status})" # Deepak (VIP) showing like this in output
    
    # For the Developer (Precise & Unambiguous)
    def __repr__(self):
        return f"Guest(name={self.name!r}, status={self.status!r} rsvp={self.rsvp})"
    
# --- Testing the output ---
guest = Guest("Deepak", "VIP", True)

# 1. Print (calls __str__)
print("Print Output:", guest)

# 2. Inside a list (call __repr__ even if printed)
print("List Output:", [guest])

# 3. F-string vs Developer string
print(f"User View: {guest}")
print(f"Developer View: {guest!r}")  # !r forces __repr__ inside an f-string

# 4. Logging Output
logging.basicConfig(level=logging.DEBUG)
logging.debug(f"State of object during excecution: {repr(guest)}")

"""Note: In the __repr__, I used {self.name!r}. The !r tells Python to use the repr() of the string itself, which automatically adds the necessary quotes around "Deepak"!"""


# Problem:-1 The Wedding Menu
"""Create a MenuItem class with fields name: str, price: float, and is_veg: bool.

Expected str(item): "Truffle Risotto - $25.50"

Expected repr(item): "MenuItem(name='Truffle Risotto', price=25.5, is_veg=True)"""

class MenuItem:
    def __init__(self, name: str, price: float, is_veg: bool):
        self.name = name
        self.price = price
        self.is_veg = is_veg

    def __str__(self):
        return f"{self.name}, - ${self.price:.2f}"
    
    def __repr__(self):
        return f"MenuItem(name={self.name!r}, price={self.price!r}, is_veg={self.is_veg})"

# --- Testing the output ---
menu = MenuItem("Truffle Risotto", 25.50, True)

# Print (call __str__)
print("Print output:", menu)

# Inside a list (call __repr__ even if printed)
print("List Output:", [menu])


"""Problem 2: The Seating Chart
Create a Table class with fields number: int and capacity: int.

Expected str(table): "Table 4 (Seats 8)"

Expected repr(table): "Table(number=4, capacity=8)"""

class Table:
    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity

    def __str__(self):
        return f"Table {self.number} (Seats {self.capacity})"
    
    def __repr__(self):
        return f"Table(number={self.number}, capacity={self.capacity})"
    
# --- Testing the output ---
table = Table(4, 8)

# Print (call __str__)
print("Print Output:", table)

# Inside a list (call __repr__ even if printed)
print("List Output:", [table])


