# 01 Import all required libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

# 02 Create a sample dataset for predicting continous numerical values
# We are predicting Salary (Continous) based on Years of Experience.

data = {
    'YearsExperience': [1.1, 1.5, 2.0, 3.2, 4.0, 4.5, 5.5, 6.0, 7.1, 8.2, 9.0, 10.5],
    'Salary': [39343, 46205, 43750, 54445, 60150, 61111, 83088, 93940, 98273, 113812, 105582, 122391]
 
}

# Convert the dictionary into a pandas DataFrame (a 2D table of data)
df = pd.DataFrame(data)

# 03 Separate the dataset into features (X) and Target values (y)
# X must be a 2D array/DataFrame because scikit-learn expect multiple features
X = df[['YearsExperience']]

# y is a 1D array/series because we are predicting a single target
y = df['Salary']

# 4. Split the dataset into 80% Training data and 20% Testing data
# random_state ensures we get the exact same split every time we run the code
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.20,
                                                    random_state=42)

# 5. Import and initialize the Linear Regression model
model = LinearRegression()

# 6. Train the Linear Regression model (The "Learning" Phase)
# The model looks at X_train and y_train to figure out the mathematical relationship
model.fit(X_train, y_train)

# 7. Make predictions (The "Testing" Phase)
# We ask the model to guess the salaries for the X_test data it hasn't seen yet
y_pred = model.predict(X_test)

# 8. Print Predicted values, Actual values, and Model Accuracy Metrics
print("--- Linear Regression Result ---")
print("\n1. Comparison:")
# Zip the actual and predicted values together to print them nicely
for actual, predicted in zip(y_test, y_pred):
    print(f"  Actual Salary: ${actual:.2f} | Predicted Salary: ${predicted:,.2f}")

print("\n2. Model Accuracy Matrics:")
# Mean Absolute Error (MAE): The average magnitude of errors in a set of predictions
mae = mean_absolute_error(y_test, y_pred)
print(f"   Mean  Absolute Error (MAE): {mae:,.2f}")

# Mean Squared Error(MSE) Averages the squares of the errors (penalizes larger errors)
mse = mean_squared_error(y_test, y_pred)
print(f"   Mean Squared Error (MSE):  {mse:,.2f}")

# R² Score: How well the independent variables explain the variance of the dependent variable (1.0 is perfect)
r2 = r2_score(y_test, y_pred)
print(f"   R-squared (R²) Score:      {r2:.4f}")

# Optional: Visualize the result to see the "Line of Best Fit"
plt.scatter(X, y, color='blue', label='Actual Data Points')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Linear Regression Line')
plt.title('Years of Experience vs Salary')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend()
plt.show()
