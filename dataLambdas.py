# Useful lambas 
import pandas as pd

# Lambda one liners are great for simplifying functions

# Function , if x divisible by 3 then ** 2 else // 2
df.age.apply(lambda x: x ** 2 if x % 3 == 0 else x // 2)

# Make a column of summarized data rows
df['Summary'] = df.apply(lambda row: f'Age: {row["age"]}, Job: {row["job"]}', axis=1)

# lambda for adding bday col to dataframe
df['birthday'] = df['age'].apply(lambda x: dt.datetime.now() - dt.timedelta(days=365*x))
