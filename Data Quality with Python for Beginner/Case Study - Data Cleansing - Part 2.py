import pandas as pd 

# Baca csv
uncleaned_raw = pd.read_csv('dataset.csv')

q1 = uncleaned_raw['UnitPrice'].quantile(0.25)
q3 = uncleaned_raw['UnitPrice'].quantile(0.75)

iqr = q3 - q1

# Removing outliner
uncleaned_raw = uncleaned_raw[~((uncleaned_raw['UnitPrice'] < q1 - 1.5 * iqr) | (uncleaned_raw['UnitPrice'] > q3 + 1.5 * iqr))]

# Check duplicate
print(uncleaned_raw.duplicated(subset = None))

# Removing duplicate
uncleaned_raw = uncleaned_raw.drop_duplicates()