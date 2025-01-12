import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

# Load dataset
data = pd.read_csv('nim_dataset.csv')

# Split dataset into features and target variable
X = data[['points']]
y = data['move']

# Train a decision tree model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save the trained model
joblib.dump(model, 'model.pkl')