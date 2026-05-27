# 1.Import all required libraries
# pandas is the industry standard for data manipulation and analysis in python.

import pandas as pd

# 2. Load the dataset from a CSV file 
# We are using a public URL for the Iris dataset so it loads instantly without needing local files.
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
# Create the dataframe
df = pd.read_csv(url)

print("--- 1. FIRST 5 ROWS ---")
# 3. Display the first 5 rows of the dataset using .head()
# This gives us a quick visual check of what the data looks like.
print(df.head())
print("\n" + "="*40 + "\n")

print("--- 2. DATASET INFORMATION ---")
# 4a. Display dataset shape (number of rows and columns)
print(f"Columns in the dataset: {df.shape}")
print("-" * 20)

# 4b. Display the column names
print(f"Columns in the dataset: {list(df.columns)}")
print("-" * 20)

# 4c. Display the data types of each column
print("Data types for each column:")
print(df.dtypes)
print("\n" + "="*40 + "\n")

print("--- 3. STATISTICAL SUMMARY ---")
# 5. Use .describe() to calculate means, std, min, max, and quartiles (25%, 50%, 75%)
# Note: By default, .describe() only processes numerical columns.
print(df.describe())
print("\n" + "="*40 + "\n")

print("--- 4. MISSING VALUES ---")
# 6. Use .isnull().sum() to check for missing values
# .isnull() creates a boolean mask (True for missing, False for present).
# .sum() adds them up (True = 1, False = 0), giving a count of missing items per column.

print(df.isnull().sum())