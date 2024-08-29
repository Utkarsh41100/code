import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import joblib

# Load dataset
# Replace 'your_dataset.csv' with your dataset file path
data = pd.read_csv('your_dataset.csv')

# Feature selection (example features)
features = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService', 
            'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 
            'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 
            'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges']
X = data[features]
y = data['Churn']

# Preprocessing pipeline
categorical_features = ['gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 
                        'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 
                        'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 
                        'PaperlessBilling', 'PaymentMethod']
numeric_features = ['SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(), categorical_features)])

# Model pipeline
model_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                                 ('classifier', RandomForestClassifier(random_state=42))])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model training
model_pipeline.fit(X_train, y_train)

# Save the trained model
joblib.dump(model_pipeline, 'churn_model.pkl')

# Function to make predictions based on user input
def predict_churn(model, user_input):
    user_df = pd.DataFrame([user_input], columns=features)
    prediction = model.predict(user_df)
    return 'Churn' if prediction[0] else 'Not Churn'

# Load the trained model
model = joblib.load('churn_model.pkl')

# User input
user_input = {
    'gender': input("Enter gender (Male/Female): "),
    'SeniorCitizen': int(input("Enter if senior citizen (1 for Yes, 0 for No): ")),
    'Partner': input("Enter if has partner (Yes/No): "),
    'Dependents': input("Enter if has dependents (Yes/No): "),
    'tenure': float(input("Enter tenure in months: ")),
    'PhoneService': input("Enter if has phone service (Yes/No): "),
    'MultipleLines': input("Enter if has multiple lines (Yes/No/No phone service): "),
    'InternetService': input("Enter type of internet service (DSL/Fiber optic/No): "),
    'OnlineSecurity': input("Enter if has online security (Yes/No/No internet service): "),
    'OnlineBackup': input("Enter if has online backup (Yes/No/No internet service): "),
    'DeviceProtection': input("Enter if has device protection (Yes/No/No internet service): "),
    'TechSupport': input("Enter if has tech support (Yes/No/No internet service): "),
    'StreamingTV': input("Enter if has streaming TV (Yes/No/No internet service): "),
    'StreamingMovies': input("Enter if has streaming movies (Yes/No/No internet service): "),
    'Contract': input("Enter type of contract (Month-to-month/One year/Two year): "),
    'PaperlessBilling': input("Enter if has paperless billing (Yes/No): "),
    'PaymentMethod': input("Enter payment method (Electronic check/Mailed check/Bank transfer/Direct debit): "),
    'MonthlyCharges': float(input("Enter monthly charges: ")),
    'TotalCharges': float(input("Enter total charges: "))
}

# Predict churn
churn_prediction = predict_churn(model, user_input)
print(f'The prediction is: {churn_prediction}')
