import pandas as pd 
import matplotlib.pyplot as plt

raw_data = pd.read_csv('raw_data.csv')

# Menghitung frekuensi dari kolom Produk
produk_freq = raw_data['Produk'].value_counts()

# Bar chart menggunakan pandas
plt.figure()
produk_freq.plot.bar()
plt.title('.bar dari pandas', size=14)
plt.tight_layout()
plt.show()

# Bar chart menggunakan matplotlib
plt.figure()
plt.bar(x = produk_freq.index, height = produk_freq.values)
plt.title('.bar dari matplotlib.pyplot', size=14)
plt.tight_layout()
plt.show()