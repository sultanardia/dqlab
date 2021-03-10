import pandas as pd 

df = pd.read_csv('dataset.csv', sep = ';')

# Kolom First_Transaction
df['First_Transaction'] = pd.to_datetime(df['First_Transaction']/1000, unit = 's', origin = '1970-01-01')

# Kolom Last_Transaction
df['Last_Transaction'] = pd.to_datetime(df['Last_Transaction']/1000, unit = 's', origin = '1970-01-01')

print('Lima teratas :')
print(df.head())

print('\nInfo dataset :')
print(df.info())