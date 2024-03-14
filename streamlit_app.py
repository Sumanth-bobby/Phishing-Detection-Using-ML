import streamlit as st
import requests

st.title("Phishing Site Checker")

# Input box for the URL
url_input = st.text_input("Enter a URL:")
if st.button("Check"):
    try:
        # Send the URL to Flask app for prediction
        response = requests.get("http://localhost:5000/predict", params={'feature': url_input})

        if response.status_code == 200:
            result = response.json().get('result')
            if result is not None:
                st.success(f"Prediction: {result}")
            else:
                st.error("Error: Result not received from Flask app.")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"Error predicting the URL: {str(e)}")
