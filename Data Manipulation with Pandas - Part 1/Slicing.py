import pandas as pd 

df = pd.read_csv('dataset.csv')

# df_slice = df.loc[(df['customer_id'] == '18055') & (df['product_id'].isin(["P0029", "P0040", "P0041", "P0116", "P0117"]))]

df_x = pd.IndexSlice

df = df.set_index(['order_date', 'customer_id'])

df_slice = df.sort_index().loc[df_x['2019-01-01', '12681':'17511'], : ]

print(df)