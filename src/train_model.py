# Huấn luyện mô hình AI

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import joblib

# Load data
data = pd.read_csv("data/experiments.csv")

X = data[["mud_ratio", "carbon_ratio", "temperature", "time"]]
y = data["no2_efficiency"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(
    n_estimators=300,
    random_state=42
)

model.fit(X_train, y_train)

pred = model.predict(X_test)
print("R² score:", r2_score(y_test, pred))

joblib.dump(model, "models/rf_model.pkl")
print("Model saved to models/rf_model.pkl")
