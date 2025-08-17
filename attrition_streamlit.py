import pandas as pd
import numpy as np
import streamlit as st
import pickle

pickle_in = open(r"D:\guvi\Projects\.venv\project_3_Emp_Attrition\final_model.pkl","rb")
final_model = pickle.load(pickle_in)

def prediction_of_attrition(age,dailyrate,distancefromhome,hourlyrate,monthlyincome,monthlyrate,overtime,totalworkingyears,yearsatcompany):
    prediction = final_model.predict([[age,dailyrate,distancefromhome,hourlyrate,monthlyincome,monthlyrate,overtime,totalworkingyears,yearsatcompany]])
    print(prediction)
    return prediction

def main():
    st.title("Employee Attrition")

    age	= st.number_input("Age",min_value=18, max_value=100, step = 1)
    dailyrate = st.number_input("Daily Rate",min_value=100, max_value=2000, step = 10)
    distancefromhome = st.number_input("Distance from home",min_value=0, max_value=28, step = 1)
    hourlyrate = st.number_input("Hourly Rate",min_value=10, max_value=150, step = 1)
    monthlyincome = st.number_input("Monthly Income",min_value=1000, max_value=25000, step = 100)
    monthlyrate = st.number_input("Monthly Rate",min_value=1000, max_value=30000, step = 100)
    overtime = st.number_input("Over Time",min_value=0, max_value=1, step = 1)
    totalworkingyears = st.number_input("Total Working Years",min_value=0, max_value=30, step = 1)
    yearsatcompany = st.number_input("Years at Company",min_value=0, max_value=30, step = 1)

    result = ""

    if st.button("Predict"):
        result = prediction_of_attrition(age,dailyrate,distancefromhome,hourlyrate,monthlyincome,monthlyrate,overtime,
                                         totalworkingyears,yearsatcompany)
    output = "Yes" if result == 1 else "No"
    st.success(f"The Attrition prediction is {output}")

if __name__ == '__main__':
    main()