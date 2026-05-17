"""1. INTUITION FIRST
What is a DataFrame?
In simple words, a DataFrame is a digital filing cabinet. It’s a 2D structure where data is organized into rows and columns, much like an Excel Spreadsheet or a SQL Table.

The Excel Comparison: If a Series (a single column) is a single list of names, a DataFrame is the entire sheet containing names, ages, and emails.

The "Why": AI and ML models don't "read" raw text well; they need numbers organized in grids. DataFrames allow us to clean, filter, and transform millions of rows of data in milliseconds—something manual Excel work simply can’t touch.

2. CORE THEORY
The Tabular Engine
Pandas: A library built on top of NumPy. It provides fast, flexible data structures designed to work with structured (tabular) data.

The Anatomy:

Rows: Individual records (e.g., one specific customer).

Columns: Features or attributes (e.g., "Age", "Price").

Index: The "address" of a row (usually starting at 0).

Data Types (dtypes): Pandas assigns types like int64, float64, or object (strings) to ensure mathematical operations are lightning-fast.

Why not plain Python? A Python "list of dictionaries" is slow because Python has to check the type of every single item one by one. Pandas uses vectorization, performing operations on entire columns at once using C-optimized code under the hood.

3. STEP-BY-STEP BREAKDOWN
To get started, you follow a standard workflow:

Import: Bringing the tool into your script.

Creation: Turning raw data (like a dictionary) into a DataFrame object.

Inspection: Using .head() to see the first 5 rows and .info() to see the "health" of your data (missing values, types, etc.)."""


# Practical Code:-
import pandas as pd

# Create a dictionary of data
data = {
    'user_id': [101, 102, 103, 104, 105],
    'policy_type': ['Auto', 'Home', 'Auto', 'Life', 'Home'],
    'safety_score': [88.5, 92.0, 75.2, None, 95.8]
}

# 2. Convert to DataFrame
df = pd.DataFrame(data)

# 3. Inspection
print("---TOP 5 ROWS---")
print(df.head())

print("\n--- DATAFRAME SUMMARY ---")
df.info()


# Explainig the output:-
# Column Type:- user_id is an integer, policy_type is an "object" (string), and safety_score is a float.
# Memory Usages:- .info() shows exactly how many kilobytes(KB) this takes up.
# Null Values:- Notice entry 104 has None. .info() will show "4-non-null" for that columns, alerting you that one value missing

print("--------------------------------------------------------------")

# Mini-Task:-
import pandas as pd

# Task:-1
# 01:- Create the DataFrame
Employee_Data = {
    'emp_id': [20594200, 20594221, 20594222, 20594223],
    'department': ["IT", "Sales", "Marketing", "HR"],
    "salary": [70000, 40000, 35000, 50000]
}

df = pd.DataFrame(Employee_Data)

# Task:- 2
# 02:- Filters rows where department is "sales"
# This create a boolean mask (True/False) and hands it to the DataFrame
sales_df = df[df['department'] == "Sales"].copy()

# Task:- 3
# 03:- Add a new columns 'bonus' (10% of salary)
# Vectorized operation no loops needed!
sales_df['bonus'] = sales_df['salary'] * 0.10

# Task:- 4
# 04:- Add a new columns 'New Salary' after getting the bonus the person who's is sales department
sales_df['New_Salary'] = sales_df['salary'] + sales_df['bonus']

print(sales_df)


"""Let’s dissect this line piece by piece: sales_df = df[df['department'] == "Sales"].copy()

Step 1: The Inner Code (The Question)
Look at the innermost part first: df['department'] == "Sales"

Instead of just checking one thing, Pandas goes down the entire department column and asks a Yes/No question for every single row: "Is this department Sales?"

It generates a "Boolean Mask" (a list of True/False values) behind the scenes that looks exactly like this:

Row 0 (IT) ➔ False

Row 1 (Sales) ➔ True

Row 2 (Marketing) ➔ False

Row 3 (HR) ➔ False

Step 2: The Outer Brackets (The Filter)
Now look at the outer part: df[ ... ]

When you pass that True/False list into the DataFrame's brackets, you are telling Pandas: "Only keep the rows where the answer is True."

It acts like a bouncer at a club. It checks the list, denies entry to IT, Marketing, and HR (False), and only lets the Sales row (True) pass through.

Step 3: .copy() (The Safe Copy)
By default, when you filter a DataFrame in Pandas, it doesn't give you a brand new DataFrame. Instead, it gives you a "view" (like looking at the original data through a window).

If you try to add a new column (like your bonus or New_Salary columns) to a "view", Pandas gets confused and will yell at you with a massive red warning called a SettingWithCopyWarning.

Adding .copy() tells Pandas: "Take these filtered rows and create a completely brand-new, independent DataFrame in the computer's memory." This makes it safe to modify."""


"""Clarifying the Brackets: [[]] vs df[df[...]]
You asked why I mentioned [[]]. In your original code that triggered an error, you wrote: df[["Sales"]]

Here is the difference between how Pandas reads brackets:

1. Double Brackets with a string inside: df[['column_name']]
When Pandas sees a string inside double brackets, it thinks you are asking to select columns.

Example: df[['department', 'salary']] returns a DataFrame with just those two columns.

Why yours failed: When you wrote df[["Sales"]], Pandas searched for a column named "Sales", couldn't find one, and crashed.

2. Nested Brackets with logic inside: df[df['col'] == 'value']
This is what we used in the correct code. It looks like double brackets, but it's actually nested brackets.

The inner bracket df['department'] selects the column to check.

The outer bracket df[...] applies the True/False filter."""