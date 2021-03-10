import pandas as pd 
import io
import pandas_profiling as prof 

# Baca csv
uncleaned_raw = pd.read_csv('dataset.csv')

# Inspeksi dataframe uncleaned_raw
top5 = uncleaned_raw.head(5)

# Cek missing value
print(uncleaned_raw.isnull().any())

# Persentase missing value
length_qty = len(uncleaned_raw['Quantity'])
count_qty = uncleaned_raw['Quantity'].count()

# Mengurangi length dengan count
number_of_missing_values_qty = length_qty - count_qty

# Mengubah ke bentuk float
float_of_missing_values_qty = float(number_of_missing_values_qty / length_qty)

# Mengubah ke dalam bentuk persen
pct_of_missing_values_qty = '{0:.1f}%'.format(float_of_missing_values_qty * 100)

# Print hasil percent dari missing value
print('Persentase missing value kolom Quantity:', pct_of_missing_values_qty)

# Mengisi missing value tersebut dengan mean dari kolom tersebut
uncleaned_raw['Quantity'] = uncleaned_raw['Quantity'].fillna(uncleaned_raw['Quantity'].mean())

print(uncleaned_raw.isnull().any())