import numpy as np
import pandas as pd

np.random.seed(42)

samples = 50
data = []

for _ in range(samples):
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
        + np.random.normal(0, 2)
    )

    efficiency = max(30, min(95, efficiency))

    data.append([mud, carbon, temp, time, efficiency])

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

df.to_csv("data/experiments.csv", index=False)
print("Generated data/experiments.csv")
