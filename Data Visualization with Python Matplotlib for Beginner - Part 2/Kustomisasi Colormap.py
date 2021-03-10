# Import library
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt

# Baca dataset
dataset = pd.read_csv('dataset.csv')

# Buat kolom baru yang bertipe datetime dalam format '%Y-%m'
dataset['order_month'] = dataset['order_date'].apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))

# Buat Kolom GMV
dataset['gmv'] = dataset['item_price']*dataset['quantity']

# Buat Multi-Line Chart
dataset.groupby(['order_month','province'])['gmv'].sum().unstack().plot(cmap = 'tab20c') # Membuat plot berdasarkan sumbu X (order_month), breakdown province, dan sumbu Y (sum(gmv))
# parameter cmap untuk mapping color dari matplotlib

plt.title('Monthly GMV Year 2019 - Breakdown by Province',loc='center',pad=30, fontsize=20, color='blue')
plt.xlabel('Order Month', fontsize = 15)
plt.ylabel('Total Amount (in Billions)',fontsize = 15)
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt.ylim(ymin=0)

labels, locations = plt.yticks()
plt.yticks(labels, (labels/1000000000).astype(int))

# Kustomisasi legend dan colormap
plt.legend(loc = 'right', bbox_to_anchor = (1.6, 0.5), shadow = True, ncol = 2, title = 'Province', fontsize = 9, title_fontsize = 11)
plt.gcf().set_size_inches(10, 5)
plt.tight_layout()
plt.show()