
import pandas as pd
import numpy as np
import streamlit as st
import pickle

# Load trained model
with open(r"D:\guvi\Projects\.venv\project_3_Emp_Attrition\final_model.pkl", "rb") as f:
    final_model = pickle.load(f)

# Load encoder
with open(r"D:\guvi\Projects\.venv\project_3_Emp_Attrition\attrition_encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

def prediction_of_attrition(user_df):
    new_df = user_df.copy()

    for col in user_df.columns:
        if col in encoder:
            new_df[col] = encoder[col].transform(user_df[col])

    # Make prediction
    prediction = final_model.predict(new_df)

    return int(prediction[0])


def main():
    
    st.title("🧑‍💼 Employee Attrition Prediction ")


    # Collect user input

    age = st.number_input("Age", min_value=18, max_value=100, step=1)
    environmentsatisfaction = st.number_input("Environment Satisfaction", min_value=1, max_value=4, step=1)
    jobinvolvement = st.number_input("Job Involvement", min_value=1, max_value=4, step=1)
    joblevel = st.number_input("Job Level", min_value=1, max_value=5, step=1)
    jobsatisfaction = st.number_input("Job Satisfaction", min_value=1, max_value=4, step=1)
    maritalstatus = st.selectbox("Marital Status", ["Married", "Single", "Divorced"])
    monthlyincome = st.number_input("Monthly Income", min_value=1000, max_value=25000, step=100)
    overtime = st.selectbox("Over Time", ["No", "Yes"])
    stockoptionlevel = st.number_input("Stock Option Level", min_value=0, max_value=3, step=1)
    totalworkingyears = st.number_input("Total Working Years", min_value=0, max_value=30, step=1)
    yearsatcompany = st.number_input("Years at Company", min_value=0, max_value=30, step=1)
    yearsincurrentrole = st.number_input("Years in Current Role", min_value=0, max_value=30, step=1)
    yearswithcurrmanager = st.number_input("Years with Current Manager", min_value=0, max_value=30, step=1)

    # Create DataFrame for inputs

    user_df = pd.DataFrame({
        "age": [age],
        "environmentsatisfaction": [environmentsatisfaction],
        "jobinvolvement": [jobinvolvement],
        "joblevel": [joblevel],
        "jobsatisfaction": [jobsatisfaction],
        "maritalstatus": [maritalstatus],
        "monthlyincome": [monthlyincome],
        "overtime": [overtime],
        "stockoptionlevel": [stockoptionlevel],
        "totalworkingyears": [totalworkingyears],
        "yearsatcompany": [yearsatcompany],
        "yearsincurrentrole": [yearsincurrentrole],
        "yearswithcurrmanager": [yearswithcurrmanager]
    })

    # Predict on button click

    if st.button("Predict"):
        result = prediction_of_attrition(user_df)
        output = "Yes" if result == 1 else "No"
        st.success(f"The Attrition prediction is: {output}")


if __name__ == '__main__':
    main()
