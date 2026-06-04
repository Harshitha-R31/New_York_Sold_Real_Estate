import streamlit as st
from utils.ml_model import train_model

model = train_model()

st.title("🤖 Property Price Predictor")

sqft = st.number_input(
    "Square Feet",
    value=2000
)

beds = st.number_input(
    "Bedrooms",
    value=3
)

baths = st.number_input(
    "Bathrooms",
    value=2
)

if st.button("Predict Price"):

    prediction = model.predict(
        [[sqft,beds,baths]]
    )[0]

    st.success(
        f"Predicted Property Price: ${prediction:,.0f}"
    )
