import pandas as pd

# Empty Cells
# Remove Rows

df = pd.read_csv('data.csv')

new_df = df.dropna()

print(new_df.to_string())

# Another example

df = pd.read_csv('data.csv')

df.dropna(inplace = True) # change the original DataFrame

print(df.to_string())

# Replace Empty Values

df = pd.read_csv('data.csv')

df.fillna(130, inplace = True)

print(df.to_string())

# Replace Only For Specified Columns

df = pd.read_csv('data.csv')

df["Calories"].fillna(555, inplace = True)

# Replace Using Mean, Median, or Mode

df = pd.read_csv('data.csv')

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)

print(df.to_string())

# Another example

df = pd.read_csv('data.csv')

x = df["Calories"].median()

df["Calories"].fillna(x, inplace = True)

print(df.to_string())

# Another example

df = pd.read_csv('data.csv')

x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace = True)

print(df.to_string())





