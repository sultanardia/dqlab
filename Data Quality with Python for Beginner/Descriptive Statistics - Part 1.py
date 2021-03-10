import pandas as pd 
import numpy as np 
import io
import pandas_profiling

retail_raw = pd.read_csv('dataset.csv')

# Fungsi len untuk menghitung jumlah pengamatan dalam suatu series / column
# len(dataframe['column_name'])
print(len(retail_raw['city']))