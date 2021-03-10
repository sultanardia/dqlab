import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv('dataset.csv', sep = ';')

# Menghapus kolom yang tidak diperlukan
del df[',no']
del df['Row_Num']

# Konversi ke tanggal
df['First_Transaction'] = pd.to_datetime(df['First_Transaction']/1000, unit = 's', origin = '1970-01-01')
df['Last_Transaction'] = pd.to_datetime(df['Last_Transaction']/1000, unit = 's', origin = '1970-01-01')

# Ambil tahun
df['First_Year'] = df['First_Transaction'].dt.year
df['Last_Year'] = df['Last_Transaction'].dt.year

# print(df.head())
data = df.groupby('First_Year')['Count_Transaction'].sum()

plt.figure()
data.plot(x = 'First_Year', y = 'Count_Transaction', kind = 'bar', title = 'Transaction by year')
plt.xlabel('Year')
plt.ylabel('Transaction')
plt.tight_layout()
plt.show()