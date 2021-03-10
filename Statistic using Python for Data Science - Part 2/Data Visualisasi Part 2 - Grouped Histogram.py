import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

raw_data = pd.read_csv('raw_data.csv')

raw_data[raw_data['Produk'] == 'A'].hist()
plt.tight_layout()
plt.show()