import pandas as pd 

dataset = pd.read_csv('dataset.csv')

print('Shape dataset:', dataset.shape) # Shape untuk melihat dimensi dari dataset
print('\nLima data teratas:\n', dataset.head()) # Head untuk mengambil 5 data teratas
print('\nInformasi dataset:')
print(dataset.info()) # Info untuk melihat informasi dari dataset
print('\nStatistik deskriptif:\n', dataset.describe()) # Describe untuk melihat statistik deskriptif