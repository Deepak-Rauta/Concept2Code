"""1. INTUITION FIRST: The Factory vs. The Clerk
Imagine you have 1,000 envelopes that need stamps.

Standard Python List: This is like hiring a clerk. The clerk picks up one envelope, finds a stamp, licks it, sticks it, puts it down, and then moves to the next. If the clerk gets distracted (Python’s overhead), the whole process slows down.

NumPy Vectorization: This is a factory assembly line. A specialized machine grabs all 1,000 envelopes at once, and a giant press applies 1,000 stamps in a single "thump."

Why Python lists are slow: Python is "dynamically typed." Every time it looks at an item in a list, it has to ask: "Are you an integer? A string? A float?" This constant checking (overhead) kills performance in AI, where we process billions of data points.

Why NumPy is critical: In AI/ML, we represent everything (images, text, sound) as numbers. Training a model is just doing billions of additions and multiplications. Without NumPy, training ChatGPT would take centuries instead of months."""

"""2. CORE THEORY
What are NumPy Arrays?
A NumPy array (ndarray) is a grid of values, all of the same type. Unlike Python lists, which can hold a mix of strings and numbers, NumPy demands uniformity so it can map the data directly to your computer's memory.

Vectorization Defined
Vectorization is the process of performing an operation on an entire array (an entire "vector") at once, rather than looping through individual elements.

The Secret Sauce: C-Level Optimization
When you run a NumPy operation, the "looping" doesn't happen in Python. It happens in optimized C and Fortran code running under the hood. It bypasses the slow Python Interpreter entirely."""

"""Feature    Python Lists            NumPy Arrays
Data Type    Heterogeneous (Mixed)    Homogeneous (Same type)
Speed        Slow (High overhead)     Fast (C-level speed)
Memory       Scattered in memory      Contiguous (Side-by-side)
Functionality General purpose          Specialized for Math/Science"""


# 4. Practical Code:- The speed test

# import numpy as np
# import time

# # Create 1 million random numbers
# size = 1_000_000
# python_list = list(range(size))
# numpy_array = np.arange(size)

# # --- Test Pyhton Loop ---
# start_time = time.time()
# list_result = [x**2 for x in python_list]
# python_time = time.time() - start_time

# # -- Test Numpy Vectorization ---
# start_time = time.time()
# numpy_result = numpy_array ** 2
# numpy_time = time.time() - start_time

# print(f"Python Loop Time: {python_time:.4f} seconds")
# print(f"NumPy vectorized Time: {numpy_time:.4f} seconds")
# print(f"Speedup: {python_time / numpy_time:.2f}x faster!")

# Afetr run this code we will get a ZeroDivisionError because:- numpy_time was exactly 0.0

# Why was it 0.0? Because squaring 1,000,000 numbers using NumPy's optimized C-backend is so incredibly fast that it happened faster than your computer's clock could measure using time.time().

# The time.time() function is meant for general timekeeping (like checking the time of day) and usually only updates every 1 to 15 milliseconds depending on your operating system. Because the NumPy operation took less than a millisecond, the start_time and the end time.time() were perfectly identical.

# The Fix: How to Benchmark Properly
# To fix this, we need to use a high-resolution clock designed specifically for measuring tiny fractions of a second: time.perf_counter().

import numpy as np
import time

# Let's increase the size to 10 million to get better measurements
size = 10_000_000
python_list = list(range(size))
numpy_array = np.arange(size)

# --- Test Python Loop ---
# Use perf_counter() for highly accurate benchmarking
start_time = time.perf_counter() 
list_result = [x**2 for x in python_list]
python_time = time.perf_counter() - start_time

# --- Test NumPy Vectorization ---
start_time = time.perf_counter()
numpy_result = numpy_array ** 2
numpy_time = time.perf_counter() - start_time

print(f"Python Loop Time: {python_time:.4f} seconds") # .4 tells python to round the number to exactly 4 decimal points
print(f"NumPy Vectorized Time: {numpy_time:.6f} seconds") # Added more decimal places here

# Safe division check just in case you run this on a supercomputer!
if numpy_time > 0:
    print(f"Speedup: {python_time / numpy_time:.2f}x faster!")
else:
    print("NumPy was too fast to measure!")


"""7. INTERVIEW QUESTIONS
What is vectorization? It is performing operations on entire arrays at once by leveraging optimized, compiled code (C/Fortran) to avoid Python loop overhead.

Why is NumPy faster than Python lists? Because of Contiguous Memory (data is next to each other), Homogeneity (no type checking), and C-level implementation.

What is Broadcasting? The ability of NumPy to perform operations on arrays of different shapes (within certain rules)."""

# Mini Practice Task:-
"""Task 1: The Salary Bump
You have an array of salaries: [50000, 60000, 75000, 45000]. Give everyone a 10% raise using vectorization.

Expected Output: [55000., 66000., 82500., 49500.]"""

import numpy as np
# First we must convert the standard python list into a Numpy array
salaries = np.array([50000, 60000, 70000, 45000])

# Apply the 10% rise using Broadcasting
new_salaries = salaries * 1.10

print("Original:", salaries)
print("With Rise:", new_salaries)

"""Why this works:
This uses Broadcasting. You told NumPy to multiply an array of 4 numbers by a single number (1.10). NumPy instantly "broadcasts" (stretches) that 1.10 across the entire array, multiplying every single element simultaneously in optimized C-code."""

"""Task 2: The Filter
From the array np.array([10, 5, 20, 3, 15]), find all values greater than 10. (Hint: arr[arr > 10])

Expected Output: [20, 15]"""

import numpy as np

arr = np.array([10, 5, 20, 3, 15])

# Find all values strictly greater then 10
filtered_array = arr[arr > 10]

print("Filtered Result:", filtered_array)
