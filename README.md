# Predicting Hospital Readmission Risk Using AI

This project implements a machine learning model to predict the likelihood of a patient being readmitted within 30 days of discharge. It demonstrates the complete AI Development Workflow—from problem definition to deployment—while emphasizing ethical integrity and practical applications in healthcare.

---

## 🚀 Objectives

- Accurately identify patients at high risk for readmission.
- Support hospital decision-making and resource allocation.
- Develop a transparent and ethical AI model suitable for clinical use.

---

## 📊 Data Sources

- Electronic Health Records (EHR)
- Patient demographics and socioeconomic indicators
- Admission and medication history  
*(Note: This project uses synthetic data to simulate real-world conditions.)*

---

## 🧠 Workflow Overview

1. Problem Definition  
2. Data Collection & Preprocessing  
3. Feature Engineering  
4. Model Development & Evaluation  
5. Deployment via API  
6. Monitoring & Compliance Strategy  

---

## 📁 Project Structure

HospitalReadmissionAI/ ├── data/ │ ├── preprocess.py │ ├── feature_engineering.py │ └── data_sources.md ├── model/ │ ├── train.py │ ├── evaluate.py │ ├── config.yaml │ ├── metrics.py ├── deployment/ │ ├── api.py │ ├── monitor.py │ └── compliance_notes.md ├── utils/ │ ├── helpers.py │ └── logger.py ├── notebook/ │ └── exploratory_analysis.ipynb ├── docs/ │ ├── Submission.pdf │ ├── AI_Workflow_Diagram.png │ └── references.md ├── requirements.txt ├── .gitignore └── README.md

---

## 🧪 Model Details

- **Type:** Logistic Regression
- **Features Used:**  
  - Scaled age  
  - Scaled length of stay  
  - Prior admissions  
  - Medication complexity score
- **Metrics Evaluated:**  
  - Precision  
  - Recall  
  - F1 Score  
  - Confusion Matrix

---

## 🔐 Ethical & Regulatory Compliance

- Data de-identification and encryption standards applied.
- Alignment with HIPAA (USA) and POPIA (South Africa).
- Bias mitigation strategies outlined in `compliance_notes.md`.
- Human oversight emphasized in model interpretation.

---

## 🚀 Running the Project

### 1. 📦 Install Dependencies
```bash
pip install -r requirements.txt
2. 📊 Train the Model
bash
python model/train.py
3. 🧪 Evaluate the Model
bash
python model/evaluate.py
4. 🌐 Launch the API
bash
python deployment/api.py
5. 🔁 Monitor Performance Drift
bash
python deployment/monitor.py
🔍 API Usage
Endpoint: /predict Method: POST Request Payload (JSON):
json
{
  "age": 65,
  "length_of_stay": 5,
  "admission_dates": "2022-02-15,2022-05-10",
  "medications": "medA;medB;medC"
}
Response:
json
{
  "readmission_risk": 1
}
📚 References
Please see docs/references.md for sources including:
•	HIPAA & POPIA compliance frameworks
•	Fairness auditing tools (Fairlearn)
•	CRISP-DM methodology
•	PLP Academy lecture notes
💬 Contributors
Created by [Your Name / Group Name]. Feel free to submit feedback or fork the repo for educational use!

