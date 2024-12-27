import pickle
import streamlit as st
import pandas as pd
import numpy as np



pipe = pickle.load(open("pipeline.pkl","rb"))
X = pickle.load(open("X.pkl","rb"))

st.title("tata sales")

CustomerID = st.selectbox("CustomerID",X["CustomerID"].unique()).astype("int32")
Quantity_log = st.selectbox("Quantity",X["Quantity_log"].unique()).astype("int32")
UnitPrice_log = st.selectbox("UnitPrice",X["UnitPrice_log"].unique()).astype("int32")
Day = st.selectbox("Day",X["Day"].unique()).astype("int32")
Month = st.selectbox("Month",X["Month"].unique()).astype("int32")
Year = st.selectbox("Year",X["Year"].unique()).astype("int32")

if st.button("Predict Sales"):+
    # Create a DataFrame using the selected values
    query = pd.DataFrame([[CustomerID, Quantity_log, UnitPrice_log, Day, Month, Year]],
                         columns=["CustomerID", "Quantity_log", "UnitPrice_log", "Day", "Month", "Year"])

    # Use the pipeline to predict
    prediction = pipe.predict(query)

    # Display the prediction
    st.title(f"Predicted Sales: {prediction[0]}")
