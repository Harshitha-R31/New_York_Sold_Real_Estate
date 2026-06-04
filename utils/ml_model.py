import pandas as pd
import joblib

from sklearn.ensemble import RandomForestRegressor

from sklearn.model_selection import (
    train_test_split
)

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


MODEL_PATH = "models/price_predictor.pkl"


def train_model():

    df = pd.read_csv(
        "data/ny_real_estate_sold_properties_2026.csv"
    )

    features = [
        "sqft",
        "beds",
        "baths"
    ]

    X = df[features].fillna(0)

    y = df["lastSoldPrice"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=300,
        max_depth=15,
        random_state=42
    )

    model.fit(
        X_train,
        y_train
    )

    predictions = model.predict(
        X_test
    )

    metrics = {

        "MAE":
            mean_absolute_error(
                y_test,
                predictions
            ),

        "RMSE":
            mean_squared_error(
                y_test,
                predictions
            ) ** 0.5,

        "R2":
            r2_score(
                y_test,
                predictions
            )
    }

    joblib.dump(
        model,
        MODEL_PATH
    )

    return model, metrics


def load_model():

    return joblib.load(
        MODEL_PATH
    )


def predict_price(
    sqft,
    beds,
    baths
):

    model = load_model()

    prediction = model.predict(
        [[
            sqft,
            beds,
            baths
        ]]
    )[0]

    return prediction


def feature_importance():

    model = load_model()

    features = [
        "sqft",
        "beds",
        "baths"
    ]

    importance = model.feature_importances_

    importance_df = pd.DataFrame({

        "Feature": features,
        "Importance": importance

    }).sort_values(
        by="Importance",
        ascending=False
    )

    return importance_df
