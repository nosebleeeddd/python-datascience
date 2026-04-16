# Iterate using For-loops and Filter through dataFrames

import pandas as pd
import datatime as dt

# Iterating through dataframes
#For-loop for going thru individual rows
for i, row in df.iterrows():
    print(i)

# For-loop for Columns as well
for i, col in df.items():
    print(col)


# Filtering & Querying data
# Populate [[ with our > 40 booleans
df.age > 40
# Manually filtered data frame
df[[False, True, False, True]]


# Filters
# Automatic Conditions that filter
df[df.age > 40]

# Surrounding with df[] will show dataframe
(df.age > 35) & (df.job.notna())
df[(df.age > 35) & (df.job.notna())]

# ~ will flip your boolean, this shows NaN's
df[~df.job.notna()]

# Filter for string endings
df[df.name.str.endswith('e')]
# Filter Combined example
df[(df.name.str.endswith('e')) & (df.age.notna())]

# lambda for adding bday col to dataframe
df['birthday'] = df['age'].apply(lambda x: dt.datetime.now() - dt.timedelta(days=365*x))

# Filter through birthdays
df[df.birthday.dt.year > 1984]

# Filter by list
ages = [34, 41]
df[df.age.isin(ages)]

# Querying is a much faster way but limited
df.query('age > 30')