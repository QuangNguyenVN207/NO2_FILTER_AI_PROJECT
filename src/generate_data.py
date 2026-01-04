# Tạo số liệu để train mô hình

import numpy as np
import pandas as pd

# Cố định seed (giúp mỗi lần chạy cho số liệu như nhau)
np.random.seed(42)

# Lặp tạo dữ liệu
samples = 50
data = []

for _ in range(samples):
    # Bùn đỏ từ 10–80%. Phần trăm Than hoạt tính, nhiệt độ, thời gian
    mud = np.random.uniform(10, 80)
    carbon = 100 - mud
    temp = np.random.choice([400, 500, 600, 700])
    time = np.random.choice([1, 2, 3])

    # Hàm giả lập hiệu suất (giả sử tối ưu gần 40% bùn – 60% than)
    efficiency = (
        90
        - abs(mud - 40) * 0.5
        + (temp - 400) * 0.03
        + time * 2
        + np.random.normal(0, 2) # Sai số thí nghiệm
    )

    efficiency = max(30, min(95, efficiency)) # Không có hiệu suất >100% hay <0%

    data.append([mud, carbon, temp, time, efficiency])

# Tạo DataFrame (tạo bảng dữ liệu)
df = pd.DataFrame(
    data,
    columns=[
        "mud_ratio",
        "carbon_ratio",
        "temperature",
        "time",
        "no2_efficiency"
    ]
)

# Ghi ra file .csv (Lưu dữ liệu cho AI học)
df.to_csv("data/experiments.csv", index=False)
print("Generated data/experiments.csv")
