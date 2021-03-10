import pandas as pd 
import matplotlib.pyplot as plt 

raw_data = pd.read_csv('raw_data.csv')

# Histogram menggunakan pandas
raw_data.hist(column = 'Pendapatan')
plt.title('.hist dari pandas', size=14)
plt.tight_layout()
plt.show()

# Histogram menggunakan matplotlib
plt.hist(x = 'Pendapatan', data = raw_data)
plt.xlabel('Pendapatan')
plt.title('pyplot.hist dari matplotlib.pyplot', size=14)
plt.tight_layout()
plt.show()