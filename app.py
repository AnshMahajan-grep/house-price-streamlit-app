import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

# Load pipeline
@st.cache_resource
def load_pipeline():
    return joblib.load('./models/pipeline.pkl')

pipe = load_pipeline()

# ---- Sidebar Inputs ----
st.sidebar.header("Enter House Details for Single Prediction")
bedrooms = st.sidebar.number_input('Bedrooms', min_value=0, max_value=20, value=3)
bathrooms = st.sidebar.number_input('Bathrooms', min_value=0.0, max_value=10.0, value=2.0, step=0.25)
sqft_living = st.sidebar.number_input('Living Area (sqft)', min_value=100, max_value=10000, value=1800)
sqft_lot = st.sidebar.number_input('Lot Area (sqft)', min_value=100, max_value=100000, value=5000)
floors = st.sidebar.number_input('Floors', min_value=1.0, max_value=4.0, value=1.0, step=0.5)
waterfront = st.sidebar.selectbox('Waterfront', options=[0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
view = st.sidebar.slider('View Quality (0-4)', min_value=0, max_value=4, value=0)
condition = st.sidebar.slider('Condition (1-5)', min_value=1, max_value=5, value=3)
sqft_above = st.sidebar.number_input('Sqft Above Ground', min_value=0, max_value=10000, value=1500)
sqft_basement = st.sidebar.number_input('Sqft Basement', min_value=0, max_value=5000, value=300)
house_age = st.sidebar.number_input('House Age', min_value=0, max_value=200, value=20)
has_been_renovated = st.sidebar.selectbox('Has Been Renovated?', options=[0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')

# ---- Main App ----
st.title("🏠 House Price Prediction App")
st.write("Predict house prices instantly! Enter features in the sidebar or upload a CSV for batch predictions.")

# --- Single Prediction ---
input_dict = {
    'bedrooms': bedrooms,
    'bathrooms': bathrooms,
    'sqft_living': sqft_living,
    'sqft_lot': sqft_lot,
    'floors': floors,
    'waterfront': waterfront,
    'view': view,
    'condition': condition,
    'sqft_above': sqft_above,
    'sqft_basement': sqft_basement,
    'house_age': house_age,
    'has_been_renovated': has_been_renovated
}
input_df = pd.DataFrame([input_dict])

if st.button('Predict Single House Price'):
    try:
        pred = pipe.predict(input_df)[0]
        st.success(f"Estimated House Price: ${pred:,.0f}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")

# --- Batch Prediction ---
st.header("Batch Prediction")
uploaded_file = st.file_uploader("Upload CSV file with house features for batch prediction", type="csv")
expected_cols = list(input_dict.keys())
if uploaded_file:
    try:
        batch_df = pd.read_csv(uploaded_file)
        if list(batch_df.columns) != expected_cols:
            st.error(f"CSV columns must match: {expected_cols}")
        batch_preds = pipe.predict(batch_df)
        st.write("Batch Predictions (first 10):")
        st.dataframe(pd.DataFrame({
            "Predicted Price": batch_preds
        }).head(10))
        # Download button
        result_df = batch_df.copy()
        result_df['Predicted Price'] = batch_preds
        csv = result_df.to_csv(index=False)
        st.download_button("Download All Predictions as CSV", csv, file_name="batch_predictions.csv")
        # Interactive plot
        st.subheader("Predicted Price Distribution")
        fig, ax = plt.subplots()
        ax.hist(batch_preds, bins=30, color='skyblue')
        ax.set_xlabel("Predicted Price")
        ax.set_ylabel("Count")
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Batch prediction failed: {e}")

st.write("---")
st.caption("Powered by Streamlit and scikit-learn | All-in-one demo app")

