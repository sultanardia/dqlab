import pandas as pd 
import matplotlib.pyplot as plt

raw_data = pd.read_csv('raw_data.csv')

plt.figure()

# Scatterplot menggunakan pandas
raw_data.plot.scatter(x = 'Pendapatan', y = 'Total')
plt.title('plot.scatter dari pandas', size=14)
plt.tight_layout()
plt.show()

# Scatterplot menggunakan matplotlib
plt.scatter(x = 'Pendapatan', y = 'Total', data = raw_data)
plt.title('plt.scatter dari matplotlib', size=14)
plt.tight_layout()
plt.show()
