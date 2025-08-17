# Employee-Attrition-Prediction-using-ML 🚀
📌 Project Overview

Employee attrition (also known as employee turnover) is one of the major challenges faced by organizations. High attrition rates can lead to increased costs, reduced productivity, and disruptions in team dynamics.

This project aims to:

Analyze employee data

Identify key factors contributing to attrition

Build a machine learning model to predict whether an employee is likely to leave the company

Deploy the model as a Streamlit web app for easy usage

📊 Business Use Case

Employee Retention: Identify at-risk employees before they leave

Data-driven Decisions: HR teams can use insights to improve workplace satisfaction

Cost Reduction: Save on rehiring and retraining costs

🛠️ Tech Stack

Python 3.10+

Pandas, NumPy – Data processing

Matplotlib, Seaborn – Data visualization

Scikit-learn – Machine learning model

🔎 Exploratory Data Analysis (EDA)

In the notebook:

Distribution of employees based on Job Satisfaction, Work-Life Balance, Income

Correlation analysis to identify important features

Visualization of attrition rates across departments, age groups, and overtime work

🤖 Model Development

Trained using classification algorithms (e.g., Logistic Regression, Random Forest, etc.)

Evaluated using metrics like Accuracy, Precision, Recall, F1-score

Final trained model saved as final_model.pkl

🌐 Streamlit App

The app provides an interactive interface for HR teams:

Input Features:

Age

Daily Rate

Distance from Home

Hourly Rate

Monthly Income

Monthly Rate

Over Time (0 = No, 1 = Yes)

Total Working Years

Years at Company

Output:

Prediction: Yes / No → Whether the employee is likely to leave
Streamlit – Model deployment

Pickle – Model saving/loading
