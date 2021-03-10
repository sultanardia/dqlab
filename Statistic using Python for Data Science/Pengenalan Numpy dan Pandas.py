import pandas as pd 
import numpy as np 

raw_data = pd.read_csv('raw_dataset.csv')

# Metode shape
print(raw_data.shape)
print(raw_data.shape[0])
print('\n')

# Melihat kolom tabel
print(raw_data.columns)
print('\n')

# Metode isna
print(raw_data.isna())
print(raw_data.isna().sum())
print('\n')

# Metode describe
print(raw_data.describe())
print(raw_data.mean())
print(raw_data['Harga'].max())
print('\n')

# Metode sum
print(raw_data.sum())
print(raw_data.sum(numeric_only = True))
print(raw_data[['Harga', 'Pendapatan']].sum())
print('\n')

# Metode loc
print(raw_data[:10]) # Mengambil data dari 0 sampai 10-1
print(raw_data[3:5]) # Mengambil data dari 3 sampai 5-1
print(raw_data.loc[[3,5,10]]) # Mengambil data dari 3, 5 dan 10
print(raw_data[['Harga', 'Pendapatan']][:10]) # Mengambil data harga dan pendapatan dari 0 sampai 10-1
print(raw_data[['Harga', 'Pendapatan']].loc[[3,5,10]]) # Mengambil data harga dan pendapatan dari 3, 5 dan 10