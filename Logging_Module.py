"""What is the logging module?
Python includes a built-in module called logging. It provides a flexible framework for generating log messages from Python programs."""


"""The 5 Logging Levels (Severity)
Logs are categorized by urgency. By setting a minimum level, you can filter out noise.

DEBUG (10): Detailed information, typically of interest only when diagnosing problems (e.g., Fetched user_id 42 from DB).

INFO (20): Confirmation that things are working as expected (e.g., Server started on port 8080).

WARNING (30): An indication that something unexpected happened, but the software is still working (e.g., Disk space running low, or Retrying failed API call).

ERROR (40): Due to a more serious problem, the software has not been able to perform some function (e.g., Failed to save user profile).

CRITICAL (50): A serious error, indicating that the program itself may be unable to continue running (e.g., Database connection completely lost)."""

"""How logs are stored
By default, logs print to the console. However, in production, they are usually routed to a .log file, or formatted as JSON and sent to logging services like Datadog, Splunk, or AWS CloudWatch."""

# STEP-BY-STEP BREAKDOWN
import logging
# Configure using logging.basicConfig():
# You should only call this once, usually at the very beginning of your main script.
logging.basicConfig(
    level = logging.INFO, # The minimum severity to track, here all DEBUG messages are ignored.
    format = '%(asctime)s - %(levelname)s - %(message)s', # Current date and time, injects the severity level (INFO, ERROR, etc), actual log message
    filename = 'app.log' # Optional:- Remove this to print to console
)


# Practical Code:-

# 01:- Setup the Configuration 
import logging
logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    force= True # Ignore any previous logging settings and apply my new configuration

)
# 02:- Sample Data
transactions = [150.0, 20.50, -5.00, 99.99]

logging.info("Starting transcaction processing job!")

# 03:- Processing loop
for amount in transactions:
    if amount > 0:
        logging.info(f"Successfully processed transaction of ${amount}")
    elif amount == 0:
        logging.warning("Received a $0.00 transaction. Ignoring.")
    else:
        logging.error(f"Invalid transaction amount: ${amount}. Data might be corrupted.")

logging.info("Transaction processing job finished!")      

print("---------------------------------------------------------------")

"""Task 1 (INFO): Create a function download_file(filename). If the filename ends with .txt, log an INFO message saying it downloaded successfully."""

import logging

# STEP:-1 Global setup (Excecute only once)
logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

# STEP:-2 Function Definition
def download_file(filename):
    """Simulates downloading a file and logs the result."""

    # STEP:-3 Check the file extension
    if filename.endswith('.txt'):
        # STEP:-4 Log the success as an INFO level event
        logging.info(f"Successfully downloaded {filename}")

# Test the function
download_file("report.txt")
download_file("data.csv")

print("----------------------------------------------------------------")

"""Task 2 (WARNING): If the filename ends with .exe, log a WARNING saying "Suspicious file type detected", but allow the code to finish (do not use return to stop it)."""

import logging

# STEP:-01 Global setup (Excecute only once)
logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

# STEP:-02 Function Definition
def warning_file(filename):
    # STEP:-3 Check the file extension
    if filename.endswith(".exe"):
        # STEP:-4 Log the warning
        logging.warning(f"Suspicious file type detected {filename}")

warning_file('data.exe')

"""Task 3 (ERROR): If the filename is an empty string "", log an ERROR saying "Filename cannot be empty" and stop the process (use return)."""

import logging

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

def download_file(filename):
    if filename == "":
        logging.error("File name can not be empty! please, eneter a valid filename.")
        return # Stop the function immediately
download_file("")



print("---------------------------------------------------------------")

# All together
import logging

# 1. Global Setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# 2. The Universal Download Function
def download_file(filename):
    # Task 3: ERROR (Circuit Breaker)
    if filename == "":
        logging.error("File name cannot be empty! Please enter a valid filename.")
        return # Stops the function immediately
        
    # Task 1: INFO (Happy Path)
    elif filename.endswith(".txt"):
        logging.info(f"Successfully downloaded {filename}")
        
    # Task 2: WARNING (Suspicious but allowed)
    elif filename.endswith(".exe"):
        logging.warning(f"Suspicious file type detected: {filename}")
        
    # Fallback for anything else
    else:
        logging.info(f"Downloaded unknown file type: {filename}")

# 3. Testing the System
print("--- Starting Processing ---")
download_file("report.txt")  # Triggers INFO
download_file("malware.exe") # Triggers WARNING
download_file("")            # Triggers ERROR and stops
print("--- Finished Processing ---")