# Import library
import pandas as pd 
import datetime as dt 
import matplotlib.pyplot as plt 

# Ambil data csv
dataset = pd.read_csv('dataset.csv')

# Buat kolom order_month
dataset['order_month'] = dataset['order_date'].apply(lambda x: dt.datetime.strptime(x, '%Y-%m-%d').strftime('%Y-%m'))

# Analisis top brand bulan desember 2019
top_brands = dataset.groupby('brand')['quantity'].sum().reset_index().sort_values(by='quantity', ascending=False).head(5)

dataset_top5brand_dec = dataset[(dataset['order_month'] == '2019-12') & (dataset['brand'].isin(top_brands['brand']).to_list())].to_csv(r'csv.csv')