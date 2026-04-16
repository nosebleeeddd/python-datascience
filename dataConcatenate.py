# Concatenating DataFrames

import pandas as pd

#----Concatenating----
# Data Frames we will work with for rows
df1 = pd.DataFrame({
    'Item': ['A', 'B', 'C'],
    'Price': [10, 20, 30]
})

df2 = pd.DataFrame({
    'Item': ['D', 'E', 'F'],
    'Price': [40, 50, 60]
})

# Stacking rows/columns
# Stacks the two dataframes rows together
pd.concat([df1, df2])
# Corrects the index
pd.concat([df1, df2]).reset_index().drop('index', axis=1)

# Data Frames we will work with for columns
df1 = pd.DataFrame({
    'Item': ['A', 'B', 'C'],
    'Price': [10, 20, 30]
})

df2 = pd.DataFrame({
    'Country': ['X', 'Y', 'Z'],
    'Available': [True, True, False]
})

# Stacking Columns
# Stacks the two dataframes column wise
pd.concat([df1, df2], axis=1)
#----Concatenating----


