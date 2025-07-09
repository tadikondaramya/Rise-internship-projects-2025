# Step 1: Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve

# Step 2: Load dataset (replace with your actual file)
# Example synthetic data (you can replace with your own CSV)
data = pd.DataFrame({
    'Age': [25, 32, np.nan, 45, 35, 28, 40],
    'Income': [50000, 60000, 55000, np.nan, 72000, 40000, 80000],
    'Education': ['Graduate', 'Not Graduate', 'Graduate', 'Graduate', 'Not Graduate', 'Graduate', 'Graduate'],
    'CreditScore': [700, 680, 690, 710, 720, 600, np.nan],
    'LoanApproved': ['Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes']
})

# Step 3: Preprocessing
# Handle missing values
imputer = SimpleImputer(strategy='mean')
data[['Age', 'Income', 'CreditScore']] = imputer.fit_transform(data[['Age', 'Income', 'CreditScore']])

# Encode categorical variables
le_edu = LabelEncoder()
data['Education'] = le_edu.fit_transform(data['Education'])  # Graduate=1, Not Graduate=0

le_target = LabelEncoder()
data['LoanApproved'] = le_target.fit_transform(data['LoanApproved'])  # Yes=1, No=0

# Step 4: Split data
X = data.drop('LoanApproved', axis=1)
y = data['LoanApproved']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train models
# Logistic Regression
log_model = LogisticRegression()
log_model.fit(X_train, y_train)
log_pred = log_model.predict(X_test)
log_prob = log_model.predict_proba(X_test)[:, 1]

# Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)
rf_prob = rf_model.predict_proba(X_test)[:, 1]

# Step 6: Evaluation
def evaluate_model(name, y_true, y_pred, y_prob):
    print(f"\n=== {name} ===")
    print("Confusion Matrix:")
    print(confusion_matrix(y_true, y_pred))
    print("Classification Report:")
    print(classification_report(y_true, y_pred))
    auc = roc_auc_score(y_true, y_prob)
    print(f"ROC-AUC Score: {auc:.2f}")
    
    fpr, tpr, _ = roc_curve(y_true, y_prob)
    plt.plot(fpr, tpr, label=f"{name} (AUC = {auc:.2f})")

evaluate_model("Logistic Regression", y_test, log_pred, log_prob)
evaluate_model("Random Forest", y_test, rf_pred, rf_prob)

# Step 7: ROC Curve
plt.plot([0, 1], [0, 1], 'k--')
plt.title("ROC Curve Comparison")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
