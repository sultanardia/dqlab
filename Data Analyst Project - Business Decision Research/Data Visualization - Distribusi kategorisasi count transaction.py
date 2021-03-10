import pandas as pd 
import matplotlib.pyplot as plt 

matrix = [[1,2,3],
          ['a','b','c'],
          [3,4,5],
          ['d',4,6]]

matrix = pd.DataFrame(matrix)

print(matrix.iloc[2,0:2])
print('\n')
print(matrix.loc[2,0:2])

# df = pd.read_csv('dataset.csv', sep = ';')

# del df[',no']

# def func(row):
# 	if row['Count_Transaction'] == 1:
# 		val = '1.1'
# 	elif (row['Count_Transaction'] >= 2) and (row['Count_Transaction'] <= 3):
# 		val = '2.2 - 3'
# 	elif (row['Count_Transaction'] >= 4) and (row['Count_Transaction'] <= 6):
# 		val = '3.4 - 6'
# 	elif (row['Count_Transaction'] >= 7) and (row['Count_Transaction'] <= 10):
# 		val = '4.7 - 10'
# 	else:
# 		val = '5. > 10'
# 	return val

# df['Count_Transaction_Group'] = df.apply(func, axis = 1)

# print(df[df['Count_Transaction_Group'] == '1.1'])
