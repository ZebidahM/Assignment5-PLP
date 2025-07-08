# deployment/monitor.py

import pandas as pd
import joblib
from model.metrics import calculate_metrics
from data.preprocess import preprocess_data
from data.feature_engineering import engineer_features
from sklearn.model_selection import train_test_split

def monitor_model(new_data_path="data/new_patient_data.csv"):
    """
    Monitor concept drift by evaluating model on fresh data.
    Compares current performance to baseline metrics.
    """

    # Load and process new data
    df = pd.read_csv(new_data_path)
    df = preprocess_data(df)
    df = engineer_features(df)

    feature_cols = ["age_scaled", "length_of_stay_scaled", "prior_admissions", "med_complexity_score"]
    label_col = "readmitted"

    X = df[feature_cols]
    y = df[label_col]

    # Load model and predict
    model = joblib.load("model/readmission_model.pkl")
    y_pred = model.predict(X)

    # Calculate metrics
    metrics = calculate_metrics(y, y_pred)
    print("📊 Concept Drift Monitor Results:")
    for key, value in metrics.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    monitor_model()
