import pandas as pd 
from sklearn.preprocessing import LabelEncoder

dataset = pd.read_csv('dataset.csv')
LE = LabelEncoder()

dataset['Month'] = LE.fit_transform(dataset['Month'])

print(LE.classes_)
print(dataset['Month'].unique())
# print(dataset['Month'])