import pandas as pd
import streamlit as st
import os

@st.cache_data
def load_data():

    file_path = "data/ny_real_estate_sold_properties_2026.csv"

    st.write("Looking for:", file_path)

    st.write("File exists:", os.path.exists(file_path))

    st.write(
        "File size:",
        os.path.getsize(file_path)
        if os.path.exists(file_path)
        else "Not Found"
    )

    df = pd.read_csv(file_path)

    return df
