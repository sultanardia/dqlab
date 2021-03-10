import pandas as pd 
import numpy as np 
import io
import pandas_profiling

retail_raw = pd.read_csv('dataset.csv')

# Cetak tipe data disetiap kolom retail_raw
print(retail_raw.dtypes)