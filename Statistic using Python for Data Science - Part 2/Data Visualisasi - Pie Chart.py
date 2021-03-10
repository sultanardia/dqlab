import pandas as pd 
import matplotlib.pyplot as plt

raw_data = pd.read_csv('raw_data.csv')

# Menghitung frekuensi dari kolom Produk
produk_freq = raw_data['Produk'].value_counts()

# Pie chart menggunakan pandas
plt.figure()
produk_freq.plot.pie()
plt.title('.pie dari pandas', size=14)
plt.tight_layout()
plt.show()

# Pie chart menggunakan matplotlib
plt.figure()
plt.pyplot.pie(produk_freq.values, labels = produk_freq.index)
plt.title('.pie dari matplotlib.pyplot', size=14)
plt.tight_layout()
plt.show()