import matplotlib.pyplot as plt 
import pandas as pd

dataset = pd.read_csv('dataset.csv')

plt.hist(dataset['Region'], color = 'lightblue')
plt.title('Distribution of Customers', fontsize = 20)
plt.xlabel('Region Codes', fontsize = 14)
plt.ylabel('Count Users', fontsize = 14)
plt.show()