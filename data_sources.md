# 🧬 Data Sources for Hospital Readmission Risk Prediction

This file outlines the assumed data inputs used for modeling hospital readmission risk. As real patient data is sensitive and protected, we base this project on structured synthetic inputs.

---

## ✅ Primary Data Sources

### 1. Electronic Health Records (EHR)
- Patient age, gender, diagnosis codes
- Admission and discharge dates
- Comorbidities and procedures

### 2. Demographic & Socioeconomic Data
- Zip code or region
- Insurance status
- Income and education brackets (optional enrichment)

### 3. Medication Logs
- Lists of prescribed medications during hospitalization
- Frequency and complexity of regimens

### 4. Admission History
- Historical admission dates over the past 12 months
- Number of prior admissions within that timeframe

---

## 🧪 Data Assumptions

- All patient data is de-identified before processing.
- Admission dates are comma-separated strings (e.g., `2022-01-15,2022-05-08`).
- Medications are stored as semicolon-separated strings (`medA;medB;medC`).
- Age and length_of_stay are numeric fields; some may require normalization.

---

## ⚠️ Ethical Note

This project simulates data to explore technical workflows and ethical strategies, but in real deployments:
- Informed consent must be obtained for all data usage.
- Compliance with health data laws (e.g., HIPAA, POPIA) is essential.
