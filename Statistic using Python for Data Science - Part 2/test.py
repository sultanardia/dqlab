import pandas as pd 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('iris.csv')

scaler = StandardScaler()
scaler.fit(df)
scaler.transform(df)

X = df.drop(['class'], axis = 1)
Y = df['class']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

model = LogisticRegression()

model = model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

print('Train accuracy : ', model.score(X_train, Y_train))
print('Test accuracy : ', model.score(X_test, Y_test))

print('\nConfusion matrix : ')
print(confusion_matrix(Y_test, Y_pred))

print('\nClassification report : ')
print(classification_report(Y_test, Y_pred))

# print(df.head())