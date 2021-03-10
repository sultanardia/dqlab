# Import library
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt 

# Baca dataset
dataset = pd.read_csv('dataset.csv')

# Buat kolom baru bernama order_month dengan tipe datetime format %Y-%m
dataset['order_month'] = dataset['order_date'].apply(lambda x: dt.datetime.strptime(x, '%Y-%m-%d').strftime('%Y-%m'))

# Buat kolom gmv
dataset['gmv'] = dataset['item_price']*dataset['quantity']

# Buat variabel untuk 5 propinsi dengan GMV tertinggi
top_provinces = dataset.groupby('province')['gmv'].sum().reset_index().sort_values('gmv', ascending=False).head(5)

# Buat kolom baru province_top pada dataset
dataset['province_top'] = dataset['province'].apply(lambda x: x if(x in top_provinces['province'].to_list()) else 'other')

# Buat subset data
dataset_dki_q4 = dataset[(dataset['province'] == 'DKI Jakarta') & (dataset['order_month'] >= '2019-10')]

# Buat pie chart
gmv_per_city_dki_q4 = dataset_dki_q4.groupby('city')['gmv'].sum().reset_index()

plt.figure(figsize=(6,6))
plt.pie(gmv_per_city_dki_q4['gmv'], labels = gmv_per_city_dki_q4['city'], autopct='%1.2f%%')
plt.title('GMV Contribution Per City - DKI Jakarta in Q4 2019', loc='center', pad=30, fontsize = 15, color = 'blue')
plt.show()