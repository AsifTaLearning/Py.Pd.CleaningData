import pandas as pd

# Wrong Data
# Replacing Values

df = pd.read_csv('data.csv')

df.loc[7,'Duration'] = 45

print(df.to_string())

# Another example

df = pd.read_csv('data.csv')

for x in df.index:
  
  if df.loc[x, "Duration"] > 120:

    df.loc[x, "Duration"] = 120

print(df.to_string())

# Removing Rows

df = pd.read_csv('data.csv')

for x in df.index:
  
  if df.loc[x, "Duration"] > 120:

    df.drop(x, inplace = True)

print(df.to_string())





