import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_data

st.set_page_config(layout="wide")

df = load_data()

st.title("🧠 AI Property Recommendations")

st.markdown(
    "Get smart property recommendations based on your budget and preferences."
)

# User Inputs
budget = st.slider(
    "Budget ($)",
    int(df["lastSoldPrice"].min()),
    int(df["lastSoldPrice"].max()),
    500000
)

min_beds = st.selectbox(
    "Minimum Bedrooms",
    sorted(df["beds"].dropna().unique())
)

min_baths = st.selectbox(
    "Minimum Bathrooms",
    sorted(df["baths"].dropna().unique())
)

# Filter
recommended = df[
    (df["lastSoldPrice"] <= budget) &
    (df["beds"] >= min_beds) &
    (df["baths"] >= min_baths)
].copy()

# Investment Score Algorithm
recommended["investment_score"] = (
      recommended["sqft"] * 0.4
    + recommended["beds"] * 50
    + recommended["baths"] * 40
    - recommended["lastSoldPrice"] / 10000
)

recommended = recommended.sort_values(
    by="investment_score",
    ascending=False
)

top10 = recommended.head(10)

# KPIs
col1, col2, col3 = st.columns(3)

col1.metric(
    "Matching Properties",
    len(recommended)
)

col2.metric(
    "Best Investment Score",
    round(top10["investment_score"].max(), 2)
)

col3.metric(
    "Average Price",
    f"${top10['lastSoldPrice'].mean():,.0f}"
)

st.divider()

# Recommendation Table
st.subheader("🏆 Top Recommended Properties")

st.dataframe(
    top10[
        [
            "city",
            "beds",
            "baths",
            "sqft",
            "lastSoldPrice",
            "investment_score"
        ]
    ],
    use_container_width=True
)

# Visualization
fig = px.bar(
    top10,
    x="city",
    y="investment_score",
    color="lastSoldPrice",
    hover_data=["sqft"],
    title="Top Investment Opportunities"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# AI Insights
st.subheader("📈 Smart Insights")

if len(top10) > 0:

    best_city = (
        top10.groupby("city")["investment_score"]
        .mean()
        .idxmax()
    )

    st.success(
        f"Best city for investment currently: {best_city}"
    )

    avg_price = top10["lastSoldPrice"].mean()

    st.info(
        f"Average recommended property price: ${avg_price:,.0f}"
    )

    largest_property = top10.loc[
        top10["sqft"].idxmax()
    ]

    st.write(
        f"""
        Largest property recommendation:
        
        📍 City: {largest_property['city']}
        
        🏠 Size: {largest_property['sqft']:,.0f} sqft
        
        💰 Price: ${largest_property['lastSoldPrice']:,.0f}
        """
    )

else:
    st.warning(
        "No properties match your criteria."
    )

# Export Recommendations
csv = top10.to_csv(index=False)

st.download_button(
    "📥 Download Recommendations",
    csv,
    "recommended_properties.csv",
    "text/csv"
)
