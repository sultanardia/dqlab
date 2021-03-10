import pandas as pd 

df = pd.read_csv('dataset.csv', sep = ';')

# Menghapus kolom
del df[',no']
del df['Row_Num']

print(df.head())