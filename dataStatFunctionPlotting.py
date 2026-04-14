# Functions on and aggregating columns

import pandas as pd
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt

# Data frame that we can work with
df = fetch_california_housing(as_frame=True).frame

# Statistics overview
df.describe()

# Individual series(column) data
df['HouseAge']         # or df.HouseAge

# Functions on Columns
# Sum 
df['HouseAge'].sum()
# Count
df['HouseAge'].count()
# Average
df['HouseAge'].mean()
# Minimum
df['HouseAge'].min()
# Maximum
df['HouseAge'].max()
# Standard Deviation
df['HouseAge'].std()
# Middle value
df['HouseAge'].median()
# Most common value
df['HouseAge'].mode()