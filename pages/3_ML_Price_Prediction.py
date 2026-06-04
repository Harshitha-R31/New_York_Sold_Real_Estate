import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(
    page_title="ML Price Prediction",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Property Price Prediction")

MODEL_PATH = "models/price_predictor.pkl"

# Check if model exists
if not os.path.exists(MODEL_PATH):
    st.error(
        "Model file not found. Please run train_model.py first."
    )
    st.stop()

# Load model
try:
    model = joblib.load(MODEL_PATH)

except Exception as e:
    st.error(
        f"Error loading model: {e}"
    )
    st.stop()

st.markdown(
    "Predict property prices based on size, bedrooms and bathrooms."
)

col1, col2, col3 = st.columns(3)

with col1:
    sqft = st.number_input(
        "Square Feet",
        min_value=100,
        max_value=20000,
        value=1500,
        step=100
    )

with col2:
    beds = st.number_input(
        "Bedrooms",
        min_value=1,
        max_value=20,
        value=3
    )

with col3:
    baths = st.number_input(
        "Bathrooms",
        min_value=1,
        max_value=20,
        value=2
    )

st.divider()

if st.button("🔮 Predict Property Price"):

    try:

        input_data = pd.DataFrame(
            [[sqft, beds, baths]],
            columns=[
                "sqft",
                "beds",
                "baths"
            ]
        )

        prediction = model.predict(
            input_data
        )[0]

        st.success(
            f"Estimated Property Price: ${prediction:,.0f}"
        )

    except Exception as e:

        st.error(
            f"Prediction Error: {e}"
        )

st.divider()

st.subheader("📊 About This Model")

st.info(
    """
    This machine learning model predicts property sale prices
    using:

    • Square Feet

    • Number of Bedrooms

    • Number of Bathrooms

    Model: Random Forest Regressor
    """
)
