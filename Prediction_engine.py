# Import all required libraries
import pandas as pd
from sklearn.model_selection import train_test_split

# 2. Load a public dataset from a CSV file
# We are using the famous Iris flower dataset via a public raw URL
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# 3. Separate the dataset into Features (X) and Target variables (y)
# Features (X): The inputs (measurements of the flowers)
# Target (y): The output we eventually want to predict (the species of the flower)

X = df.drop(columns=['species'])
y = df['species']

# 5. Split the dataset into 80% Training and 20% Testing data
# 6. Use random_state for reproducible results (it ensures we get the same split every time we run the code)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,   # 20% of the data goes to the set
    random_state=42   # The seed for the random number generator

)

# 7. Print the shapes of the resulting datasets to verify the split
print("--- DATA SPLIT SUMMARY ---")
print(f"Total dataset shape: {df.shape}\n")

# Training data shapes (Features and Target)
print(f"Shape of X_train (Training Features): {X_train.shape}")
print(f"Shape of y_train (Training Target):   {y_train.shape}\n")

# Testing data shapes (Features and Target)
print(f"Shape of X_test (Testing Features):   {X_test.shape}")
print(f"Shape of y_test (Testing Target):     {y_test.shape}")