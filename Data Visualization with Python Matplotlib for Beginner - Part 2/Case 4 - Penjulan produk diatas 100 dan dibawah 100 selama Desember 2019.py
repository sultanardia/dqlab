# Import library
import pandas as pd 
import datetime as dt 
import matplotlib.pyplot as plt 

# Ambil data csv
dataset = pd.read_csv('dataset.csv')

# Buat kolom baru order_month
dataset['order_month'] = dataset['order_date'].apply(lambda x: dt.datetime.strptime(x, '%Y-%m-%d').strftime('%Y-%m'))

# Analisis top 5 bulan desember 2019
top_brands = dataset.groupby('brand')['quantity'].sum().reset_index().sort_values(by = 'quantity',ascending = False).head(5)

dataset_top5brand_dec = dataset[(dataset['order_month'] == '2019-12') & (dataset['brand'].isin(top_brands['brand']).to_list())]

# Analisis penjualan
dataset_top5brand_dec_per_product = dataset_top5brand_dec.groupby(['brand', 'product_id'])['quantity'].sum().reset_index()

dataset_top5brand_dec_per_product['quantity_group'] = dataset_top5brand_dec_per_product['quantity'].apply(lambda x: '> 100' if (x >= 100) else '< 100')

# Membuat referensi pengurutan berdasarkan banyaknya product
sort_ref = dataset_top5brand_dec_per_product.groupby('brand')['product_id'].nunique().sort_values(ascending = False)

# Membuat stack chart
dataset_top5brand_dec_per_product.groupby(['brand', 'quantity_group'])['product_id'].nunique().reindex(index = sort_ref.index, level = 'brand').unstack().plot(kind = 'bar', stacked = True)
plt.show()