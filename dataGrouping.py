# Grouping

import pandas as pd

# Data frame that we can work with
df = pd.DataFrame({
    'name': ['Bob', 'John', 'Tim','Alice'],
    'age' : [23, 43, 34, 41],
    'job' : ['no job', 'cook', 'no job','cook']
})


#Grouping by common values

# Applying aggregation functions
#Groupby average ages with no job
df.groupby('job').agg({
    'age':'mean'
})

# More aggregations
df.groupby('job').agg({
    'age': ['mean', 'min', 'max', 'sum']
})