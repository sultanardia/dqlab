# Import library
import pandas as pd 
import matplotlib.pyplot as plt 
import datetime as dt

# Mengambil data csv
dataset = pd.read_csv('dataset.csv')

# Membuat kolom baru order_month
dataset['order_month'] = dataset['order_date'].apply(lambda x: dt.datetime.strptime(x, '%Y-%m-%d').strftime('%Y-%m'))

# Membuat kolom baru gmv
dataset['gmv'] = dataset['item_price']*dataset['quantity']

# Membuat kolom baru province_top
top_province = dataset.groupby('province')['gmv'].sum().reset_index().sort_values(by='gmv', ascending=False).head(5)

dataset['province_top'] = dataset['province'].apply(lambda x: x if(x in top_province['province'].to_list()) else 'other')

# Membuat subset data
province_dki_q4 = dataset[(dataset['province'] == 'DKI Jakarta') & (dataset['order_month'] >= '2019-07')]


# Membuat stacked chart
province_dki_q4.groupby(['city', 'order_month'])['gmv'].sum().unstack().plot(kind='bar', stacked=True)

plt.title('GMV Contribution Per City - DKI Jakarta in Q4 2019', loc='center', pad=30, fontsize = 15, color = 'blue')
plt.xlabel('City', fontsize = 15)
plt.ylabel('Total Amount (in Billions)',fontsize = 15)
plt.ylim(ymin=0)

labels, locations = plt.yticks()

plt.yticks(labels, (labels/100000000).astype(int))
plt.xticks(rotation=0)
plt.show()
