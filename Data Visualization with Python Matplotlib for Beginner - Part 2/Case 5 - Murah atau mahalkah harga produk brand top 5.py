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

# Membuat histogram
plt.figure()
plt.hist(dataset_top5brand_dec.groupby('product_id')['item_price'].median(), bins=10, stacked=True, range=(1,2000000), color='green')
plt.title('Distribution of Price Median per Product\nTop 5 Brands in Dec 2019',fontsize=15, color='blue')
plt.xlabel('Price Median', fontsize = 12)
plt.ylabel('Number of Products',fontsize = 12)
plt.xlim(xmin=1,xmax=2000000)
plt.show()