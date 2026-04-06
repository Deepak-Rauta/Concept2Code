"""1. INTUITION FIRST
What are custom exceptions?
At their core, custom exceptions are just specific error labels you create for your own application's unique rules. Python has built-in errors for general programming mistakes, but it doesn't know anything about your specific business logic."""

# Step 1: Create a basic custom exception
class MyCustomError(Exception):
    """Base class for my custom errors."""

# Step 2: Add custom messages and attributes
# You can override the __init__ method to pass dynamic data to the error.

# Here i created my own error (Exception)
# I want to create a new error type
# It is based on python's built-in Exception

# This class means:-
# “If temperature is too high, raise a clear error with the exact temperature value.”
class TemperatureTooHighError(Exception):
    # This runs when the error is created!
    # Here message is default message (i can override it!)
    def __init__(self, temperature, message="Temperature exceeds safe limits"):
        # 
        self.temperature = temperature # Store the temperature inside the error, later we can access it like:- error.temperature
        self.message = f"{message}: {temperature}°C" # Custom message
        super().__init__(self.message) # It send my message to the base Exception class

# Function to check temperature
def check_temperature(current_temp):
    if current_temp > 100:
        raise TemperatureTooHighError(current_temp)
    else:
        print("Temperature is safe! Have a good day.")

# Raise and catch the exception
try:
    current_temp = 190
    check_temperature(current_temp)

except TemperatureTooHighError as e:
        print(f"Caught an error: {e}")
        print(f"Actual temperature was: {e.temperature}")


print("---------------------------------------------------------------")

# Task:-1
class AgeTooLowerError(Exception):
     def __init__(self, age, message="Age is below the minimal limit"):
          self.age = age
          self.message = f"{message}: {age} years"
          super().__init__(self.message)

def check_age(age):
     if age < 18:
          raise AgeTooLowerError(age)
     else:
          print("Access granted! You can welcome")

try:
     age = 10
     check_age(age)

except AgeTooLowerError as e:
     print(f"Caught an error: {e}")
     print(f"Actual age was:{e.age}")


print("---------------------------------------------------------------")

# 4. PRACTICAL CODE

import random
# 1. Define the custom exception
class DataFormatError(Exception):
     """Raised when the input data is not in the expected format (e.g., missing columns)."""
     pass

class ModelTimeoutError(Exception):
     "Raised when the meachine learning model takes too long to respond"
     pass

# 2. Dummy function that randomly raises one of these exceptions
def process_machine_learning_request():
     print("Starting ML pipeline...")

     # Simulate a random failure state (0: Success, 1: Bad Data, 2: Timeout)
     outcome = random.choice([0, 1, 2])

     if outcome == 1:
          raise DataFormatError("Expected CSV format, but recevied JSON data.")
     
     elif outcome == 2:
          raise ModelTimeoutError("Model inference exceeded the 5.0 second limit.")
     
     else:
          return "Prediction successful: [0.89, 0.92]"
     
# 3. Call the function and catch exceptions separately 
def run_pipeline():
    try:
        result = process_machine_learning_request()
        print(result)
        
    except DataFormatError as e:
        print(f"DATA ERROR: Please check your input pipeline. Details: {e}")
        
    except ModelTimeoutError as e:
        print(f"SYSTEM ERROR: The server is under heavy load. Details: {e}")
        
    except Exception as e:
        # A fallback catch-all for any other unexpected errors
        print(f"UNEXPECTED ERROR: {e}")

# Run the simulation
run_pipeline()