import pandas as pd 

raw_dataset = pd.read_csv('raw_dataset.csv')

# Korelasi pearson
print(raw_dataset.corr())
print('\n')

# Korelasi kendall
print(raw_dataset.corr(method = 'kendall'))
print('\n')

# Korelasi spearman
print(raw_dataset.corr(method = 'spearman'))
print('\n')