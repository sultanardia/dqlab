import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

raw_data = pd.read_csv('raw_data.csv')

# Transformasi string ke angka
transform_produk = pd.get_dummies(raw_data['Produk'])

print(transform_produk)