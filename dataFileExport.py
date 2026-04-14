# Setting Index and exporting/importing DataFrames

import pandas as pd

# Series --column of a data frame--
values = [10, 20, 30, 40, 50]

# specify index for values
s = pd.Series(values, index=['a','b','c','d','e'])
#s.loc['b']   lets you access indexes value or rows

# Data Frame -- table of data --
df = pd.DataFrame({
    'name': ['Mike', 'Bob', 'Alice'],
    'age': [30, 60, 45],
    'job': ['programmer', 'clerk', 'designer']
})

# can set it as index value and access with .loc
df = df.set_index('name')
#df.loc['Bob']

# Resets index
df = df.reset_index()

df

# Exporting dataframes
df.to_csv('mydata.csv', index=None)

# Read in clean dataframe (fix index issues)
pd.read_csv('mydata.csv',index_col=0)