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
plt.legend(loc = 'upper center', bbox_to_anchor = (1.1, 1), shadow = True, ncol = 2)

# Anotasi pertama
plt.annotate('GMV other meningkat pesat', xy=(5, 900000000), xytext=(4, 1700000000), weight='bold', color='red', arrowprops=dict(arrowstyle='fancy', connectionstyle='arc3', color='red'))

# Anotasi kedua
plt.annotate('DKI Jakarta mendominasi', xy=(3, 3350000000), xytext=(0, 3700000000), weight='bold', color='red', arrowprops=dict(arrowstyle='->', connectionstyle='angle', color='red'))

plt.gcf().set_size_inches(12, 5)
plt.tight_layout()
plt.show()