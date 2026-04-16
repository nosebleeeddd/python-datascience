# Ways to get clean data , no NaNs
import pandas as pd

# Data frame that we can work with
df = pd.DataFrame({
    'name': ['Bob', 'John', 'Tim'],
    'age' : [23, 43, 34],
    'job' : ['chef', 'teacher', 'lawyer']
})

# Data Cleaning

# Set a NaN value to test on
df.at['Alice', 'age'] = float('nan')
df.info()

# Remove NaN values
df.dropna()
# Replace NaN values
df.fillna(0)

# Fill age column with the average age
df.age.fillna(df.age.mean())

# Set a cell to none
df.at['Bob', 'job'] = None
df.info()

# All numbers are true and NaN are false
df.notna()
# Drops all rows where age column is NaN
df[df.age.notna()]