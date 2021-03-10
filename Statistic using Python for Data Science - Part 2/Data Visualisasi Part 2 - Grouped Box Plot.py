import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

raw_data = pd.read_csv('raw_data.csv')

raw_data.boxplot(rot=90)
plt.title('Boxplot tanpa pengelompokkan', size=14)
plt.tight_layout()
plt.show()

raw_data.boxplot(by = 'Produk')
plt.title('Boxplot grouped by Produk', size=14)
plt.tight_layout()
plt.show()