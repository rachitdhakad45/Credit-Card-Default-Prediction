import streamlit as st
import joblib
from datetime import date
from dateutil.relativedelta import relativedelta

# Load trained model
model = joblib.load("models/credit_default_gradient_boosting_model.joblib")

# Load feature names
feature_names = joblib.load("models/feature_names.joblib")

st.title("Credit Card Default Prediction")

from datetime import date

# Get the current month
current_date = date.today()

# Generate labels for the last 6 months
months = []
year = current_date.year
month = current_date.month

for _ in range(6):
    months.append(date(year, month, 1).strftime("%B %Y"))
    
    month -= 1
    if month == 0:
        month = 12
        year -= 1


# Customer Information
st.header("Customer Information")

col1, col2 = st.columns(2)

with col1:
    limit_bal = st.number_input(
        "Credit Limit",
        min_value=0,
        value=50000,
        step=5000
    )

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=30,
        step=1
    )

    sex = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

with col2:
    education = st.selectbox(
        "Education",
        [
            "Graduate School",
            "University",
            "High School",
            "Others"
        ]
    )

    marriage = st.selectbox(
        "Marital Status",
        [
            "Married",
            "Single",
            "Others"
        ]
    )

# Payment History
st.header("Payment History")

st.write("Select the repayment status for each of the last 6 months.")

pay_options = {
    "No consumption": -2,
    "Paid on time": -1,
    "No delay": 0,
    "1 month delay": 1,
    "2 months delay": 2,
    "3 months delay": 3,
    "4 months delay": 4,
    "5 months delay": 5,
    "6 months delay": 6,
    "7 months delay": 7,
    "8 months delay": 8,
    "9+ months delay": 9
}

col1, col2, col3 = st.columns(3)

with col1:
    pay_0 = st.selectbox(months[0], list(pay_options.keys()))
    pay_2 = st.selectbox(months[1], list(pay_options.keys()))

with col2:
    pay_3 = st.selectbox(months[2], list(pay_options.keys()))
    pay_4 = st.selectbox(months[3], list(pay_options.keys()))

with col3:
    pay_5 = st.selectbox(months[4], list(pay_options.keys()))
    pay_6 = st.selectbox(months[5], list(pay_options.keys()))

# Bill Amounts
st.header("Monthly Bill Amounts")

st.write("Enter the bill amount for each of the last 6 months.")

col1, col2, col3 = st.columns(3)

with col1:
    bill_amt1 = st.number_input(
        "September Bill",
        min_value=0,
        value=20000,
        step=1000
    )

    bill_amt4 = st.number_input(
        "June Bill",
        min_value=0,
        value=20000,
        step=1000
    )

with col2:
    bill_amt2 = st.number_input(
        "August Bill",
        min_value=0,
        value=20000,
        step=1000
    )

    bill_amt5 = st.number_input(
        "May Bill",
        min_value=0,
        value=20000,
        step=1000
    )

with col3:
    bill_amt3 = st.number_input(
        "July Bill",
        min_value=0,
        value=20000,
        step=1000
    )

    bill_amt6 = st.number_input(
        "April Bill",
        min_value=0,
        value=20000,
        step=1000
    )

# Previous Payment Amounts
st.header("Previous Payment Amounts")

st.write("Enter the payment amount made in each of the last 6 months.")

col1, col2, col3 = st.columns(3)

with col1:
    pay_amt1 = st.number_input(
        "September Payment",
        min_value=0,
        value=2000,
        step=500
    )

    pay_amt4 = st.number_input(
        "June Payment",
        min_value=0,
        value=2000,
        step=500
    )

with col2:
    pay_amt2 = st.number_input(
        "August Payment",
        min_value=0,
        value=2000,
        step=500
    )

    pay_amt5 = st.number_input(
        "May Payment",
        min_value=0,
        value=2000,
        step=500
    )

with col3:
    pay_amt3 = st.number_input(
        "July Payment",
        min_value=0,
        value=2000,
        step=500
    )

    pay_amt6 = st.number_input(
        "April Payment",
        min_value=0,
        value=2000,
        step=500
    )

# Prepare input for the model
input_data = {
    "LIMIT_BAL": limit_bal,
    "SEX": 1 if sex == "Male" else 2,
    "EDUCATION": {
        "Graduate School": 1,
        "University": 2,
        "High School": 3,
        "Others": 4
    }[education],
    "MARRIAGE": {
        "Married": 1,
        "Single": 2,
        "Others": 3
    }[marriage],

    "AGE": age,

    "PAY_0": pay_options[pay_0],
    "PAY_2": pay_options[pay_2],
    "PAY_3": pay_options[pay_3],
    "PAY_4": pay_options[pay_4],
    "PAY_5": pay_options[pay_5],
    "PAY_6": pay_options[pay_6],

    "BILL_AMT1": bill_amt1,
    "BILL_AMT2": bill_amt2,
    "BILL_AMT3": bill_amt3,
    "BILL_AMT4": bill_amt4,
    "BILL_AMT5": bill_amt5,
    "BILL_AMT6": bill_amt6,

    "PAY_AMT1": pay_amt1,
    "PAY_AMT2": pay_amt2,
    "PAY_AMT3": pay_amt3,
    "PAY_AMT4": pay_amt4,
    "PAY_AMT5": pay_amt5,
    "PAY_AMT6": pay_amt6
}

import pandas as pd


# Convert input dictionary into a DataFrame
input_df = pd.DataFrame([input_data])

# Make sure the columns are in the exact order used during training
input_df = input_df[feature_names]


# Prediction button
if st.button("Predict Default Risk", type="primary"):

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    st.divider()
    st.header("Prediction Result")

    probability_percent = probability * 100

    # Determine risk level
    if probability_percent < 30:
        risk_level = "Low Risk"
    elif probability_percent < 60:
        risk_level = "Medium Risk"
    else:
        risk_level = "High Risk"

    # Display prediction
    if prediction == 1:
        st.error("⚠️ Customer is likely to default")
    else:
        st.success("✅ Customer is unlikely to default")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Default Probability",
            f"{probability_percent:.2f}%"
        )

    with col2:
        st.metric(
            "Risk Level",
            risk_level
        )

    st.info(
        "The result shows how likely the customer is to miss their upcoming "
        "credit card payment. A higher percentage means higher default risk. "
    )

