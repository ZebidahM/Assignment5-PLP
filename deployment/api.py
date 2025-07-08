# deployment/api.py

from flask import Flask, request, jsonify
import joblib
import pandas as pd
from data.preprocess import preprocess_data
from data.feature_engineering import engineer_features

app = Flask(__name__)
model = joblib.load("model/readmission_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse incoming JSON into DataFrame
        input_data = pd.DataFrame([request.json])

        # Apply preprocessing and feature engineering
        input_data = preprocess_data(input_data)
        input_data = engineer_features(input_data)

        # Extract required features
        features = ["age_scaled", "length_of_stay_scaled", "prior_admissions", "med_complexity_score"]
        input_data = input_data[features]

        # Make prediction
        prediction = model.predict(input_data)[0]
        response = {"readmission_risk": int(prediction)}
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
