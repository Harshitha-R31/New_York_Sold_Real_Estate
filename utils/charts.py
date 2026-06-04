import plotly.express as px
import plotly.graph_objects as go


def price_distribution(df):

    fig = px.histogram(
        df,
        x="lastSoldPrice",
        nbins=50,
        title="Property Price Distribution"
    )

    fig.update_layout(
        xaxis_title="Price ($)",
        yaxis_title="Count"
    )

    return fig


def sqft_vs_price(df):

    fig = px.scatter(
        df,
        x="sqft",
        y="lastSoldPrice",
        color="beds",
        size="baths",
        hover_data=["city"],
        title="Square Feet vs Property Price"
    )

    return fig


def city_average_prices(df):

    city_prices = (
        df.groupby("city")["lastSoldPrice"]
        .mean()
        .sort_values(ascending=False)
        .head(15)
        .reset_index()
    )

    fig = px.bar(
        city_prices,
        x="city",
        y="lastSoldPrice",
        title="Top Cities by Average Sale Price"
    )

    return fig


def beds_price_chart(df):

    fig = px.box(
        df,
        x="beds",
        y="lastSoldPrice",
        title="Bedrooms vs Property Price"
    )

    return fig


def property_type_chart(df):

    fig = px.pie(
        df,
        names="type",
        title="Property Type Distribution"
    )

    return fig


def investment_score_chart(df):

    fig = px.bar(
        df.head(10),
        x="city",
        y="investment_score",
        color="lastSoldPrice",
        title="Top Investment Opportunities"
    )

    return fig


def heatmap_correlation(df):

    corr = df.select_dtypes(
        include="number"
    ).corr()

    fig = px.imshow(
        corr,
        text_auto=True,
        title="Correlation Heatmap"
    )

    return fig


def price_trend_by_city(df):

    city_avg = (
        df.groupby("city")["lastSoldPrice"]
        .mean()
        .sort_values(ascending=False)
        .head(20)
        .reset_index()
    )

    fig = px.line(
        city_avg,
        x="city",
        y="lastSoldPrice",
        markers=True,
        title="Average Property Prices by City"
    )

    return fig
