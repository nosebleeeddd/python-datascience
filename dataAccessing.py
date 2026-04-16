# Accessing/changing data fields 

import pandas as pd

# Create our Dataframe we'll work with
df = pd.DataFrame({
    'name': ['Mike', 'Alice', 'Bob'],
    'age': [30, 55, 34],
    'job': ['programmer', 'designer', 'teacher']
})

# set index to be accessible by name
df = df.set_index('name')

# Access index and all data fields with .loc
df.loc[1]

# Access by name once set_index('name')
df.loc['Alice']
# Acess field from the index which we set to name
df.loc['Alice','age']

# Access index after setting index to name string
df.iloc[1]
# Access index data fields
df.iloc[1,0]

# PREFFERED WAY FOR ACCESSING SINGLE DATA FIELDS
df.at['Alice', 'age']
df.iat[1, 0]

# Changing Data fields
df.at['Alice', 'age'] = 60
df.loc['Alice'] = [75, 'clerk']

# Append new rows to data frame
df.loc['John'] = [40, 'coach']

# Slice of dataframe  'everything up until'
df.iloc[0:3]
# Slice and show specific column
df.iloc[0:2, 1]
# Get everything
df.iloc[:,:]