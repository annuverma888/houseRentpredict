# import streamlit as st
# st.title("Predict bp ")
# age = st.number_input("Enter your age  (in years):",min_value=0, max_value=100, value=0)
# weight = st.number_input("Enter your weight (in kg):")
# if st.button("Predict")


import streamlit as st
import joblib
import category_encoders as ce
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
st.title("House Rent Prediction")
model = joblib.load('house_rent_prediction.pkl')

BHK = st.number_input("Enter the number of BHK:", min_value=1, max_value=10, value=1)
Size = st.number_input("Enter the size of the house (in sq. ft.):", min_value=100, max_value=10000, value=500)
Area_Type = st.selectbox("Select the area type:", ['Super Area', 'Carpet Area', 'Built Area'])
City = st.selectbox("Select the city:", ['Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata'])
Furnishing_Status = st.selectbox("Select the furnishing status:", ['Unfurnished', 'Semi-Furnished', 'Furnished'])
Tenant_Preferred = st.selectbox("Select the tenant preferred:", ['Family', 'Bachelors', 'Any'])
Bathroom = st.number_input("Enter the number of bathrooms:", min_value=1, max_value=10, value=1)
Point_of_Contact = st.selectbox("Select the point of contact:", ['Contact Owner', 'Contact Agent', 'Contact Builder'])  

input = pd.DataFrame({
    'BHK':[BHK],
    'Size':[Size],
    'Area Type':[Area_Type],
    'City':[City],
    'Furnishing Status':[Furnishing_Status],
    'Tenant Preferred':[Tenant_Preferred],
    'Bathroom':[Bathroom],
    'Point of Contact':[Point_of_Contact]
})
if st.button("Predict Rent"):
    prediction = model.predict(input)[0]

    # Agar negative value aaye to 0 kar do (optional)
    prediction = max(0, prediction)

    st.success(f"🏠 Predicted House Rent: ₹{prediction:,.0f} per month")