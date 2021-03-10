import pandas as pd 

dataset = pd.read_csv('dataset.csv')

# Missing value handling menggunakan metode imputasi
dataset.fillna(dataset.mean(), inplace = True)

print(dataset.isnull().sum())
