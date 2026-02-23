import pandas as pd

df = pd.read_csv("pokemons.csv")

df = df.drop(columns=["Legendary", "No"])

# Clear empty slots: 
# df = df.dropna()

df = df.fillna({"Type2": "None"})

# Replace instance of a value
df["Type1"] = df["Type1"].replace({"Rock" : "RocknRoll"})


print(df.to_string())