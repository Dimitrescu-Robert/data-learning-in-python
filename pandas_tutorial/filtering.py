import pandas as pd

df = pd.read_csv("pokemons.csv")

heavy_pokemon = df[df["Weight"] > 100]
tall_pokemon = df[df["Height"] > 2]
legends = df[df["Legendary"] == True]
water_pokemon = df[(df["Type1"] == "Water") | (df["Type2"] == "Water")]


print(water_pokemon)