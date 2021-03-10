import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.linear_model import LogisticRegression

# Baca file csv
dataset = pd.read_csv('csv.csv')

# Handling missing value menggunakan imputation
dataset.fillna(dataset.mean(), inplace = True)

# Mengubah data string menjadi integer dengan encoder
LE = LabelEncoder()
dataset['Month'] = LE.fit_transform(dataset['Month'])

LE = LabelEncoder()
dataset['VisitorType'] = LE.fit_transform(dataset['VisitorType'])

# Memisahkan feature dengan label
X = dataset.drop(['Revenue'], axis = 1) # Feature
y = dataset['Revenue'] # Label

# Splitting train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Memanggil classifier dengan metode decision tree
model = LogisticRegression()

# Model training
model = model.fit(X_train, y_train)

# Predict test
y_pred = model.predict(X_test)

# Evaluating model
print('Training accuracy : ', model.score(X_train, y_train))
print('Testing accuracy : ', model.score(X_test, y_test))

# Confusion matrix
print('\nConfusion matrix :')
print(confusion_matrix(y_test, y_pred))

# Classification report
print('\nClassification report :')
print(classification_report(y_test, y_pred))