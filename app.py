import streamlit as st
import numpy as np
import pandas as pd
import joblib

st.set_page_config(page_title="Customer Churn Prediction", layout="centered")

st.title("📊 Customer Churn Prediction App")
st.write("Predict whether a customer will churn or not.")

# Load model
try:
    model = joblib.load("rf_model.pkl")
except:
    st.error("Model file not found.")
    st.stop()

st.subheader("Enter Customer Details")

age = st.number_input("Age", 18, 100, 30)
gender = st.selectbox("Gender", ["Female", "Male"])
is_senior = st.selectbox("Senior Citizen", ["No", "Yes"])
tenure = st.number_input("Tenure (Months)", 0, 120, 12)
usage = st.number_input("Avg Monthly Usage (GB)", 0.0, 1000.0, 50.0)
tickets = st.number_input("Support Tickets (Last 6 Months)", 0, 50, 1)
monthly_charges = st.number_input("Monthly Charges", 0.0, 500.0, 50.0)
delay_ratio = st.number_input("Payment Delay Ratio", 0.0, 1.0, 0.1)

internet = st.selectbox("Has Internet Service", ["No", "Yes"])
streaming = st.selectbox("Has Streaming Service", ["No", "Yes"])
device_protection = st.selectbox("Has Device Protection", ["No", "Yes"])

contract = st.selectbox("Contract Type",
                        ["Month-to-month", "One year", "Two year"])

if st.button("Predict"):

    # Binary Encoding
    gender_male = 1 if gender == "Male" else 0
    is_senior_citizen = 1 if is_senior == "Yes" else 0
    has_internet_service = 1 if internet == "Yes" else 0
    has_streaming_service = 1 if streaming == "Yes" else 0
    has_device_protection = 1 if device_protection == "Yes" else 0

    contract_month_to_month = 1 if contract == "Month-to-month" else 0
    contract_one_year = 1 if contract == "One year" else 0
    contract_two_year = 1 if contract == "Two year" else 0

    avg_charge_per_gb = monthly_charges / usage if usage > 0 else 0
    high_support_contact = 1 if tickets > 5 else 0
    long_term_customer = 1 if tenure > 24 else 0
    engagement_score = usage * tenure / 100

    input_data = pd.DataFrame([{
        'age': age,
        'gender_male': gender_male,
        'is_senior_citizen': is_senior_citizen,
        'tenure_months': tenure,
        'avg_monthly_usage_gb': usage,
        'support_tickets_last_6m': tickets,
        'monthly_charges': monthly_charges,
        'payment_delay_ratio': delay_ratio,
        'has_internet_service': has_internet_service,
        'has_streaming_service': has_streaming_service,
        'has_device_protection': has_device_protection,
        'contract_month_to_month': contract_month_to_month,
        'contract_one_year': contract_one_year,
        'contract_two_year': contract_two_year,
        'avg_charge_per_gb': avg_charge_per_gb,
        'high_support_contact': high_support_contact,
        'long_term_customer': long_term_customer,
        'engagement_score': engagement_score
    }])

    probability = model.predict_proba(input_data)[0][1]
    prediction = 1 if probability > 0.35 else 0

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ Customer is likely to churn")
    else:
        st.success("✅ Customer is not likely to churn")

    st.write(f"Churn Probability: {probability:.2f}")