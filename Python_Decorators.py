"""1. INTUITION FIRST
What is a decorator?
In simple terms, a decorator is a function that takes another function, adds some extra functionality to it, and then returns it. It allows you to "decorate" an existing function with new behavior without modifying the original function's source code.""" 

"""Why are they powerful?
Decorators enforce the DRY (Don't Repeat Yourself) principle. If you need to check if a user is logged in before they view a profile, edit a post, or delete a comment, you don't want to write if not logged_in: return error in all three functions. Instead, you write one @require_login decorator and slap it on top of those functions. It keeps your core logic clean and separates concerns like logging, authentication, and performance monitoring."""

"""2. CORE THEORY
To understand decorators, you must understand a few Python rules:

Functions are First-Class Objects: In Python, functions aren't just blocks of code. They are objects. You can assign them to variables, pass them as arguments to other functions, and return them from other functions.

Wrapper Functions: Because you can return a function from a function, you can create a "wrapper." This is a nested function that executes around the original function.

The @ Syntax Internals: The @decorator syntax is just "syntactic sugar" (a shortcut). Writing @my_decorator above def my_func() is secretly doing this under the hood: my_func = my_decorator(my_func).

*args and kwargs: These allow a function to accept any number of positional (*args) and keyword (kwargs) arguments. Wrappers use these so they can wrap any function, no matter how many arguments the original function requires."""


# 3. STEP-BY-STEP BREAKDOWN
# Let's build a decorator manually, step-by-step

# Step 1:- The Normal Function
def say_hello(name):
    return f"Hello, {name}!"

# Step 2: Wrap it manually using another function
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        # 1. Run the original function
        original_result = func(*args, **kwargs)
        # 2. Modify the result
        return original_result.upper()
    
    # 3. Return the new wrapper function
    return wrapper

# Manually wrapping
say_hello_loud = uppercase_decorator(say_hello)
print(say_hello_loud("Deepak"))

# Step: 3 Convert to the @syntax
@uppercase_decorator
def say_hello(name):
    return f"Hello, {name}!"

print(say_hello("Nita"))

# 4. PRACTICAL CODE: Performance Timer
# Let's build a highly practical decorator used in the real world: a timer to measure execution speed. We will apply it to a Binary Search algorithm.

import time
# 1. Define the decorator
def perfomance_timer(func):
    # The 'func' argument is the opriginal function being decorated (in this case, binary search)
    def wrapper(*args, **kwargs):
        # *args and **kwargs act as a catch-all for any arguments passed to the function.
        start_time = time.perf_counter()  # Start timer  1. Note the exact time before the function runs.
        result = func(*args, **kwargs)    # Excecute function
        end_time = time.perf_counter()    # End timer # 3. Note the exact time the function finishes.


        # Calculate time in miliseconds
        excecution_time = (end_time - start_time) * 1000
        # 5. Print the time it took. func.__name__ dynamically gets the name of the original function.
        print(f"[{func.__name__}] executed in {excecution_time:.4f} ms")
        # 6. Crucial step: Return the result of the original function back to the user.
        return result
    # Return the newly constructed wrapper function so it can replace the original function.
    return wrapper

# 2. Apply it to a binary search
@perfomance_timer
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Execution
my_list = list(range(1, 1000000)) # List of numbers 1 to 999,999
target_num = 999999

print(f"Searching for {target_num}...")
index = binary_search(my_list, target_num)
print(f"Output: Found at index {index}")

print("------------------------------------------------------------")



"""5. REAL-WORLD SCENARIO
Where will you see decorators on the job?

API Frameworks (Flask/FastAPI): They use decorators for routing. @app.get("/users") tells the framework, "Whenever a GET request hits /users, run the function beneath this decorator."

Logging Systems: Automatically writing to a log file whenever a sensitive function (like a bank transfer) is called, recording the time, arguments, and the user who called it.

Authentication/Authorization: Checking if a JSON Web Token (JWT) is valid before allowing access to a protected route (e.g., @login_required or @admin_only)."""

# Mini Task:-1
"""Problem 1: Create a @logger decorator.
It should print "Calling function: [name]" before the function runs, and "Finished function: [name]" after.
Apply it to a simple multiplication function."""

# 1. Define the Decorator
def logger(func):
    def wrapper(*args, **kwargs):
        # Action BEFORE the function runs
        print(f"Calling function: {func.__name__}") # func.__name__ dynaically gets the original function.

        # Excecute the original function and save it result
        result = func(*args, **kwargs)

        # Action AFTER the function runs
        print(f"Finished function: {func.__name__}")

        # Return the original result back to the user
        return result
    
    return wrapper

# 2. Apply it ton a simple multiplication function
@logger
def multiply(a, b):
    return a * b

# Test it out
result = multiply(4, 5)
print(f"Result: {result}")

print("-----------------------------------------------------------")




