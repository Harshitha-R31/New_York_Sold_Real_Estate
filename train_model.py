import pandas as pd
import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Load dataset
df = pd.read_csv(
    "data/ny_real_estate_sold_properties_2026.csv"
)

# Features
X = df[
    [
        "sqft",
        "beds",
        "baths"
    ]
].fillna(0)

# Target
y = df["lastSoldPrice"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestRegressor(
    n_estimators=300,
    random_state=42
)

model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)

score = r2_score(
    y_test,
    predictions
)

print(f"R² Score: {score:.4f}")

# Save model
joblib.dump(
    model,
    "models/price_predictor.pkl"
)

print("Model saved successfully!")
