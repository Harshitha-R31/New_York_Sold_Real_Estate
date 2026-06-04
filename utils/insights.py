import pandas as pd


def generate_market_insights(df):

    insights = []

    avg_price = df["lastSoldPrice"].mean()

    max_price = df["lastSoldPrice"].max()

    min_price = df["lastSoldPrice"].min()

    avg_sqft = df["sqft"].mean()

    insights.append(
        f"Average property price is ${avg_price:,.0f}"
    )

    insights.append(
        f"Highest property sold for ${max_price:,.0f}"
    )

    insights.append(
        f"Lowest property sold for ${min_price:,.0f}"
    )

    insights.append(
        f"Average property size is {avg_sqft:,.0f} sqft"
    )

    return insights


def top_city(df):

    city = (
        df.groupby("city")["lastSoldPrice"]
        .mean()
        .idxmax()
    )

    return city


def best_investment_city(df):

    if "investment_score" not in df.columns:
        return "Not Available"

    city = (
        df.groupby("city")["investment_score"]
        .mean()
        .idxmax()
    )

    return city


def investment_score(df):

    df["investment_score"] = (
        df["sqft"] * 0.4
        + df["beds"] * 50
        + df["baths"] * 40
        - df["lastSoldPrice"] / 10000
    )

    return df


def generate_recommendation(df):

    city = top_city(df)

    return (
        f"Based on average sale prices, "
        f"{city} appears to be the strongest market."
    )


def market_summary(df):

    summary = {
        "total_properties": len(df),
        "avg_price": round(df["lastSoldPrice"].mean(), 2),
        "avg_sqft": round(df["sqft"].mean(), 2),
        "max_price": df["lastSoldPrice"].max(),
        "min_price": df["lastSoldPrice"].min()
    }

    return summary
