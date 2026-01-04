# Chạy toàn bộ pipeline

import os

os.system("python src/generate_data.py")
os.system("python src/train_model.py")
os.system("python src/optimize_ratio.py")
