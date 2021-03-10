import pandas as pd 
import numpy as np 
import io
import pandas_profiling

retail_raw = pd.read_csv('dataset.csv')

# Fungsi count untuk menghitung jumlah pengamatan non-NA / non-null dalam suatu series / column
# dataframe['column_name'].count
print(retail_raw['city'].count())