# Import all packages
# export PATH="/usr/local/opt/python/libexec/bin:$PATH"
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import scipy.io 

# Import url for table
from urllib.request import urlretrieve
url = 'https://assets.datacamp.com/production/course_2023/datasets/tb.csv'
urlretrieve(url, 'tb.csv')

df = pd.read_csv(url, sep=',')
# print(df.head())

# Create two tables, then concatenate them from df
concat1 = pd.melt(frame = df, id_vars = ['country', 'year'], value_vars = ['m014', 'm1524'], value_name = 'value')
concat2 = pd.melt(frame = df, id_vars = ['country', 'year'], value_vars = ['m2534', 'm3544'], value_name = 'value')

concat = pd.concat([concat1, concat2], ignore_index = True)
print(concat.head())