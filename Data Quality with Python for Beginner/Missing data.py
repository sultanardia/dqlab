import pandas as pd 
import numpy as np 
import io
import pandas_profiling

retail_raw = pd.read_csv('dataset.csv')

# Cek missing value
print(retail_raw.isnull().any())

# Imputasi, merupakan suatu metode treatment terhadap missing value dengan mengisinya menggunakan teknik tertentu
imputated = retail_raw['quantity'].fillna(retail_raw['quantity'].mean())

# Drop row, menghapus baris kosong
drop = retail_raw['quantity'].dropna()