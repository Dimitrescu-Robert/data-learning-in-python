import pandas as pd

df = pd.read_csv("pokemons.csv", index_col="Name")

# Select by column
print(df[["No", "Height", "Weight"]])

# Select by row
try:
    print(df.loc["Squirtle" : "Weedle"])
except:
    print("oops error")
print(df.iloc[0:10])

pokemon = input("Choose one:")
try:
    print(df.loc[pokemon])
except:
    print("No such pokemon")