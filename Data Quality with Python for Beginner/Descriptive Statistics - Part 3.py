import pandas as pd 
import numpy as np 
import io
import pandas_profiling

retail_raw = pd.read_csv('dataset.csv')

length_city = len(retail_raw['city'])
count_city = retail_raw['city'].count()

missing_values = float(((length_city - count_city)/length_city)*100)

print('{0:.3f}%'.format(missing_values))