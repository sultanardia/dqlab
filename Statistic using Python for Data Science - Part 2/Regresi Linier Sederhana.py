import pandas as pd 
import statsmodels.api as sm 

raw_data = pd.read_csv('raw_data.csv')

# Variabel bebas
nilai_X = raw_data['Pendapatan']

# Variabel tak bebas
nilai_Y = raw_data['Total']

# Membuat model regresi linear
model_regresi = sm.OLS(endog = nilai_Y, exog = nilai_X).fit()

print(raw_data, '\n\n\n\n')
print(model_regresi.summary())