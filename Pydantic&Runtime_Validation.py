"""What is Pydantic?
Pydantic is Python's most popular data validation library. It is widely used because it is incredibly fast (its core is written in Rust) and it uses standard Python type hints to do its job, making it very natural to write."""

"""The BaseModel
BaseModel is the heart of Pydantic. When you create a class that inherits from BaseModel, you aren't just making a normal Python object. You are creating a strict data schema."""

# Let's build a Guest model for a wedding bot.
from pydantic import BaseModel, ValidationError

# Create the BaseModel
class Guest(BaseModel):
    name: str
    phone_number: int

print("--- SCENARIO A: valid Input ---")
try:
    # Valid Data
    guest1 = Guest(name="Deepak Kumar Rauta", phone_number= 6372756353)
    print(f"Success! Created guest: {guest1.name}")
except ValidationError as e:
    print(e)

print("\n--- SCENARIO B: Invalid Input (Wrong Type) ---")
try:
    # Phone number is a string that CANNOT be converted to an int
    guest2 = Guest(name="Nita", phone_number="not-a-number")
except ValidationError as e:
    print("Validation error Caught!")
    print(e.errors()[0]['msg'])  # Prints: Input should be integer...

print("\n--- SCENARIO C: Missing Field ---")
try:
    # Forgot the phone number
    guest3 = Guest(name="Smruti Sikha")
except ValidationError as e:
    print("Validation error Cought!")
    print(e.errors()[0]["msg"]) # Prints: Field required





# REAL-WORLD SCENARIO
"""Imagine your wedding bot receives a messy JSON payload from a web form. Here is how Pydantic sanitizes it before letting it touch your database."""

from pydantic import BaseModel, ValidationError
class Guest(BaseModel):
    name: str
    phone_number: int

# Simulating raw, untrusted input from an API request
incoming_api_payload = {
    "name": "Nita",
    "phone_number": "987652314",
    "hacker_injection": "DROP TABLE guests;" # Extra garbage data
}

try:
    # We unpack the dictionary into the model
    clean_data = Guest(**incoming_api_payload)

    print("Data sanitized successfully!")
    print(f"Name: {clean_data.name} (Type: {type(clean_data.name)})")
    # Pydantic coerced the string into an integer!
    print(f"phone: {clean_data.phone_number} (Type:{type(clean_data.phone_number)})")

    # Notice 'hacker_injection' is ignored by default because it's not in the model!

except ValidationError as e:
    print("Blocked bad API request.")


# Common Mistakes
# 1. Correct: guest = Guest(name="Alice", phone_number=123) (Pydantic requires keyword arguments by default).
# 2. Wrong: guest = Guest("Alice", 123) (Passing positional arguments).


# Task:-1 
"""Problem 1: The User Profile
Create a User model inheriting from BaseModel.
Fields: username (str), age (int), is_active (bool).
Test: Instantiate it with age="25" (string) and is_active="yes".
Expected Behavior: Pydantic should successfully coerce "25" to 25 and "yes" to True."""

class User(BaseModel):
    username: str
    age: int
    is_active: bool

try:
    user1 = User(username="Deepak Kumar Rauta", age="25", is_active="yes")
    # ADDED: Let's print the object to see the converted data types!
    print("Success! No errors were raised!")
    print(f"User Object: {user1}")
    print(f"Notice the types! Age is {type(user1.age)}, Is_Active is {type(user1.is_active)}")
except ValidationError as e:
    print("Validation error Cought!")
    print(e.errors()[0]["msg"])



"""Problem 2: The Product Catalog
Create a Product model.
Fields: title (str), price (float).
Test: Instantiate it with price="expensive".
Expected Behavior: It should raise a ValidationError because "expensive" cannot be converted to a float. Catch this error and print the message."""
class Product(BaseModel):
    title: str
    price: float

try:
    my_product = Product(title="LPG", price="Expensive")
    print("No Error! All Good")
    print(f"User Object: {my_product}")
    print(f"Notice! the types Title is {type(my_product.title)}, Price is {type(my_product.price)}")

except ValidationError as e:
    print("Validation Cought an error!")
    print(e.errors()[0]["msg"])