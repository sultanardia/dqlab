import pandas as pd 
import numpy as np 

raw_data = pd.read_csv('raw_dataset.csv')

produk_A = raw_data[raw_data['Produk'] == 'A'] # Mengambil produk A

# Mean
print(produk_A['Pendapatan'].mean())
print(np.mean(produk_A['Pendapatan'])) # Menggunakan numpy
print('\n')

# Median
print(produk_A['Pendapatan'].median())
print(np.median(produk_A['Pendapatan'])) # Menggunakan numpy
print('\n')

# Melihat jumlah dari masing-masing produk
print(raw_data['Produk'].value_counts())
print(raw_data['Produk'].mode())
print('\n')

# Kuantil
print(raw_data['Pendapatan'].quantile(q = 0.5))
print(raw_data['Pendapatan'].quantile([0.25, 0.75]))
print(np.quantile(raw_data['Pendapatan'], q = 0.5)) # Menggunakan numpy
print('\n')

# Metode agg
print(raw_data[['Pendapatan', 'Harga']].agg([np.mean, np.median])) # Menghitung mean dan median 'Pendapatan' dan 'Harga'
print(raw_data[['Pendapatan', 'Harga', 'Produk']].groupby('Produk').agg([np.mean, np.median])) # Menghitung mean dan median Pendapatan dan Harga dari tiap produk
print('\n')