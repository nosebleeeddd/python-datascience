# Query for fast filtering

import pandas as pd

data = {
    'Name': ['John', 'Emily', 'Mike', 'Jim', 'John'],
    'Age': [25, 30, 35, 26, 32]
    'City': ['New York', 'San Francisco', 'Chicago', 'Los Angeles', 'Boston']
    'Salary': [50000, 60000, 70000, 55000, 65000]
}

# Query quick filters

# Prints ages over 30
result = df.query("Age > 30")
print(result)

# Prints anyone over 30 name and salary
result = df.query("Age > 30")[["Name","Salary"]]
print(result)

# Gets anyone over 20 and field value matching
result = df.query("(Age > 20) & (City == 'New York')")
print(result)

# Get a data for Salaries above 60000
result = df.query("Salary > 60000")
print(result)

# Gets data for just specific values
result = df.query("City in ['New York', 'Boston']")
print(result)

# Gets data for names starting with specific letter
result = df[df["Name"].str.startswith('J')]
print(result)

# Gets data for names containing an 'a'
result = df[df["Name"].str.contains('a')]
print(result)

# Selecting rows for ages 25 and 35
result = df.query("Age >= 25 and Age <= 25")
print(result)

