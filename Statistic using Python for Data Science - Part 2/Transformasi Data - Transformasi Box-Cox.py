import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

raw_data = pd.read_csv('raw_data.csv')

# Transformasi menggunakan boxcox
boxcox_pendapatan, _ = stats.boxcox(raw_data['Pendapatan'])

# Histogram boxcox pendapatan
plt.hist(boxcox_pendapatan)
plt.title('Histogram', size=14)
plt.tight_layout()
plt.show()

# qqplot boxcox pendapatan
stats.probplot(boxcox_pendapatan, plot = plt)
plt.title('qqplot', size=14)
plt.tight_layout()
plt.show()