import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_data

st.set_page_config(layout="wide")

df = load_data()

st.title("🔍 Property Explorer")
st.markdown("Explore properties using advanced filters.")

# Sidebar Filters
st.sidebar.header("Filters")

city_options = sorted(df["city"].dropna().unique())

selected_cities = st.sidebar.multiselect(
    "Select City",
    city_options,
    default=city_options[:5]
)

price_range = st.sidebar.slider(
    "Property Price ($)",
    int(df["lastSoldPrice"].min()),
    int(df["lastSoldPrice"].max()),
    (
        int(df["lastSoldPrice"].min()),
        int(df["lastSoldPrice"].max())
    )
)

bedroom_range = st.sidebar.slider(
    "Bedrooms",
    int(df["beds"].min()),
    int(df["beds"].max()),
    (
        int(df["beds"].min()),
        int(df["beds"].max())
    )
)

bathroom_range = st.sidebar.slider(
    "Bathrooms",
    int(df["baths"].min()),
    int(df["baths"].max()),
    (
        int(df["baths"].min()),
        int(df["baths"].max())
    )
)

# Filtering
filtered_df = df.copy()

if selected_cities:
    filtered_df = filtered_df[
        filtered_df["city"].isin(selected_cities)
    ]

filtered_df = filtered_df[
    (filtered_df["lastSoldPrice"] >= price_range[0]) &
    (filtered_df["lastSoldPrice"] <= price_range[1]) &
    (filtered_df["beds"] >= bedroom_range[0]) &
    (filtered_df["beds"] <= bedroom_range[1]) &
    (filtered_df["baths"] >= bathroom_range[0]) &
    (filtered_df["baths"] <= bathroom_range[1])
]

# KPIs
col1, col2, col3 = st.columns(3)

col1.metric(
    "Properties Found",
    len(filtered_df)
)

col2.metric(
    "Average Price",
    f"${filtered_df['lastSoldPrice'].mean():,.0f}"
)

col3.metric(
    "Average SqFt",
    f"{filtered_df['sqft'].mean():,.0f}"
)

st.divider()

# Scatter Plot
fig = px.scatter(
    filtered_df,
    x="sqft",
    y="lastSoldPrice",
    color="beds",
    size="baths",
    hover_data=["city"],
    title="Property Size vs Price"
)

st.plotly_chart(fig, use_container_width=True)

# Data Table
st.subheader("Filtered Properties")

st.dataframe(
    filtered_df,
    use_container_width=True
)

# Download
csv = filtered_df.to_csv(index=False)

st.download_button(
    "📥 Download Filtered Data",
    csv,
    "filtered_properties.csv",
    "text/csv"
)
