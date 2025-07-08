# This script loads your trained model and test set, then computes metrics like precision, recall, F1 score, and confusion matrix.
python
# model/evaluate.py

import pandas as pd
import joblib
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix
from sklearn.model_selection import train_test_split
from data.preprocess import preprocess_data
from data.feature_engineering import engineer_features

def evaluate_model(file_path="data/patient_data.csv"):
    """
    Evaluate the trained model using precision, recall, F1, and confusion matrix.
    """

    # Load dataset
    df = pd.read_csv(file_path)
    df = preprocess_data(df)
    df = engineer_features(df)

    feature_cols = ["age_scaled", "length_of_stay_scaled", "prior_admissions", "med_complexity_score"]
    label_col = "readmitted"

    X = df[feature_cols]
    y = df[label_col]

    # Split same way as training
    _, X_test, _, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Load trained model
    model = joblib.load("model/readmission_model.pkl")

    # Predict
    y_pred = model.predict(X_test)

    # Metrics
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    print(f"Precision: {precision:.2f}")
    print(f"Recall:    {recall:.2f}")
    print(f"F1 Score:  {f1:.2f}")
    print("Confusion Matrix:")
    print(cm)

if __name__ == "__main__":
    evaluate_model()
