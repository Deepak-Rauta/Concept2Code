"""1. INTUITION FIRST
What is Data Filtering?
Imagine you are a bouncer at an exclusive club. Your job is to look at the line of people (your dataset) and only let in those who meet specific criteria, like being over 21 or being on the VIP list. Everyone else is turned away.

In data science, filtering (or slicing) is exactly this: inspecting a massive spreadsheet and extracting only the rows that meet your specific rules, while hiding or removing the rest.

Why is Filtering Extremely Important in AI/ML?

Garbage In, Garbage Out: AI models learn from data. If your dataset is full of errors, irrelevant records, or outliers, your model will fail. Filtering cleans this up.

Targeted Analytics: You rarely analyze everyone at once. You filter to analyze specific segments (e.g., "users who clicked the checkout button but didn't buy").

Feature Engineering: You often need to isolate specific conditions to create new data points (e.g., flagging any transaction over $10,000 as is_high_risk = True)."""


"""2. CORE THEORY
What is Boolean Indexing in Pandas?
"Boolean" simply means True or False. "Indexing" is the act of selecting data. Therefore, Boolean Indexing is the process of selecting data by asking Pandas a True/False question for every single row.

How Conditions Create True/False Masks
When you apply a condition to a Pandas column (like df['age'] > 18), Pandas doesn't immediately give you a new table. Instead, it generates a Boolean Mask—a hidden list of True and False values corresponding to every row.

How Pandas Filters Rows Internally
You then pass this mask back into the DataFrame using square brackets: df[mask]. Pandas lines up the True/False mask alongside your data. It keeps the rows where the mask is True and drops the rows where the mask is False.

Selecting Specific Columns After Filtering
Once you've filtered down to the right rows, you might only care about a specific piece of information. For example, after finding all users with low safety scores, you might only want their user_id to send them a warning email, rather than their entire profile."""


"""3. STEP-BY-STEP BREAKDOWN
Let’s visualize a Policy Violations DataFrame:

Rows: Each row represents a single event (e.g., one comment posted by a user).

Columns: The attributes of that event (e.g., User ID, the type of policy broken, the safety score given by an AI).

Conditions: The rule we want to enforce (e.g., "Safety score is less than 0.5").

The 3-Step Process:

The Mask: Create the True/False list.
mask = (safety_score < 0.5)

Filtering Rows: Apply the mask to the table.
filtered_table = df[mask]

Selecting Specific Columns: Grab only the column you need.
final_result = filtered_table['user_id']

(Note: In practice, we combine these steps into a single, clean line of code)."""


# Practical Code:-
import pandas as pd

# Create a dataframe with sample records
data = {
    'user_id': ['U101', 'U102', 'U103', 'U104', 'U105'],
    'policy_type': ['Dangerous Content', 'Sexual Explicity', 'Harassment', 'Medical Advice', 'Violance and Gore'],
    'safety_score': [0.2, 0.8, 0.4, 0.1, 0.9]
}
df = pd.DataFrame(data)

print("--- Original DataFrame ---")
print(df)
print("\n")

# 02. Now filter the dataframe where shown only rows where safety_score < 0.5
# EXPLANATION: df['safety_score'] < 0.5 creates the True/False mask.
# Wrapping it in df[...] applies the mask to the DataFrame.
high_risk_rows = df[df['safety_score'] < 0.5]

print("--- Filtered Rows (Score < 0.5) ---")
print(high_risk_rows)
print("\n")

# 03. Select only the user_id column for those filterred rows
# EXPLANATION: We take the filtered DataFrame and specify the ['user_id'] column.
high_risk_users = df[df['safety_score'] < 0.5]['user_id']

print("--- Just the user IDs ---")
print(high_risk_users)


"""7. INTERVIEW QUESTIONS
What is Boolean Indexing?
It is a technique for filtering data by passing a Series or array of boolean values (True or False) to a DataFrame. The DataFrame returns only the rows that correspond to True.

How does Pandas filter rows?
Pandas evaluates a given condition against a column in a vectorized manner (using underlying C code for speed), generating a boolean mask. It then aligns this mask with the DataFrame's index to return the subset of rows.

Difference between .loc and Boolean filtering?
Standard boolean filtering (df[mask]) is great for filtering rows. .loc (df.loc[mask, 'column_name']) is more powerful because it allows you to filter rows and select specific columns in one step, which also prevents "SettingWithCopy" warnings if you intend to modify the data.

Why is filtering important in data analysis?
It allows analysts to handle missing values, remove extreme outliers, segment populations for A/B testing, and prepare highly specific datasets for training machine learning algorithms."""

"""8. MINI PRACTICE TASK
Using the DataFrame from step 4, try writing the code for these 3 exercises.

Exercise 1: Filter rows above a threshold
Find all rows where the safety_score is strictly greater than 0.7.

Expected Output: Rows for U102 and U105."""

import pandas as pd

# Create a dataframe with sample records
data = {
    'user_id': ['U101', 'U102', 'U103', 'U104', 'U105'],
    'policy_type': ['Dangerous Content', 'Sexual Explicity', 'Harassment', 'Medical Advice', 'Violance and Gore'],
    'safety_score': [0.2, 0.8, 0.4, 0.1, 0.9]
}

df = pd.DataFrame(data)

print("--- Original DataFrame ---")
print(df)
print("\n")

# Exercise 1: Filter rows above a threshold
# 01. Filter the data frame where safety_score is strictly greater than 0.7
high_restricted_data = df[df['safety_score'] > 0.7]
print(high_restricted_data)
print("\n")

# Exercise 2: Select multiple columns
# 02. Filter the rows where safety_score is less than 0.3, but return both the user_id and the safety_score columns.

"""Exercise 2: Select multiple columns
Find rows where safety_score is less than 0.3, but return both the user_id and the safety_score columns. (Hint: pass a list of columns [['col1', 'col2']] at the end).

Expected Output: A table with U101 (0.2) and U104 (0.1)."""

multiple_result = df[df['safety_score'] < 0.3][['user_id', 'safety_score']]
print(multiple_result)
print("\n")

"""When you want to select multiple columns in pandas, we have to pass a list of column names inside the selection brackets. So thsi means we need to use the double brackets."""

# The .loc approach
# df.loc[ row_condition , [list_of_columns] ]
multiple_result = df.loc[df['safety_score'] < 0.3, ['user_id', 'safety_score']]

print(multiple_result)

print("--------------------------------------------------------------")

"""Exercise 3: Use multiple conditions
Find rows where the safety_score is less than 0.5 AND the policy_type is exactly 'Spam'.

Expected Output: Rows for U101 and U103."""

# 1. Condition one: (df['safety_score'] < 0.5)
# 2. Condition two: (df['policy_type'] == 'Sexual Explicity')
# Combine with & and wrap the whole thing inside df

multi_condition = df[(df['safety_score'] < 0.5) & (df['policy_type'] == "Sexual Explicity")]

print(multi_condition)








