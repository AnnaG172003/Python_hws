import numpy as np
from sklearn.datasets import load_wine
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
# Load sheet
wine = load_wine()
X = wine.data               # feature analysis attributes
y = wine.target             # labels 
#  Split data 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
# Logistic Regression
model = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=500)
model.fit(X_train, y_train)
#  Predictions 
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)
# Evaluation (got it from lab 115 just changed it to be wine)
print("=== Model Parameters ===")
print("Weights (w):")
print(model.coef_)
print("Bias (b):", model.intercept_)
print()

print("=== Predictions ===")
print("Test predictions:", y_test_pred)
print("True labels:     ", y_test)
print()

print("=== Performance ===")
print("Train Accuracy:", round(accuracy_score(y_train, y_train_pred), 3))
print("Test Accuracy:", round(accuracy_score(y_test, y_test_pred), 3))
print()
print("Confusion Matrix:\n", confusion_matrix(y_test, y_test_pred))
print()
print("Classification Report:\n", classification_report(y_test, y_test_pred, target_names=wine.target_names))