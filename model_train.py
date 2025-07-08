# This script trains a Logistic Regression model using your preprocessed and feature-engineered dataset. It also saves the trained model using joblib for future use in deployment.
python
# model_train.py

import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from data.preprocess import preprocess_data
from data.feature_engineering import engineer_features

def train_model(file_path="data/patient_data.csv"):
    """
    Train a logistic regression model to predict hospital readmission.
    Saves model to 'model/readmission_model.pkl'.
    """

    # Load dataset
    df = pd.read_csv(file_path)

    # Apply preprocessing and feature engineering
    df = preprocess_data(df)
    df = engineer_features(df)

    # Features and label selection
    feature_cols = ["age_scaled", "length_of_stay_scaled", "prior_admissions", "med_complexity_score"]
    label_col = "readmitted"  # Binary target column

    X = df[feature_cols]
    y = df[label_col]

    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Train logistic regression model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Save the trained model
    joblib.dump(model, "model/readmission_model.pkl")

    print("✅ Model trained and saved to model/readmission_model.pkl")

if __name__ == "__main__":
    train_model()
