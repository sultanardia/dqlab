import pandas as pd 
import datetime, dateutil

df = pd.read_csv('dataset.csv', sep = ';')

# Transaksi terakhir
print(df.tail())

df['Last_Transaction'] = pd.to_datetime(df['Last_Transaction']/1000, unit = 's', origin = '1970-01-01')

date = datetime.datetime.today() - dateutil.relativedelta.relativedelta(months = 6)

# Mengecek churn
df.loc[df['Last_Transaction'] <= '2018-08-01', 'is_churn'] = True
df.loc[df['Last_Transaction'] > '2018-08-01', 'is_churn'] = False

print(df.head())

print(df.info())