# Huấn luyện mô hình AI

import pandas as pd
from sklearn.ensemble import RandomForestRegressor # Mô hình AI
from sklearn.model_selection import train_test_split # Chia train/test
from sklearn.metrics import r2_score # Đánh giá mô hình (phương sai)
import joblib # Lưu mô hình

# Load data
data = pd.read_csv("data/experiments.csv")

X = data[["mud_ratio", "carbon_ratio", "temperature", "time"]]
y = data["no2_efficiency"]

# Chia tập train/test (80% học – 20% kiểm tra)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Khởi tạo mô hình (300 cây)
model = RandomForestRegressor(
    n_estimators=300,
    random_state=42
)

# Huấn luyện mô hình
model.fit(X_train, y_train)

# Đánh giá
pred = model.predict(X_test)
print("R² score:", r2_score(y_test, pred))

# Lưu mô hình
joblib.dump(model, "models/rf_model.pkl")
print("Model saved to models/rf_model.pkl")
