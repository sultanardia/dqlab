import pandas as pd 
from sklearn.preprocessing import MinMaxScaler

dataset = pd.read_csv('dataset.csv')
scaler = MinMaxScaler()

scaling_column = ['Administrative','Administrative_Duration','Informational','Informational_Duration','ProductRelated','ProductRelated_Duration','BounceRates','ExitRates','PageValues']

dataset[scaling_column] = scaler.fit_transform(dataset[scaling_column])

print(dataset[scaling_column].describe().T[['mean']])