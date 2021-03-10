# Import library
import pandas as pd 
import datetime as dt 
import matplotlib.pyplot as plt 

# Baca csv
dataset = pd.read_csv('dataset.csv')

# Buat kolom order_month
dataset['order_month'] = dataset['order_date'].apply(lambda x: dt.datetime.strptime(x, '%Y-%m-%d').strftime('%Y-%m'))

# Buat kolom gmv
dataset['gmv'] = dataset['quantity']*dataset['item_price']

# Membuat kolom baru province_top
top_province = dataset.groupby('province')['gmv'].sum().reset_index().sort_values(by='gmv', ascending=False).head(5)

dataset['province_top'] = dataset['province'].apply(lambda x: x if(x in top_province['province'].to_list()) else 'other')

# Membuat subset data
province_dki_q4 = dataset[(dataset['province'] == 'DKI Jakarta') & (dataset['order_month'] >= '2019-07')]

# Buat data agregat
data_per_customer = province_dki_q4.groupby('customer_id').agg({
		'order_id' : 'nunique',
		'quantity' : 'sum',
		'gmv' : 'sum'
	}).reset_index().rename(columns={'order_id' : 'orders'}).sort_values(by='orders', ascending=False)

# Buat histogram
plt.figure(figsize=(10,5))
plt.hist(data_per_customer['gmv'], bins=100, range=(1,200000000), color='green')
plt.title('Distribution of Total GMV per Customer\nDKI Jakarta in Q4 2019',fontsize=15, color='blue')
plt.xlabel('GMV (in Millions)', fontsize = 12)
plt.ylabel('Number of Customers',fontsize = 12)
plt.xlim(xmin=0,xmax=200000000)

labels, locations = plt.xticks()
plt.xticks(labels, (labels/1000000).astype(int))
plt.show()