# Merging DataFrames

import pandas as pd

#----Merging----

# Merging Data frames
df3 = pd.DataFrame({
    'Item': ['B', 'C', 'D'],
    'Country': ['X', 'Y', 'Z']
})

# Merge Common values into dataFrame
pd.merge(df1,df3)

# Merge showing all indexes, NaN for empty
pd.merge(df1, df3, how='outer')
# Merge showing all indexes without NaN
pd.merge(df1, df3, how='inner')
# Merge just showing first dataframe
pd.merge(df1, df3, how='left')
# Merge just showing second dataframe
pd.merge(df1, df3, how='right')

# Merge on specified column
pd.merge(df1, df3, on='Item', how='outer')

#----Merging----