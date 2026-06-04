import pandas as pd
import streamlit as st

@st.cache_data
def load_data():

    df = pd.read_csv(
        "data/ny_real_estate_sold_properties_2026.csv"
    )

    return df
