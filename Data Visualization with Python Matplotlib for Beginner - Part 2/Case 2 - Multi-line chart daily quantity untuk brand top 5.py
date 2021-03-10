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

# Buat multi-line chart
dataset_top5brand_dec.groupby(['order_date', 'brand'])['quantity'].sum().unstack().plot(marker='o', cmap='plasma')

plt.title('Daily Sold Quantity Dec 2019 - Breakdown by Brands', color = 'blue', fontsize = 15, loc = 'center', pad = '30')
plt.xlabel('Order Date', fontsize = 12)
plt.ylabel('Quantity', fontsize = 12)
plt.grid(color = 'gray', linestyle = ':', linewidth = 0.5)
plt.ylim(ymin = 0)
plt.legend(loc = 'upper center', bbox_to_anchor = (1.1, 1), shadow = True, ncol = 2)
plt.annotate('Terjadi lonjakan', xy = (7, 310), xytext = (8, 300), weight = 'bold', color = 'red', arrowprops = dict(
		arrowstyle = '->',
		connectionstyle = 'arc3',
		color = 'red'
	))
plt.gcf().set_size_inches(10, 5)
plt.tight_layout()
plt.show()