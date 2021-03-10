import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

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
model = DecisionTreeClassifier()

# Model training
model = model.fit(X_train, y_train)

# Predict test
y_pred = model.predict(X_test)