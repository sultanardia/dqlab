import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

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

# Membuat plot
sns.pointplot(data = df.groupby(['First_Year', 'Product']).mean().reset_index(), x = 'First_Year', y = 'Average_Transaction_Amount', hue = 'Product')
plt.tight_layout()
plt.show()