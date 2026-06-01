
"""1. INTUITION FIRST
What is Logistic Regression?
In the simplest terms, Logistic Regression is a mathematical algorithm that sorts data into two buckets. Instead of predicting a specific number (like a price or a temperature), it predicts the probability that an item belongs to a specific category.

The Misleading Name
The term "regression" is notoriously confusing here. In machine learning, regression usually means predicting continuous numbers (like predicting a house will cost $305,000). Logistic Regression, however, is definitively a classification algorithm. It is called "regression" purely for historical, statistical reasons: it fits a linear regression model to the logarithm of the odds of an event occurring. Despite the name, its final job is to classify data.

Why It Matters
Logistic Regression is incredibly fast, highly interpretable, and mathematically robust. It doesn't act like a "black box"—it tells you exactly why it made a decision by showing you the importance of each feature. Furthermore, a single neuron in a neural network using a sigmoid activation function is mathematically identical to Logistic Regression. Mastering this means you are laying the foundation for deep learning.

2. CORE THEORYBinary ClassificationBinary classification is any problem where there are exactly two possible outcomes. Examples include True/False, Yes/No, or Spam/Not Spam.  Target Labels (0 and 1)We represent these two outcomes mathematically as 0 and 1.0 represents the "Negative Class" (e.g., Safe, Not Spam, Healthy).1 represents the "Positive Class" (e.g., Dangerous, Spam, Sick)

Predicting ProbabilitiesUnlike algorithms that simply draw a hard line and output a 0 or a 1, Logistic Regression outputs a probability percentage between 0.0 and 1.0. For example, it might output 0.82, meaning "there is an 82% probability this data point belongs to class 1."  The Sigmoid FunctionTo ensure our model only outputs numbers between 0 and 1, we pass our data through a mathematical filter called the Sigmoid Function. It creates a smooth, S-shaped curve.


$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

No matter how large or small the input number ($z$) is, the Sigmoid function squashes it perfectly into a range between 0 and 1.  

Decision BoundariesOnce we have a probability, we need to make a final choice. The decision boundary is the threshold we set to convert the probability into a final 0 or 1. The default threshold is usually 0.5 (50%).

Converting Probabilities to Classes:-
If Output >= 0.5: Classify as 1
If Output < 0.5: Classify as """

# Practical Code:-
# 01. Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# 02. Create a simple dataset
# 0 = safe, 1 = dangerous

data = {
    'safety_score': [0.95, 0.90, 0.85, 0.70, 0.60, 0.45, 0.30, 0.20, 0.10, 0.05],
    'is_dangerous': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
}

# 03. Create the dataframe
df = pd.DataFrame(data)

# 04. Separate the feature(X) and target (y)
# X must be a 2D array/DataFrame
X = df[['safety_score']]
y = df['is_dangerous']

# 05. Split data into training (70%) and testing (30%) sets
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.3,
                                                    random_state=42)
# 06. Train the Logistic Regression Model 
model = LogisticRegression()
model.fit(X_train, y_train)

# 07. Predict on new, queries
# When we trained our Logistic Regression model earlier, we gave it a pandas DataFrame (which is just Python's version of an Excel spreadsheet). That spreadsheet had a specific column header named safety_score.

# Because the model learned by looking at a spreadsheet with a specific column name, it expects all future questions to be asked in the exact same format.

new_queries = pd.DataFrame({'safety_score': [0.88, 0.25, 0.55]})
prediction = model.predict(new_queries)
# predict_proba (The Confidence Meter)
probabilities = model.predict_proba(new_queries)

# Display the results
print("New Queries (Safety_Scores): \n", new_queries['safety_score'].values)
print("\nPredicted Classes (0=safe, 1=Dangerous): \n", prediction)
print("\nPredicted Probabilities [Prob of 0, Prob of 1]: \n", np.round(probabilities))




