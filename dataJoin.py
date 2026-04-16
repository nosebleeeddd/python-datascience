# Joining DataFrames

import pandas as pd

#----Joining----

# Joining Data Frames
df4 = pd.DataFrame({
    'Price': [10, 20, 30],
}, index=['A', 'B', 'C'])

df5 = pd.DataFrame({
    'Country': ['A', 'Y', 'Z'],
}, index=['B', 'C', 'D'])


# 'left' join first data frame
df4.join(df5)
# 'right' join second data frame
df4.join(df5, how='right')
# 'inner' common join
df4.join(df5, how='inner')
# 'outer' gets all
df4.join(df5, how='outer')


#----Joining----