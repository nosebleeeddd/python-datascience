# Plotting dataframe to histogram & Stock like plotline

import pandas as pd
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt
import yfinance as yf


# Data frame that we can work with
df = fetch_california_housing(as_frame=True).frame

# Histogram (graph) uses matplotlib
df['HouseAge'].hist()
# Set histogram size
df['HouseAge'].hist(figsize=(12,8))
# Can set line chart or any other
df['HouseAge'].plot(figsize=(12,8))

# Sets title for chart
plt.title('House Age')
plt.show()

# Histogram per all column data
df.hist(figsize=(12,8))
# Format or readibility
plt.tight_layout()

# Stock Plotting chart
stock_df = yf.download('BTC-USD')

# Stock Data
stock_df
# Stock Close Plot
stock_df.Close.plot()
# Stock plot everything
stock_df.plot()
# Stock histogram
stock_df.hist()