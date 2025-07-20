# 🎓 Student Final Exam Score Predictor – Streamlit Web App

🚀 **Live App**:  
👉 [https://exam-score-predictor.streamlit.app/](https://exam-score-predictor.streamlit.app/)  
*(Replace this with your actual app URL once deployed)*

✅ **Hosted on**: [Streamlit Cloud](https://streamlit.io/cloud)  
👩‍💻 **Created by**: Komal Sewda

---

## 📌 Project Overview

This interactive web app predicts a student's **final exam score (G3)** using a trained **machine learning model**.  
It allows users to input personal, academic, and family-related information and receive a predicted final score.

The model used is a **Random Forest Regressor**, trained on cleaned student performance data.  
The interface is built with **Streamlit** and includes sliders and radio buttons for intuitive input.

---

## 🧠 Model Details

- **Model Used**: Random Forest Regressor
- **Target Variable**: G3 (Final Grade)
- **Key Features**:
  - G1, G2 (First & Second Period Grades)
  - Number of Past Failures
  - Study Time, Absences
  - School Support, Family Support
  - Paid Classes, Higher Education Desire
  - Parental Education
  - Free Time, Health, Activities, Relationships

---

## 🛠 Built With

- Python
- Streamlit
- scikit-learn (`RandomForestRegressor`)
- pandas, NumPy
- joblib

---

## 🧪 How to Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/komalsewda/your-repo-name.git
cd your-repo-name
