import pandas as pd

dataset = pd.read_csv('dataset.csv')

# Membersihkan data null dengan metode dropna()
dataset_clean = dataset.dropna()
print(dataset_clean.shape)