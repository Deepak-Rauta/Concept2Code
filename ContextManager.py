"""1. INTUITION FIRST
What is Resource Management?
Whenever your Python program talks to the "outside world," it borrows resources from the Operating System. These resources include opening a file, establishing a database connection, or claiming a network port. Because these resources are limited, you must return them when you are done."""

"""What is a Context Manager?
A context manager is an object designed to strictly control the setup and teardown of resources. It guarantees that the "cleanup" step happens no matter what occurs inside your code."""

"""__enter__ and __exit__ methods:
For an object to be a context manager, it must implement two "magic" (dunder) methods:

__enter__(self): Runs at the start of the with block. It sets up the resource and returns it.

__exit__(self, exc_type, exc_val, exc_tb): Runs at the end of the with block. It handles the cleanup. If an error occurred inside the block, Python passes the error details to these arguments."""

# The Old Way (Manual Handling):
# file = open("data.txt", "w")
# file.write("Hello")
# file.close() # We must remember this!

# # The Danger (Error before close):
# file = open("data.txt", "w")
# 10 / 0  # CRASH! The program halts here.
# file.close() # This never runs. The file is left open and locked.

# # The Pythonic Way (with statement):
# with open("data.txt", "w") as file:
#     file.write("Hello")
#     10 / 0

# Even with the crash, python autometically closes the file here!

# Execution Flow:

# open() is evaluated.

# The context manager's __enter__ method is called (opening the file).

# The returned value is assigned to file.

# The block executes (write(), then the crash).

# The context manager's __exit__ method is triggered immediately, closing the file safely.


# 4. PRACTICAL CODE
# Let's write a practical script that reads a policy document and audits it for restricted keywords.

# The function basically does “Scan a file and flag dangerous/restricted words”
def audit_policy_document(filepath: str, keywords: list[str]) -> None:
    print(f"--- Auditing {filepath}")

    # Using 'with' ensures the file is safely closed after reading
    try:
        with open(filepath, "r", encoding="utf-8") as file: # Here it open the file in read mode  and uses UTF-8 encoding, store file object in file.
            # Here it reads the file line-by-line and here line is the actual text
            for line_num, line in enumerate(file, start=1):
                # Check for any restricted keywords in the current line
                # Goes through each word ["banned", "restricted", "prohibited"]
                for keyword in keywords:
                    if keyword in line.lower():
                        print(f"[FLAG] line {line_num}: Contains restricted word '{keyword}'")
                        print(f"      -> {line.strip()}")

    except FileNotFoundError:
        print(f"[ERROR] The file {filepath} was not found.")
    
    print("--- Audit Complete ---\n")

# Excecute the audit
restricted_word = ["banned", "restricted", "prohibited"]
audit_policy_document("safety_policy_guidelines.txt", restricted_word)


# Practice Task:- 01
class MockDBConnection:
    def __enter__(seelf):
        print("Connecting to database...")
        # What we return here gets assigned to the variables 'as'
        return "DB_CONN_OBJECT"
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # This is guaranteed to run, even if the code inside the 'with' block crashes
        print("Closing databse Connection...")

        # We return False (or implicitly None) to ensure any exceptions 
        # that occur inside the with block are NOT swallowed/hidden.

        return False
# --- Testing the Context Manager ---

print("--- Starting Application ---")

with MockDBConnection() as conn:
    print(f"Performing queries with: {conn}")

print("--- Application Finished ---")


print()


"""Problem 2: The Execution Timer
Create a class called Timer.

__enter__ should record the start time using time.time().

__exit__ should record the end time, calculate the difference, and print "Execution took X.XXXX seconds."""

import time

class Timer:
    def __enter__(self):
        # Record the exact moment the block starts
        self.start_time = time.time()

        # We can return 'self' just in case we wnated to access
        # # the timer object inside the 'with' block, but it's optional here

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Record the exact moment the block finished!
        self.end_time = time.time()

        # Calculate the elapsed time
        elapsed_time = self.end_time - self.start_time

        # Print the result, formatting to 4 decimal places
        print(f"Excecution took {elapsed_time:.4f} seconds.")

        # Return False so we don't accidentally hide any bugs/exceptions
        # that might occur while the code is being timed.
        return False
# --- Testing the Context Manager ---
print("--- Starting Task ---")

# We don't necessarily need 'as t' here since we just want the side-effect of timing

with Timer():
    # Simulating a slow operation like a network request or heavy calculation
    time.sleep(1)

print("--- Task Finished ---")