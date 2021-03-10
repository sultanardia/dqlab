import pandas as pd 
import numpy as np 
import io
import pandas_profiling

retail_raw = pd.read_csv('dataset.csv')

# Outliers merupakan data observasi yang muncul dengan nilai-nilai ekstrim. Yang dimaksud dengan nilai-nilai ekstrim dalam observasi adalah nilai yang jauh atau beda sama sekali dengan sebagian besar nilai lain dalam kelompoknya

# Cara treatment terhadap outliers antara lain:
# 1. Remove the outliers (dibuang)
# 2. Filling the missing value (imputasi)
# 3. Capping
# 4. Prediction 

# Pada umumnya, outliers dapat ditentukan dengan metric IQR (interquartile range).
# Rumus dasar dari IQR: Q3 - Q1, dan data suatu observasi dapat dikatakan outliers jika memenuhi kedua syarat dibawah ini:
# n < Q1 - 1.5 * IQR
# n > Q3 + 1.5 * IQR

q1 = retail_raw['quantity'].quantile(0.25)
q3 = retail_raw['quantity'].quantile(0.75)
iqr = q3 - q1

print('Shape awal : ', retail_raw.shape)

retail_raw = retail_raw[~((retail_raw['quantity'] < (q1 - 1.5 * iqr)) | (retail_raw['quantity'] > (q3 + 1.5 * iqr)))]

print('Shape akhir : ', retail_raw.shape)