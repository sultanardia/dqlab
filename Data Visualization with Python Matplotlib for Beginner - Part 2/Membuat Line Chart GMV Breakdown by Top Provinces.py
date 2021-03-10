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

# Buat kolom province_top pada dataset
dataset['province_top'] = dataset['province'].apply(lambda x: x if(x in top_provinces['province'].to_list()) else 'other')

# Buat plot 5 provinsi tertinggi
dataset.groupby(['order_month', 'province_top'])['gmv'].sum().unstack().plot(cmap = 'plasma')

plt.title('Monthly GMV Year 2019 - Breakdown by Province',loc='center',pad=30, fontsize=20, color='blue')
plt.xlabel('Order Month', fontsize = 15)
plt.ylabel('Total Amount (in Billions)',fontsize = 15)
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt.ylim(ymin=0)

labels, locations = plt.yticks()
plt.yticks(labels, (labels/1000000000).astype(int))

# Kustomisasi legend
plt.legend(loc = 'right', bbox_to_anchor = (1.6, 0.5), shadow = True, ncol = 2)
plt.gcf().set_size_inches(10, 5)
plt.tight_layout()
plt.show()