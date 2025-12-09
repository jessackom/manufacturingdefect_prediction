import streamlit as st
import os
import requests

# Load secrets from the environment variables
# These variables come from the TOML configuration you just entered
DATABRICKS_HOST = os.environ.get("DATABRICKS_HOST")
DATABRICKS_TOKEN = os.environ.get("DATABRICKS_TOKEN")
MLFLOW_URL = os.environ.get("MLFLOW_URL")

st.set_page_config(page_title="Manufacturing Defect Prediction")
st.title("🏭 Manufacturing Defect Prediction")

st.write("Enter the required parameters to predict a manufacturing defect.")

# --- Input Fields ---
# Add your specific input fields here
param1 = st.slider("Parameter 1", 0.0, 100.0, 50.0)
param2 = st.selectbox("Parameter 2", ["A", "B", "C"])

# --- Prediction Logic ---
if st.button("Predict Defect"):
    # 1. Prepare the data payload for your MLflow endpoint
    # You will need to customize this structure based on your model's input
    payload = {
        "dataframe_split": {
            "columns": ["param1", "param2"],
            "data": [[param1, param2]]
        }
    }
    
    # 2. Set up headers for Databricks/MLflow API call
    headers = {
        "Authorization": f"Bearer {DATABRICKS_TOKEN}",
        "Content-Type": "application/json"
    }

    # 3. Make the request to the MLflow Model Serving Endpoint
    try:
        with st.spinner('Making prediction...'):
            response = requests.post(MLFLOW_URL, headers=headers, json=payload)
            response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
            
            prediction = response.json().get('predictions', [None])[0]
            
            if prediction is not None:
                st.success(f"Prediction successful! Predicted Value: {prediction}")
            else:
                st.error("Prediction failed or returned an unexpected format.")
                
    except requests.exceptions.HTTPError as e:
        st.error(f"HTTP Error: Could not get prediction. Check your MLflow URL and Token. Details: {e}")
    except requests.exceptions.RequestException as e:
        st.error(f"Network Error: Could not connect to the MLflow endpoint. Details: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")

# Display the configured URL (for debugging)
# st.caption(f"MLflow Endpoint: {MLFLOW_URL}")
