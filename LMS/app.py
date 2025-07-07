import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('student_score_predictor.pkl')

st.set_page_config(page_title="Student Exam Score Predictor")
st.title("🎓 Student Final Exam Score Predictor (G3)")
st.write("Enter student details below:")

# Input fields
G1 = st.slider("G1 - First Period Grade", 0, 20, 10)
G2 = st.slider("G2 - Second Period Grade", 0, 20, 10)
failures = st.slider("Number of Past Class Failures", 0, 4, 0)
studytime = st.slider("Weekly Study Time (1-4)", 1, 4, 2)
absences = st.slider("Total Absences", 0, 93, 5)

schoolsup = st.radio("School Support", ["yes", "no"])
famsup = st.radio("Family Support", ["yes", "no"])
paid = st.radio("Extra Paid Classes", ["yes", "no"])
higher = st.radio("Wants Higher Education", ["yes", "no"])
romantic = st.radio("In a Romantic Relationship", ["yes", "no"])
activities = st.radio("In Extra-Curricular Activities", ["yes", "no"])

Medu = st.slider("Mother's Education (0=none, 4=Higher)", 0, 4, 2)
Fedu = st.slider("Father's Education (0=none, 4=Higher)", 0, 4, 2)
freetime = st.slider("Free Time after School (1-5)", 1, 5, 3)
health = st.slider("Health Status (1-5)", 1, 5, 3)

# Encode categorical variables
def encode(val):
    return 1 if val == "yes" else 0

input_data = np.array([[
    G1, G2, failures, studytime, absences,
    encode(schoolsup), encode(famsup), encode(paid),
    Medu, Fedu, encode(higher), encode(romantic),
    freetime, health, encode(activities)
]])

# Predict and display result
if st.button("Predict Final Exam Score"):
    prediction = model.predict(input_data)[0]
    st.success(f"🎯 Predicted Final Exam Score (G3): {prediction:.2f}")
