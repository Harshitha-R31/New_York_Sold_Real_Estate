import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

df = load_data()

st.title("📈 Market Insights")

tab1,tab2,tab3 = st.tabs([
    "Price Analysis",
    "Size Analysis",
    "Property Types"
])

with tab1:

    fig = px.histogram(
        df,
        x="lastSoldPrice",
        nbins=50
    )

    st.plotly_chart(fig,use_container_width=True)

with tab2:

    fig = px.scatter(
        df,
        x="sqft",
        y="lastSoldPrice",
        color="beds",
        size="baths"
    )

    st.plotly_chart(fig,use_container_width=True)

with tab3:

    fig = px.sunburst(
        df,
        path=["type","city"],
        values="lastSoldPrice"
    )

    st.plotly_chart(fig,use_container_width=True)
