import pandas as pd 

# df = pd.read_csv('dataset.csv')

# del df['Unnamed: 0.1']
# del df['Unnamed: 0']

# # for inv, desc in zip(df['InvoiceNo'].head(), df['Description'].head()):
# # 	print(inv, ' : ', desc)
# # print(df.columns)

# # df_x = df.set_index(['InvoiceNo', 'Description', 'Quantity', 'InvoiceDate'])

# # print(df_x.index)
# # print('\n')
# # print(df.index)

# city = df.groupby('City')

# # print(city.get_group('Jakarta'))
# print(df[df['City'] == 'Jakarta'])

df_week = pd.DataFrame({
		'day' : [i+1 for i in range (7)],
		'week_type' : ['weekday' for i in range (5)] + ['weekend' for i in range (2)]
	})

df_week_index = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

df_week.index = [df_week_index, df_week['day'].to_list()]

df_week.index.names = ['name', 'num']

print(df_week.index.name)