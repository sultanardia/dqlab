import pandas as pd 
import matplotlib.pyplot as plt 

raw_data = pd.read_csv('raw_data.csv')

# Boxplot menggunakan pandas
plt.figure()
raw_data.boxplot(column = 'Pendapatan')
plt.title('.boxplot dari pandas', size=14)
plt.tight_layout()
plt.show()

# Boxplot menggunakan matplotlib
plt.figure()
plt.boxplot(x = 'Pendapatan', data = raw_data)
plt.xlabel('Pendapatan')
plt.title('pyplot.boxplot dari matplotlib.pyplot', size=14)
plt.tight_layout()
plt.show()