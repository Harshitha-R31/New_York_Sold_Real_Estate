import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

df = load_data()

st.title("📊 Executive Dashboard")

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Total Properties",
    len(df)
)

col2.metric(
    "Average Sold Price",
    f"${df['lastSoldPrice'].mean():,.0f}"
)

col3.metric(
    "Highest Sale",
    f"${df['lastSoldPrice'].max():,.0f}"
)

col4.metric(
    "Average SqFt",
    f"{df['sqft'].mean():,.0f}"
)

st.divider()

city_sales = (
    df.groupby("city")["lastSoldPrice"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

fig = px.bar(
    city_sales,
    title="Top Cities by Average Sale Price"
)

st.plotly_chart(fig,use_container_width=True)

fig2 = px.pie(
    df,
    names="sold_vs_asking",
    title="Sold vs Asking"
)

st.plotly_chart(fig2,use_container_width=True)
