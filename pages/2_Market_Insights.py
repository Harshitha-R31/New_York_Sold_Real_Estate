import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_data

st.set_page_config(layout="wide")

df = load_data()

st.title("📈 Market Insights")

# Convert columns to numeric safely
numeric_cols = [
    "sqft",
    "lastSoldPrice",
    "beds",
    "baths"
]

for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

# Remove invalid rows
df = df.dropna(
    subset=[
        "sqft",
        "lastSoldPrice",
        "beds",
        "baths"
    ]
)

# Remove negative/zero values
df = df[
    (df["sqft"] > 0) &
    (df["lastSoldPrice"] > 0) &
    (df["beds"] >= 0) &
    (df["baths"] > 0)
]

tab1, tab2, tab3 = st.tabs(
    [
        "Price Analysis",
        "Size Analysis",
        "Property Types"
    ]
)

# --------------------------
# PRICE ANALYSIS
# --------------------------
with tab1:

    fig = px.histogram(
        df,
        x="lastSoldPrice",
        nbins=50,
        title="Property Price Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# --------------------------
# SIZE ANALYSIS
# --------------------------
with tab2:

    fig = px.scatter(
        df,
        x="sqft",
        y="lastSoldPrice",
        color="beds",
        size="baths",
        hover_data=["city"],
        title="Property Size vs Price"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# --------------------------
# PROPERTY TYPES
# --------------------------
with tab3:

    if "type" in df.columns:

        fig = px.pie(
            df,
            names="type",
            title="Property Type Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:
        st.warning(
            "Property type column not found."
        )
