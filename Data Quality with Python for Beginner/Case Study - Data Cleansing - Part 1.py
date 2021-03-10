import pandas as pd 
import matplotlib.pyplot as plt 

# Baca csv
uncleaned_raw = pd.read_csv('dataset.csv')

# Mengisi missing value tersebut dengan mean dari kolom tersebut
uncleaned_raw['Quantity'] = uncleaned_raw['Quantity'].fillna(uncleaned_raw['Quantity'].mean())

uncleaned_raw.boxplot()
plt.show()