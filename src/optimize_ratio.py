# Tìm tỉ lệ phối trộn tối ưu bằng mô hình AI (đã sửa warning feature names)

import numpy as np
import pandas as pd
import joblib

# Load mô hình đã huấn luyện
model = joblib.load("models/rf_model.pkl")

best_efficiency = -1
best_config = None

# Quét tỉ lệ bùn đỏ từ 10% → 80%
for mud in np.linspace(10, 80, 71):
    carbon = 100 - mud

    # Giữ cố định điều kiện công nghệ (có thể thay sau)
    temperature = 600
    time = 2

    # ✅ Đưa dữ liệu dự đoán về DataFrame có TÊN CỘT
    X_pred = pd.DataFrame(
        [[mud, carbon, temperature, time]],
        columns=["mud_ratio", "carbon_ratio", "temperature", "time"]
    )

    # Dự đoán hiệu suất NO2
    predicted_eff = model.predict(X_pred)[0]

    # Cập nhật cấu hình tốt nhất
    if predicted_eff > best_efficiency:
        best_efficiency = predicted_eff
        best_config = (mud, carbon, temperature, time)

# In kết quả
print("🔍 TỈ LỆ TỐI ƯU DỰ ĐOÁN:")
print(f"  Bùn đỏ: {best_config[0]:.1f}%")
print(f"  Than hoạt tính: {best_config[1]:.1f}%")
print(f"  Nhiệt độ nung: {best_config[2]} °C")
print(f"  Thời gian nung: {best_config[3]} giờ")
print(f"  Hiệu suất NO₂ dự đoán: {best_efficiency:.2f}%")
