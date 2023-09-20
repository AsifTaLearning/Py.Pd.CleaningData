import pandas as pd

# Pandas - Removing Duplicates
# Discovering Duplicates

df = pd.read_csv('data.csv')

print(df.duplicated())

# Removing Duplicates

df = pd.read_csv('data.csv')

df.drop_duplicates(inplace = True)

print(df.to_string())





