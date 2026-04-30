"""1. Intuition First
In many languages, functions and data are entirely separate. But in Python, functions are objects.

Think of a function like a specialized power tool—say, a power drill. Usually, you just turn it on to drill a hole (calling the function). But because it's a physical object, you can also do other things with it:

1. You can put it in a toolbox (assign it to a variable or list).

2. You can hand it to your coworker (pass it to another function).

3. Your coworker can build a custom drill and hand it back to you (returning a function)."""

"""2. Core Theory
Let's look at the formal definitions of what's happening under the hood.

First-Class Objects: In Python, functions are "first-class citizens." This means they have the exact same rights as strings, integers, or dictionaries. They are created at runtime, can be assigned to variables, passed as arguments, and returned.

Higher-Order Functions: A mathematical term for a function that does at least one of two things: it takes one or more functions as arguments, or it returns a function as its result.

Closures: A closure occurs when a nested (inner) function "remembers" the state of its surrounding (outer) environment, even after the outer function has finished executing. The inner function essentially takes a snapshot of the variables it needs.

Python Internals: Under the hood, when you define a function using def, Python creates an object of type function in memory. It has attributes just like any other object (e.g., my_func.__name__ or my_func.__doc__). When a closure is created, Python stores the captured variables in a special attribute called __closure__."""

# Step-by-step breakdown
# Let's see the four pillar of this concept in action.

# 1. Assining a function to a variable:
def say_hello():
    return "Hello"
# Assign the function object to a new variable (NO parentheses)
greet = say_hello
print(greet())

# 2. Passing a function as an argument:
def excecute_twice(func):
    func()
    func()
excecute_twice(say_hello) # Passes the tool, doesn't execute it right away

# 3. Returning a function:
def get_greeter():
    def greeter():
        return "Hi from inside!"
    return greeter  # Returning the function object itself!

my_new_func = get_greeter()
print(my_new_func)

# 4. The Closure (Remembering state):
def make_multiplier(n):
    # This inner function remembers 'n' even after make_multiplier is done
    def multiplier(x):
        return x * n
    return multiplier

times_three = make_multiplier(3)
print(times_three(30))


"""4. Practical Code
Here is your requested real-world scenario. We will build a basic wrapper function that intercepts another function to perform a security check."""

def security_check(func):
    """A higher-order function acting as a security checkpoint."""
    def wrapper():
        print("Checking permissions...")
        print("Permission granted. Excecuting task.")
        # Excecute the function that was passed in
        func()

    return wrapper # Note: we return the wrapper, we don't call it here!

def access_secure_data():
    print("-> ACCESSED: Top Secret Financial Records")

# 1. Pass our secure function into the security check
secure_access = security_check(access_secure_data)

# 2. Execute the returned wrapper function
secure_access()