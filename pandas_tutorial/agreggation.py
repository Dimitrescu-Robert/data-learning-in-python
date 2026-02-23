import pandas as pd

df = pd.read_csv("pokemons.csv")

print(df.mean(numeric_only=True))
print("\n")

print(df["Height"].sum())
print("\n")

print(df["Weight"].min(numeric_only=True))
print("\n")

print(df.max(numeric_only=True))
print("\n")

print(df.count())
print("\n")

# Basically create a series based on a certain column but still have acces to other values
group = df.groupby("Type1")
print(group["Height"].max())