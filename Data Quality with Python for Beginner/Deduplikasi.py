import pandas as pd 
import numpy as np 
import io
import pandas_profiling

retail_raw = pd.read_csv('dataset.csv')

# Duplikasi data merupakan data dengan kondisi pada row-row tertentu memiliki kesamaan data di seluruh kolomnya. Tentunya ada data yang duplikat dalam dataset yang dimiliki. Kondisi duplikasi harus diatasi dengan jalan mengeliminir baris yang mengalami duplikasi

retail_raw.duplicated(subset = None).to_csv(r'csv.csv') # Cek duplikasi

retail_raw.drop_duplicates() # Dropping duplikasi