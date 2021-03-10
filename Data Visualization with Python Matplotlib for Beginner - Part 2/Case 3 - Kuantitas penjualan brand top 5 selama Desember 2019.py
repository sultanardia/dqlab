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

dataset_top5brand_dec = dataset[(dataset['order_month'] == '2019-12') & (dataset['brand'].isin(top_brands['brand']))]

# Buat bar chart
dataset_top5brand_dec.groupby('brand')['product_id'].nunique().sort_values(ascending = False).plot(kind = 'bar')

plt.title('Number of Sold Products per Brand, December 2019', fontsize = 15, color = 'blue', pad = 30, loc = 'center')
plt.xlabel('Brand', fontsize = 12)
plt.ylabel('Number of Products', fontsize = 12)
plt.ylim(ymin = 0)
plt.xticks(rotation = 0)
plt.show()