# Tìm tỉ lệ phối trộn tối ưu bằng AI

import numpy as np
import joblib

model = joblib.load("models/rf_model.pkl")

best_eff = 0
best_config = None

for mud in np.linspace(10, 80, 71):
    carbon = 100 - mud
    temp = 600
    time = 2

    pred = model.predict([[mud, carbon, temp, time]])[0]

    if pred > best_eff:
        best_eff = pred
        best_config = (mud, carbon, temp, time)

print("  TỈ LỆ TỐI ƯU DỰ ĐOÁN:")
print(f"  Bùn đỏ: {best_config[0]:.1f}%")
print(f"  Than hoạt tính: {best_config[1]:.1f}%")
print(f"  Nhiệt độ nung: {best_config[2]} °C")
print(f"  Thời gian nung: {best_config[3]} giờ")
print(f"  Hiệu suất NO₂ dự đoán: {best_eff:.2f}%")
