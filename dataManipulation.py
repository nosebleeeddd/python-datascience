#Manipulating data with functions

import pandas as pd

# Data frame that we can work with
df = pd.DataFrame({
    'name': ['Bob', 'John', 'Tim'],
    'age' : [23, 43, 34],
    'job' : ['chef', 'teacher', 'lawyer']
})


# Multiplies age * 2, division works too
df.age * 2
# Applies changes to dataframe age * 2
df.age = df.age * 2


# Functions to manipulate data(Integers)
# if number divisible by 3
def myfunction(x):
    if x % 3 == 0:
        return x ** 2
    else:
        return x // 2
df.age.apply(myfunction)

# if job ends with r we return no job(Strings)
def myfunction2(x):
    if x.endswith('r'):
        return 'Without Job'
    else:
        return x
df.job = df.job.apply(myfunction2)

#REMOVING COLUMNS
# Removes the series , set df = df.drop to apply
df.drop('Summary', axis=1)
# Removes mulitple columns
df.drop(['age', 'job'], axis=1)