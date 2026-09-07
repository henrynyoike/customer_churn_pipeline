import matplotlib.pyplot as plt
from data import DataCleaner , DataLoader
import os
from pathlib import Path

project_dir = Path(__file__).resolve().parent.parent
data_dir = os.path.join(project_dir , "data")
file_dir = os.path.join(data_dir , "WA_Fn-UseC_-Telco-Customer-Churn.csv")

print(file_dir)
loader = DataLoader(file_dir)
data = loader.load()

cleaner = DataCleaner(data)
data = cleaner.clean()

plt.show()


