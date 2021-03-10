import pandas as pd 
from matplotlib import pyplot as plt 

df = pd.read_csv('dataset.csv', sep = ';')

# Menghapus kolom yang tidak diperlukan
del df[',no']
del df['Row_Num']

# Konversi Last_Transaction ke datetime
df['Last_Transaction'] = pd.to_datetime(df['Last_Transaction']/1000, unit = 's', origin = '1970-01-01')
df['First_Transaction'] = pd.to_datetime(df['First_Transaction']/1000, unit = 's', origin = '1970-01-01')

# Menentukan churn
df.loc[df['Last_Transaction'] <= '2018-08-01', 'is_churn'] = True
df.loc[df['Last_Transaction'] > '2018-08-01', 'is_churn'] = False

df['First_Year'] = df['First_Transaction'].dt.year
df['Last_Year'] = df['Last_Transaction'].dt.year

# Melihat perkembangan customer tiap tahun
data = df.groupby('First_Year')['Customer_ID'].count()

plt.figure()
data.plot(x = 'year', y = 'Customer_ID', kind = 'bar', title = 'Graph of Customer Acquisition')
plt.xlabel('Year_First_Transaction')
plt.ylabel('Num_of_Customer')
plt.tight_layout()
plt.show()