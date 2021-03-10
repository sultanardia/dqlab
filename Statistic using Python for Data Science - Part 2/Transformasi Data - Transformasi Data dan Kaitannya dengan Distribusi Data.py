import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

raw_data = pd.read_csv('raw_data.csv')

# Menampilkan histogram semua kolom
raw_data.hist()
plt.title('Histogram semua kolom')
plt.tight_layout()
plt.show()

# Menampilkan histogram pendapatan
raw_data['Pendapatan'].hist()
plt.title('Histogram kolom pendapatan')
plt.tight_layout()
plt.show()

# Transformasi data
transform_pendapatan = np.power(raw_data['Pendapatan'], 1/5)

# Menampilkan histogram pendapatan tertransformasi
transform_pendapatan.hist()
plt.title('Histogram kolom pendapatan tertransformasi')
plt.tight_layout()
plt.show()

# Menampilkan qqplot
stats.probplot(transform_pendapatan, plot = plt)
plt.title('qqplot kolom pendapatan tertransformasi')
plt.tight_layout()
plt.show()

stats.probplot(raw_data['Pendapatan'], plot = plt)
plt.title('qqplot kolom pendapatan')
plt.tight_layout()
plt.show()