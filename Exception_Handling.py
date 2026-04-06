"""
Think of writing code like driving a car
1. The 'try' block is you driving down the highway. Everything is going smoothly.
2. An 'Exceopction' is sudden, unexpected pproblem-like a blown tire. if you don't handle it, the car crashes.
3. The 'expect' block is your safety protocol:pulling over to the shoulder and putting on a spare tire. The journey is delayed, but you survive and keep moving.
"""

"""Exception handling in Python is built on four distinct pillars:

try: The code that might potentially fail or throw an error.

except: The code that runs only if an error occurs in the try block. You can have multiple except blocks to handle different types of errors differently.

else: The code that runs only if the try block completes successfully (without any exceptions).

finally: The cleanup crew. This code runs no matter what—whether the try succeeded, whether an error was caught, or even if an uncaught error crashed the program."""

# Here is the anatomy of a complete exception handling block:
try:
    # STEP:-1: Attempt the risky operation
    print("Trying risky operation...")
    result = 10 / 0

except ZeroDivisionError:
    # STEP:-2: Handle specific known error
    print("Error: You can not divide by Zero!")

except Exception as e:
    # STEP:-3: fallback for other errors (Not a bare expect!)
    print(f"An unexpected error occurred: {e}")

else:
    # STEP:-4: Run only if the try block succeeds
    print(f"Success! The result is {result}")

finally:
    # STEP:-5: Always runs, perfect for cleanup!
    print("Cleanup: Closing resources.")



print("-------------------------------------------------------------")


# 4. PRACTICAL CODE
# Let’s apply this to a common scenario: reading a configuration dictionary.

def load_database_config(config_dict):
    print("--- Starting Database Connection Process ---")
    try:
        # Intentionally accessing a key that does not exist
        host = config_dict['DB_HOST']
        port = config_dict['DB_PORT']

    except KeyError as e:
        # Catching the exact error type
        print(f"Configuration Error: Missing required key {e} in settings.")

    else:
        # This only run if both keys were found successfully
        print(f"Config loaded successfully! Connecting to {host}:{port}")

    finally:
        # This always runs, ensuring we close files/connections or log the end of the attempt
        print("--- Database Connection Process Finished---")

# Let's test it with a missing keys
bad_config = {'DB_HOST': 'localhost'}
load_database_config(bad_config)


print("---------------------------------------------------------------")

"""Problem 1 (KeyError): Create a dictionary with user data: user = {"name": "Alice", "role": "Admin"}. Safely try to print the user's "age". If it's missing, print "Age data not found."""

# 1. Setup the initial dictionary
user = {"name": "Alice", "role": "Admin"}

# 2. Use try/except block to safely access the data
try:
    # We attempt the risky operation: accessing a key that might not exist
    print(user["age"])

except KeyError:
    # We catch the EXACT error (KeyError) and handle it gracefully
    print("Age data not found!")


print("--------------------------------------------------------------")

"""Problem 2 (ValueError): Write a script that asks the user for their birth year (input()). Convert it to an integer. If they type a word instead of a number, safely catch the error and print "Please enter a valid number."""

my_year = input("Enter your birth year:")
try:
    # The specifically risky operation
    result = int(my_year)

except ValueError:
    # Catching the exact typing error
    print("Please enter a valid number!")

else:
    # Runs only if the conversion successed!
    print(f"Awesome, you were born in {result}.")

"""Problem 3 (Finally):
Simulate opening a file by printing "File opened." Try to divide 10 / 0 (which causes a ZeroDivisionError). Catch it and print "Math error!" Ensure that "File closed." is printed no matter what happens."""

try:
    print("File Opened!")
    result = 10 / 0

except ZeroDivisionError:
    print("Math Error!")

finally:
    print("File Closed!")