import pandas as pd 
import numpy as np 

df = pd.read_csv('dataset.csv')

# Transforming to_datetime
df['order_date'] = pd.to_datetime(df['order_date'])

# Transforming to_numeric
df['quantity'] = pd.to_numeric(df['quantity'], downcast = 'float')
df['city'] = df['city'].astype('category')

# Transforming apply and map
df['brand'] = df['brand'].apply(lambda x : x.lower() if x == 'BRAND_H' else x)
df['brand'] = df['brand'].map(lambda x : x[-1])

# Transformin applymap
df_tr = pd.DataFrame(np.random.rand(3, 5))

def trans(x):
	print(x)
	return

df_tr_trans = df_tr.applymap(trans)
print(df_tr)
print(df_tr_trans)