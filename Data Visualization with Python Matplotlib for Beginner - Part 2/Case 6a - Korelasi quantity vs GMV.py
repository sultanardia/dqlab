# Import library
import pandas as pd 
import datetime as dt 
from matplotlib import pyplot as plt 

# Baca csv
dataset = pd.read_csv('dataset.csv')

# Buat kolom baru gmv
dataset['gmv'] = dataset['quantity'] * dataset['item_price']

# Buat kolom baru order_month
dataset['order_month'] = dataset['order_date'].apply(lambda x: dt.datetime.strptime(x, '%Y-%m-%d').strftime('%Y-%m'))

# Analisis data
top_brand = dataset.groupby('brand')['quantity'].sum().reset_index().sort_values(by = 'quantity', ascending = False).head(5)

dataset_top5brand_des = dataset[(dataset['order_month'] == '2019-12') & (dataset['brand'].isin(top_brand['brand']).to_list())]

data_per_product = dataset_top5brand_des.groupby('product_id').agg({
		'quantity' : 'sum',
		'gmv' : 'sum',
		'item_price' : 'median'
	}).reset_index()

# Buat scatterplot
plt.figure(figsize = (10, 5))
plt.scatter(data_per_product['quantity'], data_per_product['gmv'], marker = '+', color = 'red')
plt.title('Correlation of Quantity and GMV per Product\nTop 5 Brands in December 2019', color = 'blue', fontsize = 15, pad = 30)
plt.xlabel('Quantity', fontsize = 12)
plt.ylabel('GMV', fontsize = 12)
plt.xlim(xmin=0,xmax=300)
plt.ylim(ymin=0,ymax=200000000)

labels, locations = plt.yticks()

plt.yticks(labels, (labels/1000000).astype(int))
plt.show()