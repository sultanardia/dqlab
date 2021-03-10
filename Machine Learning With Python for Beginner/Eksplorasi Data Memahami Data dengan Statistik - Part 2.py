import pandas as pd 

dataset = pd.read_csv('dataset.csv')

# Melihat korelasi antar feature
dataset_corr = dataset.corr()
print('Korelasi feature: ', dataset_corr)
print('Distribusi Label (Revenue): \n', dataset['Revenue'].value_counts()) # Menghitung persebaran tiap values

# Melihat korelasi antar 2 feature
print('Korelasi ExitRates - BounceRates', dataset.corr().loc['ExitRates', 'BounceRates'])
print('Korelasi Revenue - PageValues', dataset.corr().loc['Revenue', 'PageValues'])
print('Korelasi TrafficType - Weekend', dataset.corr().loc['TrafficType', 'Weekend'])