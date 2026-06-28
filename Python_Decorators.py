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



# Example 1: Function inside Function
# Before decorators, understand that functions are objects in Python.
def greet():
    print("Hello!")

print(greet)

# <function greet at 0x...>
# Python treats functions like variables.

## Example 2: Pass a Function as an Argument
def greet():
    print("Hello!")

def execute_function(func):
    func()

execute_function(greet)

# DRY run for better understanding
# execute_function(greet)
# func = greet
# func() it becomes greet()

# Example 3: Return a Function
def outer():
    
    def inner():
        print("Inside Inner")

    return inner

my_function = outer()
my_function()

# DRY run for better understanding
# my_function = outer() return inner
# so my_function = inner
# my_function() becomes inner()
# So, output is Inside Inner

# Example 4: First Real Decorator
# Suppose we want to print a message before a function runs.
def decorator(func):

    def wrapper():
        print("Before function excecution!")

        func()  # here it is actually referring to greet. memory view func ------> greet function

    return wrapper

# Original function
def greet():
    print("Hello Deepak!")

# Apply decorator manually!
greet = decorator(greet)
greet()

# Dry Run
# Step:- 1
# greet = decorator(greet)
# Inside decorator func = greet
# Create wrapper and return wrapper
# Now, greet = wrapper
# Now, greet() actually call wrapper()
# Insdie wrapper print("Before function execution")
# So, output is Before function execution
# Then, func(), which is original function and return "Hello Deepak!"

# Example 6: Decorator That Adds a Line Before and After
def decorator(func):  

    # Define the inner function
    # It won't be created until decorator() is called.
    # When decorator() is called, it will return the wrapper function.
    def wrapper():
        print("---- Start ----")

        func()

        print("---- End ----")

    return wrapper

@decorator
def greet():
    print("Welcome!")

greet()

# When python see @decorator python actually converts this to 

# def greet():
#     print("Welcome!")

# greet = decorator(greet)

# Practical task
def my_decorator(func):

    def wrapper():

        print("Function Started")

        func()

    return wrapper

@my_decorator
def greet():
    print("Welcome")

greet()


# 1. Decorators with Arguments (*args and **kwargs)
# So far my decorator only works for functions with no parameters.

# @decorator
# def greet():
#     print(f"Hello {name}")  
# In the above code my current decorator will fail because wrapper() doesn't accept argument

# The solution:-

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        func(*args, **kwargs)
        print("After")
    return wrapper

# This is the most common decorator pattern in real projects.

# 2. Closures ⭐ (Very Important)

# Decorators are built on closures.
# Example:-
def outer():
    x = 10

    def inner():
        print(x)

    return inner

func = outer()
func()

# Question:

# How can inner() still access x after outer() has finished executing?

# Answer:
# Because Python remembers the surrounding variables. This is called a closure.

# 4. PRACTICAL CODE: Performance Timer
import time

# 01. Define the decorator
def perfomance_timer(func): # Here func is actually 
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # Start time
        result = func(*args, **kwargs)    # Excecute function  it becomes result = calculate()
        end_time = time.perf_counter()    # End timer

        # Calculate time in milisecond
        excecution_time = (end_time - start_time) * 1000
        # This line prints the function name and how long it took to execute.
        print(f"[{func.__name__}] excecuted in {excecution_time:.4f}ms")

        return result       # return the 
    return wrapper


# 2. Apply it to binary search
@perfomance_timer
def binary_serach(arr, target):
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

# 3. Excecution
my_list = list(range(1, 1000000))
target_num = 750000

print(f"Searching for {target_num}")
index = binary_search(my_list, target_num)
print(f"Output: Found at Index {index}")

#         print(f"[{func.__name__}] excecuted in {excecution_time:.4f}ms") Let's understand this
# func.__name__ we alreday know i.e func is the original function.
# so my func = binary_search




