import pandas as pd 
import numpy as np 

raw_data = pd.read_csv('raw_dataset.csv')

# Proporsi kategori
print(raw_data['Produk'].value_counts()/raw_data.shape[0])
print('\n')
# Rumus: N kategori ke i/N total

# Range
print(raw_data['Pendapatan'].max() - raw_data['Pendapatan'].min())
print('\n')
# Rumus : max(x) - min(x)

# Variansi
print(raw_data['Pendapatan'].var()) # Menggunakan variansi populasi
print(np.var(raw_data['Pendapatan'])) # Menggunakan variansi sampel
print(raw_data['Pendapatan'].var(ddof = 0)) # Menggunakan variansi populasi pandas
print('\n')

# Standar deviasi
print(raw_data['Pendapatan'].std()) # Menggunakan variansi populasi
print(np.std(raw_data['Pendapatan'], ddof=1)) # Menggunakan variansi populasi numpy