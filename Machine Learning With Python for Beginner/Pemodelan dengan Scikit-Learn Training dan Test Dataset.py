import pandas as pd 
from sklearn.model_selection import train_test_split

# Sebelum kita melatih model dengan suatu algorithm machine, dataset perlu kita bagi ke dalam training dataset dan test dataset dengan perbandingan 80:20. 80% digunakan untuk training dan 20% untuk proses testing.
dataset = pd.read_csv('dataset.csv')

X = dataset.drop(['Revenue'], axis = 1)
y = dataset['Revenue']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)
# print(train_test_split(X, y, test_size = 0.2, random_state = 0))