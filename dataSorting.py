# Sorting in ascending and descending order

import pandas as pd

# Data frame that we can work with
df = pd.DataFrame({
    'name': ['Bob', 'John', 'Tim','Alice'],
    'age' : [23, 43, 34, 41],
    'job' : ['no job', 'cook', 'no job','cook']
})


# Sorting

# Ascending
df.sort_values('age')
# Descending
df.sort_values('age', ascending=False)