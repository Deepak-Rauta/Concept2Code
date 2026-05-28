"""Why do we split the data?
If we train a model on all our available data and then evaluate it on that exact same data, the model might just memorize the answers (a problem called overfitting). To know if the model can generalize—meaning it can make accurate predictions on data it has never seen before—we must hide a portion of the data during the learning phase."""

"""The Beginner-Friendly Dictionary
Training Data: The "study material." This is the large chunk of data (usually 70-80%) that the model uses to find patterns and rules.

Testing Data: The "final exam." This is the remaining data (20-30%) kept entirely secret from the model until the very end to test its true performance.

train_test_split: A Scikit-learn utility function that randomly shuffles our dataset and slices it into the training and testing sets. Randomization ensures both sets accurately represent the overall data.

fit(): The learning action. When you call model.fit(X_train, y_train), you are telling the algorithm: "Here are the features (X) and the correct answers (y). Figure out the mathematical relationship between them."

predict(): The testing action. Once trained, you pass the hidden features to model.predict(X_test). The model outputs its best guesses, which we then compare against the actual hidden answers."""


"""2. The Implementation
Here is the complete, well-commented Python script using the classic Iris dataset. It applies a Logistic Regression model to classify iris flower species based on their petal and sepal measurements."""

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# ----------------------------------------------------------------
# Step:-01 Load teh Dataset
# ----------------------------------------------------------------
# Loading the Iris dataset
iris = load_iris()

# Converting to a Pandas dataframe for cleaner handling and viewing
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target

# ----------------------------------------------------------------
# Step 2: Separate Features (X) and Target Labels (y)
# ----------------------------------------------------------------
# X contain the data we use to make prediction
X = df.drop(columns=['species'])

# y contains the actual answers we want to predict (flower type)
y = df['species']

# ----------------------------------------------------------------
# Step:- 03 Split the Data
# ----------------------------------------------------------------
# We reserve 20% of the data for testing, 80% for training.
# random_state=42 acts as a seed so we get the exact same split every time we run the code.
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.20,
                                                    random_state=42)

# ----------------------------------------------------------------
# Step 4: Initialize and Train the Model (The fit API)
# ----------------------------------------------------------------
# Instantiating a Logistic Regression model (max_iter increased to ensure it converges)
model = LogisticRegression(max_iter=200)

# Training the model - it is learning the patterns here!
model.fit(X_train, y_train)

# ----------------------------------------------------------------
# Step 5: Make Predictions (The predict API)
# ----------------------------------------------------------------
# Asking the trained model to guess the species for our hidden test data
y_pred = model.predict(X_test)

# ---------------------------------------------------------
# Step 6: Evaluate and Print Results
# ---------------------------------------------------------
# Calculate the accuracy score (Percentage of correct predictions)
accuracy = accuracy_score(y_test, y_pred)

print("---- DATA SHAPE ---")
print(f"Training data shape (X_train): {X_train.shape}")
print(f"Testing data shape (X_test): {X_test.shape}\n")

print("--- PREDICTION RESULTS ---")
# Converting arrays to lists for a cleaner print output
print(f"Predicted values: {y_pred.tolist()}")
print(f"Actual values: {list(y_test.tolist())}\n")

print("--- PERFORMANCE ---")
# Formatting the accuracy as a percentage
print(f"Accuracy Score: {accuracy * 100:.2f}%")













