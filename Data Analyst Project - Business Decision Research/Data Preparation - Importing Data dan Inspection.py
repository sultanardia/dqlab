import pandas as pd 

df = pd.read_csv('dataset.csv', sep = ';')

print('Lima teratas :')
print(df.head())

print('\nInfo dataset :')
print(df.info())