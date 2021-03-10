import pandas as pd

dataset = pd.read_csv('dataset.csv')

print('Checking missing value for each feature:')
print(dataset.isnull().sum())

print('Checking missing total value:')
print(dataset.isnull().sum().sum())