import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd 

dataset = pd.read_csv('dataset.csv')

# Membuat visualisasi data
plt.rcParams['figure.figsize'] = (12, 5)
# checking the Distribution of customers on Revenue
plt.subplot(1, 2, 1)
sns.countplot(dataset['Revenue'], palette = 'pastel')
plt.title('Buy or Not', fontsize = 20)
plt.xlabel('Revenue or not', fontsize = 14)
plt.ylabel('count', fontsize = 14)
# checking the Distribution of customers on Weekend
plt.subplot(1, 2, 2)
sns.countplot(dataset['Weekend'], palette = 'inferno')
plt.title('Purchase on Weekend', fontsize = 20)
plt.xlabel('Weekend or not', fontsize = 14)
plt.ylabel('count', fontsize = 14)

plt.show()