# Getting Info within a dataframe

import pandas as pd
from sklearn.datasets import fetch_california_housing

# Data frame that we can work with
df = fetch_california_housing(as_frame=True).frame

# Get first 10, default first 5
df.head(10)
# Get last 10, default last 5
df.tail(10)
# Get 10 random df, default 1
df.sample(10)

# Gets columns in tuple
df.columns
# Gets columns in list
list(df.columns)

# Set to show certain amount of columns
pd.options.display.max_columns = 500

# Data Frame info. Memory, datatypes, count
df.info()
